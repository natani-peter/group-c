from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text, Column, Integer
from typing import List


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = 'authors'
    id: Mapped[int] = mapped_column(primary_key=True)
    f_name: Mapped[str] = mapped_column(nullable=False)
    l_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    nationality: Mapped[str] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column(nullable=False)
    birth_day: Mapped[str] = mapped_column(Text, nullable=False)
    death_day: Mapped[str] = mapped_column(Text, nullable=True)
    books: Mapped[List["Book"]] = relationship(back_populates='authors')

    def __repr__(self) -> str:
        return f"{self.f_name} {self.l_name}"

    def __len__(self):
        return len(f"{self.f_name} {self.l_name}")


class Book(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"), nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    genre: Mapped[str] = mapped_column(Text, nullable=False)
    publication_year: Mapped[str] = mapped_column(Text, nullable=False)
    state = Column(Integer, default=1)
    authors: Mapped[List["Author"]] = relationship(back_populates='books')
    copies: Mapped[List['BookCopy']] = relationship(back_populates='original')

    def __repr__(self):
        return f"{self.title} by {self.authors}"

    def __lt__(self, other):
        return self.title < other.title


class Publisher(Base):
    __tablename__ = 'publishers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    address: Mapped[str] = mapped_column(nullable=False)
    website: Mapped[str] = mapped_column(nullable=False)
    books: Mapped[List['BookCopy']] = relationship(back_populates='publishers')


class BookCopy(Base):
    __tablename__ = 'BookCopy'
    id: Mapped[int] = mapped_column(primary_key=True)
    book: Mapped[int] = mapped_column(ForeignKey("books.id"), nullable=False)
    publisher: Mapped[int] = mapped_column(ForeignKey("publishers.id"), nullable=False)
    ISBN: Mapped[str] = mapped_column(nullable=False, unique=True)
    original: Mapped["Book"] = relationship(back_populates='copies')
    publishers: Mapped['Publisher'] = relationship(back_populates='books')

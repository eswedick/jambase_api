from dataclasses import dataclass


@dataclass
class Pagination:
    page: int
    perPage: int
    totalItems: int
    totalPages: int
    nextPage: str
    previousPage: str

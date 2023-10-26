from dataclasses import dataclass


@dataclass
class Error:
    errorCode: str
    errorMessage: str

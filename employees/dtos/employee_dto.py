from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class EmployeeDTO:
    username: str
    password: str
    id_number: str
    first_name: str
    last_name: str
    position: str
    department: str


@dataclass(frozen=True)
class UpdateEmployeeDTO:
    id_number: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    position: Optional[str] = None
    department: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None

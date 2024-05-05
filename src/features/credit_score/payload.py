from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field


class Gender(str, Enum):
    male = "male"
    female = "female"


class Education(str, Enum):
    high_school = "high school"
    university = "university"
    none = "none"


class Income(str, Enum):
    working_class = "working class"
    poverty = "poverty"
    middle_class = "middle class"
    upper_class = "upper class"


class VehicleType(str, Enum):
    sports_car = "sports car"
    sedan = "sedan"


class CheckCreditScorePayload(BaseModel):
    age: int = Field(..., ge=16, le=100)
    gender: Gender
    driving_experience: int = Field(..., ge=0)
    education: Education
    income: Income
    vehicle_year: int = Field(..., ge=1990, le=datetime.now().year)
    vehicle_type: VehicleType
    annual_mileage: int = Field(..., ge=0)

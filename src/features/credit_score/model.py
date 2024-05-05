import math
from pydantic import BaseModel, field_validator
from src.core.util import populate_pydantic_base_model_from_dict


class CarInsuranceClaimModel(BaseModel):
    id: int
    age: str
    gender: str
    race: str
    driving_experience: str
    education: str
    income: str
    credit_score: float | None
    vehicle_ownership: float
    vehicle_year: str
    married: float
    children: float
    postal_code: str
    annual_mileage: float | None
    vehicle_type: str
    speeding_violations: int
    duis: int
    past_accidents: int
    outcome: float

    @field_validator("postal_code", mode="before")
    def convert_to_str(cls, v):
        return str(v)

    @field_validator("annual_mileage", "credit_score", mode="before")
    def check_nan(cls, v):
        return v if not math.isnan(v) else None

    @staticmethod
    def from_dict(dict_value, upper_keys=False):
        return populate_pydantic_base_model_from_dict(CarInsuranceClaimModel, dict_value, upper_keys=upper_keys)

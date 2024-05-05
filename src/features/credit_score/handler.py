from fastapi import APIRouter, HTTPException
from src.features.credit_score import data
from src.features.credit_score.util import check_age, check_driving_experience, check_vehicle_year
from src.features.credit_score.payload import CheckCreditScorePayload

router_v1 = APIRouter(prefix="/v1/credit-score")


@router_v1.post("")
def check_credit_score(payload: CheckCreditScorePayload):
    car_insurances = data.get_data()

    # Filtering by age
    car_insurances = [ci for ci in car_insurances if check_age(ci.age, payload.age)]

    # Filtering by gender
    car_insurances = [ci for ci in car_insurances if ci.gender == payload.gender]

    # Filtering by driving experience
    car_insurances = [
        ci for ci in car_insurances if check_driving_experience(ci.driving_experience, payload.driving_experience)
    ]

    # Filtering by education
    car_insurances = [ci for ci in car_insurances if ci.education == payload.education]

    # Filtering by income
    car_insurances = [ci for ci in car_insurances if ci.income == payload.income]

    # Filtering by vehicle year
    car_insurances = [ci for ci in car_insurances if check_vehicle_year(ci.vehicle_year, payload.vehicle_year)]

    # Filtering by vehicle type
    car_insurances = [ci for ci in car_insurances if ci.vehicle_type == payload.vehicle_type]

    # Filtering by vehicle annual mileage
    car_insurances = [
        ci for ci in car_insurances if ci.annual_mileage is not None and payload.annual_mileage <= ci.annual_mileage
    ]

    if len(car_insurances) == 0:
        raise HTTPException(status_code=400, detail="No scores found")

    return {"score": sorted(car_insurances, key=lambda x: x.annual_mileage)[0].credit_score}

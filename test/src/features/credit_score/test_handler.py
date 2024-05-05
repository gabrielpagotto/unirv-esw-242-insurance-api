from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_check_credit_score():
    data = {
        "age": 23,
        "gender": "male",
        "driving_experience": 5,
        "education": "high school",
        "income": "upper class",
        "vehicle_year": 2019,
        "vehicle_type": "sedan",
        "annual_mileage": 15000,
    }
    response = client.post("/v1/credit-score", json=data)
    assert response.status_code == 200

    data = response.json()

    assert data["score"] == 0.5764579008950959

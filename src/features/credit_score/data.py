import pandas as pd
from typing import List
from src.features.credit_score.model import CarInsuranceClaimModel


def get_data() -> List[CarInsuranceClaimModel]:
    df = pd.read_csv("dataset/Car_Insurance_Claim.csv")
    return [CarInsuranceClaimModel.from_dict(row, True) for _, row in df.iterrows()]

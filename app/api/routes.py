from fastapi import APIRouter
from app.models.company import Company
from app.models.company import CompanyScore
from app.services.scoring_service import calculate_company_score


router = APIRouter()

@router.post('/companies/evaluate', response_model=CompanyScore)
def evaluate_company(company: Company) -> CompanyScore:
    return calculate_company_score(company)
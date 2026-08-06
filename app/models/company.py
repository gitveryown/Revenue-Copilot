from pydantic import BaseModel

class Company(BaseModel):
    name: str
    industry: str
    annual_revenue: int
    headquarters: str
    city: str
    state: str
    has_existing_nba_partnership: bool
    
    

class CompanyScore(BaseModel):
    company:Company
    partnership_score: int
    recommendation: str
    reasoning: list[str]
    
    
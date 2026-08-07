from app.models.company import Company
from app.services.scoring_service import calculate_company_score


def test_target_score(): 
    target = Company(
        name="Target", industry="Retail/Merchadise", 
        annual_revenue=1500000000, 
        headquarters="Seattle",             
        city="Seattle",  state="Washington", 
        has_existing_nba_partnership= False
    )
    
    result = calculate_company_score(target)
    assert result.partnership_score == 25
    
    
    
def test_apple_score():
    apple = Company(
        name="Apple", industry="Technology", 
        annual_revenue=25000000000, 
        headquarters="Silicon Valley",             
        city="Cupertino",  state="California", 
        has_existing_nba_partnership= True
    )  
    
    result = calculate_company_score(apple)
    assert result.partnership_score == 20
    assert result.recommendation == "Low Priority"
from app.models.company import Company
from app.models.company import CompanyScore

def calculate_company_score(company: Company) -> CompanyScore:
    partnership_score = 0
    reasoning: list[str] = []
    recommendation = 'Pending'

    if company.industry.lower() == 'technology':
         partnership_score += 25
         reasoning.append('Technology companies typically have strong marketing budgets and align well with innovation-focused sponsorship initiatives.')
         
    
    if company.annual_revenue >= 1000000000:
        partnership_score += 25
        reasoning.append('A company that generates a billion or more in revenue indicates a strong financial sponsorship')
        
    elif company.annual_revenue >= 500000000:
        partnership_score += 15
        reasoning.append('The company demonstrates strong financial growth and has the potential to support meaningful sponsorship investments.')
        
    if company.city.lower() == 'atlanta':
        partnership_score += 10
        reasoning.append('A local company partnership plays a positive role in the community.')
        
    if company.has_existing_nba_partnership  == True:
        partnership_score -= 30
        reasoning.append('Company already has an existing NBA partnership, reducing the likelihood of securing a new sponsorship opportunity.')
    else:
        company.has_existing_nba_partnership ==  False
    
    if partnership_score >= 75:
       recommendation = 'High Priority'
    elif partnership_score >= 40:
       recommendation = 'Medium Priority'
    else :
       recommendation = 'Low Priority'
    
    return CompanyScore(
        company = company,
        partnership_score = partnership_score,
        recommendation = recommendation,
        reasoning = reasoning
    )
    
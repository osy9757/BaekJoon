def solution(today, terms, privacies):
    terms_dict = {term.split()[0]: int(term.split()[1]) for term in terms}    
    today_year, today_month, today_day = map(int, today.split('.'))    
    discard_indices = []
    
    for idx, privacy in enumerate(privacies):
        collection_date, term_type = privacy.split()
        year, month, day = map(int, collection_date.split('.'))        
        month += terms_dict[term_type]
        while month > 12:
            year += 1
            month -= 12
        
        if year < today_year or (year == today_year and month < today_month) or (year == today_year and month == today_month and day <= today_day):
            discard_indices.append(idx + 1)  
    
    return discard_indices
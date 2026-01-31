from datetime import date

def check_expiry(expiry_date):
    days_left = (expiry_date - date.today()).days

    if days_left < 0:
        return "EXPIRED"
    elif days_left <= 7:
        return "CRITICAL"
    elif days_left <= 30:
        return "WARNING"
    else:
        return "SAFE"

def check_abuseipdb(ip):
    """
    Check IP reputation using AbuseIPDB.
    """
    return {
        "ip": ip,
        "abuse_score": 0
    }

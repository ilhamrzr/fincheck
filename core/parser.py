def parse_ewallet_response(resp):
    if resp.get("status") != "success":
        return None, resp.get("message", "Unknown error")

    d = resp.get("data", {})
    return {
        "name": d.get("customer_name"),
        "wallet": d.get("ewallet_name"),
        "phone": d.get("phone_number"),
    }, None


def parse_bank_response(resp):
    if resp.get("status") != "success":
        return None, resp.get("message", "Unknown error")

    d = resp.get("data", {})
    return {
        "name": d.get("account_name") or d.get("customer_name"),
        "bank": d.get("bank_name"),
        "account": d.get("account_number"),
    }, None

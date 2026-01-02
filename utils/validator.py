def normalize_input(v):
    return v.strip().lower().replace(" ", "").replace("-", "")


def find_by_key(data, user_input):
    key = normalize_input(user_input)
    return data.get(key)

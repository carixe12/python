def find_key(data, key, max_depth=None, current_depth=0):
    if max_depth is not None and current_depth > max_depth:
        return None

    if key in data:
        return data[key]

    for k, v in data.items():
        if isinstance(v, dict):
            result = find_key(v, key, max_depth, current_depth + 1)
            if result is not None:
                return result

    return None


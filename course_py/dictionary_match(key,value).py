def index(keys, values, match):
    return {k: [v for v in values if match(k, v)] for k in keys}

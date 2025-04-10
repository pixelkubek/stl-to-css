def wrap_html(type: str, body: str = "", attributes: dict = dict()) -> str:
    attributes_list = []
    for key, val in attributes.items():
        attributes_list.append(f"{key}=\"{val}\"")
    return f"<{type} {" ".join(attributes_list)}>{body}</{type}>"
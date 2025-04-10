def wrap_http(body: str = "", type: str = "div", **kwargs) -> str:
    attributes = []
    for key, val in kwargs:
        attributes.append(f"{key}=\"{val}\"")
    return f"<div {" ".join(attributes)}>{body}</div>"
from triangle3d import triangle_3d, get_xyz

def wrap_html(type: str, body: str = "", attributes: dict = dict()) -> str:
    attributes_list = []
    for key, val in attributes.items():
        attributes_list.append(f"{key}=\"{val}\"")
    return f"<{type} {" ".join(attributes_list)}>{body}</{type}>"

def html_css_of_triangle(triangle: triangle_3d, html_class: str, size, unit: str = 'px') -> tuple[str, str]:
        p1, p2, p3 = triangle.vertices
        p2_x, p2_y, p2_z = get_xyz(p2)
        p3_x, p3_y, p3_z = get_xyz(p3)
        polygon = f'<polygon points="0,0 {p2_x},{p2_z} {p3_x},{p3_z} class="{html_class} object3d-element"/>'
        svg = wrap_html("svg", polygon, {"class":f'{html_class} object3d-element'})
        return svg
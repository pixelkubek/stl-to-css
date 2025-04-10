from triangle3d import triangle_3d, get_xyz

def wrap_html(type: str, body: str = "", attributes: dict = dict()) -> str:
    attributes_list = []
    for key, val in attributes.items():
        attributes_list.append(f"{key}=\"{val}\"")
    return f"<{type} {" ".join(attributes_list)}>{body}</{type}>"

def html_css_of_triangle(triangle: triangle_3d, html_class: str, size, unit: str = 'px') -> tuple[str, str]:
        _, p2, p3 = triangle.vertices
        p2_x, _, p2_z = get_xyz(p2)
        p3_x, _, p3_z = get_xyz(p3)
        polygon = f'<polygon points="0,0 {p3_x:.10f},{p3_z:.10f} {p2_x:.10f},{p2_z:.10f}" class="{html_class} object3d-element"/>'
        svg = wrap_html("svg", polygon, {"class":f'{html_class} object3d-element', 'viewBox': "0 0 100 100"})

        svg_css = f'''svg.{html_class} {{
    fill: red;
    stroke: black;
}}'''
        

        html = svg
        css = '\n'.join([svg_css])
        return html, css
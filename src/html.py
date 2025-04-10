from triangle3d import triangle_3d, get_xyz
from transformations import transformation_3d

def wrap_html(type: str, body: str = "", attributes: dict = dict()) -> str:
    attributes_list = []
    for key, val in attributes.items():
        attributes_list.append(f"{key}=\"{val}\"")
    return f"<{type} {" ".join(attributes_list)}>{body}</{type}>"

def html_css_of_triangle(triangle: triangle_3d, transforms: list[transformation_3d], html_class: str, size, unit: str = 'px') -> tuple[str, str]:
        _, p2, p3 = triangle.vertices
        p2_x, _, p2_z = get_xyz(p2)
        p3_x, _, p3_z = get_xyz(p3)


        # add polygon tag
        html = f'<polygon points="0,0 {p3_x:.10f},{p3_z:.10f} {p2_x:.10f},{p2_z:.10f}" class="{html_class} object3d-element"/>'

        # add svg tag
        html = wrap_html("svg", html, {"class":f'{html_class} object3d-element', 'viewBox': "0 0 100 100"})
        svg_css = f'svg.{html_class} {{fill: red;stroke: black;}}'
        css = [svg_css]

        counter = 0
        transforms = [transformation.inverted() for transformation in reversed(transforms)]
        for transformation in transforms:
            html = wrap_html("div", html, {"class":f'{html_class} object3d-element transformation-wrapper transformation-{counter}-wrapper'})
            transformation_css = transformation.to_css()
            css.append(f'div.{html_class}.transformation-{counter}-wrapper {transformation_css}')
            counter += 1

        return html, '\n'.join(css)
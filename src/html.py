from triangle3d import triangle_3d, get_xyz
from transformations import transformation_3d
from object3d import object_3d

def wrap_html(type: str, body: str = "", attributes: dict = dict()) -> str:
    attributes_list = []
    for key, val in attributes.items():
        attributes_list.append(f"{key}=\"{val}\"")
    return f"<{type} {" ".join(attributes_list)}>{body}</{type}>"

def html_css_of_triangle(triangle: triangle_3d, transforms: list[transformation_3d], html_class: str, scale = 1, unit: str = 'px') -> tuple[str, str]:
        _, p2, p3 = triangle.vertices
        p2_x, _, p2_z = get_xyz(p2)
        p3_x, _, p3_z = get_xyz(p3)


        # add polygon tag
        html = f'<polygon points="0,0 {p3_x:.10f},{p3_z:.10f} {p2_x:.10f},{p2_z:.10f}" class="{html_class} object3d-element"/>'

        # add svg tag
        html = wrap_html("svg", html, {"class":f'{html_class} object3d-element', 'viewBox': "0 0 100 100"})
        svg_css = f'svg.{html_class} {{fill: red;stroke: black;height: 500px;width: 500px}}' # todo parametrize
        css = [svg_css]

        counter = 0
        transforms = [transformation.inverted() for transformation in reversed(transforms)]
        for transformation in transforms:
            html = wrap_html("div", html, {"class":f'{html_class} object3d-element preserve-3d-wrapper transformation-{counter}-wrapper'})
            transformation_css = transformation.to_css(scale, unit)
            css.append(f'div.{html_class}.transformation-{counter}-wrapper {transformation_css}')
            counter += 1

        return html, '\n'.join(css)

def html_css_of_object3d(object: object_3d, html_class: str, scale = 1, unit: str = 'px') -> tuple[str, str]:
    html = []
    css = []

    counter=0
    for triangle, transformations in object.transformed_faces():
        triangle_html, triangle_css = html_css_of_triangle(triangle, transformations, f"{html_class}-face{counter}", scale, unit)
        html.append(
            wrap_html('div', triangle_html, {"class":f'{html_class}-face{counter} object3d-element preserve-3d-wrapper position-absolute-wrapper'})
        )
        css.append(triangle_css)
        css.append(
            f'div.{html_class}-face{counter}.position-absolute-wrapper {{position: absolute;}}'
        )
        counter += 1

    html = wrap_html('div', ''.join(html), {"class":f'{html_class} object3d-element preserve-3d-wrapper'})

    return html, '\n'.join(css)
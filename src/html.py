from triangle3d import triangle_3d, get_xyz
from transformations import transformation_3d, translate_3d
from object3d import object_3d

import numpy as np

# Wrap text in a pair of html brackets.
# <type x.key="x.value" for x in attributes>body</type>
def wrap_html(type: str, body: str = "", attributes: dict = dict()) -> str:
    attributes_list = []
    for key, val in attributes.items():
        attributes_list.append(f"{key}=\"{val}\"")
    return f"<{type} {" ".join(attributes_list)}>{body}</{type}>"

# Return a html div and the appropriate css for a triangle after applying transforms.
def html_css_of_triangle(triangle: triangle_3d, transforms: list[transformation_3d], html_class: str, size, unit: str = 'px', svg_pixel_scale: int = 1) -> tuple[str, str]:
        _, p2, p3 = triangle.vertices
        p2_x, _, p2_z = get_xyz(p2)
        p3_x, _, p3_z = get_xyz(p3)

        # Add polygon tag.
        html = f'<polygon points="0,0 {svg_pixel_scale * p3_x:.10f},{svg_pixel_scale * p3_z:.10f} {svg_pixel_scale * p2_x:.10f},{svg_pixel_scale * p2_z:.10f}" class="{html_class} object3d-element {' '.join(triangle.classes)}"/>'

        # Add svg tag.
        html = wrap_html("svg", html, {"class":f'{html_class} object3d-element', 'viewBox': f"0 0 {svg_pixel_scale * size} {svg_pixel_scale * size}"})
        css = []

        counter = 0
        transforms = [transformation.inverted() for transformation in reversed(transforms)]
        for transformation in transforms:
            html = wrap_html("div", html, {"class":f'{html_class} object3d-element preserve-3d-wrapper transformation-{counter}-wrapper transform-origin-top-left'})
            transformation_css = transformation.to_css(unit)
            css.append(f'div.{html_class}.transformation-{counter}-wrapper {{{transformation_css}}}')
            counter += 1

        return html, '\n'.join(css)

# Return a html div and the appropriate css for a 3d object.
def html_css_of_object3d(object: object_3d, size, unit: str = 'px', svg_pixel_scale: int = 1, color='red') -> tuple[str, str]:
    center_point_vector = object.center()
    html_class = object.name
    html = []
    css = []

    counter=0
    for triangle, transformations in object.transformed_faces():
        triangle_html, triangle_css = html_css_of_triangle(triangle, transformations, f"{html_class}-face{counter}", size, unit, svg_pixel_scale)
        html.append(
            wrap_html('div', triangle_html, {"class":f'{html_class}-face{counter} object3d-element preserve-3d-wrapper position-absolute-wrapper'})
        )
        css.append(triangle_css)
        counter += 1

    html = wrap_html('div', ''.join(html), {"class":f'{html_class} object3d-element preserve-3d-wrapper center-wrapper'})

    center_0_0_vector = np.array([size / 2, 0, size / 2]).reshape(-1, 1)

    centering_vector = center_0_0_vector - center_point_vector

    css.append(f'div.{html_class}.center-wrapper {{{translate_3d(*get_xyz(centering_vector.ravel())).to_css(unit)}}}')

    html = wrap_html('div', html, {"class":f'{html_class}-base {html_class} object3d-element preserve-3d-wrapper', 'id':html_class})
    css.append(f'.{html_class}-base {{width:{size}{unit};height:{size}{unit};transform-style: preserve-3d;}}')

    css.append(f'.{html_class}-base .preserve-3d-wrapper {{transform-style: preserve-3d;}}')
    css.append(f'.{html_class}-base .transform-origin-top-left {{transform-origin: top left;}}')
    css.append(f'.{html_class}-base .position-absolute-wrapper {{position: absolute;}}')
    css.append(f'.{html_class}-base svg {{fill: {color};stroke: black;height: {size}{unit};width: {size}{unit};opacity: 50%;}}')

    html = wrap_html('div', html, {"class":f'{html_class}-outer-wrapper {html_class} object3d-element'})
    css.append(f'.{html_class}-outer-wrapper {{overflow:hidden}}')

    return html, '\n'.join(css)
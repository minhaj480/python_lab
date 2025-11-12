from graphics.rectangle import area as rect_area, perimeter as rect_perimeter
from graphics.circle import area as circ_area, perimeter as circ_perimeter
from graphics.threeDgraphics.cuboid import area as cub_area, perimeter as cub_peri
from graphics.threeDgraphics.sphere import area as sph_area, perimeter as sph_peri

print("Rectangle:", rect_area(10, 5), rect_perimeter(10, 5))
print("Circle:", circ_area(7), circ_perimeter(7))
print("Cuboid:", cub_area(2, 3, 4), cub_peri(2, 3, 4))
print("Sphere:", sph_area(3), sph_peri(3))

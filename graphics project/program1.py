import graphics.rectangle
import graphics.circle
import graphics.threeDgraphics.cuboid
import graphics.threeDgraphics.sphere

print("Rectangle area:", graphics.rectangle.area(5, 3))
print("Rectangle perimeter:", graphics.rectangle.perimeter(5, 3))

print("Circle area:", graphics.circle.area(7))
print("Circle perimeter:", graphics.circle.perimeter(7))

print("Cuboid area:", graphics.threeDgraphics.cuboid.area(5, 3, 2))
print("Cuboid perimeter:", graphics.threeDgraphics.cuboid.perimeter(5, 3, 2))

print("Sphere area:", graphics.threeDgraphics.sphere.area(4))
print("Sphere perimeter:", graphics.threeDgraphics.sphere.perimeter(4))

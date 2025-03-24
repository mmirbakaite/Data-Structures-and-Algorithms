from add import *
import random
import math
import trimesh
import numpy as np
from pywavefront import Wavefront

def circle_on_cylinder(radius, color):
 # Calculate the number of circles and their positions
    num_circles = 1000  # Adjust the number of circles as desired
    for _ in range(num_circles):
        u = random.random() * 2 * math.pi
        v = random.random() * cylinder_top_radius - 0.01
        x = v * math.cos(u)
        y = v * math.sin(u)
        z = cylinder_start[2] + cylinder_top_thickness / 2
        start_point = (x, y, z)
        end_point = (x, y, z - 1)  # Offset the end point slightly to avoid division by zero error
        circle(start_point, end_point, radius,  circle_detail, color)

# Define the dimensions and positions of the table components
table_width = 2.0
table_length = 4.0
table_height = 0.8
leg_thickness = 0.1
leg_height = table_height - leg_thickness
table_top_thickness = 0.05

# Define the border thickness
border_thickness = 0.05

# Create the table legs
leg1_center = (table_length / 4, table_width / 4, leg_height / 2)
leg2_center = (table_length / 4, -table_width / 4, leg_height / 2)
leg3_center = (-table_length / 4, table_width / 4, leg_height / 2)
leg4_center = (-table_length / 4, -table_width / 4, leg_height / 2)

leg_width = leg_thickness
leg_length = table_top_thickness + border_thickness

surface_color = (154, 113, 67)
surf_color = (140, 90, 50)
leg_color = (112, 83, 50)

rectangle3D(leg1_center, (leg_length, leg_width, leg_height), leg_color)
rectangle3D(leg2_center, (leg_length, leg_width, leg_height), leg_color)
rectangle3D(leg3_center, (leg_length, leg_width, leg_height), leg_color)
rectangle3D(leg4_center, (leg_length, leg_width, leg_height), leg_color)

# Create the table top
table_top_center = (0, 0, table_height - table_top_thickness / 2)
rectangle3D(table_top_center, (table_length, table_width, table_top_thickness), surface_color)

# Create the table border
table_border_center = (0, 0, table_height - table_top_thickness - border_thickness / 2)
rectangle3D(table_border_center, (table_length, table_width, border_thickness), surf_color)

# Create the thin cylinder on the table surface
cylinder_start = (0, 0, table_height - table_top_thickness / 2)
cylinder_end = (0, 0, table_height + table_top_thickness / 2)
cylinder_radius = min(table_length, table_width) / 4
cylinder_detail = 20
cylinder_color = (160, 186, 179)  # Red color (RGB)
cylinder(cylinder_start, cylinder_end, cylinder_radius, cylinder_detail, cylinder_color)

# Calculate the number of circles and their positions
circle_radius = 0.009  # Adjust the circle radius as desired
circle_color = (89, 49, 110)  # Blue color (RGB)
circle_detail = 30  # Adjust the circle detail as desired
cylinder_top_thickness = table_top_thickness + 0.07
cylinder_top_radius = cylinder_radius - circle_radius
circle_on_cylinder(circle_radius, circle_color)


# Calculate the dimensions of the transparent cylinder
transparent_cylinder_start = (0, 0, table_height + table_top_thickness + cylinder_top_thickness - 0.26 / 2)
transparent_cylinder_end = (0, 0, table_height + table_top_thickness / 2 + 0.3)  # Adjust the height of the tall cylinder as desired
transparent_cylinder_radius_outer = cylinder_radius / 2  # Adjust the outer radius of the tall cylinder as desired
transparent_cylinder_radius_inner = transparent_cylinder_radius_outer - 0.01  # Adjust the inner radius of the tall cylinder as desired
transparent_cylinder_detail = 20
transparent_cylinder_color_outer = (178,178,255, 255)  # Transparent green color (RGB with alpha value)
# Create the outer surface of the transparent cylinder
cylinder(transparent_cylinder_start, transparent_cylinder_end, transparent_cylinder_radius_outer, transparent_cylinder_detail, transparent_cylinder_color_outer)

# Calculate the height of the boat-like shape to match the green cylinder
boat_height1 = transparent_cylinder_end[2] - transparent_cylinder_start[2]
transparent_cylinder_color_inner1 = (160,196,255, 255)  # Black color for the inside of the cylinder with full opacity
# Calculate the adjusted boat_start and boat_end positions
boat_start1 = (transparent_cylinder_start[0], transparent_cylinder_start[1], transparent_cylinder_start[2] + boat_height1 * 0.1)
boat_end1 = (transparent_cylinder_start[0], transparent_cylinder_start[1], transparent_cylinder_start[2] + boat_height1 *1.1)
# Adjust the radius and detail of the boat-like shape as desired
boat_radius1 = transparent_cylinder_radius_inner * 0.86
boat_detail1 = transparent_cylinder_detail
# Create the boat-like shape inside the transparent cylinder
cylinder(boat_start1, boat_end1, boat_radius1, boat_detail1, transparent_cylinder_color_inner1)

# Calculate the height of the boat-like shape to match the green cylinder
boat_height2 = transparent_cylinder_end[2] - transparent_cylinder_start[2]
transparent_cylinder_color_inner2 = (155,246,255, 255)  # Black color for the inside of the cylinder with full opacity
# Calculate the adjusted boat_start and boat_end positions
boat_start2 = (transparent_cylinder_start[0], transparent_cylinder_start[1], transparent_cylinder_start[2] + boat_height2 * 0.2)
boat_end2 = (transparent_cylinder_start[0], transparent_cylinder_start[1], transparent_cylinder_start[2] + boat_height2 *1.2)
# Adjust the radius and detail of the boat-like shape as desired
boat_radius2 = transparent_cylinder_radius_inner * 0.72
boat_detail2 = transparent_cylinder_detail
# Create the boat-like shape inside the transparent cylinder
cylinder(boat_start2, boat_end2, boat_radius2, boat_detail2, transparent_cylinder_color_inner2)

# Calculate the height of the boat-like shape to match the green cylinder
boat_height3 = transparent_cylinder_end[2] - transparent_cylinder_start[2]
transparent_cylinder_color_inner3 = (202,255,191, 255)  # Black color for the inside of the cylinder with full opacity
# Calculate the adjusted boat_start and boat_end positions
boat_start3 = (transparent_cylinder_start[0], transparent_cylinder_start[1], transparent_cylinder_start[2] + boat_height3 * 0.3)
boat_end3 = (transparent_cylinder_start[0], transparent_cylinder_start[1], transparent_cylinder_start[2] + boat_height3 *1.3)
# Adjust the radius and detail of the boat-like shape as desired
boat_radius3 = transparent_cylinder_radius_inner * 0.58
boat_detail3 = transparent_cylinder_detail
# Create the boat-like shape inside the transparent cylinder
cylinder(boat_start3, boat_end3, boat_radius3, boat_detail3, transparent_cylinder_color_inner3)

# Calculate the height of the boat-like shape to match the green cylinder
boat_height4 = transparent_cylinder_end[2] - transparent_cylinder_start[2]
transparent_cylinder_color_inner4 = (253,255,182, 255)  # Black color for the inside of the cylinder with full opacity
# Calculate the adjusted boat_start and boat_end positions
boat_start4 = (transparent_cylinder_start[0], transparent_cylinder_start[1], transparent_cylinder_start[2] + boat_height4 * 0.4)
boat_end4 = (transparent_cylinder_start[0], transparent_cylinder_start[1], transparent_cylinder_start[2] + boat_height4 *1.5)
# Adjust the radius and detail of the boat-like shape as desired
boat_radius4 = transparent_cylinder_radius_inner * 0.44
boat_detail4 = transparent_cylinder_detail
# Create the boat-like shape inside the transparent cylinder
cylinder(boat_start4, boat_end4, boat_radius4, boat_detail4, transparent_cylinder_color_inner4)

# Calculate the height of the boat-like shape to match the green cylinder
boat_height5 = transparent_cylinder_end[2] - transparent_cylinder_start[2]
transparent_cylinder_color_inner5 = (255,214,165, 255)  # Black color for the inside of the cylinder with full opacity
# Calculate the adjusted boat_start and boat_end positions
boat_start5 = (transparent_cylinder_start[0], transparent_cylinder_start[1], transparent_cylinder_start[2] + boat_height5 * 0.5)
boat_end5 = (transparent_cylinder_start[0], transparent_cylinder_start[1], transparent_cylinder_start[2] + boat_height5 *1.8)
# Adjust the radius and detail of the boat-like shape as desired
boat_radius5 = transparent_cylinder_radius_inner * 0.3
boat_detail5 = transparent_cylinder_detail
# Create the boat-like shape inside the transparent cylinder
cylinder(boat_start5, boat_end5, boat_radius5, boat_detail5, transparent_cylinder_color_inner5)

# Calculate the height of the boat-like shape to match the green cylinder
boat_height6 = transparent_cylinder_end[2] - transparent_cylinder_start[2]
transparent_cylinder_color_inner6 = (255,173,173, 255)  # Black color for the inside of the cylinder with full opacity
# Calculate the adjusted boat_start and boat_end positions
boat_start6 = (transparent_cylinder_start[0], transparent_cylinder_start[1], transparent_cylinder_start[2] + boat_height6 * 0.6)
boat_end6 = (transparent_cylinder_start[0], transparent_cylinder_start[1], transparent_cylinder_start[2] + boat_height6 *2)
# Adjust the radius and detail of the boat-like shape as desired
boat_radius6 = transparent_cylinder_radius_inner * 0.1
boat_detail6 = transparent_cylinder_detail
# Create the boat-like shape inside the transparent cylinder
cylinder(boat_start6, boat_end6, boat_radius6, boat_detail6, transparent_cylinder_color_inner6)

# Save the dining table mesh as an OFF file
mesh_file = 'dining_table.off'

off(mesh_file)
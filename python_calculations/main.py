g_ratio = 5
sun_teeth = 12
module = 1.5

n2_n1 = g_ratio/2 -1

planet_teeth = n2_n1 * sun_teeth

print(planet_teeth)

sun_ref_diam = sun_teeth * module
planet_ref_diam = planet_teeth * module

ring_ref_radius = sun_ref_diam/2 + planet_ref_diam
ring_ref_diam = 2 * ring_ref_radius

ring_teeth = ring_ref_diam / module

print(f"Module: {module}")

print("\nSun gear:")
print(f"Teeth:{sun_teeth}")
print(f"Reference diameter: {sun_ref_diam}")

print("\nPlanet gears:")
print(f"Teeth:{planet_teeth}")
print(f"Reference diameter: {planet_ref_diam}")

print("\nRing gears:")
print(f"Teeth:{ring_teeth}")
print(f"Reference diameter: {ring_ref_diam}\n")

sun_planet_center_dist = sun_ref_diam/2 + planet_ref_diam/2
print(f"Sun-planet center distance: {sun_planet_center_dist}")
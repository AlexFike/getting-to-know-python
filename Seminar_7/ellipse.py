def find_farthest_orbit(orb):
    return max(filter(lambda x: x[0] != x[1], orb), key=lambda x: x[0]*x[1])


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

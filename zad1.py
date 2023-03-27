from math import ceil


def how_many_boxes(floor_length, floor_width, tile_length, tile_width, box_capacity):
    floor = floor_length * floor_width
    floor = floor + floor * 0.1
    tile = tile_length * tile_width
    req_tiles = floor / tile
    return ceil(req_tiles / box_capacity)


print("Potrzeba: " + str(how_many_boxes(4, 4, 0.2, 1, 10)))

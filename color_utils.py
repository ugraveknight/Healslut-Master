def get_closest_color(colors, color, max_difference = None):
    search_r, search_g, search_b = color
    best_color_difference = None
    best_color = None
    for check_color in colors:
        ref_r, ref_g, ref_b = check_color
        difference = abs(ref_r - search_r) + abs(ref_g - search_g) + abs(ref_b - search_b)
        if (max_difference is None or difference <= max_difference) and (best_color_difference is None or best_color_difference > difference):
            best_color_difference = difference
            best_color = check_color

    if best_color is not None:
        return best_color
    
    raise Exception('No close color found', color)
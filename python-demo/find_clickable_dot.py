def find_will_click_dot(left_pos, right_pos, top_pos, letter_dots):
    DOT_RANGE = 10
    smallest_y_dot = None
    validated_letter_dots = []
    # filter dots between left_pos and right_pos letter_dots
    for letter_dot in letter_dots:
        if left_pos <= letter_dot[0] <= right_pos:
            validated_letter_dots.append(letter_dot)
    del letter_dots
    # filter dots between top_pos and top_pos + DOT_RANGE
    in_range_dots = []
    for validated_letter_dot in validated_letter_dots:
        if top_pos <= validated_letter_dot[1] <= top_pos + DOT_RANGE:
            in_range_dots.append(validated_letter_dot)
    del validated_letter_dots
    # find the smallest y dot
    for in_range_dot in in_range_dots:
        if smallest_y_dot == None or in_range_dot[1] < smallest_y_dot[1]:
            smallest_y_dot = in_range_dot

    return smallest_y_dot

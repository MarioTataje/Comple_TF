
def get_side_length():
    return 40;

def get_screen_dimensions():
    side_length = get_side_length();
    height = 18 * side_length;
    width = 32 * side_length;
    return dict(width= width, height = height);
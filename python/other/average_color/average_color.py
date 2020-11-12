
def find_average_color(hex_color_1: str, hex_color_2: str) -> str:
    rgb_color_1 = convert_hex_to_rgb_color(hex_color_1)
    rgb_color_2 = convert_hex_to_rgb_color(hex_color_2)

    average_rgb_color = []
    for i in range(len(rgb_color_1)):
        color_avg = (rgb_color_1[i] + rgb_color_2[i]) // 2
        average_rgb_color.append(color_avg)

    return convert_rgb_to_hex_color(tuple(average_rgb_color))

def convert_hex_to_rgb_color(hex_color: str) -> tuple:
    rgb_color = []
    for i in [0, 2, 4]:
        rgb_color.append(int(hex_color[i:i + 2], 16))

    return tuple(rgb_color)


def convert_rgb_to_hex_color(rgb_color: tuple) -> str:
    return '%02X%02X%02X' % rgb_color


hex_color_1 = input('Enter hex1: ').lstrip('#')
hex_color_2 = input('Enter hex2: ').lstrip('#')

print(find_average_color(hex_color_1, hex_color_2))


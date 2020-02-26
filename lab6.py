import arcade


def draw_section_outlines():
    color = arcade.color.BLACK

    # squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, color)
    arcade.draw_rectangle_outline(450, 150, 300, 300, color)
    arcade.draw_rectangle_outline(750, 150, 300, 300, color)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, color)

    # squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, color)
    arcade.draw_rectangle_outline(450, 450, 300, 300, color)
    arcade.draw_rectangle_outline(750, 450, 300, 300, color)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, color)


def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = (column * 10) + 5
 
            y = (row * 10) + 5

            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    pass


def draw_section_3():
    pass


def draw_section_4():
    pass


def draw_section_5():
    pass


def draw_section_6():
    pass


def draw_section_7():
    pass


def draw_section_8():
    pass


def main():
    # window
    arcade.open_window(1200, 600, "Lab 06 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # outlines
    draw_section_outlines()

    # sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()

if __name__=='__main__':
    main()
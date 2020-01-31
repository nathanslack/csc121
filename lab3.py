import arcade
arcade.open_window(600, 600, "A  N E W  H O P E")
arcade.set_background_color(arcade.color.LIGHT_PINK)
arcade.start_render()
# START//

# GRADIENT IN THE SKY //

arcade.draw_rectangle_filled(
    300, 410, 600, 25, arcade.color.LAVENDER_PINK
)

arcade.draw_rectangle_filled(
    300, 390, 600, 25, arcade.color.LIGHT_ORCHID
)

arcade.draw_rectangle_filled(
    300, 375, 600, 25, arcade.color.LILAC
)

arcade.draw_rectangle_filled(
    300, 340, 600, 50, arcade.color.LIGHT_MEDIUM_ORCHID
)

# DRAWING THE GROUND //

arcade.draw_rectangle_filled(
    300, 100, 600, 400, arcade.color.SAND
)

arcade.draw_ellipse_filled(
    100, 300, 600, 100, arcade.color.SAND
)

arcade.draw_ellipse_filled(
    375, 300, 600, 100, arcade.color.SAND
)

# DRAWING THE BINARY SUNSET //

arcade.draw_circle_filled(
    401, 474, 25, arcade.color.RED_ORANGE
)

arcade.draw_circle_filled(
    400, 475, 25, arcade.color.WHITE_SMOKE
)

arcade.draw_circle_filled(
    500, 400, 25, arcade.color.RED_ORANGE
)

# DRAWING THE HUT //

arcade.draw_rectangle_outline(
    260, 250, 125, 125, arcade.color.BLACK_BEAN
)

arcade.draw_circle_filled(
    100, 250, 175, arcade.color.SAND
)

arcade.draw_circle_outline(
    100, 250, 175, arcade.color.BLACK_BEAN
)

arcade.draw_circle_outline(
    115, 260, 75, arcade.color.BLACK_BEAN
)

arcade.draw_rectangle_filled(
    75, 150, 500, 225, arcade.color.SAND
)

arcade.draw_rectangle_outline(
    75, 200, 525, 125, arcade.color.BLACK_BEAN
)

# THING IN DISTANCE //

arcade.draw_rectangle_filled(
    550, 350, 10, 50, arcade.color.ONYX
)

arcade.draw_rectangle_filled(
    545, 338, 5, 25, arcade.color.ONYX
)

arcade.draw_rectangle_filled(
    556, 338, 5, 25, arcade.color.ONYX
)

arcade.draw_rectangle_filled(
    550, 375, 2, 30, arcade.color.ONYX
)

# TEXT //

arcade.draw_text(
    "A", 75, 550, arcade.color.JET
)

arcade.draw_text(
    "N E W", 62, 525, arcade.color.JET
)

arcade.draw_text(
    "H O P E", 58, 500, arcade.color.JET
)

arcade.finish_render()
arcade.run()
import arcade

def gradient_sky():
    arcade.draw_rectangle_filled(
        300, 410, 600, 25, 
        arcade.color.LAVENDER_PINK
    )

    arcade.draw_rectangle_filled(
        300, 390, 600, 25, 
        arcade.color.LIGHT_ORCHID
    )

    arcade.draw_rectangle_filled(
        300, 375, 600, 25, 
        arcade.color.LILAC
    )

    arcade.draw_rectangle_filled(
        300, 340, 600, 50, 
        arcade.color.LIGHT_MEDIUM_ORCHID
    )

def clouds(x,y):
    arcade.draw_ellipse_filled(
        x, y, 110, 30,
        arcade.color.BLUE_BELL
    )

    arcade.draw_ellipse_filled(
        x - 10, y + 10, 80, 30,
        arcade.color.BLUE_BELL
    )

    arcade.draw_ellipse_filled(
        x + 20, y + 10, 95, 40, 
        arcade.color.BLUE_BELL
    )

def ground():
    arcade.draw_rectangle_filled(
        300, 100, 600, 400, 
        arcade.color.SAND
    )

    arcade.draw_ellipse_filled(
        100, 300, 600, 100, 
        arcade.color.SAND
    )

    arcade.draw_ellipse_filled(
        375, 300, 600, 100, 
        arcade.color.SAND
    )

def binary_sunset():
    arcade.draw_circle_filled(
        401, 474, 25, 
        arcade.color.RED_ORANGE
    )

    arcade.draw_circle_filled(
        400, 475, 25, 
        arcade.color.WHITE_SMOKE
    )

    arcade.draw_circle_filled(
        500, 400, 25, 
        arcade.color.RED_ORANGE
    )

def hut():
    arcade.draw_rectangle_outline(
        260, 250, 125, 125, 
        arcade.color.BLACK_BEAN
    )

    arcade.draw_circle_filled(
        100, 250, 175, 
        arcade.color.SAND
    )

    arcade.draw_circle_outline(
        100, 250, 175, 
        arcade.color.BLACK_BEAN
    )

    arcade.draw_circle_outline(
        115, 260, 75, 
        arcade.color.BLACK_BEAN
    )

    arcade.draw_rectangle_filled(
        75, 150, 500, 225, 
        arcade.color.SAND
    )

    arcade.draw_rectangle_outline(
        75, 200, 525, 125, 
        arcade.color.BLACK_BEAN
    )

def distance_object():
    arcade.draw_rectangle_filled(
        550, 350, 10, 50, 
        arcade.color.ONYX
    )

    arcade.draw_rectangle_filled(
        545, 338, 5, 25, 
        arcade.color.ONYX
    )

    arcade.draw_rectangle_filled(
        556, 338, 5, 25, 
        arcade.color.ONYX
    )

    arcade.draw_rectangle_filled(
        550, 375, 2, 30, 
        arcade.color.ONYX
    )

def title():
    arcade.draw_text(
        "A", 75, 550, 
        arcade.color.JET
    )

    arcade.draw_text(
        "N E W", 62, 525, 
        arcade.color.JET
    )

    arcade.draw_text(
        "H O P E", 58, 500, 
        arcade.color.JET
    )

positions = {
    "x": 300,
    "y": 450
}

def on_draw(delta_time):
    arcade.start_render()
    gradient_sky()
    ground()
    binary_sunset()

    clouds(positions["x"], positions["y"])
    clouds(positions["x"] + 100, positions["y"] + 100)
    clouds(positions["x"] + 75, positions["y"] + 200)
    clouds(positions["x"] + 200, positions["y"] - 75)
    clouds(positions["x"] - 100, positions["y"] + 100)
    clouds(positions["x"] - 90, positions["y"] - 75)
    clouds(positions["x"] + 275, positions["y"] + 50)
    clouds(positions["x"] + 350, positions["y"] - 25)

    speed = -3/2
    positions["x"] += speed
    
    hut()
    distance_object()
    title()

def main():
    arcade.open_window(600, 600, "A  N E W  H O P E")
    arcade.set_background_color(arcade.color.LIGHT_PINK)

    arcade.schedule(on_draw, 1/60)
    sound = arcade.load_sound('Star Wars IV A new hope - Binary Sunset (Force Theme).mp3')
    arcade.play_sound(sound)
    arcade.run()

if __name__ == "__main__":
    main()
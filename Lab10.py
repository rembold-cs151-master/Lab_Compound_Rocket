from pgl import GWindow, GRect, GCompound, GPolygon, GState, GLabel, GOval

WIDTH = 300
HEIGHT = 600
ROCKET_WIDTH = 50
ROCKET_HEIGHT = 200
GROUND_HEIGHT = 50


def create_filled_rect(x, y, w, h, color):
    """ Creates a filled rectangle of the desired color. """
    r = GRect(x, y, w, h)
    r.set_filled(True)
    r.set_color(color)
    return r


def launch_rocket():
    """ Creates an animation of a rocket lifting off into the sky. """

    def lift():
        """ Timer callback to animate rocket liftoff. """
        gs.v -= 0.25
        rocket.move(0, gs.v)
        if rocket.get_y() < -ROCKET_HEIGHT:
            timer.stop()

    def create_rocket():
        """
        Function to create the compound rocket object. Including the core,
        1 fin on each side, and a nose cap. Should return the compound object.
        """
        rocket = GCompound()
        core = create_filled_rect(0, 0, ROCKET_WIDTH, ROCKET_HEIGHT, "oldlace")
        rocket.add(core, -ROCKET_WIDTH / 2, -ROCKET_HEIGHT)

        # Add your code below to add more pieces to the rocket!



        return rocket

    gw = GWindow(WIDTH, HEIGHT)
    gs = GState()
    gs.v = 0

    gw.add(create_filled_rect(0, 0, WIDTH, HEIGHT, "dodgerblue"))  # sky
    gw.add( create_filled_rect(0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT, "darkgreen"))  # ground

    rocket = create_rocket()
    gw.add(rocket, WIDTH / 2, HEIGHT - GROUND_HEIGHT)
    timer = gw.set_interval(lift, 30)


if __name__ == "__main__":
    launch_rocket()

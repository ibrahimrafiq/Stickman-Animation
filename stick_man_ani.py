"""
Name: Ibrahim Rafiq
Date: 1st August 2023
Purpose: This program makes a stick figure animation
        the stick figure animation consists of four
        stick figures. All four of them perform a stick
        figure dance with some ballet moves. then the middle
        two stick figures perform a fusion. The fusion was
        inspired by Dragon Ball Z the tv show. After the
        fusion the middle two stick figures transform into a
        cooler version.
        which then also performs the dance.
"""


from graphics import graphics

win = graphics(w=800, h=800, title="Stick Figure")


def create_stick_man(win, x, y):
    """
    This function makes a simple stick figure.
    Parameters: win which is the window x & y
                which are the position of the figure
                on the graphics window.
    Returns: no returns
    """
    width = 50
    height = 50

    win.ellipse(x, y, width, height, fill="grey")

    # Calculate the lower part
    lower_y = y + height / 2

    # Draw the body
    win.line(x, lower_y, x, 300)

    # Calculate the arm starting points
    arm_start_x = x + 50
    arm_start_y = y + height - 50

    # arms
    win.line(x, y + height, x + 50, y + height + 100)
    win.line(x, y + height, x - 50, y + height + 100)

    # legs
    win.line(x, 300, arm_start_x, height + 300)
    win.line(x, 300, x - 50, height + 300)


def hands_up(win, x, y):
    """
    This function makes a simple stick figure with hands up.
    Parameters: win which is the window x & y
                which are the position of the figure
                on the graphics window.
    Returns: no returns
    """
    width = 50
    height = 50

    win.ellipse(x, y, width, height, fill="grey")

    # Calculate the lower part
    lower_y = y + height / 2

    # Draw the body
    win.line(x, lower_y, x, 300)

    # Calculate the arm starting points
    arm_start_x = x + 50
    arm_start_y = y + height - 50
    # arms
    win.line(x, y + height, x + 50, y + height - 100)
    win.line(x, y + height, x - 50, y + height - 100)

    # legs
    win.line(x, 300, arm_start_x, height + 300)
    win.line(x, 300, x - 50, height + 300)


def one_hand_up1(win, x, y):
    """
    This function makes a simple stick figure
    with one hand up.
    Parameters: win which is the window x & y
                which are the position of the figure
                on the graphics window.
    Returns: no returns
    """
    width = 50
    height = 50

    win.ellipse(x, y, width, height, fill="grey")

    # Calculate the lower part
    lower_y = y + height / 2

    # Draw the body
    win.line(x, lower_y, x, 300)
    # Calculate the arm starting points
    arm_start_x = x + 50
    arm_start_y = y + height - 50
    # arms

    win.line(x, y + height, x - 50, y + height - 100)

    # legs
    win.line(x, 300, arm_start_x, height + 300)
    win.line(x, 300, x - 50, height + 300)


def one_hand_up2(win, x, y):
    """
    This function makes a simple stick figure
    with one hand up.
    Parameters: win which is the window x & y
                which are the position of the figure
                on the graphics window.
    Returns: no returns
    """
    width = 50
    height = 50

    win.ellipse(x, y, width, height, fill="grey")

    # Calculate the lower part (legs and body)
    lower_y = y + height / 2

    # Draw the body
    win.line(x, lower_y, x, 300)

    # Calculate the arm starting points
    arm_start_x = x + 50
    arm_start_y = y + height - 50

    # arms
    win.line(x, y + height, x + 50, y + height - 100)

    # legs
    win.line(x, 300, arm_start_x, height + 300)
    win.line(x, 300, x - 50, height + 300)


def slant_position_left(win, x, y):
    """
    This function makes a simple stick figure
    with slanting arms dance position.
    Parameters: win which is the window x & y
                which are the position of the figure
                on the graphics window.
    Returns: no returns
    """

    width = 50
    height = 50

    win.ellipse(x, y, width, height, fill="grey")

    # Calculate the lower part
    lower_y = y + height / 2

    # Draw the body
    win.line(x, lower_y, x, 300)

    # Calculate the arm starting points
    arm_start_x = x + 50
    arm_start_y = y + height - 50
    # arms
    win.line(x, y + height, x + 50, 100)
    win.line(x, y + height, x - 50, 200)

    # legs
    win.line(x, 300, arm_start_x, height + 300)
    win.line(x, 300, x - 50, height + 300)


def slant_position_right(win, x, y):
    """
    This function makes a simple stick figure
    with slanting arms dance position.
    Parameters: win: is the graphics window; x & y
                are the position of the figure
                on the graphics window.
    Returns: no returns
    """

    width = 50
    height = 50

    win.ellipse(x, y, width, height, fill="grey")

    # Calculate the lower part
    lower_y = y + height / 2

    # Draw the body (line)
    win.line(x, lower_y, x, 300)

    # Calculate the arm starting points
    arm_start_x = x + 50
    arm_start_y = y + height - 50

    # arms
    win.line(x, y + height, x + 50, 200)
    win.line(x, y + height, x - 50, 100)
    # legs
    win.line(x, 300, arm_start_x, height + 300)
    win.line(x, 300, x - 50, height + 300)


def legs_bend(win, x, y):
    """
    This function makes a simple stick figure
    with ballet position legs and arms up.
    Parameters: win: is the graphics window; x & y
                are the position of the figure
                on the graphics window.
    Returns: no returns
    """

    width = 50
    height = 50

    win.ellipse(x, y, width, height, fill="grey")

    # Calculate the lower part
    lower_y = y + height / 2

    # Draw the body
    win.line(x, lower_y, x, 300)

    # arm
    arm_start_x = x + 50
    arm_start_y = y + height - 50

    win.line(x, y + height, x + 50, y + height - 100)
    win.line(x, y + height, x - 50, y + height - 100)
    # draw bend legs

    # arms
    win.line(x, 300, arm_start_x, height + 300)
    win.line(x, 300, x - 50, height + 300)
    # bend the legs
    win.line(arm_start_x, height + 300, x, y + 250)
    win.line(x - 50, height + 300, x, y + 300)


def legs_bend_oneside(win, x, y):
    """
    This function makes a simple stick figure
    with ballet position legs and arms on one side.
    Parameters: win: is the graphics window; x & y
                are the position of the figure
                on the graphics window.
    Returns: no returns
    """
    width = 50
    height = 50

    win.ellipse(x, y, width, height, fill="grey")

    lower_y = y + height / 2

    # Draw the body (line)
    win.line(x, lower_y, x, 300)

    # Calculate the arm starting points
    arm_start_x = x + 50
    arm_start_y = y + height - 50
    # arms
    win.line(x, y + height, x + 50, y + height + 100)
    win.line(x, y + height, x + 50, y + height - 100)

    # legs
    win.line(x, 300, arm_start_x, height + 300)
    win.line(x, 300, x - 50, height + 300)
    # bend the legs
    win.line(arm_start_x, height + 300, x, y + 250)
    win.line(x - 50, height + 300, x, y + 300)


def hands_oneside_up(win, x, y):
    """
    This function makes a simple stick figure
    with straight legs and hands on one side.
    Parameters: win: is the graphics window; x & y
                are the position of the figure
                on the graphics window.
    Returns: no returns
    """
    width = 50
    height = 50

    win.ellipse(x, y, width, height, fill="grey")

    # Calculate the lower part
    lower_y = y + height / 2

    # Draw the body
    win.line(x, lower_y, x, 300)

    # Calculate the arm starting points
    arm_start_x = x + 50
    arm_start_y = y + height - 50

    win.line(x, y + height, x + 50, y + height + 100)
    win.line(x, y + height, x + 50, y + height - 100)

    # legs
    win.line(x, 300, arm_start_x, height + 300)
    win.line(x, 300, x - 50, height + 300)


def ballet_position_right(win, x, y):
    """
    This function makes a simple stick figure
    with ballet position with hands on the
    right side.
    Parameters: win: is the graphics window; x & y
                are the position of the figure
                on the graphics window.
    Returns: no returns
    """
    width = 50
    height = 50

    win.ellipse(x, y, width, height, fill="grey")

    # Calculate the lower part
    lower_y = y + height / 2

    # Draw the body
    win.line(x, lower_y, x, 300)

    # Calculate the arm starting points
    arm_start_x = x + 50
    arm_start_y = y + height - 50

    win.line(x, y + height, x + 50, y + height + 100)
    win.line(x, y + height, x + 50, y + height - 100)

    # legs
    win.line(x, 300, arm_start_x, height + 300)
    win.line(x, 300, x - 50, height + 300)

    win.line(arm_start_x, height + 300, x, y + 250)
    win.line(x - 50, height + 300, x, y + 300)


def ballet_position_left(win, x, y):
    """
    This function makes a simple stick figure
    with ballet position with hands on the
    leftside.
    Parameters: win: is the graphics window; x & y
                are the position of the figure
                on the graphics window.
    Returns: no returns
    """
    width = 50
    height = 50

    win.ellipse(x, y, width, height, fill="grey")

    # Calculate the lower part
    lower_y = y + height / 2

    # Draw the body
    win.line(x, lower_y, x, 300)

    # Calculate the arm starting points
    arm_start_x = x + 50
    arm_start_y = y + height - 50

    # arms
    win.line(x, y + height, x - 50, y + height - 100)
    win.line(x, y + height, x - 50, y + height + 100)

    # legs
    win.line(x, 300, arm_start_x, height + 300)
    win.line(x, 300, x - 50, height + 300)

    win.line(arm_start_x, height + 300, x, y + 250)
    win.line(x - 50, height + 300, x, y + 300)


def up_down(win, x, y):
    """
    This function makes a simple stick figure
    with one hand up and one down.
    Parameters: win: is the graphics window; x & y
                are the position of the figure
                on the graphics window.
    Returns: no returns
    """

    width = 50
    height = 50

    win.ellipse(x, y, width, height, fill="grey")

    # Calculate the lower part
    lower_y = y + height / 2

    # Draw the body
    win.line(x, lower_y, x, 300)

    # Calculate the arm starting points
    arm_start_x = x + 50
    arm_start_y = y + height - 50

    win.line(x, y + height, x + 50, y + height + 50)
    win.line(x, y + height, x - 50, y + height - 100)

    # bend the legs
    win.line(x, 300, arm_start_x, height + 300)
    win.line(x, 300, x - 50, height + 300)


def after_fusion(win, x, y):
    """
    This function  makes the cooler stick
    figure after fusion.
    Parameters: win: is the graphics window; x & y
                are the position of the figure
                on the graphics window.
    Returns: no returns
    """
    width = 50
    height = 50

    win.ellipse(x, y, width, height, fill="gold")

    lower_y = y + height / 2

    # Draw the body
    win.line(x, lower_y, x, 300, fill="orange")

    # Calculate the arm starting points
    arm_start_x = x + 50
    arm_start_y = y + height - 50

    # arms
    win.line(x, y + height, x + 50, y + height - 100, fill="blue")
    win.line(x, y + height, x - 50, y + height - 100, fill="blue")
    # legs
    win.line(x, 300, arm_start_x, height + 300, fill="blue")
    win.line(x, 300, x - 50, height + 300, fill="blue")


def after_fusion_ballet(win, x, y):
    """
    This function makes a simple stick figure
    with ballet position after fusion.
    which means it is the cooler version.
    Parameters: win: is the graphics window; x & y
                are the position of the figure
                on the graphics window.
    Returns: no returns
    """
    width = 50
    height = 50

    win.ellipse(x, y, width, height, fill="gold")

    # Calculate the lower part
    lower_y = y + height / 2

    # Draw the body
    win.line(x, lower_y, x, 300, fill="orange")
    # Calculate the arm starting points
    arm_start_x = x + 50
    arm_start_y = y + height - 50

    # arms
    win.line(x, y + height, x - 50, y + height - 100, fill="blue")
    win.line(x, y + height, x - 50, y + height + 100, fill="blue")

    # legs
    win.line(x, 300, arm_start_x, height + 300, fill="blue")
    win.line(x, 300, x - 50, height + 300, fill="blue")

    win.line(arm_start_x, height + 300, x, y + 250, fill="blue")
    win.line(x - 50, height + 300, x, y + 300, fill="blue")


def after_fusion_legs(win, x, y):
    """
    This function makes a simple stick figure
    with ballet position with both hands up.
    It is also for the cooler version.
    Parameters: win: is the graphics window; x & y
                are the position of the figure
                on the graphics window.
    Returns: no returns
    """
    width = 50
    height = 50

    win.ellipse(x, y, width, height, fill="gold")

    # Calculate the lower part
    lower_y = y + height / 2

    # Draw the body
    win.line(x, lower_y, x, 300, fill="orange")

    # Calculate the arm starting points
    arm_start_x = x + 50
    arm_start_y = y + height - 50

    win.line(x, y + height, x + 50, y + height - 100, fill="blue")
    win.line(x, y + height, x - 50, y + height - 100, fill="blue")
    # draw bend legs

    # arms
    win.line(x, 300, arm_start_x, height + 300, fill="blue")
    win.line(x, 300, x - 50, height + 300, fill="blue")

    # legs
    win.line(arm_start_x, height + 300, x, y + 250, fill="blue")
    win.line(x - 50, height + 300, x, y + 300, fill="blue")


def stick_dance():
    """
    this function uses all the other functions to make
    frames each frame represents a single image.
    when compiled together under this function they animate
    the stick figures.
    Parameters: no parameters
    Returns: no returns
    """
    while True:
        # frame1
        win.clear()
        slant_position_right(win, 100, 100)  # stick man 1
        one_hand_up2(win, 300, 100)  # stick man 2
        up_down(win, 500, 100)  # stickman 3
        create_stick_man(win, 700, 100)  # stickman 4
        win.update_frame(2)

        # frame2
        win.clear()
        legs_bend(win, 100, 100)  # stick man 1
        legs_bend_oneside(win, 300, 100)  # stick man 2
        legs_bend(win, 500, 100)  # stick man 3
        legs_bend(win, 700, 100)  # stick man 4
        win.update_frame(1)

        # frame3
        win.clear()
        one_hand_up2(win, 100, 100)  # stick man 1
        slant_position_right(win, 300, 100)  # stick man 2
        hands_oneside_up(win, 500, 100)  # stickman 3
        create_stick_man(win, 700, 100)  # stickman 4
        win.update_frame(1)

        # frame4
        win.clear()
        ballet_position_right(win, 100, 100)  # stick man 1
        ballet_position_right(win, 300, 100)  # stick man 2
        ballet_position_right(win, 500, 100)  # stickman 3
        ballet_position_right(win, 700, 100)  # stick man 4
        win.update_frame(1)

        # frame5
        win.clear()
        up_down(win, 100, 100)  # stick man 1
        ballet_position_left(win, 300, 100)  # stick man 2
        ballet_position_right(win, 500, 100)  # stick man 3
        up_down(win, 700, 100)  # stickman 4
        win.update_frame(1)

        # frame6- fusion frame
        win.clear()
        up_down(win, 100, 100)  # stick man 1
        ballet_position_right(win, 350, 100)  # stick man 2
        ballet_position_left(win, 450, 100)  # stick man 3
        hands_up(win, 700, 100)
        win.update_frame(0.5)

        # frame 7 after fusion frame
        win.clear()
        ballet_position_right(win, 100, 100)
        after_fusion(win, 400, 100)
        ballet_position_left(win, 700, 100)
        win.update_frame(0.5)

        # frame 8
        win.clear()
        hands_up(win, 100, 100)
        after_fusion_ballet(win, 400, 100)
        hands_oneside_up(win, 700, 100)
        win.update_frame(1)

        # frame 9
        win.clear()
        slant_position_left(win, 100, 100)
        after_fusion_legs(win, 400, 100)
        slant_position_right(win, 700, 100)
        win.update_frame(1)

        # frame last
        win.clear()
        create_stick_man(win, 100, 100)  # stick man 1
        create_stick_man(win, 300, 100)  # stick man 2
        create_stick_man(win, 500, 100)  # stickman 3
        legs_bend(win, 700, 100)  # stick man 4
        win.update_frame(3)


stick_dance()

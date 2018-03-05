"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Isaiah Jolly.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg
window = rg.TurtleWindow()

jake = rg.SimpleTurtle('turtle')
jake.pen = rg.Pen('steel blue', 10)
jake.speed = 10

franklin = rg.SimpleTurtle('turtle')
franklin.pen = rg.Pen('spring green', 10)
franklin.speed = 10

for k in range(10):

    jake.draw_circle(k*25)
    franklin.draw_regular_polygon(5,30*k)

    jake.pen_up()
    jake.right(90)
    jake.forward(25*k)
    jake.left(90)
    jake.forward(20*k)
    jake.pen_down()

    franklin.pen_up()
    franklin.right(90)
    franklin.forward(20*k)
    franklin.left(90)
    franklin.forward(25*k)
    franklin.pen_down()

window.close_on_mouse_click()
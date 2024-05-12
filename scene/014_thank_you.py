from manim import * # 
import math
from manim_slides import Slide

class XMinusYProofWhen(Slide):
    def construct(self):
        ax = Axes(tips=False).add_coordinates()
        plane = NumberPlane()

        t = ValueTracker(0.88)
        def func(x):
            return math.sqrt(abs(t.get_value() * math.cos(4*x) - x*x))

        graph = ax.plot(lambda x: func(x), x_range=[-2, 2], use_smoothing=False)
        self.add(ax, plane)
        self.play(Write(graph))

        # func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3
        # self.play(StreamLines(func).create())
        # thanks = Tex("Thank you for watching!", color=GREEN).scale(2).to_edge(DOWN)

        # self.play(Write(thanks))


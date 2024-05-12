from manim import *  # noqa
from component.graph import ComplementGraph
from manim_slides import Slide


class XMinusYProofWhen(Slide):
    def construct(self):
        graph = ComplementGraph(4)
        graph.mobjects().scale(0.8).shift(LEFT)
        self.play(
            graph.show_graph(),
            graph.show_dots(),
            graph.show_lines(),
            graph.show_control_box(),
            graph.show_value_indicators(),
        )

        self.play(*graph.update_x_y(x=-7, y=7))
        self.play(*graph.update_x_y(x=-7, y=-7))
        self.play(*graph.update_x_y(x=-7, y=-6))
        self.play(*graph.update_x_y(x=-7, y=-5))
        self.play(*graph.update_x_y(x=-4, y=-7))
        self.play(*graph.update_x_y(x=-4, y=-6))
        self.play(*graph.update_x_y(x=-4, y=-5))
        self.play(*graph.update_x_y(x=-1, y=-7))
        self.play(*graph.update_x_y(x=-1, y=-6))
        self.play(*graph.update_x_y(x=-1, y=-5))
from manim import * # noqa
from manim_slides import Slide
from component.graph import ComplementGraph

class XPlusYGraph(Slide):
    def construct(self):
        graph = ComplementGraph(4)
        self.play(graph.show_graph(), graph.show_dots(), graph.show_lines(), graph.show_control_box())
        self.play(graph.show_value_indicators())
        self.play(*graph.update_x_y(x=1, y=2))
        self.next_slide()
        self.play(*graph.update_x_y(x=3, y=4))
        self.next_slide()
        self.play(*graph.update_x_y(x=3, y=5))
        self.play(*graph.update_x_y(x=3, y=6))
        self.play(*graph.update_x_y(x=3, y=7))
        self.play(*graph.update_x_y(x=4, y=7))
        self.play(*graph.update_x_y(x=5, y=7))
        self.play(*graph.update_x_y(x=6, y=7))
        self.play(*graph.update_x_y(x=7, y=7))
        self.next_slide()

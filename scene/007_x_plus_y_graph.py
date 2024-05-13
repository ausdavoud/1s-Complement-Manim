from manim import * # noqa
from manim_slides import Slide
from component.graph import ComplementGraph

class XPlusYGraph(Slide):
    def construct(self):
        title = Tex("1's Complement").scale(3/4).to_edge(UL).set_color_by_gradient(YELLOW, RED)

        subtitle = (
            Tex("$x + y$: Plane")
            .scale(3 / 4)
            .to_edge(UR)
            .set_color_by_gradient(WHITE, GRAY)
        )
        self.add(title, subtitle)
        graph = ComplementGraph(4)
        graph.mobjects().scale(.9)
        self.play(graph.show_graph(), graph.show_dots(), graph.show_lines(), graph.show_control_box())
        self.play(graph.show_value_indicators())
        self.play(*graph.update_x_y(x=1, y=2))
        self.next_slide()
        self.play(*graph.update_x_y(x=3, y=4))
        self.next_slide()
        self.play(*graph.update_x_y(x=3, y=5))
        self.next_slide()
        self.play(*graph.update_x_y(x=3, y=6))
        self.next_slide()
        self.play(*graph.update_x_y(x=3, y=7))
        self.next_slide()
        self.play(*graph.update_x_y(x=4, y=7))
        self.next_slide()
        self.play(*graph.update_x_y(x=5, y=7))
        self.next_slide()
        self.play(*graph.update_x_y(x=6, y=7))
        self.next_slide()
        self.play(*graph.update_x_y(x=7, y=7))
        self.next_slide()

        next_subtitle = Tex("$x + y$: Proof").scale(3)

        self.play(FadeOut(graph.mobjects()), ReplacementTransform(subtitle, next_subtitle))

        self.wait(2)

        self.play(next_subtitle.animate.scale(1/4).to_edge(UR).set_color_by_gradient(WHITE, GRAY))
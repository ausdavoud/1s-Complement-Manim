from component.graph import ComplementGraph
from manim import * # noqa
from manim_slides import Slide


class XMinusYGraph(Slide):
    def construct(self):
        title = Tex("1's Complement").scale(3/4).to_edge(UL).set_color_by_gradient(YELLOW, RED)

        subtitle = (
            Tex("$x - y$: Plane")
            .scale(3 / 4)
            .to_edge(UR)
            .set_color_by_gradient(WHITE, GRAY)
        )
        self.add(title, subtitle)

        graph = ComplementGraph(4)
        graph.mobjects().scale(0.9).shift(LEFT)
        self.play(
            graph.show_graph(),
            graph.show_dots(),
            graph.show_lines(),
            graph.show_control_box(),
        )

        examples = VGroup()

        def move_examples_aside(buffer=0):
            arrow = (
                Arrow(LEFT, ORIGIN)
                .next_to(graph.control_box, DOWN)
                .align_to(graph.x_tex[1], RIGHT)
                .shift(buffer * DOWN / 2)
            )

            new_x = graph.x_dec.copy()
            new_x.clear_updaters()
            new_x.next_to(arrow, LEFT)

            new_y = graph.y_dec.copy()
            new_y.clear_updaters()
            new_y.next_to(arrow, RIGHT)

            examples.add(VGroup(new_x, new_y, arrow))

            anims = AnimationGroup(
                TransformFromCopy(graph.x_dec, new_x),
                TransformFromCopy(graph.y_dec, new_y),
                Write(arrow),
                lag_ratio=0.3,
            )
            self.play(anims)

        self.play(graph.show_value_indicators())
        self.play(*graph.update_x_y(x=-7, y=0))
        self.next_slide()
        self.play(*graph.update_x_y(x=-7, y=1))
        self.next_slide()
        self.play(*graph.update_x_y(x=-7, y=2))
        self.next_slide()
        self.play(*graph.update_x_y(x=-7, y=3))
        self.next_slide()
        self.play(*graph.update_x_y(x=-7, y=4))
        self.next_slide()
        self.play(*graph.update_x_y(x=-7, y=5))
        self.next_slide()
        self.play(*graph.update_x_y(x=-7, y=6))
        self.next_slide()
        self.play(*graph.update_x_y(x=-7, y=7))

        self.next_slide()

        self.play(*graph.update_x_y(x=-5, y=0))
        self.next_slide()
        self.play(*graph.update_x_y(x=-5, y=1))
        self.next_slide()
        self.play(*graph.update_x_y(x=-5, y=2))
        self.next_slide()
        self.play(*graph.update_x_y(x=-5, y=3))
        self.next_slide()
        self.play(*graph.update_x_y(x=-5, y=4))
        self.next_slide()
        self.play(*graph.update_x_y(x=-5, y=5))
        self.next_slide()
        self.play(*graph.update_x_y(x=-5, y=6))

        move_examples_aside()
        self.next_slide()


        self.play(graph.subtract_carry())
        self.play(graph.add_value_to_xy())
        self.next_slide()


        self.play(*graph.update_x_y(x=-3, y=0))
        self.next_slide()
        self.play(*graph.update_x_y(x=-3, y=1))
        self.next_slide()
        self.play(*graph.update_x_y(x=-3, y=2))
        self.next_slide()
        self.play(*graph.update_x_y(x=-3, y=3))
        self.next_slide()
        self.play(*graph.update_x_y(x=-3, y=4))

        move_examples_aside(1)
        self.next_slide()

        self.play(graph.subtract_carry())
        self.play(graph.add_value_to_xy())

        self.next_slide()


        self.play(*graph.update_x_y(x=-2, y=0))
        self.next_slide()
        self.play(*graph.update_x_y(x=-2, y=1))
        self.next_slide()
        self.play(*graph.update_x_y(x=-2, y=2))
        self.next_slide()

        self.play(*graph.update_x_y(x=-2, y=3))

        move_examples_aside(2)
        self.next_slide()


        self.play(graph.subtract_carry())
        self.play(graph.add_value_to_xy())

        self.next_slide()

        self.play(*graph.update_x_y(x=-2, y=2))

        self.play(VGroup(graph.mobjects(), examples).animate.scale(5/6))
        self.play(*graph.update_x_y(x=-2, y=5))

        self.next_slide()
        self.play(graph.subtract_carry())
        self.play(graph.add_value_to_xy())

        self.next_slide()

        # Fade
        self.play(FadeOut(graph.mobjects(), examples))

        # Next sub
        next_subtitle = Tex("$x - y$: Proof").scale(3)
        self.play(ReplacementTransform(subtitle, next_subtitle))
        self.wait(2)

        self.play(next_subtitle.animate.scale(1/4).to_edge(UR).set_color_by_gradient(WHITE, GRAY))


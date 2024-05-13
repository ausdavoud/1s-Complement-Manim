from manim import * #noqa
from manim_slides import Slide

from component.graph import ComplementGraph


class Graph(Slide):
    def construct(self):
        title = Tex("1's Complement").scale(3/4).to_edge(UL).set_color_by_gradient(YELLOW, RED)

        subtitle = (
            Tex("The Plane")
            .scale(3 / 4)
            .to_edge(UR)
            .set_color_by_gradient(WHITE, GRAY)
        )

        self.add(title, subtitle)

        p_table = MathTable(
            [
                [("+0"), ("0000")],
                [("1"), ("0001")],
                [("2"), ("0010")],
                [("3"), ("0011")],
                [("4"), ("0100")],
                [("5"), ("0101")],
                [("6"), ("0110")],
                [("7"), ("0111")],
            ],
            col_labels=[Tex("Decimal"), Tex("Binary (1'sC)")],
            include_outer_lines=True,
        ).scale(0.5)

        for item in p_table.get_entries():
            item.set_color(BLUE)

        n_table = (
            MathTable(
                [
                    [("-7"), ("1000")],
                    [("-6"), ("1001")],
                    [("-5"), ("1010")],
                    [("-4"), ("1011")],
                    [("-3"), ("1100")],
                    [("-2"), ("1101")],
                    [("-1"), ("1110")],
                    [("-0"), ("1111")],
                ],
                col_labels=[Tex("Decimal"), Tex("Binary (1'sC)")],
                include_outer_lines=True,
            )
            .scale(0.5)
            .shift(2 * RIGHT)
        )

        for item in n_table.get_entries():
            item.set_color(PURPLE)

        self.play(FadeIn(p_table))
        self.next_slide()

        self.play(p_table.animate.shift(2 * LEFT))
        self.play(FadeIn(n_table))

        self.next_slide()

        self.play(FadeOut(n_table))
        self.play(p_table.animate.shift(6 * RIGHT))

        oc_graph = ComplementGraph(4, True)
        oc_graph.mobjects().shift(1.5 * LEFT).scale(.9)
        self.play(oc_graph.show_graph())
        self.play(oc_graph.transform_positive_dots(p_table))

        n_table.shift(2 * RIGHT)
        self.play(FadeOut(p_table))
        self.play(FadeIn(n_table))

        self.play(oc_graph.transform_negative_dots(n_table))

        self.play(FadeOut(n_table), oc_graph.show_lines())

        self.next_slide()

        self.play(oc_graph.show_control_box(), oc_graph.show_value_indicators())
        self.play(*oc_graph.update_x_y(x=2, y=3))
        self.next_slide()
        self.play(*oc_graph.update_x_y(x=3, y=7))
        self.next_slide()
        self.play(*oc_graph.update_x_y(x=-3, y=1))
        self.next_slide()
        self.play(*oc_graph.update_x_y(x=-3, y=2))
        self.next_slide()
        self.play(*oc_graph.update_x_y(x=-3, y=3))
        self.next_slide()
        self.play(*oc_graph.update_x_y(x=-3, y=4))
        self.next_slide()
        self.play(*oc_graph.update_x_y(x=-3, y=5))
        self.next_slide()
        self.play(oc_graph.subtract_carry())
        self.next_slide()
        self.play(oc_graph.add_value_to_xy())

        self.next_slide()
        self.play(FadeOut(oc_graph.mobjects()))

        next_subtitle = Tex("When?").scale(3)
        self.play(ReplacementTransform(subtitle, next_subtitle))
        self.wait(2)
        self.play(next_subtitle.animate.scale(1/4).to_edge(UR).set_color_by_gradient(WHITE, GRAY))

from manim import * #noqa
from manim_slides import Slide

from scene.component.graph import ComplementGraph


class Graph(Slide):
    def construct(self):
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

        self.play(FadeIn(p_table))
        self.next_slide()

        self.play(p_table.animate.shift(2 * LEFT))
        self.play(FadeIn(n_table))

        self.next_slide()

        self.play(FadeOut(n_table))
        self.play(p_table.animate.shift(6 * RIGHT))

        # graph = (
        #     NumberPlane(
        #         x_range=(-7, 7),
        #         y_range=(0, 15),
        #         x_length=7,
        #         y_length=7,
        #         tips=False,
        #         background_line_style={"stroke_color": TEAL, "stroke_opacity": 0.5},
        #     )
        #     .add_coordinates()
        #     .to_edge(LEFT)
        #     .shift(0.5 * RIGHT)
        # )
        oc_graph = ComplementGraph(4)
        oc_graph.mobjects().shift(1.5 * LEFT)
        self.play(oc_graph.show_graph())
        self.play(oc_graph.transform_positive_dots(p_table))

        self.next_slide()

        n_table.shift(2 * RIGHT)
        self.play(FadeOut(p_table))
        self.play(FadeIn(n_table))

        self.play(oc_graph.transform_negative_dots(n_table))

        self.play(FadeOut(n_table), oc_graph.show_lines())

        self.next_slide()

        # x_value = ValueTracker(0)
        # y_value = ValueTracker(0)
        # x_graph_value = ValueTracker(0)
        # y_graph_value = ValueTracker(0)
        # x_plus_y_graph_value = ValueTracker(0)

        # x_color = YELLOW
        # y_color = RED
        # x_plus_y_color = WHITE

        # x_decimal_number = DecimalNumber(
        #     0, num_decimal_places=1, include_sign=False, color=x_color
        # ).add_updater(lambda d: d.set_value(x_value.get_value()))

        # y_decimal_number = DecimalNumber(
        #     0, num_decimal_places=1, include_sign=False, color=y_color
        # ).add_updater(lambda d: d.set_value(y_value.get_value()))

        # x_tex = (
        #     VGroup(MathTex("x = ", color=x_color), x_decimal_number)
        #     .arrange(RIGHT)
        #     .next_to(graph)
        #     .shift(2 * UP)
        # )

        # y_tex = (
        #     VGroup(MathTex("y = ", color=y_color), y_decimal_number)
        #     .arrange(RIGHT)
        #     .next_to(graph)
        #     .shift(UP)
        # )
        # y_decimal_number.shift(0.075 * UP)

        # x_plus_y_decimal_number = DecimalNumber(
        #     0,
        #     num_decimal_places=1,
        #     include_sign=False,
        # ).add_updater(lambda d: d.set_value(x_value.get_value() + y_value.get_value()))

        # x_plus_y_tex = (
        #     VGroup(MathTex("x + y = "), x_plus_y_decimal_number)
        #     .arrange(RIGHT)
        #     .next_to(graph, RIGHT)
        # )
        # x_plus_y_decimal_number.shift(0.07 * UP)

        # x_dot = Dot(color=x_color)
        # y_dot = Dot(color=y_color)
        # x_plus_y_dot = Dot()

        # def get_y(x: float, exceed_max=False) -> tuple[float, float]:
        #     if x < 0 or exceed_max:
        #         return x, x + 15
        #     elif 0 <= x:
        #         return x, x

        # x_dot.add_updater(
        #     lambda mobject: mobject.move_to(graph.c2p(*get_y(x_value.get_value())))
        # )
        # y_dot.add_updater(lambda d: d.move_to(graph.c2p(*get_y(y_value.get_value()))))
        # x_plus_y_dot.add_updater(
        #     lambda d: d.move_to(
        #         graph.c2p(
        #             7, get_y(x_value.get_value())[1] + get_y(y_value.get_value())[1]
        #         )
        #     )
        # )
        # x_plus_y_dot.update()

        # x_line = always_redraw(
        #     lambda: Line(
        #         graph.c2p(*get_y(x_value.get_value())),
        #         graph.c2p(x_value.get_value(), 0),
        #         color=x_color,
        #     )
        # )

        # y_line = always_redraw(
        #     lambda: Line(
        #         graph.c2p(*get_y(y_value.get_value())),
        #         graph.c2p(y_value.get_value(), 0),
        #         color=y_color,
        #     )
        # )

        # x_plus_y_line = always_redraw(
        #     lambda: Line(
        #         x_plus_y_dot.get_center(),
        #         graph.c2p(7, 0),
        #     )
        # )

        # self.play(
        #     Write(x_tex),
        #     Write(y_tex),
        #     Write(x_plus_y_tex),
        #     Create(x_dot),
        #     Create(y_dot),
        #     Create(x_plus_y_dot),
        #     Create(x_line),
        #     Create(y_line),
        #     Create(x_plus_y_line),
        # )

        self.play(oc_graph.show_control_box(), oc_graph.show_value_indicators())
        self.play(*oc_graph.update_x_y(x=1, y=3))
        self.next_slide()
        self.play(*oc_graph.update_x_y(x=3, y=7))
        self.next_slide()
        self.play(*oc_graph.update_x_y(x=-4, y=2))
        self.next_slide()
        self.play(*oc_graph.update_x_y(x=-4, y=3))
        self.next_slide()
        self.play(*oc_graph.update_x_y(x=-4, y=4))
        self.next_slide()
        self.play(*oc_graph.update_x_y(x=-4, y=5))
        self.next_slide()
        self.play(oc_graph.subtract_carry())
        self.next_slide()
        self.play(oc_graph.add_value_to_xy())
        # oc_graph.subtract_result()

        # self.play(x_value.animate.set_value(1), y_value.animate.set_value(3))
        # self.next_slide()
        # self.play(x_value.animate.set_value(3), y_value.animate.set_value(7))
        # self.next_slide()
        # self.play(x_value.animate.set_value(-5), y_value.animate.set_value(3))
        # self.next_slide()
        # self.play(x_value.animate.set_value(-5), y_value.animate.set_value(4))
        # self.next_slide()
        # self.play(x_value.animate.set_value(-5), y_value.animate.set_value(5))
        # self.next_slide()
        # self.play(x_value.animate.set_value(-5), y_value.animate.set_value(6))

        # Subtract 16, Add 1
        # x_plus_y_dot.clear_updaters()
        # self.play(x_plus_y_dot.animate.move_to(graph.c2p(7, 0)))
        # self.next_slide()
        # self.play(x_plus_y_dot.animate.move_to(graph.c2p(7, 1)))
        # self.next_slide()

        self.wait(3)

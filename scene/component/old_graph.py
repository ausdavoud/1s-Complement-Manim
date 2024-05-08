from manim import *
from manim_slides import Slide


class ComplementGraph:
    """One's Complement Graph"""

    def __init__(self, bit: int) -> None:
        self.bit = bit
        self.max_x = 2 ** (self.bit - 1) - 1
        self.max_y = 2 ** (self.bit) - 1
        self.negative_color = PURPLE
        self.positive_color = BLUE_E

        self.graph = NumberPlane(
            x_range=(-self.max_x, self.max_x),
            y_range=(0, self.max_y),
            x_length=self.max_x,
            y_length=self.max_x,
            tips=False,
            background_line_style={"stroke_color": TEAL, "stroke_opacity": 0.5},
        ).add_coordinates()
        self.labels = self.graph.get_axis_labels(
            Tex("B").scale(0.5), Tex("D").scale(0.5)
        )

        self.dots = self.get_dots()
        self.lines = self.get_lines()

        self.scale_factor = 0.7
        self.control_box = (
            Rectangle(color=TEAL, height=2, width=3)
            .next_to(self.graph, RIGHT)
            .shift(2.5 * UP)
        )
        # X
        self.x_color = YELLOW
        self.x_vt = ValueTracker(0)
        self.x_tex = (
            MathTex("x", " =", color=self.x_color)
            .scale(self.scale_factor)
            .move_to(self.control_box)
            .shift(0.5 * UP + 0.25 * LEFT)
        )
        self.x_dec = (
            DecimalNumber(
                0, num_decimal_places=1, include_sign=True, color=self.x_color
            )
            .scale(self.scale_factor)
            .next_to(self.x_tex[1], RIGHT)
            .add_updater(lambda d: d.set_value(self.x_vt.get_value()))
        )
        self.x_dot = (
            Dot(color=self.x_color)
            .add_updater(
                lambda d: d.move_to(
                    self.graph.c2p(self.x_vt, self.x_func(self.x_vt.get_value(), True))
                )
            )
            .update()
        )
        self.x_height_dec = (
            DecimalNumber(0, num_decimal_places=1, color=self.x_color)
            .scale(0.5)
            .add_updater(
                lambda d: d.set_value(self.x_func(self.x_vt.get_value(), True))
            )
            .add_updater(lambda d: d.next_to(self.x_dot, UP))
        )
        self.x_line = always_redraw(
            lambda: Line(
                self.graph.c2p(self.x_vt.get_value(), 0),
                self.x_dot.get_center(),
                color=self.x_color,
            )
        ).update()

        # Y
        self.y_color = RED
        self.y_vt = ValueTracker(0)
        self.y_tex = (
            MathTex("y", " =", color=self.y_color)
            .scale(self.scale_factor)
            .next_to(self.x_tex, DOWN)
            .align_to(self.x_tex, RIGHT)
        )
        self.y_dec = (
            DecimalNumber(
                0, num_decimal_places=1, include_sign=True, color=self.y_color
            )
            .scale(self.scale_factor)
            .add_updater(lambda d: d.set_value(self.y_vt.get_value()))
            .next_to(self.y_tex[1], RIGHT)
        )
        self.y_dot = (
            Dot(color=self.y_color)
            .add_updater(
                lambda d: d.move_to(
                    self.graph.c2p(self.y_vt, self.x_func(self.y_vt.get_value()))
                )
            )
            .update()
        )
        self.y_height_dec = (
            DecimalNumber(0, num_decimal_places=1, color=self.y_color)
            .scale(0.5)
            .add_updater(lambda d: d.set_value(self.x_func(self.y_vt.get_value())))
            .add_updater(lambda d: d.next_to(self.y_dot, UP))
        )
        self.y_line = always_redraw(
            lambda: Line(
                self.graph.c2p(self.y_vt.get_value(), 0),
                self.y_dot.get_center(),
                color=self.y_color,
            )
        ).update()

        # X + Y
        self.xy_tex = (
            MathTex("x + y", " =")
            .scale(self.scale_factor)
            .next_to(self.y_tex, DOWN)
            .align_to(self.y_tex, RIGHT)
        )
        self.xy_dec = (
            DecimalNumber(0, num_decimal_places=1, include_sign=True)
            .scale(self.scale_factor)
            .add_updater(
                lambda d: d.set_value(self.x_vt.get_value() + self.y_vt.get_value())
            )
            .next_to(self.xy_tex[1], RIGHT)
        )
        self.xy_dot = (
            Dot()
            .add_updater(
                lambda d: d.move_to(
                    self.graph.c2p(
                        self.max_x,
                        self.func(
                            self.func(self.x_vt.get_value() + self.y_vt.get_value())
                        ),
                    ),
                )
            )
            .update()
        )
        self.xy_height_dec = (
            DecimalNumber(0, num_decimal_places=1)
            .scale(0.5)
            .add_updater(
                lambda d: d.set_value(
                    self.func(self.x_vt.get_value()) + self.func(self.y_vt.get_value())
                ).add_updater(lambda d: d.next_to(self.xy_dot, UP))
            )
        )
        self.xy_line = always_redraw(
            lambda: Line(
                self.graph.c2p(self.max_x, 0),
                self.graph.c2p(
                    self.max_x,
                    self.func(self.x_vt.get_value() + self.y_vt.get_value()),
                ),
            )
        ).update()

        self.positive_color = BLUE_E
        self.negative_color = PURPLE

    def transform_positive_dots(self, positive_table: MathTable) -> list:
        anims = self.transform_dots(positive_table)

        anims = AnimationGroup(*anims, lag_ratio=0.3)

        return anims

    def transform_negative_dots(self, negative_table: MathTable):
        anims = self.transform_dots(negative_table, True)

        anims = AnimationGroup(*anims, lag_ratio=0.3)

        return anims

    def transform_dots(self, table: MathTable, margin: bool = False):
        """Don't Use Explicitly"""
        anims = []
        for i in range(self.max_x + 1):
            table_row = VGroup(*[table.get_entries((i + 2, j)) for j in [1, 2]])
            dot = self.dots[i + ((self.max_x + 1) * int(margin))]
            anims.append(ReplacementTransform(table_row, dot))

        return anims
    
    def show_dots(self):
        return FadeIn(*self.dots)

    def show_lines(self):
        return FadeIn(*self.lines)

    def show_graph(self):
        return Write(self.graph)

    def mobjects(self):
        return VGroup(
            self.graph,
            *self.dots,
            *self.lines,
            self.control_box,
            self.x_dec,
            self.x_tex,
            self.x_dot,
            self.x_height_dec,
            self.x_line,
            self.y_dec,
            self.y_tex,
            self.y_dot,
            self.y_height_dec,
            self.y_line,
            self.xy_dec,
            self.xy_tex,
            self.xy_dot,
            self.xy_height_dec,
            self.xy_line,
        )

    def get_point_pair(self, x: float, exceed_max=False) -> tuple[float, float]:
        if x < 0 or exceed_max:
            return x, x + self.max_y
        elif 0 <= x:
            return x, x
        
    def x_func(self, x: float, negative_zero=False) -> float:
        if x > 0:
            return x
        elif x < 0:
            return x + self.max_y
        else:
            return (negative_zero * 1) or self.max_y

    def get_dots(self):
        dots = []
        dot_color = self.negative_color
        for i in range(-self.max_x, self.max_x + 1):
            if i == 0:
                dot = Dot(self.graph.c2p(0, self.max_y), color=dot_color)
                dots.append(dot)

                dot_color = self.positive_color

                dot = Dot(self.graph.c2p(0, 0), color=dot_color)
                dots.append(dot)
                continue

            dot = Dot(self.graph.c2p(*self.get_point_pair(i)), color=dot_color)
            dots.append(dot)

        return dots

    def get_lines(self):
        positive_line = self.graph.plot(
            self.x_func, x_range=[0, self.max_x], color=self.positive_color
        )
        negative_line = self.graph.plot(
            lambda x: self.x_func(x, True),
            x_range=[-self.max_x, 0],
            color=self.negative_color,
        )

        lines = [positive_line, negative_line]
        return lines

    def update_x(self, x_value):
        return self.x_vt.animate.set_value(x_value)

    def update_y(self, y_value):
        return self.y_vt.animate.set_value(y_value)

    def exceed(self):
        new_xy_line = always_redraw(
            lambda: Line(
                self.graph.c2p(self.max_x, 0),
                self.graph.c2p(self.max_x, 12),
            )
        ).update()
        self.xy_line = new_xy_line

        return ReplacementTransform(self.xy_line, new_xy_line)

    def not_exceed(self):
        self.xy_line = always_redraw(
            lambda: Line(
                self.graph.c2p(self.max_x, 0),
                self.graph.c2p(self.max_x, 12),
            )
        ).update()

    def subtract_result(self):
        """
        Subtract 2^n from x + y, then add 1.
        """
        self.xy_line = always_redraw(
            lambda: Line(
                self.graph.c2p(self.max_x, 0),
                self.graph.c2p(
                    self.max_x,
                    self.func(self.x_vt.get_value() + self.y_vt.get_value())
                    - self.max_y,
                ),
            )
        )

        self.xy_height_dec = (
            DecimalNumber(0, num_decimal_places=1)
            .scale(0.5)
            .add_updater(
                lambda d: d.set_value(
                    self.func(self.x_vt.get_value())
                    + self.func(self.y_vt.get_value())
                    - self.max_y
                    + 1
                ).add_updater(lambda d: d.next_to(self.xy_dot, UP))
            )
        ).update()

        self.xy_line = always_redraw(
            lambda: Line(
                self.graph.c2p(self.max_x, 0),
                self.graph.c2p(
                    self.max_x,
                    self.func(self.x_vt.get_value() + self.y_vt.get_value())
                    - self.max_y,
                ),
            )
        )

        self.xy_height_dec = (
            DecimalNumber(0, num_decimal_places=1)
            .scale(0.5)
            .add_updater(
                lambda d: d.set_value(
                    self.func(self.x_vt.get_value())
                    + self.func(self.y_vt.get_value())
                    - self.max_y
                    + 1
                ).add_updater(lambda d: d.next_to(self.xy_dot, UP))
            )
        ).update()

        self.xy_line = always_redraw(
            lambda: Line(
                self.graph.c2p(self.max_x, 0),
                self.graph.c2p(
                    self.max_x,
                    self.func(self.x_vt.get_value() + self.y_vt.get_value()),
                ),
            )
        )

        self.xy_height_dec = (
            DecimalNumber(0, num_decimal_places=1)
            .scale(0.5)
            .add_updater(
                lambda d: d.set_value(
                    self.func(self.x_vt.get_value()) + self.func(self.y_vt.get_value())
                ).add_updater(lambda d: d.next_to(self.xy_dot, UP))
            )
        ).update()

    def show_control_box(self):
        return FadeIn(
            self.control_box,
            self.x_tex,
            self.x_dec,
            self.y_tex,
            self.y_dec,
            self.xy_tex,
            self.xy_dec,
        )

    def show_value_indicator(self):
        return FadeIn(
            self.x_dot,
            self.x_line,
            self.x_height_dec,
            self.y_dot,
            self.y_line,
            self.y_height_dec,
            self.xy_dot,
            self.xy_line,
            self.xy_height_dec,
        )


class Test(Slide):
    def construct(self):
        graph = self.FCGraph(4)
        self.play(graph.show_graph())
        self.play(graph.update_x(1), graph.update_y(3))
        self.wait(2)
        self.play(graph.mobjects().animate.shift(LEFT))
        self.wait(2)

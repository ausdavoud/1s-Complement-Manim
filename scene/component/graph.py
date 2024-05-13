from manim import * #noqa


class ComplementGraph:
    """One's Complement Graph"""

    def __init__(self, order: int, binary_coordinates: bool = False) -> None:
        self.bit = order
        self.binary_coordinates = binary_coordinates
        self.max_x = 2 ** (self.bit - 1) - 1
        self.max_y = 2 ** (self.bit) - 1
        self.negative_color = PURPLE
        self.positive_color = BLUE_E
        self.text_scale_factor = 0.7
        self.scale_factor = 0.95


        y_pos = [x for x in range(1, self.max_y+1)]

        # strings are automatically converted into a Tex mobject.
        self.graph: NumberPlane = (
            NumberPlane(
                x_range=(-self.max_x, self.max_x),
                y_range=(0, self.max_y),
                x_length=self.max_x,
                y_length=self.max_x,
                tips=False,
                background_line_style={"stroke_color": TEAL, "stroke_opacity": 0.5},
            )
            .scale(self.scale_factor)
        )

        if self.binary_coordinates:
            y_vals = [format(num, "b").zfill(order) for num in y_pos]
            y_labels = dict(zip(y_pos, y_vals))

            self.graph.add_coordinates(None, y_labels, None)
        else:
            self.graph.add_coordinates()

        self.labels = self.graph.get_axis_labels(
            Tex("D").scale(self.text_scale_factor), Tex("C").scale(self.text_scale_factor)
        )

        self.dots = self.get_dots()
        self.lines = self.get_lines()

        self.control_box = (
            Rectangle(color=TEAL, height=2, width=3)
            .next_to(self.graph, RIGHT)
            .shift(1.5 * UP)
        )

        # X
        self.X_COLOR = YELLOW
        self.x_vt = ValueTracker(0)
        self.x_tex = (
            MathTex("x", "=", color=self.X_COLOR)
            .scale(self.text_scale_factor)
            .move_to(self.control_box)
            .shift(0.5 * UP + 0.25 * LEFT)
        )
        self.x_dec = (
            DecimalNumber(
                0, num_decimal_places=1, include_sign=True, color=self.X_COLOR
            )
            .scale(self.text_scale_factor)
            .next_to(self.x_tex[1], RIGHT)
            .add_updater(lambda d: d.set_value(self.x_vt.get_value()))
        )
        self.x_dot = (
            Dot(color=self.X_COLOR)
            .add_updater(
                lambda d: d.move_to(
                    self.graph.c2p(
                        self.x_vt.get_value(),
                        self.decimal_of_complement(self.x_vt.get_value()),
                    )
                )
            )
            .update()
        )
        self.x_height_dec = (
            DecimalNumber(0, num_decimal_places=1, color=self.X_COLOR)
            .scale(self.text_scale_factor)
            .add_updater(
                lambda d: d.set_value(self.decimal_of_complement(self.x_vt.get_value()))
            )
            .add_updater(lambda d: d.next_to(self.x_dot, 0.25 * LEFT + 0.25 * UP))
        )

        self.x_line = always_redraw(
            lambda: Line(
                self.graph.c2p(self.x_vt.get_value(), 0),
                self.x_dot.get_center(),
                color=self.X_COLOR,
            )
        ).update()

        # Y
        self.Y_COLOR = RED
        self.y_vt = ValueTracker(0)
        self.y_tex = (
            MathTex("y", "=", color=self.Y_COLOR)
            .scale(self.text_scale_factor)
            .move_to(self.control_box)
            .shift(0.25 * LEFT)
        )
        self.y_dec = (
            DecimalNumber(
                0, num_decimal_places=1, include_sign=True, color=self.Y_COLOR
            )
            .scale(self.text_scale_factor)
            .next_to(self.y_tex[1], RIGHT)
            .add_updater(lambda d: d.set_value(self.y_vt.get_value()))
        )
        self.y_dot = (
            Dot(color=self.Y_COLOR)
            .add_updater(
                lambda d: d.move_to(
                    self.graph.c2p(
                        self.y_vt.get_value(),
                        self.decimal_of_complement(self.y_vt.get_value()),
                    )
                )
            )
            .update()
        )
        self.y_height_dec = (
            DecimalNumber(0, num_decimal_places=1, color=self.Y_COLOR)
            .scale(self.text_scale_factor)
            .add_updater(
                lambda d: d.set_value(self.decimal_of_complement(self.y_vt.get_value()))
            )
            .add_updater(lambda d: d.next_to(self.y_dot, 0.25 * LEFT + 0.25 * UP))
        )
        self.y_line = always_redraw(
            lambda: Line(
                self.graph.c2p(self.y_vt.get_value(), 0),
                self.y_dot.get_center(),
                color=self.Y_COLOR,
            )
        ).update()
        # X + Y
        self.xy_vt = ValueTracker(0)
        self.xy_tex = (
            MathTex("x + y", "=")
            .scale(self.text_scale_factor)
            .move_to(self.control_box)
            .shift(0.5 * DOWN + 0.25 * LEFT)
            .align_to(self.x_tex, RIGHT)
        )
        self.xy_dec = (
            DecimalNumber(0, num_decimal_places=1, include_sign=1)
            .scale(self.text_scale_factor)
            .next_to(self.xy_tex[1], RIGHT)
            .add_updater(
                lambda d: d.set_value(self.x_vt.get_value() + self.y_vt.get_value())
            )
        )
        self.xy_dot = (
            Dot()
            .add_updater(
                lambda d: d.move_to(self.graph.c2p(self.max_x, self.xy_vt.get_value()))
            )
            .update()
        )
        self.xy_height_dec = (
            DecimalNumber(0, num_decimal_places=1)
            .scale(self.text_scale_factor)
            .add_updater(lambda d: d.set_value(self.xy_vt.get_value()))
            .add_updater(lambda d: d.next_to(self.xy_dot, 0.25 * LEFT + 0.25 * UP))
        )
        self.xy_line = always_redraw(
            lambda: Line(
                self.graph.c2p(self.max_x, 0),
                self.graph.c2p(self.max_x, self.xy_vt.get_value()),
            )
        ).update()

    def decimal_of_complement(self, x: float, support_negative_zero=False) -> float:
        if x > 0:
            return x
        if x < 0:
            return x + self.max_y
        elif support_negative_zero:
            return self.max_y
        return 0

    def update_x_y(self, **kwargs):
        new_x = kwargs.get("x", self.x_vt.get_value())
        new_y = kwargs.get("y", self.y_vt.get_value())
        new_xy = kwargs.get(
            "xy", self.decimal_of_complement(new_x) + self.decimal_of_complement(new_y)
        )
        # new_x = x if x else self.x_vt.get_value()
        # new_y = y if y else self.y_vt.get_value()
        # new_xy = xy if xy else self.decimal_of_complement(new_x) + self.decimal_of_complement(new_y)

        return [
            self.x_vt.animate.set_value(new_x),
            self.y_vt.animate.set_value(new_y),
            self.xy_vt.animate.set_value(new_xy),
        ]

    def subtract_carry(self):
        return self.xy_vt.animate.set_value(self.xy_vt.get_value() - self.max_y - 1)

    def add_value_to_xy(self, value = 1):
        return self.xy_vt.animate.set_value(self.xy_vt.get_value() + value)

    def transform_positive_dots(self, positive_table: MathTable) -> list:
        anims = self.transform_dots(positive_table)
        anims = AnimationGroup(*anims, lag_ratio=0.3)
        return anims

    def transform_negative_dots(self, negative_table: MathTable):
        anims = self.transform_dots(negative_table, False)
        anims = AnimationGroup(*anims, lag_ratio=0.3)
        return anims

    def transform_dots(self, table: MathTable, positive_half: bool = True):
        """Don't Use Explicitly"""
        anims = []
        for i in range(self.max_x + 1):
            table_row = VGroup(*[table.get_entries((i + 2, j)) for j in [1, 2]])
            dot = self.dots[i + ((self.max_x + 1) * int(positive_half))]
            anims.append(ReplacementTransform(table_row, dot))

        return anims

    def mobjects(self):
        return VGroup(
            self.graph,
            *self.dots,
            *self.lines,
            self.labels,
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
    
    def change_coordinate(self):
        return FadeOut(self.graph.coordinate_labels)

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

            dot = Dot(self.graph.c2p(i, self.decimal_of_complement(i)), color=dot_color)
            dots.append(dot)

        return dots

    def get_lines(self):
        positive_line = self.graph.plot(
            self.decimal_of_complement,
            x_range=[0, self.max_x],
            color=self.positive_color,
        )
        negative_line = self.graph.plot(
            lambda x: self.decimal_of_complement(x, True),
            x_range=[-self.max_x, 0],
            color=self.negative_color,
        )

        lines = [positive_line, negative_line]
        return lines

    def show_dots(self):
        return FadeIn(*self.dots)

    def show_lines(self):
        return FadeIn(*self.lines)

    def show_graph(self):
        return AnimationGroup(Write(self.graph), Write(self.labels))

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

    def show_value_indicators(self):
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

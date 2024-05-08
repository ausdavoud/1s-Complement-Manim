from manim import *
from manim_slides import Slide


class When(Slide):
    def construct(self):
        xy_in_N = MathTex(r"x, y \in \mathbb{N}").scale(2)
        x_plus_y = MathTex("x + y").scale(2)
        x_minus_y = MathTex("x - y").scale(2)
        minus_x_minus_y = MathTex("-x-y").scale(2)
        possible_ways = (
            VGroup(x_plus_y, x_minus_y, minus_x_minus_y)
            .arrange(DOWN, buff=1.4)
            .shift(0.75 * RIGHT)
        )
        minus_x_minus_y.align_to(x_minus_y, LEFT)
        brace = Brace(possible_ways, LEFT).shift(0.4 * LEFT)

        self.play(Write(xy_in_N))
        self.next_slide()

        self.play(xy_in_N.animate.shift(3.5 * LEFT))
        self.play(Write(brace))
        self.play(Write(x_plus_y))
        self.next_slide()

        self.play(Write(x_minus_y))
        self.next_slide()

        self.play(Write(minus_x_minus_y))
        self.next_slide()

        eg_plus = (
            MathTex("1 + 2", color=GRAY)
            .scale(0.75)
            .next_to(x_plus_y, RIGHT)
            .to_edge(RIGHT)
            .shift(LEFT)
        )
        eg_minus = (
            MathTex("3-4, 4 - 2", color=GRAY)
            .scale(0.75)
            .next_to(x_minus_y, RIGHT)
            .to_edge(RIGHT)
            .shift(LEFT)
        )
        eg_minus_minus = (
            MathTex("-5 - 6", color=GRAY)
            .scale(0.75)
            .next_to(minus_x_minus_y, RIGHT)
            .to_edge(RIGHT)
            .shift(LEFT)
        )

        self.play(Write(eg_plus))
        self.play(Write(eg_minus))
        self.play(Write(eg_minus_minus))
        self.next_slide()

        anims = AnimationGroup(
            FadeOut(
                xy_in_N,
                brace,
                x_minus_y,
                minus_x_minus_y,
                eg_plus,
                eg_minus,
                eg_minus_minus,
            ),
            x_plus_y.animate.move_to(ORIGIN),
        )

        self.play(anims)

        self.next_slide()

        self.play(x_plus_y.animate.scale(0.5).to_edge(UR))

        


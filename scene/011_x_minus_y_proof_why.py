from manim import *  # noqa
from manim_slides import Slide


class XMinusYProofWhy(Slide):
    def construct(self):
        """
        x - y = x + 2^n - 1 - y
        @ - > x >= y + 1: x + 2^n - 1 - y - 2^n + 1 = x - y
         |_ > x <= y: 2^n - 1 - (x + 2^n - 1 - y) = -x + y = -(-x + y) = x - y
        """
        title = (
            Tex("1's Complement")
            .scale(3 / 4)
            .to_edge(UL)
            .set_color_by_gradient(YELLOW, RED)
        )

        subtitle = (
            Tex("$x - y$: Proof")
            .scale(3 / 4)
            .to_edge(UR)
            .set_color_by_gradient(WHITE, GRAY)
        )
        self.add(title, subtitle)

        how_title = Tex("How to fix it?").scale(2)
        self.play(Write(how_title))

        self.next_slide()

        self.play(Unwrite(how_title))

        equation_1 = MathTex("x - y", "=", "x + 2^n - 1 - y").scale(1)
        equation_1[0].set_color(GREEN)

        self.play(Write(equation_1[0]))
        self.play(Write(equation_1[1:]))

        equation_2 = MathTex("x + 2^n - 1 - y").scale(1).to_edge(LEFT)

        self.next_slide()
        self.play(TransformMatchingTex(equation_1, equation_2))

        arrow_top = Arrow(
            equation_2.get_right(), equation_2.get_right() + UP + 0.7 * RIGHT
        )
        arrow_down = Arrow(
            equation_2.get_right(), equation_2.get_right() + DOWN + 0.7 * RIGHT
        )

        self.play(Write(arrow_top), Write(arrow_down))

        condition_top = (
            MathTex("x \ge y + 1: ", color=YELLOW).next_to(arrow_top.get_tip(), RIGHT).shift(0.5 * UP)
        )
        condition_down = (
            MathTex("x \le y: ", color=YELLOW).next_to(arrow_down.get_tip(), RIGHT).shift(0.5 * DOWN)
        )

        self.play(Write(condition_top), Write(condition_down))
        self.next_slide()

        equation_top_1 = MathTex(
            "x", "+", "2^n", "-", "1", "- y", "-", "2^n", " +", "1"
        ).next_to(condition_top, RIGHT)
        equation_top_2 = MathTex("=", "x", "-", "y").next_to(equation_top_1, RIGHT)
        equation_top_2[1:].set_color(GREEN)
        self.play(Write(equation_top_1[:5]))
        self.next_slide()
        self.play(Write(equation_top_1[5:]))

        self.next_slide()

        self.play(
            Indicate(equation_top_1[1:5], color=GREEN),
            Indicate(equation_top_1[6:], color=RED),
        )

        self.play(Write(equation_top_2))

        equation_down_1 = MathTex("x +", "2^n - 1", "- y").next_to(
            condition_down, RIGHT
        )
        equation_down_2 = MathTex(
            "2^n", "- 1", "- (", "x + ", "2^n - 1", "- y", ")"
        ).next_to(condition_down, RIGHT)
        equation_down_3 = MathTex("= - x + y").next_to(equation_down_2)

        self.next_slide()

        self.play(Write(equation_down_1))
        self.next_slide()

        self.play(TransformMatchingTex(equation_down_1, equation_down_2))

        self.next_slide()
        
        self.play(
            Indicate(equation_down_2[:2], color=GREEN),
            Indicate(equation_down_2[4], color=RED),
        )
        self.play(Write(equation_down_3))

        equation_down_4 = (
            MathTex("= -(- x + y) =", " x - y")
            .next_to(equation_down_2, DOWN)
            .align_to(equation_down_2, LEFT)
        )
        equation_down_4[1].set_color(GREEN)

        self.next_slide()

        self.play(Write(equation_down_4))

        self.next_slide()
        self.play(
            FadeOut(
                equation_2,
                arrow_top,
                condition_top,
                equation_top_1,
                equation_top_2,
                arrow_down,
                condition_down,
                equation_down_2,
                equation_down_3,
                equation_down_4,
            )
        )

        next_subtitle = Tex("$-x - y$: Plane").scale(3)
        self.play(ReplacementTransform(subtitle, next_subtitle))

        self.wait(2)

        self.play(next_subtitle.animate.scale(1/4).to_edge(UR).set_color_by_gradient(WHITE, GRAY))


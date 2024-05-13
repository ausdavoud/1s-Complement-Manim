from manim import *  # noqa
from manim_slides import Slide


class MinusXMinusYProof(Slide):
    def construct(self):
        """
        - x - y = 2^n - 1 - x + 2^n - 1 - y
                = Show(It overflows!)
                = 2^n - 1 - x + 2^n - 1 - y - 2^n + 1
                = 2^n - 1 -x - y
                = Show(Its negative!)
                = 2^n - 1 - (2^n - 1 - x - y)
                = + x + y
                = - (+ x + y)
                = - x - y
        """
        title = (
            Tex("1's Complement")
            .scale(3 / 4)
            .to_edge(UL)
            .set_color_by_gradient(YELLOW, RED)
        )

        subtitle = (
            Tex("$-x - y$: Proof")
            .scale(3 / 4)
            .to_edge(UR)
            .set_color_by_gradient(WHITE, GRAY)
        )

        self.add(title, subtitle)

        equation_1 = MathTex("-", "x", "-", "y").scale(1)
        equation_2 = MathTex(
            "-",
            "x",
            "-",
            "y",
            "=",
            "2^n",
            "-",
            "1",
            "-",
            "x",
            "+",
            "2^n",
            "-",
            "1",
            "-",
            "y",
        ).scale(1)

        self.play(Write(equation_1))

        self.play(equation_1.animate.shift(4 * LEFT))

        equation_2.align_to(equation_1, LEFT)

        self.play(TransformMatchingTex(equation_1, equation_2))

        self.next_slide()

        self.play(Indicate(equation_2[5:8]), Indicate(equation_2[11:14]))

        self.next_slide()

        overflow = Tex("It overflows!").scale(2)

        self.play(FadeOut(equation_2))
        self.play(Write(overflow))
        self.play(Unwrite(overflow))
        self.play(FadeIn(equation_2))

        equation_3 = (
            MathTex(
                "=",
                "2^n",
                "-",
                "1",
                "-",
                "x",
                "+",
                "2^n",
                "-",
                "1",
                "-",
                "y",
                "-",
                "2^n",
                "+",
                "1",
            )
            .scale(1)
            .next_to(equation_2, DOWN)
            .align_to(equation_2[4], LEFT)
        )

        self.play(Write(equation_3))

        self.play(Indicate(equation_3[-4:]))

        self.next_slide()

        self.play(
            Indicate(equation_3[6:10], color=GREEN),
            Indicate(equation_3[12:], color=RED),
        )

        self.play(VGroup(equation_2, equation_3).animate.shift(2 * UP))

        equation_4 = (
            MathTex("=", "2^n", "-", "1", "-", "x", "-", "y")
            .scale(1)
            .next_to(equation_3, DOWN)
            .align_to(equation_3[0], LEFT)
        )

        self.play(Write(equation_4))
        self.next_slide()

        negative = Tex("It's negative!").scale(2)

        self.play(FadeOut(equation_2, equation_3, equation_4))
        self.play(Write(negative))
        self.play(Unwrite(negative))
        self.play(FadeIn(equation_2, equation_3, equation_4))

        equation_5 = (
            MathTex(
                "=", "2^n", "-", "1", "-", "(", "2^n", "-", "1", "-", "x", "-", "y", ")"
            )
            .scale(1)
            .next_to(equation_4, DOWN)
            .align_to(equation_4[0], LEFT)
        )

        self.play(Write(equation_5))
        self.next_slide()

        self.play(
            Indicate(equation_5[1:4], color=GREEN), Indicate(equation_5[6:9], color=RED)
        )

        equation_6 = (
            MathTex("=", "+", "x", "+", "y")
            .scale(1)
            .next_to(equation_5, DOWN)
            .align_to(equation_5[0], LEFT)
        )

        self.play(Write(equation_6))

        equation_7 = (
            MathTex("=", "-", "(", "+", "x", "+", "y", ")")
            .scale(1)
            .next_to(equation_6, DOWN)
            .align_to(equation_6[0], LEFT)
        )

        self.next_slide()

        self.play(Write(equation_7))

        equation_8 = (
            MathTex("=", "-", "x", "-", "y", "")
            .scale(1)
            .next_to(equation_7, DOWN)
            .align_to(equation_7[0], LEFT)
        )

        self.play(Write(equation_8))

        self.next_slide()

        self.play(
            FadeOut(
                equation_2,
                equation_3,
                equation_4,
                equation_5,
                equation_6,
                equation_7,
                equation_8,
            )
        )


        next_subtitle = Tex("Thank you!").scale(3)
        self.play(ReplacementTransform(subtitle, next_subtitle))

        self.wait(2)

        self.play(next_subtitle.animate.scale(1/4).to_edge(UR).set_color_by_gradient(WHITE, GRAY).set_opacity(0), FadeOut(title))

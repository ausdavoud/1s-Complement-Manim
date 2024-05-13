from manim import * # noqa
from manim_slides import Slide

class XMinusYProofWhen(Slide):
    def construct(self):
        """
        x - y >= 2^n
        x + (-y) = x + (2^n - 1 - y)
        x + 2^n - 1 - y >= 2^n
        indicate and delete 2^n
        x - 1 -y >= 0
        x >= y + 1
        """
        title = Tex("1's Complement").scale(3/4).to_edge(UL).set_color_by_gradient(YELLOW, RED)

        subtitle = (
            Tex("$x - y$: Proof")
            .scale(3 / 4)
            .to_edge(UR)
            .set_color_by_gradient(WHITE, GRAY)
        )
        self.add(title, subtitle)

        when_title = Tex("When does overflow occur?").scale(1.5)
        self.play(Write(when_title))
        self.next_slide()
        self.play(FadeOut(when_title))

        ge_sign = MathTex("\ge").scale(1.5)
        equation_1_l = MathTex("x", "-", "y").scale(1.5).next_to(ge_sign, LEFT)
        equation_1_r = MathTex("2^n").scale(1.5).next_to(ge_sign, RIGHT)
        
        equation_2_l = MathTex("x", "+", "(", "-", "y", ")").scale(1.5).next_to(ge_sign, LEFT)

        equation_3_l = MathTex("x", "+", "(", "2^n", "-", "1", "-", "y", ")").scale(1.5).next_to(ge_sign, LEFT)


        self.play(Write(equation_1_l) , Write(ge_sign), Write(equation_1_r))
        self.next_slide()
        self.play(TransformMatchingTex(equation_1_l, equation_2_l))
        self.next_slide()
        self.play(TransformMatchingTex(equation_2_l, equation_3_l))

        self.next_slide()

        self.play(Indicate(equation_3_l[3], color=RED), Indicate(equation_1_r, color=RED))


        equation_4_l = MathTex("x", "+", "(", "-", "1", "-", "y", ")").scale(1.5).next_to(ge_sign, LEFT)
        equation_4_r = MathTex("0").scale(1.5).next_to(ge_sign, RIGHT)

        self.next_slide()

        self.play(TransformMatchingTex(equation_3_l, equation_4_l), FadeOut(equation_1_r), FadeIn(equation_4_r))
        self.next_slide()

        equation_4_l_without_paranthesis = MathTex("x", "-", "1", "-", "y").scale(1.5).next_to(ge_sign, LEFT)
        self.play(TransformMatchingTex(equation_4_l, equation_4_l_without_paranthesis))

        equation_5_l = MathTex("x").scale(2).next_to(ge_sign, LEFT)
        equation_5_r = MathTex("y", "+", "1").scale(2).next_to(ge_sign, RIGHT)
        self.next_slide()

        self.play(TransformMatchingTex(VGroup(equation_4_l_without_paranthesis, equation_4_r), VGroup(equation_5_l, equation_5_r)))


        self.next_slide()
        self.play(FadeOut(equation_5_l, equation_5_r, ge_sign))

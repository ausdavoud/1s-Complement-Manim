from manim import * #noqa
from manim_slides import Slide

class XPlusYProof(Slide):
    def construct(self):
        """
        max(x) = 2^n-1 -1 
        2^n-1 -1 + 2^n-1 -1 = 2(2^n-1) -2 
        2^n - 2 < 2^n
        """
        title = Tex("1's Complement").scale(3/4).to_edge(UL).set_color_by_gradient(YELLOW, RED)

        subtitle = (
            Tex("$x + y$: Proof")
            .scale(3 / 4)
            .to_edge(UR)
            .set_color_by_gradient(WHITE, GRAY)
        )
        self.add(title, subtitle)

        max_x = MathTex("Max(x) = 2^{n-1} - 1:", color=LIGHT_GREY).shift(UP + 2*LEFT)


        proof_line_1 = MathTex("2^{n-1} - 1", " + 2^{n-1} - 1", "=", "2(2^{n-1}) - 2").align_to(max_x, LEFT)
        proof_line_2 = MathTex("= 2^n - 2 < 2^n").shift(DOWN).align_to(proof_line_1[2], LEFT)

        
        self.play(Write(max_x))
        self.next_slide()
        self.play(Write(proof_line_1[0]))
        self.play(Write(proof_line_1[1]))
        self.play(Write(proof_line_1[2]), Write(proof_line_1[3]))
        self.next_slide()
        self.play(Write(proof_line_2))
        self.next_slide()

        self.play(FadeOut(max_x, proof_line_1, proof_line_2))

        x_minus_y = MathTex("x", "-", "y").scale(2)
        # self.play(ReplacementTransform(Corner, x_minus_y))
        self.play(ReplacementTransform(subtitle, x_minus_y))


        self.next_slide()
        minus_y_plus_x = MathTex("-", "y", "+", "x").scale(2)

        self.play(TransformMatchingTex(x_minus_y, minus_y_plus_x))

        self.next_slide()

        self.play(TransformMatchingTex(minus_y_plus_x, x_minus_y))

        self.play(ReplacementTransform(subtitle, x_minus_y))

        self.wait(2)

        next_subtitle = Tex("$x - y$: Plane").scale(1/2).to_edge(UR).set_color_by_gradient(WHITE, GRAY)

        self.play(ReplacementTransform(x_minus_y, next_subtitle))

        

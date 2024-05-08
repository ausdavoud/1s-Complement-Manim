from manim import * #noqa
from manim_slides import Slide

class XPlusYProof(Slide):
    def construct(self):
        """
        max(x) = 2^n-1 -1 
        2^n-1 -1 + 2^n-1 -1 = 2(2^n-1) -2 
        2^n - 2 < 2^n
        """
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
        self.play(Write(x_minus_y))


        self.next_slide()
        minus_y_plus_x = MathTex("-", "y", "+", "x").scale(2)

        self.play(TransformMatchingTex(x_minus_y, minus_y_plus_x))

        self.next_slide()

        self.play(FadeOut(minus_y_plus_x))

        

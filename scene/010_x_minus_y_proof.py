from manim import * # noqa
from manim_slides import Slide

class XMinusYProof(Slide):
    def construct(self):
        """
        x - y >= 2^n
        x + (-y) = x + (2^n - 1 - y)
        x + 2^n - 1 - y >= 2^n
        indicate and delete 2^n
        x - 1 -y >= 0
        x >= y + 1

        x - y = x + 2^n - 1 - y
              = x + 2^n - 1 - y - 2^n + 1 = x - y
        """
        max_x = MathTex("Max(x) = 2^{n-1} - 1:", color=LIGHT_GREY).shift(UP + 2*LEFT)

        proof_line_1 = MathTex("2^{n-1} - 1", " + 2^{n-1} - 1", "=", "2(2^{n-1}) - 2").align_to(max_x, LEFT)
        proof_line_2 = MathTex("= 2^n - 2 < 2^n").shift(DOWN).align_to(proof_line_1[2], LEFT) # noqa
        
        self.play(Write(max_x))
        self.next_slide()
        self.play(Write(proof_line_1[0]))
        self.play(Write(proof_line_1[1]))
        self.play(Write(proof_line_1[2]), Write(proof_line_1[3]))
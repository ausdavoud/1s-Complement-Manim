import config
from manim import *
from manim_slides import Slide

class Intro(Slide):
    def construct(self):
        title = Tex(r"1's Complement").scale(3).set_color_by_gradient(YELLOW, RED)
        by = Tex("By: Davoud Nosrati").next_to(title, DOWN, 1)
        self.play(Write(title))
        self.play(Write(by))

        self.next_slide()

        section_title = Tex("Example").scale(3)
        self.play(
            title.animate.scale(1/4)
            .to_edge(UP + LEFT),
            ReplacementTransform(by, section_title),
            
        )

        self.wait(1)

        self.play(
            section_title.animate.scale(1/4).to_edge(
                UP + RIGHT
            ).set_color_by_gradient(WHITE, GRAY)
        )

        self.wait(3)

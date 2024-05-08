import config
from manim import *
from manim_slides import Slide


class Intro(Slide):
    def construct(self):
        title = Tex(r"1's Complement", color=config.TITLE_COLOR).scale(
            config.TITLE_SCALE
        )
        by = Tex("By: Davoud Nosrati", color=config.SECTION_TITLE_COLOR).next_to(
            title, DOWN, 1
        )
        self.play(Write(title))
        self.play(Write(by))

        self.wait(1)

        section_title = Tex("Example", color=config.SECTION_TITLE_COLOR).scale(
            config.SECTION_TITLE_SCALE
        )
        self.play(
            title.animate.scale(config.TITLE_CORNER_SCALE)
            .to_edge(UP + LEFT)
            .align_to(title),
            ReplacementTransform(by, section_title),
        )

        self.wait(1)

        self.play(
            section_title.animate.scale(config.SECTION_TITLE_CORNER_SCALE).to_edge(
                UP + RIGHT
            )
        )

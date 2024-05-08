from manim import *
from manim_slides import Slide


class Complement(Slide):
    def construct(self):
        complement = MathTex("Complement").scale(4)
        self.play(Write(complement))

        self.next_slide()

        self.play(complement.animate.scale(0.25).to_edge(UR))

        number_45 = MathTex("(", "1", "0", "1", "1", "0", "1", ")_{_2}").scale(2)

        self.play(Write(number_45))

        self.next_slide()

        self.play(number_45.animate.shift(UP * 1.5))

        number_45_complement = MathTex(
            "(", "0", "1", "0", "0", "1", "0", ")_{_2}"
        ).scale(2)

        complement_line = Line(
            number_45[0].get_bottom(), number_45[-1].get_bottom()
        ).shift(DOWN * 0.3)

        complementation = AnimationGroup(
            TransformFromCopy(number_45[-2], number_45_complement[-2]),
            TransformFromCopy(number_45[-3], number_45_complement[-3]),
            TransformFromCopy(number_45[-4], number_45_complement[-4]),
            TransformFromCopy(number_45[-5], number_45_complement[-5]),
            TransformFromCopy(number_45[-6], number_45_complement[-6]),
            TransformFromCopy(number_45[-7], number_45_complement[-7]),
            lag_ratio=0.3,
        )
        self.play(complementation)

        self.next_slide()

        self.play(
            Create(complement_line),
            Write(number_45_complement[-1]),
            Write(number_45_complement[0]),
        )

        self.play(
            VGroup(number_45, number_45_complement, complement_line).animate.shift(
                DOWN * 1.5
            )
        )

        number_full_31 = MathTex("(111111", ")_{_2}").scale(2).shift(UP * 1.25)
        negative_sign = MathTex("-").scale(2).next_to(number_45, LEFT)

        self.play(Write(number_full_31), Write(negative_sign))

        self.next_slide()

        binary_group = VGroup(
            number_full_31,
            negative_sign,
            number_45,
            complement_line,
            number_45_complement,
        )

        self.play(binary_group.animate.shift(LEFT * 2.5))

        vertical_separator_line = Line(
            number_full_31[-1].get_top(),
            number_45_complement[-1].get_bottom(),
            color=YELLOW,
        ).shift(RIGHT)

        self.play(Create(vertical_separator_line))

        number_full_31_decimal = (
            MathTex("2^n - 1").scale(2).next_to(number_full_31, RIGHT)
        )
        number_placeholder = MathTex("Number").scale(1.5).next_to(number_45, RIGHT)
        negative_sign_decimal = MathTex("-").scale(2).next_to(number_placeholder, LEFT)
        first_complement = (
            MathTex("1's \; Complement")
            .scale(1.25)
            .next_to(number_45_complement, RIGHT)
        )
        complement_line_decimal = Line(
            first_complement.get_left(), first_complement.get_right()
        ).next_to(complement_line, RIGHT)

        decimal_group = VGroup(
            number_full_31_decimal,
            number_placeholder,
            negative_sign_decimal,
            complement_line_decimal,
            first_complement,
        ).shift(RIGHT * 2)

        self.play(
            AnimationGroup(
                TransformFromCopy(number_full_31, number_full_31_decimal),
                TransformFromCopy(number_45, number_placeholder),
                Write(negative_sign_decimal),
                TransformFromCopy(number_45_complement, first_complement),
                Write(complement_line_decimal),
                lag_ratio=0.3,
            )
        )

        self.next_slide()

        self.play(FadeOut(binary_group, vertical_separator_line))

        self.play(decimal_group.animate.shift(LEFT * 3.5))

        self.next_slide()

        self.play(FadeOut(decimal_group))

        self.next_slide()

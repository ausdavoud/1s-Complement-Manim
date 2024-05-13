from manim import *
from manim_slides import Slide


class Example(Slide):
    def construct(self):
        title = (
            Tex("1's Complement")
            .scale(3 / 4)
            .to_edge(UL)
            .set_color_by_gradient(YELLOW, RED)
        )
        subtitle = (
            Tex("Example").scale(3 / 4).to_edge(UR).set_color_by_gradient(WHITE, GRAY)
        )
        self.add(title, subtitle)

        five = Integer(5).scale(2).shift(1.5 * UP).set_color(GREEN)
        three = Integer(3).scale(2).set_color(RED)
        negative_sign = MathTex("-").scale(2).next_to(three, LEFT).set_color(RED)
        horizontal_line = Line(negative_sign.get_left(), three.get_right()).shift(
            0.8 * DOWN
        )
        question_mark = MathTex("?").scale(2).next_to(three, 3.5 * DOWN)

        self.play(
            Write(five),
            Write(negative_sign),
            Write(three),
            Create(horizontal_line),
        )
        self.play(Write(question_mark))

        # Moving things to LEFT

        decimal_addition = VGroup(
            five,
            three,
            negative_sign,
            horizontal_line,
            question_mark,
        )

        self.play(decimal_addition.animate.shift(4 * LEFT))

        separator_line = DashedLine(
            start=five.get_top(), end=question_mark.get_bottom(), color=DARK_GRAY
        ).shift(1.2 * RIGHT)
        self.play(Create(separator_line))

        five_in_binary = (
            MathTex(r"(", "0", "1", "0", "1", r")_{_{1sC}}")
            .scale(2)
            .shift(1.5 * UP + RIGHT)
            .set_color(GREEN)
        )
        neg_three_in_binary = (
            MathTex(r"(", "1", "1", "0", "0", r")_{_{1sC}}")
            .set_color(RED)
            .scale(2)
            .shift(RIGHT)
        )
        plus_sign = MathTex("+").scale(2).next_to(neg_three_in_binary, LEFT)
        binary_horizontal_line = Line(
            plus_sign.get_left(), neg_three_in_binary.get_right()
        ).shift(0.8 * DOWN)

        self.play(
            TransformFromCopy(five, five_in_binary),
        )

        self.play(
            TransformFromCopy(
                VGroup(three, negative_sign), VGroup(neg_three_in_binary, plus_sign)
            ),
        )
        self.play(
            Create(binary_horizontal_line),
        )

        # Start Adding Bit by Bit
        result_first_bit = (
            MathTex("1").scale(2).move_to(neg_three_in_binary[4]).shift(1.7 * DOWN)
        )
        result_second_bit = (
            MathTex("0").scale(2).move_to(neg_three_in_binary[3]).shift(1.7 * DOWN)
        )
        result_third_bit = (
            MathTex("0").scale(2).move_to(neg_three_in_binary[2]).shift(1.7 * DOWN)
        )
        result_first_carry_bit = (
            MathTex("1").scale(1).move_to(five_in_binary[1]).shift(0.7 * UP)
        )
        result_forth_bit = (
            MathTex("0").scale(2).move_to(neg_three_in_binary[1]).shift(1.7 * DOWN)
        )
        result_fifth_bit = (
            MathTex("1").scale(2).next_to(result_forth_bit, LEFT).shift(0.13 * RIGHT)
        )

        self.next_slide()

        anims = AnimationGroup(
            Indicate(five_in_binary[4]),
            Indicate(neg_three_in_binary[4]),
            Write(result_first_bit),
            lag_ratio=0.3,
        )

        self.play(anims)

        anims = AnimationGroup(
            Indicate(five_in_binary[3]),
            Indicate(neg_three_in_binary[3]),
            Write(result_second_bit),
            lag_ratio=0.3,
        )

        self.play(anims)

        anims = AnimationGroup(
            Indicate(five_in_binary[2]),
            Indicate(neg_three_in_binary[2]),
            Write(result_third_bit),
            Write(result_first_carry_bit),
            lag_ratio=0.3,
        )

        self.play(anims)

        anims = AnimationGroup(
            Indicate(result_first_carry_bit),
            Indicate(five_in_binary[1]),
            Indicate(neg_three_in_binary[1]),
            lag_ratio=0.3,
        )

        self.play(anims)

        anims = AnimationGroup(
            Write(result_forth_bit), Write(result_fifth_bit), lag_ratio=0.3
        )

        self.play(anims)

        add_end_carry_plus_sign = (
            MathTex("+").scale(2).move_to(result_fifth_bit).shift(DOWN + 0.25 * LEFT)
        )

        self.next_slide()

        self.play(
            result_fifth_bit.animate.move_to(result_first_bit).shift(DOWN),
            Write(add_end_carry_plus_sign),
        )

        anims = [
            FadeOut(add_end_carry_plus_sign, result_fifth_bit),
            result_first_bit.animate.move_to(result_second_bit),
            result_second_bit.animate.move_to(result_first_bit),
        ]

        self.wait(1)

        self.play(*anims)

        left_parenthesis = (
            MathTex(r"(").scale(2).move_to(result_forth_bit).shift(0.45 * LEFT)
        )
        right_parenthesis = (
            MathTex(r")_{_{1sC}}")
            .scale(2)
            .move_to(result_first_bit)
            .align_to(left_parenthesis, UP)
            .align_to(neg_three_in_binary, RIGHT)
        )

        self.play(Write(left_parenthesis), Write(right_parenthesis))

        two = MathTex("2").scale(2).move_to(question_mark)
        self.play(
            TransformFromCopy(
                VGroup(
                    result_first_bit,
                    result_second_bit,
                    result_third_bit,
                    result_forth_bit,
                ),
                two,
            ),
            FadeOut(question_mark),
        )

        self.next_slide()

        self.play(
            FadeOut(
                five,
                negative_sign,
                three,
                horizontal_line,
                two,
                five_in_binary,
                plus_sign,
                neg_three_in_binary,
                binary_horizontal_line,
                result_first_bit,
                result_second_bit,
                result_third_bit,
                result_forth_bit,
                left_parenthesis,
                right_parenthesis,
                separator_line,
                result_first_carry_bit       
            )
        )

        complement = Tex("Complement").scale(3)
        self.play(ReplacementTransform(subtitle, complement))
        self.wait(2)
        self.play(
            complement.animate.scale(1 / 4)
            .to_edge(UR)
            .set_color_by_gradient(WHITE, GRAY)
        )

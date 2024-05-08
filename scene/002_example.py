from manim import *
from manim_slides import Slide

class Example(Slide):
    def construct(self):
        five = Integer(5, font_size=100).shift(1.5 * UP)
        three = Integer(3, font_size=100)
        negative_sign = MathTex("-", font_size=100).next_to(three, LEFT)
        horizontal_line = Line(negative_sign.get_left(), three.get_right()).shift(
            0.8 * DOWN
        )
        question_mark = MathTex("?", font_size=100).next_to(three, 3.5 * DOWN)
        # two = Integer(2, font_size=100).move_to(question_mark)

        self.play(
            Write(five),
            Write(negative_sign),
            Write(three),
            Create(horizontal_line),
        )
        self.play(Write(question_mark))

        self.next_slide()

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
            start=five.get_top(), end=question_mark.get_bottom()
        ).shift(RIGHT)
        self.play(Create(separator_line))

        five_in_binary = MathTex(
            r"(", "0", "1", "0", "1", r")_{_{1sC}}", font_size=100
        ).shift(1.5 * UP + RIGHT)
        neg_three_in_binary = MathTex(
            r"(", "1", "1", "0", "0", r")_{_{1sC}}", font_size=100
        ).shift(RIGHT)
        plus_sign = MathTex("+", font_size=100).next_to(neg_three_in_binary, LEFT)
        binary_horizontal_line = Line(
            plus_sign.get_left(), neg_three_in_binary.get_right()
        ).shift(0.8 * DOWN)

        self.play(
            TransformFromCopy(five, five_in_binary),
        )

        self.next_slide()


        self.play(
            TransformFromCopy(
                VGroup(three, negative_sign), VGroup(neg_three_in_binary, plus_sign)
            ),
        )
        self.play(
            Create(binary_horizontal_line),
        )

        self.next_slide()


        # Start Adding Bit by Bit
        result_first_bit = (
            MathTex("1", font_size=100)
            .move_to(neg_three_in_binary[4])
            .shift(1.7 * DOWN)
        )
        result_second_bit = (
            MathTex("0", font_size=100)
            .move_to(neg_three_in_binary[3])
            .shift(1.7 * DOWN)
        )
        result_third_bit = (
            MathTex("0", font_size=100)
            .move_to(neg_three_in_binary[2])
            .shift(1.7 * DOWN)
        )
        result_first_carry_bit = (
            MathTex("1", font_size=70).move_to(five_in_binary[1]).shift(0.7 * UP)
        )
        result_forth_bit = (
            MathTex("0", font_size=100)
            .move_to(neg_three_in_binary[1])
            .shift(1.7 * DOWN)
        )
        result_fifth_bit = (
            MathTex("1", font_size=100)
            .next_to(result_forth_bit, LEFT)
            .shift(0.13 * RIGHT)
        )

        self.play(Indicate(five_in_binary[4]))
        
        self.play(Indicate(neg_three_in_binary[4]))

        self.play(Write(result_first_bit))

        self.next_slide()

        self.play(Indicate(five_in_binary[3]))
        self.play(Indicate(neg_three_in_binary[3]))

        self.play(Write(result_second_bit))

        self.next_slide()

        self.play(Indicate(five_in_binary[2]))
        self.play(Indicate(neg_three_in_binary[2]))

        self.play(Write(result_third_bit))
        self.play(Write(result_first_carry_bit))
        self.next_slide()

        self.play(Indicate(result_first_carry_bit))
        self.play(Indicate(five_in_binary[1]))
        self.play(Indicate(neg_three_in_binary[1]))

        self.play(Write(result_forth_bit))
        self.play(Write(result_fifth_bit))

        self.next_slide()

        add_end_carry_plus_sign = (
            MathTex("+", font_size=100)
            .move_to(result_fifth_bit)
            .shift(DOWN + 0.25 * LEFT)
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

        self.next_slide()

        self.play(*anims)

        left_parenthesis = (
            MathTex(r"(", font_size=100).move_to(result_forth_bit).shift(0.45 * LEFT)
        )
        right_parenthesis = (
            MathTex(r")_{_{1sC}}", font_size=100)
            .move_to(result_first_bit)
            .align_to(left_parenthesis, UP)
            .align_to(neg_three_in_binary, RIGHT)
        )

        self.play(Write(left_parenthesis), Write(right_parenthesis))

        self.next_slide()

        two = MathTex("2", font_size=100).move_to(question_mark)
        self.play(
            TransformFromCopy(
                VGroup(
                    result_first_bit,
                    result_second_bit,
                    result_third_bit,
                    result_forth_bit,
                ),
                two
            ),
            FadeOut(question_mark)
        )

        self.next_slide()

        self.wait(5)

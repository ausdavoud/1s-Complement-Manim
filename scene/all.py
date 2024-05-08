from manim import *

from manim_slides import Slide


class All(Slide):
    def construct(self):

# class Intro:
#     def construct(self):
        title = Tex(r"1's Complement").scale(3)
        by = Tex("By: Davoud Nosrati").next_to(title, DOWN, 1)
        self.play(Write(title))
        self.play(Write(by))


# class Example(Slide):
#     def construct(self):

        self.next_slide()

        # New
        example = Tex("Example").scale(4)
        anims = [
            title.animate.scale(1/3).to_edge(UP + LEFT),
            ReplacementTransform(by, example),
        ]
        self.play(*anims)

        # self.next_slide()

        self.play(example.animate.scale(0.25).to_edge(UP + RIGHT))

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

        self.play(AnimationGroup(Indicate(five_in_binary[4]), Indicate(neg_three_in_binary[4]), lag_ratio=0.5))
        

        self.play(Write(result_first_bit))

        self.next_slide()

        # self.play(Indicate(five_in_binary[3]))
        # self.play(Indicate(neg_three_in_binary[3]))
        self.play(AnimationGroup(Indicate(five_in_binary[3]), Indicate(neg_three_in_binary[3]), lag_ratio=0.5))


        self.play(Write(result_second_bit))

        self.next_slide()

        # self.play(Indicate(five_in_binary[2]))
        # self.play(Indicate(neg_three_in_binary[2]))
        self.play(AnimationGroup(Indicate(five_in_binary[2]), Indicate(neg_three_in_binary[2]), lag_ratio=0.5))

        self.play(Write(result_third_bit))
        self.play(Write(result_first_carry_bit))
        self.next_slide()

        # self.play(Indicate(result_first_carry_bit))
        # self.play(Indicate(five_in_binary[1]))
        # self.play(Indicate(neg_three_in_binary[1]))
        self.play(AnimationGroup(Indicate(result_first_carry_bit), Indicate(five_in_binary[1]) ,Indicate(neg_three_in_binary[1]), lag_ratio=0.5))


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

        example_last_objects = VGroup(
            five, negative_sign, three, horizontal_line, two,
            separator_line,
            plus_sign, five_in_binary, neg_three_in_binary, binary_horizontal_line, left_parenthesis, right_parenthesis,
            result_first_bit, result_second_bit, result_third_bit, result_forth_bit, result_first_carry_bit,
        )
        self.play(FadeOut(example_last_objects))


# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
# class Complement(Slide):
#     def construct(self):
        

        complement = Tex("Complement").scale(4)
        self.play(ReplacementTransform(example, complement))

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
        number_placeholder = Tex("Number").scale(1.5).next_to(number_45, RIGHT)
        negative_sign_decimal = MathTex("-").scale(2).next_to(number_placeholder, LEFT)
        first_complement = (
            Tex("1's Complement")
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

        # --------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------


# class AddCarry(Slide):
#     def construct(self):
#         pass
        carry = Tex("Carry").scale(4)

        # Animation Transform
        self.play(ReplacementTransform(complement, carry))

        self.next_slide()
        # Title to UR
        self.play(carry.animate.scale(0.25).to_edge(UR))

        five_in_binary = MathTex("(0101)_{_{1sC}}").scale(2).shift(3 * UP)
        neg_three_in_binary = (
            MathTex("(110", "0", ")_{_{1sC}}").scale(2).next_to(five_in_binary, DOWN)
        )
        plus_sign = MathTex("+").scale(2).next_to(neg_three_in_binary, LEFT)
        addition_horizontal_line = Line(
            plus_sign.get_left(), neg_three_in_binary.get_right()
        ).next_to(VGroup(neg_three_in_binary, plus_sign), DOWN)
        result_in_binary = (
            MathTex("1", "000", "1")
            .scale(2)
            .next_to(addition_horizontal_line, DOWN)
            .align_to(neg_three_in_binary[1], RIGHT)
        )
        result_in_binary[0].set_color(YELLOW)

        # Save carry bit's state to restore later
        result_in_binary[0].save_state()

        self.play(Write(five_in_binary))
        self.play(
            Write(plus_sign),
            Write(neg_three_in_binary),
            Create(addition_horizontal_line),
        )
        self.play(Write(result_in_binary))

        self.next_slide()

        self.play(result_in_binary[0].animate.next_to(result_in_binary[2], DOWN))

        plus_sign_add_carry = (
            MathTex("+")
            .scale(2)
            .next_to(result_in_binary[0], LEFT)
            .align_to(plus_sign, LEFT)
        )
        carry_addition_horiz_line = Line(
            plus_sign_add_carry.get_left(), result_in_binary[0].get_right()
        ).next_to(VGroup(plus_sign_add_carry, result_in_binary[0]), DOWN)

        result_with_added_carry = (
            MathTex("(0010)_{_{1sC}}")
            .scale(2)
            .next_to(carry_addition_horiz_line, DOWN)
            .align_to(neg_three_in_binary, RIGHT)
        )

        self.play(Write(plus_sign_add_carry), Create(carry_addition_horiz_line))
        self.play(Write(result_with_added_carry))

        self.next_slide()

        negative_sign = MathTex("-", color=RED).scale(2).move_to(plus_sign_add_carry)
        sixteen_in_binary = (
            MathTex("10000", color=RED)
            .scale(2)
            .next_to(result_in_binary[1], DOWN)
            .align_to(result_in_binary, RIGHT)
        )
        one_in_binary = (
            MathTex("1", color=GREEN)
            .scale(2)
            .next_to(sixteen_in_binary, DOWN)
            .align_to(sixteen_in_binary, RIGHT)
        )

        plus_sign_after_minus_sixteen = (
            MathTex("+", color=GREEN)
            .scale(2)
            .move_to(one_in_binary)
            .align_to(negative_sign, LEFT)
        )

        self.play(Restore(result_in_binary[0]))

        self.play(
            ReplacementTransform(plus_sign_add_carry, negative_sign),
            Write(sixteen_in_binary),
            VGroup(result_with_added_carry, carry_addition_horiz_line)
            .animate.next_to(one_in_binary, DOWN)
            .align_to(neg_three_in_binary, RIGHT),
        )

        self.play(
            Write(plus_sign_after_minus_sixteen),
            Write(one_in_binary),
        )

        self.next_slide()

        arrow_result = Arrow(start=LEFT, end=RIGHT, color=GRAY_C).next_to(
            result_in_binary, RIGHT
        )
        result = Tex("Result").scale(2).next_to(arrow_result, RIGHT)

        arrow_sixteen = Arrow(start=LEFT, end=RIGHT, color=GRAY_C).next_to(
            sixteen_in_binary, RIGHT
        )
        two_power_n = MathTex("- 2^n", color=RED).scale(2).next_to(arrow_sixteen, RIGHT)

        arrow_one = Arrow(start=LEFT, end=RIGHT, color=GRAY_C).next_to(
            one_in_binary, RIGHT
        )
        one = MathTex("+ 1", color=GREEN).scale(2).next_to(arrow_one, RIGHT)

        self.play(AnimationGroup(GrowArrow(arrow_result), Write(result), lag_ratio=0.4))
        self.play(
            AnimationGroup(GrowArrow(arrow_sixteen), Write(two_power_n), lag_ratio=0.4)
        )
        self.play(AnimationGroup(GrowArrow(arrow_one), Write(one), lag_ratio=0.4))

        self.next_slide()

        # add_carry_formula_group = VGroup(result, two_power_n, one)
        add_carry_formula_group = MathTex(r"\text{Result}", "- 2^n", "+1").scale(2)
        add_carry_formula_group[1].set_color(RED)
        add_carry_formula_group[2].set_color(GREEN)

        self.play(
            FadeOut(
                five_in_binary,
                plus_sign,
                neg_three_in_binary,
                addition_horizontal_line,
                result_in_binary,
                negative_sign,
                sixteen_in_binary,
                plus_sign_after_minus_sixteen,
                one_in_binary,
                carry_addition_horiz_line,
                result_with_added_carry,
                arrow_result,
                arrow_sixteen,
                arrow_one,
            ),
            ReplacementTransform(VGroup(result, two_power_n, one), add_carry_formula_group),
        )

        self.next_slide()

        so_dotdotdot = Tex("So...").move_to(carry)
        rule_one = MathTex(r"1) \text{Complement} = ", "2^n - 1", r" - \text{Result}")
        rule_one[1].set_color(YELLOW)

        rule_two = (
            MathTex(r"2) \text{Add Carry} = ", r"\text{" , "Result", "}", "- 2^n", "+ 1")
            .next_to(rule_one, DOWN)
            .align_to(rule_one, LEFT)
        )

        rule_two[4].set_color(RED)
        rule_two[5].set_color(GREEN)

        anims = AnimationGroup(
            ReplacementTransform(carry, so_dotdotdot),
            ReplacementTransform(add_carry_formula_group, rule_two),
            Write(rule_one),
            lag_ratio=0.3,
        )

        self.play(anims)

        self.next_slide()

        self.play(FadeOut(
            rule_one, rule_two
        ))


        graph = Tex("The Graph").scale(4)
        self.play(
            ReplacementTransform(so_dotdotdot, graph)
        )

        self.next_slide()

        self.play(graph.animate.scale(0.25).to_edge(UR))

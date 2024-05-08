from manim import *
from manim_slides import Slide

# noqa: F405


class AddCarry(Slide):
    def construct(self):
        pass
        carry = MathTex("Carry").scale(4)

        # Animation Transform
        ...

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
        result = MathTex("Result").scale(2).next_to(arrow_result, RIGHT)

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
        add_carry_formula_group = MathTex("Result", "- 2^n", "+1").scale(2)
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

        so_dotdotdot = MathTex("So...").move_to(carry)
        rule_one = MathTex("1)\; Complement = ", "2^n - 1", " - Result")
        rule_one[1].set_color(YELLOW)

        rule_two = (
            MathTex("2)\; Add\; Carry = ", "Result", "- 2^n", "+ 1")
            .next_to(rule_one, DOWN)
            .align_to(rule_one, LEFT)
        )

        rule_two[2].set_color(RED)
        rule_two[3].set_color(GREEN)

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


        when = Tex("When?").scale(4)
        self.play(
            ReplacementTransform(so_dotdotdot, when)
        )

        self.next_slide()

        self.play(when.animate.scale(0.25).to_edge(UR))

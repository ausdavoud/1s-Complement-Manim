from manim import *  #
from manim_slides import Slide


class ThankYou(Slide):
    def construct(self):
        title = (
            Tex("1's Complement")
            .scale(3 / 4)
            .to_edge(UL)
            .set_color_by_gradient(YELLOW, RED)
        )

        subtitle = (
            Tex("Thank you!")
            .scale(3 / 4)
            .to_edge(UR)
            .set_color_by_gradient(WHITE, GRAY)
        )
        self.add(title, subtitle)

        number_plane = NumberPlane(
            x_range=[-30, 30],
            y_range=[-30, 30],
            x_length=15,
            y_length=15,
            background_line_style={
                "stroke_color": DARK_GRAY,
                "stroke_width": 4,
                "stroke_opacity": 0.6,
            }
        )
        self.play(Write(number_plane))
        r = lambda theta: 4 * np.sin(24 * theta / 25) + 10
        graph = number_plane.plot_polar_graph(r, [0, 60 * PI], color=[PURE_BLUE])
        

        self.play(Write(graph), run_time=10)

        # self.play(Write(MathTex("3")))
        self.wait(3)



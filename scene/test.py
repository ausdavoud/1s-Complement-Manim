# from manim import (
#     Scene, Rectangle, Tex, Create, VGroup,
#     Write, FadeOut, DR
# )

# from manim_slides import Slide

# class video(Slide):
#     def construct(self):
#         id1 = MathTex(r"\frac{dy}{dx}=\frac{1}{\frac{dx}{dy}}", font_size=96)
#         g1 = NumberPlane(x_range=[-1, 7, 1], y_range=[-1, 7, 1], x_length=6, y_length=6)
#         label1 = g1.get_axis_labels(x_label="x", y_label="y")
#         self.play(Write(id1), run_time=1.6)
#         self.wait()
#         self.play(id1.animate.shift(LEFT*3))

#         graph_group = VGroup(g1, label1)
#         graph_group.to_edge(RIGHT)

#         e_graph = g1.plot(lambda x: np.e**x, color=BLUE)
#         ln_graph = g1.plot(lambda x: np.log(x), x_range=[0.1,7,0.1], color=RED)

#         self.play(DrawBorderThenFill(graph_group))
#         self.play(Create(e_graph), Create(ln_graph))
#         self.wait()

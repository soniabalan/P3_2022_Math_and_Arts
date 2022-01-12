from manim import *

class ParametricCruve(ThreeDScene):
    def construct(self):
        colors = ["#0000ff", "#8bff26", "#26e9ff", "#ff3c00", "#ffa600"]
        surface  = ParametricFunction(
            lambda t : np.array([
                5 * np.cos(t) + np.sin(t) * np.cos(60*t),
                np.sin(2*t) + np.sin(60*t),
                2
            ]), color=RED, t_range = np.array([0, TAU, 0.01])
        )
        surface.set_color_by_gradient(colors)
        self.play(Create(surface, stroke_width = 0.1), run_time = 15)
        self.wait(2)
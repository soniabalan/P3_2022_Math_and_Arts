# Recaman Sequence (Cairo backend)
# Numberphile video: https://www.youtube.com/watch?v=FGC5TdIiT9U

from manim import *
import pprint


class RecamanSequence(MovingCameraScene):
    # CONFIG = {
    #     "n": 100,  # number of iterations
    # }
    
    n=100

    def construct(self):
        self.count = 0
        visited = [0] + [None] * self.n
        arcs = VGroup()

        self.index = 0  # acts as a pointer
        self.highest = max(self.index, 3)  # use to define the frame width

        for i in range(self.n):
            index = self.index - self.count

            if index < 0 or index in visited:
                index = self.index + self.count

            # defining the start and end of the arc
            start = np.array([visited[self.count], 0, 0])
            end = np.array([index, 0, 0])

            # defining the angle of arc (i.e., upwards arc or downwards arc)
            angle = -PI if self.count % 2 == 0 else PI

            if index < visited[self.count]:
                angle *= -1

            arc = ArcBetweenPoints(start, end, angle)
            arcs.add(arc)

            # updating variables
            self.index = index
            self.count += 1
            visited[self.count] = self.index

        VIBGYOR=[PURPLE, BLUE, TEAL, GREEN, YELLOW, GOLD, RED]
        
        VIBGYOR.reverse()

        arcs.set_color_by_gradient(*VIBGYOR)

        # rendering
        for i, arc in enumerate(arcs):
            self.highest = max(self.highest, max(visited[:i+2]))
            arc.set_stroke(opacity=1 - (np.sqrt(i)/self.n))

            self.play(
                Write(arc),
                self.camera.frame.animate.set_width(self.highest).move_to(self.highest/2 * RIGHT),
                rate_func=linear,
                run_time=0.25
            )

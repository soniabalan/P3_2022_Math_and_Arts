from manim import *
import datetime as date

class ParametricCruve(ThreeDScene):
    
    def construct(self):
        colors = ["#0000ff", "#8bff26", "#26e9ff", "#ff3c00", "#ffa600"]
        

        #inputs
        day = 14
        month = 4
        year = 1986

        #trackers
        daytrk = ValueTracker(day)
        monthtrk = ValueTracker(month)
        yeartrk = ValueTracker(year)
        datetrk = [daytrk, monthtrk, yeartrk]

        #labels
        day_var = Variable(day, "Day ", var_type = Integer).add_updater(lambda v: v.tracker.set_value(daytrk.get_value()))
        month_var = Variable(month, "Month ", var_type = Integer).add_updater(lambda v: v.tracker.set_value(monthtrk.get_value()))   
        year_var = Variable(year, "Year", var_type = Integer).add_updater(lambda v: v.tracker.set_value(yeartrk.get_value()))
        Group(day_var, month_var, year_var).arrange(DOWN).move_to(LEFT*5)
        title = Text("Your life as a unique animation", stroke_width=1, font_size=55)
        
        #current date
        today = date.datetime.now()
        datum = [today.day, today.month, today.year]

        #create and update parametric function
        func = always_redraw(lambda :
            get_param_func(monthtrk.get_value(), daytrk.get_value(), yeartrk.get_value())
        )
        func.set_color_by_gradient(colors)

        #animating  
        self.play(Write(title))
        self.wait(2)
        self.play(FadeTransformPieces(title, func))
        self.play(Write(day_var), Write(month_var), Write(year_var))    #labels
        self.add(func)
        self.wait(2)
        self.play(
            datetrk[0].animate.set_value(datum[0]),
            datetrk[1].animate.set_value(datum[1]),         #animating function by updating trackers
            datetrk[2].animate.set_value(datum[2]), 
            run_time = 8, func_rate=smooth
        )
        self.wait(2)
        
#parametric function class 
def get_param_func(month, day, year):
    colors = ["#0000ff", "#8bff26", "#26e9ff", "#ff3c00", "#ffa600"]
    surface  = ParametricFunction(
            lambda t : np.array([
                (np.cos(month*t)+np.cos(year%30*t)/2 +np.sin((month+day)*t)/3),
                (np.sin(month*t)+np.sin(year%30*t)/2 +np.cos((month+day)*t)/3),
                0
            ]), color=RED, t_range = np.array([0, 2*PI, 0.01]), stroke_width = 5,  tolerance_for_point_equality=1e-9
    )
    surface.set_color_by_gradient(colors)

    
    return surface
        

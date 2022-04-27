from build_regression import BuildRegression
import matplotlib.pyplot as plt

class drawPlot:
    def draw(coefficients , features , T , y , fig):
        if features == 1:
            plt.pause(0.0001)
            plt.clf()
            plt.scatter(T , y)
            BuildRegression.draw_line(BuildRegression.f , coefficients[1] , coefficients[0])
            fig.canvas.draw()
            fig.canvas.flush_events()
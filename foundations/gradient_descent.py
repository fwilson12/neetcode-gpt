class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        

        for i in range(iterations):
            direction = -2 * init # negative gradient of the cost function; the direction we need to go to minimize the cost as quickly as possible
            # our new location (value in the parameter space): starting from the current location, travel in the direction of the steepest descent, scaled by a (in this case) linear lr
            init = init + learning_rate * direction # when direction is negative, we're moving to the left, and vice versa

        return round(init, 5)

        

class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
       
        

        for i in range(iterations):
            direction = -2 * init 
            init = init + learning_rate * direction 

        return round(init, 5)

        

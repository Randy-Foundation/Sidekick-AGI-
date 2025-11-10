class CollatzResolver:
    def __init__(self, lambda_value=0.003645):
        self.phi = 1.6180339887
        self.lambda_val = lambda_value

    def entropy_wave(self, n):
        import math
        return math.sin(n) * math.log(n + 1) / (n + 1)

    def refined_collatz(self, n):
        if n <= 0:
            return None
        Ew = self.entropy_wave(n)
        step = self.phi * ((n / 2) + ((3 * n + 1) / self.phi) - self.lambda_val * Ew)
        return int(round(step))

    def full_trajectory(self, n):
        trajectory = [n]
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.refined_collatz(n)
            trajectory.append(n)
        return trajectory
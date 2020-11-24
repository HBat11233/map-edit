import logging
import numpy as np

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class Normal:
    def __init__(self, _u, _o, _len):
        self.list = np.random.normal(_u, _o, _len)
        self.set = set(self.list)

    def randn(self):
        ans = 0
        for i in self.set:
            ans = i
            self.set.remove(i)
            break
        return ans

    def empty(self):
        return len(self.set) == 0

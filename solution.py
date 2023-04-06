import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1369690762 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    return (x.max() - .014)/alpha**(1/len(x)) + .014, \
           x.max()

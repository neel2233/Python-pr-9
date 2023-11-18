import numpy as np
import scipy
import time


def timer(func):
    def wrapper(X, m, C):
        start_time = time.time()
        f = func(X, m, C)
        end_time = time.time()
        print(end_time - start_time)
        return f
    return wrapper


@timer
def log_m_v(X, m, C):
    D = X.shape[1]
    diff = X - m
    inv_cov = np.linalg.inv(C)
    det_cov = np.linalg.det(C)
    log_pdf = -0.5 * (D * np.log(2 * np.pi) + np.log(det_cov) + np.sum(diff @ inv_cov * diff, axis=1))
    return log_pdf

N, D = 1000, 2
X = np.random.normal(size=(N, D))
m = np.array([0, 0])
C = np.array([[1, 0.5], [0.5, 1]])
l = log_m_v(X, m, C)
stime = time.time()
l1 = scipy.stats.multivariate_normal(m, C).logpdf(X)
etime = time.time()
print(etime - stime)
print(l)
print("-----------------------------------------------------------------------")
print(l1)

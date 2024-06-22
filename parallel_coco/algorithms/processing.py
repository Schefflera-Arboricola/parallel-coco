from joblib import Parallel, delayed
import time
import os

__all__ = [
    "temper",
    "melt",
]


def temper(C):
    if hasattr(C, "chocolate_obj"):
        C = C.chocolate_obj
    print("tempering...")
    t = C.cooling_time()
    C.temp = C.tempering_point
    n_jobs = os.cpu_count()

    def temper_process(t):
        time.sleep(t)

    if t > 4:
        Parallel(n_jobs=n_jobs)(
            delayed(temper_process)(t / n_jobs) for _ in range(n_jobs)
        )
        t_ = t / n_jobs
    else:
        time.sleep(t)
        t_ = t
    print(f"tempering done in {t_:.2f} seconds")


def melt(C):
    if hasattr(C, "chocolate_obj"):
        C = C.chocolate_obj
    print("melting...")
    t = C.melting_time()
    C.temp = C.melting_point
    n_jobs = os.cpu_count()

    def melt_process(t):
        time.sleep(t)

    if t > 4:
        Parallel(n_jobs=n_jobs)(
            delayed(melt_process)(t / n_jobs) for _ in range(n_jobs)
        )
        t_ = t / n_jobs
    else:
        time.sleep(t)
        t_ = t

    print(f"melting done in {t_:.2f} seconds")

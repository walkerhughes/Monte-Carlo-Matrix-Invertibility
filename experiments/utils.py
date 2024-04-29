import functools
from joblib import Parallel, delayed

def parallelize(n_jobs: int = -1, n_trials: int = 10_000):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = Parallel(n_jobs = n_jobs)(delayed(func)(*args, **kwargs) for _ in range(n_trials))
            return results
        return wrapper
    return decorator
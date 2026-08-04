"""
Flaky tests — pass or fail RANDOMLY on each run, independent of any code change.
This is the textbook definition of flakiness, and the signal your model learns.

Each test documents its TRUE failure rate — this is your ground truth. When you
later train a model, you already know which tests are flaky and how flaky, so you
can measure exactly how well the model recovered that truth.

We seed randomness from the clock + pid so every run differs (real flakiness),
rather than being reproducible.
"""
import random
import time
import os

# Fresh entropy each run -> outcomes vary run to run, like true flakiness.
random.seed(time.time_ns() ^ os.getpid())


def _fails_with_probability(p):
    """Return True (=> test should fail) with probability p."""
    return random.random() < p


def test_flaky_low():
    # TRUE FLAKINESS RATE: ~5%
    assert not _fails_with_probability(0.05), "flaky_low tripped (expected ~5%)"


def test_flaky_medium():
    # TRUE FLAKINESS RATE: ~15%
    assert not _fails_with_probability(0.15), "flaky_medium tripped (expected ~15%)"


def test_flaky_high():
    # TRUE FLAKINESS RATE: ~30%
    assert not _fails_with_probability(0.30), "flaky_high tripped (expected ~30%)"


def test_timing_sensitive():
    # TRUE FLAKINESS RATE: ~10%
    # Simulates a test with a race/timeout: occasionally the "operation"
    # takes too long and the assertion on elapsed time fails.
    # elapsed uniform(0, 0.020), budget 0.018  ->  P(fail) = 0.002/0.020 = 10%
    budget_s = 0.018
    elapsed = random.uniform(0.0, 0.020)  # occasionally exceeds the budget
    time.sleep(elapsed)
    assert elapsed <= budget_s, f"timing test exceeded budget ({elapsed:.4f}s)"
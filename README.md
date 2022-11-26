# rebench

A tiny regular expression benchmark tool.

## A tiny benchmark

```python
# Pseudo code
elapsed_sec = 0.0
for i in range(1, number_of_trials+1):
    string = generate_random_string_contains_expected(
            expected=expected,
            n=search_target_length
    )
    start_perf_counter = time.perf_counter()
    matched = benchmark_method(pattern, string)
    end_perf_counter = time.perf_counter()
```

## Installation

```sh
pip install https://github.com/kanjirz50/regbench
```

## How to use

```sh
$ regbench ".test" "test" --search-target-length=50000 --number_of_trials=10
Trying 10/10
{"times": 10, "total_elapsed_sec": 0.0017024570000000183, "average_search_sec": 0.00017024570000000183, "method": "search", "pattern": ".test", "string": {"head_of_last_trial_string": "kRVr3kkfqX", "length": 50000}, "matched": {"head_of_matched": "Wtest"}}

$ regbench ".*test$" "test" --search-target-length=50000 --number_of_trials=10
Trying 10/10
{"times": 10, "total_elapsed_sec": 14.512343084, "average_search_sec": 1.4512343084, "method": "search", "pattern": ".*test$", "string": {"head_of_last_trial_string": "io0Z59TxXN", "length": 50000}, "matched": {"head_of_matched": null}}
```
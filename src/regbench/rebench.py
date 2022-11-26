import time
import re
import sys

from .random_string import generate_random_string_contains_expected


choice_re_method = {
    'search': re.search,
    'match': re.match,
    'finditer': re.finditer,
}


def rebench(
        number_of_trials: int,
        expected: str,
        pattern: str,
        search_target_length: int,
        benchmark_method_name: str,
        ):
    string = ""
    benchmark_method = choice_re_method[benchmark_method_name]

    elapsed_sec = 0.0
    for i in range(1, number_of_trials+1):
        print(f'\rTrying {i}/{number_of_trials}', end="", file=sys.stderr)

        string = generate_random_string_contains_expected(
                expected=expected,
                n=search_target_length
        )

        start_perf_counter = time.perf_counter()
        matched = benchmark_method(pattern, string)
        end_perf_counter = time.perf_counter()
        elapsed_sec += end_perf_counter - start_perf_counter
    print("")

    if benchmark_method is re.finditer and matched:
        matched = [m for m in matched][0]

    return {
        'times': number_of_trials,
        'total_elapsed_sec': elapsed_sec,
        'average_search_sec': elapsed_sec / number_of_trials,
        'method': benchmark_method_name,
        'pattern': pattern,
        'string': {
            'head_of_last_trial_string': string[:10],
            'length': len(string),
        },
        'matched': {
            'head_of_matched': matched.group()[:10] if matched else matched,
        }
    }

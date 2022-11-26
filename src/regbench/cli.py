import argparse
import json

from .rebench import rebench, choice_re_method


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument(
            'pattern',
            type=str,
            help='Regular expression pattern.'
    )
    parser.add_argument(
            'expected',
            type=str,
            help='Expected string for generating random text which contains expected string.'
    )
    parser.add_argument(
            '--method',
            type=str,
            default='search',
            choices=choice_re_method.keys(),
            help='Choice a benchmark re method.'
    )
    parser.add_argument(
            '--number_of_trials',
            type=int,
            default=10,
            help='Number of trials.'
    )
    parser.add_argument(
            '--search-target-length',
            type=int,
            default=50000,
            help='Search target character length.'
    )
    args = parser.parse_args()

    result = rebench(
        number_of_trials=args.number_of_trials,
        expected=args.expected,
        pattern=args.pattern,
        search_target_length=args.search_target_length,
        benchmark_method_name=args.method,
    )

    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()

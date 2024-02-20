import argparse
import glob

import pandas as pd


def parse_args():
    """
    Parses the user arguments.

    Returns:
        argparse.Namespace: The parsed user arguments.
    """
    parser = argparse.ArgumentParser(
        allow_abbrev=False, description="parse user arguments"
    )
    parser.add_argument("--input_data_path", type=str)

    args, _ = parser.parse_known_args()
    return args


def main():
    """
    The main function that orchestrates the data preparation process.
    """
    args = parse_args()

    input_data_path = args.input_data_path
    input_data_df = pd.read_json(input_data_path, lines=True)

    print(input_data_df)
    return


if __name__ == "__main__":
    main()

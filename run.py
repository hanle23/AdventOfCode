#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path

def run_solution(year: str, day: str, part: str = ""):
    """
    Run the solution for the specified year and day.
    If part is specified, only run that part. Otherwise, run both parts if they exist.
    """
    # Ensure day is two digits
    day = day.zfill(2)

    # Construct the base path
    base_path = Path(year) / day

    if not base_path.exists():
        print(f"Error: Directory {base_path} does not exist")
        return

    # Define which parts to run
    parts_to_run = [part] if part else ['1', '2']

    for p in parts_to_run:
        file_path = base_path / f"a-p{p}.py"

        if file_path.exists():
            print(f"\nRunning Year {year} Day {day} Part {p}:")
            print("-" * 40)

            try:
                # Run the Python script and capture output
                result = subprocess.run(
                    ['python3', str(file_path)],
                    capture_output=True,
                    text=True
                )

                # Print stdout if there is any
                if result.stdout:
                    print(result.stdout.rstrip())

                # Print stderr if there is any
                if result.stderr:
                    print("Errors:", result.stderr.rstrip(), file=sys.stderr)

                # Print the return code if it's not 0
                if result.returncode != 0:
                    print(f"Process exited with code {result.returncode}")

            except Exception as e:
                print(f"Error running {file_path}: {e}")
        else:
            print(f"Warning: File {file_path} does not exist")

def main():
    parser = argparse.ArgumentParser(description='Run solutions for specific year and day')
    parser.add_argument('--year', required=True, help='Year of the solution')
    parser.add_argument('--day', required=True, help='Day of the solution')
    parser.add_argument('--part', choices=['1', '2'], help='Specific part to run (optional)')

    args = parser.parse_args()

    run_solution(args.year, args.day, args.part)

if __name__ == '__main__':
    main()

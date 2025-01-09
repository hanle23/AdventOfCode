#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys
from pathlib import Path

def run_solution(year: str, day: str, part: str = None):
    """
    Run the solution for the specified year and day.
    If part is specified, only run that part. Otherwise, run both parts if they exist.
    """
    # Ensure day is two digits
    day = day.zfill(2)

    # Construct the base path
    base_path = Path(year) / day

    if not base_path.exists():
        print(f"Error: Directory {base_path} does not exist", flush=True)
        return

    # Define which parts to run
    parts_to_run = [part] if part else ['1', '2']

    for p in parts_to_run:
        file_path = base_path / f"a-p{p}.py"

        if file_path.exists():
            print(f"\nRunning Year {year} Day {day} Part {p}:", flush=True)
            print("-" * 40, flush=True)

            try:
                # Set environment variable for unbuffered output
                env = os.environ.copy()
                env['PYTHONUNBUFFERED'] = '1'

                # Run the Python script and capture output
                process = subprocess.Popen(
                    ['python3', '-u', str(file_path)],  # -u flag forces unbuffered output
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    env=env,
                    bufsize=1,  # Line buffered
                    universal_newlines=True
                )

                # Read output in real-time
                while True:
                    stdout_line = process.stdout.readline()
                    stderr_line = process.stderr.readline()

                    if stdout_line == '' and stderr_line == '' and process.poll() is not None:
                        break

                    if stdout_line:
                        print(stdout_line.rstrip(), flush=True)
                    if stderr_line:
                        print("Error:", stderr_line.rstrip(), file=sys.stderr, flush=True)

                # Get the return code
                return_code = process.poll()
                if return_code != 0:
                    print(f"Process exited with code {return_code}", flush=True)

            except Exception as e:
                print(f"Error running {file_path}: {e}", flush=True)
        else:
            print(f"Warning: File {file_path} does not exist", flush=True)

def main():
    parser = argparse.ArgumentParser(description='Run solutions for specific year and day')
    parser.add_argument('--year', required=True, help='Year of the solution')
    parser.add_argument('--day', required=True, help='Day of the solution')
    parser.add_argument('--part', choices=['1', '2'], help='Specific part to run (optional)')

    args = parser.parse_args()

    run_solution(args.year, args.day, args.part)

if __name__ == '__main__':
    main()

#!/usr/bin/python3
"""Log parsing script that reads stdin and computes metrics."""
import sys


def print_stats(total_size, status_counts):
    """Print current statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Main function to parse logs from stdin."""
    total_size = 0
    line_count = 0
    valid_codes = {"200", "301", "400", "401", "403", "404", "405", "500"}
    status_counts = {code: 0 for code in valid_codes}

    try:
        for line in sys.stdin:
            parts = line.split()

            # Validate format: at least enough parts and check structure
            if len(parts) < 7:
                continue

            try:
                # Check status code and file size (last two fields)
                status_code = parts[-2]
                file_size = int(parts[-3] if len(parts) > 7 else parts[-1])
                file_size = int(parts[-1])

                # Validate the line format more strictly
                if parts[1] != "-" or not parts[3].startswith('"GET'):
                    continue

                total_size += file_size

                if status_code in valid_codes:
                    status_counts[status_code] += 1

                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)

            except (ValueError, IndexError):
                continue

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()

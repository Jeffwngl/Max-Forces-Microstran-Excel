# 3.12.6
# Import CSV file and calculate Fxb ranges for specific cases and segments

import pandas as pd
from typing import Union


def find_range(file_path: str, start_row: int, end_row: int, case_number: int, is_max: bool) -> Union[float, None]:
    """Returns the max or min Fxb value for a given member and case range."""
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

    mask = (
        (df["CaseNo"] == case_number) &
        (df["MemberNo"].between(start_row, end_row))
    )
    values = df.loc[mask, "Fxb"]

    if values.empty:
        print(f"No data found for Case {case_number}, Members {start_row}-{end_row}")
        return None

    return values.max() if is_max else values.min()


if __name__ == "__main__":
    file_path = "public/Steels Assignment 2_results.csv"  # Adjust file path as needed

    # Segment definitions (start, end)
    segments = {
        "Top Chord": [(201, 206), (207, 214), (215, 220)],
        "Bottom Chord": [(102, 106), (107, 115), (116, 120)],
        "Diagonal Chord": [(401, 412), (413, 428), (429, 440)]
    }

    # Case configurations
    # Format: case_number: {segment_type: is_max_boolean}
    cases = {
        5: {"Top Chord": True, "Bottom Chord": False, "Diagonal Chord": True},
        6: {"Top Chord": False, "Bottom Chord": True, "Diagonal Chord": True},
        7: {"Top Chord": True, "Bottom Chord": False, "Diagonal Chord": True}
    }

    # Compute and print results
    for case_no, chord_config in cases.items():
        print(f"\n=== Case {case_no} Results ===")
        for chord_type, seg_ranges in segments.items():
            is_max = chord_config[chord_type]
            for i, (start, end) in enumerate(seg_ranges, start=1):
                result = find_range(file_path, start, end, case_no, is_max)
                if result is not None:
                    print(f"{chord_type} | Segment {i}: {result:.3f}")

#!/usr/bin/python3

# Define a function to check if a report is safe
def is_safe(report):
    differences = [report[i+1] - report[i] for i in range(len(report)-1)]
    if all(1 <= diff <= 3 for diff in differences):  # Check if levels are increasing gradually
        return True
    if all(-3 <= diff <= -1 for diff in differences):  # Check if levels are decreasing gradually
        return True
    return False

# Define a function to check if removing one level can make the report safe
def is_safe_with_dampener(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]  # Remove one level
        if is_safe(modified_report):
            return True
    return False

# Read the input file
file_path = "input.txt"
with open(file_path, "r") as file:
    lines = file.readlines()

# Process each line as a report
safe_count_with_dampener = 0
for line in lines:
    report = list(map(int, line.strip().split()))
    if is_safe(report) or is_safe_with_dampener(report):
        safe_count_with_dampener += 1

print(safe_count_with_dampener)

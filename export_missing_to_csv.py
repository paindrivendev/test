#!/usr/bin/env python3
import csv

def read_job_refs(filename):
    """Read external_job_ref from a CSV file."""
    refs = set()
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            refs.add(row['external_job_ref'])
    return refs

print("Reading live_jobs.csv...")
live_jobs = read_job_refs('live_jobs.csv')
print(f"Found {len(live_jobs)} jobs in live_jobs.csv")

print("\nReading live_approved_jobs.csv...")
live_approved = read_job_refs('live_approved_jobs.csv')
print(f"Found {len(live_approved)} jobs in live_approved_jobs.csv")

# Find differences
missing_in_approved = live_jobs - live_approved
missing_in_live = live_approved - live_jobs

# Save to CSV files
print(f"\nExporting {len(missing_in_approved)} jobs missing in approved...")
with open('missing_in_approved.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['external_job_ref'])
    for ref in sorted(missing_in_approved):
        writer.writerow([ref])
print("Saved to: missing_in_approved.csv")

print(f"\nExporting {len(missing_in_live)} jobs missing in live...")
with open('missing_in_live.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['external_job_ref'])
    for ref in sorted(missing_in_live):
        writer.writerow([ref])
print("Saved to: missing_in_live.csv")

print("\nDone!")

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

print("\n" + "="*80)
print(f"\nJobs in live_jobs.csv but NOT in live_approved_jobs.csv: {len(missing_in_approved)}")
print(f"Jobs in live_approved_jobs.csv but NOT in live_jobs.csv: {len(missing_in_live)}")

# Save results to files
if missing_in_approved:
    with open('missing_in_approved.txt', 'w') as f:
        for ref in sorted(missing_in_approved):
            f.write(f"{ref}\n")
    print(f"\nSaved to: missing_in_approved.txt")

if missing_in_live:
    with open('missing_in_live.txt', 'w') as f:
        for ref in sorted(missing_in_live):
            f.write(f"{ref}\n")
    print(f"Saved to: missing_in_live.txt")

print("\n" + "="*80)
print("\nSummary:")
print(f"  Common jobs: {len(live_jobs & live_approved)}")
print(f"  Only in live_jobs: {len(missing_in_approved)}")
print(f"  Only in live_approved: {len(missing_in_live)}")

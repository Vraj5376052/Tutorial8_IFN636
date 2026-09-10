"""
app.py

Build a few jobs, register them, run them, print a summary.
"""

from executor import Executor
from models import DataProcessingJob, EmailJob, PriorityJob
from task_manager import TaskManager


def build_jobs():
    return [
        EmailJob(1, "user@example.com"),
        DataProcessingJob(2, "dataset_A"),
        EmailJob(3, "admin@example.com"),
        DataProcessingJob(4, "dataset_B"),
        # Activity 2: these two carry a priority, 1 beats 3.
        PriorityJob(5, "Send critical alert to on-call", priority=1),
        PriorityJob(6, "Rebuild nightly report", priority=3),
    ]


if __name__ == "__main__":
    jobs = build_jobs()

    manager = TaskManager()
    for job in jobs:
        manager.add_job(job)  # all start as 'pending'

    # FIX (app.py): pass 'manager' to Executor so it can update statuses.
    # Previously Executor(jobs).run() had no manager reference, statuses never changed.
    Executor(jobs, manager).run()

    print("\n=== SUMMARY ===")
    print(f"Pending:   {len(manager.get_jobs_by_status('pending'))}")
    print(f"Completed: {len(manager.get_jobs_by_status('completed'))}")
    # FIX (app.py): added 'failed' count to summary so failures are visible.
    print(f"Failed:    {len(manager.get_jobs_by_status('failed'))}")

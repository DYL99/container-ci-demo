"""CPS 310 container and CI demo project."""

import csv
import json


def load_config(filename):
    """Load application configuration from JSON."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def load_tasks(filename):
    """Load tasks from a CSV file."""
    tasks = []

    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            tasks.append(
                {
                    "name": row["name"],
                    "status": row["status"],
                }
            )

    return tasks


def count_completed(tasks, completed_status):
    """Count tasks matching the configured completed status."""
    return sum(
        1
        for task in tasks
        if task["status"].lower() == completed_status.lower()
    )


def build_summary(tasks, completed_status):
    """Build summary information for the task list."""
    completed = count_completed(tasks, completed_status)

    return {
        "total": len(tasks),
        "completed": completed,
        "remaining": len(tasks) - completed,
    }


def main():
    """Run the task report."""
    config = load_config("config.json")
    tasks = load_tasks(config["data_file"])
    summary = build_summary(tasks, config["completed_status"])

    print(config["report_title"])
    print("-" * len(config["report_title"]))
    print(f"Total tasks: {summary['total']}")
    print(f"Completed: {summary['completed']}")
    print(f"Remaining: {summary['remaining']}")


if __name__ == "__main__":
    main()

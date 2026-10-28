"""Tests for the CPS 310 container and CI demo project."""

from app import build_summary, count_completed, load_config, load_tasks


def test_count_completed_counts_matching_status():
    tasks = [
        {"name": "Write tests", "status": "done"},
        {"name": "Update README", "status": "todo"},
        {"name": "Push branch", "status": "done"},
    ]

    assert count_completed(tasks, "done") == 2


def test_count_completed_is_case_insensitive():
    tasks = [
        {"name": "Write tests", "status": "Done"},
        {"name": "Update README", "status": "DONE"},
    ]

    assert count_completed(tasks, "done") == 2


def test_build_summary_reports_totals():
    tasks = [
        {"name": "Write tests", "status": "done"},
        {"name": "Update README", "status": "todo"},
        {"name": "Push branch", "status": "done"},
    ]

    assert build_summary(tasks, "done") == {
        "total": 3,
        "completed": 2,
        "remaining": 1,
    }


def test_load_config_reads_json(tmp_path):
    config_file = tmp_path / "config.json"
    config_file.write_text(
        """{
  "report_title": "Demo Report",
  "data_file": "tasks.csv",
  "completed_status": "done"
}""",
        encoding="utf-8",
    )

    result = load_config(config_file)

    assert result == {
        "report_title": "Demo Report",
        "data_file": "tasks.csv",
        "completed_status": "done",
    }


def test_load_tasks_reads_csv(tmp_path):
    data_file = tmp_path / "tasks.csv"
    data_file.write_text(
        "name,status\nWrite tests,done\nUpdate README,todo\n",
        encoding="utf-8",
    )

    result = load_tasks(data_file)

    assert result == [
        {"name": "Write tests", "status": "done"},
        {"name": "Update README", "status": "todo"},
    ]


def test_build_summary_empty_list():
    assert build_summary([], "done") == {
        "total": 0,
        "completed": 0,
        "remaining": 0,
    }

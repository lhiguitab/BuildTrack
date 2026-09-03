from data.mock_data import mock_milestones_data, mock_tasks_data

def get_milestones():
    return mock_milestones_data


def update_milestone_status(milestone_id: str, status: str):
    milestone = next(
        (item for item in mock_milestones_data if item["id"] == milestone_id),
        None
    )

    if milestone is None:
        raise LookupError("Milestone not found")

    if status == "completed":
        has_open_tasks = any(
            task["milestone_id"] == milestone_id and task["status"] != "completed"
            for task in mock_tasks_data
        )

        if has_open_tasks:
            raise ValueError(
                "A milestone cannot be completed while it has open tasks"
            )

    milestone["status"] = status
    return milestone

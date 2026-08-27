import sys
import unittest
from pathlib import Path

from fastapi import HTTPException

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from data.mock_data import mock_milestones_data, mock_tasks_data
from main import MilestoneStatusUpdate, update_milestone


MILESTONE_ID = "550e8400-e29b-41d4-a716-446655440001"


class UpdateMilestoneStatusTests(unittest.TestCase):
    def setUp(self):
        self.milestone = mock_milestones_data[0]
        self.task = mock_tasks_data[0]
        self.original_milestone_status = self.milestone["status"]
        self.original_task_status = self.task["status"]

    def tearDown(self):
        self.milestone["status"] = self.original_milestone_status
        self.task["status"] = self.original_task_status

    def test_allows_completion_when_no_tasks_are_open(self):
        self.milestone["status"] = "in_progress"

        result = update_milestone(
            MILESTONE_ID,
            MilestoneStatusUpdate(status="completed")
        )

        self.assertEqual(result["status"], "completed")

    def test_rejects_completion_with_open_tasks(self):
        self.milestone["status"] = "in_progress"
        self.task["status"] = "in_progress"

        with self.assertRaises(HTTPException) as context:
            update_milestone(
                MILESTONE_ID,
                MilestoneStatusUpdate(status="completed")
            )

        self.assertEqual(context.exception.status_code, 400)
        self.assertIn("open tasks", context.exception.detail)

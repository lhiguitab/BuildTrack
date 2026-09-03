import sys
import unittest
from pathlib import Path

from fastapi import HTTPException

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from data.mock_data import mock_tasks_data
from main import TaskStatusUpdate, update_task


TASK_ID = "550e8400-e29b-41d4-a716-446655440201"


class UpdateTaskStatusTests(unittest.TestCase):
    def setUp(self):
        self.task = mock_tasks_data[0]
        self.original_status = self.task["status"]

    def tearDown(self):
        self.task["status"] = self.original_status

    def test_updates_task_status(self):
        result = update_task(TASK_ID, TaskStatusUpdate(status="in_progress"))

        self.assertEqual(result["status"], "in_progress")

    def test_returns_not_found_for_unknown_task(self):
        with self.assertRaises(HTTPException) as context:
            update_task("unknown-task", TaskStatusUpdate(status="completed"))

        self.assertEqual(context.exception.status_code, 404)
        self.assertEqual(context.exception.detail, "Task not found")

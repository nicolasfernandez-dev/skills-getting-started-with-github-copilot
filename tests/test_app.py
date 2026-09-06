from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_delete_participant_removes_email_from_activity():
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    response = client.delete(f"/activities/{activity_name}/participants/{email}")

    assert response.status_code == 200
    assert email not in response.json()["participants"]


def test_delete_participant_returns_404_for_missing_email():
    response = client.delete("/activities/Chess Club/participants/ghost@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"

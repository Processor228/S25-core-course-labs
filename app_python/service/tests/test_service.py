from main import app
from fastapi.testclient import TestClient
from bs4 import BeautifulSoup
from datetime import datetime

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

    page = response.text
    assert "Current Time in" in page

    soup = BeautifulSoup(page, "html.parser")

    time_div = soup.find("div", class_="time")

    assert time_div, "No time div found!"

    time_str = time_div.text.strip()
    print("Extracted time:", time_str)

    time_str = time_str.replace("UTC", "").strip()

    # Parse the datetime
    parsed_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S %z")

    now = datetime.now(parsed_time.tzinfo)
    # the difference in 2 seconds is fine.
    assert abs((parsed_time - now).total_seconds()) < 2, \
        "time is not current."

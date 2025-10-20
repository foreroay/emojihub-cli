from unittest.mock import patch
from src.main import main

MOCK_EMOJI = {
    "name": "test emoji",
    "htmlCode": ["&#9999;"],
    "group": "test-group",
    "category": "test-category"
}

@patch("src.main.get_random_emoji")
def test_main_random(mock_api, capsys, monkeypatch):
    mock_api.return_value = MOCK_EMOJI
    monkeypatch.setattr("sys.argv", ["src/main.py", "random"])
    main()
    output = capsys.readouterr().out
    assert "test emoji" in output

@patch("src.main.get_all_groups")
def test_main_list_groups(mock_api, capsys, monkeypatch):
    mock_api.return_value = ["group-a", "group-b"]
    monkeypatch.setattr("sys.argv", ["src/main.py", "list-groups"])
    main()
    output = capsys.readouterr().out
    assert "- group-a" in output
    assert "- group-b" in output

@patch("src.main.get_emojis_by_group")
def test_main_by_group(mock_api, capsys, monkeypatch):
    mock_api.return_value = [MOCK_EMOJI]
    monkeypatch.setattr("sys.argv", ["src/main.py", "by-group", "test-group"])
    main()
    output = capsys.readouterr().out
    assert "test emoji" in output
    assert "test-group" in output

@patch("src.main.search_emojis")
def test_main_search(mock_api, capsys, monkeypatch):
    mock_api.return_value = [MOCK_EMOJI]
    monkeypatch.setattr("sys.argv", ["src/main.py", "search", "test"])
    main()
    output = capsys.readouterr().out
    assert "test emoji" in output
    assert "test" in output

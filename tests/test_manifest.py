import json
from pathlib import Path


def test_manifest():
    data = json.loads(Path("plugin.json").read_text(encoding="utf-8"))
    assert data["id"]
    assert data["version"].count(".") == 2
    assert data["api_version"] == 1
    assert data["entry"].endswith(":PLUGIN")

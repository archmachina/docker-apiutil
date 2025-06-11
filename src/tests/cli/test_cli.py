
import sys
import subprocess
import pytest

class TestCli:
    def test_1(self):
        # Test running the entrypoint with curl
        ret = subprocess.call(["/work/bin/entrypoint", "curl", "--help"])

        assert ret == 0

    def test_2(self):
        # Test running the entrypoint with jq
        ret = subprocess.call(["/work/bin/entrypoint", "jq", "--help"])

        assert ret == 0

    def test_3(self):
        # Test running the entrypoint
        text = "{ \"a\": 1 }"
        result = subprocess.run(
            ["/work/bin/entrypoint", "jq", "-c", "."],
            text=True,
            input=text,
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE
        )

        assert result.returncode == 0
        assert result.stdout.strip() == "{\"a\":1}"

    def test_4(self):
        # Test that the image contains pyyaml
        import yaml

        text = """\
        items:
          - 1
          - 2
          - 3
        """

        result = yaml.safe_load(text)

        assert result is not None
        assert isinstance(result, dict)
        assert "items" in result and isinstance(result["items"], list)
        assert len(result["items"]) == 3

        items = result["items"]
        assert items[0] == 1 and items[1] == 2 and items[2] == 3

    def test_5(self):
        # Test that we can use requests
        import requests

        result = requests.get("https://github.com/")

        assert result.status_code == 200

    def test_6(self):
        # Test that curl can access a site
        ret = subprocess.call(["/work/bin/entrypoint", "curl", "https://github.com/"])

        assert ret == 0



import sys
import subprocess
import pytest

class TestCli:
    def test_1(self):
        # Test running the entrypoint
        ret = subprocess.call(["/work/bin/entrypoint", "curl", "--help"])

        assert ret == 0

    def test_2(self):
        # Test running the entrypoint
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


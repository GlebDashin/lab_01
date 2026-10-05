import subprocess
import sys


def test_calc_cli():
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "calc", "2+3"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert result.stdout.strip() == "5.0"
    assert result.stderr == ""


def test_calc_error_cli():
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "calc", "5/0"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 2
    assert result.stdout == ""
    assert result.stderr.strip() != ""
    assert "Traceback" not in result.stderr

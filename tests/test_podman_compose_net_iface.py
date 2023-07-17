"""
test_podman_compose_net_iface.py

Tests the podman compose to specify network interface name
"""
# pylint: disable=redefined-outer-name
import os
from test_podman_compose import capture
import pytest


@pytest.fixture
def profile_compose_file(test_path):
    """ "Returns the path to the `net_iface` compose file used for this test module"""
    return os.path.join(test_path, "net_iface", "docker-compose.yaml")


def test_up(podman_compose_path, profile_compose_file):
    up_cmd = [
        "python3",
        podman_compose_path,
        "--dry-run",
        "-f",
        profile_compose_file,
        "up",
    ]

    _, command, return_code = capture(up_cmd)

    assert return_code == 0
    assert "--net net_iface_test:interface_name=int0" in command.decode("utf-8")

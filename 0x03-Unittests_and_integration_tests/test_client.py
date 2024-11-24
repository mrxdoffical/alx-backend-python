#!/usr/bin/env python3
"""A module for testing the client module.
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests the `GithubOrgClient` class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """Test that the result of _public_repos_url is the expected one
        based on the mocked payload.
        """
        test_payload = {
            'repos_url': "https://api.github.com/orgs/google/repos"
        }

        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock,
            return_value=test_payload
        ) as mock_org:
            test_client = GithubOrgClient("google")
            result = test_client._public_repos_url
            self.assertEqual(
                result,
                test_payload["repos_url"]
            )
            mock_org.assert_called_once()


if __name__ == '__main__':
    unittest.main()

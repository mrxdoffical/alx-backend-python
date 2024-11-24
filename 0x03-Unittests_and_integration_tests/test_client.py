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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test the public_repos method."""
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]
        mock_get_json.return_value = test_payload

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
            return_value="https://api.github.com/orgs/google/repos"
        ) as mock_public_repos_url:
            test_client = GithubOrgClient("google")
            result = test_client.public_repos()

            self.assertEqual(result, ["repo1", "repo2"])
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos"
            )
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Unit-test for GithubOrgClient.has_license static method."""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

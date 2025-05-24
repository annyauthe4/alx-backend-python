#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient"""

from client import GithubOrgClient
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """TestCase for GithubOrgClient.org"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns correct value and
        calls get_json once with expected URL.
        """
        expected_payload = {"login": org_name}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, expected_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

        def test_public_repos_url(self):
            """Test that _public_repos_url returns correct repos URL"""
            expected_url = "https://api.github.com/orgs/testorg/repos"
            payload = {"repos_url": expected_url}

            with patch.object(
                GithubOrgClient,
                "org",
                new_callable=PropertyMock
            ) as mock_org:
                mock_org.return_value = payload
                client = GithubOrgClient("testorg")
                self.assertEqual(client._public_repos_url, expected_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns expected list of repo names"""
        test_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "mit"}},
        ]
        mock_get_json.return_value = test_repos_payload

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as m_repos_url:
            m_repos_url.return_value = "https://api.github.com/orgs/test/repos"

            client = GithubOrgClient("test")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_get_json.assert_called_once()
            m_repos_url.assert_called_once()

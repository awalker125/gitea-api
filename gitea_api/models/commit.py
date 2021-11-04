# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.15.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from gitea_api.configuration import Configuration


class Commit(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'author': 'User',
        'commit': 'RepoCommit',
        'committer': 'User',
        'created': 'datetime',
        'files': 'list[CommitAffectedFiles]',
        'html_url': 'str',
        'parents': 'list[CommitMeta]',
        'sha': 'str',
        'url': 'str'
    }

    attribute_map = {
        'author': 'author',
        'commit': 'commit',
        'committer': 'committer',
        'created': 'created',
        'files': 'files',
        'html_url': 'html_url',
        'parents': 'parents',
        'sha': 'sha',
        'url': 'url'
    }

    def __init__(self, author=None, commit=None, committer=None, created=None, files=None, html_url=None, parents=None, sha=None, url=None, _configuration=None):  # noqa: E501
        """Commit - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._author = None
        self._commit = None
        self._committer = None
        self._created = None
        self._files = None
        self._html_url = None
        self._parents = None
        self._sha = None
        self._url = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if commit is not None:
            self.commit = commit
        if committer is not None:
            self.committer = committer
        if created is not None:
            self.created = created
        if files is not None:
            self.files = files
        if html_url is not None:
            self.html_url = html_url
        if parents is not None:
            self.parents = parents
        if sha is not None:
            self.sha = sha
        if url is not None:
            self.url = url

    @property
    def author(self):
        """Gets the author of this Commit.  # noqa: E501


        :return: The author of this Commit.  # noqa: E501
        :rtype: User
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Commit.


        :param author: The author of this Commit.  # noqa: E501
        :type: User
        """

        self._author = author

    @property
    def commit(self):
        """Gets the commit of this Commit.  # noqa: E501


        :return: The commit of this Commit.  # noqa: E501
        :rtype: RepoCommit
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this Commit.


        :param commit: The commit of this Commit.  # noqa: E501
        :type: RepoCommit
        """

        self._commit = commit

    @property
    def committer(self):
        """Gets the committer of this Commit.  # noqa: E501


        :return: The committer of this Commit.  # noqa: E501
        :rtype: User
        """
        return self._committer

    @committer.setter
    def committer(self, committer):
        """Sets the committer of this Commit.


        :param committer: The committer of this Commit.  # noqa: E501
        :type: User
        """

        self._committer = committer

    @property
    def created(self):
        """Gets the created of this Commit.  # noqa: E501


        :return: The created of this Commit.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Commit.


        :param created: The created of this Commit.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def files(self):
        """Gets the files of this Commit.  # noqa: E501


        :return: The files of this Commit.  # noqa: E501
        :rtype: list[CommitAffectedFiles]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Commit.


        :param files: The files of this Commit.  # noqa: E501
        :type: list[CommitAffectedFiles]
        """

        self._files = files

    @property
    def html_url(self):
        """Gets the html_url of this Commit.  # noqa: E501


        :return: The html_url of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this Commit.


        :param html_url: The html_url of this Commit.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def parents(self):
        """Gets the parents of this Commit.  # noqa: E501


        :return: The parents of this Commit.  # noqa: E501
        :rtype: list[CommitMeta]
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """Sets the parents of this Commit.


        :param parents: The parents of this Commit.  # noqa: E501
        :type: list[CommitMeta]
        """

        self._parents = parents

    @property
    def sha(self):
        """Gets the sha of this Commit.  # noqa: E501


        :return: The sha of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this Commit.


        :param sha: The sha of this Commit.  # noqa: E501
        :type: str
        """

        self._sha = sha

    @property
    def url(self):
        """Gets the url of this Commit.  # noqa: E501


        :return: The url of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Commit.


        :param url: The url of this Commit.  # noqa: E501
        :type: str
        """

        self._url = url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Commit, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Commit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Commit):
            return True

        return self.to_dict() != other.to_dict()

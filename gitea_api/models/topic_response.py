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


class TopicResponse(object):
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
        'created': 'datetime',
        'id': 'int',
        'repo_count': 'int',
        'topic_name': 'str',
        'updated': 'datetime'
    }

    attribute_map = {
        'created': 'created',
        'id': 'id',
        'repo_count': 'repo_count',
        'topic_name': 'topic_name',
        'updated': 'updated'
    }

    def __init__(self, created=None, id=None, repo_count=None, topic_name=None, updated=None, _configuration=None):  # noqa: E501
        """TopicResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created = None
        self._id = None
        self._repo_count = None
        self._topic_name = None
        self._updated = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        if repo_count is not None:
            self.repo_count = repo_count
        if topic_name is not None:
            self.topic_name = topic_name
        if updated is not None:
            self.updated = updated

    @property
    def created(self):
        """Gets the created of this TopicResponse.  # noqa: E501


        :return: The created of this TopicResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this TopicResponse.


        :param created: The created of this TopicResponse.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this TopicResponse.  # noqa: E501


        :return: The id of this TopicResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TopicResponse.


        :param id: The id of this TopicResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def repo_count(self):
        """Gets the repo_count of this TopicResponse.  # noqa: E501


        :return: The repo_count of this TopicResponse.  # noqa: E501
        :rtype: int
        """
        return self._repo_count

    @repo_count.setter
    def repo_count(self, repo_count):
        """Sets the repo_count of this TopicResponse.


        :param repo_count: The repo_count of this TopicResponse.  # noqa: E501
        :type: int
        """

        self._repo_count = repo_count

    @property
    def topic_name(self):
        """Gets the topic_name of this TopicResponse.  # noqa: E501


        :return: The topic_name of this TopicResponse.  # noqa: E501
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        """Sets the topic_name of this TopicResponse.


        :param topic_name: The topic_name of this TopicResponse.  # noqa: E501
        :type: str
        """

        self._topic_name = topic_name

    @property
    def updated(self):
        """Gets the updated of this TopicResponse.  # noqa: E501


        :return: The updated of this TopicResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this TopicResponse.


        :param updated: The updated of this TopicResponse.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

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
        if issubclass(TopicResponse, dict):
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
        if not isinstance(other, TopicResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TopicResponse):
            return True

        return self.to_dict() != other.to_dict()

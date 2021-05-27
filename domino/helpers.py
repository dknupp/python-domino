import os

from distutils.version import LooseVersion as parse_version
from urllib import parse as url_parse
from .constants import *


def is_version_compatible(version: str) -> bool:
    """
    Helper function to check for version compatibility

    @:param version  Domino version to check version compatibility against
    @:return bool   Boolean representing if version is compatible or not
    """
    return parse_version(version) >= parse_version(MINIMUM_SUPPORTED_DOMINO_VERSION)


def is_cluster_type_supported(version: str, cluster_type: str) -> bool:
    curr_version = parse_version(version)

    return next(
        (True for ct,min_version in CLUSTER_TYPE_MIN_SUPPORT if ct == cluster_type and curr_version >= parse_version(min_version)),
        False
    )


def is_compute_cluster_properties_supported(version: str) -> bool:
    return parse_version(version) >= parse_version(MINIMUM_DISTRIBUTED_CLUSTER_SUPPORT_DOMINO_VERSION)


def is_on_demand_spark_cluster_supported(version: str) -> bool:
    return parse_version(version) >= parse_version(MINIMUM_ON_DEMAND_SPARK_CLUSTER_SUPPORT_DOMINO_VERSION)


def clean_host_url(host_url):
    """
    Helper function to clean 'host_url'. This will extract
    hostname (with scheme) from the url
    """
    url_split = url_parse.urlsplit(host_url)
    return f"{url_split.scheme}://{url_split.netloc}"

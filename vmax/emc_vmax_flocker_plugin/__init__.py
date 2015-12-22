# Copyright Hybrid Logic Ltd.
# Copyright 2015 EMC Corporation
# See LICENSE file for details.

from flocker.node import BackendDescription, DeployerType
from .emc_vmax_blockdevice import vmax_from_configuration

__VERSION__ = '0.0.1'

def api_factory(cluster_id, **kwargs):
    protocol = 'iSCSI'
    if 'protocol' in kwargs:
        protocol = kwargs['protocol']

    hosts = {}
    if 'hosts' in kwargs:
        hosts = kwargs['hosts']

    dbhost='localhost'
    if 'database' in kwargs:
        dbhost = kwargs['database']

    min_allocation = 15
    if 'min_allocation' in kwargs:
        min_allocation = int(kwargs['min_allocation'])

    lock_path = '/tmp'
    if 'lockdir' in kwargs:
        lock_path = kwargs['lockdir']

    return vmax_from_configuration(cluster_id=cluster_id, protocol=protocol,
                                   hosts=hosts, min_allocation=min_allocation, dbhost=dbhost,
                                   lock_path=lock_path)

FLOCKER_BACKEND = BackendDescription(
    name=u"emc_vmax_flocker_plugin",  # name isn't actually used for 3rd party plugins
    needs_reactor=False, needs_cluster_id=True,
    api_factory=api_factory, deployer_type=DeployerType.block)

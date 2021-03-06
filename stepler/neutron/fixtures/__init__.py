"""
----------------
Neutron fixtures
----------------
"""

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .agents import *  # noqa
from .networks import *  # noqa
from .neutron import *  # noqa
from .neutron_resources import *  # noqa
from .ports import *  # noqa
from .routers import *  # noqa
from .subnets import *  # noqa


__all__ = sorted([  # sort for documentation
    'create_network',
    'network',
    'public_network',
    'baremetal_network',
    'create_port',
    'port',
    'create_subnet',
    'subnet',
    'create_router',
    'router',
    'add_router_interfaces',
    'create_port',
    'port_steps',
    'neutron_client',
    'get_neutron_client',
    'network_steps',
    'get_network_steps',
    'router_steps',
    'get_router_steps',
    'subnet_steps',
    'get_subnet_steps',
    'net_subnet_router',
    'neutron_2_servers_different_networks',
    'neutron_2_servers_same_network',
    'neutron_2_servers_iperf_different_networks',
    'get_agent_steps',
    'agent_steps',
])

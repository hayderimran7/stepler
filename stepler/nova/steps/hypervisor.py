"""
----------------
Hypervisor steps
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

from hamcrest import assert_that, empty, greater_than, is_not  # noqa

from stepler import base
from stepler.third_party import steps_checker

__all__ = [
    'HypervisorSteps'
]


class HypervisorSteps(base.BaseSteps):
    """Hypervisor steps."""

    @steps_checker.step
    def get_hypervisors(self, check=True):
        """Step to get hypervisors.

        Args:
            check (bool): flag whether to check step or not


        Returns:
            list: list of hyervisors objects

        Raises:
            AssertionError: if hypervisors list are empty
        """

        hypervisors = list(self._client.list())
        if check:
            assert_that(hypervisors, is_not(empty()))
        return hypervisors

    @steps_checker.step
    def get_hypervisor_capacity(self, hypervisor, flavor, check=True):
        """Step to get hypervisor capacity.

        This method calculates max available count of instances, which can be
        booted on hypervisor with choosen flavor.

        Args:
            hypervisor (obj): nova hypervisor
            flavor (obj): nova flavor
            check (bool): flag whether to check step or not

        Returns:
            int: possible instances count

        Raises:
            AssertionError: if capacity equal or less zero.
        """
        if hypervisor.vcpus < flavor.vcpus:
            capacity = 0
        if flavor.disk > 0:
            capacity = min(
                hypervisor.disk_available_least // flavor.disk,
                hypervisor.free_ram_mb // flavor.ram)
        else:
            capacity = hypervisor.free_ram_mb // flavor.ram

        if check:
            assert_that(capacity, greater_than(0))

        return capacity

    @steps_checker.step
    def get_another_hypervisor(self, server, check=True):
        """Step to get any hypervisor except server's one.

        Args:
            server (obj): nova server
            check (bool, optional): flag whether to check step or not

        Returns:
            obj: nova hypervisor

        Raises:
            ValueError: if there is no one hypervisor except server's one
        """
        server_hypervisor = getattr(server,
                                    'OS-EXT-SRV-ATTR:hypervisor_hostname')

        for hypervisor in self.get_hypervisors():
            if hypervisor.hypervisor_hostname != server_hypervisor:
                return hypervisor
        else:
            if check:
                raise ValueError(
                    'No available hypervisors except ' + server_hypervisor)

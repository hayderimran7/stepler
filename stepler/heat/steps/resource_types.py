"""
------------------------
Heat resource type steps
------------------------
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

from hamcrest import assert_that, is_not, empty  # noqa

from stepler import base
from stepler.third_party import steps_checker

__all__ = ['ResourceTypeSteps']


class ResourceTypeSteps(base.BaseSteps):
    """Heat resource type steps."""

    @steps_checker.step
    def get_resource_types(self, check=True):
        """Step to get list of resource types.

        Args:
            check (bool): flag whether check step or not

        Returns:
            list: resource types list for stack

        Raises:
            AssertionError: if list is empty
        """
        resource_types = self._client.list()

        if check:
            assert_that(resource_types, is_not(empty()))

        return resource_types

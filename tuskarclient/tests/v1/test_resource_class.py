# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import mock

from tuskarclient.v1 import resource_classes
import tuskarclient.tests.utils as tutils


class ResourceClassManagerTest(tutils.TestCase):
    def setUp(self):
        super(ResourceClassManagerTest, self).setUp()
        self.api = mock.Mock()
        self.rcm = resource_classes.ResourceClassManager(self.api)

    def test_get(self):
        self.rcm._get = mock.Mock(return_value='fake_resource_class')

        self.assertEqual(self.rcm.get(42), 'fake_resource_class')
        self.rcm._get.assert_called_with('/v1/resource_classes/42')

    def test_list(self):
        self.rcm._list = mock.Mock(return_value=['fake_resource_class'])

        self.assertEqual(self.rcm.list(), ['fake_resource_class'])
        self.rcm._list.assert_called_with('/v1/resource_classes')
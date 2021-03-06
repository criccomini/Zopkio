# Copyright 2014 LinkedIn Corp.
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import unittest

from zopkio.remote_host_helper import ParamikoError, better_exec_command, get_ssh_client

class TestDeployer(unittest.TestCase):
  def test_better_exec(self):
    """
    Tests that the better_exec in the deployer module works and detects failed
    commands
    """
    with get_ssh_client("127.0.0.1") as ssh:
      better_exec_command(ssh, "true", "This command succeeds")
      self.assertRaises(ParamikoError, better_exec_command, ssh,
                        "false", "This command fails")

if __name__ == '__main__':
  unittest.main()

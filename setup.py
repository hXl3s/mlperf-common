#!/usr/bin/env python
# Copyright (c) 2022, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()


setup(
    author="MLPerf",
    author_email="mlperf@local",  # TODO
    python_requires=">=3.8",
    description="MLPerf utilities for NVIDIA related submissions",
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    name="mlperf-common",
    packages=find_packages(where="."),
    scripts=['client/bindpcie','client/slurm2pytorch','client/mgpurun','client/mlperf-sysjson.sh','client/fastcp', 'client/truncate_log.sh', 'client/direct_io.py'],
    url="https://github.com/NVIDIA/mlperf-common",
    version="0.3",
)

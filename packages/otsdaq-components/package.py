# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack import *


class OtsdaqComponents(CMakePackage):
    """The toolkit currently provides functionality for data transfer,
    event building, event reconstruction and analysis (using the art analysis
    framework), process management, system and process state behavior, control
    messaging, local message logging (status and error messages), DAQ process
    and art module configuration, and the writing of event data to disk in ROOT
    format."""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/artdaq/wiki"
    url = "https://github.com/art-daq/otsdaq_components/archive/refs/tags/v2_06_08.tar.gz"
    git = "https://github.com/art-daq/otsdaq_components.git"

    version("develop", branch="develop", get_full_repo=True)
    version("v2_06_08", sha256="59bdb4fd6aab1fc97072890824530cf8c9db7e57bd9d9647faf8f32aaaada4a5")

    variant(
        "cxxstd",
        default="17",
        values=("14", "17"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    variant(
        "s",
        default="0",
        values=("0", "112", "117", "118"),
        multi=False,
        description="Art suite version to use",
    )
    depends_on("art-suite@s118", when="s=118")
    depends_on("art-suite@s117", when="s=117")
    depends_on("art-suite@s112", when="s=112")

    depends_on("cetmodules", type="build")

    with when('@develop'):
        depends_on("otsdaq")
        depends_on("otsdaq-utilities")
    with when('@v2_06_08'):
        depends_on("otsdaq@v2_06_08")
        depends_on("otsdaq-utilities@v2_06_08")


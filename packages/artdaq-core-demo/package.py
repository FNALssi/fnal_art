# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack import *


class ArtdaqCoreDemo(CMakePackage):
    """The toolkit currently provides functionality for data transfer,
    event building, event reconstruction and analysis (using the art analysis
    framework), process management, system and process state behavior, control
    messaging, local message logging (status and error messages), DAQ process
    and art module configuration, and the writing of event data to disk in ROOT
    format."""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/artdaq/wiki"
    url = "https://github.com/art-daq/artdaq_core_demo/archive/refs/tags/v1_10_02.tar.gz"
    git = "https://github.com/art-daq/artdaq_core_demo.git"

    version("develop", branch="develop", get_full_repo=True)
    version("v1_10_02", sha256="ea6b04590bfa158e1528bf4b46cc04a0a7b065848d48ba3ab1cf94ac1bc45389")


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
        depends_on("artdaq-core")
    with when('@v1_10_02'):
        depends_on("artdaq-core@v3_09_04")

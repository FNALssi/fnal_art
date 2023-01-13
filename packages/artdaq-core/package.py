# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack import *


class ArtdaqCore(CMakePackage):
    """The toolkit currently provides functionality for data transfer,
    event building, event reconstruction and analysis (using the art analysis
    framework), process management, system and process state behavior, control
    messaging, local message logging (status and error messages), DAQ process
    and art module configuration, and the writing of event data to disk in ROOT
    format."""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/artdaq/wiki"
    url = "https://github.com/art-daq/artdaq_core/archive/refs/tags/v3_09_04.tar.gz"
    git = "https://github.com/art-daq/artdaq_core.git"

    version("develop", branch="develop", get_full_repo=True)
    version("v3_09_04", sha256="8d4315e0ebe7b663d171352d8e08dd87393d34319f672837eb8c93ea83b8ba63")


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

    depends_on("canvas-root-io", when="s=0")
    depends_on("canvas-root-io@1.09.04", when="s=112")
    depends_on("canvas-root-io@1.09.05", when="s=117")
    depends_on("canvas-root-io@1.11.00", when="s=118")
    depends_on("cetmodules", type="build")

    with when('@develop'):
        depends_on("trace+mf")
    with when('@v3_09_04'):
        depends_on("trace@v3_17_07 +mf")

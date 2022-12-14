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
    url = "https://github.com/art-daq/artdaq_core/archive/refs/tags/v3_09_03.tar.gz"
    git = "https://github.com/art-daq/artdaq_core.git"

    version(
        "artdaq-v3_12_01",
        commit="49e62b4aeaaf4e459def6f74363760bb57c6201e",
        git_full_repo=True,
    )
    version("develop", branch="develop", get_full_repo=True)

    variant(
        "cxxstd",
        default="17",
        values=("14", "17"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    depends_on("art")
    depends_on("boost")
    depends_on("canvas")
    depends_on("canvas-root-io")
    depends_on("art-root-io")
    depends_on("cetmodules", type="build")
    depends_on("clhep")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("root")
    depends_on("sqlite")
    depends_on("tbb")
    depends_on("trace")

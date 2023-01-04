# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack import *


class Artdaq(CMakePackage):
    """The toolkit currently provides functionality for data transfer,
    event building, event reconstruction and analysis (using the art analysis
    framework), process management, system and process state behavior, control
    messaging, local message logging (status and error messages), DAQ process
    and art module configuration, and the writing of event data to disk in ROOT
    format."""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/artdaq/wiki"
    url = "https://github.com/art-daq/artdaq/archive/refs/tags/v3_09_03.tar.gz"
    git = "https://github.com/art-daq/artdaq.git"

    version("develop", branch="develop", get_full_repo=True)

    variant(
        "cxxstd",
        default="17",
        values=("14", "17"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    depends_on("artdaq-core")
    depends_on("artdaq-utilities")
    depends_on("xmlrpc-c+curl")
    depends_on("art-root-io")
    depends_on("cetmodules", type="build")
    depends_on("swig")
    depends_on("node-js")
    depends_on("artdaq-mfextensions")
    depends_on("trace+mf")

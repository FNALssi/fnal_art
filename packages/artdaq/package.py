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
    url = "https://github.com/art-daq/artdaq/archive/refs/tags/v3_12_02.tar.gz"
    git = "https://github.com/art-daq/artdaq.git"

    version("develop", branch="develop", get_full_repo=True)    
    version("v3_12_02", sha256="98baad840c49be9b16d8dc819a708505fa8601fcb42844c17c1013f9d75b728e")

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

    depends_on("art-root-io")
    
    depends_on("cetmodules", type="build")
    depends_on("xmlrpc-c+curl")
    depends_on("swig", type="build")
    depends_on("node-js", type="build")

    # Any version of dependencies when using develop
    with when('@develop'):
        depends_on("artdaq-core")
        depends_on("artdaq-utilities")
        depends_on("artdaq-mfextensions")

    # Use a certain version for tag
    with when('@v3_12_02'):
        depends_on("artdaq-core@v3_09_04")
        depends_on("artdaq-utilities@v1_08_02")
        depends_on("artdaq-mfextensions@v1_08_02")

    

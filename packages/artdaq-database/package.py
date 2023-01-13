# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack import *


class ArtdaqDatabase(CMakePackage):
    """The toolkit currently provides functionality for data transfer,
    event building, event reconstruction and analysis (using the art analysis
    framework), process management, system and process state behavior, control
    messaging, local message logging (status and error messages), DAQ process
    and art module configuration, and the writing of event data to disk in ROOT
    format."""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/artdaq/wiki"
    url = "https://github.com/art-daq/artdaq_database/archive/refs/tags/v1_07_02.tar.gz"
    git = "https://github.com/art-daq/artdaq_database.git"

    version("develop", branch="develop", get_full_repo=True)
    version("v1_07_02", sha256="8cb937967d16f25b59ee8e7104cd968956d892dbe24b29e393c5db982969e432")

    variant(
        "cxxstd",
        default="17",
        values=("14", "17"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )
    variant("builtin_fhicl", default=True, description="Use built-in FHiCL-cpp with database fixes")

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

    depends_on("curl")
    depends_on("boost+filesystem+program_options")
    depends_on("swig", type="build")
    depends_on("node-js", type="build")
    depends_on("python", type="build")

    depends_on("cetmodules", type="build")

    depends_on("cetlib", when="~builtin_fhicl")

    with when('@develop'):
        depends_on("trace+mf")
    with when('@v1_07_02'):
        depends_on("trace+mf@v3_17_07")

    def cmake_args(self):
        args = [self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
                "-DUSE_FHICLCPP={0}".format("TRUE" if "+builtin_fhicl" in self.spec else "FALSE")]
        return args

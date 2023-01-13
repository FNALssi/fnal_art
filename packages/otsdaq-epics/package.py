# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack import *


class OtsdaqEpics(CMakePackage):
    """The toolkit currently provides functionality for data transfer,
    event building, event reconstruction and analysis (using the art analysis
    framework), process management, system and process state behavior, control
    messaging, local message logging (status and error messages), DAQ process
    and art module configuration, and the writing of event data to disk in ROOT
    format."""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/artdaq/wiki"
    url = "https://github.com/art-daq/otsdaq_epics/archive/refs/tags/v2_06_08.tar.gz"
    git = "https://github.com/art-daq/otsdaq_epics.git"

    version("develop", branch="develop", get_full_repo=True)
    version("v2_06_08", sha256="5f24df325f4e27dfbd5a30892a80ba75a3eef642d60a759d1580f846f2e22813")


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
        values=("0", "112", "118"),
        multi=False,
        description="Art suite version to use",
    )

    depends_on("cetmodules", type="build")
    depends_on("epics")
    depends_on("libpqxx")

    with when('@develop'):
        depends_on("otsdaq")
        depends_on("otsdaq-utilities")
    with when('@v2_06_08'):
        depends_on("otsdaq@v2_06_08")
        depends_on("otsdaq-utilities@v2_06_08")

    depends_on('otsdaq s=0', when="s=0")
    depends_on('otsdaq s=118', when="s=118")
    depends_on('otsdaq s=112', when="s=112")

    depends_on('otsdaq-utilities s=0', when="s=0")
    depends_on('otsdaq-utilities s=118', when="s=118")
    depends_on('otsdaq-utilities s=112', when="s=112")


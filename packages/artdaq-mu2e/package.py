# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack import *


class ArtdaqMu2e(CMakePackage):
    """The toolkit currently provides functionality for data transfer,
    event building, event reconstruction and analysis (using the art analysis
    framework), process management, system and process state behavior, control
    messaging, local message logging (status and error messages), DAQ process
    and art module configuration, and the writing of event data to disk in ROOT
    format."""

    homepage = "https://github.com/Mu2e/artdaq_mu2e"
    url = "https://github.com/Mu2e/artdaq_mu2e/archive/refs/tags/v1_05_02.tar.gz"
    git = "https://github.com/Mu2e/artdaq_mu2e.git"

    version("develop", branch="develop", get_full_repo=True)
    version("v1_05_02", sha256="480fcd8580a11e08de55dbc0e71a16482e0de0ba23a4ac633ff2e2353877d3be")


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

    with when('@develop'):
        depends_on("artdaq")
        depends_on("artdaq-core-mu2e")
    with when('@v1_05_02'):
        depends_on("artdaq@v3_12_02")
        depends_on("artdaq-core-mu2e@v1_08_04")

    depends_on('artdaq s=0', when="s=0")
    depends_on('artdaq s=118', when="s=118")
    depends_on('artdaq s=112', when="s=112")

    depends_on('artdaq-core-mu2e s=0', when="s=0")
    depends_on('artdaq-core-mu2e s=118', when="s=118")
    depends_on('artdaq-core-mu2e s=112', when="s=112")
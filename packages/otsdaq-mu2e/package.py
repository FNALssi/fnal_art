# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from collections import defaultdict
import os
import sys

from spack import *


class OtsdaqMu2e(CMakePackage):
    """The toolkit currently provides functionality for data transfer,
    event building, event reconstruction and analysis (using the art analysis
    framework), process management, system and process state behavior, control
    messaging, local message logging (status and error messages), DAQ process
    and art module configuration, and the writing of event data to disk in ROOT
    format."""

    homepage = "https://github.com/Mu2e/otsdaq_mu2e"
    url = "https://github.com/Mu2e/otsdaq_mu2e/archive/refs/tags/v1_02_02.tar.gz"
    git = "https://github.com/Mu2e/otsdaq_mu2e.git"

    version("develop", branch="develop", get_full_repo=True)
    version("v1_02_02", commit="92aa08f")


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
    depends_on("art-suite@s118+root", when="s=118")
    depends_on("art-suite@s117+root", when="s=117")
    depends_on("art-suite@s112+root", when="s=112")

    depends_on("cetmodules", type="build")

    with when('@develop'):
        depends_on("otsdaq")
        depends_on("otsdaq-utilities")
        depends_on("otsdaq-components")
        depends_on("otsdaq-epics")
        depends_on("artdaq-mu2e")
    with when('@v1_02_02'):
        depends_on("otsdaq@v2_06_08")
        depends_on("otsdaq-utilities@v2_06_08")
        depends_on("otsdaq-components@v2_06_08")
        depends_on("otsdaq-epics@v2_06_08")
        depends_on("artdaq-mu2e@v1_05_02")


# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack import *


class ArtdaqMfextensions(CMakePackage):
    """The toolkit currently provides functionality for data transfer,
    event building, event reconstruction and analysis (using the art analysis
    framework), process management, system and process state behavior, control
    messaging, local message logging (status and error messages), DAQ process
    and art module configuration, and the writing of event data to disk in ROOT
    format."""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/artdaq/wiki"
    url = "https://github.com/art-daq/artdaq_mfextensions/archive/refs/tags/v1_08_02.tar.gz"
    git = "https://github.com/art-daq/artdaq_mfextensions.git"

    version("develop", branch="develop", get_full_repo=True)
    version("v1_08_02", sha256="d03b4261491bc879a34908c70f7f49cd64624ec889bfb8f486f7ce9fd1bd7f6b")

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
    depends_on("qt@5.15:")

    with when('@develop'):
        depends_on("trace+mf")
    with when('@v1_08_02'):
        depends_on("trace+mf@v3_17_07")



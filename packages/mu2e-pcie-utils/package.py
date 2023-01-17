# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack import *


class Mu2ePcieUtils(CMakePackage):
    """The toolkit currently provides functionality for data transfer,
    event building, event reconstruction and analysis (using the art analysis
    framework), process management, system and process state behavior, control
    messaging, local message logging (status and error messages), DAQ process
    and art module configuration, and the writing of event data to disk in ROOT
    format."""

    homepage = "https://github.com/Mu2e/pcie_linux_kernel_module/"
    url = "https://github.com/Mu2e/mu2e_pcie_utils/archive/refs/tags/v2_08_00.tar.gz"
    git = "https://github.com/Mu2e/mu2e_pcie_utils.git"

    version("develop", branch="develop", get_full_repo=True)
    version("2_08_00", sha256="75e70eddf2fbceaeb5e2bf0f0db8194fe2050b95a3b73fdcbe0d3b2b324732a2")

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
    depends_on("messagefacility")

    with when('@develop'):
        depends_on("trace+kmod")
    with when('@2_08_00'):
        depends_on("trace+kmod@3_17_07")

    

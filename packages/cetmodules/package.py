# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

import spack.util.spack_json as sjson
from spack.package import *


class Cetmodules(CMakePackage):
    """CMake glue modules and scripts required by packages originating at
    Fermilab and associated experiments and other collaborations.
    """

    homepage = "https://fnalssi.github.io/cetmodules/"
    git = "https://github.com/FNALssi/cetmodules.git"
    url = "https://github.com/FNALssi/cetmodules/archive/refs/tags/3.19.02.tar.gz"

    maintainers = ["chissg", "gartung", "marcmengel", "vitodb"]

    version("develop", branch="develop", get_full_repo=True)
    version("3.19.02", sha256="214172a59f4c3875a5d7c2617b9f50ed471c86404d85e2e5c72cadf5b499cdc6")

    depends_on("cmake@3.11:", type="build", when="@:1.01.99")
    depends_on("cmake@3.12:", type="build", when="@1.02.00:")
    depends_on("cmake@3.18:", type="build", when="@2.07.00:")
    depends_on("py-sphinxcontrib-moderncmakedomain", when="@2.00.10:", type="build")
    depends_on("py-sphinxcontrib-moderncmakedomain", when="@develop", type="build")
    depends_on("py-sphinx-rtd-theme", when="@2.00.10:", type="build")
    depends_on("py-sphinx-rtd-theme", when="@develop", type="build")

    @run_before("cmake")
    def fix_fix_man(self):
        filter_file(r"exit \$status", "exit 0", "%s/libexec/fix-man-dirs" % self.stage.source_path)


    def setup_run_environment(self, run_env):
        run_env.prepend_path("CMAKE_PREFIX_PATH", "{0}/Modules".format(self.prefix))

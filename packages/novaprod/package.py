# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Novaprod(Package):
    """NOvA production toolkit"""

    homepage = "https://www.github.com/novaexperiment/novaprod"
    git = "git@github.com:novaexperiment/novaprod"

    maintainers("vhewes")

    version("develop", branch="main")
    version("7.02", tag="novaproduction-v07.02")

    depends_on("py-future")
    depends_on("sam-web-client")

    extends("python")

    def install(self, spec, prefix):
        mkdirp(prefix.bin, python_platlib)

        # binaries
        install("NovaGridUtils/bin/recommended_sites.py", prefix.bin)
        install("NovaGridUtils/bin/setup_fnal_security", prefix.bin)
        install("NovaGridUtils/bin/submit_cafana.py", prefix.bin)
        install("NovaGridUtils/bin/cafe_grid_script.sh", prefix.bin)
        install("NovaGridUtils/bin/sl7-nova", prefix.bin)

        # python libraries
        install("NovaGridUtils/lib/python/NovaGridUtils.py", python_platlib)

    def setup_run_environment(self, env):
        env.set("GROUP", "nova")
        env.set("NOVAGRIDUTILS_DIR", self.prefix)
        env.set("IFDH_DEBUG", "0")
        env.set("SAM_STATION", "nova")

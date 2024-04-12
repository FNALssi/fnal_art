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

    version("6.98", tag="novaproduction-v06.98")

    depends_on("py-future")
    depends_on("sam-web-client")

    extends("python")

    def install(self, spec, prefix):
        mkdirp(prefix.bin, python_platlib)
        install("NovaGridUtils/bin/submit_cafana.py", prefix.bin)
        install("NovaGridUtils/bin/submit_nova_art.py", prefix.bin)
        install("NovaGridUtils/bin/recommended_sites.py", prefix.bin)
        install("NovaGridUtils/bin/cafe_grid_script.sh", prefix.bin)

        # python libraries
        install("NovaGridUtils/lib/python/NovaGridUtils.py", python_platlib)
        install("novaproduction/lib/python/fake_sam.py", python_platlib)

    def setup_run_environment(self, env):
        env.set("GROUP", "nova")
        env.set("NOVAGRIDUTILS_DIR", self.prefix)

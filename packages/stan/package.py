# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Stan(Package):
    """C++ package for Bayesian inference"""

    homepage = "https://mc-stan.org/"
    url = "https://github.com/stan-dev/stan/archive/v2.26.0.tar.gz"

    maintainers = ["marc.mengel@gmail.com"]

    version("2.26.0", sha256="3b6ff0cbeddaa5b0f94692862d7a2266d12c3e7a6833ea0f5c7c20ff7b28907a")
    version("2.25.0", sha256="9c2f936be00f28f95b58e061e95b5a81990b978001eb9df5b03f7803906b1d78")
    version("2.24.0", sha256="f398098eb030036d23b2a8e131598bc89c2e4fa5e85be9ab1d0a8b0d91739f99")

    depends_on("stan-math")

    def install(self, spec, prefix):
        install_tree("src", prefix.include)

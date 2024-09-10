# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Osclib(CMakePackage):
    """Neutrino oscillation probability tools."""

    homepage = "https://github.com/cafana/OscLib"
    url = "https://github.com/cafana/OscLib/archive/v00.25.tar.gz"

    maintainers("vhewes")

    version("00.25", sha256="ee4f4120e414acb065ad967bda9de12e7a5594e6539b25b721084c8f112a3f4c")

    depends_on("cetmodules", type="build")

    depends_on("root")
    depends_on("boost")
    depends_on("eigen")

    with when("+stan"):
        depends_on("stan-math")
        depends_on("intel-tbb@2020.3")

    variant("stan", default=True, description="Build with Stan dependency")

    def setup_build_environment(self, env):
        # need to set up STAN_MATH_INC so Findstan_math.cmake will work as-is
        if self.spec.satisfies("+stan"):
            env.set("STAN_MATH_INC", self.spec["stan-math"].prefix)

    def cmake_args(self):
        return [self.define_from_variant("STAN", "stan")]

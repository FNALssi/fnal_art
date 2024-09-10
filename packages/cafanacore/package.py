# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Cafanacore(CMakePackage):
    """Base libraries of the CAFAna analysis framework"""

    homepage = "https://github.com/cafana/CAFAnaCore"
    git = "https://github.com/cafana/CAFAnaCore"

    maintainers("vhewes")

    version("develop", branch="main")

    variant("stan", default=True, description="Build with Stan Math support")
    variant("ifdhc", default=True, description="Build with IFDHC support")

    depends_on("cetmodules", type="build")
    depends_on("boost")
    depends_on("osclib")
    depends_on("osclib+stan", when="+stan")
    depends_on("stan-math")
    depends_on("ifdhc", when="+ifdhc")

    def setup_build_environment(self, env):
        # stan-math
        env.set("STAN_MATH_INC", self.spec["stan-math"].prefix)

        # ifdhc
        if self.spec.satisfies("+ifdhc"):
            env.set("IFDHC_DIR", self.spec["ifdhc"].prefix)
            env.set("IFDHC_FQ_DIR", self.spec["ifdhc"].prefix)
            env.set("IFDHC_VERSION", self.spec["ifdhc"].version)
            env.set("IFDHC_LIB", self.spec["ifdhc"].prefix.lib)

    def cmake_args(self):
        return [
            self.define("NO_IFDHC", self.spec.satisfies("~ifdhc")),
            self.define_from_variant("STAN", "stan")
        ]
        

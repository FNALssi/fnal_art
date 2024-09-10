# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Cafanacore(CMakePackage):
    """Base libraries of the CAFAna analysis framework"""

    homepage = "https://github.com/cafana/CAFAnaCore"
    url = "https://github.com/cafana/CAFAnaCore/archive/v02.01.tar.gz"

    maintainers("vhewes")

    version("02.01", sha256="cb747ef71586bead03233ef58ad038c8e133b7c210971e8e6ba6df0cbef7e1ae")

    variant("stan", default=True, description="Build with Stan Math support")
    variant("ifdhc", default=True, description="Build with IFDHC support")
    variant("cxxstd", values=("17", "20", "23"), default="17", multi=False,
            sticky=True, description="C++ standard")

    depends_on("cetmodules", type="build")
    depends_on("boost")
    depends_on("osclib")
    depends_on("osclib+stan", when="+stan")
    depends_on("stan-math")
    depends_on("ifdhc", when="+ifdhc")

    def setup_build_environment(self, env):

        # stan-math
        env.set("STAN_MATH_DIR", self.spec["stan-math"].prefix)
        env.set("STAN_MATH_VERSION", self.spec["stan-math"].version)
        env.set("STAN_MATH_INC", self.spec["stan-math"].prefix)

        # sundials
        env.set("SUNDIALS_INC", self.spec["sundials"].prefix.include)

        # ifdhc
        if self.spec.satisfies("+ifdhc"):
            env.set("IFDHC_DIR", self.spec["ifdhc"].prefix)
            env.set("IFDHC_FQ_DIR", self.spec["ifdhc"].prefix)
            env.set("IFDHC_VERSION", self.spec["ifdhc"].version)
            env.set("IFDHC_INC", self.spec["ifdhc"].prefix.inc)
            env.set("IFDHC_LIB", self.spec["ifdhc"].prefix.lib)

    def cmake_args(self):
        return [
            self.define("SPACK", "YES"),
            self.define("CAFANACORE_VERSION", self.spec.version),
            self.define("NO_IFDHC", self.spec.satisfies("~ifdhc")),
            self.define_from_variant("STAN", "stan"),
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
        ]

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class NuhepmcCmakeModules(CMakePackage):
    """CMake Modules for neutrino event generator tools."""

    homepage = "https://github.com/NuHepMC/CMakeModules"
    url = "https://github.com/NuHepMC/CMakeModules/archive/v0.2.5.tar.gz"

    license("UNKNOWN")

    version("0.2.5", sha256="8ecc2eeae1fb25779736b57ff5d660e8cd747b038d91b4433bedf58d36ee7673")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake", type="build")

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.set("NuHepMCModules_ROOT", self.spec.prefix.cmake)

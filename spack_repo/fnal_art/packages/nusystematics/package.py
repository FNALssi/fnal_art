# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Nusystematics(CMakePackage):
    """Neutrino interaction systematics for GENIE3 events."""

    homepage = "https://github.com/NuSystematics/nusystematics"
    url = "https://github.com/LArSoft/nusystematics/archive/v1_05_07.tar.gz"

    def url_for_version(self, version):
        org = "NuSystematics" if version[0] >= 2 else "LArSoft"
        return f"https://github.com/{org}/nusystematics/archive/v{version.underscored}.tar.gz"

    license("UNKNOWN")

    version("02.00.05", sha256="89cad28d6f01b248e2a9b255d4b6256de5b8cf31937c3a105a311589784c58aa")
    version("1.06.02", sha256="13b306cef60fad91ca35bde40fdefbcb55411804864caa1b9812ec1cdffb50cc")
    version("1.05.14", sha256="775ee40a132f1f00bb3900f71b7ffcb1b7366e98de20e9561d28307debd2e7af")
    version("1.05.07", sha256="8d273475c43cd42cb62f5a66f6fd6bcd90c6ad3cb9b8592c0ca24982356a2db5")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("nugen")
    depends_on("systematicstools")
    depends_on("nufinder")
    depends_on("cetmodules", type="build")
    depends_on("cmake", type="build")
    depends_on("nuhepmc-cmake-modules", type="build")

    with when("@=02.00.05"):
        depends_on("systematicstools @02.00.03")

    def setup_build_environment(self, env):
        env.set("CPM_LOCAL_PACKAGES_ONLY", "1")
        env.set("PYTHIA6_LIB_DIR", self.spec["pythia6"].prefix.lib)

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.set("PYTHIA6_LIB_DIR", self.spec["pythia6"].prefix.lib)

    def cmake_args(self):
        args = []
        return args

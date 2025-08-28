# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.fnal_art.packages.fnal_github_package.package import *
from spack.package import *


class Tpythia6(CMakePackage, FnalGithubPackage):
    """TPythia6 library extracted from ROOT 6.28.X"""

    homepage = "https://github.com/ShipSoft/TPythia6"
    url = "https://github.com/ShipSoft/TPythia6"

    maintainers("gartung")

    license("LGPL2_1", checked_by="gartung")

    version("main", branch="main", git="https://github.com/ShipSoft/TPythia6.git")

    cxxstd_variant("17", "20", default="17")

    patch("targets.patch")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("nufinder", type="build")
    depends_on("root")
    depends_on("pythia6")

    def cmake_args(self):
        args = [
                self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
                self.define("CMAKE_MODULE_PATH", self.spec["nufinder"].prefix.Modules),
            ]
        return args

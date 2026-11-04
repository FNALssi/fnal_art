# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems import cmake, makefile
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage
from spack.package import *


class Marley(MakefilePackage, CMakePackage):
    """A Monte Carlo event generator for tens-of-MeV neutrino-nucleus
    interactions in liquid argon"""

    homepage = "https://github.com/MARLEY-MC/marley"
    url = "https://github.com/MARLEY-MC/marley/archive/v1.2.1.tar.gz"

    version("2.1.0", sha256="2d32ee1f57b41fbb480076a8a2fc6a076301f9fc5eafab4e9cfe0d57442aab54")
    version("2.0.0", sha256="db5011af0b8fe98bd54ecbbc31c52d00aacaff4ad1577c320f7569390f34cb36")
    version("1.2.1", sha256="75e8e4acbbcf7ad9de0ef629ac9e8764ebf90fda2242ff5e6e590e77f9df6972")
    version("1.2.0", sha256="8bb0a68924c8e5d7773904151e3134c6c59837723ecf4e1b586a6cb5b48b520d")
    version("1.0.0", sha256="4dea9918cff0aed3b9c38f74351c373c32235496ca6e321078f2c7b56bce719e")
    version("1.1.0", sha256="04d484468d08e5447dfd2fde20bea5bbebfd04ecb6eb34ad65b30f3825bcd577")
    version("1.1.1", sha256="214f8a40e59d47dd563be53640c5f197f5529bcb0ee65a9402cca450a611c0f8")

    variant(
        "cxxstd",
        default="17",
        values=("98", "11", "14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    build_system(
        conditional("cmake", when="@2.0:"),
        conditional("makefile", when="@:1.2.1"),
        default="cmake",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.18:", type="build", when="build_system=cmake")
    depends_on("gsl")
    depends_on("root")
    depends_on("root@6.22:", when="@2.0:")

    # MARLEY 2.x requires at least C++17 (its CMake floor); ROOT must have been
    # built with the same standard that MARLEY is built with.
    conflicts("cxxstd=98", when="@2.0:")
    conflicts("cxxstd=11", when="@2.0:")
    conflicts("cxxstd=14", when="@2.0:")
    for _std in ("11", "14", "17", "20"):
        depends_on(f"root cxxstd={_std}", when=f"cxxstd={_std}")

    patch("marley-1.0.0.patch", when="@1.0.0")
    patch("marley-1.1.0.patch", when="@1.1.0")
    patch("marley-1.1.1.patch", when="@1.1.1")
    patch("marley-1.2.0.patch", when="@1.2.0")
    patch("marley-1.2.1.patch", when="@1.2.1")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("PATH", self.prefix.bin)
        env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)
        if self.spec.satisfies("@2.0:"):
            # Vendored HepMC3 headers, needed to parse MARLEY headers in ROOT
            env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include.marley.builtin)
        else:
            # MARLEY 2.x locates its data relative to libMARLEY; 1.x needs this
            data = self.prefix.share.marley.data
            env.append_path("FW_SEARCH_PATH", data)
            env.append_path("FW_SEARCH_PATH", data.react)
            env.append_path("FW_SEARCH_PATH", data.structure)


class CMakeBuilder(cmake.CMakeBuilder):
    def cmake_args(self):
        return [self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd")]


class MakefileBuilder(makefile.MakefileBuilder):
    @property
    def build_directory(self):
        return join_path(self.pkg.stage.source_path, "build")

    @run_before("edit")
    def set_cxxstd(self):
        cxxstd = self.spec.variants["cxxstd"].value
        filter_file(r"CXX_STD=c\+\+14", f"CXX_STD=c++{cxxstd}", "build/Makefile")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.append_flags("CPPFLAGS", "-I../include")
        cxxstd_flag = "cxx{0}_flag".format(self.spec.variants["cxxstd"].value)
        env.append_flags("CXXFLAGS", getattr(self.pkg.compiler, cxxstd_flag))

    def install(self, pkg, spec, prefix):
        with working_dir(self.build_directory):
            pkg.module.make(f"prefix={prefix}", "install")

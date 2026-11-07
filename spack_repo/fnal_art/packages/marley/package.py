# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakeBuilder, CMakePackage
from spack_repo.builtin.build_systems.makefile import MakefileBuilder, MakefilePackage

from spack.package import *


class Marley(CMakePackage, MakefilePackage):
    """A Monte Carlo event generator for tens-of-MeV neutrino-nucleus
    interactions in liquid argon"""

    homepage = "https://github.com/MARLEY-MC/marley"
    url = "https://github.com/MARLEY-MC/marley/archive/v1.2.1.tar.gz"

    version("2.1.0", sha256="2d32ee1f57b41fbb480076a8a2fc6a076301f9fc5eafab4e9cfe0d57442aab54")
    version("1.2.1", sha256="75e8e4acbbcf7ad9de0ef629ac9e8764ebf90fda2242ff5e6e590e77f9df6972")
    version("1.2.0", sha256="8bb0a68924c8e5d7773904151e3134c6c59837723ecf4e1b586a6cb5b48b520d")
    version("1.0.0", sha256="4dea9918cff0aed3b9c38f74351c373c32235496ca6e321078f2c7b56bce719e")
    version("1.1.0", sha256="04d484468d08e5447dfd2fde20bea5bbebfd04ecb6eb34ad65b30f3825bcd577")
    version("1.1.1", sha256="214f8a40e59d47dd563be53640c5f197f5529bcb0ee65a9402cca450a611c0f8")

    # MARLEY added a CMake build path in v2. It is preferred over a
    # hand-written Makefile which is also still provided.
    build_system(
        conditional("cmake", when="@2:"), conditional("makefile", when="@:1"), default="cmake"
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("root")
    depends_on("gsl")

    with when("build_system=cmake"):
        depends_on("cmake@3.18:", type="build")
        depends_on("hepmc3")

    with when("build_system=makefile"):
        depends_on("gmake", type="build")

    variant(
        "cxxstd",
        default="17",
        values=("98", "11", "14", "17", "20"),
        multi=False,
        when="@:1",
        description="Use the specified C++ standard when building.",
    )

    # v2 requires C++17. The value given is a floor: MARLEY raises it to match
    # ROOT when ROOT was built with a later standard, since it links ROOT's
    # targets PUBLIC.
    variant(
        "cxxstd",
        default="17",
        values=("17", "20", "23"),
        multi=False,
        when="@2:",
        description="Use the specified C++ standard when building.",
    )

    patch("marley-1.0.0.patch", when="@1.0.0")
    patch("marley-1.1.0.patch", when="@1.1.0")
    patch("marley-1.1.1.patch", when="@1.1.1")
    patch("marley-1.2.0.patch", when="@1.2.0")
    patch("marley-1.2.1.patch", when="@1.2.1")

    @when("@:1")
    def patch(self):
        cxxstd = self.spec.variants["cxxstd"].value
        filter_file("CXX_STD=c\+\+14", f"CXX_STD=c\+\+{cxxstd}", "build/Makefile")

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.bin)
        env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)

        # v1 has no way to locate its own data files, so every consumer has to
        # be told where they are. v2 resolves them from the installed
        # libMARLEY and needs nothing set; "marley info" reports what it found.
        if self.spec.satisfies("@:1"):
            env.append_path("FW_SEARCH_PATH", self.prefix.share.data)
            env.append_path("FW_SEARCH_PATH", self.prefix.share.data.react)
            env.append_path("FW_SEARCH_PATH", self.prefix.share.data.structure)


class CMakeBuilder(CMakeBuilder):
    def cmake_args(self):
        # Name the discovery route for each dependency rather than leaving it
        # to MARLEY's "auto" search. Under "auto" a dependency that fails to
        # turn up is replaced by a vendored copy or dropped, and the build
        # succeeds; naming the route turns that into a configure error.
        return [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define("GSL_FIND_MODE", "cmake"),
            self.define("HEPMC3_FIND_MODE", "cmake"),
            self.define("ROOT_FIND_MODE", "cmake"),
        ]


class MakefileBuilder(MakefileBuilder):
    def setup_build_environment(self, env):
        env.append_flags("CPPFLAGS", "-I../include")
        cxxstd_flag = "cxx{0}_flag".format(self.pkg.spec.variants["cxxstd"].value)
        env.append_flags("CXXFLAGS", getattr(self.pkg.compiler, cxxstd_flag))

    def build(self, pkg, spec, prefix):
        with working_dir("build"):
            make()

    def install(self, pkg, spec, prefix):
        with working_dir("build"):
            make("prefix={0}".format(prefix), "install")

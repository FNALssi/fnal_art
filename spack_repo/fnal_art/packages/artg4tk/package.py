# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.fnal_art.packages.fnal_github_package.package import *
from spack.package import *


class Artg4tk(CMakePackage,FnalGithubPackage):
    """Artg4tk"""

    homepage = "https://github.com/art-framework-suite/art-g4tk/"
    git = "https://github.com/art-framework-suite/art-g4tk"
    version_patterns = ['v13_00_02']

    version("13.01.02", sha256="72139413640db927fc7049850b04c39cd87f512c9615e4f8a17b112edaf92d7a")
    version("13.01.01", sha256="9db3d36c55b70772510929eae8eeb66beb3e5cbf6ef57fff952169e5bd58e97c")
    version("13.01.00", sha256="784fadde426fedc7b9e081005099f06d4ec6c659c59887c1c6c7238a6f01274f")
    version("13.00.02", sha256="0bdba091c1b17326fc8185495572494e285a0e40bf93e3244b257d670890517a")
    version("13.00.01", sha256="fe09f4d007c643160f996baf8c046488ff1e46f160332373130573e44b578089")
    version("13.00.00", sha256="451cab497901836b4bbd939cafef26d45a6ff425df1cfb6dea1761385433f73d")
    version("develop", branch="develop", get_full_repo=True)

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    patch("cetmodules2-c06a0ed7a0a543cba5c23fc588f7dd6dcb6609e2.patch", when="@c06a0ed7a0")
    patch("11.00.01.patch", when="@11.00.01")
    # patch('mwm.patch')
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cetmodules", type="build")
    depends_on("cetbuildtools", type="build")
    depends_on("art")
    depends_on("art-root-io")
    depends_on("canvas-root-io")
    depends_on("geant4@:10.6.1", when="@:12")
    depends_on("geant4@11.2.2:", when="@13:")
    depends_on("root")
    depends_on("boost")

    def cmake_args(self):
        args = [self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd")]
        return args

    def flag_handler(self, name, flags):
        if name == "cxxflags" and self.spec.compiler.name == "gcc":
            flags.append("-Wno-error=deprecated-declarations")
            flags.append("-Wno-error=class-memaccess")
        return (flags, None, None)

    def setup_build_environment(self, spack_env):
        spack_env.set("CETBUILDTOOLS_VERSION", self.spec["cetmodules"].version)
        spack_env.set("CETBUILDTOOLS_DIR", self.spec["cetmodules"].prefix)
        spack_env.set("LD_LIBRARY_PATH", self.spec["root"].prefix.lib)

    def setup_run_environment(self, run_env):
        run_env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)
        run_env.append_path("FHICL_FILE_PATH", "{0}/fcl".format(self.prefix))
        run_env.append_path("CET_PLUGIN_PATH", self.prefix.lib)

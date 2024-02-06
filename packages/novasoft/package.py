# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Novasoft(CMakePackage, MakefilePackage):
    """NOvA offline code repository."""

    build_system("cmake", "makefile", default="cmake")

    homepage = "https://www.github.com/novaexperiment/novasoft"
    git = "git@github.com:novaexperiment/novasoft"

    maintainers("vhewes")
    # license("Apache-2.0", checked_by="vhewes")

    version("develop", branch="feature/vhewes-spack")

    # variant(
    #     "cxxstd",
    #     default="17",
    #     values=("17", "20", "23"),
    #     multi=False,
    #     sticky=True,
    #     description="C++ standard",
    # )

    depends_on("art")
    depends_on("boost+math+serialization")
    depends_on("geant4")
    depends_on("ifdh-art")
    depends_on("ifdhc")
    depends_on("libwda")
    depends_on("log4cpp")
    depends_on("nufinder")
    depends_on("nusimdata")
    depends_on("postgresql")
    depends_on("xerces-c")

    # CMake build system
    with when("build_system=cmake"):

        # CMake dependencies
        depends_on("cetmodules", type="build")

        # def cmake_args(self):
        #     args = [ '--trace' ]
        #     return args

        # def setup_build_environment(self, spack_env):
        #     # Binaries.
        #     spack_env.prepend_path("PATH", os.path.join(self.build_directory, "bin"))
        #     # Ensure we can find plugin libraries.
        #     spack_env.prepend_path("CET_PLUGIN_PATH", os.path.join(self.build_directory, "lib"))
        #     # Ensure Root can find headers for autoparsing.
        #     for d in self.spec.traverse(
        #         root=False, cover="nodes", order="post", deptype=("link"), direction="children"
        #     ):
        #         spack_env.prepend_path("ROOT_INCLUDE_PATH", str(self.spec[d.name].prefix.include))
        #     # Perl modules.
        #     spack_env.prepend_path("PERL5LIB", os.path.join(self.build_directory, "perllib"))
        #     # Cleaup.
        #     sanitize_environments(spack_env)

        # def setup_run_environment(self, run_env):
        #     # Ensure we can find plugin libraries.
        #     run_env.prepend_path("CET_PLUGIN_PATH", self.prefix.lib)
        #     # Ensure Root can find headers for autoparsing.
        #     for d in self.spec.traverse(
        #         root=False, cover="nodes", order="post", deptype=("link"), direction="children"
        #     ):
        #         run_env.prepend_path("ROOT_INCLUDE_PATH", str(self.spec[d.name].prefix.include))
        #     run_env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)
        #     # Perl modules.
        #     run_env.prepend_path("PERL5LIB", os.path.join(self.prefix, "perllib"))
        #     # Cleaup.
        #     sanitize_environments(run_env)

        # def setup_dependent_build_environment(self, spack_env, dependent_spec):
        #     # Binaries.
        #     spack_env.prepend_path("PATH", self.prefix.bin)
        #     # Ensure we can find plugin libraries.
        #     spack_env.prepend_path("CET_PLUGIN_PATH", self.prefix.lib)
        #     # Ensure Root can find headers for autoparsing.
        #     spack_env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)
        #     # Perl modules.
        #     spack_env.prepend_path("PERL5LIB", os.path.join(self.prefix, "perllib"))
        #     # Cleanup.
        #     sanitize_environments(spack_env)

        # def setup_dependent_run_environment(self, run_env, dependent_spec):
        #     # Binaries.
        #     run_env.prepend_path("PATH", self.prefix.bin)
        #     # Ensure we can find plugin libraries.
        #     run_env.prepend_path("CET_PLUGIN_PATH", self.prefix.lib)
        #     # Ensure Root can find headers for autoparsing.
        #     run_env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)
        #     # Perl modules.
        #     run_env.prepend_path("PERL5LIB", os.path.join(self.prefix, "perllib"))
        #     # Cleanup.
        #     sanitize_environments(run_env)

    # gmake build system
    with when("build_system=makefile"):

        # gmake dependencies
        depends_on("gmake", type="build")

        # SRT build environment
        def setup_build_environment(self, env):
            # env.set("MAKEFLAGS", "-I/cvmfs/nova-development.opensciencegrid.org/novasoft/releases/development/include -I/cvmfs/nova-development.opensciencegrid.org/novasoft/releases/development/include/SRT_NOVA")
            env.set("SRT_CXX", "GCC")
            env.set("SRT_ARCH", "Linux3.1")

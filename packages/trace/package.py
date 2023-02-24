# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import os
import sys
from spack.util.environment import EnvironmentModifications
from llnl.util.filesystem import join_path

from spack import *

def sanitize_environments(env, *vars):
    for var in vars:
        env.prune_duplicate_paths(var)
        env.deprioritize_system_paths(var)

class Trace(CMakePackage):
    """TRACE is yet another logging (time stamp) tool, but it allows
    fast and/or slow logging - dynamically (you choose)."""

    homepage = "https://github.com/art-daq/trace"
    url = "https://github.com/art-daq/trace/archive/refs/tags/v3_17_07.tar.gz"
    git = "https://github.com/art-daq/trace.git"

    parallel = False

    depends_on("cetmodules", type="build")

    version("develop", branch="develop", get_full_repo=True)
    version("v3_17_07", commit="acd94af")
    version("v3_17_06", commit="4173644")



    if "SPACK_CMAKE_GENERATOR" in os.environ:
        generator = os.environ["SPACK_CMAKE_GENERATOR"]
        if generator.endswith("Ninja"):
            depends_on("ninja@1.10:", type="build")

    variant("kmod", default=True, description="Create Linux kernel module")
    variant("mf", default=False, description="Compile MessageFacility library")

    depends_on("messagefacility", when="+mf")

    def cmake_args(self):
        args = ["-DWANT_KMOD={0}".format("TRUE" if "+kmod" in self.spec else "FALSE"),"-DWANT_MF={0}".format("TRUE" if "+mf" in self.spec else "FALSE")]
        return args

    def setup_build_environment(self, env):
        prefix = self.build_directory
        # Binaries.
        env.prepend_path("PATH", os.path.join(prefix, "bin"))
        # Ensure we can find plugin libraries.
        env.prepend_path("CET_PLUGIN_PATH", os.path.join(prefix, "lib"))
        # Perl modules.
        env.prepend_path("PERL5LIB", os.path.join(prefix, "perllib"))
        # Cleaup.
        sanitize_environments(env, "PATH", "CET_PLUGIN_PATH", "PERL5LIB")

    def setup_run_environment(self, env):
        prefix = self.prefix 

        # Source the functions
        file_to_source = self.prefix.join("bin/trace_functions.sh")
        print(f'source {file_to_source}')
        
        # Binaries.
        env.prepend_path("PATH", os.path.join(prefix, "bin"))
        # Ensure we can find plugin libraries.
        env.prepend_path("CET_PLUGIN_PATH", os.path.join(prefix, "lib"))
        # Perl modules.
        env.prepend_path("PERL5LIB", os.path.join(prefix, "perllib"))
        # Cleaup.
        sanitize_environments(env, "PATH", "CET_PLUGIN_PATH", "PERL5LIB")

    def setup_dependent_build_environment(self, env, dependent_spec):
        prefix = self.prefix
        # Binaries.
        env.prepend_path("PATH", os.path.join(prefix, "bin"))
        # Ensure we can find plugin libraries.
        env.prepend_path("CET_PLUGIN_PATH", os.path.join(prefix, "lib"))
        # Perl modules.
        env.prepend_path("PERL5LIB", os.path.join(prefix, "perllib"))
        # Cleaup.
        sanitize_environments(env, "PATH", "CET_PLUGIN_PATH", "PERL5LIB")

    def setup_dependent_run_environment(self, env, dependent_spec):
        prefix = self.prefix

        # Source the functions
        file_to_source = self.prefix.join("bin/trace_functions.sh")
        print(f'source {file_to_source}')
             
        # Binaries.
        env.prepend_path("PATH", os.path.join(prefix, "bin"))
        # Ensure we can find plugin libraries.
        env.prepend_path("CET_PLUGIN_PATH", os.path.join(prefix, "lib"))
        # Perl modules.
        env.prepend_path("PERL5LIB", os.path.join(prefix, "perllib"))
        # Cleaup.
        sanitize_environments(env, "PATH", "CET_PLUGIN_PATH", "PERL5LIB")

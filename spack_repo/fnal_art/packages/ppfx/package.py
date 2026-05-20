# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Ppfx(CMakePackage):
    """Package to Predict the FluX"""

    homepage = "https://github.com/NuSoftHEP/ppfxv2"
    homepage_soon = "https://github.com/kordosky/ppfx"
    git = "https://github.com/kordosky/ppfx"
    url = "https://github.com/NuSoftHEP/ppfxv2/archive/v02_18_03.tar.gz"
    url_soon = "https://github.com/kordosky/ppfx/archive/tag/v02.13.03.tar.gz"

    maintainers = ["marcmengel", "kordosky"]

    def url_for_version(self, version):
        if version[0] < 3:
            return f"https://github.com/NuSoftHEP/ppfxv2/archive/v{version.underscored}.tar.gz"
        return f"https://github.com/kordosky/ppfx/archive/tag/v{version}.tar.gz"

    version("02.20.05", sha256="d01a7e5cff2502700ad4adc9c9dd17d405c262a1544351fc3f3f23fcbc325ba5")
    version("02.20.03", sha256="6639c2aef59e7e45e22bb7fce2f61fda025ce6233b829facdf49a84eede521a8")
    version("02.18.05", sha256="182ab28fbdcd1e8a0f436fe8396273e9ce97b2100cb97cf30c4a8a5d95ccbfad")
    version("02.18.03", sha256="e5e76a9a510abc0c3b5d517e6866e5394e8a58bee1e22a2b2a2552dbf5d2ad45")

    variant(
        "cxxstd",
        default="17",
        values=("17", "20", "23"),
        multi=False,
        sticky=True,
        description="C++ standard",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cetmodules", type="build")
    depends_on("cetbuildtools", type="build")
    depends_on("doxygen", type="build")
    depends_on("nufinder", type="build")

    depends_on("art")
    depends_on("boost")
    depends_on("canvas")
    depends_on("canvas-root-io")
    depends_on("cetbuildtools")
    depends_on("cry")
    depends_on("dk2nudata")
    depends_on("dk2nugenie")
    depends_on("fftw")
    depends_on("genie")
    depends_on("ifdh-art")
    depends_on("ifdhc")
    depends_on("lhapdf")
    depends_on("libwda")
    depends_on("libxml2")
    depends_on("log4cpp")
    depends_on("nusimdata")
    depends_on("postgresql")
    depends_on("pythia6")
    depends_on("root")
    depends_on("xerces-c")

    def cmake_args(self):
        args = [self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"), "-Dppfx_FW_DIR=fw"]
        return args

    def setup_build_environment(self, env):
        env.set("CANVAS_ROOT_IO_DIR", self.spec["canvas"].prefix)
        env.set("CETBUILDTOOLS_DIR", self.spec["cetbuildtools"].prefix)
        env.set("CRYHOME", self.spec["cry"].prefix)
        env.set("DK2NUDATA_LIB", self.spec["dk2nudata"].prefix)
        env.set("DK2NUGENIE_INC", self.spec["dk2nugenie"].prefix)
        env.set("GENIE_INC", self.spec["genie"].prefix)
        env.set("GENIE_LIB", self.spec["genie"].prefix)
        env.set("IFDH_ART_FQ_DIR", self.spec["ifdh-art"].prefix)
        env.set("IFDH_ART_LIB", self.spec["ifdh-art"].prefix)
        env.set("IFDHC_FQ_DIR", self.spec["ifdhc"].prefix)
        env.set("IFDHC_LIB", self.spec["ifdhc"].prefix)
        env.set("LHAPDF_LIB", self.spec["lhapdf"].prefix)
        env.set("LIBXML2_INC", self.spec["libxml2"].prefix)
        env.set("LOG4CPP_INC", self.spec["log4cpp"].prefix)
        env.set("LOG4CPP_LIB", self.spec["log4cpp"].prefix)
        env.set("PYLIB", self.spec["pythia6"].prefix)
        env.set("XERCES_C_INC", self.spec["xerces-c"].prefix)

    def setup_run_environment(self, run_env):
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("ROOT_INCLUDE_PATH", self.prefix.include)
        run_env.append_path("FW_SEARCH_PATH", "{0}/fw".format(self.prefix))
        run_env.append_path("CET_PLUGIN_PATH", self.prefix.lib)


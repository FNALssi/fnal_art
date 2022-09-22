# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ifbeam(MakefilePackage):
    """Data handling client code for intensity frontier experiments"""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/ifbeam"
    url = "https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/ifdhc-ifbeam.v2_5_2.tbz2"

    version("2.5.2", sha256="7c1bac69dae5d3130741d9dd79295eb917e74eaadde9f808f10599db94a6a488")
    version("2.4.8", sha256="676b43be56c51f68c189d19e8c23a68e9bc489a7e3aaedb632e7600a168d9448")
    version("2.3.0", sha256="4b6a29443b631957ca2a7712b5c577620c6543e542ee9c77d246cef1e10f7324")
    version("2.2.13", sha256="b341ffc73421b7187b06c205f9feaccf117bdba06509e9b1b8f491fdc182029c")

    parallel = False

    build_directory = "src"

    variant(
        "cxxstd",
        default="17",
        values=("default", "98", "11", "14", "17"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    depends_on("ifdhc")
    depends_on("libwda")

    def url_for_version(self, version):
        url = "https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/{0}.v{1}.tbz2"
        return url.format("ifdhc-" + self.name, version.underscored)

    @property
    def build_targets(self):
        cxxstd = self.spec.variants["cxxstd"].value
        cxxstdflag = (
            "" if cxxstd == "default" else getattr(self.compiler, "cxx{0}_flag".format(cxxstd))
        )
        tlist = [
            "LIBWDA_FQ_DIR=" + self.spec["libwda"].prefix,
            "LIBWDA_LIB=" + self.spec["libwda"].prefix.lib,
            "IFDHC_FQ_DIR=" + self.spec["ifdhc"].prefix,
            "IFDHC_LIB=" + self.spec["ifdhc"].prefix.lib,
            "ARCH=" + cxxstdflag,
        ]

        if "ubuntu" in self.spec.architecture:
            tlist.append("LDFLAGS=-lcrypto")

        return tlist

    @property
    def install_targets(self):
        return ("DESTDIR={0}/".format(self.prefix), "install")

    def setup_build_environment(self, spack_env):
        spack_env.set("IFBEAM_DIR", self.prefix)

    def setup_run_unvironment(self, run_env):
        run_env.set("IFBEAM_DIR", self.prefix)

    def setup_dependent_build_environment(self, spack_env, dspec):
        spack_env.set("IFBEAM_DIR", self.prefix)

    def setup_dependent_run_environment(self, run_env, dspec):
        run_env.set("IFBEAM_DIR", self.prefix)

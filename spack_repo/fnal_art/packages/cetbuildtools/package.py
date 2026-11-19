# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install cetbuildtools
#
# You can edit this file again by typing:
#
#     spack edit cetbuildtools
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

import spack.util.spack_json as sjson
import spack.util.web
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Cetbuildtools(CMakePackage):

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://cdcvs.fnal.gov/redmine/projects/cetbuildtools"
    git_base = "https://github.com/art-framework-suite/cetbuildtools"
    url = "https://github.com/art-framework-suite/cetbuildtools/archive/refs/tags/v8_15_00.tar.gz"
    list_url = "https://api.github.com/repos/art-framework-suite/cetbuildtools/tags"

    version("8.20.00", sha256="e61a69d02b39ecbf9b8d15ba6e97a8b8dde299b7b0bbd3496852d7a7a50e6c0d")
    version("8.19.02", sha256="90a902eab52eb69e7be9c5e873917c0aa438c78642a207f6156ade2f976eacaf")
    version("8.19.01", sha256="daa43aab22451ba2fd763376b6e5bfc60139ee0f403492e2f4e2573d0b8282c7")
    version("8.19.00", sha256="eed55e04a7be0c71ea8e2033d9704ba00c3048939c40e8d2a606b6dc8a1fd14b")
    version("8.18.11", sha256="f4722aa3550a4f8b61704b83256bf52a00a2dde54833c2a120e86bd5ed2d8ef9")
    version("8.18.10", sha256="be816559424eb475f08480926b7b3ab739cf8fff57968da5e0087356996c9f6a")
    version("8.18.09", sha256="9f3b53bfca48c9053c7434250c6fe75d07f0ac1a218889f06501876477fba96f")
    version("8.18.08", sha256="fcdb8ee668a2b3392da0f53b5d273ddededffbbf03de48dfcd8efebcf060482f")
    version("8.18.07", sha256="3583bb7eb27a0c21fe9608427509ce98cb5194ea26f3c2850e7fca54df497ef2")
    version("8.18.06", sha256="a6f5f47e639483ff1182db7354958f62451e6177b8e34cab9839cc4925f1c233")
    version("8.18.05", sha256="009a82d56f2149399de45eb81d3ed021b83b3e8c8c3fcc4f3db13b7d49d51759")
    version("8.18.04", sha256="6ef9838ceeb361d41a36edc9c83b6c7ce13899ea543022cb94cac4df00386aad")
    version("8.18.03", sha256="de4db6e4066668f24620d5ca1a8f00036c5afdb65f8a649855ee75e9fe7232a4")
    version("8.18.02", sha256="9e6de0eeadb1def81903cbb026b8141482cbc828f6e29bcb69344f6540c144b2")
    version("8.18.01", sha256="335f31eea442a1e22d17e3ac37a112bf8524f8ce161d1ebe04fff22fa21a4327")
    version("8.18.00", sha256="d31652b2002ce2b198cf274ba76448783ee1f6c4d3b076086bb07edb0c28db7f")
    version("8.17.03", sha256="c2e15d06d80a81f1763318c612580d8b855847ebd5683056edb9d66185b98ea0")
    version("8.17.02", sha256="78722424bccafa6de2d651395daf3b737112c7f83a9ab22ac087cccd36e90982")
    version("8.17.01", sha256="b9e04af24359716c13fbe4d2459134fa78297dbd14bb0b2134499c0755b534b9")
    version("8.17.00", sha256="fe27ba75e08f225fafa22f852ec4c4587a214e4114e1fc8779d6827137c6a5a0")
    version("8.16.00", sha256="f82d4e167b91adf177260db99b0fc9b9b10b5a7f3c21971c2224b7e3a71fc9b6")
    version("8.15.01", sha256="492758d00d7ddab25e2297aa2c5e73f11d3796661fca32ca75b05335d6ebb6bb")
    version("8.15.00", sha256="e1560da61d83e190c6d7a25068696479d99d067a53700caa6c072f5a986caa83")
    version("8.14.02", sha256="edbb01fc737d583009385e51e5542329c38ebeeed57dd355bc18c817038acc52")
    version("8.14.01", sha256="f54feaf621c75249977d82ab3b35219845d962de24fac031d040fd4e7acd0815")
    version("8.14.00", sha256="d08df1a866a9476decd68148b2f43c5497643e2b571836663ff98624d2baa169")
    version("8.13.04", sha256="00037208d17fb1a993b14d7e0587bf184037fa19cc507d8e962293d43ea67eec")
    version("8.13.03", sha256="0f7ded1c1c97e2f597b54879c4ab56a68ff6688f54450afce0182ca143d2e904")
    version("8.13.02", sha256="c9348219757cfad1b8a0ffb143ab156bc2faca4df4ff635f4bb3af867fb4aeca")
    version("8.13.01", sha256="ec45669c371531dcd24e0c6d876ee1454efcaac5a34064049b53bfd25ab7f6e0")
    version("8.06.00", sha256="eeceb410c6ec710c384ea4b3bca4d02adc8b6d8c84886d9d3647204c32d3d8ef")

    def url_for_version(self, version):
        url = "https://github.com/art-framework-suite/{0}/archive/v{1}.tar.gz"
        return url.format(self.name, version.underscored)

    def fetch_remote_versions(self, concurrency=None):
        return dict(
            map(
                lambda v: (v.dotted, self.url_for_version(v)),
                [
                    Version(d["name"][1:])
                    for d in sjson.load(
                        spack.util.web.read_from_url(
                            self.list_url, accept_content_type="application/json"
                        )[2]
                    )
                    if d["name"].startswith("v")
                ],
            )
        )

    depends_on("cetmodules@3.12.02:3")
    depends_on("cmake@3.21:", type="build")

    maintainers = ["marc_mengel"]

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args

    def setup_dependent_build_environment(self, env, dep):
        # lots of CMakefiles check this...
        env.set("CETBUILDTOOLS_VERSION", "v%s" % self.version.underscored)
        # they look in $CETBUILDTOOLS_DIR/Modules for things that are now
        # in cetmodules...
        env.set("CETBUILDTOOLS_DIR", self.spec["cetmodules"].prefix)
        env.prepend_path("CMAKE_PREFIX_PATH", self.prefix)

    @run_after("install")
    def rename_README(self):
        import os

        if os.path.exists(join_path(self.spec.prefix, "README")):
            os.rename(
                join_path(self.spec.prefix, "README"),
                join_path(self.spec.prefix, "README_%s" % self.spec.name),
            )

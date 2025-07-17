# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import os

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class GeniePhyopt(Package):
    """Phyopt files used by genie."""

    homepage = "https://www.example.com"
    url = "https://scisoft.fnal.gov/scisoft/packages/genie_phyopt/v3_04_00/genie_phyopt-3.04.00-noarch-dkcharm.tar.bz2"
    version(
        "3.04.00", sha256="c4a5360e379d371df2b2e845aee673b984a2f0f6ba62dae682f8cb0223e84a0f", expand=False
    )

    variant(
        "phyopt_name",
        default="dkcharm",
        multi=False,
        values=("dkcharm", "dkcharmtau"),
        description="Name of genie phyopt to use.",
    )

    baseurl = "https://scisoft.fnal.gov/scisoft/packages/genie_phyopt/v3_04_00/genie_phyopt-3.04.00-noarch-"
    resource(
        name="dkcharm",
        when="phyopt_name=dkcharm",
        url=baseurl + "dkcharm.tar.bz2",
        sha256="c4a5360e379d371df2b2e845aee673b984a2f0f6ba62dae682f8cb0223e84a0f",
    )

    resource(
        name="dkcharmtau",
        when="phyopt_name=dkcharmtau",
        url=baseurl + "dkcharmtau.tar.bz2",
        sha256="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    )

    def install(self, spec, prefix):
        val = spec.variants["phyopt_name"].value
        install_tree(
            "{0}/genie_phyopt/v{1}/NULL/{2}".format(
                self.stage.source_path, self.version.underscored, val
            ),
            "{0}/{1}".format(prefix, val),
        )

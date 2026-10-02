# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import os, sys

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *

default_variant = 'dkcharm'

# Checksums by version and variant.
# Checksum = versions[version][variant]
# Variant is either tune_name or xsec_name.

_checksums = {
    # Variant tune_name
    '3.04.00': {
        'dkcharm': 'c4a5360e379d371df2b2e845aee673b984a2f0f6ba62dae682f8cb0223e84a0f',
        'dkcharmtau': '61ff222f2e3da12fbba80b2f6bf430e9fd89336829c4159da6636542f37c231e'
    },
    '3.06.00': {
        'dkcharm': '880d315274957ea087bf06ba96aacedaab507c7e4fcbca2f064a7651581d6d4e',
        'dkcharmtau': 'fdeedc9e8cd371b5b142b7f21180ce6de22a9900c3b7205fbfa9a532b83f6ba2'
    }
}

class GeniePhyopt(Package):
    """Phyopt files used by genie."""

    # Construct lists of variants

    phyopt_names = set()
    for v in _checksums.keys():
        for var in _checksums[v]:
            if not var in phyopt_names:
                phyopt_names.add(var)


    variant(
        "phyopt_name",
        default="dkcharm",
        multi=False,
        values=tuple(phyopt_names),
        description="Name of genie phyopt to use.",
    )

    # Declare versions and their resources with checksums.

    for v,vars in _checksums.items():
        v_underscored=v.replace('.', '_')
        for var,checksum in vars.items():
            if var == default_variant:
                version(
                    v,
                    url = f'https://scisoft.fnal.gov/scisoft/packages/genie_phyopt/v{v_underscored}/genie_phyopt-{v}-noarch-{var}.tar.bz2',
                    expand=False,
                    sha256=checksum,
                )
            resource(
                name=var,
                expand=True,
                when=f"@{v} phyopt_name={var}",
                url = f'https://scisoft.fnal.gov/scisoft/packages/genie_phyopt/v{v_underscored}/genie_phyopt-{v}-noarch-{var}.tar.bz2',
                sha256=checksum,
                )



    def url_for_version(self, version):
        return f'https://scisoft.fnal.gov/scisoft/packages/genie_phyopt/v{version.underscored}/genie_phyopt-{version}-noarch-{default_variant}.tar.bz2'

    def install(self, spec, prefix):
        val = spec.variants["phyopt_name"].value
        resource_path = os.path.join(self.stage.source_path, "genie_phyopt", f"v{self.version.underscored}", "NULL", val)
        install_tree(
            resource_path,
            "{0}/{1}".format(prefix, val),
        )

    def setup_run_environment(self, run_env):
        val = self.spec['genie-phyopt'].variants['phyopt_name'].value
        data_str = "{0}/{1}".format(self.spec['genie-phyopt'].prefix, val)

        run_env.set("GENIEPHYOPTPATH", data_str)
        run_env.prepend_path("GXMLPATH", data_str)
        run_env.set("GENIE_PHYOPT_VARIANT", val)

        run_env.prune_duplicate_paths("GXMLPATH")


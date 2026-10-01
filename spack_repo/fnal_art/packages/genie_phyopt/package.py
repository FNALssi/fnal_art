# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import os, sys

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *

default_variant = 'dkcharmtau'

# Checksums by version and variant.
# Checksum = versions[version][variant]
# Variant is either tune_name or xsec_name.

versions = {
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
    for v in versions:
        for var in versions[v]:
            if not var in phyopt_names:
                phyopt_names.add(var)

    variant(
        "phyopt_name",
        default="dkcharm",
        multi=False,
        values=tuple(phyopt_names),
        description="Name of genie phyopt to use.",
    )

    # Declare version checksums.

    url = "https://scisoft.fnal.gov/scisoft/packages/genie_phyopt/v3_04_00/genie_phyopt-3.04.00-noarch-dkcharm.tar.bz2"

    for v in versions:
        if len(versions[v]) == 1:
            default_variant = list(versions[v].values())[0]
        if default_variant in versions[v]:
            checksum = versions[v][default_variant]
            version(v, sha256=checksum)

    def url_for_version(self, v):
        print("genie-phyopt url_for_version called", file=sys.stderr)
        print(f"version {v}", file=sys.stderr)
        print(self.spec, file=sys.stderr)
        print(self.spec.variants, file=sys.stderr)
        var = ''
        if 'phyopt_name' in self.spec.variants:
            var = self.spec.variants['phyopt_name'].value
        else:
            var = default_variant
        if type(var) == type(()) and len(var) == 1:
            var = var[0]
        if var != default_variant:
            print(f"Selected variant {var} doesn't match default variant {default_variant}.", file=sys.stderr)
        print(var, file=sys.stderr)
        url = 'https://scisoft.fnal.gov/scisoft/packages/genie_phyopt/v{0}/genie_phyopt-{1}-noarch-{2}.tar.bz2'.format(v.underscored, v, var)
        print(url, file=sys.stderr)
        return url

    def install(self, spec, prefix):
        print("genie-phyopt install function called.", file=sys.stderr)
        val = spec.variants["phyopt_name"].value
        install_tree(
            "{0}/v{1}/NULL/{2}".format(
                self.stage.source_path, self.version.underscored, val
            ),
            "{0}/{1}".format(prefix, val),
        )

    def setup_run_environment(self, run_env):
        print("genie-phyopt setup_run_environment called", file=sys.stderr)
        val = self.spec['genie-phyopt'].variants['phyopt_name'].value
        print('phyopt_name = %s' % val, file=sys.stderr)
        data_str = "{0}/{1}".format(self.spec['genie-phyopt'].prefix, val)
        print(f"data_str = {data_str}", file=sys.stderr)

        run_env.set("GENIEPHYOPTPATH", data_str)
        run_env.prepend_path("GXMLPATH", data_str)
        run_env.set("GENIE_PHYOPT_VARIANT", val)

        run_env.prune_duplicate_paths("GXMLPATH")


# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os, sys

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *

#default_variant = 'AR2320i00000-k250-e1000'
#default_variant = 'G1801a00000-k250-e1000'
default_variant = 'G1802a00000-k250-e1000'
    
# Checksums by version and variant.
# Checksum = versions[version][variant]
# Variant is either tune_name or xsec_name.

versions = {
    # Variant tune_name
    '3.04.00': {
        'AR2320i00000-k250-e1000': '13cc9d740c170af9033623049162eeff0fb0b68156122d380aa3262e92e9f61f',
        'G1801a00000-k250-e1000': 'f222ff56360c9c221e8f793a9c09ddbe6578dbbaa9031b3b3a49cb5ec186595d',
        'G1802a00000-k250-e1000': 'd7189bd6c3933b3017c83fafddb84d57b48414632b577835e49babec8537ab6e',
        'G1810a0211a-k250-e1000': 'fb4dc9badd1771c92fabbf818b33544006e8b60c7fb0f33d5288a66d93bd19ea',
        'G1810a0211b-k250-e1000': 'a1031e49ac8ac426074f247d91b2c886edaf7c4fef13993fe69aad92ad698c34',
        'G2111a00000-k250-e1000': 'ae159887772a54891fc4bddb189ab108d74c4a48db68c13ed7166524e8797590',
        'GDNu2001a00000-k120-e200': '69146aacc6c55bdc5c519e917e48ea005d160824bf960d17734e9c7c6d85b6cb',
        'N1810j0211a-k250-e1000': '79e7ecd8d0dc577efb525831b90eb2f650c0cdd7fe5cd17e3ea610a686248e33'
    },
    '3.06.00': {
        'AR2320i00000-k250-e1000': 'f435a98f5d491a181333f27a9a0b675cb94c326770447b0e98d5190983962dd0',
        'G1802a00000-k250-e1000': '8d3823a30daec4f9e7fce42e43129ace0a6f35b95c793016b257df5a59e422f1',
        'G1802c00000-k250-e1000': 'ba8da487a79fb936f90bb6aaa1452dd18a6a39daf388c892b9aede0fb59277a2',
        'G1810a0211a-k250-e1000': '3015e8f2c2b78292cc8b3bc72e238ab941fbcd81c708732e1f70eb5bd63a2617',
        'G1810a0211b-k250-e1000': '17a0b04392231d65cf3da8d18edfe615693f7907dc82682175d6175bcdbb50fa',
        'N2420i0211b-k250-e1000': 'ea17249e6bb3159b27bb865e2a6a0133c3ba20acc8b0232ef8e82d88c40440af'
    },
    # Variant xsec_name
    '2.12.10': {
        'AltPion': '49c4c5332c96edc4147e8cacd5b68e8dd89737e205741a21bc75a5ba18b967c4',
        'DefaultPlusMECWithNC': '7c57caa96c319ad8007253e2a81c6ffcc4dcc6d0923dabbf7b8938d8363ac621',
        'DefaultPlusValenciaMEC': 'fe1b584e7014bba6c4cba5646e1031f344e9efbf799a2aa26b706e28c40a4481',
        'EffSFTEM': 'b6365f1a150b90b79788f51b084a1dce7432d8ba10b7faa03ade3f6d558c82f6',
        'LocalFGNievesQEAndMEC': '5f02d7efa46ef42052834d80b6923b41e502994daaf6037dad9793799ad4b346',
        'ValenciaQEBergerSehgalCOHRES': '3e7c117777cb0da6232df1e1fe481fdb2afbfe55639b0d7b4ddf8027954ed1fa'
    }
}

class GenieXsec(Package):
    """Data files used by genie."""

    # Construct lists of variants

    tune_names = set()
    xsec_names = set()
    for v in versions:
        for var in versions[v]:
            if v >= '3':
                if not var in tune_names:
                    tune_names.add(var)
            else:
                if not var in xsec_names:
                    xsec_names.add(var)

    # tune_name values are designed to line up with the ups setup command
    # when setting the environment variable, we change to match typical
    # genie tune format
    variant(
        "tune_name",
        default="AR2320i00000-k250-e1000",
        multi=False,
        values=tuple(tune_names),
        when="@3.0:",
        description="Name of genie xsec tune set to install.",
    )

    variant(
        "xsec_name",
        default="DefaultPlusMECWithNC",
        multi=False,
        values=tuple(xsec_names),
        when="@:3.0",
        description="Name of genie xsec set to install.",
    )

    # Declare version checksums.

    url = 'https://scisoft.fnal.gov/scisoft/packages/genie_xsec/v3_04_00/genie_xsec-3.04.00-noarch-AR2320i00000-k250-e1000.tar.bz2'
    for v in versions:
        if len(versions[v]) == 1:
            default_variant = list(versions[v].values())[0]
        if default_variant in versions[v]:
            checksum = versions[v][default_variant]
            version(v, sha256=checksum)


    def url_for_version(self, v):
        print("genie-xsec url_for_version called", file=sys.stderr)
        print(f"version {v}", file=sys.stderr)
        print(self.spec, file=sys.stderr)
        print(self.spec.variants, file=sys.stderr)
        var = ''
        if(self.version >= Version("3.0")):
            var = self.spec.variants['tune_name'].value
        else:
            var = self.spec.variants['xsec_name'].value
        if type(var) == type(()) and len(var) == 1:
            var = var[0]
        if var != default_variant:
            print(f"Selected variant {var} doesn't match default variant {default_variant}.", file=sys.stderr)
            sys.exit(1)
        print(var, file=sys.stderr)
        url = 'https://scisoft.fnal.gov/scisoft/packages/genie_xsec/v{0}/genie_xsec-{1}-noarch-{2}.tar.bz2'.format(v.underscored, v, var)
        print(url, file=sys.stderr)
        return url

    def install(self, spec, prefix):
        print("genie-xsec install function called", file=sys.stderr)
        if(self.version >= Version("3.0")):
            val = spec.variants["tune_name"].value
            install_tree(
                "{0}/v{1}/NULL/{2}".format(self.stage.source_path, self.version.underscored,val),
                "{0}/v{1}/NULL/{2}".format(prefix, self.version.underscored, val),
            )
        elif(self.version < Version("3.0")):
            val = spec.variants["xsec_name"].value
            install_tree(
                "{0}/v{1}/NULL/{2}".format(self.stage.source_path, self.version.underscored, val),
                "{0}/{1}".format(prefix, val),
            )

    def setup_run_environment(self, run_env):
        if(self.version >= Version("3.0")):
            val = self.spec['genie-xsec'].variants['tune_name'].value
            data_str = "{0}/v{1}/NULL/{2}/data".format(self.spec['genie-xsec'].prefix, self.version.underscored, val)
            raw_str = self.spec['genie-xsec'].variants['tune_name'].value
            comb_str = raw_str.split(':')[0].split('-')[0]
            tune_str = comb_str[:-8]+"_"+comb_str[-8:-5]+"_"+comb_str[-5:-3]+"_"+comb_str[-3:] 

            run_env.set("GENIEXSECPATH", data_str)
            run_env.set("GENIEXSECFILE", data_str+"/gxspl-NUsmall.xml")
            run.env.prepend_path("GXMLPATH", data_str)
            run_env.set("GENIE_XSEC_TUNE", tune_str)
            run_env.set("GENIE_XSEC_GENLIST", "Default")
            run_env.set("GENIE_XSEC_KNOTS", "250")
            run_env.set("GENIE_XSEC_EMAX", "1000.0")

            env.prune_duplicate_paths("GXMLPATH")

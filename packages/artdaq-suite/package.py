# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *

class ArtdaqSuite(BundlePackage):
    """The artdaq suite; artdaq is a data acquisition framework that leverages the analysis capabilities of art
    """

    version("v3_12_03")
    version("v3_12_02")
    
    variant(
        "s",
        default="0",
        values=("0", "112", "117", "118", "122", "123"),
        multi=False,
        description="Art suite version to use",
    )
    depends_on("art-suite@s123+root", when="s=123")
    depends_on("art-suite@s122+root", when="s=122")
    depends_on("art-suite@s118+root", when="s=118")
    depends_on("art-suite@s117+root", when="s=117")
    depends_on("art-suite@s112+root", when="s=112")
    depends_on("art-suite+root", when="s=0")

    variant("demo", default=False, description="Also install artdaq_demo components")
    variant("db", default=True, description="Install artdaq_database")
    variant("epics", default=True, description="Install artdaq EPICS plugin")
    variant("pcp", default=True, description="Install artdaq PCP MMV plugin")

    with when("@v3_12_03"):
        depends_on("artdaq@v3_12_03")
        depends_on("artdaq-core@v3_09_08")
        depends_on("artdaq-utilities@v1_08_03")
        depends_on("artdaq-mfextensions@v1_08_03")
        depends_on("trace@v3_17_09")
        depends_on("artdaq-daqinterface@v3_12_03")
        depends_on("artdaq-core-demo@v1_10_03", when="+demo")
        depends_on("artdaq-demo@v3_12_03", when="+demo")
        depends_on("artdaq-demo-hdf5@v1_04_03", when="+demo")
        depends_on("artdaq-database@v1_07_03", when="+db")
        depends_on("artdaq-epics-plugin@v1_05_03", when="+epics")
        depends_on("artdaq-pcp-mmv-plugin@v1_03_03", when="+pcp")
    with when("@v3_12_02"):
        depends_on("artdaq@v3_12_02")
        depends_on("artdaq-core@v3_09_04")
        depends_on("artdaq-utilities@v1_08_02")
        depends_on("artdaq-mfextensions@v1_08_02")
        depends_on("trace@v3_17_07")
        depends_on("artdaq-daqinterface@v3_12_02")
        depends_on("artdaq-core-demo@v1_10_02", when="+demo")
        depends_on("artdaq-demo@v3_12_02", when="+demo")
        depends_on("artdaq-demo-hdf5@v1_04_02", when="+demo")
        depends_on("artdaq-database@v1_07_02", when="+db")
        depends_on("artdaq-epics-plugin@v1_05_02", when="+epics")
        depends_on("artdaq-pcp-mmv-plugin@v1_03_02", when="+pcp")

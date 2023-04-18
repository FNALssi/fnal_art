# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *

class OtsdaqSuite(BundlePackage):
    """The Off-The-Shelf DAQ suite, otsdaq, providing graphical wrappers for artdaq
    """
    
    version("v2_06_09")
    version("v2_06_08")
    
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

    variant(
        "artdaq",
        default="0",
        values("0","31202","31203"),
        multi=False,
        description="Artdaq suite version to use",
    )   
    depends_on("artdaq-suite@v3_12_03", when="artdaq=31203")
    depends_on("artdaq-suite@v3_12_02", when="artdaq=31202")
    depends_on("artdaq-suite+db+epics~demo~pcp")

    variant("demo", default=False, description="Install otsdaq-demo")
    variant("prep", default=False, description="Install PREP modernization library")
    
    with when("@v2_06_09"):
        depends_on("otsdaq@v2_06_09")
        depends_on("otsdaq-utilities@v2_06_09")
        depends_on("otsdaq-components@v2_06_09")
        depends_on("otsdaq-epics@v2_06_09")
        depends_on("otsdaq-demo@v2_06_09", when="+demo")
        depends_on("otsdaq-prepmodernization@v2_06_09", when="+prep")
    with when("@v2_06_08"):
        depends_on("otsdaq@v2_06_08")
        depends_on("otsdaq-utilities@v2_06_08")
        depends_on("otsdaq-components@v2_06_08")
        depends_on("otsdaq-epics@v2_06_08")
        depends_on("otsdaq-demo@v2_06_08", when="+demo")
        depends_on("otsdaq-prepmodernization@v2_06_08", when="+prep")

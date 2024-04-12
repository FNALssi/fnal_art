# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class SamWebClient(Package):
    """Executable and Python client interfaces for SAM Web"""

    homepage = "http://cdcvs.fnal.gov/projects/sam-web-client"
    git = "http://cdcvs.fnal.gov/projects/sam-web-client"

    maintainers("vhewes")

    license("UNKNOWN")

    version("3.4", tag="v3_4")

    depends_on("python")
    extends("python")

    def install(self, spec, prefix):
        samweb_client_path = join_path(python_platlib, "samweb_client")
        mkdirp(prefix.bin, samweb_client_path)
   
        install("bin/*", prefix.bin)
        install("python/*.py", python_platlib)
        install("python/samweb_client/*.py", samweb_client_path)

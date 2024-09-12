# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class StanMath(Package):
    """C++ template library for automatic differentiation"""

    homepage = "https://mc-stan.org/math"
    url = "https://github.com/stan-dev/math/archive/v4.0.0.tar.gz"

    maintainers("vhewes")

    version("4.9.0", sha256="876881b71dee6fec32f2b4aa52692994cccd2a19c6de1b986d7fc457155f219c")
    version("4.8.1", sha256="78e115c89c298fb9e6fa5941b7e39c84cfea0a8f491a0dc556ab5746d5699136")
    version("4.8.0", sha256="b707737c8ce6833cf2b0d279f380c0d7fd47c76288578982dafeabf583b738c1")
    version("4.7.0", sha256="c314325d20c3f4a3b6eda31b41f84f71c3fff9521906b5c3ff671e5702ded92f")
    version("4.6.2", sha256="30df8657e02ddc77b6c96ac32f8d6f099a61064a113373cd3a11ffd736372ba1")
    version("4.6.1", sha256="2df2be173e922b2794e0457f537fe0b0276a66515051cbb8c61e488cfe12f795")
    version("4.0.0", sha256="99ccd238eb2421be55d290a858ab5aa31022eded5c66201fcee35b2638f0bb42")
    version("3.4.0", sha256="3e768d1c2692543d3560f9d954d19e58fd14c9aaca22f5140c9f7f1437ddccf9")
    version("3.3.0", sha256="fb96629fd3e5e06f0ad4c03a774e54b045cc1dcfde5ff65b6f78f0f05772770a")

    depends_on("boost")
    depends_on("eigen")
    depends_on("intel-tbb@2020.3")
    depends_on("sundials@6.1")

    def install(self, spec, prefix):
        # NOTE: there are some tests that require building, but these are mostly
        #       targeted at Stan developers.
        #       We're just going to unwind the tarball and install the headers,
        #       which are all users need
        mkdir(prefix.stan)
        install_tree("stan", prefix.stan)

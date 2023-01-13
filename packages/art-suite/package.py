# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *

class ArtSuite(BundlePackage):
    """The art suite; art is an event-processing framework for particle physics experiments.
    """

    version("s118")
    version("s117")
    version("s112")

    variant("root", default=True, description="Also bring in the ROOT IO packages")
    
    with when("@s118"):
        depends_on("art@3.12.00")
        depends_on("art-root-io@1.11.00", when="+root")
        depends_on("boost@1.80.0")
        depends_on("canvas@3.14.00")
        depends_on("canvas-root-io@1.11.00", when="+root")
        depends_on("catch2@2.13.8")
        depends_on("cetlib@3.16.00")
        depends_on("cetlib-except@1.08.00")
        depends_on("cetmodules@3.19.02")
        depends_on("clhep@2.4.5.3")
        depends_on("fftw@3.3.10")
        depends_on("fhicl-cpp@4.17.00")
        depends_on("gsl@2.7")
        depends_on("hep-concurrency@1.08.00")
        depends_on("libxml2@2.9.12")
        depends_on("messagefacility@2.09.00")
        depends_on("py-numpy@1.22.3")
        depends_on("openblas@0.3.21")
        depends_on("postgresql@14.0")
        depends_on("py-pybind11@2.10.0")
        depends_on("pythia6@6.4.28")
        depends_on("python@3.9.13")
        depends_on("range-v3@master") # 0.12.0 not published to Spack
        depends_on("root@6.26.06", when="+root")
        depends_on("sqlite@3.39.2")
        depends_on("tbb@2021.7.0")
        depends_on("xrootd@5.5.1") # 5.4.3 not published to Spack
    with when("@s117"):
        depends_on("art@3.09.04")
        depends_on("art-root-io@1.08.05", when="+root")
        depends_on("boost@1.75.0")
        depends_on("canvas@3.12.05")
        depends_on("canvas-root-io@1.09.05", when="+root")
        depends_on("catch2@2.13.4")
        depends_on("cetlib@3.13.04")
        depends_on("cetlib-except@1.07.04")
        depends_on("clhep@2.4.5.1")
        depends_on("fftw@3.3.9")
        depends_on("fhicl-cpp@4.15.03")
        depends_on("gsl@2.6")
        depends_on("hep-concurrency@1.07.04")
        depends_on("jemalloc@5.2.1")
        depends_on("libxml2@2.9.10")
        depends_on("messagefacility@2.08.04")
        depends_on("mysql-client@8.0.23")
        depends_on("ninja@1.10.2")
        depends_on("py-numpy@1.20.1")
        depends_on("openblas@0.3.13")
        depends_on("postgresql@14.0") # 13.2 not published to Spack
        depends_on("py-pybind11@2.6.2")
        depends_on("pythia6@6.4.28")
        depends_on("python@3.9.2")
        depends_on("range-v3@0.11.0")
        depends_on("root@6.22.08", when="+root")
        depends_on("sqlite@3.34.0")
        depends_on("tbb@2021.1.1")
        depends_on("xrootd@5.1.0")
    with when("@s112"):
        depends_on("art@3.09.03")
        depends_on("art-root-io@1.08.03", when="+root")
        depends_on("boost@1.75.0")
        depends_on("canvas@3.12.04")
        depends_on("canvas-root-io@1.09.04", when="+root")
        depends_on("catch2@2.13.4")
        depends_on("cetlib@3.13.04")
        depends_on("cetlib-except@1.07.04")
        depends_on("cetpkgsupport@1.14.01")
        depends_on("clhep@2.4.5.1") # 2.4.4.1 not published to spack
        depends_on("fftw@3.3.9")
        depends_on("fhicl-cpp@4.15.03")
        depends_on("gsl@2.6")
        depends_on("hep-concurrency@1.07.04")
        depends_on("jemalloc@5.2.1")
        depends_on("libxml2@2.9.10")
        depends_on("messagefacility@2.08.04")
        depends_on("mysql-client@8.0.23")
        depends_on("ninja@1.10.2")
        depends_on("py-numpy@1.20.1")
        depends_on("openblas@0.3.13")
        depends_on("postgresql@14.0") # 13.2 not published to Spack
        depends_on("py-pybind11@2.6.2")
        depends_on("pythia6@6.4.28")
        depends_on("python@3.9.2")
        depends_on("range-v3@0.11.0")
        depends_on("root@6.22.08", when="+root")
        depends_on("sqlite@3.34.0")
        depends_on("tbb@2021.1.1")
        depends_on("xrootd@5.1.0")
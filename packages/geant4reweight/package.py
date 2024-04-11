# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Geant4reweight(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/NuSoftHEP/Geant4Reweight"
    git = "https://github.com/NuSoftHEP/Geant4Reweight"
    # git = "/exp/nova/app/users/vhewes/al9/Geant4Reweight"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.


    # See https://spdx.org/licenses/ for a list.
    license("UNKNOWN")

    version("1.16.05", branch="nova_v01_16_br")
    version("01_20_00", sha256="f8d30f2a1426ee9e100694d4d19d58a7b98af93c8e71ff0a52cb0a1e7a6d3d96")

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    # FIXME: Add dependencies if required.
    # depends_on("cetlib")
    # depends_on("fhicl-cpp")
    # depends_on("geant4")
    # depends_on("root")
    depends_on("nug4")
    depends_on("cetmodules")
    depends_on("cmake")

    patch("patch.p")

    def cmake_args(self):
        # Set CMake args.
        args = [
            "-DCMAKE_CXX_STANDARD={0}".format(self.spec.variants["cxxstd"].value),
        ]
        return args

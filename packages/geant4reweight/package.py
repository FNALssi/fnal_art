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
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("1.16.05", branch="nova_v01_16_br")

    depends_on("cetlib")
    depends_on("fhicl-cpp")
    depends_on("geant4")
    depends_on("root")

    depends_on("cetmodules", type="build")

    patch("patch.p")

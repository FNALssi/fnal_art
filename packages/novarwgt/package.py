# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Novarwgt(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.github.com/novaexperiment/novarwgt"
    git = "git@github.com:novaexperiment/novarwgt"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("develop", branch="feature/spack")

    variant(
        "cxxstd",
        default="17",
        values=("17", "20", "23"),
        multi=False,
        sticky=True,
        description="C++ standard",
    )

    depends_on("root")

    depends_on("cetmodules", type="build")

    # optional cetlib dependency
    variant("cetlib", default=False, description="Enable CETLib dependency")
    depends_on("cetlib", when="+cetlib")

    # optional genie dependency
    variant("genie", default=True, description="Enable GENIE dependency")
    depends_on("nufinder", when="+genie")
    depends_on("genie", when="+genie")

    # optional nusimdata dependency
    variant("nusimdata", default=True, description="Enable NuSimData dependency")
    depends_on("nusimdata", when="+nusimdata")

    def cmake_args(self):
        args = [
            self.define_from_variant("NOVARWGT_USE_CETLIB", "cetlib"),
            self.define_from_variant("NOVARWGT_USE_GENIE", "genie"),
            self.define_from_variant("NOVARWGT_USE_NUSIMDATA", "nusimdata"),
        ]
        return args

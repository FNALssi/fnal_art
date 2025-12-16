# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Systematicstools(CMakePackage):
    """Framework for writing, using and interpreting experimental systematic uncertainties."""

    homepage = "https://github.com/LArSoft/systematicstools"
    url = "https://github.com/LArSoft/systematicstools/archive/v01_04_02.tar.gz"

    def url_for_version(self, version):
        return f"https://github.com/LArSoft/systematicstools/archive/v{version.underscored}.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")
    version("01.04.04", sha256="7436341f63ea205d8b901b75859a26ec81f29fd272bf324c7bdcde713a3b937c")
    version("01.04.02", sha256="0e14b9736b31b7911307e8703d0f386f2a1fb5c1dcaa69a8d7ce9916afb974cd")

    variant(
        "cxxstd",
        default="17",
        values=("17", "20", "23"),
        multi=False,
        sticky=True,
        description="C++ standard",
    )

    # include cstdint
    patch("01_04_02.patch", when="@=01.04.02",
          sha256="170e1254063f4ced77dd760555696a7aa721fd2b6b4a0e324ac58f379abd7691")
    patch("01_04_04.patch", when="@=01.04.04",
          sha256="42cb526cf7da40f54277454addfc71ad4adfa9a00b44737f7c6371eceed27bba")


    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")

    depends_on("art-root-io")

    def cmake_args(self):
        return [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
        ]

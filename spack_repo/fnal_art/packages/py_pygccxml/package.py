# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyPygccxml(PythonPackage):
    """pygccxml"""

    homepage = "https://pygccxml.readthedocs.io/en/develop/"
    url = "https://github.com/CastXML/pygccxml/archive/v2.0.1.tar.gz"

    version("3.0.2", sha256="ed245663f0d4056d68b42983cdcfe8822b8167aa5f9f265928432c70cf46cf1d")
    version("3.0.1", sha256="5c93b0f2de159f4f9ad3b133442d0cd27fab7c6b75f5e2514e26d5896b3f567a")
    version("3.0.0", sha256="fead5bec1a26a1a709e971124be19721240f3f3774f989c3971babe38207b350")
    version("2.6.1", sha256="4c0f12a076ee27ff48bdbb73eecaecd8376ac64282fb84685994000f1a0c8c8d")
    version("2.6.0", sha256="64a8cf784160aaf8db662149589644bce8a07fb16593e65969ab662c1e126e6c")
    version("2.5.0", sha256="ac6b15f17c4640b0d5dce3a0b903e7c7d0a66c6a5ebf3cff1cd263998bd55c9d")
    version("2.4.0", sha256="d59867809f8008ec48a5567a7203bb4c130ff203a8ddd708c945690749723c70")
    version("2.3.0", sha256="bc20be367074af644e8ab4faca04dc905c6b93de0717bcbe92ef8e2a3934b91b")
    version("2.2.1", sha256="9815a12e3bf6b83b2e9d8c88335fb3fa0e2b4067d7fbaaed09c3bf26c6206cc7")
    version("2.2.0", sha256="88d79080e7c0d6a8b1b239d0a9871b49fa2ca46a26a7e37877059b29a43b5e08")
    version("2.0.1", sha256="25c6f693da741139c538d751b4bee1408764a4470c4f5ee982ac2611032cebc2")
    version("2.0.0", sha256="b941698700bc52c4aa9014d8d7d687c35b82273e1b5857c81bf1ea2b384ec90e")
    version("1.9.1", sha256="2fb4e18f7a3ae039a05230ca58f11e1fc925c8643f926a1be481bb4338414a95")

    depends_on("python", type=("build", "run"))
    depends_on("castxml", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    def build_args(self, spec, prefix):
        args = []
        return args

# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *

class GoogleCloudCpp(CMakePackage):
    """ This repository contains idiomatic C++ client libraries for the following Google Cloud Platform services.

        Google Cloud Bigtable [quickstart]
        Google Cloud Spanner [quickstart]
        Google Cloud Pub/Sub [quickstart]
        Google Cloud Storage [quickstart]
    """

    homepage = "https://github.com/googleapis/google-cloud-cpp/"
    url      = "https://github.com/googleapis/google-cloud-cpp/archive/v1.24.0.tar.gz"

    maintainers = ['marcmengel',]

    version('1.24.0', sha256='705992bbf5d86a5d5b4276fe249ca495bc0827f1835cb433f3f6be777072aa62')
    version('1.23.0', sha256='914c9596ee9f271a4ba2de701388009d1f6a7eb0ea269d625aae06be1a51ee9e')
    version('1.22.0', sha256='2f52dcc679a31e738c01fb68aa0fc966fe0be5322d1a4ec7e6337363281a4704')
    version('1.21.0', sha256='14bf9bf97431b890e0ae5dca8f8904841d4883b8596a7108a42f5700ae58d711')

    depends_on('crc32c')
    depends_on('curl')
    depends_on('google-benchmark')
    depends_on('googletest +gmock')
    depends_on('grpc')
    depends_on('nlohmann-json')
    # depends_on('benchmark')
    # depends_on('abseil')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args

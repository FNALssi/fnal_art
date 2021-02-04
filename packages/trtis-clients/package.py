# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os

class TrtisClients(CMakePackage):
    """C++ client code for Triton Inference Server."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/triton-inference-server/server"
    url      = "https://github.com/triton-inference-server/server/archive/v2.6.0.tar.gz"

    # maintainers = ['github_user1', 'github_user2']

    version('2.6.0',                    sha256='c4fad25c212a0b5522c7d65c78b2f25ab0916ccf584ec0295643fec863cb403e')

    depends_on('cmake@3.18:', type='build')
    depends_on('py-grpcio', type='build')
    depends_on('rapidjson')
    depends_on('opencv ~videoio~gtk~java~vtk~jpeg')
    depends_on('protobuf')
    depends_on('grpc')
    depends_on('googletest')
    depends_on('c-ares')
    depends_on('libevent')
    depends_on('libevhtp')
    
    patch('fix_compile_flags.patch')
    patch('use_existing.patch')

    root_cmakelists_dir = 'build'
  
    def cmake_args(self):
        args = [
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_C_COMPILER=cc',
            '-DCMAKE_CXX_COMPILER=c++',
            '-DTRITON_CURL_WITHOUT_CONFIG:BOOL=ON',
            '-DTRITON_ENABLE_GPU:BOOL=OFF',
            '-DTRITON_ENABLE_METRICS_GPU:BOOL=OFF',
        ]
        return args

    def setup_build_environment(self, env):
        env.prepend_path('CMAKE_MODULE_PATH', self.stage.source_path +'/cmake/modules')
        pass

    def flag_handler(self, name, flags):
        if name == 'cxxflags' and  self.spec.compiler.name == 'gcc':
            flags.append('-Wno-error=deprecated-declarations')
            flags.append('-Wno-error=class-memaccess')
        return (flags, None, None)

    def install(self, spec, prefix):
        install_tree(self.stage.source_path+'/install/include', prefix+'/include/trts_clients')
        install_tree(self.stage.source_path+'/install/lib', prefix+'/lib')

# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Artg4(CMakePackage):
    """Generic geant4 infrastructure for Art"""

    homepage = "https://cdcvs.fnal.gov/projects/artg4/wiki"
    url = "https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/artg4.v9_70_00.tbz2"

    maintainers = ["marcmengel"]

    variant("cxxstd", default="17")

    version("9.70.00", sha256="f77c5afac341562451127ebe7657844049a1fb8c860850638fff32641ffce2e6")

    def patch(self):
        """ 
            changes needed for current package versions, etc.
            which should be made in the package and removed from here...
        """

        filter_file(
            "^CMAKE_MINIMUM_REQUIRED.*",
            "CMAKE_MINIMUM_REQUIRED( VERSION 3.14 )\nfind_package(cetmodules)",
            "CMakeLists.txt",
        )
        filter_file(
            "^PROJECT.*",
            "PROJECT({0} VERSION {1} LANGUAGES CXX C)".format(self.name, self.version),
            "CMakeLists.txt",
        )
        # build assumes source is in a directory named "artg4"...
        filter_file(
            r'add_subdirectory\( ups \)', 
            'if(WANT_UPS)\n add_subdirectory( ups )\nendif()\n',
            "CMakeLists.txt"
        )
        symlink(".", "artg4")
        filter_file(
            r'SetImportFileType\(p.get<bool>\("file_type"\)\)',
            'SetImportFileType(p.get<string>("file_type"))',
            'pluginActions/particleGun/SingleParticleSource.cc',
        )
        filter_file(
            r'cetlib/exception.h', 
            'cetlib_except/exception.h',
            'util/StringIDs.cc'
        )
        filter_file(
            r'cetlib/exception.h', 
            'cetlib_except/exception.h',
            'util/util.cc'
        )
        filter_file(
            r'#include "Geant4/"',
            '#include "Geant4/G4Normal3D.hh"\n#include "Geant4/"',
            'gm2Geane/gm2GeaneCylSurfaceTarget.cc'
        )
        filter_file(
            r'#include "Geant4/',
            '#include "Geant4/G4Normal3D.hh"\n#include "Geant4/G4Point3D.hh"\n#include "Geant4/',
            'gm2Geane/gm2GeanePlaneSurfaceTarget.cc',
        )
        filter_file(
            r'#include "Geant4/',
            '#include "Geant4/G4Normal3D.hh"\n#include "Geant4/G4Point3D.hh"\n#include "Geant4/',
            'gm2Geane/gm2GeaneCylSurfaceTarget.cc',
        )
        filter_file(
            r'#include "Geant4/',
            '#include "Geant4/G4Normal3D.hh"\n#include "Geant4/G4Point3D.hh"\n#include "Geant4/',
            'gm2Geane/gm2GeanePlaneSurfaceTarget.hh',
        )
        filter_file(
            'producer->produces', 
            '''
  // Kluge alert: 
  // produces() is protected, so make a subclass that lets us call it...
  // Really should rework this so we call produces() in a constructor
  // of a subclass of EDProducer to add our data, but for now..  
  class produceable : public art::EDProducer { friend void artg4::WriteGdmlService::callArtProduces(art::EDProducer * producer); };

  ((produceable *)producer)->produces''',
            'pluginActions/writeGdml/writeGdml_service.cc',
        )
        filter_file(
            'prod -> produces', 
            '''
  // Kluge alert: 
  // produces() is protected, so make a subclass that lets us call it...
  // Really should rework this so we call produces() in a constructor
  // of a subclass of EDProducer to add our data, but for now..  
  class produceable : public art::EDProducer { friend void artg4::DummyService::notifyArtOfProduction(art::EDProducer * prod); };

  ((produceable *)prod) -> produces''',
            'services/Dummy_service.cc',
        )

        filter_file(
            'producer->produces', 
            '''
  // Kluge alert: 
  // produces() is protected, so make a subclass that lets us call it...
  // Really should rework this so we call produces() in a constructor
  // of a subclass of EDProducer to add our data, but for now..  
  class produceable : public art::EDProducer { friend void artg4::PhysicalVolumeStoreService::callArtProduces(art::EDProducer * producer); };

  ((produceable *)producer)->produces''',
            'pluginActions/physicalVolumeStore/physicalVolumeStore_service.cc',
        )

        filter_file('G4MagInt_Driver','G4VIntegrationDriver','gm2Geane/gm2GeanePropagatorManager.cc')

        filter_file(
            r'logInfo_\("ArtG4Main"\)',
            'logInfo_("ArtG4Main"),\n     EDProducer(p)',
            'Core/artg4Main_module.cc'
        )
        filter_file(
            r'artg4_services_ActionHolder_service',
            'services_ActionHolder_service',
            'pluginActions/clock/CMakeLists.txt',
        )
        filter_file(
            r'artg4_services_ActionHolder_service',
            'services_ActionHolder_service',
            'pluginActions/particleGun/CMakeLists.txt',
        )


    def url_for_version(self, version):

        url = "https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/{0}.v{1}.tbz2"
        # url = 'https://github.com/SBNSoftware/{0}/archive/v{1}.tar.gz'
        return url.format(self.name, version.underscored)

    variant("cxxstd", default="17")

    depends_on("cetbuildtools", type=("build"))
    depends_on("cetmodules", type=("build"))
    depends_on("art", type=("build", "run"))
    depends_on("boost", type=("build","run"))
    depends_on("canvas-root-io", type=("build", "run"))
    depends_on("canvas", type=("build", "run"))
    depends_on("cetlib", type=("build","run"))
    depends_on("cetlib-except", type=("build","run"))
    depends_on("cetpkgsupport", type=("build", "run"))
    depends_on("clhep", type=("build", "run"))
    depends_on("fhicl-cpp", type=("build", "run"))

    # limiting geant4 to versions before 11.0.0 because 
    # all sorts of Spline calls are different
    # assuming this will be fixed in 9.70.01 and later
    # https://geant4.web.cern.ch/download/release-notes/notes-v11.0.0.html
    depends_on("geant4@:10.99.99 +vecgeom+opengl+x11", type=("build", "run"), when="@:9.70.00")
    depends_on("geant4@11: +vecgeom+tbb+opengl+x11", type=("build", "run"), when="@9.70.01:")
    depends_on("hep-concurrency", type=("build", "run"))
    depends_on("intel-tbb-oneapi", type=("build","run"))
    depends_on("messagefacility", type=("build", "run"))
    depends_on("range-v3", type=("build","run"))
    depends_on("root", type=("build", "run"))
    depends_on("vecgeom", type=("build", "run"))
    depends_on("veccore", type=("build", "run"))
    depends_on("xerces-c", type=("build", "run"))

    def cmake_args(self):
        args = [
            "-DCXX_STANDARD=%s" % self.spec.variants["cxxstd"].value,
            "-DOLD_STYLE_CONFIG_VARS=True",
            "-DCMAKE_MODULE_PATH={0}".format(
                          self.spec['cetmodules'].prefix.Modules.compat),
            "-DUPS_PRODUCT_VERSION=v{0}".format(self.spec.version.underscored),
            "-Dartg4_OLD_STYLE_CONFIG_VARS=True",
            "-DWANT_UPS=False",
        ]
        return args

#    @run_before("build")
#    def make_missing_target(self):
#        with working_dir(self.build_directory):
#            make("services_ActionHolder_service")


    def flag_handler(self, name, flags):
        # some include directories aren't properly added, so just always
        # include them...
        dep_pkg_list = ["cetbuildtools", "cetmodules", "art", "boost", 
             "canvas-root-io", "canvas", "cetlib", "cetlib-except", 
             "cetpkgsupport", "clhep", "fhicl-cpp", "geant4", 
             "hep-concurrency", "intel-tbb-oneapi", "messagefacility", 
             "range-v3", "root", "vecgeom", "veccore", "xerces-c",
        ]
        if name == 'cxxflags':
           for dep_pkg in dep_pkg_list:
               flags.append("-I%s" % self.spec[dep_pkg].prefix.include)
        return (None, None, flags)

    def setup_build_environment(self, env):
        # set environment variables used in CMakeLists.txt and cetmodules...
        env.set("CETBUILDTOOLS_VERSION", self.spec['cetbuildtools'].version)
        env.set("CANVAS_ROOT_IO_DIR", self.spec['canvas-root-io'].prefix)
        env.set("GEANT4_FQ_DIR", self.spec['geant4'].prefix)
        env.set("BOOST_DIR", self.spec['boost'].prefix)
        if 'cppunit' in self.spec: 
            env.set("CPPUNIT_DIR", self.spec['cppunit'].prefix)


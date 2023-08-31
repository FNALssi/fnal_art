# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
import glob


class Gm2geom(CMakePackage):
    """Gm2 experiment tracking code"""

    homepage = "https://redmine.fnal.gov/projects/gm2geom"
    url = "https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/gm2geom.v9_60_00.tbz2"
    git_base = "https://cdcvs.fnal.gov/projects/gm2geom"

    version("10.16.00", sha256="a98d877a5b11d93454dfc7251a4280ab268aa8edf58d249253cbe64bd1ce24c6")
    version("spack_branch", branch="feature/mengel_spack", git=git_base, get_full_repo=True)

    def url_for_version(self, version):
        return (
            "https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/gm2geom.v%s.tbz2"
            % version.underscored
        )


    depends_on("cetmodules", type=("build"))
    depends_on("cetpkgsupport", type=("build"))
    depends_on("cetbuildtools", type=("build"))
    depends_on("pkgconfig", type="build")
    depends_on("artg4", type=("build", "run"))
    depends_on("art", type=("build", "run"))
    depends_on("boost", type=("build", "run"))
    depends_on("canvas", type=("build", "run"))
    depends_on("cetlib", type=("build", "run"))
    depends_on("cetlib_except", type=("build", "run"))
    depends_on("eigen", type=("build", "run"))
    depends_on("fhicl-cpp", type=("build", "run"))
    depends_on("hep-concurrency", type=("build", "run"))
    depends_on("geant4", type=("build", "run"))
    depends_on("intel-tbb-oneapi", type=("build", "run"))
    depends_on("libwda", type=("build", "run"))
    depends_on("messagefacility", type=("build", "run"))
    depends_on("root", type=("build", "run"))
    depends_on("xerces-c", type=("build", "run"))


    # gm2geom doesn't list these packages as dependencies, because
    # that would make a dependency cycle, but it *does* need some
    # of their include files, so we pull them down as a resource so it
    # can find the include files it needs.
    resource(
       name="gm2util",
       url="https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/gm2util.v9_76_00.tbz2",
       sha256="d19e313fbb368f3996c96b4b45c549a5030a9caf16d74e71c54c594ee298e2c7",
       destination=".",
       placement="gm2util",
    )
    resource(
       name="gm2dataproducts",
       url="https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/gm2dataproducts.v9_60_00.tbz2",
       sha256="c453f4edff4d53635d177d553dfccc0a42c98d71a6945e0c4cffbeca254800e2",
       destination=".",
       placement="gm2dataproducts",

    )
    resource(
        name="gm2db",
        url="https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/gm2db.v9_60_00.tbz2",
        sha256="4931fd154c35124cf8d7f60fc8e7ce09ff693ca6e2e4a022aff432c7c5efe45c",
        destination=".",
        placement="gm2db",
    )
    resource(
       name="art_cpp_db_interfaces",
       url="https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/art_cpp_db_interfaces.v1_4.tbz2",
       sha256="a4500c065d4bf595f23b5ce2e1748cf590cc1b7468189774aa4b7b5d79f16d78",
       destination=".",
       placement="art_cpp_db_interfaces",
    )

    variant("cxxstd", default="17")

    def patch(self):

        # makefile assumes we are in a directory named gm2geom, and not 
        # "spack-src"...
        symlink(".", "gm2geom")
        filter_file('#include <cstring>', '#include <cstring>\n#include<boost/algorithm/string.hpp>', 'fields/FringeField.cc')
        filter_file('#include <cstring>', '#include <cstring>\n#include<boost/algorithm/string.hpp>', 'fields/StorageFieldController_service.cc')

        filter_file(
            r'add_subdirectory\( ups \)', 
            'if(WANT_UPS)\n add_subdirectory( ups )\nendif()\n',
            "CMakeLists.txt"
        )
        filter_file(r'find_ups_product\(libwda.*', 'find_package(libwda)', 'CMakeLists.txt')
        filter_file(
             r'find_ups_product\(gm2util',
             '# xx find_ups_product(gm2util',
             'CMakeLists.txt'
        )

        filter_file(
            r'cetlib/exception.h', 
            'cetlib_except/exception.h',
            'coordSystems/CoordSystemsStoreData.cc',
        )   
        filter_file(
            r'cetlib/exception.h', 
            'cetlib_except/exception.h',
            'strawtracker/StrawTrackerGeometryConstants_service.cc',
        )   
        filter_file(
            r'cetlib/exception.h', 
            'cetlib_except/exception.h',
            'fields/StorageFieldController_service.cc',
        )   
        filter_file(
           'gm2geom::BuildCoordSystems::BuildCoordSystems\(fhicl::ParameterSet const & p\)',
           'gm2geom::BuildCoordSystems::BuildCoordSystems(fhicl::ParameterSet const & p):\n'
           'EDProducer(p)',
           'coordSystems/BuildCoordSystems_module.cc',
        )
        # couldn't figure out what was needed here, picked a similar header(?)
        filter_file(
            r'#include "art/Framework/Services/Optional/TFileService.h"',
            '#include "art/Framework/Services/FileServiceInterfaces/CatalogInterface.h"',
            'common/StraightLineToolsTest_module.cc'
        )
        filter_file(
             'myProducer->produces', 
            '''
  // Kluge alert: 
  // produces() is protected, so make a subclass that lets us call it...
  // Really should rework this so we call produces() in a constructor
  // of a subclass of EDProducer to add our data, but for now..  
  class produceable : public art::EDProducer { friend void gm2FieldManager::callArtProduces(art::EDProducer* myProducer); };

  ((produceable *)myProducer)->produces''',
             'fields/gm2FieldManager_service.cc'
        )
        filter_file(
            'producer->produces',
            '''
  // Kluge alert: 
  // produces() is protected, so make a subclass that lets us call it...
  // Really should rework this so we call produces() in a constructor
  // of a subclass of EDProducer to add our data, but for now..  
  class produceable : public art::EDProducer { friend void gm2geom::CoordSystemsStore::callArtProduces(art::EDProducer * producer); };

  ((produceable *)producer)->produces''',
            'coordSystems/CoordSystemsStore_service.cc',
        )

        filter_file( 'gm2util_common', 'art_Utilities', 'strawtracker/CMakeLists.txt')
        filter_file( 'gm2geom_coordSystems$', 'gm2geom_coordSystems\n    art_Utilities ', 'coordSystems/CMakeLists.txt')

        for f in glob.glob('*/CMakeLists.txt'):
            filter_file(
                r'gm2geom_Core_Geometry_service',
                'Core_Geometry_service',
                f
            ) 
            filter_file(
                r'gm2geom_common_Gm2Constants_service',
                'common_Gm2Constants_service',
                f
            ) 
            filter_file(
                r'gm2geom_inflector_InflectorGeometry_service',
                'inflector_InflectorGeometry_service',
                f
            ) 
            filter_file(
                r'art_Framework_Services_Optional_TFileService_service',
                'art_Framework_Services_Optional_TrivialFileDelivery_service',
                f
            ) 
            filter_file(
                r'gm2geom_coordSystems_CoordSystemsStore_service',
                'coordSystems_CoordSystemsStore_service',
                f
            ) 

    def cmake_args(self):
        args = [
            "-DCXX_STANDARD=%s" % self.spec.variants["cxxstd"].value,
            "-DOLD_STYLE_CONFIG_VARS=True", 
            "-DCMAKE_MODULE_PATH={0}".format(
                          self.spec['cetmodules'].prefix.Modules.compat),
            "-DUPS_PRODUCT_VERSION=v{0}".format(self.spec.version.underscored),
            "-Dgm2geom_OLD_STYLE_CONFIG_VARS=True",
            "-DWANT_UPS=False",
        ]
        return args
      

    def setup_build_environment(self, env):
        env.set("CETBUILDTOOLS_VERSION", self.spec['cetbuildtools'].version)
        env.set("CANVAS_DIR", self.spec['canvas'].prefix)
        env.set("LIBWDA_DIR", self.spec['libwda'].prefix)
        env.set("LIBWDA_FQ_DIR", self.spec['libwda'].prefix)
        env.set("LIBWDA_LIB", self.spec['libwda'].prefix.lib)
        env.set("LIBWDA_INC", self.spec['libwda'].prefix.include)
        env.prepend_path('LD_LIBRARY_PATH', self.spec['art'].prefix.lib)

    def flag_handler(self, name, flags):
        # some include directories aren't properly added, so just always
        # include them...
        dep_pkg_list = [ 
            "artg4", "art", "boost", "canvas", "cetlib", "cetmodules",
            "eigen", "libwda", "xerces-c", "cetlib-except", "fhicl-cpp",
            "hep-concurrency", "intel-tbb-oneapi", "messagefacility", "root",
            "geant4",
        ]
        if name == 'cxxflags':
           for dep_pkg in dep_pkg_list:
               flags.append("-I%s" % self.spec[dep_pkg].prefix.include)
           flags.append("-I%s" % self.spec["eigen"].prefix.include.eigen3)
           flags.append("-I%s" % self.spec["root"].prefix.include.root)
           flags.append("-I%s/art_cpp_db_interfaces" % self.stage.source_path)
        if name == 'ldflags':
           flags.append("-L%s" % self.spec["cetlib"].prefix.lib)
           flags.append("-L%s" % self.spec["artg4"].prefix.lib)
           flags.append("-L%s" % self.spec["art"].prefix.lib)
        return (None, None, flags)


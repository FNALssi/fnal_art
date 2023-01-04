from spack.package import *

class Epics(MakefilePackage):
    
    homepage = "https://epics.anl.gov"
    url = "https://epics.anl.gov/download/base/base-7.0.7.tar.gz"
    git = "https://git.launchpad.net/epics-base"

    
    version("7.0.7", sha256="44d6980e19c7ad097b9e3d20c3401fb20699ed346afc307c8d1b44cf7109d475")
    depends_on('gmake', type='build')

    def install(self, spec, prefix):
        install_tree('.', prefix)
        

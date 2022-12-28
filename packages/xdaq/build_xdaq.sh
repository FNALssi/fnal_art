

for pack in $Packages;do
  cd $pack
  make install
  cd $daqdir
done

cd $INSTALL_PREFIX/x86_64_*
mv doc share
cp -a $daqdir/build ./config
cp config/favicon.ico htdocs
find scripts -type f -exec mv {} bin \;
rm -rf scripts
mkdir etc
cp -p $daqdir/xdaq/etc/*.profile* etc
#echo Installing docs...

echo fixup libs??? cd lib - do ln -s

#
mv share ${product_dir}/${package}/${pkgver}
mv include ${product_dir}/${package}/${pkgver}
mkdir -p ${pkgdir}
mv bin ${pkgdir}
mv config ${pkgdir}
mv etc ${pkgdir}
mv htdocs ${pkgdir}
mv lib ${pkgdir}

echo Done with install.

ssi_info "finished building ${package} ${pkgver}"

####################################
# Pre-declaration processing. *C*
#
# Move things, install from contrib, clean build products from in-source
# builds, etc.
####################################

echo Cleaning up...
cd "${pkgdir}"   # e.g. /home/ron/work/otsdaqPrj/myFW_workdir/xdaq/v14_4_0/Linux64bit+3.10-2.17-e14-prof

echo Wrapper scripts and config files...
find bin etc -type f | while read file; do
  [[ "$(file "${file}")" == *"text"* ]] && \
   perl -wapi\~ -e 's&\Q'"${pkgdir}"'\E&\${XDAQ_FQ_DIR}&g' "${file}"
done

#rm -rvf lib/pkgconfig lib/*.la
find . -name '*~' -exec rm -vf \{\} \;

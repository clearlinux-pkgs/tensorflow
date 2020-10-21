Name     : tensorflow
Version  : 2.3.1
Release  : 102
URL      : https://github.com/tensorflow/tensorflow/archive/v2.3.1/tensorflow-2.3.1.tar.gz
Source0  : https://github.com/tensorflow/tensorflow/archive/v2.3.1/tensorflow-2.3.1.tar.gz
Summary  : Machine learning framework
Group    : Development/Tools
License  : Apache-2.0 GPL-3.0 MPL-2.0-no-copyleft-exception
Requires : Keras
Requires : Keras_Applications
Requires : Keras_Preprocessing
Requires : Markdown
Requires : Werkzeug
Requires : absl-py
Requires : astor
Requires : astunparse
Requires : backports.weakref
Requires : bleach
Requires : gast
Requires : google-pasta
Requires : grpcio
Requires : h5py
Requires : opt_einsum
Requires : protobuf
Requires : tensorboard
Requires : tensorflow-estimator
Requires : termcolor
Requires : wrapt
Requires : wheel
Requires : six
BuildRequires : Keras
BuildRequires : Keras_Applications
BuildRequires : Keras_Preprocessing
BuildRequires : bazel
BuildRequires : c-ares-dev
BuildRequires : gcc9
BuildRequires : gcc9-dev
BuildRequires : mkl-dnn-dev
BuildRequires : numpy
BuildRequires : openjdk
BuildRequires : openjdk-dev
BuildRequires : pip
BuildRequires : protobuf
BuildRequires : protobuf-c
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : wheel

# SOURCES BEGIN
Source10: http://mirror.tensorflow.org/files.pythonhosted.org/packages/c7/11/345f3173809cea7f1a193bfbf02403fff250a3360e0e118a1630985e547d/dill-0.3.1.1.tar.gz
Source11: https://dl.google.com/go/go1.13.3.linux-amd64.tar.gz
Source12: https://files.pythonhosted.org/packages/83/4a/07c7e59cef23fb147454663c3271c21da68ba2ab141427c20548ae5a8a4d/gast-0.4.0.tar.gz
Source13: https://files.pythonhosted.org/packages/ec/c4/8c651f3240a73c28a218194f3d527eb2be5a173d08501060cdee84ade33f/tblib-1.3.2.tar.gz
Source14: https://github.com/Maratyszcza/FP16/archive/4dfe081cf6bcd15db339cf2680b9281b8451eeb3.zip
Source15: https://github.com/Maratyszcza/psimd/archive/072586a71b55b7f8c584153d223e95687148a900.zip
Source16: https://github.com/Maratyszcza/pthreadpool/archive/029c88620802e1361ccf41d1970bd5b07fd6b7bb.zip
Source17: https://github.com/aws/aws-sdk-cpp/archive/1.7.336.tar.gz
Source18: https://github.com/awslabs/aws-c-common/archive/v0.4.29.tar.gz
Source19: https://github.com/awslabs/aws-c-event-stream/archive/v0.1.4.tar.gz
Source20: https://github.com/awslabs/aws-checksums/archive/v0.1.5.tar.gz
Source21: https://github.com/bazelbuild/bazel-gazelle/releases/download/0.18.2/bazel-gazelle-0.18.2.tar.gz
Source22: https://github.com/bazelbuild/bazel-skylib/archive/1.0.2.tar.gz
Source23: https://github.com/bazelbuild/rules_docker/releases/download/v0.12.1/rules_docker-v0.12.1.tar.gz
Source24: https://github.com/bazelbuild/rules_go/releases/download/v0.20.1/rules_go-v0.20.1.tar.gz
Source25: https://github.com/bazelbuild/rules_python/archive/f46e953f6e0315a3f884154f9395a32ec9999eab.tar.gz
Source26: https://github.com/c-ares/c-ares/archive/e982924acee7f7313b4baa4ee5ec000c5e373c30.tar.gz
Source27: https://github.com/google/XNNPACK/archive/8b283aa30a3186c6e640aed520543e9c067132d2.zip
Source28: https://github.com/llvm/llvm-project/archive/7e825abd5704ce28b166f9463d4bd304348fd2a9.tar.gz
Source29: https://github.com/protocolbuffers/upb/archive/9effcbcb27f0a665f9f345030188c0b291e32482.tar.gz
Source30: https://mirror.bazel.build/github.com/bazelbuild/rules_java/archive/7cf3cefd652008d0a64a419c34c13bdca6c8f178.zip
Source31: https://mirror.bazel.build/github.com/bazelbuild/rules_proto/archive/97d8af4dc474595af3900dd85cb3a29ad28cc313.tar.gz
Source32: https://storage.googleapis.com/mirror.tensorflow.org/curl.haxx.se/download/curl-7.69.1.tar.gz
Source33: https://storage.googleapis.com/mirror.tensorflow.org/download.open-mpi.org/release/hwloc/v2.0/hwloc-2.0.3.tar.gz
Source34: https://storage.googleapis.com/mirror.tensorflow.org/files.pythonhosted.org/packages/f3/af/4182184d3c338792894f34a62672919db7ca008c89abee9b564dd34d8029/astunparse-1.6.3.tar.gz
Source35: https://storage.googleapis.com/mirror.tensorflow.org/github.com/GoogleCloudPlatform/tensorflow-gcp-tools/archive/2643d8caeba6ca2a6a0b46bb123953cb95b7e7d5.tar.gz
Source36: https://storage.googleapis.com/mirror.tensorflow.org/github.com/GrahamDumpleton/wrapt/archive/1.11.1.tar.gz
Source37: https://storage.googleapis.com/mirror.tensorflow.org/github.com/LMDB/lmdb/archive/LMDB_0.9.22.tar.gz
Source38: https://storage.googleapis.com/mirror.tensorflow.org/github.com/Maratyszcza/FXdiv/archive/b408327ac2a15ec3e43352421954f5b1967701d1.zip
Source39: https://storage.googleapis.com/mirror.tensorflow.org/github.com/NVlabs/cub/archive/1.8.0.zip
Source40: https://storage.googleapis.com/mirror.tensorflow.org/github.com/NervanaSystems/ngraph-tf/archive/v0.9.0.zip
Source41: https://storage.googleapis.com/mirror.tensorflow.org/github.com/NervanaSystems/ngraph/archive/v0.11.0.tar.gz
Source42: https://storage.googleapis.com/mirror.tensorflow.org/github.com/abseil/abseil-cpp/archive/df3ea785d8c30a9503321a3d35ee7d35808f190d.tar.gz
Source43: https://storage.googleapis.com/mirror.tensorflow.org/github.com/abseil/abseil-py/archive/pypi-v0.9.0.tar.gz
Source44: https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/apple_support/archive/501b4afb27745c4813a88ffa28acd901408014e4.tar.gz
Source45: https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/bazel-toolchains/archive/92dd8a7a518a2fb7ba992d47c8b38299fe0be825.tar.gz
Source46: https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_android/archive/v0.1.1.zip
Source47: https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_apple/archive/5131f3d46794bf227d296c82f30c2499c9de3c5b.tar.gz
Source48: https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_cc/archive/01d4a48911d5e7591ecb1c06d3b8af47fe872371.zip
Source49: https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_closure/archive/308b05b2419edb5c8ee0471b67a40403df940149.tar.gz
Source50: https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_python/releases/download/0.0.1/rules_python-0.0.1.tar.gz
Source51: https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_swift/archive/3eeeb53cebda55b349d64c9fc144e18c5f7c0eb8.tar.gz
Source52: https://storage.googleapis.com/mirror.tensorflow.org/github.com/cython/cython/archive/0.28.4.tar.gz
Source53: https://storage.googleapis.com/mirror.tensorflow.org/github.com/dmlc/dlpack/archive/3efc489b55385936531a06ff83425b719387ec63.tar.gz
Source54: https://storage.googleapis.com/mirror.tensorflow.org/github.com/glennrp/libpng/archive/v1.6.37.tar.gz
Source55: https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/boringssl/archive/80ca9f9f6ece29ab132cce4cf807a9465a18cfac.tar.gz
Source56: https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/double-conversion/archive/3992066a95b823efc8ccc1baf82a1cfc73f6e9b8.zip
Source57: https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/farmhash/archive/816a4ae622e964763ca0862d9dbd19324a1eaf45.tar.gz
Source58: https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/flatbuffers/archive/v1.12.0.tar.gz
Source59: https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/gemmlowp/archive/fda83bdc38b118cc6b56753bd540caa49e570745.zip
Source60: https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/highwayhash/archive/fd3d9af80465e4383162e4a7c5e2f406e82dd968.tar.gz
Source61: https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/nsync/archive/1.22.0.tar.gz
Source62: https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/pasta/archive/v0.1.8.tar.gz
Source63: https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/re2/archive/506cfa4bffd060c06ec338ce50ea3468daa6c814.tar.gz
Source64: https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/ruy/archive/34ea9f4993955fa1ff4eb58e504421806b7f2e8f.zip
Source65: https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/snappy/archive/1.1.8.tar.gz
Source66: https://storage.googleapis.com/mirror.tensorflow.org/github.com/googleapis/google-cloud-cpp/archive/v1.14.0.tar.gz
Source67: https://storage.googleapis.com/mirror.tensorflow.org/github.com/googleapis/googleapis/archive/541b1ded4abadcc38e8178680b0677f65594ea6f.zip
Source68: https://storage.googleapis.com/mirror.tensorflow.org/github.com/grpc/grpc/archive/b54a5b338637f92bfcf4b0bc05e0f57a5fd8fadd.tar.gz
Source69: https://storage.googleapis.com/mirror.tensorflow.org/github.com/hfp/libxsmm/archive/1.14.tar.gz
Source70: https://storage.googleapis.com/mirror.tensorflow.org/github.com/intel/ARM_NEON_2_x86_SSE/archive/1200fe90bb174a6224a525ee60148671a786a71f.tar.gz
Source71: https://storage.googleapis.com/mirror.tensorflow.org/github.com/intel/mkl-dnn/releases/download/v0.21/mklml_lnx_2019.0.5.20190502.tgz
Source72: https://storage.googleapis.com/mirror.tensorflow.org/github.com/intel/mkl-dnn/releases/download/v0.21/mklml_mac_2019.0.5.20190502.tgz
Source73: https://storage.googleapis.com/mirror.tensorflow.org/github.com/intel/mkl-dnn/releases/download/v0.21/mklml_win_2020.0.20190813.zip
Source74: https://storage.googleapis.com/mirror.tensorflow.org/github.com/joe-kuo/sobol_data/archive/835a7d7b1ee3bc83e575e302a985c66ec4b65249.tar.gz
Source75: https://github.com/libjpeg-turbo/libjpeg-turbo/archive/2.0.5/libjpeg-turbo-2.0.5.tar.gz
Source76: https://storage.googleapis.com/mirror.tensorflow.org/github.com/mborgerding/kissfft/archive/36dbc057604f00aacfc0288ddad57e3b21cfc1b8.tar.gz
Source77: https://storage.googleapis.com/mirror.tensorflow.org/github.com/nlohmann/json/archive/v3.4.0.tar.gz
Source78: https://storage.googleapis.com/mirror.tensorflow.org/github.com/oneapi-src/oneDNN/archive/v0.21.3.tar.gz
Source79: https://storage.googleapis.com/mirror.tensorflow.org/github.com/oneapi-src/oneDNN/archive/v1.4.tar.gz
Source80: https://storage.googleapis.com/mirror.tensorflow.org/github.com/open-source-parsers/jsoncpp/archive/1.9.2.tar.gz
Source81: https://storage.googleapis.com/mirror.tensorflow.org/github.com/petewarden/OouraFFT/archive/v1.0.tar.gz
Source82: https://storage.googleapis.com/mirror.tensorflow.org/github.com/protocolbuffers/protobuf/archive/v3.9.2.zip
Source83: https://storage.googleapis.com/mirror.tensorflow.org/github.com/pybind/pybind11/archive/v2.4.3.tar.gz
Source84: https://storage.googleapis.com/mirror.tensorflow.org/github.com/pytorch/cpuinfo/archive/6cecd15784fcb6c5c0aa7311c6248879ce2cb8b2.zip
Source85: https://storage.googleapis.com/mirror.tensorflow.org/github.com/pytorch/cpuinfo/archive/d5e37adf1406cf899d7d9ec1d317c47506ccb970.tar.gz
Source86: https://storage.googleapis.com/mirror.tensorflow.org/github.com/unicode-org/icu/archive/release-64-2.zip
Source87: https://storage.googleapis.com/mirror.tensorflow.org/gitlab.com/libeigen/eigen/-/archive/386d809bde475c65b7940f290efe80e6a05878c4/eigen-386d809bde475c65b7940f290efe80e6a05878c4.tar.gz
Source88: https://storage.googleapis.com/mirror.tensorflow.org/pilotfiber.dl.sourceforge.net/project/giflib/giflib-5.2.1.tar.gz
Source89: https://storage.googleapis.com/mirror.tensorflow.org/pypi.python.org/packages/8a/48/a76be51647d0eb9f10e2a4511bf3ffb8cc1e6b14e9e4fab46173aa79f981/termcolor-1.1.0.tar.gz
Source90: https://storage.googleapis.com/mirror.tensorflow.org/pypi.python.org/packages/99/80/f9482277c919d28bebd85813c0a70117214149a96b08981b72b63240b84c/astor-0.7.1.tar.gz
Source91: https://storage.googleapis.com/mirror.tensorflow.org/pypi.python.org/packages/bc/cc/3cdb0a02e7e96f6c70bd971bc8a90b8463fda83e264fa9c5c1c98ceabd81/backports.weakref-1.0rc1.tar.gz
Source92: https://storage.googleapis.com/mirror.tensorflow.org/pypi.python.org/packages/bf/3e/31d502c25302814a7c2f1d3959d2a3b3f78e509002ba91aea64993936876/enum34-1.1.6.tar.gz
Source93: https://storage.googleapis.com/mirror.tensorflow.org/pypi.python.org/packages/c5/60/6ac26ad05857c601308d8fb9e87fa36d0ebf889423f47c3502ef034365db/functools32-3.2.3-2.tar.gz
Source94: https://storage.googleapis.com/mirror.tensorflow.org/pypi.python.org/packages/f6/d6/44792ec668bcda7d91913c75237314e688f70415ab2acd7172c845f0b24f/opt_einsum-2.3.2.tar.gz
Source95: https://storage.googleapis.com/mirror.tensorflow.org/pypi.python.org/packages/source/s/six/six-1.12.0.tar.gz
Source96: https://storage.googleapis.com/mirror.tensorflow.org/www.nasm.us/pub/nasm/releasebuilds/2.13.03/nasm-2.13.03.tar.bz2
Source97: https://storage.googleapis.com/mirror.tensorflow.org/www.sqlite.org/2020/sqlite-amalgamation-3330000.zip
Source98: https://storage.googleapis.com/mirror.tensorflow.org/zlib.net/zlib-1.2.11.tar.gz
# SOURCES END

# From https://storage.googleapis.com/mirror.tensorflow.org/raw.githubusercontent.com/simonpercivall/astunparse/v1.6.2/LICENSE
Source1000 : ASTUNPARSE_LICENSE
# From https://storage.googleapis.com/mirror.tensorflow.org/docs.python.org/2.7/_sources/license.rst.txt
# Note: We need the mirrored copy because the non-mirrored copy is a living
# document. Since the mirrored copy was made, a copyright year and URL were
# modified within the document.
Source1001 : PYTHON2_LICENSE

Source1010 : answers.txt
Source1011 : MNIST_example.ipynb

Patch1 : 0001-gast-update-to-0.4.0.patch
Patch2 : 0002-WORKSPACE-changes-as-bazel-version-update.patch
Patch3 : 0003-Provide-overload-to-cope-with-const-ness-change-of-N.patch
Patch4 : 0004-Mark-bfloat16-ufunc-arguments-const-to-fix-compilati.patch
Patch5 : 0005-Relax-numpy-requirement.patch
Patch6 : 0006-Update-libjpeg-turbo-to-2.0.5.patch

%description
TensorFlow is an end-to-end open source platform for machine learning. It has a
comprehensive, flexible ecosystem of tools, libraries, and community resources
that lets researchers push the state-of-the-art in ML and developers easily
build and deploy ML-powered applications.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

InstallCacheBazel() {
  sha256=$(sha256sum $1 | cut -f1 -d" ")
  mkdir -p /var/tmp/cache/content_addressable/sha256/$sha256
  cp $1 /var/tmp/cache/content_addressable/sha256/$sha256/file
}

# CACHE BAZEL BEGIN
InstallCacheBazel %{SOURCE10}
InstallCacheBazel %{SOURCE11}
InstallCacheBazel %{SOURCE12}
InstallCacheBazel %{SOURCE13}
InstallCacheBazel %{SOURCE14}
InstallCacheBazel %{SOURCE15}
InstallCacheBazel %{SOURCE16}
InstallCacheBazel %{SOURCE17}
InstallCacheBazel %{SOURCE18}
InstallCacheBazel %{SOURCE19}
InstallCacheBazel %{SOURCE20}
InstallCacheBazel %{SOURCE21}
InstallCacheBazel %{SOURCE22}
InstallCacheBazel %{SOURCE23}
InstallCacheBazel %{SOURCE24}
InstallCacheBazel %{SOURCE25}
InstallCacheBazel %{SOURCE26}
InstallCacheBazel %{SOURCE27}
InstallCacheBazel %{SOURCE28}
InstallCacheBazel %{SOURCE29}
InstallCacheBazel %{SOURCE30}
InstallCacheBazel %{SOURCE31}
InstallCacheBazel %{SOURCE32}
InstallCacheBazel %{SOURCE33}
InstallCacheBazel %{SOURCE34}
InstallCacheBazel %{SOURCE35}
InstallCacheBazel %{SOURCE36}
InstallCacheBazel %{SOURCE37}
InstallCacheBazel %{SOURCE38}
InstallCacheBazel %{SOURCE39}
InstallCacheBazel %{SOURCE40}
InstallCacheBazel %{SOURCE41}
InstallCacheBazel %{SOURCE42}
InstallCacheBazel %{SOURCE43}
InstallCacheBazel %{SOURCE44}
InstallCacheBazel %{SOURCE45}
InstallCacheBazel %{SOURCE46}
InstallCacheBazel %{SOURCE47}
InstallCacheBazel %{SOURCE48}
InstallCacheBazel %{SOURCE49}
InstallCacheBazel %{SOURCE50}
InstallCacheBazel %{SOURCE51}
InstallCacheBazel %{SOURCE52}
InstallCacheBazel %{SOURCE53}
InstallCacheBazel %{SOURCE54}
InstallCacheBazel %{SOURCE55}
InstallCacheBazel %{SOURCE56}
InstallCacheBazel %{SOURCE57}
InstallCacheBazel %{SOURCE58}
InstallCacheBazel %{SOURCE59}
InstallCacheBazel %{SOURCE60}
InstallCacheBazel %{SOURCE61}
InstallCacheBazel %{SOURCE62}
InstallCacheBazel %{SOURCE63}
InstallCacheBazel %{SOURCE64}
InstallCacheBazel %{SOURCE65}
InstallCacheBazel %{SOURCE66}
InstallCacheBazel %{SOURCE67}
InstallCacheBazel %{SOURCE68}
InstallCacheBazel %{SOURCE69}
InstallCacheBazel %{SOURCE70}
InstallCacheBazel %{SOURCE71}
InstallCacheBazel %{SOURCE72}
InstallCacheBazel %{SOURCE73}
InstallCacheBazel %{SOURCE74}
InstallCacheBazel %{SOURCE75}
InstallCacheBazel %{SOURCE76}
InstallCacheBazel %{SOURCE77}
InstallCacheBazel %{SOURCE78}
InstallCacheBazel %{SOURCE79}
InstallCacheBazel %{SOURCE80}
InstallCacheBazel %{SOURCE81}
InstallCacheBazel %{SOURCE82}
InstallCacheBazel %{SOURCE83}
InstallCacheBazel %{SOURCE84}
InstallCacheBazel %{SOURCE85}
InstallCacheBazel %{SOURCE86}
InstallCacheBazel %{SOURCE87}
InstallCacheBazel %{SOURCE88}
InstallCacheBazel %{SOURCE89}
InstallCacheBazel %{SOURCE90}
InstallCacheBazel %{SOURCE91}
InstallCacheBazel %{SOURCE92}
InstallCacheBazel %{SOURCE93}
InstallCacheBazel %{SOURCE94}
InstallCacheBazel %{SOURCE95}
InstallCacheBazel %{SOURCE96}
InstallCacheBazel %{SOURCE97}
InstallCacheBazel %{SOURCE98}
# CACHE BAZEL END

InstallCacheBazel %{SOURCE1000}
InstallCacheBazel %{SOURCE1001}

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1485959355
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${buildroot}/usr/lib64:${buildroot}/usr/lib:${builddir}/usr/://tensorflow/contrib
export GCC_IGNORE_WERROR=1

# external/upb fails to build with GCC 10...
# https://github.com/tensorflow/tensorflow/issues/39467
export CC=gcc-9
export CXX=g++-9

./configure < %{SOURCE1010}

bazel --output_base=/var/tmp/bazel build \
  --repository_cache=/var/tmp/cache \
  --config=v2 \
  --config=opt \
  --copt=-Wno-sign-compare \
  --verbose_failures \
  //tensorflow/tools/pip_package:build_pip_package

bazel-bin/tensorflow/tools/pip_package/build_pip_package /var/tmp
bazel clean

export TF_BUILD_MAVX=MAVX2
./configure < %{SOURCE1010}
mkdir -pv /var/tmp/avx2
bazel --output_base=/var/tmp/bazel build \
  --repository_cache=/var/tmp/cache \
  --config=v2 \
  --config=opt \
  --copt=-mavx2 \
  --copt=-march=haswell \
  --copt=-mfma \
  --verbose_failures \
  //tensorflow/tools/pip_package:build_pip_package

bazel-bin/tensorflow/tools/pip_package/build_pip_package /var/tmp/avx2/
bazel clean

export TF_BUILD_MAVX=MAVX512
./configure < %{SOURCE1010}
mkdir -pv /var/tmp/avx512
bazel --output_base=/var/tmp/bazel build \
  --repository_cache=/var/tmp/cache \
  --config=v2 \
  --config=opt \
  --copt=-mavx2 \
  --copt=-march=skylake-avx512 \
  --copt=-mfma \
  --verbose_failures \
  //tensorflow/tools/pip_package:build_pip_package

bazel-bin/tensorflow/tools/pip_package/build_pip_package /var/tmp/avx512/


%install
export SOURCE_DATE_EPOCH=1485959355

cpver="cp$(python3 -c "import sys; print(f'{sys.version_info[0]}{sys.version_info[1]}')")"
wheel="tensorflow-%{version}-$cpver-$cpver-linux_x86_64.whl"

pip3 install --no-deps --user --force-reinstall /var/tmp/avx512/"$wheel"
for i in $(find $HOME/.local/ -name "*.so.2"); do
  mv -v $i $i.avx512
done

pip3 install --no-deps --user --force-reinstall /var/tmp/avx2/"$wheel"
for i in $(find $HOME/.local/ -name "*.so.2"); do
  mv -v $i $i.avx2
done

pip3 install --no-deps --user --force-reinstall /var/tmp/"$wheel"

sitedir="$(python3 -c "import sys; print(sys.path[-1])")"

avx512_dest="$HOME/.local/${sitedir#/usr/}/tensorflow/haswell/avx512_1"
mkdir -pv $avx512_dest
for i in $(find $HOME/.local/ -name "*.so.2.avx512"); do
  base=$(basename $i)
  mv -v $i "$avx512_dest"/"${base%.avx512}"
done

avx2_dest="$HOME/.local/${sitedir#/usr/}/tensorflow/haswell"
for i in $(find $HOME/.local/ -name "*.so.2.avx2"); do
  base=$(basename $i)
  mv -v $i "$avx2_dest"/"${base%.avx2}"
done

rm -fv $HOME/.local/bin/tf_upgrade_v2
mkdir -pv %{buildroot}/usr
mv -v $HOME/.local/bin %{buildroot}/usr/
mv -v $HOME/.local/lib %{buildroot}/usr/

install -Dm0644 %{SOURCE1011} %{buildroot}/usr/share/doc/tensorflow/MNIST_example.ipynb

%files
%defattr(-,root,root,-)
/usr/bin/estimator_ckpt_converter
/usr/bin/saved_model_cli
%exclude /usr/bin/tensorboard
/usr/bin/tflite_convert
/usr/bin/toco
/usr/bin/toco_from_protos
/usr/lib/python3*/site-packages/*
/usr/share/doc/tensorflow/MNIST_example.ipynb

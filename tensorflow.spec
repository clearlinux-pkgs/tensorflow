Name     : tensorflow
Version  : 1.4.0
Release  : 23
URL      : https://github.com/tensorflow/tensorflow/archive/v1.4.0.tar.gz
Source0  : https://github.com/tensorflow/tensorflow/archive/v1.4.0.tar.gz
Source10 : http://localhost/tensorflow/tensorflow-1.4.0-cp36-cp36m-linux_x86_64.whlavx2
Source15 : http://localhost/tensorflow/tensorflow-1.4.0-cp36-cp36m-linux_x86_64.whlavx512
Source20 : http://localhost/tensorflow/tensorflow-1.4.0-cp36-cp36m-linux_x86_64.whlgeneric

Source100: grab-and-bag.sh
Source101: answers.txt
Source102: powf.patch
Source103: MNIST_example.ipynb

Source104: 0001-enum34-is-only-required-for-Python-3.4.patch

Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 GPL-3.0 MPL-2.0-no-copyleft-exception
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : wheel
BuildRequires : numpy
BuildRequires : six
BuildRequires : protobuf
BuildRequires : protobuf-c


Requires: Werkzeug
Requires: Markdown
Requires: bleach
Requires: backports.weakref
Requires: tensorboard

%description
TensorFlow

%prep
%setup -q  -n tensorflow-1.4.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1485959355

%install
export SOURCE_DATE_EPOCH=1485959355
rm -rf %{buildroot}
mkdir -p %{buildroot}

mv %{SOURCE10} tensorflow-1.4.0-cp36-cp36m-linux_x86_64.whl

pip3 install --no-deps  --root %{buildroot} tensorflow-1.4.0-cp36-cp36m-linux_x86_64.whl
for i in `find %{buildroot} -name "*.so" `; do mv $i $i.avx2 ; done
mkdir -p %{buildroot}/usr/lib/python3.6/site-packages/tensorflow/haswell/avx512_1
mv %{buildroot}//usr/lib/python3.6/site-packages/tensorflow/libtensorflow_framework.so.avx2 %{buildroot}/usr/lib/python3.6/site-packages/tensorflow/haswell/libtensorflow_framework.so

#mv %{SOURCE15} tensorflow-1.4.0-cp36-cp36m-linux_x86_64.whl
#
#pip3 install --no-deps  --root %{buildroot} tensorflow-1.4.0-cp36-cp36m-linux_x86_64.whl
#for i in `find %{buildroot} -name "*.so" `; do mv $i $i.avx512 ; done

 
#mv %{buildroot}/usr/lib/python3.6/site-packages/tensorflow/libtensorflow_framework.so.avx512 %{buildroot}/usr/lib/python3.6/site-packages/tensorflow/haswell/avx512_1/libtensorflow_framework.so

mv %{SOURCE20} tensorflow-1.4.0-cp36-cp36m-linux_x86_64.whl

pip3 install --no-deps --force-reinstall  --root %{buildroot} tensorflow-1.4.0-cp36-cp36m-linux_x86_64.whl

mkdir -p %{buildroot}/usr/share/doc/tensorflow/
mv %{SOURCE103} %{buildroot}/usr/share/doc/tensorflow/MNIST_example.ipynb

pushd %{buildroot}/usr/lib/python3.6/site-packages
cat %{SOURCE104} | patch -p1
popd

%files
%defattr(-,root,root,-)
/usr/lib/python3.6/site-packages
/usr/bin/tensorboard
/usr/bin/saved_model_cli
/usr/share/doc/*

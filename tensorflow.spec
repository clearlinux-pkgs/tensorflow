Name     : tensorflow
Version  : 1.0.0
Release  : 7
URL      : https://github.com/tensorflow/tensorflow/archive/v1.0.0-alpha.tar.gz
Source0  : https://github.com/tensorflow/tensorflow/archive/v1.0.0.tar.gz
Source10 : http://localhost/tensorflow/tensorflow-1.0.0-cp36-cp36m-linux_x86_64.whlavx2
Source15 : http://localhost/tensorflow/tensorflow-1.0.0-cp36-cp36m-linux_x86_64.whlavx512
Source20 : http://localhost/tensorflow/tensorflow-1.0.0-cp36-cp36m-linux_x86_64.whlgeneric

Source100: grab-and-bag.sh
Source101: answers.txt
Source102: powf.patch

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



%define __strip /bin/true
%define debug_package %{nil}

%description
TensorFlow

%prep
%setup -q  -n tensorflow-1.0.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1485959355

%install
export SOURCE_DATE_EPOCH=1485959355
rm -rf %{buildroot}
mkdir -p %{buildroot}

mv %{SOURCE10} tensorflow-1.0.0-cp36-cp36m-linux_x86_64.whl

pip3 install --no-deps  --root %{buildroot} tensorflow-1.0.0-cp36-cp36m-linux_x86_64.whl
for i in `find %{buildroot} -name "*.so" `; do mv $i $i.avx2 ; done

mv %{SOURCE15} tensorflow-1.0.0-cp36-cp36m-linux_x86_64.whl

pip3 install --no-deps  --root %{buildroot} tensorflow-1.0.0-cp36-cp36m-linux_x86_64.whl
for i in `find %{buildroot} -name "*.so" `; do mv $i $i.avx512 ; done

mv %{SOURCE20} tensorflow-1.0.0-cp36-cp36m-linux_x86_64.whl

pip3 install --no-deps --force-reinstall  --root %{buildroot} tensorflow-1.0.0-cp36-cp36m-linux_x86_64.whl


%files
%defattr(-,root,root,-)
/usr/lib/python3.6/site-packages
/usr/bin/tensorboard

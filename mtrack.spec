Name:           xorg-x11-drv-mtrack
Version:        git
Release:        1
Summary:        Multitouch touchpad driver

License:        GPLv2
URL:            https://github.com/p2rkw/xf86-input-mtrack/
Source0:        https://github.com/p2rkw/xf86-input-mtrack/

BuildRequires:  xorg-x11-util-macros xorg-x11-server-devel mtdev-devel
Requires:       mtdev 

%description
An Xorg driver for multitouch trackpads. Supports any trackpad whose kernel driver uses the slotted multitouch protocol. For more information on the protocol see the kernel documentation.

This driver is compatible with Xorg server versions 1.7 to 1.12. It requires the mtdev library to operate.

%prep
git clone https://github.com/p2rkw/xf86-input-mtrack/ $RPM_BUILD_DIR

%build
autoreconf --install
./configure --with-xorg-module-dir=/usr/lib64/xorg/modules
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
libtool --finish %{_buildrootdir}/xorg-x11-drv-mtrack*/usr/lib64/xorg/modules/input

%files
%doc
%defattr(-,root,root)
%_libdir/xorg/modules/input/mtrack_drv.la
%_libdir/xorg/modules/input/mtrack_drv.so




%changelog
* Thu Jun 09 2016 Gianguido Sorà <g.sora4@gmail.com>
- this time be a good release number please (g.sora4@gmail.com)
- ffs (g.sora4@gmail.com)
- remove fedora release from version tag (g.sora4@gmail.com)

* Thu Jun 09 2016 Gianguido Sorà <g.sora4@gmail.com>
- this time be a good release number please (g.sora4@gmail.com)
- ffs (g.sora4@gmail.com)
- remove fedora release from version tag (g.sora4@gmail.com)

* Thu Jun 09 2016 Gianguido Sorà <g.sora4@gmail.com>
- ffs (g.sora4@gmail.com)
- remove fedora release from version tag (g.sora4@gmail.com)

* Thu Jun 09 2016 Gianguido Sorà <g.sora4@gmail.com>
- remove fedora release from version tag (g.sora4@gmail.com)

* Thu Jun 09 2016 Gianguido Sorà <g.sora4@gmail.com> git-2
- add git as a build dependency (g.sora4@gmail.com)

* Thu Jun 09 2016 Gianguido Sorà <g.sora4@gmail.com>
- add git as a build dependency (g.sora4@gmail.com)

* Thu Jun 09 2016 Gianguido Sorà <g.sora4@gmail.com>
- add git as a build dependency (g.sora4@gmail.com)

* Thu Jun 09 2016 Gianguido Sorà <g.sora4@gmail.com>
- add git as a build dependency (g.sora4@gmail.com)

* Thu Jun 09 2016 Gianguido Sorà <g.sora4@gmail.com>
- add git as a build dependency (g.sora4@gmail.com)

* Thu Jun 09 2016 Gianguido Sorà <g.sora4@gmail.com>
- add git as a build dependency (g.sora4@gmail.com)

* Thu Jun 09 2016 Gianguido Sorà <g.sora4@gmail.com> git-1
- new package built with tito

* Thu Jun 09 2016 Gianguido Sorà <g.sora4@gmail.com> - git-3
- First RPM release, built against commit c8a1f85 of
  https://github.com/p2rkw/xf86-input-mtrack


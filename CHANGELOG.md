# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.6.7] - 2023-04-26

### Changed

- Update Windows app version to `6119`.
- Update Android app version to `2011`.
- Removal of the load balancer for the license request.
- Update `README.md`

### Fixed

- Release date of versions in `CHANGELOG.md` 

## [1.6.6] - 2023-03-20

### Changed

- Update Windows app version to `6114`.
- Update Android app version to `2010`.

## [1.6.5] - 2023-03-12

### Changed

- Update Windows app version to `6112`.

## [1.6.4] - 2023-03-04

### Added

- Added `pid` option for a session (optional).

### Changed

- Merge session `reference` to `pid`.
- Python standards enforcement `None`.
- If `None` (default), `pid` is a random md5.

### Fixed

- Fixed bad table key for cached keys.

## [1.6.3] - 2023-03-04

### Fixed

- Fixed setup.py

## [1.6.2] - 2023-03-04

### Added

- Added StreamFab loadbalancer.

### Changed

- New compiler version of the Mod Key function.
- Removal of unused code.
- Merge Random Bytes from `Crypto` to `Cryptodome`.

### Fixed

- Fix cached keys url error for multi-region service.

## [1.6.1] - 2023-03-02

### Added

- Added new cached key support.
- Added support for unencrypted responses.

### Changed

- Preparing DLL implementation.
- Removing unused exceptions.
- Update C code to display in uppercase.

### Fixed

- Fix adding a service certificate.
- Fix missing .so lib.

## [1.6.0] - 2023-03-01

### Added

- Added full support for Python 3.11.
- Added full support Android API.
- Added ModKey decryption system.
- Added full support cached keys.
- Added PSSH lib.

### Changed

- Windows API update.
- Updated decryption method.
- Global Operation Upgrade.

## [1.4.2] - 2023-03-01

Initial Release.

[1.6.7]: https://github.com/hyugogirubato/pydvdfab/releases/tag/v1.6.7
[1.6.6]: https://github.com/hyugogirubato/pydvdfab/releases/tag/v1.6.6
[1.6.5]: https://github.com/hyugogirubato/pydvdfab/releases/tag/v1.6.5
[1.6.4]: https://github.com/hyugogirubato/pydvdfab/releases/tag/v1.6.4
[1.6.3]: https://github.com/hyugogirubato/pydvdfab/releases/tag/v1.6.3
[1.6.2]: https://github.com/hyugogirubato/pydvdfab/releases/tag/v1.6.2
[1.6.1]: https://github.com/hyugogirubato/pydvdfab/releases/tag/v1.6.1
[1.6.0]: https://github.com/hyugogirubato/pydvdfab/releases/tag/v1.6.0
[1.4.2]: https://github.com/hyugogirubato/pydvdfab/releases/tag/v1.4.2

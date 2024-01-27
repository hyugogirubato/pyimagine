# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.3.8] - 2024-01-27

### Changed

- Using the [Aiby](https://aiby.com/) API.
- Updating constants.
- Removing custom exceptions.

## Added

- Updated `aiby.py` according to the new requests parameters.

## [2.7.5] - 2023-06-25

### Fixed

- Fix `README`.

## [2.7.4] - 2023-06-25

### Added

- Identifying new endpoints.
- `BannedContent` exception for content that does not respect the guidelines.
- Detection of a negative image response.

### Fixed

- Requests parameter.
- `strength` variable type.

### Changed

- Updating constants.
- Updated `test.py` according to the new requests parameters.

## [2.7.3] - 2023-06-11

### Fixed

- Headers parameter.

### Changed

- Updating constants.

## [2.7.2] - 2023-06-09

### Changed

- Updating constants.
- Updating `README`.

## [2.7.1] - 2023-06-07

### Added

- `InvalidSize` exception for size difference between two images.

### Fixed

- Add missing params to the `sdimg` method.

### Changed

- `inspire` method renamed to `sdinsp`.
- Updating constants.

## [2.7.0] - 2023-06-06

### Added

- Optional word restriction.
- Face correction.
- Detect prompt errors before execution.
- Added inspiration.
- Request timeout (60s).

### Fixed

- `PNG` image output format.
- Body generation for `POST` requests.

### Changed

- Code optimization.
- Updating constants.

## [2.6.4] - 2023-05-26

### Added

- Initial release.

[3.3.8]: https://github.com/hyugogirubato/pyimagine/releases/tag/v3.3.8
[2.7.5]: https://github.com/hyugogirubato/pyimagine/releases/tag/v2.7.5
[2.7.4]: https://github.com/hyugogirubato/pyimagine/releases/tag/v2.7.4
[2.7.3]: https://github.com/hyugogirubato/pyimagine/releases/tag/v2.7.3
[2.7.2]: https://github.com/hyugogirubato/pyimagine/releases/tag/v2.7.2
[2.7.1]: https://github.com/hyugogirubato/pyimagine/releases/tag/v2.7.1
[2.7.0]: https://github.com/hyugogirubato/pyimagine/releases/tag/v2.7.0
[2.6.4]: https://github.com/hyugogirubato/pyimagine/releases/tag/v2.6.4

# Changelog

All notable changes to the `python-domino` library will be documented in this file.

## [Unreleased]

### Added

### Changed

## 1.0.4

### Added

* `collaborators_remove` method
* Model export and AWS SageMaker API integration

### Changed

* Model version publish method (model_version_publish) doesn't take name anymore
* `collaborators_add` method changed to use v4 API

## 1.0.3

### Added

* Add v4 API endpoint `job_start` to start job with `onDemandSparkCluster` option
* Add v4 API endpoint `job_stop`, `job_status` & `job_start_blocking`

### Changed

* Started caching project_id
* Started using request session instead of creating new session every time
* Check if an App is running before attempting to stop it (in `app_unpublish`)

## 1.0.2

### Added

* Added HW tier validation in DominoOperator
* Added ENV Variable `DOMINO_LOG_LEVEL` to set log level

### Changed

* Fixed issue in `run_stop` method
* Better logging in `runs_start_blocking` method
* Added raise for error code (4xx & 5xx)
* Fixed library initialization error in case host url had trailing slash
* Fix app publish issue with domino 4.3

## 1.0.1

### Added

* HW tier functions.
* Airflow DominoOperator support.

### Changed

* Better error handling in `runs_start_blocking`.

## 1.0.0

### Added

* `Domino`/`python-domino` version compatibility matrix.
* Installation instructions for older `python-domino` version.
* `retry` parameter for `runs_start_blocking` method.
* Support for Domino authentication tokens.

### Changed

* Fixed issues in `model_version_publish` method.
* Fixed issues in `app_publish` and `app_unpublish` methods. 
* Fixed issues in `project_create`, `fork_project` and `collaborators_add` methods.
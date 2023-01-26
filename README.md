# Angreal Python Template
---

A template for working on python projects. 

## Usage

```code
$: angreal init https://github.com/angreal/python.git
```

After initialization : 
- setup your remote on github (if you didn't already)
- register it as a remote via `git add remote`
- go to `Settings`->`Pages`, set source to `Github Actions`
- go to `Settings`->`Secrets and variables` and setup 
    - `TEST_PYPI_API_TOKEN`
    - `PYPI_API_TOKEN`

## System Requirements
- Hugo for local doc site

## Features

Github Actions for : 
    - continuous testing
    - doc site publication
    - distribution via pypi




```code
$: angreal --help

angreal 2.0.0

USAGE:
    angreal [OPTIONS] <SUBCOMMAND>

OPTIONS:
    -h, --help       Print help information
    -v, --verbose    verbose level, (may be used multiple times for more verbosity)
    -V, --version    Print version information

SUBCOMMANDS:
    build-docs         build our doc site
    clean              cleans out generated cruft
    dev-setup          setup a development environment
    dist               build your project for distribution
    help               Print this message or the help of the given subcommand(s)
    init               Initialize an Angreal template from source.
    run-tests          run our test suite. default is unit tests only
    static-analysis    run our static analysis
```
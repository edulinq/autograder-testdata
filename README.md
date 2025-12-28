# Autograder Test Data

Test data for [EduLinq's Lynx Grader](https://github.com/edulinq/autograder-server).

The full data generation is as follows:
 - [github.com/edulinq/autograder-server](https://github.com/edulinq/autograder-server) holds the core test data (made available with the `--unit-testing` flag).
 - [github.com/edulinq/autograder-server](https://github.com/edulinq/autograder-server) builds Docker images to run the autograder server.
 - [github.com/edulinq/autograder-py](https://github.com/edulinq/autograder-py) provides the Python interface and test cases (as functions).
 - [github.com/edulinq/python-utils](https://github.com/edulinq/python-utils) provides tools for running tests, storing HTTP exchanges, and creating mock HTTP servers.
 - [This repo](https://github.com/edulinq/autograder-testdata)
   starts a server using the Docker images from [edulinq/autograder-server](https://github.com/edulinq/autograder-server),
   runs the tests from [edulinq/autograder-py](https://github.com/edulinq/autograder-py),
   and saves the HTTP exchanges using [edulinq/python-utils](https://github.com/edulinq/python-utils).

## Cloning

This repository includes submodules used for testing/development/generation.
If you only need the data, you can clone normally (and skip the submodules).

To fetch these submodules on clone, add the `--recurse-submodules` flag.
For example:
```sh
git clone --recurse-submodules git@github.com:edulinq/autograder-testdata.git
```

To fetch the submodules after cloning, you can use:
```sh
git submodule update --init --recursive
```

## Usage

There are two flavors of scripts used to interact with the test data: docker and local.
Both versions will use the [autograder-server](./autograder-server) submodule to figure out the default server version to use.

The "docker" variant uses a Docker container to run an autograder server.
By default, the [ghcr.io/edulinq/autograder-server (prebuilt)](https://github.com/edulinq/autograder-server/pkgs/container/autograder-server) image is used.
The `--image-name` flag can be used to choose alternate (even local) images.

The "local" variant uses a specified source directory to build and run a local autograder server.
By default, these scripts will use the autograder-server submodule built into this repo.
The `--source-dir` flag can be used to choose an alternate path.
During execution, the scripts will go into the source dir and run `go run cmd/server/main.go --unit-testing`.

### Generating Test HTTP Data

To generate test HTTP data (for use in a [mock HTTP server](https://github.com/edulinq/python-utils/blob/main/edq/testing/httpserver.py)),
you can use the `scripts/*-generate-test-data.py` scripts:
```sh
# Use a pre-made Docker image.
./scripts/docker-generate-test-data.py

# Use the autograder-server submodule.
./scripts/local-generate-test-data.py ../autograder-server
```

This will generate test HTTP exchanges in the [testdata/http](testdata/http) directory.

Use `--help` to see other available options (such as output directory).

### Verifying Test HTTP Data

To verify that test data matches the output of a server image,
you can use the `scripts/*-verify-test-data.py` scripts:
```sh
# Use a pre-made Docker image.
./scripts/docker-verify-test-data.py

# Use the autograder-server submodule.
./scripts/local-verify-test-data.py ../autograder-server
```

This will verify that the test HTTP exchanges in the [testdata/http](testdata/http) directory
get the same response from your server image.

This verification step is also done as part of CI.

Use `--help` to see other available options (such as the test data directory).

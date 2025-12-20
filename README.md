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

## Usage

### Generating Test HTTP Data

To generate test HTTP data (for use in a [mock HTTP server](https://github.com/edulinq/python-utils/blob/main/edq/testing/httpserver.py)),
you can use the [scripts/generate-test-data.py](scripts/generate-test-data.py) script:
```sh
./scripts/generate-test-data.py
```

This will generate test HTTP exchanges in the [testdata/http](testdata/http) directory.

Use `--help` to see other available options (such as output directory).

### Verifying Test HTTP Data

To verify that test data matches the output of a server image,
you can use the [scripts/verify-test-data.py](scripts/verify-test-data.py) script:
```sh
./scripts/verify-test-data.py
```

This will verify that the test HTTP exchanges in the [testdata/http](testdata/http) directory
get the same response from your server image.

This verification step is also done as part of CI.

Use `--help` to see other available options (such as the test data directory).

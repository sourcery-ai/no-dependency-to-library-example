# README

This is an example project to show how to flag dependencies to a library using Sourcery custom rules.

In this example, we'll flag any dependency to the library `requests`.

## Prereuqisites

In order for this example to work, you need:

* The [sourcery-cli](https://pypi.org/project/sourcery-cli/) package from PyPI. Min. version: 0.12.6 (Released on 2022-07-30.)
* A Sourcery token with a team subscription.
  
After installing Sourcery CLI, first you'll need to log in using the `login` command.

```
sourcery login --token YOUR_TOKEN
```

This step is necessary only once per installation.

## Configuration

Currently, 4 custom rules are necessary for flagging various ways of dependencies to a library.  
You can find these in `rules/no-dependency-requests.yaml`

If you use [isort](https://pycqa.github.io/isort/), you don't have `import` statements importing multiple packages.  
=>  
You can omit the 3rd and 4th rules.

## Usage

```
sourcery review \
--config-path rules/no-dependency-requests.yaml \
--include no-dependency-requests-import \
--include no-dependency-requests-from \
--include no-dependency-requests-import-after-others \
--include no-dependency-requests-import-before-others \
code
```

To get the output in csv format and redirect it to a file:

```
sourcery review \
--config-path rules/no-dependency-requests.yaml \
--include no-dependency-requests-import \
--include no-dependency-requests-from \
--include no-dependency-requests-import-after-others \
--include no-dependency-requests-import-before-others \
--csv \
code \
> ~/sourcery_review_example_output.csv
```

### Options Used

* `--config-path`: The path of the yaml file containing the rules. If not provided, `.sourcery.yaml` in the current directory is used.
* `--include`: The IDs of the rules that Sourcery should apply. If not provided, Sourcery will check for all (ca. 110) Sourcery core rules. This will make the review significantly slower.

## Out of Scope Currently

These rules won't detect a dependency via:

* `__import__` built-in function
* `importlib`
* the edge case, where multiple packages are imported in 1 `import` statement and one of them is a subpackage of `requests`. E.g. `import json, requests.auth` (This edge case can't occur if your imports adhere to [isort](https://pycqa.github.io/isort/)'s standards.)

## Roadmap: Coming Soon

* Detect the edge case, where multiple packages are imported in 1 line and one of them is a subpackage of `requests` (see above)
* Express `no-dependency` with 1 rule instead of 4.
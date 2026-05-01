# Copy Pasta

Basic Python template using copier as the engine.


## Usage

### Setup

This project uses `uv` for dependency management.

**Install `uv`**:
Follow the instructions at [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/).
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Create a new repo

To create a new repo:

Navigate to the directory you keep your projects in (e.g. `~/repos/`) then run the following command. 
```bash
uvx run copier copy gh:msharp9/copy-pasta $REPO_NAME
```
Update `$REPO_NAME`. Follow the prompts, answering questions to be used when filling out the template

### Migrate to Copy Pasta

Navigate to a current python project and run:
```bash
uvx run copier copy gh:msharp9/copy-pasta .
```
You will be prompted to ignore or replace any conflicting files.

### Update your project

To update your project to get the latest updates from this template:

```bash
uvx run copier update
```


## Development

### Test your changes

You can test your template locally:
```bash
uv run copier copy . template_copy
```

Or if you push it, you can reference your dev branch name by specifying the --vcs-ref option like so:
```bash
uv run copier copy --vcs-ref $DEV_BRANCH gh:msharp9/copy-pasta path/to/template_copy
```


## Contributing

### Setup Pre-Commit (Optional)

All linting and testing is done in CI, however, if you want to run them locally, you can use prek (preferred) or pre-commit as documented below.

```bash
uvx prek install
```

### Running Tests
Run the test suite using `pytest`. This will also check that code coverage is at least 80%.
```bash
uv run pytest
```

### Linting and Formatting
Check for linting errors using `ruff`:
```bash
uv run ruff check
```

Format code:
```bash
uv run ruff format
```

We have additional linting in this repo to cover the template files.

```bash
uv run j2lint . --ignore S6
uv run yamllint .
```

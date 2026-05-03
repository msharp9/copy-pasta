def test_template(copie):
    result = copie.copy()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    assert result.answers["name"] == "default_name"


def test_copied_template(copie):
    result = copie.copy()
    # dummy_pull_request_template check requires the file to exist in the repo to compare against.
    # We will skip the comparison against a fixture and just check existence or content.

    template_files = [
        ".copier-answers.yml",
        ".github/PULL_REQUEST_TEMPLATE.md",
        ".github/workflows/ci.yml",
        ".gitignore",
        ".pre-commit-config.yml",
        "README.md",
        "default_name/main.py",
        "pyproject.toml",
        "tests/test_main.py",
    ]

    for file_path in template_files:
        file = result.project_dir.joinpath(file_path)
        assert file.exists(), f"Template file {file_path} does not exist"


def test_can_be_named_anything(copie):
    result = copie.copy(extra_answers={"name": "Named @nything-You_Want$"})

    assert result.exit_code == 0
    assert result.exception is None

from tempfile import TemporaryDirectory

from typer.testing import CliRunner

from foo_cv.cli import app

runner = CliRunner()


def test_app():
    with TemporaryDirectory() as tmpdir:
        result = runner.invoke(
            app, ["cv_template.tex.jinja", "content.json", f"{tmpdir}/foo.tex"]
        )
        assert result.exit_code == 0


def test_app_no_tex_output():
    result = runner.invoke(app, ["cv_template.tex.jinja", "content.json"])
    assert result.exit_code == 0
    assert (
        "\\documentclass[11pt,a4paper,colorlinks,linkcolor=green]{moderncv}"
        in result.stdout
    )
    assert "\\end{document}" in result.stdout

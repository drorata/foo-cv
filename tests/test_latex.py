import pytest

from foo_cv import utils


def test_basic():
    input_dict = {
        "foo": {"bar": "some *text*", "bar2": "some more _text_"},
        "another_key": {"some_key": "new text", "list_key": ["*foo*", "bar", "goo"]},
        "key_with_dicts": [{"foo": "bar", "la": "lala"}, {"foo2": "bar2"}],
    }
    expected_dict = {
        "foo": {"bar": "some \\textit{text}", "bar2": "some more \\textit{text}"},
        "another_key": {
            "some_key": "new text",
            "list_key": ["\\textit{foo}", "bar", "goo"],
        },
        "key_with_dicts": [{"foo": "bar", "la": "lala"}, {"foo2": "bar2"}],
    }

    result_dict = utils.latex_render_content(input_dict)
    assert expected_dict == result_dict


def test_non_supported_value_type():
    input_dict = {"foo": "bar", "goo": None}
    with pytest.raises(ValueError):
        utils.latex_render_content(input_dict)


def test_non_supported_tokens():
    with pytest.raises(ValueError):
        utils.render_latex(
            """# Section 1
        # Section 2
        """
        )

    with pytest.raises(ValueError):
        utils.render_latex('![alt text](Isolated.png "Title")')


def test_non_minimal():
    res = utils.render_latex("some text", minimal=False)
    expected = """\\documentclass{article}
\\begin{document}

some text
\\end{document}
"""
    assert res == expected

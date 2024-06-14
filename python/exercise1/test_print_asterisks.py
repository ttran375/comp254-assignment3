import pytest
from .print_asterisks import print_asterisks


@pytest.mark.parametrize(
    "n, expected_output",
    [
        (1, "*\n"),
        (2, "*\n**\n*\n"),
        (3, "*\n**\n***\n**\n*\n"),
        (4, "*\n**\n***\n****\n***\n**\n*\n"),
        (5, "*\n**\n***\n****\n*****\n****\n***\n**\n*\n"),
        (6, "*\n**\n***\n****\n*****\n******\n*****\n****\n***\n**\n*\n"),
        (
            7,
            "*\n**\n***\n****\n*****\n******\n*******\n******\n*****\n****\n***\n**\n*\n",
        ),
        (None, None),
        ("a", None),
        ("1", None),
        ([], None),
        ({}, None),
        ((), None),
        (complex(1, 1), None),
        (b"bytes", None),
        (frozenset([1, 2, 3]), None),
        (bytearray(b"byte array"), None),
        (range(5), None),
        (memoryview(b"memory view"), None),
        (lambda x: x, None),
        (Ellipsis, None),
        (NotImplemented, None),
        (object(), None),
        (dict(a=1), None),
        (set([1, 2, 3]), None),
        ([1, 2, 3], None),
        ([1, 2], None),
        ((1, 2, 3), None),
        ((1, 2), None),
        ("", None),
        ("*", None),
        ("**", None),
        ("***", None),
        ("*****", None),
        ("******", None),
        ("*******", None),
        ("********", None),
        ("*********", None),
        ("**********", None),
        (b"", None),
        (bytearray(), None),
        (None, None),
        ("One", None),
        ("tWo", None),
        ("thRee", None),
        ("fouR", None),
        ("five", None),
        ("six", None),
        ("seven", None),
        ("eight", None),
    ],
)
def test_print_asterisks(capsys, n, expected_output):
    if isinstance(n, int) and n > 0:
        print_asterisks(n)
        captured = capsys.readouterr()
        assert captured.out == expected_output
    else:
        with pytest.raises((TypeError, ValueError)):
            print_asterisks(n)

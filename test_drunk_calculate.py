import sys
from io import StringIO
from drunk_polish_calculator import op_plus, op_minus, op_multiply, op_divide, main


def test_op_plus():
    # given
    x = 1
    y = 1
    expected = 2

    # when
    result = op_plus(1, 1)


def test_op_minus():
    # given
    x = 1
    y = 2
    expected = 1

    # when
    result = op_minus(1, 2)

    # then
    assert result == expected


def test_op_multiply():
    # given
    x = 2
    y = 2
    expected = 4

    # when
    result = op_multiply(2, 2)

    # then
    assert result == expected


def test_op_divide():
    # given
    x = 6
    y = 2
    expected = 3

    # when
    result = op_divide(6, 2)

    # then
    assert result == expected


def test_main(capsys):
    # given
    test_input = '2 2 + 4 5 * / 4 2 -'
    sys.stdin = StringIO(test_input)

    # when

    main()
    captured = capsys.readouterr()
    output = captured.out.strip()

    # then
    assert output == "Expression with space delimiter:5.0"

    sys.stdin = sys.__stdin__

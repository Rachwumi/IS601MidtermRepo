'''My Commands/Plugins Test'''
import pytest
from app import App

def test_app_subtract_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'subtract' command."""
    # Simulate user entering 'subtract' followed by the decimals '12' and '2' then exiting the program 'exit'
    inputs = iter(['subtract', '12', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    captured = capfd.readouterr()#get output
    assert "The value of 12 - 2 is equal to 10" in captured.out

def test_app_divide_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'divide' command."""
    # Simulate user entering 'divide' followed by the decimals '30' and '2' then exiting the program 'exit'
    inputs = iter(['divide', '30', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    captured = capfd.readouterr()
    assert "The value of 30 / 2 is equal to 15" in captured.out

def test_app_multiply_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'multiply' command."""
    # Simulate user entering 'multiply' followed by the decimals '40' and '6' then exiting the program 'exit'
    inputs = iter(['multiply', '40', '6', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    captured = capfd.readouterr()
    assert "The value of 40 * 6 is equal to 240" in captured.out

def test_app_add_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'add' command."""
    # Simulate user entering 'add' followed by the decimals '2' and '2' then exiting the program 'exit'
    inputs = iter(['add', '2', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    captured = capfd.readouterr()
    assert "The value of 2 + 2 is equal to 4" in captured.out

def test_error_app_subtract_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the error 'subtract' command."""
    # Simulate user entering 'subtract' followed by the decimals '12' and '*' then exiting the program 'exit'
    inputs = iter(['subtract', '12', '*', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    captured = capfd.readouterr()
    assert 'Please type in Decimal or Integer format: 2.0, 1.5, 18' in captured.out

def test_error_app_divide_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the error 'divide' command."""
    # Simulate user entering 'divide' followed by the decimals '30' and '/' then exiting the program 'exit'
    inputs = iter(['divide', '30', '/', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    captured = capfd.readouterr()
    assert 'Please type in Decimal or Integer format: 2.0, 1.5, 18' in captured.out

def test_error_app_multiply_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the error 'multiply' command."""
    # Simulate user entering 'multiply' followed by the decimals '40' and 'c' then exiting the program 'exit'
    inputs = iter(['multiply', '40', 'c', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    captured = capfd.readouterr()
    assert 'Please type in Decimal or Integer format: 2.0, 1.5, 18' in captured.out

def test_error_app_add_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the error 'add' command."""
    # Simulate user entering 'add' followed by the decimals 'x' and '2' then exiting the program 'exit'
    inputs = iter(['add', 'x', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    captured = capfd.readouterr()
    assert 'Please type in Decimal or Integer format: 2.0, 1.5, 18' in captured.out

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    captured = capfd.readouterr()
    assert "Here is the Menu of available commands: add, divide, exit, menu, multiply, subtract" in captured.out

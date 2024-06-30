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

def test_app_display_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'display' command."""
    # Simulate user entering 'add' followed by the decimals '2' and '2', displaying the add calculation, then exiting the program 'exit'
    inputs = iter(['clear', 'add', '2', '2', 'display', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    captured = capfd.readouterr()
    print(captured.out)
    assert "Here is the list of logged calculations: \n0 :  2 2 add" in captured.out

def test_app_displaylast_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'displayLast' command."""
    # Simulate user entering 'add' followed by the decimals '2' and '2', displaying the add calculation, then exiting the program 'exit'
    inputs = iter(['clear', 'add', '2', '2', 'displayLast', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    captured = capfd.readouterr()
    assert "Here is the last calculation that was made: 2, 2, add" in captured.out

def test_app_save_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'save' command."""
    # Simulate user entering 'add' followed by the decimals '2' and '2' then exiting the program 'exit'
    inputs = iter(['clear', 'add', '2', '2', 'save', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    captured = capfd.readouterr()
    assert "Saving 1 calculation(s)." in captured.out

def test_app_load_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'load' command."""
    # Simulate user entering 'load' then exiting the program 'exit'
    inputs = iter(['clear','load', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    captured = capfd.readouterr()
    assert "Loaded 0 previous calculation(s) into the calculator" in captured.out

def test_app_delete_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'add' command."""
    # Simulate user entering 'add' followed by the decimals '2' and '2', and deleting the first record in the list, then exiting the program 'exit'
    inputs = iter(['add', '2', '2', 'delete', '0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    captured = capfd.readouterr()
    assert "History record was deleted" in captured.out

def test_app_clear_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'clear' command."""
    # Simulate user entering 'clear' then exiting the program 'exit'
    inputs = iter(['clear', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    captured = capfd.readouterr()
    assert "Calculation history and database were cleared" in captured.out

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
    assert "Here is the Menu of available commands: add, clear, delete, display, displayLast, divide, exit, load, menu, multiply, save, subtract" in captured.out

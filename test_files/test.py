def test_function():
    print("test message")
    test_var = 42
    return test_var

if __name__ == "__main__":
    result = test_function()
    print(result)
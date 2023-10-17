def outer_function(text):
    text = text
    def inner_function():
        print(text)
    inner_function()
if __name__ == "__main__":
    outer_function("Hey !")
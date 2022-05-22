from rich.traceback import install
install(show_locals=True)
data = [
    {
        "person": {
            "friends": [
                {"name": "Sally",
                "age": 32},
                {"name": "Yuri",
                "age": 43}
            ],
            "location": "Warsaw, Poland"
        }
    }
]

print(data[0]["person"]["friends"][2]["name"])
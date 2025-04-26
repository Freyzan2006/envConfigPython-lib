# test.py

# python3.12 tests/test_basic.py

from env_config_lib import EnvConfig 

def main():
    env = EnvConfig(
        schema = {
            "TEST": str,
            "TEST2": int,
            "TEST3": float,
            "TEST4": bool,
            "TEST5": list,
            "TEST6": tuple,
            "TEST7": dict,
            "TEST8": set,
        },
        path = "tests/.env"
    )

    print(env.get("TEST2"))




if __name__ == "__main__":
    main()


from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class BunTestData:
    NAME_CASES = [
        (("black bun", 100), "black bun"),
        (("white bun", 200.50), "white bun"),
        (("red bun", 0), "red bun"),
        (("", 300), ""),
        (("a" * 100, 999.99), "a" * 100)
    ]
    PRICE_CASES = [
        (("black bun", 100), 100),
        (("white bun", 200.50), 200.50),
        (("red bun", 0), 0),
        (("special bun", 999.99), 999.99)
    ]
    INVALID_CASES = [
        (None, 100),
        (123, 100),
        ("black bun", "100"),
        ("black bun", None)
    ]


class IngredientTestData:
    COMMON_CASES = [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_FILLING, "cutlet", 200.50),
        (INGREDIENT_TYPE_SAUCE, "", 0),
        (INGREDIENT_TYPE_FILLING, "a" * 100, 999.99),
        (INGREDIENT_TYPE_SAUCE, "sour cream", -1),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 999.99),
        (INGREDIENT_TYPE_FILLING, "sausage", -5)
    ]
    INVALID_CASES = [
        (None, "hot sauce", 100),
        (123, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, None, 100),
        (INGREDIENT_TYPE_SAUCE, 123, 100),
        (INGREDIENT_TYPE_SAUCE, "hot sauce", "100")
    ]


class BurgerTestData:
    BURGERS_PRICE_DATA = [
        (100.10, [], 200.20),
        (250.55, [50.00], 551.10),
        (200, [500, 1500, 500, 150, 250], 3300)
    ]
    NONE_PARAMETERS_ACCEPT_CASES = [
        ("set_buns", [None], "bun_is_none", False),
        ("add_ingredient", [None], "last_ingredient_is_none", False),
    ]
    NONE_PARAMETERS_ERROR_CASES = [
        ("remove_ingredient", [None], (TypeError, IndexError), False),
        ("move_ingredient", [None, 0], (TypeError, IndexError), True),
        ("move_ingredient", [0, None], (TypeError, IndexError), True),
    ]


class ReceiptData:
    EXP_ONLY_BUN = (
        "(==== White ====)\n"
        "(==== White ====)\n\n"
        "Price: 400"
    )
    EXP_DIFF_INGREDS = (
        "(==== White ====)\n"
        "= filling dinosaur =\n"
        "= sauce hot sauce =\n"
        "(==== White ====)\n\n"
        "Price: 700"
    )
    EXP_SAME_INGREDS = (
        "(==== White ====)\n"
        "= filling dinosaur =\n"
        "= filling dinosaur =\n"
        "= sauce hot sauce =\n"
        "(==== White ====)\n\n"
        "Price: 900"
    )
    EXP_EMPTY_NAME = (
        "(====  ====)\n"
        "=   =\n"
        "(====  ====)\n\n"
        "Price: 600"
    )


class DatabaseData:
    DATABASE_BUNS = [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ]
    DATABASE_INGREDS = [
        (0, 'SAUCE', "hot sauce", 100),
        (1, 'SAUCE', "sour cream", 200),
        (2, 'SAUCE', "chili sauce", 300),
        (3, 'FILLING', "cutlet", 100),
        (4, 'FILLING', "dinosaur", 200),
        (5, 'FILLING', "sausage", 300)
    ]

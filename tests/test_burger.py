import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from data import BurgerTestData, IngredientTestData, ReceiptData


class InvalidIngredient:
    pass


def _assert_bun_is_none(burger):
    assert burger.bun is None, "Bun should be None after set_buns(None)"


def _assert_last_ingredient_is_none(burger):
    assert burger.ingredients[-1] is None, "Last ingredient should be None"


POST_CHECKS = {
    "bun_is_none": _assert_bun_is_none,
    "last_ingredient_is_none": _assert_last_ingredient_is_none,
}


class TestBurger:

    def test_bun_should_be_none_by_default(self):
        burger = Burger()
        assert burger.bun == None

    def test_ingredients_should_be_empty_list_by_default(self):
        burger = Burger()
        assert burger.ingredients == []

    def test_set_buns_updates_bun_correctly(self, mock_bun, burger_fixture):
        name = mock_bun.name
        burger_fixture.set_buns(mock_bun)
        assert burger_fixture.bun.name == name

    def test_add_ingredient_appends_to_ingredients_list(self, mock_ingredient_filling, burger_fixture):
        burger_fixture.add_ingredient(mock_ingredient_filling)
        assert burger_fixture.ingredients[0].name == mock_ingredient_filling.name

    def test_add_ingredient_multiple_same_correctly(self, mock_ingredient_filling, burger_fixture):
        for _ in range(5):
            burger_fixture.add_ingredient(mock_ingredient_filling)
        assert len(burger_fixture.ingredients) == 5 and \
            all(ingredient == mock_ingredient_filling for ingredient in burger_fixture.ingredients), \
            (f"Количество ингредиентов: {len(burger_fixture.ingredients)}/5, "
                f"Совпадение с mock-объектом: {all(ingredient == mock_ingredient_filling for ingredient in burger_fixture.ingredients)}") 
    
    def test_remove_ingredient_decreases_ingredients_count(self, burger_fixture):
        ingredient = IngredientTestData.COMMON_CASES
        burger_fixture.add_ingredient(ingredient[0])
        burger_fixture.add_ingredient(ingredient[1])
        burger_fixture.remove_ingredient(0)
        assert len(burger_fixture.ingredients) == 1 and burger_fixture.ingredients[0] == ingredient[1]

    def test_move_ingredient_changes_positions_correctly(self, burger_fixture):
        ingredient = IngredientTestData.COMMON_CASES
        burger_fixture.add_ingredient(ingredient[0])
        burger_fixture.add_ingredient(ingredient[1])
        burger_fixture.move_ingredient(0, 1)
        assert burger_fixture.ingredients[0] == ingredient[1] and burger_fixture.ingredients[1] == ingredient[0]

    @pytest.mark.parametrize('bun_price, ingredients_prices, expected_price', BurgerTestData.BURGERS_PRICE_DATA)
    def test_get_price_with_multiple_ingredients_correctly(
        self, mock_bun, burger_fixture, bun_price, ingredients_prices, expected_price):
        mock_bun.get_price.return_value = bun_price
        burger_fixture.set_buns(mock_bun)
        for price in ingredients_prices:
            mock = Mock()
            mock.get_price.return_value = price
            burger_fixture.add_ingredient(mock)
        assert burger_fixture.get_price() == expected_price

    def test_get_price_with_none_bun(self, mock_ingredient_filling, burger_fixture):
        burger_fixture.add_ingredient(mock_ingredient_filling)
        with pytest.raises(AttributeError):
            burger_fixture.get_price()

    def test_get_receipt_structure_with_only_bun(self, burger_fixture, mock_bun):
        burger_fixture.set_buns(mock_bun)
        assert burger_fixture.get_receipt() == ReceiptData.EXP_ONLY_BUN

    def test_get_receipt_with_ingredients_of_different_type(
            self, burger_fixture, mock_bun, mock_ingredient_filling, mock_ingredient_sauce):
        burger_fixture.set_buns(mock_bun)
        burger_fixture.add_ingredient(mock_ingredient_filling)
        burger_fixture.add_ingredient(mock_ingredient_sauce)
        assert burger_fixture.get_receipt() == ReceiptData.EXP_DIFF_INGREDS

    def test_get_receipt_with_multiple_ingredients_of_same_type(
        self, burger_fixture, mock_bun, mock_ingredient_filling, mock_ingredient_sauce):
        burger_fixture.set_buns(mock_bun)
        burger_fixture.add_ingredient(mock_ingredient_filling)
        burger_fixture.add_ingredient(mock_ingredient_filling)
        burger_fixture.add_ingredient(mock_ingredient_sauce)
        assert burger_fixture.get_receipt() == ReceiptData.EXP_SAME_INGREDS
        
    def test_get_receipt_with_empty_ingredient_name(self, burger_fixture, mock_bun, mock_ingredient_filling):
        mock_ingredient_filling.get_type.return_value = ""
        mock_ingredient_filling.get_name.return_value = ""
        mock_bun.get_name.return_value = ""
        burger_fixture.set_buns(mock_bun)
        burger_fixture.add_ingredient(mock_ingredient_filling)
        assert burger_fixture.get_receipt() == ReceiptData.EXP_EMPTY_NAME

    def test_get_price_with_none_bun(self, mock_ingredient_filling, burger_fixture):
        burger_fixture.add_ingredient(mock_ingredient_filling)
        with pytest.raises(AttributeError):
            burger_fixture.get_price()

    def test_get_receipt_with_no_bun_raises_error(self, burger_fixture, mock_ingredient_filling):
        burger_fixture.add_ingredient(mock_ingredient_filling)
        with pytest.raises(AttributeError):
            burger_fixture.get_receipt()

    def test_get_receipt_with_none_ingredient_raises_error(self, burger_fixture, mock_bun):
        burger_fixture.set_buns(mock_bun)
        burger_fixture.ingredients.append(None)  
        with pytest.raises(AttributeError):
            burger_fixture.get_receipt()

    def test_get_receipt_with_invalid_ingredient_type(self, burger_fixture, mock_bun):
        invalid_ingredient = InvalidIngredient()
        burger_fixture.set_buns(mock_bun)
        burger_fixture.add_ingredient(invalid_ingredient)
        with pytest.raises(AttributeError):
            burger_fixture.get_receipt()

    def test_get_receipt_with_long_ingredient_name(self, burger_fixture, mock_bun, mock_ingredient_filling):
        mock_bun.get_name.return_value = "б" * 100
        mock_ingredient_filling.get_type.return_value = "т" * 100
        mock_ingredient_filling.get_name.return_value = "и" * 100
        burger_fixture.set_buns(mock_bun)
        burger_fixture.add_ingredient(mock_ingredient_filling)
        receipt = burger_fixture.get_receipt()
        assert all(x in receipt for x in ("б" * 100, "т" * 100, "и" * 100))


    @pytest.mark.parametrize(
        "method, args, post_check_id, needs_preparation",
        BurgerTestData.NONE_PARAMETERS_ACCEPT_CASES
    )
    def test_none_handling_accepts(
        self,
        burger_fixture,
        burger_with_ingredient,
        method,
        args,
        post_check_id,
        needs_preparation
    ):
        burger = burger_with_ingredient if needs_preparation else burger_fixture
        getattr(burger, method)(*args)
        POST_CHECKS[post_check_id](burger)

    @pytest.mark.parametrize(
        "method, args, expected_exception, needs_preparation",
        BurgerTestData.NONE_PARAMETERS_ERROR_CASES
    )
    def test_none_handling_raises(
        self,
        burger_fixture,
        burger_with_ingredient,
        method,
        args,
        expected_exception,
        needs_preparation
    ):
        burger = burger_with_ingredient if needs_preparation else burger_fixture
        with pytest.raises(expected_exception):
            getattr(burger, method)(*args)

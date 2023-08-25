class TestCategoryModel :
    def test_string_method_output(self, category_factory):
        x = category_factory()
        assert x.__str__() == "test_category"


class TestBrandModel :
    pass


class TestProductModel :
    pass

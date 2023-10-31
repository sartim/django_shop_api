from tests.base import Base


class TestProduct(Base):
    def test_get_all(self):
        r = self.client.get(self.product_url)
        assert r.status_code == 200

    def test_get_by_id(self):
        r = self.client.get('{}1'.format(self.product_url))
        assert r.status_code == 401  # TODO authenticate

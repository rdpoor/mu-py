class TestExample:

    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = lambda:0
        setattr(x, 'check', 'hello')
        assert hasattr(x, 'check')

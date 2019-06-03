
import pytest
import random

class TestRerun:

    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_random_rerun(self):
        assert random.choice([1, 2]) == 2
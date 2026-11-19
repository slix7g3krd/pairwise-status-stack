import pytest
from gameplay import status_stack as mod

CASES = [
    ("refresh", 'm.refresh_stack(2, 2, 4) == 4'),
    ("tick", 'm.tick_once(0.5, 0.5) is True'),
    ("dispel", 'm.dispel_count(5, 1, 2) == 3'),
    ("attr", 'm.dynamic_attr(10, 2, 3) == 16'),
    ("resist", 'm.resist_clear(5, True) == 0'),
    ("death", 'm.death_clear(True, 3) == 0'),
    ("icon", 'm.icon_slot(5, 3) == 2'),
    ("remaining", 'm.remaining_time(5, 2) == 3'),
    ("comp", 'm.tick_compensation(3, 0.5) == approx(1.5)'),
    ("cap", 'm.cap_policy(3, 3, 2) == 3'),
    ("source", 'm.source_filter("boss", ["player"]) is False'),
    ("revive", 'm.revive_snapshot(5, True) is None'),
    ("lock", 'm.concurrency_lock(True) is True'),
    ("damage", 'm.periodic_damage(2, 3, 4) == 24'),
    ("priority", 'm.dispel_priority(2, 2) is True')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})

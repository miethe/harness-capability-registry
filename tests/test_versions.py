from hcr.versions import release_timeline_key, version_key


def test_numeric_components_sort_naturally() -> None:
    assert version_key("2.1.100") > version_key("2.1.99")
    assert version_key("0.147.0") > version_key("0.99.0")


def test_stable_sorts_after_prerelease_with_same_core() -> None:
    assert version_key("1.2.3") > version_key("1.2.3-rc.2")
    assert version_key("1.2.3-rc.2") > version_key("1.2.3-rc.1")


def test_known_dates_sort_ahead_of_dateless_cross_product_entries() -> None:
    dated = {"version": "1.0.0", "published_at": "2026-08-01T00:00:00Z", "harness_id": "a"}
    dateless = {"version": "9.0.0", "published_at": None, "harness_id": "b"}
    assert release_timeline_key(dated) > release_timeline_key(dateless)

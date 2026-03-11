from travel_agent.skills.filesystem import load_skill_bundles


def test_sample_skill_bundle_is_discoverable() -> None:
    bundles = load_skill_bundles()
    names = {bundle.name for bundle in bundles}
    assert "weekend_city_planner" in names


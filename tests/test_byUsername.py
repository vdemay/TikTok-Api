from TikTokApi import TikTokApi
import os

api = TikTokApi.get_instance(
    custom_verifyFp=os.environ.get("verifyFp", None), use_test_endpoints=True
)


def test_trending():
    assert abs(len(api.byUsername("therock", 5)) - 5) <= 2
    assert abs(len(api.byUsername("therock", 10)) - 10) <= 2
    assert abs(len(api.byUsername("therock", 20)) - 20) <= 2

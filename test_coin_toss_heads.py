import coin_toss_heads

def test_coin_toss_1():
    #setup
    expected_result = 1
    expexed_sec_result = 2

    #invoke
    actual_result = coin_toss_heads.coin_toss()

    #analyze
    assert actual_result == expected_result or actual_result == expexed_sec_result
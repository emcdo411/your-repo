from scripts import mini_etl

def test_norm_cat():
    assert mini_etl.norm_cat(' Coffee ') == 'coffee'
    assert mini_etl.norm_cat('Green Tea') == 'green_tea'

def test_parse_date():
    d = mini_etl.parse_date('2025-01-02')
    assert (d.year, d.month, d.day) == (2025, 1, 2)

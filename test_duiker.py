from datetime import datetime as dt
import time

import pytest

import duiker


@pytest.mark.parametrize('size,expected', [
    (1024**0, '1.0 B'),
    (1024**1 / 2, '512.0 B'),
    (1024**1, '1.0 KiB'),
    (1024**2, '1.0 MiB'),
    (1024**3, '1.0 GiB'),
    (1024**4, '1.0 TiB'),
    (1024**5, '1.0 PiB'),
    (1024**6, '1.0 EiB'),
    (1024**7, '1.0 ZiB'),
    (1024**8, '1.0 YiB'),
    (1024**9, '1024.0 YiB'),
])
def test_sizeof_human_binary(size, expected):
    assert duiker.sizeof_human(size) == expected

@pytest.mark.parametrize('size,expected', [
    (1000**0, '1.0 B'),
    (1000**1 / 2, '500.0 B'),
    (1000**1, '1.0 kB'),
    (1000**2, '1.0 MB'),
    (1000**3, '1.0 GB'),
    (1000**4, '1.0 TB'),
    (1000**5, '1.0 PB'),
    (1000**6, '1.0 EB'),
    (1000**7, '1.0 ZB'),
    (1000**8, '1.0 YB'),
    (1000**9, '1000.0 YB'),
])
def test_sizeof_human_decimal(size, expected):
    assert duiker.sizeof_human(size, False) == expected


@pytest.fixture
def millenium():
    from datetime import datetime as dt
    return dt.strptime('2001-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')


@pytest.fixture
def millenium_unix():
    import time
    return time.mktime(millenium().timetuple())


@pytest.mark.parametrize('line,histtimeformat,expected', [
    ('  1  help history', None, duiker.Command(None, None, 'help history')),
    ('100  help history', None, duiker.Command(None, None, 'help history')),
    ('  1  2001-01-01 00:00:00 help history', '%Y-%m-%d %H:%M:%S ', duiker.Command(None, millenium_unix(), 'help history')),
    ('100  2001-01-01 00:00:00 help history', '%Y-%m-%d %H:%M:%S ', duiker.Command(None, millenium_unix(), 'help history')),
    ('  1  2001-01-01 00:00:00 help history', '%Y-%m-%d %H:%M:%S', duiker.Command(None, millenium_unix(), 'help history')),
    ('100  2001-01-01 00:00:00 help history', '%Y-%m-%d %H:%M:%S', duiker.Command(None, millenium_unix(), 'help history')),
])
def test_parse_history_line(line, histtimeformat, expected):
    assert duiker.parse_history_line(line, histtimeformat) == expected


@pytest.mark.parametrize('line,histtimeformat', [
    ('  1  2001-01-01 00:00:00 help history', '%%'),
    ('100  2001-01-01 00:00:00 help history', '%%'),
])
def test_parse_history_line_failure(line, histtimeformat):
    with pytest.raises(ValueError):
        duiker.parse_history_line(line, histtimeformat)
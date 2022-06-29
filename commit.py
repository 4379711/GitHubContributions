import random
from datetime import datetime, timedelta

from git import Repo
from tqdm import tqdm


def make_date(start_str, end_str, _format='%Y-%m-%d %H:%M:%S'):
    _start = datetime.strptime(start_str, _format)
    _end = datetime.strptime(end_str, _format)
    _date_list = []
    while _start < _end:
        _start = _start + timedelta(minutes=random.randint(60, 24 * 60 * 3))
        _start.strftime(_format)
        _date_list.append(_start)
    return _date_list


def git_commit(_git_path: str, _date_list: list):
    with Repo(_git_path) as repo:
        for _time_str in tqdm(_date_list):
            repo.git.commit('--allow-empty', f'--date={_time_str}', '--allow-empty-message', f'-m ', )


if __name__ == '__main__':
    git_path = "C:\\Users\\admin\\Desktop\\GitHubContributions\\.git"
    start = "2016-01-01 00:00:00"
    end = "2022-06-29 00:00:00"
    date_list = make_date(start, end)
    git_commit(git_path, date_list)

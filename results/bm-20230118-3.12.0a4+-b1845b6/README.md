# Results

- fork: brandtbucher
- version: 3.12.0a4+
- commit hash: [b1845b6](https://github.com/brandtbucher/cpython/commit/b1845b6)
- commit date: 2023-01-18T03:01:42-08:00
- commit merge base: [1a9d8c750be83e6abb65769d312361fe9742de02](https://github.com/brandtbucher/cpython/commit/1a9d8c750be83e6abb65769d312361fe9742de02)
- ref: remove_old_branch

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4%2B-b1845b6.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4%2B-b1845b6-vs-3.10.4.md)
- [plot](bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4%2B-b1845b6-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4%2B-b1845b6-vs-3.11.0.md)
- [plot](bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4%2B-b1845b6-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4%2B-b1845b6-vs-base.md)
- [plot](bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4%2B-b1845b6-vs-base.png)


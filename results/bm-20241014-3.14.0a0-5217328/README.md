# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [5217328](https://github.com/python/cpython/commit/5217328)
- commit date: 2024-10-14T08:24:01+00:00
- commit merge base: [4b358ee647809019813f106eb901f466a3846d98](https://github.com/python/cpython/commit/4b358ee647809019813f106eb901f466a3846d98)
- ref: 5217328f93f599755bd7

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11325548685)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328.json)

### vs. 3.10.4

- Geometric mean: 1.13x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328-vs-3.10.4.md)
- [📈time plot](bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328-vs-3.12.0.md)
- [📈time plot](bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, flaskblogging, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328-vs-3.13.0b2.md)
- [📈time plot](bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328-vs-3.13.0b2.svg)


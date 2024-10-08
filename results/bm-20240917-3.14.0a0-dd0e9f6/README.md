# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: 
- commit hash: [dd0e9f6](https://github.com/faster%2dcpython/cpython/commit/dd0e9f6)
- commit date: 2024-09-17T13:59:40+01:00
- commit merge base: [4ed7d1d6acc22807bfb5983c98fd59f7cb5061db](https://github.com/faster%2dcpython/cpython/commit/4ed7d1d6acc22807bfb5983c98fd59f7cb5061db)
- ref: spill_before_escapin

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10903585502)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240917-linux-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-dd0e9f6.json)

### vs. 3.10.4

- Geometric mean: 1.40x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240917-linux-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-dd0e9f6-vs-3.10.4.md)
- [📈time plot](bm-20240917-linux-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-dd0e9f6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240917-linux-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-dd0e9f6-vs-3.12.0.md)
- [📈time plot](bm-20240917-linux-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-dd0e9f6-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240917-linux-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-dd0e9f6-vs-3.13.0b2.md)
- [📈time plot](bm-20240917-linux-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-dd0e9f6-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 92.72%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240917-linux-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-dd0e9f6-vs-base-mem.svg)
- [📄table](bm-20240917-linux-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-dd0e9f6-vs-base.md)
- [📈time plot](bm-20240917-linux-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-dd0e9f6-vs-base.svg)


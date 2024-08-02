# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: 
- commit hash: [f748355](https://github.com/faster%2dcpython/cpython/commit/f748355)
- commit date: 2024-05-31T10:24:08+01:00
- commit merge base: [1f481fd3275dbc12a88c16129621de19ea20e4ca](https://github.com/faster%2dcpython/cpython/commit/1f481fd3275dbc12a88c16129621de19ea20e4ca)
- ref: deferred_rc_overhead

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9315983053)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240531-linux-x86_64-faster%252dcpython-deferred_rc_overhead-3.14.0a0-f748355.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240531-linux-x86_64-faster%252dcpython-deferred_rc_overhead-3.14.0a0-f748355-vs-3.10.4.md)
- [📈time plot](bm-20240531-linux-x86_64-faster%252dcpython-deferred_rc_overhead-3.14.0a0-f748355-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240531-linux-x86_64-faster%252dcpython-deferred_rc_overhead-3.14.0a0-f748355-vs-3.12.0.md)
- [📈time plot](bm-20240531-linux-x86_64-faster%252dcpython-deferred_rc_overhead-3.14.0a0-f748355-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 99.94%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240531-linux-x86_64-faster%252dcpython-deferred_rc_overhead-3.14.0a0-f748355-vs-3.13.0b2.md)
- [📈time plot](bm-20240531-linux-x86_64-faster%252dcpython-deferred_rc_overhead-3.14.0a0-f748355-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 96.72%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240531-linux-x86_64-faster%252dcpython-deferred_rc_overhead-3.14.0a0-f748355-vs-base-mem.svg)
- [📄table](bm-20240531-linux-x86_64-faster%252dcpython-deferred_rc_overhead-3.14.0a0-f748355-vs-base.md)
- [📈time plot](bm-20240531-linux-x86_64-faster%252dcpython-deferred_rc_overhead-3.14.0a0-f748355-vs-base.svg)


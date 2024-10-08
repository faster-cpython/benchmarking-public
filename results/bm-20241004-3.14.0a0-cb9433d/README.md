# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: 
- commit hash: [cb9433d](https://github.com/faster%2dcpython/cpython/commit/cb9433d)
- commit date: 2024-10-04T14:17:43+01:00
- commit merge base: [1f9025a4e7819bb4f7799784710f0f3750a9ca31](https://github.com/faster%2dcpython/cpython/commit/1f9025a4e7819bb4f7799784710f0f3750a9ca31)
- ref: load_fast_can_be_def

## linux x86_64 (azure)

- [pystats raw](bm-20241004-azure-x86_64-faster%252dcpython-load_fast_can_be_def-3.14.0a0-cb9433d-pystats.json)
- [pystats table](bm-20241004-azure-x86_64-faster%252dcpython-load_fast_can_be_def-3.14.0a0-cb9433d-pystats.md)

### vs. base

- [pystats diff](bm-20241004-azure-x86_64-faster%252dcpython-load_fast_can_be_def-3.14.0a0-cb9433d-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11180695877)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241004-linux-x86_64-faster%252dcpython-load_fast_can_be_def-3.14.0a0-cb9433d.json)

### vs. 3.10.4

- Geometric mean: 1.38x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241004-linux-x86_64-faster%252dcpython-load_fast_can_be_def-3.14.0a0-cb9433d-vs-3.10.4.md)
- [📈time plot](bm-20241004-linux-x86_64-faster%252dcpython-load_fast_can_be_def-3.14.0a0-cb9433d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241004-linux-x86_64-faster%252dcpython-load_fast_can_be_def-3.14.0a0-cb9433d-vs-3.12.0.md)
- [📈time plot](bm-20241004-linux-x86_64-faster%252dcpython-load_fast_can_be_def-3.14.0a0-cb9433d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20241004-linux-x86_64-faster%252dcpython-load_fast_can_be_def-3.14.0a0-cb9433d-vs-3.13.0b2.md)
- [📈time plot](bm-20241004-linux-x86_64-faster%252dcpython-load_fast_can_be_def-3.14.0a0-cb9433d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.93%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20241004-linux-x86_64-faster%252dcpython-load_fast_can_be_def-3.14.0a0-cb9433d-vs-base-mem.svg)
- [📄table](bm-20241004-linux-x86_64-faster%252dcpython-load_fast_can_be_def-3.14.0a0-cb9433d-vs-base.md)
- [📈time plot](bm-20241004-linux-x86_64-faster%252dcpython-load_fast_can_be_def-3.14.0a0-cb9433d-vs-base.svg)


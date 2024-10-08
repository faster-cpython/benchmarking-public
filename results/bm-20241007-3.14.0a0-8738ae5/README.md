# Results

- fork: mdboom
- version: 3.14.0a0
- config: 
- commit hash: [8738ae5](https://github.com/mdboom/cpython/commit/8738ae5)
- commit date: 2024-10-07T10:28:25-04:00
- commit merge base: [c8db0e817e7e0db501533fc8bf5b30c18e60aa3d](https://github.com/mdboom/cpython/commit/c8db0e817e7e0db501533fc8bf5b30c18e60aa3d)
- ref: marshal_slice

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11217838857)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5.json)

### vs. 3.10.4

- Geometric mean: 1.38x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5-vs-3.10.4.md)
- [📈time plot](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5-vs-3.12.0.md)
- [📈time plot](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5-vs-3.13.0b2.md)
- [📈time plot](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.78%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5-vs-base-mem.svg)
- [📄table](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5-vs-base.md)
- [📈time plot](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5-vs-base.svg)


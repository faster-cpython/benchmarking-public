# Results

- fork: mdboom
- version: 3.14.0a0
- config: JIT
- commit hash: [0e19ac7](https://github.com/mdboom/cpython/commit/0e19ac7)
- commit date: 2024-10-07T15:01:53-04:00
- commit merge base: [c8db0e817e7e0db501533fc8bf5b30c18e60aa3d](https://github.com/mdboom/cpython/commit/c8db0e817e7e0db501533fc8bf5b30c18e60aa3d)
- ref: marshal_slice

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11222290087)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json)

### vs. 3.10.4

- Geometric mean: 1.36x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.md)
- [📈time plot](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.md)
- [📈time plot](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x slower (HPT: reliability of 83.89%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0.md)
- [📈time plot](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 90.28%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base-mem.svg)
- [📄table](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base.md)
- [📈time plot](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0b2.md)
- [📈time plot](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0b2.svg)


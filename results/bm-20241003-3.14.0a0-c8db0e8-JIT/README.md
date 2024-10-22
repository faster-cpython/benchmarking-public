# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [c8db0e8](https://github.com/python/cpython/commit/c8db0e8)
- commit date: 2024-10-03T21:06:29+01:00
- commit merge base: [7ecaf21946a1da0ede664447839537a7fc5eb64e](https://github.com/python/cpython/commit/7ecaf21946a1da0ede664447839537a7fc5eb64e)
- ref: c8db0e817e7e0db50153

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11222290087)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json)

### vs. 3.10.4

- Geometric mean: 1.36x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.10.4.md)
- [📈time plot](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 99.94%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.12.0.md)
- [📈time plot](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x slower (HPT: reliability of 53.55%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0.md)
- [📈time plot](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.03x slower (HPT: reliability of 93.36%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-base-mem.svg)
- [📄table](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-base.md)
- [📈time plot](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0b2.md)
- [📈time plot](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0b2.svg)


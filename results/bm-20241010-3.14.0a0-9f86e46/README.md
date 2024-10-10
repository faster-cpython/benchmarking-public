# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: 
- commit hash: [9f86e46](https://github.com/faster%2dcpython/cpython/commit/9f86e46)
- commit date: 2024-10-10T14:49:58+01:00
- commit merge base: [99400930ac1d4e5e10a5ae30f8202d8bc2661e39](https://github.com/faster%2dcpython/cpython/commit/99400930ac1d4e5e10a5ae30f8202d8bc2661e39)
- ref: more_robust_immortal

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11275986568)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241010-linux-x86_64-faster%252dcpython-more_robust_immortal-3.14.0a0-9f86e46.json)

### vs. 3.10.4

- Geometric mean: 1.38x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241010-linux-x86_64-faster%252dcpython-more_robust_immortal-3.14.0a0-9f86e46-vs-3.10.4.md)
- [📈time plot](bm-20241010-linux-x86_64-faster%252dcpython-more_robust_immortal-3.14.0a0-9f86e46-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241010-linux-x86_64-faster%252dcpython-more_robust_immortal-3.14.0a0-9f86e46-vs-3.12.0.md)
- [📈time plot](bm-20241010-linux-x86_64-faster%252dcpython-more_robust_immortal-3.14.0a0-9f86e46-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20241010-linux-x86_64-faster%252dcpython-more_robust_immortal-3.14.0a0-9f86e46-vs-3.13.0b2.md)
- [📈time plot](bm-20241010-linux-x86_64-faster%252dcpython-more_robust_immortal-3.14.0a0-9f86e46-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 99.67%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241010-linux-x86_64-faster%252dcpython-more_robust_immortal-3.14.0a0-9f86e46-vs-base-mem.svg)
- [📄table](bm-20241010-linux-x86_64-faster%252dcpython-more_robust_immortal-3.14.0a0-9f86e46-vs-base.md)
- [📈time plot](bm-20241010-linux-x86_64-faster%252dcpython-more_robust_immortal-3.14.0a0-9f86e46-vs-base.svg)


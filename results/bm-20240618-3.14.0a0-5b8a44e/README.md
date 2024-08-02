# Results

- fork: nohlson
- version: 3.14.0a0
- config: 
- commit hash: [5b8a44e](https://github.com/nohlson/cpython/commit/5b8a44e)
- commit date: 2024-06-18T12:49:31-05:00
- commit merge base: [2c66318cdc0545da37e7046533dfe74bde129d91](https://github.com/nohlson/cpython/commit/2c66318cdc0545da37e7046533dfe74bde129d91)
- ref: 1_investigate_compil

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9569909207)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e.json)

### vs. 3.10.4

- Geometric mean: 1.37x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e-vs-3.10.4.md)
- [📈time plot](bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e-vs-3.12.0.md)
- [📈time plot](bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e-vs-3.13.0b2.md)
- [📈time plot](bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e-vs-base-mem.svg)
- [📄table](bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e-vs-base.md)
- [📈time plot](bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e-vs-base.svg)


# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [8ef2e8f](https://github.com/brandtbucher/cpython/commit/8ef2e8f)
- commit date: 2024-10-03T17:05:23-07:00
- commit merge base: [6f4d64b048133c60d40705fb5ef776f78c7dd710](https://github.com/brandtbucher/cpython/commit/6f4d64b048133c60d40705fb5ef776f78c7dd710)
- ref: tier_two_immortals

## linux x86_64 (azure)

- [pystats raw](bm-20241003-azure-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f-pystats.json)
- [pystats table](bm-20241003-azure-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f-pystats.md)

### vs. base

- [pystats diff](bm-20241003-azure-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11171600486)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f.json)

### vs. 3.10.4

- Geometric mean: 1.36x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f-vs-3.10.4.md)
- [📈time plot](bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f-vs-3.12.0.md)
- [📈time plot](bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x slower (HPT: reliability of 58.82%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f-vs-3.13.0.md)
- [📈time plot](bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f-vs-base-mem.svg)
- [📄table](bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f-vs-base.md)
- [📈time plot](bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f-vs-3.13.0b2.md)
- [📈time plot](bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f-vs-3.13.0b2.svg)


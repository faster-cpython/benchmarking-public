# Results

- fork: Fidget-Spinner
- version: 3.14.0a0
- config: 
- commit hash: [144a6fa](https://github.com/Fidget%2dSpinner/cpython/commit/144a6fa)
- commit date: 2024-05-11T05:53:21+08:00
- commit merge base: [ec9d12be9648ee60a2eb02d67069d74f8b314df9](https://github.com/Fidget%2dSpinner/cpython/commit/ec9d12be9648ee60a2eb02d67069d74f8b314df9)
- ref: stackref_all

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9037471968)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240511-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-144a6fa.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240511-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-144a6fa-vs-3.10.4.md)
- [📈time plot](bm-20240511-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-144a6fa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x slower (HPT: reliability of 99.95%, 1.00x slower at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240511-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-144a6fa-vs-3.12.0.md)
- [📈time plot](bm-20240511-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-144a6fa-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2
- [📄table](bm-20240511-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-144a6fa-vs-3.13.0b2.md)
- [📈time plot](bm-20240511-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-144a6fa-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240511-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-144a6fa-vs-base-mem.svg)
- [📄table](bm-20240511-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-144a6fa-vs-base.md)
- [📈time plot](bm-20240511-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-144a6fa-vs-base.svg)


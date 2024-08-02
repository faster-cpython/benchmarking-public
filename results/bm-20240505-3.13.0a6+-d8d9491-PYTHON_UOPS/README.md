# Results

- fork: python
- version: 3.13.0a6+
- config: T2
- commit hash: [d8d9491](https://github.com/python/cpython/commit/d8d9491)
- commit date: 2024-05-05T20:57:19+01:00
- commit merge base: [f27f8c790af1233d499b795af1c0d1b36aaecaf5](https://github.com/python/cpython/commit/f27f8c790af1233d499b795af1c0d1b36aaecaf5)
- ref: d8d94911e2393bd30ca5

## linux x86_64 (azure)

- [pystats raw](bm-20240505-azure-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6%2B-d8d9491-pystats.json)
- [pystats table](bm-20240505-azure-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6%2B-d8d9491-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8961182344)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6%2B-d8d9491.json)

### vs. 3.10.4

- Geometric mean: 1.10x faster (HPT: reliability of 99.89%, 1.01x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6%2B-d8d9491-vs-3.10.4.md)
- [📈time plot](bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6%2B-d8d9491-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.16x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6%2B-d8d9491-vs-3.12.0.md)
- [📈time plot](bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6%2B-d8d9491-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.20x slower (HPT: reliability of 100.00%, 1.14x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: bpe_tokeniser, docutils
- [📄table](bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6%2B-d8d9491-vs-3.13.0b2.md)
- [📈time plot](bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6%2B-d8d9491-vs-3.13.0b2.svg)


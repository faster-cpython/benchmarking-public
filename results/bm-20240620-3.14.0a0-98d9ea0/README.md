# Results

- fork: nohlson
- version: 3.14.0a0
- config: 
- commit hash: [98d9ea0](https://github.com/nohlson/cpython/commit/98d9ea0)
- commit date: 2024-06-20T21:40:48-05:00
- commit merge base: [1e4815692f6c8a37a3974d0d7d2025494d026d76](https://github.com/nohlson/cpython/commit/1e4815692f6c8a37a3974d0d7d2025494d026d76)
- ref: enable_no_impact_def

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9613281399)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0.json)

### vs. 3.10.4

- Geometric mean: 1.37x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0-vs-3.10.4.md)
- [📈time plot](bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0-vs-3.12.0.md)
- [📈time plot](bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0-vs-3.13.0b2.md)
- [📈time plot](bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 70.47%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0-vs-base-mem.svg)
- [📄table](bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0-vs-base.md)
- [📈time plot](bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0-vs-base.svg)


# Results

- fork: nick-arm
- version: 3.14.0a0
- config: JIT
- commit hash: [0442576](https://github.com/nick%2darm/cpython/commit/0442576)
- commit date: 2024-10-07T16:19:31+00:00
- commit merge base: [5e9e50612eb27aef8f74a0ccc234e5cfae50c4d7](https://github.com/nick%2darm/cpython/commit/5e9e50612eb27aef8f74a0ccc234e5cfae50c4d7)
- ref: codecache_rwx

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11263691829)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576.json)

### vs. 3.10.4

- Geometric mean: 1.37x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.10.4.md)
- [📈time plot](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 99.97%, 1.01x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.12.0.md)
- [📈time plot](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x faster (HPT: reliability of 99.94%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.13.0b2.md)
- [📈time plot](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 93.02%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-base-mem.svg)
- [📄table](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-base.md)
- [📈time plot](bm-20241007-linux-x86_64-nick%252darm-codecache_rwx-3.14.0a0-0442576-vs-base.svg)


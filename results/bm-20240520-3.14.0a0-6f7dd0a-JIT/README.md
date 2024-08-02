# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [6f7dd0a](https://github.com/python/cpython/commit/6f7dd0a)
- commit date: 2024-05-20T15:32:05+00:00
- commit merge base: [e406b399f9f677cda3d48ed8d7c9d29a173f51f3](https://github.com/python/cpython/commit/e406b399f9f677cda3d48ed8d7c9d29a173f51f3)
- ref: 6f7dd0a4260254390d75

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9192698890)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240520-linux-x86_64-python-6f7dd0a4260254390d75-3.14.0a0-6f7dd0a.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240520-linux-x86_64-python-6f7dd0a4260254390d75-3.14.0a0-6f7dd0a-vs-3.10.4.md)
- [📈time plot](bm-20240520-linux-x86_64-python-6f7dd0a4260254390d75-3.14.0a0-6f7dd0a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 98.07%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240520-linux-x86_64-python-6f7dd0a4260254390d75-3.14.0a0-6f7dd0a-vs-3.12.0.md)
- [📈time plot](bm-20240520-linux-x86_64-python-6f7dd0a4260254390d75-3.14.0a0-6f7dd0a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 56.54%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2
- [📄table](bm-20240520-linux-x86_64-python-6f7dd0a4260254390d75-3.14.0a0-6f7dd0a-vs-3.13.0b2.md)
- [📈time plot](bm-20240520-linux-x86_64-python-6f7dd0a4260254390d75-3.14.0a0-6f7dd0a-vs-3.13.0b2.svg)


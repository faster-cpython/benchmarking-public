# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [a905721](https://github.com/python/cpython/commit/a905721)
- commit date: 2024-06-25T14:35:12-06:00
- commit merge base: [769aea332940f03c3e5b1ad9badd6635c1ac992a](https://github.com/python/cpython/commit/769aea332940f03c3e5b1ad9badd6635c1ac992a)
- ref: a905721b9c5c15279e67

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9680044600)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721.json)

### vs. 3.10.4

- Geometric mean: 1.39x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721-vs-3.10.4.md)
- [📈time plot](bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721-vs-3.12.0.md)
- [📈time plot](bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721-vs-3.13.0b2.md)
- [📈time plot](bm-20240625-linux-x86_64-python-a905721b9c5c15279e67-3.14.0a0-a905721-vs-3.13.0b2.svg)


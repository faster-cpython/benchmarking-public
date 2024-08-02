# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [080259b](https://github.com/brandtbucher/cpython/commit/080259b)
- commit date: 2024-06-20T13:03:05-07:00
- commit merge base: [9f741e55c16376412c1473aa45b94314c00a0c43](https://github.com/brandtbucher/cpython/commit/9f741e55c16376412c1473aa45b94314c00a0c43)
- ref: warmer_side_exits

## linux x86_64 (azure)

- [pystats raw](bm-20240620-azure-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b-pystats.json)
- [pystats table](bm-20240620-azure-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b-pystats.md)

### vs. base

- [pystats diff](bm-20240620-azure-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9603665513)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b.json)

### vs. 3.10.4

- Geometric mean: 1.38x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b-vs-3.10.4.md)
- [📈time plot](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 99.84%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b-vs-3.12.0.md)
- [📈time plot](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 99.83%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b-vs-3.13.0b2.md)
- [📈time plot](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.02x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b-vs-base-mem.svg)
- [📄table](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b-vs-base.md)
- [📈time plot](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b-vs-base.svg)


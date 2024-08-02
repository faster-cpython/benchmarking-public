# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [7bff512](https://github.com/brandtbucher/cpython/commit/7bff512)
- commit date: 2024-06-20T16:10:40-07:00
- commit merge base: [9f741e55c16376412c1473aa45b94314c00a0c43](https://github.com/brandtbucher/cpython/commit/9f741e55c16376412c1473aa45b94314c00a0c43)
- ref: jump_to_top

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9608500458)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512.json)

### vs. 3.10.4

- Geometric mean: 1.38x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, djangocms, docutils, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512-vs-3.10.4.md)
- [📈time plot](bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, docutils, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512-vs-3.12.0.md)
- [📈time plot](bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 99.81%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, djangocms, docutils, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512-vs-3.13.0b2.md)
- [📈time plot](bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 87.81%, 1.00x slower at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: 🔴 docutils
- [🧠memory plot](bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512-vs-base-mem.svg)
- [📄table](bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512-vs-base.md)
- [📈time plot](bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512-vs-base.svg)


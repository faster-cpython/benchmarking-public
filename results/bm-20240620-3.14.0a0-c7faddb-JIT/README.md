# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [c7faddb](https://github.com/brandtbucher/cpython/commit/c7faddb)
- commit date: 2024-06-20T17:00:54-07:00
- commit merge base: [9f741e55c16376412c1473aa45b94314c00a0c43](https://github.com/brandtbucher/cpython/commit/9f741e55c16376412c1473aa45b94314c00a0c43)
- ref: warmer_side_exits

## linux x86_64 (azure)

- [pystats raw](bm-20240620-azure-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb-pystats.json)
- [pystats table](bm-20240620-azure-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb-pystats.md)

### vs. base

- [pystats diff](bm-20240620-azure-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9608497895)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb.json)

### vs. 3.10.4

- Geometric mean: 1.37x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb-vs-3.10.4.md)
- [📈time plot](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb-vs-3.12.0.md)
- [📈time plot](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 99.51%, 1.00x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb-vs-3.13.0b2.md)
- [📈time plot](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.94%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb-vs-base-mem.svg)
- [📄table](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb-vs-base.md)
- [📈time plot](bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb-vs-base.svg)


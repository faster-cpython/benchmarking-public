# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [ebcfcaf](https://github.com/brandtbucher/cpython/commit/ebcfcaf)
- commit date: 2024-10-14T17:42:31-07:00
- commit merge base: [3fea1d000ef0a74062fd3fe218ad94618b08d9f2](https://github.com/brandtbucher/cpython/commit/3fea1d000ef0a74062fd3fe218ad94618b08d9f2)
- ref: reset_counters

## linux x86_64 (azure)

- [pystats raw](bm-20241014-azure-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf-pystats.json)
- [pystats table](bm-20241014-azure-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf-pystats.md)

### vs. base

- [pystats diff](bm-20241014-azure-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11353478967)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser
- [📄table](bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf-vs-3.10.4.md)
- [📈time plot](bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 99.66%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf-vs-3.12.0.md)
- [📈time plot](bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 99.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf-vs-3.13.0b2.md)
- [📈time plot](bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 99.10%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf-vs-base-mem.svg)
- [📄table](bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf-vs-base.md)
- [📈time plot](bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf-vs-base.svg)


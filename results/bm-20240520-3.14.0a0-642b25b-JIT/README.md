# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [642b25b](https://github.com/python/cpython/commit/642b25b)
- commit date: 2024-05-20T10:58:08-04:00
- commit merge base: [72d07dd30bc10751fe0298915c918eb08e555a7a](https://github.com/python/cpython/commit/72d07dd30bc10751fe0298915c918eb08e555a7a)
- ref: 642b25b9a82c368b0457

## linux x86_64 (azure)

- [pystats raw](bm-20240520-azure-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b-pystats.json)
- [pystats table](bm-20240520-azure-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9165356177)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b-vs-3.10.4.md)
- [📈time plot](bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 96.43%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b-vs-3.12.0.md)
- [📈time plot](bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x faster (HPT: reliability of 93.14%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2
- [📄table](bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b-vs-3.13.0b2.md)
- [📈time plot](bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b-vs-3.13.0b2.svg)


# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [d7c7f4c](https://github.com/brandtbucher/cpython/commit/d7c7f4c)
- commit date: 2024-06-06T13:47:25-07:00
- commit merge base: [e83ce850f433fd8bbf8ff4e8d7649b942639db31](https://github.com/brandtbucher/cpython/commit/e83ce850f433fd8bbf8ff4e8d7649b942639db31)
- ref: call_list_append

## linux x86_64 (azure)

- [pystats raw](bm-20240606-azure-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c-pystats.json)
- [pystats table](bm-20240606-azure-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c-pystats.md)

### vs. base

- [pystats diff](bm-20240606-azure-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9407624996)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c-vs-3.10.4.md)
- [📈time plot](bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 98.61%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c-vs-3.12.0.md)
- [📈time plot](bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x faster (HPT: reliability of 82.24%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c-vs-3.13.0b2.md)
- [📈time plot](bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 99.33%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c-vs-base-mem.svg)
- [📄table](bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c-vs-base.md)
- [📈time plot](bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c-vs-base.svg)


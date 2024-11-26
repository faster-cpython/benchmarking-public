# Results

- fork: brandtbucher
- version: 3.14.0a1+
- config: JIT
- commit hash: [d0d3a27](https://github.com/brandtbucher/cpython/commit/d0d3a27)
- commit date: 2024-10-23T09:19:15-07:00
- commit merge base: [34653bba644aa5481613f398153757d7357e39ea](https://github.com/brandtbucher/cpython/commit/34653bba644aa5481613f398153757d7357e39ea)
- ref: jump_backward_0

## linux x86_64 (azure)

- [pystats raw](bm-20241023-azure-x86_64-brandtbucher-jump_backward_0-3.14.0a1%2B-d0d3a27-pystats.json)
- [pystats table](bm-20241023-azure-x86_64-brandtbucher-jump_backward_0-3.14.0a1%2B-d0d3a27-pystats.md)

### vs. base

- [pystats diff](bm-20241023-azure-x86_64-brandtbucher-jump_backward_0-3.14.0a1%2B-d0d3a27-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11484056518)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1%2B-d0d3a27.json)

### vs. 3.10.4

- Geometric mean: 1.330x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1%2B-d0d3a27-vs-3.10.4.md)
- [📈time plot](bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1%2B-d0d3a27-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.016x faster (HPT: reliability of 89.12%, 1.00x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1%2B-d0d3a27-vs-3.12.0.md)
- [📈time plot](bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1%2B-d0d3a27-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x slower (HPT: reliability of 98.16%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1%2B-d0d3a27-vs-3.13.0.md)
- [📈time plot](bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1%2B-d0d3a27-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.048x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: 🔴 sqlalchemy_declarative, sqlalchemy_imperative
- [🧠memory plot](bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1%2B-d0d3a27-vs-base-mem.svg)
- [📄table](bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1%2B-d0d3a27-vs-base.md)
- [📈time plot](bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1%2B-d0d3a27-vs-base.svg)


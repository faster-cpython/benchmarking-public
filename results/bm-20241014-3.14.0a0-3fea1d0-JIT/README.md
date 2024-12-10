# Results

- fork: python/3fea1d000ef0a74062fd
- version: 3.14.0a0
- config: JIT
- commit hash: [3fea1d0](https://github.com/python/cpython/commit/3fea1d0)
- commit date: 2024-10-14T17:11:58-04:00
- commit merge base: [0c8c665581ede95fe119f902b070e395614b78ed](https://github.com/python/cpython/commit/0c8c665581ede95fe119f902b070e395614b78ed)
- ref: 3fea1d000ef0a74062fd

## linux x86_64 (azure)

- [pystats raw](bm-20241014-azure-x86_64-python-3fea1d000ef0a74062fd-3.14.0a0-3fea1d0-pystats.json)
- [pystats table](bm-20241014-azure-x86_64-python-3fea1d000ef0a74062fd-3.14.0a0-3fea1d0-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11353478967)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241014-linux-x86_64-python-3fea1d000ef0a74062fd-3.14.0a0-3fea1d0.json)

### vs. 3.10.4

- Geometric mean: 1.387x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser
- [📄table](bm-20241014-linux-x86_64-python-3fea1d000ef0a74062fd-3.14.0a0-3fea1d0-vs-3.10.4.md)
- [📈time plot](bm-20241014-linux-x86_64-python-3fea1d000ef0a74062fd-3.14.0a0-3fea1d0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.051x faster (HPT: reliability of 97.81%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241014-linux-x86_64-python-3fea1d000ef0a74062fd-3.14.0a0-3fea1d0-vs-3.12.0.md)
- [📈time plot](bm-20241014-linux-x86_64-python-3fea1d000ef0a74062fd-3.14.0a0-3fea1d0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.021x faster (HPT: reliability of 54.74%, 1.00x slower at 99th %ile)
- Memory usage: 0.96x
- missing benchmarks: async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241014-linux-x86_64-python-3fea1d000ef0a74062fd-3.14.0a0-3fea1d0-vs-3.13.0.md)
- [📈time plot](bm-20241014-linux-x86_64-python-3fea1d000ef0a74062fd-3.14.0a0-3fea1d0-vs-3.13.0.svg)


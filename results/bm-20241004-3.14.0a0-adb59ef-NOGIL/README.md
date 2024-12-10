# Results

- fork: mpage/gh_115999_thread_loc
- version: 3.14.0a0
- config: NOGIL
- commit hash: [adb59ef](https://github.com/mpage/cpython/commit/adb59ef)
- commit date: 2024-10-04T23:54:52-07:00
- commit merge base: [a5fc50994a3fae46d0c3d496c4e1d5e00548a1b8](https://github.com/python/cpython/commit/a5fc50994a3fae46d0c3d496c4e1d5e00548a1b8)
- ref: gh_115999_thread_loc

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11213229021)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef.json)

### vs. 3.10.4

- Geometric mean: 1.017x slower (HPT: reliability of 97.59%, 1.00x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef-vs-3.10.4.md)
- [📈time plot](bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.239x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef-vs-3.12.0.md)
- [📈time plot](bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.281x slower (HPT: reliability of 100.00%, 1.26x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef-vs-3.13.0.md)
- [📈time plot](bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x faster (HPT: reliability of 99.05%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef-vs-base-mem.svg)
- [📄table](bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef-vs-base.md)
- [📈time plot](bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef-vs-base.svg)


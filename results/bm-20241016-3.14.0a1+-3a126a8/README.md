# Results

- fork: colesbury/gh_125610_STORE_ATTR
- version: 3.14.0a1+
- config: 
- commit hash: [3a126a8](https://github.com/colesbury/cpython/commit/3a126a8)
- commit date: 2024-10-16T19:41:13+00:00
- commit merge base: [760872efecb95017db8e38a8eda614bf23d2a22c](https://github.com/python/cpython/commit/760872efecb95017db8e38a8eda614bf23d2a22c)
- ref: gh_125610_STORE_ATTR

## linux x86_64 (azure)

- [pystats raw](bm-20241016-azure-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1%2B-3a126a8-pystats.json)
- [pystats table](bm-20241016-azure-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1%2B-3a126a8-pystats.md)

### vs. base

- [pystats diff](bm-20241016-azure-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1%2B-3a126a8-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11495908985)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1%2B-3a126a8.json)

### vs. 3.10.4

- Geometric mean: 1.417x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1%2B-3a126a8-vs-3.10.4.md)
- [📈time plot](bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1%2B-3a126a8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.072x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1%2B-3a126a8-vs-3.12.0.md)
- [📈time plot](bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1%2B-3a126a8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.018x faster (HPT: reliability of 96.60%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1%2B-3a126a8-vs-3.13.0.md)
- [📈time plot](bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1%2B-3a126a8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 99.93%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1%2B-3a126a8-vs-base-mem.svg)
- [📄table](bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1%2B-3a126a8-vs-base.md)
- [📈time plot](bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1%2B-3a126a8-vs-base.svg)


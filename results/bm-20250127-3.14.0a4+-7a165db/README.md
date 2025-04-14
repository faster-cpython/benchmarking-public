# Results

- fork: eendebakpt/pycfunctionobject_fr
- version: 3.14.0a4+
- config: 
- commit hash: [7a165db](https://github.com/eendebakpt/cpython/commit/7a165db)
- commit date: 2025-01-27T13:35:10+01:00
- commit merge base: [7ec17429d462aee071c067e3b84c8a7e4fcf7263](https://github.com/python/cpython/commit/7ec17429d462aee071c067e3b84c8a7e4fcf7263)
- ref: pycfunctionobject_fr

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12993773120)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4%2B-7a165db.json)

### vs. 3.10.4

- Geometric mean: 1.441x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4%2B-7a165db-vs-3.10.4.md)
- [📈time plot](bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4%2B-7a165db-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.106x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4%2B-7a165db-vs-3.12.0.md)
- [📈time plot](bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4%2B-7a165db-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4%2B-7a165db-vs-3.13.0.md)
- [📈time plot](bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4%2B-7a165db-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 97.49%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4%2B-7a165db-vs-base-mem.svg)
- [📄table](bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4%2B-7a165db-vs-base.md)
- [📈time plot](bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4%2B-7a165db-vs-base.svg)


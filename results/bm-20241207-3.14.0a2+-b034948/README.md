# Results

- fork: eendebakpt/int_freelist
- version: 3.14.0a2+
- config: 
- commit hash: [b034948](https://github.com/eendebakpt/cpython/commit/b034948)
- commit date: 2024-12-07T23:46:05+01:00
- commit merge base: [79b7cab50a3292a1c01466cf0e69fb7b4e56cfb1](https://github.com/python/cpython/commit/79b7cab50a3292a1c01466cf0e69fb7b4e56cfb1)
- ref: int_freelist

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12282170363)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2%2B-b034948.json)

### vs. 3.10.4

- Geometric mean: 1.431x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2%2B-b034948-vs-3.10.4.md)
- [📈time plot](bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2%2B-b034948-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.100x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2%2B-b034948-vs-3.12.0.md)
- [📈time plot](bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2%2B-b034948-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2%2B-b034948-vs-3.13.0.md)
- [📈time plot](bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2%2B-b034948-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.006x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2%2B-b034948-vs-base-mem.svg)
- [📄table](bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2%2B-b034948-vs-base.md)
- [📈time plot](bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2%2B-b034948-vs-base.svg)


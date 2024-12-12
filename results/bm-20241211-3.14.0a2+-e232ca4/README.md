# Results

- fork: eendebakpt/small_int_immortal_v
- version: 3.14.0a2+
- config: 
- commit hash: [e232ca4](https://github.com/eendebakpt/cpython/commit/e232ca4)
- commit date: 2024-12-11T21:21:01+01:00
- commit merge base: [e8f4e272cc828f2b79fa17fc6b9786bdddab7ce4](https://github.com/python/cpython/commit/e8f4e272cc828f2b79fa17fc6b9786bdddab7ce4)
- ref: small_int_immortal_v

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12282375165)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2%2B-e232ca4.json)

### vs. 3.10.4

- Geometric mean: 1.421x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2%2B-e232ca4-vs-3.10.4.md)
- [📈time plot](bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2%2B-e232ca4-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.092x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2%2B-e232ca4-vs-3.12.0.md)
- [📈time plot](bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2%2B-e232ca4-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.028x faster (HPT: reliability of 99.71%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2%2B-e232ca4-vs-3.13.0.md)
- [📈time plot](bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2%2B-e232ca4-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 99.25%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2%2B-e232ca4-vs-base-mem.svg)
- [📄table](bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2%2B-e232ca4-vs-base.md)
- [📈time plot](bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2%2B-e232ca4-vs-base.svg)


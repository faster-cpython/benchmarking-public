# Results

- fork: iritkatriel/cmq_mdboom
- version: 3.14.0a0
- config: 
- commit hash: [6cacd2b](https://github.com/iritkatriel/cpython/commit/6cacd2b)
- commit date: 2024-12-04T21:28:28+00:00
- ref: cmq_mdboom

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12171263939)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b.json)

### vs. 3.10.4

- Geometric mean: 1.418x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, raytrace, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b-vs-3.10.4.md)
- [📈time plot](bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.079x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, raytrace, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b-vs-3.12.0.md)
- [📈time plot](bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.014x faster (HPT: reliability of 97.90%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, raytrace
- [📄table](bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b-vs-3.13.0.md)
- [📈time plot](bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b-vs-3.13.0.svg)


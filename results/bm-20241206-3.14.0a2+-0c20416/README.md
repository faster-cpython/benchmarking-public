# Results

- fork: faster-cpython/use_stackrefs
- version: 3.14.0a2+
- config: 
- commit hash: [0c20416](https://github.com/faster%2dcpython/cpython/commit/0c20416)
- commit date: 2024-12-06T11:19:09+00:00
- commit merge base: [023b7d2141467017abc27de864f3f44677768cb3](https://github.com/python/cpython/commit/023b7d2141467017abc27de864f3f44677768cb3)
- ref: use_stackrefs

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12198100366)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241206-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a2%2B-0c20416.json)

### vs. 3.10.4

- Geometric mean: 1.416x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241206-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a2%2B-0c20416-vs-3.10.4.md)
- [📈time plot](bm-20241206-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a2%2B-0c20416-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.085x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241206-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a2%2B-0c20416-vs-3.12.0.md)
- [📈time plot](bm-20241206-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a2%2B-0c20416-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.019x faster (HPT: reliability of 57.22%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241206-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a2%2B-0c20416-vs-3.13.0.md)
- [📈time plot](bm-20241206-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a2%2B-0c20416-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x slower (HPT: reliability of 99.98%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241206-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a2%2B-0c20416-vs-base-mem.svg)
- [📄table](bm-20241206-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a2%2B-0c20416-vs-base.md)
- [📈time plot](bm-20241206-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a2%2B-0c20416-vs-base.svg)


# Results

- fork: faster-cpython/use_stackrefs
- version: 3.14.0a3+
- config: 
- commit hash: [ad7e1e6](https://github.com/faster%2dcpython/cpython/commit/ad7e1e6)
- commit date: 2024-12-20T17:07:07+00:00
- commit merge base: [128cc47fbd44e3e09c50d9674fe4a4bba3be450c](https://github.com/python/cpython/commit/128cc47fbd44e3e09c50d9674fe4a4bba3be450c)
- ref: use_stackrefs

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12436085426)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241220-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a3%2B-ad7e1e6.json)

### vs. 3.10.4

- Geometric mean: 1.412x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241220-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a3%2B-ad7e1e6-vs-3.10.4.md)
- [📈time plot](bm-20241220-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a3%2B-ad7e1e6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.085x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241220-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a3%2B-ad7e1e6-vs-3.12.0.md)
- [📈time plot](bm-20241220-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a3%2B-ad7e1e6-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.022x faster (HPT: reliability of 98.85%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241220-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a3%2B-ad7e1e6-vs-3.13.0.md)
- [📈time plot](bm-20241220-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a3%2B-ad7e1e6-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.011x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241220-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a3%2B-ad7e1e6-vs-base-mem.svg)
- [📄table](bm-20241220-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a3%2B-ad7e1e6-vs-base.md)
- [📈time plot](bm-20241220-linux-x86_64-faster%252dcpython-use_stackrefs-3.14.0a3%2B-ad7e1e6-vs-base.svg)


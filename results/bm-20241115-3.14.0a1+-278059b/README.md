# Results

- fork: faster-cpython/mark_first_gc
- version: 3.14.0a1+
- config: 
- commit hash: [278059b](https://github.com/faster%2dcpython/cpython/commit/278059b)
- commit date: 2024-11-15T18:27:13+00:00
- commit merge base: [c0f045f7fd3bb7ccf9828f4bfad55347d097fd41](https://github.com/python/cpython/commit/c0f045f7fd3bb7ccf9828f4bfad55347d097fd41)
- ref: mark_first_gc

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11861697962)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241115-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-278059b.json)

### vs. 3.10.4

- Geometric mean: 1.430x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241115-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-278059b-vs-3.10.4.md)
- [📈time plot](bm-20241115-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-278059b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.095x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241115-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-278059b-vs-3.12.0.md)
- [📈time plot](bm-20241115-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-278059b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 96.76%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241115-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-278059b-vs-3.13.0.md)
- [📈time plot](bm-20241115-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-278059b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.034x faster (HPT: reliability of 50.53%, 1.00x slower at 99th %ile)
- Memory usage: 0.97x
- [🧠memory plot](bm-20241115-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-278059b-vs-base-mem.svg)
- [📄table](bm-20241115-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-278059b-vs-base.md)
- [📈time plot](bm-20241115-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-278059b-vs-base.svg)


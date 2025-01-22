# Results

- fork: faster-cpython/no_conditional_stack
- version: 3.14.0a4+
- config: NOGIL
- commit hash: [d5e47ea](https://github.com/faster%2dcpython/cpython/commit/d5e47ea)
- commit date: 2025-01-20T15:53:25+00:00
- commit merge base: [f0f7b978be84c432139da1b107825aa2dc536854](https://github.com/python/cpython/commit/f0f7b978be84c432139da1b107825aa2dc536854)
- ref: no_conditional_stack

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12914042474)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250120-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d5e47ea.json)

### vs. 3.10.4

- Geometric mean: 1.228x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.51x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250120-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d5e47ea-vs-3.10.4.md)
- [📈time plot](bm-20250120-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d5e47ea-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.044x slower (HPT: reliability of 99.99%, 1.03x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250120-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d5e47ea-vs-3.12.0.md)
- [📈time plot](bm-20250120-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d5e47ea-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.105x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250120-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d5e47ea-vs-3.13.0.md)
- [📈time plot](bm-20250120-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d5e47ea-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250120-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d5e47ea-vs-base-mem.svg)
- [📄table](bm-20250120-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d5e47ea-vs-base.md)
- [📈time plot](bm-20250120-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d5e47ea-vs-base.svg)


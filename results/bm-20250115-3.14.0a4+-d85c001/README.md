# Results

- fork: faster-cpython/no_conditional_stack
- version: 3.14.0a4+
- config: 
- commit hash: [d85c001](https://github.com/faster%2dcpython/cpython/commit/d85c001)
- commit date: 2025-01-15T14:01:03+00:00
- commit merge base: [ae7f621c33c854334c69cf97260c7516170dcf0d](https://github.com/python/cpython/commit/ae7f621c33c854334c69cf97260c7516170dcf0d)
- ref: no_conditional_stack

## linux x86_64 (azure)

- [pystats raw](bm-20250115-azure-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d85c001-pystats.json)
- [pystats table](bm-20250115-azure-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d85c001-pystats.md)

### vs. base

- [pystats diff](bm-20250115-azure-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d85c001-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12789933078)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250115-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d85c001.json)

### vs. 3.10.4

- Geometric mean: 1.433x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250115-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d85c001-vs-3.10.4.md)
- [📈time plot](bm-20250115-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d85c001-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.103x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250115-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d85c001-vs-3.12.0.md)
- [📈time plot](bm-20250115-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d85c001-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.036x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250115-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d85c001-vs-3.13.0.md)
- [📈time plot](bm-20250115-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d85c001-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x slower (HPT: reliability of 99.98%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250115-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d85c001-vs-base-mem.svg)
- [📄table](bm-20250115-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d85c001-vs-base.md)
- [📈time plot](bm-20250115-linux-x86_64-faster%252dcpython-no_conditional_stack-3.14.0a4%2B-d85c001-vs-base.svg)


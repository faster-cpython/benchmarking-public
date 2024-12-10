# Results

- fork: brandtbucher/jump_backward_0
- version: 3.14.0a2+
- config: JIT
- commit hash: [29fdc6a](https://github.com/brandtbucher/cpython/commit/29fdc6a)
- commit date: 2024-11-22T12:47:39-08:00
- commit merge base: [615abb99a4538520f380ab26a42f1506e08ffd09](https://github.com/python/cpython/commit/615abb99a4538520f380ab26a42f1506e08ffd09)
- ref: jump_backward_0

## linux x86_64 (azure)

- [pystats raw](bm-20241122-azure-x86_64-brandtbucher-jump_backward_0-3.14.0a2%2B-29fdc6a-pystats.json)
- [pystats table](bm-20241122-azure-x86_64-brandtbucher-jump_backward_0-3.14.0a2%2B-29fdc6a-pystats.md)

### vs. base

- [pystats diff](bm-20241122-azure-x86_64-brandtbucher-jump_backward_0-3.14.0a2%2B-29fdc6a-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11979941156)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2%2B-29fdc6a.json)

### vs. 3.10.4

- Geometric mean: 1.360x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2%2B-29fdc6a-vs-3.10.4.md)
- [📈time plot](bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2%2B-29fdc6a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.035x faster (HPT: reliability of 99.42%, 1.00x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2%2B-29fdc6a-vs-3.12.0.md)
- [📈time plot](bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2%2B-29fdc6a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.020x slower (HPT: reliability of 97.05%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2%2B-29fdc6a-vs-3.13.0.md)
- [📈time plot](bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2%2B-29fdc6a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.034x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2%2B-29fdc6a-vs-base-mem.svg)
- [📄table](bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2%2B-29fdc6a-vs-base.md)
- [📈time plot](bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2%2B-29fdc6a-vs-base.svg)


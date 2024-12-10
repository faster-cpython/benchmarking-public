# Results

- fork: brandtbucher/justin_reserved_fram
- version: 3.14.0a1+
- config: JIT
- commit hash: [735a0ce](https://github.com/brandtbucher/cpython/commit/735a0ce)
- commit date: 2024-11-19T11:51:09-08:00
- commit merge base: [09d6f5dc7824c74672add512619e978844ff8051](https://github.com/python/cpython/commit/09d6f5dc7824c74672add512619e978844ff8051)
- ref: justin_reserved_fram

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11921098331)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1%2B-735a0ce.json)

### vs. 3.10.4

- Geometric mean: 1.387x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1%2B-735a0ce-vs-3.10.4.md)
- [📈time plot](bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1%2B-735a0ce-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.058x faster (HPT: reliability of 99.97%, 1.01x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1%2B-735a0ce-vs-3.12.0.md)
- [📈time plot](bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1%2B-735a0ce-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.004x slower (HPT: reliability of 94.22%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1%2B-735a0ce-vs-3.13.0.md)
- [📈time plot](bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1%2B-735a0ce-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 97.84%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1%2B-735a0ce-vs-base-mem.svg)
- [📄table](bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1%2B-735a0ce-vs-base.md)
- [📈time plot](bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1%2B-735a0ce-vs-base.svg)


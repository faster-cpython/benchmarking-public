# Results

- fork: brandtbucher/warmup_65536
- version: 3.14.0a1+
- config: JIT
- commit hash: [c17f578](https://github.com/brandtbucher/cpython/commit/c17f578)
- commit date: 2024-11-12T19:14:55-08:00
- commit merge base: [09d6f5dc7824c74672add512619e978844ff8051](https://github.com/python/cpython/commit/09d6f5dc7824c74672add512619e978844ff8051)
- ref: warmup_65536

## linux x86_64 (azure)

- [pystats raw](bm-20241112-azure-x86_64-brandtbucher-warmup_65536-3.14.0a1%2B-c17f578-pystats.json)
- [pystats table](bm-20241112-azure-x86_64-brandtbucher-warmup_65536-3.14.0a1%2B-c17f578-pystats.md)

### vs. base

- [pystats diff](bm-20241112-azure-x86_64-brandtbucher-warmup_65536-3.14.0a1%2B-c17f578-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11810339160)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1%2B-c17f578.json)

### vs. 3.10.4

- Geometric mean: 1.398x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1%2B-c17f578-vs-3.10.4.md)
- [📈time plot](bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1%2B-c17f578-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.066x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1%2B-c17f578-vs-3.12.0.md)
- [📈time plot](bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1%2B-c17f578-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.006x faster (HPT: reliability of 50.24%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1%2B-c17f578-vs-3.13.0.md)
- [📈time plot](bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1%2B-c17f578-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x faster (HPT: reliability of 96.25%, 1.00x faster at 99th %ile)
- Memory usage: 0.96x
- missing benchmarks: 🔴 djangocms, many_optionals, subparsers
- [🧠memory plot](bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1%2B-c17f578-vs-base-mem.svg)
- [📄table](bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1%2B-c17f578-vs-base.md)
- [📈time plot](bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1%2B-c17f578-vs-base.svg)


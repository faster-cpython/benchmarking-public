# Results

- fork: brandtbucher
- version: 3.14.0a1+
- config: JIT
- commit hash: [f863657](https://github.com/brandtbucher/cpython/commit/f863657)
- commit date: 2024-11-12T09:41:44-08:00
- commit merge base: [09d6f5dc7824c74672add512619e978844ff8051](https://github.com/brandtbucher/cpython/commit/09d6f5dc7824c74672add512619e978844ff8051)
- ref: warmup_2048

## linux x86_64 (azure)

- [pystats raw](bm-20241112-azure-x86_64-brandtbucher-warmup_2048-3.14.0a1%2B-f863657-pystats.json)
- [pystats table](bm-20241112-azure-x86_64-brandtbucher-warmup_2048-3.14.0a1%2B-f863657-pystats.md)

### vs. base

- [pystats diff](bm-20241112-azure-x86_64-brandtbucher-warmup_2048-3.14.0a1%2B-f863657-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11803047063)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1%2B-f863657.json)

### vs. 3.10.4

- Geometric mean: 1.390x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1%2B-f863657-vs-3.10.4.md)
- [📈time plot](bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1%2B-f863657-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.062x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1%2B-f863657-vs-3.12.0.md)
- [📈time plot](bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1%2B-f863657-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.000x faster (HPT: reliability of 89.05%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, mypy2, tornado_http
- new benchmarks: sqlite_synth
- [📄table](bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1%2B-f863657-vs-3.13.0.md)
- [📈time plot](bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1%2B-f863657-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x faster (HPT: reliability of 99.58%, 1.00x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: 🔴 djangocms, many_optionals, subparsers
- [🧠memory plot](bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1%2B-f863657-vs-base-mem.svg)
- [📄table](bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1%2B-f863657-vs-base.md)
- [📈time plot](bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1%2B-f863657-vs-base.svg)


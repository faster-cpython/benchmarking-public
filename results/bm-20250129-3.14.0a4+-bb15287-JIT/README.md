# Results

- fork: brandtbucher/justin_compact_exits
- version: 3.14.0a4+
- config: JIT
- commit hash: [bb15287](https://github.com/brandtbucher/cpython/commit/bb15287)
- commit date: 2025-01-29T21:32:27-08:00
- commit merge base: [a4722449caccc42ad644611d02fbdb5005f601eb](https://github.com/python/cpython/commit/a4722449caccc42ad644611d02fbdb5005f601eb)
- ref: justin_compact_exits

## linux x86_64 (azure)

- [pystats raw](bm-20250129-azure-x86_64-brandtbucher-justin_compact_exits-3.14.0a4%2B-bb15287-pystats.json)
- [pystats table](bm-20250129-azure-x86_64-brandtbucher-justin_compact_exits-3.14.0a4%2B-bb15287-pystats.md)

### vs. base

- [pystats diff](bm-20250129-azure-x86_64-brandtbucher-justin_compact_exits-3.14.0a4%2B-bb15287-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13046903565)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4%2B-bb15287.json)

### vs. 3.10.4

- Geometric mean: 1.452x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4%2B-bb15287-vs-3.10.4.md)
- [📈time plot](bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4%2B-bb15287-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.120x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4%2B-bb15287-vs-3.12.0.md)
- [📈time plot](bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4%2B-bb15287-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.047x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4%2B-bb15287-vs-3.13.0.md)
- [📈time plot](bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4%2B-bb15287-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.009x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4%2B-bb15287-vs-base-mem.svg)
- [📄table](bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4%2B-bb15287-vs-base.md)
- [📈time plot](bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4%2B-bb15287-vs-base.svg)


# Results

- fork: brandtbucher
- version: 3.14.0a1+
- config: JIT
- commit hash: [48ade84](https://github.com/brandtbucher/cpython/commit/48ade84)
- commit date: 2024-11-08T15:12:05-08:00
- commit merge base: [09d6f5dc7824c74672add512619e978844ff8051](https://github.com/brandtbucher/cpython/commit/09d6f5dc7824c74672add512619e978844ff8051)
- ref: warmup_64

## linux x86_64 (azure)

- [pystats raw](bm-20241108-azure-x86_64-brandtbucher-warmup_64-3.14.0a1%2B-48ade84-pystats.json)
- [pystats table](bm-20241108-azure-x86_64-brandtbucher-warmup_64-3.14.0a1%2B-48ade84-pystats.md)

### vs. base

- [pystats diff](bm-20241108-azure-x86_64-brandtbucher-warmup_64-3.14.0a1%2B-48ade84-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11750909529)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1%2B-48ade84.json)

### vs. 3.10.4

- Geometric mean: 1.384x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1%2B-48ade84-vs-3.10.4.md)
- [📈time plot](bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1%2B-48ade84-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.058x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1%2B-48ade84-vs-3.12.0.md)
- [📈time plot](bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1%2B-48ade84-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.004x slower (HPT: reliability of 79.75%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, gevent_hub, mypy2, tornado_http
- new benchmarks: sqlite_synth
- [📄table](bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1%2B-48ade84-vs-3.13.0.md)
- [📈time plot](bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1%2B-48ade84-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 92.20%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: 🔴 djangocms, many_optionals, subparsers
- [🧠memory plot](bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1%2B-48ade84-vs-base-mem.svg)
- [📄table](bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1%2B-48ade84-vs-base.md)
- [📈time plot](bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1%2B-48ade84-vs-base.svg)


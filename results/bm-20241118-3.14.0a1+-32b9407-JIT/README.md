# Results

- fork: brandtbucher/optimize_off_most
- version: 3.14.0a1+
- config: JIT
- commit hash: [32b9407](https://github.com/brandtbucher/cpython/commit/32b9407)
- commit date: 2024-11-18T08:27:38-08:00
- commit merge base: [2313f8421080ceb3343c6f5d291279adea85e073](https://github.com/python/cpython/commit/2313f8421080ceb3343c6f5d291279adea85e073)
- ref: optimize_off_most

## linux x86_64 (azure)

- [pystats raw](bm-20241118-azure-x86_64-brandtbucher-optimize_off_most-3.14.0a1%2B-32b9407-pystats.json)
- [pystats table](bm-20241118-azure-x86_64-brandtbucher-optimize_off_most-3.14.0a1%2B-32b9407-pystats.md)

### vs. base

- [pystats diff](bm-20241118-azure-x86_64-brandtbucher-optimize_off_most-3.14.0a1%2B-32b9407-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11896755751)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1%2B-32b9407.json)

### vs. 3.10.4

- Geometric mean: 1.299x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1%2B-32b9407-vs-3.10.4.md)
- [📈time plot](bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1%2B-32b9407-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.007x slower (HPT: reliability of 88.57%, 1.00x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1%2B-32b9407-vs-3.12.0.md)
- [📈time plot](bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1%2B-32b9407-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.064x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1%2B-32b9407-vs-3.13.0.md)
- [📈time plot](bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1%2B-32b9407-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.056x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1%2B-32b9407-vs-base-mem.svg)
- [📄table](bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1%2B-32b9407-vs-base.md)
- [📈time plot](bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1%2B-32b9407-vs-base.svg)


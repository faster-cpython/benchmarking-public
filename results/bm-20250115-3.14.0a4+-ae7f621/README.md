# Results

- fork: python/ae7f621c33c854334c69
- version: 3.14.0a4+
- config: 
- commit hash: [ae7f621](https://github.com/python/cpython/commit/ae7f621)
- commit date: 2025-01-15T10:38:43+01:00
- commit merge base: [6e4f64109b0eb6c9f1b50eb7dc5f647a1d901ff4](https://github.com/python/cpython/commit/6e4f64109b0eb6c9f1b50eb7dc5f647a1d901ff4)
- ref: ae7f621c33c854334c69

## linux x86_64 (azure)

- [pystats raw](bm-20250115-azure-x86_64-python-ae7f621c33c854334c69-3.14.0a4%2B-ae7f621-pystats.json)
- [pystats table](bm-20250115-azure-x86_64-python-ae7f621c33c854334c69-3.14.0a4%2B-ae7f621-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12789933078)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4%2B-ae7f621.json)

### vs. 3.10.4

- Geometric mean: 1.446x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4%2B-ae7f621-vs-3.10.4.md)
- [📈time plot](bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4%2B-ae7f621-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.112x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4%2B-ae7f621-vs-3.12.0.md)
- [📈time plot](bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4%2B-ae7f621-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.045x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4%2B-ae7f621-vs-3.13.0.md)
- [📈time plot](bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4%2B-ae7f621-vs-3.13.0.svg)


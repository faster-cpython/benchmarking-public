# Results

- fork: python/1f9025a4e7819bb4f779
- version: 3.14.0a0
- config: 
- commit hash: [1f9025a](https://github.com/python/cpython/commit/1f9025a)
- commit date: 2024-10-03T13:58:56+01:00
- commit merge base: [e6dd71da3acc21edcc205d024d18004c7a3c7f45](https://github.com/python/cpython/commit/e6dd71da3acc21edcc205d024d18004c7a3c7f45)
- ref: 1f9025a4e7819bb4f779

## linux x86_64 (azure)

- [pystats raw](bm-20241003-azure-x86_64-python-1f9025a4e7819bb4f779-3.14.0a0-1f9025a-pystats.json)
- [pystats table](bm-20241003-azure-x86_64-python-1f9025a4e7819bb4f779-3.14.0a0-1f9025a-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12108819708)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241003-linux-x86_64-python-1f9025a4e7819bb4f779-3.14.0a0-1f9025a.json)

### vs. 3.10.4

- Geometric mean: 1.439x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241003-linux-x86_64-python-1f9025a4e7819bb4f779-3.14.0a0-1f9025a-vs-3.10.4.md)
- [📈time plot](bm-20241003-linux-x86_64-python-1f9025a4e7819bb4f779-3.14.0a0-1f9025a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.093x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241003-linux-x86_64-python-1f9025a4e7819bb4f779-3.14.0a0-1f9025a-vs-3.12.0.md)
- [📈time plot](bm-20241003-linux-x86_64-python-1f9025a4e7819bb4f779-3.14.0a0-1f9025a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, gevent_hub, gunicorn
- [📄table](bm-20241003-linux-x86_64-python-1f9025a4e7819bb4f779-3.14.0a0-1f9025a-vs-3.13.0.md)
- [📈time plot](bm-20241003-linux-x86_64-python-1f9025a4e7819bb4f779-3.14.0a0-1f9025a-vs-3.13.0.svg)


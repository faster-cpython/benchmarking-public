# Results

- fork: faster-cpython/remove_most_conditio
- version: 3.14.0a4+
- config: 
- commit hash: [584015a](https://github.com/faster%2dcpython/cpython/commit/584015a)
- commit date: 2025-01-23T14:48:17+00:00
- commit merge base: [a10f99375e7912df863cf101a38e9703cfcd72f1](https://github.com/python/cpython/commit/a10f99375e7912df863cf101a38e9703cfcd72f1)
- ref: remove_most_conditio

## linux x86_64 (azure)

- [pystats raw](bm-20250123-azure-x86_64-faster%252dcpython-remove_most_conditio-3.14.0a4%2B-584015a-pystats.json)
- [pystats table](bm-20250123-azure-x86_64-faster%252dcpython-remove_most_conditio-3.14.0a4%2B-584015a-pystats.md)

### vs. base

- [pystats diff](bm-20250123-azure-x86_64-faster%252dcpython-remove_most_conditio-3.14.0a4%2B-584015a-pystats-vs-base.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12931778503)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250123-pythonperf2-x86_64-faster%252dcpython-remove_most_conditio-3.14.0a4%2B-584015a.json)

### vs. 3.10.4

- Geometric mean: 1.351x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250123-pythonperf2-x86_64-faster%252dcpython-remove_most_conditio-3.14.0a4%2B-584015a-vs-3.10.4.md)
- [📈time plot](bm-20250123-pythonperf2-x86_64-faster%252dcpython-remove_most_conditio-3.14.0a4%2B-584015a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.046x faster (HPT: reliability of 99.85%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250123-pythonperf2-x86_64-faster%252dcpython-remove_most_conditio-3.14.0a4%2B-584015a-vs-3.12.0.md)
- [📈time plot](bm-20250123-pythonperf2-x86_64-faster%252dcpython-remove_most_conditio-3.14.0a4%2B-584015a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.058x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250123-pythonperf2-x86_64-faster%252dcpython-remove_most_conditio-3.14.0a4%2B-584015a-vs-3.13.0.md)
- [📈time plot](bm-20250123-pythonperf2-x86_64-faster%252dcpython-remove_most_conditio-3.14.0a4%2B-584015a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x slower (HPT: reliability of 99.87%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250123-pythonperf2-x86_64-faster%252dcpython-remove_most_conditio-3.14.0a4%2B-584015a-vs-base-mem.svg)
- [📄table](bm-20250123-pythonperf2-x86_64-faster%252dcpython-remove_most_conditio-3.14.0a4%2B-584015a-vs-base.md)
- [📈time plot](bm-20250123-pythonperf2-x86_64-faster%252dcpython-remove_most_conditio-3.14.0a4%2B-584015a-vs-base.svg)


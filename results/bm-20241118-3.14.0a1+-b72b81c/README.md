# Results

- fork: faster-cpython/experiment_save_fram
- version: 3.14.0a1+
- config: 
- commit hash: [b72b81c](https://github.com/faster%2dcpython/cpython/commit/b72b81c)
- commit date: 2024-11-18T12:35:07+00:00
- commit merge base: [c0f045f7fd3bb7ccf9828f4bfad55347d097fd41](https://github.com/python/cpython/commit/c0f045f7fd3bb7ccf9828f4bfad55347d097fd41)
- ref: experiment_save_fram

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11892587711)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241118-linux-x86_64-faster%252dcpython-experiment_save_fram-3.14.0a1%2B-b72b81c.json)

### vs. 3.10.4

- Geometric mean: 1.399x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241118-linux-x86_64-faster%252dcpython-experiment_save_fram-3.14.0a1%2B-b72b81c-vs-3.10.4.md)
- [📈time plot](bm-20241118-linux-x86_64-faster%252dcpython-experiment_save_fram-3.14.0a1%2B-b72b81c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.061x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241118-linux-x86_64-faster%252dcpython-experiment_save_fram-3.14.0a1%2B-b72b81c-vs-3.12.0.md)
- [📈time plot](bm-20241118-linux-x86_64-faster%252dcpython-experiment_save_fram-3.14.0a1%2B-b72b81c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.004x faster (HPT: reliability of 54.32%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241118-linux-x86_64-faster%252dcpython-experiment_save_fram-3.14.0a1%2B-b72b81c-vs-3.13.0.md)
- [📈time plot](bm-20241118-linux-x86_64-faster%252dcpython-experiment_save_fram-3.14.0a1%2B-b72b81c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 86.80%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241118-linux-x86_64-faster%252dcpython-experiment_save_fram-3.14.0a1%2B-b72b81c-vs-base-mem.svg)
- [📄table](bm-20241118-linux-x86_64-faster%252dcpython-experiment_save_fram-3.14.0a1%2B-b72b81c-vs-base.md)
- [📈time plot](bm-20241118-linux-x86_64-faster%252dcpython-experiment_save_fram-3.14.0a1%2B-b72b81c-vs-base.svg)


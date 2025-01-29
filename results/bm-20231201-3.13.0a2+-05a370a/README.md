# Results

- fork: python/05a370abd6cdfe4b54be
- version: 3.13.0a2+
- config: 
- commit hash: [05a370a](https://github.com/python/cpython/commit/05a370a)
- commit date: 2023-12-01T17:05:56+01:00
- commit merge base: [a9073564ee50bc610e1fd36e45b0a5204618883a](https://github.com/python/cpython/commit/a9073564ee50bc610e1fd36e45b0a5204618883a)
- ref: 05a370abd6cdfe4b54be

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13018167663)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2%2B-05a370a.json)

### vs. 3.10.4

- Geometric mean: 1.359x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, djangocms, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2%2B-05a370a-vs-3.10.4.md)
- [📈time plot](bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2%2B-05a370a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.018x faster (HPT: reliability of 99.82%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2%2B-05a370a-vs-3.12.0.md)
- [📈time plot](bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2%2B-05a370a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.050x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: djangocms, gevent_hub
- [📄table](bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2%2B-05a370a-vs-3.13.0.md)
- [📈time plot](bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2%2B-05a370a-vs-3.13.0.svg)


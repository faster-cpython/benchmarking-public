# Results

- fork: Fidget-Spinner/init_slots
- version: 3.14.0a3+
- config: 
- commit hash: [8757207](https://github.com/Fidget%2dSpinner/cpython/commit/8757207)
- commit date: 2024-12-25T23:02:29+08:00
- commit merge base: [d61542b5ff1fe64705e5ce1bcc53048f14098dba](https://github.com/python/cpython/commit/d61542b5ff1fe64705e5ce1bcc53048f14098dba)
- ref: init_slots

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12550391505)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241225-pythonperf2-x86_64-Fidget%252dSpinner-init_slots-3.14.0a3%2B-8757207.json)

### vs. 3.10.4

- Geometric mean: 1.345x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241225-pythonperf2-x86_64-Fidget%252dSpinner-init_slots-3.14.0a3%2B-8757207-vs-3.10.4.md)
- [📈time plot](bm-20241225-pythonperf2-x86_64-Fidget%252dSpinner-init_slots-3.14.0a3%2B-8757207-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.046x faster (HPT: reliability of 99.76%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241225-pythonperf2-x86_64-Fidget%252dSpinner-init_slots-3.14.0a3%2B-8757207-vs-3.12.0.md)
- [📈time plot](bm-20241225-pythonperf2-x86_64-Fidget%252dSpinner-init_slots-3.14.0a3%2B-8757207-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.061x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241225-pythonperf2-x86_64-Fidget%252dSpinner-init_slots-3.14.0a3%2B-8757207-vs-3.13.0.md)
- [📈time plot](bm-20241225-pythonperf2-x86_64-Fidget%252dSpinner-init_slots-3.14.0a3%2B-8757207-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x faster (HPT: reliability of 98.19%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241225-pythonperf2-x86_64-Fidget%252dSpinner-init_slots-3.14.0a3%2B-8757207-vs-base-mem.svg)
- [📄table](bm-20241225-pythonperf2-x86_64-Fidget%252dSpinner-init_slots-3.14.0a3%2B-8757207-vs-base.md)
- [📈time plot](bm-20241225-pythonperf2-x86_64-Fidget%252dSpinner-init_slots-3.14.0a3%2B-8757207-vs-base.svg)


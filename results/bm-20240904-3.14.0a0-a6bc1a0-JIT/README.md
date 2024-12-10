# Results

- fork: Fidget-Spinner/partial_evaluator
- version: 3.14.0a0
- config: JIT
- commit hash: [a6bc1a0](https://github.com/Fidget%2dSpinner/cpython/commit/a6bc1a0)
- commit date: 2024-09-04T03:16:25+08:00
- commit merge base: [91b7f2e7f6593acefda4fa860250dd87d6f849bf](https://github.com/python/cpython/commit/91b7f2e7f6593acefda4fa860250dd87d6f849bf)
- ref: partial_evaluator

## linux x86_64 (azure)

- [pystats raw](bm-20240904-azure-x86_64-Fidget%252dSpinner-partial_evaluator-3.14.0a0-a6bc1a0-pystats.json)
- [pystats table](bm-20240904-azure-x86_64-Fidget%252dSpinner-partial_evaluator-3.14.0a0-a6bc1a0-pystats.md)

### vs. base

- [pystats diff](bm-20240904-azure-x86_64-Fidget%252dSpinner-partial_evaluator-3.14.0a0-a6bc1a0-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10689234746)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240904-linux-x86_64-Fidget%252dSpinner-partial_evaluator-3.14.0a0-a6bc1a0.json)

### vs. 3.10.4

- Geometric mean: 1.429x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240904-linux-x86_64-Fidget%252dSpinner-partial_evaluator-3.14.0a0-a6bc1a0-vs-3.10.4.md)
- [📈time plot](bm-20240904-linux-x86_64-Fidget%252dSpinner-partial_evaluator-3.14.0a0-a6bc1a0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.086x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240904-linux-x86_64-Fidget%252dSpinner-partial_evaluator-3.14.0a0-a6bc1a0-vs-3.12.0.md)
- [📈time plot](bm-20240904-linux-x86_64-Fidget%252dSpinner-partial_evaluator-3.14.0a0-a6bc1a0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.028x faster (HPT: reliability of 74.97%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240904-linux-x86_64-Fidget%252dSpinner-partial_evaluator-3.14.0a0-a6bc1a0-vs-3.13.0.md)
- [📈time plot](bm-20240904-linux-x86_64-Fidget%252dSpinner-partial_evaluator-3.14.0a0-a6bc1a0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 96.85%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240904-linux-x86_64-Fidget%252dSpinner-partial_evaluator-3.14.0a0-a6bc1a0-vs-base-mem.svg)
- [📄table](bm-20240904-linux-x86_64-Fidget%252dSpinner-partial_evaluator-3.14.0a0-a6bc1a0-vs-base.md)
- [📈time plot](bm-20240904-linux-x86_64-Fidget%252dSpinner-partial_evaluator-3.14.0a0-a6bc1a0-vs-base.svg)


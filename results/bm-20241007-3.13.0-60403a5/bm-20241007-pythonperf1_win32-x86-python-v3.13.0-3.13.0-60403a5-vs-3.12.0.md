# Results vs. 3.12.0

- fork: python
- ref: v3.13.0
- machine: windows-x86
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.153x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 250 ms: 1.12x faster                                            |
| chameleon      | 7.75 ms                                                         | 6.08 ms: 1.27x faster                                           |
| docutils       | 1.98 sec                                                        | 1.78 sec: 1.12x faster                                          |
| tornado_http   | 105 ms                                                          | 94.1 ms: 1.12x faster                                           |
| Geometric mean | (ref)                                                           | 1.15x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 494 ms: 1.37x faster                                            |
| async_tree_io              | 693 ms                                                          | 526 ms: 1.32x faster                                            |
| async_tree_none_tg         | 278 ms                                                          | 214 ms: 1.30x faster                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 282 ms: 1.24x faster                                            |
| async_tree_memoization     | 364 ms                                                          | 297 ms: 1.23x faster                                            |
| async_tree_none            | 298 ms                                                          | 245 ms: 1.22x faster                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 456 ms: 1.20x faster                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 484 ms: 1.16x faster                                            |
| Geometric mean             | (ref)                                                           | 1.25x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 80.0 ms: 1.59x faster                                           |
| float          | 76.7 ms                                                         | 54.6 ms: 1.40x faster                                           |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                           | 1.30x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 101 ms: 1.28x faster                                            |
| regex_effbot   | 2.04 ms                                                         | 1.80 ms: 1.13x faster                                           |
| regex_dna      | 127 ms                                                          | 114 ms: 1.12x faster                                            |
| regex_v8       | 15.0 ms                                                         | 16.8 ms: 1.12x slower                                           |
| Geometric mean | (ref)                                                           | 1.10x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 160 us: 1.31x faster                                            |
| tomli_loads          | 2.20 sec                                                        | 1.71 sec: 1.28x faster                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 62.6 ms: 1.24x faster                                           |
| pickle_pure_python   | 286 us                                                          | 231 us: 1.24x faster                                            |
| xml_etree_process    | 53.2 ms                                                         | 44.2 ms: 1.20x faster                                           |
| xml_etree_generate   | 72.1 ms                                                         | 61.4 ms: 1.17x faster                                           |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.05x faster                                            |
| json_dumps           | 7.40 ms                                                         | 7.30 ms: 1.01x faster                                           |
| json_loads           | 20.4 us                                                         | 21.6 us: 1.06x slower                                           |
| Geometric mean       | (ref)                                                           | 1.16x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.7 ms: 1.03x slower                                           |
| python_startup         | 22.4 ms                                                         | 28.3 ms: 1.27x slower                                           |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.09 ms: 1.40x faster                                           |
| django_template | 36.9 ms                                                         | 29.8 ms: 1.24x faster                                           |
| Geometric mean  | (ref)                                                           | 1.32x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 21.8 ms: 1.77x faster                                           |
| logging_silent             | 101 ns                                                          | 60.3 ns: 1.67x faster                                           |
| nbody                      | 127 ms                                                          | 80.0 ms: 1.59x faster                                           |
| scimark_lu                 | 93.2 ms                                                         | 60.2 ms: 1.55x faster                                           |
| deltablue                  | 3.58 ms                                                         | 2.33 ms: 1.54x faster                                           |
| hexiom                     | 6.82 ms                                                         | 4.44 ms: 1.54x faster                                           |
| comprehensions             | 19.2 us                                                         | 12.5 us: 1.53x faster                                           |
| raytrace                   | 308 ms                                                          | 201 ms: 1.53x faster                                            |
| scimark_sor                | 130 ms                                                          | 85.9 ms: 1.51x faster                                           |
| deepcopy_memo              | 38.4 us                                                         | 25.4 us: 1.51x faster                                           |
| spectral_norm              | 104 ms                                                          | 69.4 ms: 1.50x faster                                           |
| mako                       | 9.96 ms                                                         | 7.09 ms: 1.40x faster                                           |
| float                      | 76.7 ms                                                         | 54.6 ms: 1.40x faster                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 47.7 ms: 1.39x faster                                           |
| chaos                      | 69.4 ms                                                         | 50.2 ms: 1.38x faster                                           |
| async_tree_io_tg           | 677 ms                                                          | 494 ms: 1.37x faster                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.84 ms: 1.36x faster                                           |
| pyflate                    | 424 ms                                                          | 320 ms: 1.32x faster                                            |
| scimark_fft                | 271 ms                                                          | 205 ms: 1.32x faster                                            |
| async_tree_io              | 693 ms                                                          | 526 ms: 1.32x faster                                            |
| unpickle_pure_python       | 210 us                                                          | 160 us: 1.31x faster                                            |
| nqueens                    | 93.7 ms                                                         | 72.1 ms: 1.30x faster                                           |
| async_tree_none_tg         | 278 ms                                                          | 214 ms: 1.30x faster                                            |
| coroutines                 | 20.9 ms                                                         | 16.2 ms: 1.29x faster                                           |
| tomli_loads                | 2.20 sec                                                        | 1.71 sec: 1.28x faster                                          |
| regex_compile              | 129 ms                                                          | 101 ms: 1.28x faster                                            |
| chameleon                  | 7.75 ms                                                         | 6.08 ms: 1.27x faster                                           |
| richards_super             | 46.5 ms                                                         | 36.7 ms: 1.27x faster                                           |
| richards                   | 41.3 ms                                                         | 32.7 ms: 1.26x faster                                           |
| go                         | 137 ms                                                          | 109 ms: 1.26x faster                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.00 ms: 1.25x faster                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 282 ms: 1.24x faster                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 62.6 ms: 1.24x faster                                           |
| django_template            | 36.9 ms                                                         | 29.8 ms: 1.24x faster                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.24 ms: 1.24x faster                                           |
| pickle_pure_python         | 286 us                                                          | 231 us: 1.24x faster                                            |
| async_tree_memoization     | 364 ms                                                          | 297 ms: 1.23x faster                                            |
| logging_simple             | 9.75 us                                                         | 7.99 us: 1.22x faster                                           |
| crypto_pyaes               | 69.2 ms                                                         | 56.9 ms: 1.22x faster                                           |
| async_tree_none            | 298 ms                                                          | 245 ms: 1.22x faster                                            |
| xml_etree_process          | 53.2 ms                                                         | 44.2 ms: 1.20x faster                                           |
| dulwich_log                | 58.5 ms                                                         | 48.8 ms: 1.20x faster                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 456 ms: 1.20x faster                                            |
| logging_format             | 10.4 us                                                         | 8.72 us: 1.19x faster                                           |
| fannkuch                   | 354 ms                                                          | 299 ms: 1.18x faster                                            |
| mdp                        | 1.91 sec                                                        | 1.62 sec: 1.18x faster                                          |
| xml_etree_generate         | 72.1 ms                                                         | 61.4 ms: 1.17x faster                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.0 ms: 1.17x faster                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 41.4 ms: 1.17x faster                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 484 ms: 1.16x faster                                            |
| meteor_contest             | 86.9 ms                                                         | 74.6 ms: 1.16x faster                                           |
| sympy_sum                  | 123 ms                                                          | 106 ms: 1.16x faster                                            |
| async_generators           | 313 ms                                                          | 270 ms: 1.16x faster                                            |
| deepcopy                   | 360 us                                                          | 314 us: 1.15x faster                                            |
| regex_effbot               | 2.04 ms                                                         | 1.80 ms: 1.13x faster                                           |
| sympy_str                  | 240 ms                                                          | 212 ms: 1.13x faster                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.33 sec: 1.13x faster                                          |
| pycparser                  | 978 ms                                                          | 872 ms: 1.12x faster                                            |
| 2to3                       | 280 ms                                                          | 250 ms: 1.12x faster                                            |
| regex_dna                  | 127 ms                                                          | 114 ms: 1.12x faster                                            |
| tornado_http               | 105 ms                                                          | 94.1 ms: 1.12x faster                                           |
| docutils                   | 1.98 sec                                                        | 1.78 sec: 1.12x faster                                          |
| pprint_safe_repr           | 721 ms                                                          | 648 ms: 1.11x faster                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.92 us: 1.11x faster                                           |
| pathlib                    | 91.4 ms                                                         | 82.9 ms: 1.10x faster                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.00 ms: 1.10x faster                                           |
| sqlalchemy_imperative      | 12.3 ms                                                         | 11.2 ms: 1.10x faster                                           |
| sqlalchemy_declarative     | 103 ms                                                          | 94.9 ms: 1.08x faster                                           |
| sympy_expand               | 398 ms                                                          | 373 ms: 1.07x faster                                            |
| sqlite_synth               | 2.07 us                                                         | 1.95 us: 1.06x faster                                           |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.05x faster                                            |
| json_dumps                 | 7.40 ms                                                         | 7.30 ms: 1.01x faster                                           |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                            |
| json                       | 4.15 ms                                                         | 4.27 ms: 1.03x slower                                           |
| python_startup_no_site     | 19.1 ms                                                         | 19.7 ms: 1.03x slower                                           |
| json_loads                 | 20.4 us                                                         | 21.6 us: 1.06x slower                                           |
| typing_runtime_protocols   | 126 us                                                          | 138 us: 1.09x slower                                            |
| regex_v8                   | 15.0 ms                                                         | 16.8 ms: 1.12x slower                                           |
| bench_mp_pool              | 75.4 ms                                                         | 90.6 ms: 1.20x slower                                           |
| gc_traversal               | 1.44 ms                                                         | 1.75 ms: 1.21x slower                                           |
| telco                      | 5.51 ms                                                         | 6.96 ms: 1.26x slower                                           |
| python_startup             | 22.4 ms                                                         | 28.3 ms: 1.27x slower                                           |
| create_gc_cycles           | 652 us                                                          | 1.06 ms: 1.62x slower                                           |
| sqlglot_normalize          | 100 ms                                                          | 216 ms: 2.16x slower                                            |
| coverage                   | 48.4 ms                                                         | 324 ms: 6.69x slower                                            |
| Geometric mean             | (ref)                                                           | 1.15x faster                                                    |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.153x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown
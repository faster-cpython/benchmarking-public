# Results vs. 3.12.0

- fork: python
- ref: v3.13.1
- machine: windows-x86
- commit hash: 0671451
- commit date: 2024-12-03
- overall geometric mean: 1.152x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 246 ms: 1.14x faster                                            |
| chameleon      | 7.75 ms                                                         | 6.19 ms: 1.25x faster                                           |
| docutils       | 1.98 sec                                                        | 1.77 sec: 1.12x faster                                          |
| tornado_http   | 105 ms                                                          | 94.1 ms: 1.12x faster                                           |
| Geometric mean | (ref)                                                           | 1.15x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 510 ms: 1.33x faster                                            |
| async_tree_io              | 693 ms                                                          | 524 ms: 1.32x faster                                            |
| async_tree_none_tg         | 278 ms                                                          | 218 ms: 1.27x faster                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 288 ms: 1.22x faster                                            |
| async_tree_memoization     | 364 ms                                                          | 299 ms: 1.22x faster                                            |
| async_tree_none            | 298 ms                                                          | 247 ms: 1.20x faster                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 484 ms: 1.17x faster                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 473 ms: 1.15x faster                                            |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 82.6 ms: 1.54x faster                                           |
| float          | 76.7 ms                                                         | 55.6 ms: 1.38x faster                                           |
| pidigits       | 199 ms                                                          | 198 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                           | 1.29x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                           |
| regex_compile  | 129 ms                                                          | 101 ms: 1.28x faster                                            |
| regex_dna      | 127 ms                                                          | 114 ms: 1.11x faster                                            |
| regex_v8       | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                           | 1.16x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 159 us: 1.32x faster                                            |
| tomli_loads          | 2.20 sec                                                        | 1.70 sec: 1.29x faster                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.0 ms: 1.23x faster                                           |
| pickle_pure_python   | 286 us                                                          | 235 us: 1.22x faster                                            |
| xml_etree_process    | 53.2 ms                                                         | 44.5 ms: 1.20x faster                                           |
| xml_etree_generate   | 72.1 ms                                                         | 62.6 ms: 1.15x faster                                           |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.05x faster                                            |
| json_dumps           | 7.40 ms                                                         | 7.27 ms: 1.02x faster                                           |
| json_loads           | 20.4 us                                                         | 22.1 us: 1.08x slower                                           |
| Geometric mean       | (ref)                                                           | 1.15x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                           |
| python_startup         | 22.4 ms                                                         | 27.2 ms: 1.22x slower                                           |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.33 ms: 1.36x faster                                           |
| django_template | 36.9 ms                                                         | 29.9 ms: 1.23x faster                                           |
| Geometric mean  | (ref)                                                           | 1.29x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 21.5 ms: 1.79x faster                                           |
| logging_silent             | 101 ns                                                          | 60.3 ns: 1.68x faster                                           |
| deepcopy_memo              | 38.4 us                                                         | 24.9 us: 1.54x faster                                           |
| nbody                      | 127 ms                                                          | 82.6 ms: 1.54x faster                                           |
| deltablue                  | 3.58 ms                                                         | 2.36 ms: 1.52x faster                                           |
| scimark_sor                | 130 ms                                                          | 85.9 ms: 1.51x faster                                           |
| comprehensions             | 19.2 us                                                         | 12.7 us: 1.51x faster                                           |
| spectral_norm              | 104 ms                                                          | 69.4 ms: 1.50x faster                                           |
| scimark_lu                 | 93.2 ms                                                         | 62.3 ms: 1.50x faster                                           |
| hexiom                     | 6.82 ms                                                         | 4.56 ms: 1.50x faster                                           |
| raytrace                   | 308 ms                                                          | 208 ms: 1.48x faster                                            |
| float                      | 76.7 ms                                                         | 55.6 ms: 1.38x faster                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 48.3 ms: 1.37x faster                                           |
| chaos                      | 69.4 ms                                                         | 50.5 ms: 1.37x faster                                           |
| mako                       | 9.96 ms                                                         | 7.33 ms: 1.36x faster                                           |
| pyflate                    | 424 ms                                                          | 314 ms: 1.35x faster                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.88 ms: 1.34x faster                                           |
| async_tree_io_tg           | 677 ms                                                          | 510 ms: 1.33x faster                                            |
| scimark_fft                | 271 ms                                                          | 205 ms: 1.32x faster                                            |
| async_tree_io              | 693 ms                                                          | 524 ms: 1.32x faster                                            |
| unpickle_pure_python       | 210 us                                                          | 159 us: 1.32x faster                                            |
| regex_effbot               | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                           |
| coroutines                 | 20.9 ms                                                         | 15.9 ms: 1.31x faster                                           |
| nqueens                    | 93.7 ms                                                         | 72.0 ms: 1.30x faster                                           |
| tomli_loads                | 2.20 sec                                                        | 1.70 sec: 1.29x faster                                          |
| regex_compile              | 129 ms                                                          | 101 ms: 1.28x faster                                            |
| async_tree_none_tg         | 278 ms                                                          | 218 ms: 1.27x faster                                            |
| richards_super             | 46.5 ms                                                         | 36.7 ms: 1.27x faster                                           |
| richards                   | 41.3 ms                                                         | 32.7 ms: 1.26x faster                                           |
| chameleon                  | 7.75 ms                                                         | 6.19 ms: 1.25x faster                                           |
| fannkuch                   | 354 ms                                                          | 286 ms: 1.24x faster                                            |
| django_template            | 36.9 ms                                                         | 29.9 ms: 1.23x faster                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.0 ms: 1.23x faster                                           |
| go                         | 137 ms                                                          | 112 ms: 1.22x faster                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.02 ms: 1.22x faster                                           |
| deepcopy                   | 360 us                                                          | 294 us: 1.22x faster                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 288 ms: 1.22x faster                                            |
| logging_simple             | 9.75 us                                                         | 8.01 us: 1.22x faster                                           |
| pickle_pure_python         | 286 us                                                          | 235 us: 1.22x faster                                            |
| async_tree_memoization     | 364 ms                                                          | 299 ms: 1.22x faster                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.26 ms: 1.21x faster                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.67 us: 1.21x faster                                           |
| logging_format             | 10.4 us                                                         | 8.62 us: 1.21x faster                                           |
| async_tree_none            | 298 ms                                                          | 247 ms: 1.20x faster                                            |
| dulwich_log                | 58.5 ms                                                         | 48.5 ms: 1.20x faster                                           |
| crypto_pyaes               | 69.2 ms                                                         | 57.5 ms: 1.20x faster                                           |
| xml_etree_process          | 53.2 ms                                                         | 44.5 ms: 1.20x faster                                           |
| async_generators           | 313 ms                                                          | 266 ms: 1.18x faster                                            |
| sympy_integrate            | 17.5 ms                                                         | 15.0 ms: 1.17x faster                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 484 ms: 1.17x faster                                            |
| sympy_sum                  | 123 ms                                                          | 106 ms: 1.16x faster                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 41.8 ms: 1.16x faster                                           |
| mdp                        | 1.91 sec                                                        | 1.65 sec: 1.16x faster                                          |
| pycparser                  | 978 ms                                                          | 846 ms: 1.16x faster                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 473 ms: 1.15x faster                                            |
| xml_etree_generate         | 72.1 ms                                                         | 62.6 ms: 1.15x faster                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.31 sec: 1.14x faster                                          |
| meteor_contest             | 86.9 ms                                                         | 76.0 ms: 1.14x faster                                           |
| 2to3                       | 280 ms                                                          | 246 ms: 1.14x faster                                            |
| sympy_str                  | 240 ms                                                          | 212 ms: 1.13x faster                                            |
| pprint_safe_repr           | 721 ms                                                          | 639 ms: 1.13x faster                                            |
| docutils                   | 1.98 sec                                                        | 1.77 sec: 1.12x faster                                          |
| tornado_http               | 105 ms                                                          | 94.1 ms: 1.12x faster                                           |
| regex_dna                  | 127 ms                                                          | 114 ms: 1.11x faster                                            |
| sqlalchemy_imperative      | 12.3 ms                                                         | 11.1 ms: 1.11x faster                                           |
| pathlib                    | 91.4 ms                                                         | 83.0 ms: 1.10x faster                                           |
| sqlalchemy_declarative     | 103 ms                                                          | 93.5 ms: 1.10x faster                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                           |
| sqlite_synth               | 2.07 us                                                         | 1.93 us: 1.08x faster                                           |
| sympy_expand               | 398 ms                                                          | 373 ms: 1.07x faster                                            |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.05x faster                                            |
| json_dumps                 | 7.40 ms                                                         | 7.27 ms: 1.02x faster                                           |
| pidigits                   | 199 ms                                                          | 198 ms: 1.01x faster                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                           |
| regex_v8                   | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                           |
| json_loads                 | 20.4 us                                                         | 22.1 us: 1.08x slower                                           |
| json                       | 4.15 ms                                                         | 4.51 ms: 1.09x slower                                           |
| typing_runtime_protocols   | 126 us                                                          | 140 us: 1.11x slower                                            |
| bench_mp_pool              | 75.4 ms                                                         | 89.7 ms: 1.19x slower                                           |
| telco                      | 5.51 ms                                                         | 6.60 ms: 1.20x slower                                           |
| gc_traversal               | 1.44 ms                                                         | 1.74 ms: 1.21x slower                                           |
| python_startup             | 22.4 ms                                                         | 27.2 ms: 1.22x slower                                           |
| create_gc_cycles           | 652 us                                                          | 1.08 ms: 1.65x slower                                           |
| sqlglot_normalize          | 100 ms                                                          | 220 ms: 2.19x slower                                            |
| coverage                   | 48.4 ms                                                         | 326 ms: 6.74x slower                                            |
| Geometric mean             | (ref)                                                           | 1.15x faster                                                    |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20241203-3.13.1-0671451/bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451.json: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.152x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown
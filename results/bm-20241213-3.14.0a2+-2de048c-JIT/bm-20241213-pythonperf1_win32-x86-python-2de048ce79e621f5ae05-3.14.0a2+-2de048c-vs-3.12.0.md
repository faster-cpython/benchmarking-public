# Results vs. 3.12.0

- fork: python
- ref: 2de048ce79e621f5ae05
- machine: windows-x86
- commit hash: 2de048c
- commit date: 2024-12-13
- overall geometric mean: 1.078x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 262 ms: 1.07x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.93 sec: 1.03x faster                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 443 ms: 1.53x faster                                                            |
| async_tree_io              | 693 ms                                                          | 473 ms: 1.46x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 245 ms: 1.43x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 194 ms: 1.43x faster                                                            |
| async_tree_none            | 298 ms                                                          | 225 ms: 1.32x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 277 ms: 1.31x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 457 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 502 ms: 1.12x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.34x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 56.1 ms: 1.37x faster                                                           |
| nbody          | 127 ms                                                          | 99.3 ms: 1.28x faster                                                           |
| pidigits       | 199 ms                                                          | 204 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.59 ms: 1.28x faster                                                           |
| regex_compile  | 129 ms                                                          | 114 ms: 1.13x faster                                                            |
| regex_dna      | 127 ms                                                          | 114 ms: 1.11x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.74 sec: 1.26x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 65.3 ms: 1.19x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.06x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 69.3 ms: 1.04x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 203 us: 1.03x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 51.7 ms: 1.03x faster                                                           |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                           |
| pickle_pure_python   | 286 us                                                          | 298 us: 1.04x slower                                                            |
| json_dumps           | 7.40 ms                                                         | 9.22 ms: 1.25x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.33 ms: 1.36x faster                                                           |
| django_template | 36.9 ms                                                         | 36.1 ms: 1.02x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.18x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 23.7 us: 1.62x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 443 ms: 1.53x faster                                                            |
| async_tree_io              | 693 ms                                                          | 473 ms: 1.46x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 245 ms: 1.43x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 194 ms: 1.43x faster                                                            |
| spectral_norm              | 104 ms                                                          | 73.7 ms: 1.41x faster                                                           |
| float                      | 76.7 ms                                                         | 56.1 ms: 1.37x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.33 ms: 1.36x faster                                                           |
| deepcopy                   | 360 us                                                          | 270 us: 1.34x faster                                                            |
| async_tree_none            | 298 ms                                                          | 225 ms: 1.32x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 277 ms: 1.31x faster                                                            |
| logging_silent             | 101 ns                                                          | 77.5 ns: 1.30x faster                                                           |
| scimark_sor                | 130 ms                                                          | 100 ms: 1.30x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.59 ms: 1.28x faster                                                           |
| nbody                      | 127 ms                                                          | 99.3 ms: 1.28x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 73.4 ms: 1.27x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.74 sec: 1.26x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 16.7 ms: 1.25x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.13 ms: 1.23x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 457 ms: 1.19x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.3 ms: 1.19x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 50.3 ms: 1.16x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.43 us: 1.16x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.79 us: 1.16x faster                                                           |
| logging_format             | 10.4 us                                                         | 9.04 us: 1.15x faster                                                           |
| go                         | 137 ms                                                          | 119 ms: 1.15x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 3.14 ms: 1.14x faster                                                           |
| regex_compile              | 129 ms                                                          | 114 ms: 1.13x faster                                                            |
| scimark_fft                | 271 ms                                                          | 241 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 502 ms: 1.12x faster                                                            |
| regex_dna                  | 127 ms                                                          | 114 ms: 1.11x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.13 ms: 1.10x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 83.4 ms: 1.10x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.41 ms: 1.09x faster                                                           |
| pyflate                    | 424 ms                                                          | 390 ms: 1.09x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.92 us: 1.08x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 61.7 ms: 1.08x faster                                                           |
| 2to3                       | 280 ms                                                          | 262 ms: 1.07x faster                                                            |
| chaos                      | 69.4 ms                                                         | 65.2 ms: 1.06x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 116 ms: 1.06x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                            |
| pycparser                  | 978 ms                                                          | 924 ms: 1.06x faster                                                            |
| generators                 | 38.5 ms                                                         | 36.5 ms: 1.06x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.05 ms: 1.05x faster                                                           |
| comprehensions             | 19.2 us                                                         | 18.4 us: 1.04x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 69.3 ms: 1.04x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 203 us: 1.03x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.85 sec: 1.03x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 51.7 ms: 1.03x faster                                                           |
| fannkuch                   | 354 ms                                                          | 343 ms: 1.03x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.93 sec: 1.03x faster                                                          |
| raytrace                   | 308 ms                                                          | 300 ms: 1.03x faster                                                            |
| django_template            | 36.9 ms                                                         | 36.1 ms: 1.02x faster                                                           |
| sympy_str                  | 240 ms                                                          | 235 ms: 1.02x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 68.0 ms: 1.02x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 17.4 ms: 1.01x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.52 sec: 1.01x slower                                                          |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                           |
| json                       | 4.15 ms                                                         | 4.24 ms: 1.02x slower                                                           |
| pidigits                   | 199 ms                                                          | 204 ms: 1.02x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                           |
| sympy_expand               | 398 ms                                                          | 409 ms: 1.03x slower                                                            |
| meteor_contest             | 86.9 ms                                                         | 89.3 ms: 1.03x slower                                                           |
| pprint_safe_repr           | 721 ms                                                          | 741 ms: 1.03x slower                                                            |
| nqueens                    | 93.7 ms                                                         | 97.5 ms: 1.04x slower                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 50.4 ms: 1.04x slower                                                           |
| pickle_pure_python         | 286 us                                                          | 298 us: 1.04x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                           |
| async_generators           | 313 ms                                                          | 328 ms: 1.05x slower                                                            |
| hexiom                     | 6.82 ms                                                         | 7.15 ms: 1.05x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 105 ms: 1.05x slower                                                            |
| coverage                   | 48.4 ms                                                         | 53.1 ms: 1.10x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 87.6 ms: 1.16x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                           |
| mypy2                      | 584 ms                                                          | 717 ms: 1.23x slower                                                            |
| json_dumps                 | 7.40 ms                                                         | 9.22 ms: 1.25x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.80 ms: 1.25x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.10 ms: 1.29x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 168 us: 1.33x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.04 ms: 1.60x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.08x faster                                                                    |

Benchmark hidden because not significant (2): richards_super, richards
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241213-3.14.0a2+-2de048c-JIT/bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.078x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown
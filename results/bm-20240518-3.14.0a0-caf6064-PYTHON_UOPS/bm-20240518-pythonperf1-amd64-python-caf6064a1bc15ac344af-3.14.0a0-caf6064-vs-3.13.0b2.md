# Results vs. 3.13.0b2

- fork: python
- ref: caf6064a1bc15ac344af
- machine: windows-amd64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 229 ms: 1.11x slower                                                       |
| chameleon      | 4.80 ms                                                         | 5.12 ms: 1.07x slower                                                      |
| docutils       | 1.63 sec                                                        | 1.83 sec: 1.12x slower                                                     |
| html5lib       | 35.0 ms                                                         | 41.5 ms: 1.18x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 87.0 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed   | 389 ms                                                          | 400 ms: 1.03x slower                                                       |
| async_tree_io_tg          | 605 ms                                                          | 628 ms: 1.04x slower                                                       |
| async_tree_io             | 588 ms                                                          | 612 ms: 1.04x slower                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 272 ms: 1.05x slower                                                       |
| async_tree_memoization    | 264 ms                                                          | 278 ms: 1.05x slower                                                       |
| async_tree_none           | 218 ms                                                          | 231 ms: 1.06x slower                                                       |
| async_tree_none_tg        | 202 ms                                                          | 217 ms: 1.07x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.04x slower                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| float          | 49.7 ms                                                         | 53.6 ms: 1.08x slower                                                      |
| nbody          | 67.6 ms                                                         | 75.0 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                           | 1.06x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 119 ms: 1.00x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 106 ms: 1.36x slower                                                       |
| Geometric mean | (ref)                                                           | 1.08x slower                                                               |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 13.9 us: 1.02x faster                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 90.3 ms: 1.01x faster                                                      |
| pickle_dict          | 18.1 us                                                         | 18.4 us: 1.01x slower                                                      |
| unpickle             | 8.40 us                                                         | 8.58 us: 1.02x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.81 ms: 1.04x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.2 ms: 1.05x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 56.6 ms: 1.07x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.81 us: 1.07x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 39.5 ms: 1.08x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.47 sec: 1.09x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 217 us: 1.24x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 155 us: 1.27x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                               |

Benchmark hidden because not significant (2): pickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.0 ms: 1.02x faster                                                      |
| python_startup_no_site | 16.2 ms                                                         | 16.4 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.00x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 7.35 ms: 1.16x slower                                                      |
| django_template | 21.7 ms                                                         | 25.1 ms: 1.16x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 37.6 ms: 1.19x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.4 ms: 1.21x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.18x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 511 us: 15.85x faster                                                      |
| json                      | 3.19 ms                                                         | 2.93 ms: 1.09x faster                                                      |
| json_loads                | 14.2 us                                                         | 13.9 us: 1.02x faster                                                      |
| python_startup            | 20.3 ms                                                         | 20.0 ms: 1.02x faster                                                      |
| xml_etree_parse           | 90.9 ms                                                         | 90.3 ms: 1.01x faster                                                      |
| regex_dna                 | 119 ms                                                          | 119 ms: 1.00x slower                                                       |
| gc_traversal              | 1.55 ms                                                         | 1.56 ms: 1.01x slower                                                      |
| pidigits                  | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| pickle_dict               | 18.1 us                                                         | 18.4 us: 1.01x slower                                                      |
| python_startup_no_site    | 16.2 ms                                                         | 16.4 ms: 1.01x slower                                                      |
| sqlite_synth              | 1.60 us                                                         | 1.63 us: 1.02x slower                                                      |
| generators                | 19.6 ms                                                         | 19.9 ms: 1.02x slower                                                      |
| unpickle                  | 8.40 us                                                         | 8.58 us: 1.02x slower                                                      |
| create_gc_cycles          | 888 us                                                          | 912 us: 1.03x slower                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 400 ms: 1.03x slower                                                       |
| json_dumps                | 5.61 ms                                                         | 5.81 ms: 1.04x slower                                                      |
| async_tree_io_tg          | 605 ms                                                          | 628 ms: 1.04x slower                                                       |
| async_tree_io             | 588 ms                                                          | 612 ms: 1.04x slower                                                       |
| bench_mp_pool             | 64.8 ms                                                         | 67.6 ms: 1.04x slower                                                      |
| pathlib                   | 75.9 ms                                                         | 79.2 ms: 1.04x slower                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 65.2 ms: 1.05x slower                                                      |
| telco                     | 4.67 ms                                                         | 4.91 ms: 1.05x slower                                                      |
| async_tree_memoization_tg | 258 ms                                                          | 272 ms: 1.05x slower                                                       |
| async_tree_memoization    | 264 ms                                                          | 278 ms: 1.05x slower                                                       |
| richards                  | 26.7 ms                                                         | 28.2 ms: 1.06x slower                                                      |
| async_tree_none           | 218 ms                                                          | 231 ms: 1.06x slower                                                       |
| richards_super            | 30.2 ms                                                         | 32.0 ms: 1.06x slower                                                      |
| tornado_http              | 81.8 ms                                                         | 87.0 ms: 1.06x slower                                                      |
| coverage                  | 42.1 ms                                                         | 44.8 ms: 1.06x slower                                                      |
| xml_etree_generate        | 53.2 ms                                                         | 56.6 ms: 1.07x slower                                                      |
| chameleon                 | 4.80 ms                                                         | 5.12 ms: 1.07x slower                                                      |
| mdp                       | 1.31 sec                                                        | 1.40 sec: 1.07x slower                                                     |
| unpickle_list             | 2.62 us                                                         | 2.81 us: 1.07x slower                                                      |
| logging_format            | 6.22 us                                                         | 6.67 us: 1.07x slower                                                      |
| async_tree_none_tg        | 202 ms                                                          | 217 ms: 1.07x slower                                                       |
| float                     | 49.7 ms                                                         | 53.6 ms: 1.08x slower                                                      |
| deepcopy_reduce           | 1.99 us                                                         | 2.15 us: 1.08x slower                                                      |
| logging_simple            | 5.78 us                                                         | 6.23 us: 1.08x slower                                                      |
| crypto_pyaes              | 45.5 ms                                                         | 49.2 ms: 1.08x slower                                                      |
| xml_etree_process         | 36.4 ms                                                         | 39.5 ms: 1.08x slower                                                      |
| tomli_loads               | 1.35 sec                                                        | 1.47 sec: 1.09x slower                                                     |
| bench_thread_pool         | 768 us                                                          | 839 us: 1.09x slower                                                       |
| async_generators          | 223 ms                                                          | 245 ms: 1.10x slower                                                       |
| meteor_contest            | 69.9 ms                                                         | 76.7 ms: 1.10x slower                                                      |
| fannkuch                  | 243 ms                                                          | 267 ms: 1.10x slower                                                       |
| 2to3                      | 207 ms                                                          | 229 ms: 1.11x slower                                                       |
| nbody                     | 67.6 ms                                                         | 75.0 ms: 1.11x slower                                                      |
| raytrace                  | 162 ms                                                          | 180 ms: 1.11x slower                                                       |
| pprint_safe_repr          | 474 ms                                                          | 530 ms: 1.12x slower                                                       |
| docutils                  | 1.63 sec                                                        | 1.83 sec: 1.12x slower                                                     |
| pprint_pformat            | 966 ms                                                          | 1.09 sec: 1.13x slower                                                     |
| chaos                     | 38.4 ms                                                         | 43.2 ms: 1.13x slower                                                      |
| deepcopy                  | 220 us                                                          | 249 us: 1.13x slower                                                       |
| pylint                    | 205 ms                                                          | 232 ms: 1.13x slower                                                       |
| scimark_fft               | 171 ms                                                          | 195 ms: 1.14x slower                                                       |
| typing_runtime_protocols  | 101 us                                                          | 116 us: 1.14x slower                                                       |
| scimark_sor               | 75.3 ms                                                         | 86.3 ms: 1.15x slower                                                      |
| mako                      | 6.36 ms                                                         | 7.35 ms: 1.16x slower                                                      |
| django_template           | 21.7 ms                                                         | 25.1 ms: 1.16x slower                                                      |
| pyflate                   | 279 ms                                                          | 324 ms: 1.16x slower                                                       |
| spectral_norm             | 63.7 ms                                                         | 74.5 ms: 1.17x slower                                                      |
| sqlglot_transpile         | 955 us                                                          | 1.12 ms: 1.17x slower                                                      |
| nqueens                   | 56.7 ms                                                         | 66.4 ms: 1.17x slower                                                      |
| sympy_sum                 | 84.4 ms                                                         | 99.3 ms: 1.18x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 881 us: 1.18x slower                                                       |
| sqlglot_optimize          | 32.7 ms                                                         | 38.6 ms: 1.18x slower                                                      |
| html5lib                  | 35.0 ms                                                         | 41.5 ms: 1.18x slower                                                      |
| sympy_integrate           | 12.2 ms                                                         | 14.5 ms: 1.18x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 37.6 ms: 1.19x slower                                                      |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 3.01 ms: 1.20x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 17.4 ms: 1.21x slower                                                      |
| scimark_monte_carlo       | 39.1 ms                                                         | 47.6 ms: 1.22x slower                                                      |
| sympy_str                 | 159 ms                                                          | 195 ms: 1.22x slower                                                       |
| go                        | 82.1 ms                                                         | 100 ms: 1.22x slower                                                       |
| pickle_pure_python        | 175 us                                                          | 217 us: 1.24x slower                                                       |
| sympy_expand              | 271 ms                                                          | 337 ms: 1.24x slower                                                       |
| deepcopy_memo             | 22.1 us                                                         | 28.0 us: 1.27x slower                                                      |
| comprehensions            | 10.4 us                                                         | 13.1 us: 1.27x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 155 us: 1.27x slower                                                       |
| logging_silent            | 52.9 ns                                                         | 68.2 ns: 1.29x slower                                                      |
| regex_compile             | 78.0 ms                                                         | 106 ms: 1.36x slower                                                       |
| scimark_lu                | 56.6 ms                                                         | 77.2 ms: 1.36x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 2.59 ms: 1.38x slower                                                      |
| hexiom                    | 3.72 ms                                                         | 5.23 ms: 1.40x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.07x slower                                                               |

Benchmark hidden because not significant (10): regex_effbot, flaskblogging, pickle, coroutines, asyncio_tcp, regex_v8, pickle_list, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, pycparser
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, dulwich_log, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown
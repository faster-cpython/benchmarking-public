# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin_mprotect_cost
- machine: windows-amd64
- commit hash: c8d6017
- commit date: 2024-03-18
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 214 ms                                                      | 221 ms: 1.04x slower                                                              |
| chameleon      | 5.26 ms                                                     | 4.70 ms: 1.12x faster                                                             |
| docutils       | 1.64 sec                                                    | 1.58 sec: 1.04x faster                                                            |
| html5lib       | 38.9 ms                                                     | 35.8 ms: 1.09x faster                                                             |
| tornado_http   | 92.8 ms                                                     | 83.7 ms: 1.11x faster                                                             |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none            | 332 ms                                                      | 265 ms: 1.25x faster                                                              |
| async_tree_memoization     | 399 ms                                                      | 340 ms: 1.17x faster                                                              |
| async_tree_memoization_tg  | 405 ms                                                      | 346 ms: 1.17x faster                                                              |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 454 ms: 1.17x faster                                                              |
| async_tree_none_tg         | 309 ms                                                      | 269 ms: 1.15x faster                                                              |
| async_tree_io              | 808 ms                                                      | 717 ms: 1.13x faster                                                              |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 468 ms: 1.12x faster                                                              |
| async_tree_io_tg           | 829 ms                                                      | 745 ms: 1.11x faster                                                              |
| Geometric mean             | (ref)                                                       | 1.16x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 70.3 ms                                                     | 58.4 ms: 1.21x faster                                                             |
| float          | 54.4 ms                                                     | 48.1 ms: 1.13x faster                                                             |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 91.0 ms                                                     | 83.0 ms: 1.10x faster                                                             |
| regex_dna      | 116 ms                                                      | 114 ms: 1.02x faster                                                              |
| regex_effbot   | 1.50 ms                                                     | 1.56 ms: 1.04x slower                                                             |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.10x slower                                                             |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 8.09 ms                                                     | 5.51 ms: 1.47x faster                                                             |
| tomli_loads          | 1.46 sec                                                    | 1.19 sec: 1.22x faster                                                            |
| unpickle_pure_python | 157 us                                                      | 128 us: 1.22x faster                                                              |
| pickle_pure_python   | 208 us                                                      | 177 us: 1.18x faster                                                              |
| xml_etree_parse      | 97.6 ms                                                     | 91.7 ms: 1.06x faster                                                             |
| xml_etree_iterparse  | 65.6 ms                                                     | 61.9 ms: 1.06x faster                                                             |
| pickle_dict          | 18.5 us                                                     | 17.6 us: 1.05x faster                                                             |
| xml_etree_process    | 37.2 ms                                                     | 36.8 ms: 1.01x faster                                                             |
| pickle_list          | 2.70 us                                                     | 2.73 us: 1.01x slower                                                             |
| xml_etree_generate   | 52.5 ms                                                     | 54.1 ms: 1.03x slower                                                             |
| json_loads           | 13.0 us                                                     | 13.7 us: 1.05x slower                                                             |
| unpickle_list        | 2.59 us                                                     | 2.74 us: 1.06x slower                                                             |
| pickle               | 6.64 us                                                     | 7.28 us: 1.10x slower                                                             |
| unpickle             | 7.57 us                                                     | 8.70 us: 1.15x slower                                                             |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 19.8 ms                                                     | 23.4 ms: 1.19x slower                                                             |
| python_startup_no_site | 16.8 ms                                                     | 21.4 ms: 1.27x slower                                                             |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 7.58 ms                                                     | 5.48 ms: 1.38x faster                                                             |
| genshi_text     | 18.4 ms                                                     | 16.1 ms: 1.14x faster                                                             |
| django_template | 24.4 ms                                                     | 21.9 ms: 1.11x faster                                                             |
| genshi_xml      | 39.9 ms                                                     | 37.1 ms: 1.08x faster                                                             |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 326 us                                                      | 70.3 us: 4.64x faster                                                             |
| generators                 | 34.0 ms                                                     | 20.2 ms: 1.68x faster                                                             |
| pylint                     | 323 ms                                                      | 211 ms: 1.53x faster                                                              |
| asyncio_tcp                | 726 ms                                                      | 484 ms: 1.50x faster                                                              |
| comprehensions             | 15.6 us                                                     | 10.6 us: 1.47x faster                                                             |
| json_dumps                 | 8.09 ms                                                     | 5.51 ms: 1.47x faster                                                             |
| mako                       | 7.58 ms                                                     | 5.48 ms: 1.38x faster                                                             |
| spectral_norm              | 68.3 ms                                                     | 50.7 ms: 1.35x faster                                                             |
| deltablue                  | 2.70 ms                                                     | 2.04 ms: 1.32x faster                                                             |
| logging_silent             | 71.8 ns                                                     | 55.5 ns: 1.29x faster                                                             |
| async_tree_none            | 332 ms                                                      | 265 ms: 1.25x faster                                                              |
| richards_super             | 38.7 ms                                                     | 31.2 ms: 1.24x faster                                                             |
| chaos                      | 48.4 ms                                                     | 39.4 ms: 1.23x faster                                                             |
| sqlglot_parse              | 953 us                                                      | 777 us: 1.23x faster                                                              |
| tomli_loads                | 1.46 sec                                                    | 1.19 sec: 1.22x faster                                                            |
| unpickle_pure_python       | 157 us                                                      | 128 us: 1.22x faster                                                              |
| nbody                      | 70.3 ms                                                     | 58.4 ms: 1.21x faster                                                             |
| raytrace                   | 213 ms                                                      | 178 ms: 1.20x faster                                                              |
| deepcopy_memo              | 26.0 us                                                     | 21.8 us: 1.19x faster                                                             |
| fannkuch                   | 253 ms                                                      | 213 ms: 1.19x faster                                                              |
| logging_simple             | 6.86 us                                                     | 5.79 us: 1.18x faster                                                             |
| pickle_pure_python         | 208 us                                                      | 177 us: 1.18x faster                                                              |
| async_tree_memoization     | 399 ms                                                      | 340 ms: 1.17x faster                                                              |
| async_tree_memoization_tg  | 405 ms                                                      | 346 ms: 1.17x faster                                                              |
| asyncio_tcp_ssl            | 2.03 sec                                                    | 1.74 sec: 1.17x faster                                                            |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 454 ms: 1.17x faster                                                              |
| sqlglot_transpile          | 1.16 ms                                                     | 999 us: 1.17x faster                                                              |
| sympy_sum                  | 100 ms                                                      | 86.3 ms: 1.16x faster                                                             |
| scimark_sparse_mat_mult    | 2.58 ms                                                     | 2.24 ms: 1.15x faster                                                             |
| async_tree_none_tg         | 309 ms                                                      | 269 ms: 1.15x faster                                                              |
| genshi_text                | 18.4 ms                                                     | 16.1 ms: 1.14x faster                                                             |
| logging_format             | 7.16 us                                                     | 6.28 us: 1.14x faster                                                             |
| coroutines                 | 15.0 ms                                                     | 13.1 ms: 1.14x faster                                                             |
| dulwich_log                | 46.4 ms                                                     | 41.0 ms: 1.13x faster                                                             |
| float                      | 54.4 ms                                                     | 48.1 ms: 1.13x faster                                                             |
| nqueens                    | 68.3 ms                                                     | 60.6 ms: 1.13x faster                                                             |
| sqlite_synth               | 1.77 us                                                     | 1.57 us: 1.13x faster                                                             |
| async_tree_io              | 808 ms                                                      | 717 ms: 1.13x faster                                                              |
| richards                   | 31.4 ms                                                     | 27.9 ms: 1.13x faster                                                             |
| pprint_pformat             | 1.09 sec                                                    | 969 ms: 1.12x faster                                                              |
| sympy_str                  | 185 ms                                                      | 165 ms: 1.12x faster                                                              |
| chameleon                  | 5.26 ms                                                     | 4.70 ms: 1.12x faster                                                             |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 468 ms: 1.12x faster                                                              |
| django_template            | 24.4 ms                                                     | 21.9 ms: 1.11x faster                                                             |
| pprint_safe_repr           | 529 ms                                                      | 475 ms: 1.11x faster                                                              |
| async_tree_io_tg           | 829 ms                                                      | 745 ms: 1.11x faster                                                              |
| deepcopy                   | 246 us                                                      | 222 us: 1.11x faster                                                              |
| tornado_http               | 92.8 ms                                                     | 83.7 ms: 1.11x faster                                                             |
| pyflate                    | 312 ms                                                      | 282 ms: 1.11x faster                                                              |
| regex_compile              | 91.0 ms                                                     | 83.0 ms: 1.10x faster                                                             |
| scimark_monte_carlo        | 45.3 ms                                                     | 41.5 ms: 1.09x faster                                                             |
| mdp                        | 1.59 sec                                                    | 1.46 sec: 1.09x faster                                                            |
| html5lib                   | 38.9 ms                                                     | 35.8 ms: 1.09x faster                                                             |
| sqlglot_normalize          | 190 ms                                                      | 176 ms: 1.08x faster                                                              |
| sympy_integrate            | 14.0 ms                                                     | 13.0 ms: 1.08x faster                                                             |
| crypto_pyaes               | 48.9 ms                                                     | 45.3 ms: 1.08x faster                                                             |
| genshi_xml                 | 39.9 ms                                                     | 37.1 ms: 1.08x faster                                                             |
| deepcopy_reduce            | 2.06 us                                                     | 1.93 us: 1.07x faster                                                             |
| xml_etree_parse            | 97.6 ms                                                     | 91.7 ms: 1.06x faster                                                             |
| bench_thread_pool          | 872 us                                                      | 819 us: 1.06x faster                                                              |
| xml_etree_iterparse        | 65.6 ms                                                     | 61.9 ms: 1.06x faster                                                             |
| mypy2                      | 459 ms                                                      | 435 ms: 1.05x faster                                                              |
| scimark_fft                | 179 ms                                                      | 170 ms: 1.05x faster                                                              |
| pickle_dict                | 18.5 us                                                     | 17.6 us: 1.05x faster                                                             |
| sympy_expand               | 299 ms                                                      | 285 ms: 1.05x faster                                                              |
| hexiom                     | 4.55 ms                                                     | 4.36 ms: 1.04x faster                                                             |
| go                         | 101 ms                                                      | 96.8 ms: 1.04x faster                                                             |
| meteor_contest             | 75.2 ms                                                     | 72.6 ms: 1.04x faster                                                             |
| docutils                   | 1.64 sec                                                    | 1.58 sec: 1.04x faster                                                            |
| regex_dna                  | 116 ms                                                      | 114 ms: 1.02x faster                                                              |
| xml_etree_process          | 37.2 ms                                                     | 36.8 ms: 1.01x faster                                                             |
| unpack_sequence            | 46.9 ns                                                     | 46.6 ns: 1.01x faster                                                             |
| gc_traversal               | 1.49 ms                                                     | 1.50 ms: 1.01x slower                                                             |
| pickle_list                | 2.70 us                                                     | 2.73 us: 1.01x slower                                                             |
| aiohttp                    | 883 us                                                      | 898 us: 1.02x slower                                                              |
| xml_etree_generate         | 52.5 ms                                                     | 54.1 ms: 1.03x slower                                                             |
| 2to3                       | 214 ms                                                      | 221 ms: 1.04x slower                                                              |
| regex_effbot               | 1.50 ms                                                     | 1.56 ms: 1.04x slower                                                             |
| create_gc_cycles           | 713 us                                                      | 744 us: 1.04x slower                                                              |
| json_loads                 | 13.0 us                                                     | 13.7 us: 1.05x slower                                                             |
| scimark_sor                | 78.1 ms                                                     | 82.7 ms: 1.06x slower                                                             |
| unpickle_list              | 2.59 us                                                     | 2.74 us: 1.06x slower                                                             |
| coverage                   | 43.4 ms                                                     | 46.1 ms: 1.06x slower                                                             |
| pathlib                    | 70.9 ms                                                     | 77.1 ms: 1.09x slower                                                             |
| pickle                     | 6.64 us                                                     | 7.28 us: 1.10x slower                                                             |
| bench_mp_pool              | 63.2 ms                                                     | 69.3 ms: 1.10x slower                                                             |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.10x slower                                                             |
| telco                      | 4.06 ms                                                     | 4.63 ms: 1.14x slower                                                             |
| unpickle                   | 7.57 us                                                     | 8.70 us: 1.15x slower                                                             |
| python_startup             | 19.8 ms                                                     | 23.4 ms: 1.19x slower                                                             |
| scimark_lu                 | 62.8 ms                                                     | 78.2 ms: 1.24x slower                                                             |
| python_startup_no_site     | 16.8 ms                                                     | 21.4 ms: 1.27x slower                                                             |
| async_generators           | 177 ms                                                      | 240 ms: 1.35x slower                                                              |
| thrift                     | 494 us                                                      | 8.94 ms: 18.11x slower                                                            |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                                      |

Benchmark hidden because not significant (4): pycparser, sqlglot_optimize, pidigits, json
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x


# Memory

- memory change: unknown
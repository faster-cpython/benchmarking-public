# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mprotect_cost
- machine: windows-amd64
- commit hash: c8d6017
- commit date: 2024-03-18
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.01x slower                                                              |
| chameleon      | 4.98 ms                                                     | 4.70 ms: 1.06x faster                                                             |
| docutils       | 1.66 sec                                                    | 1.58 sec: 1.05x faster                                                            |
| tornado_http   | 89.5 ms                                                     | 83.7 ms: 1.07x faster                                                             |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none            | 291 ms                                                      | 265 ms: 1.10x faster                                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 454 ms: 1.08x faster                                                              |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 468 ms: 1.07x faster                                                              |
| async_tree_memoization_tg  | 367 ms                                                      | 346 ms: 1.06x faster                                                              |
| async_tree_none_tg         | 285 ms                                                      | 269 ms: 1.06x faster                                                              |
| async_tree_io_tg           | 771 ms                                                      | 745 ms: 1.03x faster                                                              |
| async_tree_io              | 731 ms                                                      | 717 ms: 1.02x faster                                                              |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                      |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 58.4 ms: 1.23x faster                                                             |
| float          | 56.8 ms                                                     | 48.1 ms: 1.18x faster                                                             |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                              |
| regex_compile  | 87.5 ms                                                     | 83.0 ms: 1.05x faster                                                             |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                             |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                             |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                            |
| pickle_pure_python   | 195 us                                                      | 177 us: 1.10x faster                                                              |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.9 ms: 1.05x faster                                                             |
| pickle_dict          | 18.4 us                                                     | 17.6 us: 1.05x faster                                                             |
| unpickle_pure_python | 133 us                                                      | 128 us: 1.04x faster                                                              |
| pickle_list          | 2.83 us                                                     | 2.73 us: 1.04x faster                                                             |
| json_dumps           | 5.70 ms                                                     | 5.51 ms: 1.03x faster                                                             |
| xml_etree_generate   | 55.8 ms                                                     | 54.1 ms: 1.03x faster                                                             |
| xml_etree_process    | 37.7 ms                                                     | 36.8 ms: 1.02x faster                                                             |
| pickle               | 7.43 us                                                     | 7.28 us: 1.02x faster                                                             |
| json_loads           | 13.9 us                                                     | 13.7 us: 1.02x faster                                                             |
| xml_etree_parse      | 93.0 ms                                                     | 91.7 ms: 1.01x faster                                                             |
| unpickle             | 8.18 us                                                     | 8.70 us: 1.06x slower                                                             |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                      |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 23.4 ms: 1.20x slower                                                             |
| python_startup_no_site | 16.2 ms                                                     | 21.4 ms: 1.31x slower                                                             |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.48 ms: 1.29x faster                                                             |
| django_template | 22.9 ms                                                     | 21.9 ms: 1.05x faster                                                             |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 95.1 us                                                     | 70.3 us: 1.35x faster                                                             |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.33x faster                                                             |
| spectral_norm              | 66.9 ms                                                     | 50.7 ms: 1.32x faster                                                             |
| mako                       | 7.09 ms                                                     | 5.48 ms: 1.29x faster                                                             |
| nbody                      | 71.9 ms                                                     | 58.4 ms: 1.23x faster                                                             |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.74 sec: 1.21x faster                                                            |
| float                      | 56.8 ms                                                     | 48.1 ms: 1.18x faster                                                             |
| mypy2                      | 509 ms                                                      | 435 ms: 1.17x faster                                                              |
| fannkuch                   | 247 ms                                                      | 213 ms: 1.16x faster                                                              |
| tomli_loads                | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                            |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.24 ms: 1.14x faster                                                             |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                             |
| generators                 | 22.5 ms                                                     | 20.2 ms: 1.11x faster                                                             |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                              |
| pickle_pure_python         | 195 us                                                      | 177 us: 1.10x faster                                                              |
| chaos                      | 43.3 ms                                                     | 39.4 ms: 1.10x faster                                                             |
| async_tree_none            | 291 ms                                                      | 265 ms: 1.10x faster                                                              |
| logging_silent             | 60.5 ns                                                     | 55.5 ns: 1.09x faster                                                             |
| deepcopy_memo              | 23.7 us                                                     | 21.8 us: 1.09x faster                                                             |
| coroutines                 | 14.3 ms                                                     | 13.1 ms: 1.09x faster                                                             |
| deepcopy_reduce            | 2.09 us                                                     | 1.93 us: 1.09x faster                                                             |
| scimark_fft                | 184 ms                                                      | 170 ms: 1.08x faster                                                              |
| logging_simple             | 6.28 us                                                     | 5.79 us: 1.08x faster                                                             |
| pprint_pformat             | 1.05 sec                                                    | 969 ms: 1.08x faster                                                              |
| pprint_safe_repr           | 513 ms                                                      | 475 ms: 1.08x faster                                                              |
| dulwich_log                | 44.3 ms                                                     | 41.0 ms: 1.08x faster                                                             |
| raytrace                   | 192 ms                                                      | 178 ms: 1.08x faster                                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 454 ms: 1.08x faster                                                              |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 468 ms: 1.07x faster                                                              |
| deepcopy                   | 238 us                                                      | 222 us: 1.07x faster                                                              |
| logging_format             | 6.72 us                                                     | 6.28 us: 1.07x faster                                                             |
| tornado_http               | 89.5 ms                                                     | 83.7 ms: 1.07x faster                                                             |
| crypto_pyaes               | 48.5 ms                                                     | 45.3 ms: 1.07x faster                                                             |
| sqlglot_normalize          | 187 ms                                                      | 176 ms: 1.06x faster                                                              |
| sympy_str                  | 175 ms                                                      | 165 ms: 1.06x faster                                                              |
| async_tree_memoization_tg  | 367 ms                                                      | 346 ms: 1.06x faster                                                              |
| async_tree_none_tg         | 285 ms                                                      | 269 ms: 1.06x faster                                                              |
| sympy_sum                  | 91.5 ms                                                     | 86.3 ms: 1.06x faster                                                             |
| deltablue                  | 2.16 ms                                                     | 2.04 ms: 1.06x faster                                                             |
| chameleon                  | 4.98 ms                                                     | 4.70 ms: 1.06x faster                                                             |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.5 ms: 1.05x faster                                                             |
| regex_compile              | 87.5 ms                                                     | 83.0 ms: 1.05x faster                                                             |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.9 ms: 1.05x faster                                                             |
| docutils                   | 1.66 sec                                                    | 1.58 sec: 1.05x faster                                                            |
| pickle_dict                | 18.4 us                                                     | 17.6 us: 1.05x faster                                                             |
| django_template            | 22.9 ms                                                     | 21.9 ms: 1.05x faster                                                             |
| bench_thread_pool          | 857 us                                                      | 819 us: 1.05x faster                                                              |
| pyflate                    | 295 ms                                                      | 282 ms: 1.04x faster                                                              |
| pathlib                    | 80.5 ms                                                     | 77.1 ms: 1.04x faster                                                             |
| unpickle_pure_python       | 133 us                                                      | 128 us: 1.04x faster                                                              |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                             |
| nqueens                    | 62.8 ms                                                     | 60.6 ms: 1.04x faster                                                             |
| pickle_list                | 2.83 us                                                     | 2.73 us: 1.04x faster                                                             |
| sqlglot_parse              | 804 us                                                      | 777 us: 1.04x faster                                                              |
| async_tree_io_tg           | 771 ms                                                      | 745 ms: 1.03x faster                                                              |
| json_dumps                 | 5.70 ms                                                     | 5.51 ms: 1.03x faster                                                             |
| xml_etree_generate         | 55.8 ms                                                     | 54.1 ms: 1.03x faster                                                             |
| meteor_contest             | 74.6 ms                                                     | 72.6 ms: 1.03x faster                                                             |
| richards_super             | 32.1 ms                                                     | 31.2 ms: 1.03x faster                                                             |
| xml_etree_process          | 37.7 ms                                                     | 36.8 ms: 1.02x faster                                                             |
| sqlglot_transpile          | 1.02 ms                                                     | 999 us: 1.02x faster                                                              |
| pickle                     | 7.43 us                                                     | 7.28 us: 1.02x faster                                                             |
| async_tree_io              | 731 ms                                                      | 717 ms: 1.02x faster                                                              |
| richards                   | 28.4 ms                                                     | 27.9 ms: 1.02x faster                                                             |
| json_loads                 | 13.9 us                                                     | 13.7 us: 1.02x faster                                                             |
| xml_etree_parse            | 93.0 ms                                                     | 91.7 ms: 1.01x faster                                                             |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                              |
| gc_traversal               | 1.52 ms                                                     | 1.50 ms: 1.01x faster                                                             |
| sympy_expand               | 284 ms                                                      | 285 ms: 1.00x slower                                                              |
| sympy_integrate            | 13.0 ms                                                     | 13.0 ms: 1.00x slower                                                             |
| 2to3                       | 218 ms                                                      | 221 ms: 1.01x slower                                                              |
| aiohttp                    | 884 us                                                      | 898 us: 1.01x slower                                                              |
| scimark_sor                | 78.8 ms                                                     | 82.7 ms: 1.05x slower                                                             |
| go                         | 91.6 ms                                                     | 96.8 ms: 1.06x slower                                                             |
| unpickle                   | 8.18 us                                                     | 8.70 us: 1.06x slower                                                             |
| hexiom                     | 4.10 ms                                                     | 4.36 ms: 1.06x slower                                                             |
| mdp                        | 1.37 sec                                                    | 1.46 sec: 1.06x slower                                                            |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                             |
| telco                      | 4.13 ms                                                     | 4.63 ms: 1.12x slower                                                             |
| coverage                   | 40.8 ms                                                     | 46.1 ms: 1.13x slower                                                             |
| python_startup             | 19.5 ms                                                     | 23.4 ms: 1.20x slower                                                             |
| unpack_sequence            | 37.5 ns                                                     | 46.6 ns: 1.24x slower                                                             |
| python_startup_no_site     | 16.2 ms                                                     | 21.4 ms: 1.31x slower                                                             |
| scimark_lu                 | 58.9 ms                                                     | 78.2 ms: 1.33x slower                                                             |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                      |

Benchmark hidden because not significant (9): create_gc_cycles, asyncio_tcp, unpickle_list, sqlglot_optimize, async_generators, bench_mp_pool, async_tree_memoization, json, pycparser
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240318-3.13.0a5+-c8d6017-JIT/bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x


# Memory

- memory change: unknown
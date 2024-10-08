# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0rc1
- machine: windows-amd64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 226 ms: 1.09x slower                                              |
| chameleon      | 4.80 ms                                                         | 5.10 ms: 1.06x slower                                             |
| docutils       | 1.63 sec                                                        | 1.68 sec: 1.03x slower                                            |
| html5lib       | 35.0 ms                                                         | 39.1 ms: 1.12x slower                                             |
| tornado_http   | 81.8 ms                                                         | 92.0 ms: 1.12x slower                                             |
| Geometric mean | (ref)                                                           | 1.08x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|---------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 627 ms: 1.04x slower                                              |
| async_tree_none           | 218 ms                                                          | 228 ms: 1.05x slower                                              |
| async_tree_memoization_tg | 258 ms                                                          | 272 ms: 1.05x slower                                              |
| async_tree_memoization    | 264 ms                                                          | 278 ms: 1.05x slower                                              |
| async_tree_none_tg        | 202 ms                                                          | 213 ms: 1.06x slower                                              |
| Geometric mean            | (ref)                                                           | 1.04x slower                                                      |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 49.7 ms                                                         | 50.1 ms: 1.01x slower                                             |
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                              |
| nbody          | 67.6 ms                                                         | 76.8 ms: 1.14x slower                                             |
| Geometric mean | (ref)                                                           | 1.05x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                             |
| regex_dna      | 119 ms                                                          | 123 ms: 1.04x slower                                              |
| regex_compile  | 78.0 ms                                                         | 83.9 ms: 1.08x slower                                             |
| Geometric mean | (ref)                                                           | 1.04x slower                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_parse      | 90.9 ms                                                         | 91.5 ms: 1.01x slower                                             |
| xml_etree_iterparse  | 62.3 ms                                                         | 63.0 ms: 1.01x slower                                             |
| xml_etree_generate   | 53.2 ms                                                         | 55.4 ms: 1.04x slower                                             |
| tomli_loads          | 1.35 sec                                                        | 1.42 sec: 1.05x slower                                            |
| json_dumps           | 5.61 ms                                                         | 5.90 ms: 1.05x slower                                             |
| xml_etree_process    | 36.4 ms                                                         | 38.4 ms: 1.05x slower                                             |
| pickle_pure_python   | 175 us                                                          | 194 us: 1.11x slower                                              |
| unpickle_pure_python | 122 us                                                          | 138 us: 1.13x slower                                              |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                      |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.5 ms: 1.11x slower                                             |
| python_startup_no_site | 16.2 ms                                                         | 18.4 ms: 1.14x slower                                             |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.66 ms: 1.05x slower                                             |
| django_template | 21.7 ms                                                         | 22.7 ms: 1.05x slower                                             |
| genshi_xml      | 31.6 ms                                                         | 33.2 ms: 1.05x slower                                             |
| genshi_text     | 14.4 ms                                                         | 15.3 ms: 1.07x slower                                             |
| Geometric mean  | (ref)                                                           | 1.05x slower                                                      |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|---------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float                     | 49.7 ms                                                         | 50.1 ms: 1.01x slower                                             |
| xml_etree_parse           | 90.9 ms                                                         | 91.5 ms: 1.01x slower                                             |
| pidigits                  | 150 ms                                                          | 151 ms: 1.01x slower                                              |
| raytrace                  | 162 ms                                                          | 164 ms: 1.01x slower                                              |
| spectral_norm             | 63.7 ms                                                         | 64.3 ms: 1.01x slower                                             |
| logging_format            | 6.22 us                                                         | 6.29 us: 1.01x slower                                             |
| logging_simple            | 5.78 us                                                         | 5.85 us: 1.01x slower                                             |
| xml_etree_iterparse       | 62.3 ms                                                         | 63.0 ms: 1.01x slower                                             |
| gc_traversal              | 1.55 ms                                                         | 1.58 ms: 1.02x slower                                             |
| regex_effbot              | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                             |
| coroutines                | 12.8 ms                                                         | 13.0 ms: 1.02x slower                                             |
| telco                     | 4.67 ms                                                         | 4.79 ms: 1.03x slower                                             |
| docutils                  | 1.63 sec                                                        | 1.68 sec: 1.03x slower                                            |
| create_gc_cycles          | 888 us                                                          | 917 us: 1.03x slower                                              |
| async_generators          | 223 ms                                                          | 231 ms: 1.03x slower                                              |
| async_tree_io_tg          | 605 ms                                                          | 627 ms: 1.04x slower                                              |
| regex_dna                 | 119 ms                                                          | 123 ms: 1.04x slower                                              |
| sqlglot_optimize          | 32.7 ms                                                         | 33.9 ms: 1.04x slower                                             |
| sympy_sum                 | 84.4 ms                                                         | 87.6 ms: 1.04x slower                                             |
| sqlglot_normalize         | 173 ms                                                          | 180 ms: 1.04x slower                                              |
| sympy_integrate           | 12.2 ms                                                         | 12.7 ms: 1.04x slower                                             |
| xml_etree_generate        | 53.2 ms                                                         | 55.4 ms: 1.04x slower                                             |
| crypto_pyaes              | 45.5 ms                                                         | 47.4 ms: 1.04x slower                                             |
| async_tree_none           | 218 ms                                                          | 228 ms: 1.05x slower                                              |
| mako                      | 6.36 ms                                                         | 6.66 ms: 1.05x slower                                             |
| django_template           | 21.7 ms                                                         | 22.7 ms: 1.05x slower                                             |
| tomli_loads               | 1.35 sec                                                        | 1.42 sec: 1.05x slower                                            |
| meteor_contest            | 69.9 ms                                                         | 73.3 ms: 1.05x slower                                             |
| json_dumps                | 5.61 ms                                                         | 5.90 ms: 1.05x slower                                             |
| mypy2                     | 418 ms                                                          | 439 ms: 1.05x slower                                              |
| typing_runtime_protocols  | 101 us                                                          | 106 us: 1.05x slower                                              |
| genshi_xml                | 31.6 ms                                                         | 33.2 ms: 1.05x slower                                             |
| generators                | 19.6 ms                                                         | 20.6 ms: 1.05x slower                                             |
| chaos                     | 38.4 ms                                                         | 40.4 ms: 1.05x slower                                             |
| xml_etree_process         | 36.4 ms                                                         | 38.4 ms: 1.05x slower                                             |
| async_tree_memoization_tg | 258 ms                                                          | 272 ms: 1.05x slower                                              |
| async_tree_memoization    | 264 ms                                                          | 278 ms: 1.05x slower                                              |
| comprehensions            | 10.4 us                                                         | 10.9 us: 1.05x slower                                             |
| nqueens                   | 56.7 ms                                                         | 59.8 ms: 1.06x slower                                             |
| async_tree_none_tg        | 202 ms                                                          | 213 ms: 1.06x slower                                              |
| sqlglot_transpile         | 955 us                                                          | 1.01 ms: 1.06x slower                                             |
| bench_thread_pool         | 768 us                                                          | 813 us: 1.06x slower                                              |
| logging_silent            | 52.9 ns                                                         | 56.1 ns: 1.06x slower                                             |
| deepcopy_reduce           | 1.99 us                                                         | 2.11 us: 1.06x slower                                             |
| richards                  | 26.7 ms                                                         | 28.3 ms: 1.06x slower                                             |
| sympy_str                 | 159 ms                                                          | 169 ms: 1.06x slower                                              |
| chameleon                 | 4.80 ms                                                         | 5.10 ms: 1.06x slower                                             |
| richards_super            | 30.2 ms                                                         | 32.1 ms: 1.06x slower                                             |
| genshi_text               | 14.4 ms                                                         | 15.3 ms: 1.07x slower                                             |
| pyflate                   | 279 ms                                                          | 298 ms: 1.07x slower                                              |
| sympy_expand              | 271 ms                                                          | 289 ms: 1.07x slower                                              |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.68 ms: 1.07x slower                                             |
| deltablue                 | 1.88 ms                                                         | 2.01 ms: 1.07x slower                                             |
| sqlglot_parse             | 748 us                                                          | 803 us: 1.07x slower                                              |
| regex_compile             | 78.0 ms                                                         | 83.9 ms: 1.08x slower                                             |
| pylint                    | 205 ms                                                          | 220 ms: 1.08x slower                                              |
| dulwich_log               | 38.0 ms                                                         | 41.0 ms: 1.08x slower                                             |
| pprint_safe_repr          | 474 ms                                                          | 512 ms: 1.08x slower                                              |
| deepcopy                  | 220 us                                                          | 237 us: 1.08x slower                                              |
| go                        | 82.1 ms                                                         | 88.6 ms: 1.08x slower                                             |
| scimark_lu                | 56.6 ms                                                         | 61.4 ms: 1.08x slower                                             |
| pathlib                   | 75.9 ms                                                         | 82.3 ms: 1.08x slower                                             |
| pprint_pformat            | 966 ms                                                          | 1.05 sec: 1.09x slower                                            |
| coverage                  | 42.1 ms                                                         | 45.7 ms: 1.09x slower                                             |
| scimark_sor               | 75.3 ms                                                         | 81.9 ms: 1.09x slower                                             |
| thrift                    | 8.11 ms                                                         | 8.84 ms: 1.09x slower                                             |
| 2to3                      | 207 ms                                                          | 226 ms: 1.09x slower                                              |
| hexiom                    | 3.72 ms                                                         | 4.08 ms: 1.10x slower                                             |
| bench_mp_pool             | 64.8 ms                                                         | 71.1 ms: 1.10x slower                                             |
| mdp                       | 1.31 sec                                                        | 1.44 sec: 1.10x slower                                            |
| pickle_pure_python        | 175 us                                                          | 194 us: 1.11x slower                                              |
| python_startup            | 20.3 ms                                                         | 22.5 ms: 1.11x slower                                             |
| fannkuch                  | 243 ms                                                          | 271 ms: 1.11x slower                                              |
| html5lib                  | 35.0 ms                                                         | 39.1 ms: 1.12x slower                                             |
| scimark_fft               | 171 ms                                                          | 192 ms: 1.12x slower                                              |
| tornado_http              | 81.8 ms                                                         | 92.0 ms: 1.12x slower                                             |
| deepcopy_memo             | 22.1 us                                                         | 24.9 us: 1.13x slower                                             |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.68 sec: 1.13x slower                                            |
| unpickle_pure_python      | 122 us                                                          | 138 us: 1.13x slower                                              |
| scimark_monte_carlo       | 39.1 ms                                                         | 44.4 ms: 1.13x slower                                             |
| nbody                     | 67.6 ms                                                         | 76.8 ms: 1.14x slower                                             |
| python_startup_no_site    | 16.2 ms                                                         | 18.4 ms: 1.14x slower                                             |
| asyncio_tcp               | 471 ms                                                          | 631 ms: 1.34x slower                                              |
| Geometric mean            | (ref)                                                           | 1.06x slower                                                      |

Benchmark hidden because not significant (7): json, pycparser, json_loads, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io, regex_v8
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown
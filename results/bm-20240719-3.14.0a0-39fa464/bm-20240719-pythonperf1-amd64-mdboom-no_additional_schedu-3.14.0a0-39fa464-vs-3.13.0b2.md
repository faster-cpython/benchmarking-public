# Results vs. 3.13.0b2

- fork: mdboom
- ref: no_additional_schedu
- machine: windows-amd64
- commit hash: 39fa464
- commit date: 2024-07-19
- overall geometric mean: 1.00x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 218 ms: 1.06x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.67 sec: 1.03x slower                                                     |
| html5lib       | 35.0 ms                                                         | 39.0 ms: 1.11x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 91.5 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                           | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 521 ms: 1.16x faster                                                       |
| async_tree_io             | 588 ms                                                          | 527 ms: 1.12x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 187 ms: 1.08x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 243 ms: 1.06x faster                                                       |
| async_tree_none           | 218 ms                                                          | 208 ms: 1.05x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 252 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 380 ms: 1.03x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.07x faster                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| nbody          | 67.6 ms                                                         | 68.8 ms: 1.02x slower                                                      |
| float          | 49.7 ms                                                         | 54.0 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                           | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| regex_dna      | 119 ms                                                          | 120 ms: 1.01x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 83.8 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 62.3 ms                                                         | 63.6 ms: 1.02x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 93.2 ms: 1.02x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 55.2 ms: 1.04x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 38.0 ms: 1.04x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.87 ms: 1.04x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.46 sec: 1.08x slower                                                     |
| unpickle_pure_python | 122 us                                                          | 134 us: 1.10x slower                                                       |
| pickle_pure_python   | 175 us                                                          | 198 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.7 ms: 1.07x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.0 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 23.0 ms: 1.06x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 34.0 ms: 1.08x slower                                                      |
| mako            | 6.36 ms                                                         | 6.88 ms: 1.08x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 15.6 ms: 1.08x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.07x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 507 us: 15.98x faster                                                      |
| deepcopy                  | 220 us                                                          | 174 us: 1.26x faster                                                       |
| deepcopy_memo             | 22.1 us                                                         | 18.9 us: 1.17x faster                                                      |
| async_tree_io_tg          | 605 ms                                                          | 521 ms: 1.16x faster                                                       |
| deepcopy_reduce           | 1.99 us                                                         | 1.78 us: 1.12x faster                                                      |
| async_tree_io             | 588 ms                                                          | 527 ms: 1.12x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 187 ms: 1.08x faster                                                       |
| json                      | 3.19 ms                                                         | 3.00 ms: 1.06x faster                                                      |
| async_tree_memoization_tg | 258 ms                                                          | 243 ms: 1.06x faster                                                       |
| async_tree_none           | 218 ms                                                          | 208 ms: 1.05x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 252 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 380 ms: 1.03x faster                                                       |
| scimark_lu                | 56.6 ms                                                         | 56.0 ms: 1.01x faster                                                      |
| regex_effbot              | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| pidigits                  | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| regex_dna                 | 119 ms                                                          | 120 ms: 1.01x slower                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.52 ms: 1.01x slower                                                      |
| crypto_pyaes              | 45.5 ms                                                         | 45.9 ms: 1.01x slower                                                      |
| raytrace                  | 162 ms                                                          | 164 ms: 1.01x slower                                                       |
| nqueens                   | 56.7 ms                                                         | 57.4 ms: 1.01x slower                                                      |
| telco                     | 4.67 ms                                                         | 4.74 ms: 1.02x slower                                                      |
| nbody                     | 67.6 ms                                                         | 68.8 ms: 1.02x slower                                                      |
| create_gc_cycles          | 888 us                                                          | 905 us: 1.02x slower                                                       |
| xml_etree_iterparse       | 62.3 ms                                                         | 63.6 ms: 1.02x slower                                                      |
| xml_etree_parse           | 90.9 ms                                                         | 93.2 ms: 1.02x slower                                                      |
| chaos                     | 38.4 ms                                                         | 39.3 ms: 1.02x slower                                                      |
| spectral_norm             | 63.7 ms                                                         | 65.4 ms: 1.03x slower                                                      |
| docutils                  | 1.63 sec                                                        | 1.67 sec: 1.03x slower                                                     |
| logging_format            | 6.22 us                                                         | 6.40 us: 1.03x slower                                                      |
| logging_simple            | 5.78 us                                                         | 5.95 us: 1.03x slower                                                      |
| coroutines                | 12.8 ms                                                         | 13.1 ms: 1.03x slower                                                      |
| bench_thread_pool         | 768 us                                                          | 791 us: 1.03x slower                                                       |
| sqlglot_optimize          | 32.7 ms                                                         | 33.7 ms: 1.03x slower                                                      |
| sympy_integrate           | 12.2 ms                                                         | 12.6 ms: 1.03x slower                                                      |
| sqlglot_normalize         | 173 ms                                                          | 179 ms: 1.03x slower                                                       |
| deltablue                 | 1.88 ms                                                         | 1.95 ms: 1.04x slower                                                      |
| sympy_sum                 | 84.4 ms                                                         | 87.5 ms: 1.04x slower                                                      |
| xml_etree_generate        | 53.2 ms                                                         | 55.2 ms: 1.04x slower                                                      |
| xml_etree_process         | 36.4 ms                                                         | 38.0 ms: 1.04x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 5.87 ms: 1.04x slower                                                      |
| bench_mp_pool             | 64.8 ms                                                         | 67.8 ms: 1.05x slower                                                      |
| scimark_sor               | 75.3 ms                                                         | 78.9 ms: 1.05x slower                                                      |
| meteor_contest            | 69.9 ms                                                         | 73.4 ms: 1.05x slower                                                      |
| pyflate                   | 279 ms                                                          | 293 ms: 1.05x slower                                                       |
| async_generators          | 223 ms                                                          | 235 ms: 1.05x slower                                                       |
| hexiom                    | 3.72 ms                                                         | 3.93 ms: 1.05x slower                                                      |
| 2to3                      | 207 ms                                                          | 218 ms: 1.06x slower                                                       |
| mdp                       | 1.31 sec                                                        | 1.39 sec: 1.06x slower                                                     |
| pathlib                   | 75.9 ms                                                         | 80.3 ms: 1.06x slower                                                      |
| django_template           | 21.7 ms                                                         | 23.0 ms: 1.06x slower                                                      |
| richards                  | 26.7 ms                                                         | 28.3 ms: 1.06x slower                                                      |
| comprehensions            | 10.4 us                                                         | 11.0 us: 1.06x slower                                                      |
| richards_super            | 30.2 ms                                                         | 32.0 ms: 1.06x slower                                                      |
| typing_runtime_protocols  | 101 us                                                          | 107 us: 1.07x slower                                                       |
| python_startup            | 20.3 ms                                                         | 21.7 ms: 1.07x slower                                                      |
| sympy_str                 | 159 ms                                                          | 171 ms: 1.07x slower                                                       |
| regex_compile             | 78.0 ms                                                         | 83.8 ms: 1.07x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 34.0 ms: 1.08x slower                                                      |
| sympy_expand              | 271 ms                                                          | 292 ms: 1.08x slower                                                       |
| go                        | 82.1 ms                                                         | 88.7 ms: 1.08x slower                                                      |
| mako                      | 6.36 ms                                                         | 6.88 ms: 1.08x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 15.6 ms: 1.08x slower                                                      |
| tomli_loads               | 1.35 sec                                                        | 1.46 sec: 1.08x slower                                                     |
| float                     | 49.7 ms                                                         | 54.0 ms: 1.09x slower                                                      |
| sqlglot_transpile         | 955 us                                                          | 1.04 ms: 1.09x slower                                                      |
| scimark_fft               | 171 ms                                                          | 187 ms: 1.09x slower                                                       |
| logging_silent            | 52.9 ns                                                         | 58.2 ns: 1.10x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 134 us: 1.10x slower                                                       |
| fannkuch                  | 243 ms                                                          | 269 ms: 1.10x slower                                                       |
| coverage                  | 42.1 ms                                                         | 46.5 ms: 1.10x slower                                                      |
| python_startup_no_site    | 16.2 ms                                                         | 18.0 ms: 1.11x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 830 us: 1.11x slower                                                       |
| asyncio_tcp               | 471 ms                                                          | 525 ms: 1.11x slower                                                       |
| html5lib                  | 35.0 ms                                                         | 39.0 ms: 1.11x slower                                                      |
| pprint_pformat            | 966 ms                                                          | 1.08 sec: 1.12x slower                                                     |
| tornado_http              | 81.8 ms                                                         | 91.5 ms: 1.12x slower                                                      |
| pprint_safe_repr          | 474 ms                                                          | 535 ms: 1.13x slower                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 44.2 ms: 1.13x slower                                                      |
| pickle_pure_python        | 175 us                                                          | 198 us: 1.13x slower                                                       |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.74 sec: 1.18x slower                                                     |
| Geometric mean            | (ref)                                                           | 1.00x faster                                                               |

Benchmark hidden because not significant (7): pycparser, regex_v8, json_loads, async_tree_cpu_io_mixed_tg, gc_traversal, generators, pylint
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown
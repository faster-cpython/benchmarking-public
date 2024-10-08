# Results vs. 3.13.0b2

- fork: mdboom
- ref: no_additional_schedu
- machine: windows-amd64
- commit hash: 8110f98
- commit date: 2024-07-19
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 222 ms: 1.08x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.66 sec: 1.02x slower                                                     |
| html5lib       | 35.0 ms                                                         | 38.3 ms: 1.09x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 91.4 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                           | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 535 ms: 1.13x faster                                                       |
| async_tree_io             | 588 ms                                                          | 538 ms: 1.09x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 247 ms: 1.05x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 194 ms: 1.04x faster                                                       |
| async_tree_none           | 218 ms                                                          | 213 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 382 ms: 1.02x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.04x faster                                                               |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| nbody          | 67.6 ms                                                         | 75.5 ms: 1.12x slower                                                      |
| float          | 49.7 ms                                                         | 56.0 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                           | 1.08x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                                      |
| regex_compile  | 78.0 ms                                                         | 83.3 ms: 1.07x slower                                                      |
| regex_dna      | 119 ms                                                          | 127 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.5 us: 1.02x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 93.8 ms: 1.03x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.95 ms: 1.06x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 66.2 ms: 1.06x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 57.5 ms: 1.08x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 39.9 ms: 1.10x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 199 us: 1.13x slower                                                       |
| tomli_loads          | 1.35 sec                                                        | 1.58 sec: 1.17x slower                                                     |
| unpickle_pure_python | 122 us                                                          | 145 us: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.5 ms: 1.06x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.7 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 14.4 ms                                                         | 16.0 ms: 1.11x slower                                                      |
| django_template | 21.7 ms                                                         | 24.3 ms: 1.12x slower                                                      |
| mako            | 6.36 ms                                                         | 7.54 ms: 1.19x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 37.6 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 529 us: 15.33x faster                                                      |
| deepcopy                  | 220 us                                                          | 178 us: 1.24x faster                                                       |
| async_tree_io_tg          | 605 ms                                                          | 535 ms: 1.13x faster                                                       |
| deepcopy_reduce           | 1.99 us                                                         | 1.82 us: 1.09x faster                                                      |
| async_tree_io             | 588 ms                                                          | 538 ms: 1.09x faster                                                       |
| deepcopy_memo             | 22.1 us                                                         | 20.3 us: 1.09x faster                                                      |
| async_tree_memoization_tg | 258 ms                                                          | 247 ms: 1.05x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 194 ms: 1.04x faster                                                       |
| async_tree_none           | 218 ms                                                          | 213 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 382 ms: 1.02x faster                                                       |
| pidigits                  | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| json_loads                | 14.2 us                                                         | 14.5 us: 1.02x slower                                                      |
| docutils                  | 1.63 sec                                                        | 1.66 sec: 1.02x slower                                                     |
| regex_effbot              | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                                      |
| telco                     | 4.67 ms                                                         | 4.79 ms: 1.03x slower                                                      |
| sympy_sum                 | 84.4 ms                                                         | 86.9 ms: 1.03x slower                                                      |
| xml_etree_parse           | 90.9 ms                                                         | 93.8 ms: 1.03x slower                                                      |
| bench_mp_pool             | 64.8 ms                                                         | 67.4 ms: 1.04x slower                                                      |
| sympy_integrate           | 12.2 ms                                                         | 12.8 ms: 1.04x slower                                                      |
| spectral_norm             | 63.7 ms                                                         | 66.7 ms: 1.05x slower                                                      |
| scimark_sor               | 75.3 ms                                                         | 78.9 ms: 1.05x slower                                                      |
| sqlglot_optimize          | 32.7 ms                                                         | 34.6 ms: 1.06x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 5.95 ms: 1.06x slower                                                      |
| sympy_str                 | 159 ms                                                          | 169 ms: 1.06x slower                                                       |
| richards_super            | 30.2 ms                                                         | 32.0 ms: 1.06x slower                                                      |
| bench_thread_pool         | 768 us                                                          | 815 us: 1.06x slower                                                       |
| xml_etree_iterparse       | 62.3 ms                                                         | 66.2 ms: 1.06x slower                                                      |
| python_startup            | 20.3 ms                                                         | 21.5 ms: 1.06x slower                                                      |
| pathlib                   | 75.9 ms                                                         | 80.6 ms: 1.06x slower                                                      |
| sympy_expand              | 271 ms                                                          | 288 ms: 1.06x slower                                                       |
| mdp                       | 1.31 sec                                                        | 1.40 sec: 1.06x slower                                                     |
| raytrace                  | 162 ms                                                          | 173 ms: 1.06x slower                                                       |
| regex_compile             | 78.0 ms                                                         | 83.3 ms: 1.07x slower                                                      |
| regex_dna                 | 119 ms                                                          | 127 ms: 1.07x slower                                                       |
| richards                  | 26.7 ms                                                         | 28.5 ms: 1.07x slower                                                      |
| sqlglot_normalize         | 173 ms                                                          | 185 ms: 1.07x slower                                                       |
| logging_format            | 6.22 us                                                         | 6.66 us: 1.07x slower                                                      |
| logging_simple            | 5.78 us                                                         | 6.20 us: 1.07x slower                                                      |
| 2to3                      | 207 ms                                                          | 222 ms: 1.08x slower                                                       |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.60 sec: 1.08x slower                                                     |
| nqueens                   | 56.7 ms                                                         | 61.2 ms: 1.08x slower                                                      |
| xml_etree_generate        | 53.2 ms                                                         | 57.5 ms: 1.08x slower                                                      |
| pyflate                   | 279 ms                                                          | 302 ms: 1.08x slower                                                       |
| go                        | 82.1 ms                                                         | 89.2 ms: 1.09x slower                                                      |
| crypto_pyaes              | 45.5 ms                                                         | 49.5 ms: 1.09x slower                                                      |
| async_generators          | 223 ms                                                          | 244 ms: 1.09x slower                                                       |
| python_startup_no_site    | 16.2 ms                                                         | 17.7 ms: 1.09x slower                                                      |
| html5lib                  | 35.0 ms                                                         | 38.3 ms: 1.09x slower                                                      |
| chaos                     | 38.4 ms                                                         | 41.9 ms: 1.09x slower                                                      |
| xml_etree_process         | 36.4 ms                                                         | 39.9 ms: 1.10x slower                                                      |
| typing_runtime_protocols  | 101 us                                                          | 111 us: 1.10x slower                                                       |
| coroutines                | 12.8 ms                                                         | 14.0 ms: 1.10x slower                                                      |
| meteor_contest            | 69.9 ms                                                         | 76.8 ms: 1.10x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 62.2 ms: 1.10x slower                                                      |
| coverage                  | 42.1 ms                                                         | 46.4 ms: 1.10x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 2.08 ms: 1.10x slower                                                      |
| generators                | 19.6 ms                                                         | 21.7 ms: 1.11x slower                                                      |
| asyncio_tcp               | 471 ms                                                          | 522 ms: 1.11x slower                                                       |
| hexiom                    | 3.72 ms                                                         | 4.13 ms: 1.11x slower                                                      |
| comprehensions            | 10.4 us                                                         | 11.5 us: 1.11x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 16.0 ms: 1.11x slower                                                      |
| tornado_http              | 81.8 ms                                                         | 91.4 ms: 1.12x slower                                                      |
| nbody                     | 67.6 ms                                                         | 75.5 ms: 1.12x slower                                                      |
| django_template           | 21.7 ms                                                         | 24.3 ms: 1.12x slower                                                      |
| pprint_pformat            | 966 ms                                                          | 1.09 sec: 1.13x slower                                                     |
| float                     | 49.7 ms                                                         | 56.0 ms: 1.13x slower                                                      |
| pprint_safe_repr          | 474 ms                                                          | 534 ms: 1.13x slower                                                       |
| sqlglot_transpile         | 955 us                                                          | 1.08 ms: 1.13x slower                                                      |
| pickle_pure_python        | 175 us                                                          | 199 us: 1.13x slower                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.86 ms: 1.14x slower                                                      |
| logging_silent            | 52.9 ns                                                         | 60.6 ns: 1.15x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 861 us: 1.15x slower                                                       |
| fannkuch                  | 243 ms                                                          | 282 ms: 1.16x slower                                                       |
| tomli_loads               | 1.35 sec                                                        | 1.58 sec: 1.17x slower                                                     |
| mako                      | 6.36 ms                                                         | 7.54 ms: 1.19x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 37.6 ms: 1.19x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 145 us: 1.19x slower                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 46.6 ms: 1.19x slower                                                      |
| scimark_fft               | 171 ms                                                          | 204 ms: 1.19x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (8): json, regex_v8, async_tree_memoization, pycparser, create_gc_cycles, gc_traversal, async_tree_cpu_io_mixed_tg, pylint
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown
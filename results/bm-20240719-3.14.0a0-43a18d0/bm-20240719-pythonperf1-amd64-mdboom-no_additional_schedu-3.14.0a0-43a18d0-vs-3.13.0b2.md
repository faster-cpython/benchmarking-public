# Results vs. 3.13.0b2

- fork: mdboom
- ref: no_additional_schedu
- machine: windows-amd64
- commit hash: 43a18d0
- commit date: 2024-07-19
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 226 ms: 1.09x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.70 sec: 1.05x slower                                                     |
| html5lib       | 35.0 ms                                                         | 40.2 ms: 1.15x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 91.8 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                           | 1.10x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 538 ms: 1.13x faster                                                       |
| async_tree_io             | 588 ms                                                          | 546 ms: 1.08x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 246 ms: 1.05x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 193 ms: 1.05x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.04x faster                                                               |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 49.7 ms                                                         | 56.7 ms: 1.14x slower                                                      |
| nbody          | 67.6 ms                                                         | 77.8 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                           | 1.09x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 116 ms: 1.03x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| regex_compile  | 78.0 ms                                                         | 89.7 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.6 us: 1.03x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 94.2 ms: 1.04x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.9 ms: 1.06x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.13 ms: 1.09x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 58.3 ms: 1.10x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 41.3 ms: 1.13x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.57 sec: 1.17x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 213 us: 1.22x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 152 us: 1.25x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.5 ms: 1.06x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 24.1 ms: 1.11x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 35.9 ms: 1.14x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 16.6 ms: 1.15x slower                                                      |
| mako            | 6.36 ms                                                         | 7.52 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 533 us: 15.20x faster                                                      |
| deepcopy                  | 220 us                                                          | 187 us: 1.17x faster                                                       |
| async_tree_io_tg          | 605 ms                                                          | 538 ms: 1.13x faster                                                       |
| async_tree_io             | 588 ms                                                          | 546 ms: 1.08x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 246 ms: 1.05x faster                                                       |
| deepcopy_reduce           | 1.99 us                                                         | 1.90 us: 1.05x faster                                                      |
| async_tree_none_tg        | 202 ms                                                          | 193 ms: 1.05x faster                                                       |
| regex_dna                 | 119 ms                                                          | 116 ms: 1.03x faster                                                       |
| deepcopy_memo             | 22.1 us                                                         | 21.7 us: 1.02x faster                                                      |
| regex_effbot              | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| json_loads                | 14.2 us                                                         | 14.6 us: 1.03x slower                                                      |
| xml_etree_parse           | 90.9 ms                                                         | 94.2 ms: 1.04x slower                                                      |
| telco                     | 4.67 ms                                                         | 4.86 ms: 1.04x slower                                                      |
| bench_thread_pool         | 768 us                                                          | 800 us: 1.04x slower                                                       |
| bench_mp_pool             | 64.8 ms                                                         | 67.6 ms: 1.04x slower                                                      |
| generators                | 19.6 ms                                                         | 20.4 ms: 1.04x slower                                                      |
| sympy_sum                 | 84.4 ms                                                         | 88.2 ms: 1.05x slower                                                      |
| docutils                  | 1.63 sec                                                        | 1.70 sec: 1.05x slower                                                     |
| sympy_integrate           | 12.2 ms                                                         | 12.8 ms: 1.05x slower                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 65.9 ms: 1.06x slower                                                      |
| coroutines                | 12.8 ms                                                         | 13.5 ms: 1.06x slower                                                      |
| python_startup            | 20.3 ms                                                         | 21.5 ms: 1.06x slower                                                      |
| pathlib                   | 75.9 ms                                                         | 80.5 ms: 1.06x slower                                                      |
| coverage                  | 42.1 ms                                                         | 44.9 ms: 1.07x slower                                                      |
| logging_format            | 6.22 us                                                         | 6.67 us: 1.07x slower                                                      |
| sqlglot_optimize          | 32.7 ms                                                         | 35.1 ms: 1.07x slower                                                      |
| mdp                       | 1.31 sec                                                        | 1.41 sec: 1.08x slower                                                     |
| logging_simple            | 5.78 us                                                         | 6.23 us: 1.08x slower                                                      |
| meteor_contest            | 69.9 ms                                                         | 75.5 ms: 1.08x slower                                                      |
| sqlglot_normalize         | 173 ms                                                          | 187 ms: 1.08x slower                                                       |
| nqueens                   | 56.7 ms                                                         | 61.2 ms: 1.08x slower                                                      |
| raytrace                  | 162 ms                                                          | 176 ms: 1.08x slower                                                       |
| sympy_str                 | 159 ms                                                          | 173 ms: 1.09x slower                                                       |
| 2to3                      | 207 ms                                                          | 226 ms: 1.09x slower                                                       |
| json_dumps                | 5.61 ms                                                         | 6.13 ms: 1.09x slower                                                      |
| async_generators          | 223 ms                                                          | 244 ms: 1.09x slower                                                       |
| python_startup_no_site    | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                      |
| xml_etree_generate        | 53.2 ms                                                         | 58.3 ms: 1.10x slower                                                      |
| asyncio_tcp               | 471 ms                                                          | 517 ms: 1.10x slower                                                       |
| typing_runtime_protocols  | 101 us                                                          | 111 us: 1.10x slower                                                       |
| sympy_expand              | 271 ms                                                          | 298 ms: 1.10x slower                                                       |
| pycparser                 | 754 ms                                                          | 830 ms: 1.10x slower                                                       |
| scimark_sor               | 75.3 ms                                                         | 83.2 ms: 1.10x slower                                                      |
| django_template           | 21.7 ms                                                         | 24.1 ms: 1.11x slower                                                      |
| pyflate                   | 279 ms                                                          | 313 ms: 1.12x slower                                                       |
| tornado_http              | 81.8 ms                                                         | 91.8 ms: 1.12x slower                                                      |
| crypto_pyaes              | 45.5 ms                                                         | 51.2 ms: 1.13x slower                                                      |
| chaos                     | 38.4 ms                                                         | 43.3 ms: 1.13x slower                                                      |
| spectral_norm             | 63.7 ms                                                         | 72.0 ms: 1.13x slower                                                      |
| xml_etree_process         | 36.4 ms                                                         | 41.3 ms: 1.13x slower                                                      |
| comprehensions            | 10.4 us                                                         | 11.8 us: 1.13x slower                                                      |
| go                        | 82.1 ms                                                         | 93.0 ms: 1.13x slower                                                      |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.84 ms: 1.14x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 2.14 ms: 1.14x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 35.9 ms: 1.14x slower                                                      |
| float                     | 49.7 ms                                                         | 56.7 ms: 1.14x slower                                                      |
| html5lib                  | 35.0 ms                                                         | 40.2 ms: 1.15x slower                                                      |
| regex_compile             | 78.0 ms                                                         | 89.7 ms: 1.15x slower                                                      |
| nbody                     | 67.6 ms                                                         | 77.8 ms: 1.15x slower                                                      |
| sqlglot_transpile         | 955 us                                                          | 1.10 ms: 1.15x slower                                                      |
| richards_super            | 30.2 ms                                                         | 34.8 ms: 1.15x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 16.6 ms: 1.15x slower                                                      |
| richards                  | 26.7 ms                                                         | 30.8 ms: 1.15x slower                                                      |
| pprint_pformat            | 966 ms                                                          | 1.12 sec: 1.16x slower                                                     |
| tomli_loads               | 1.35 sec                                                        | 1.57 sec: 1.17x slower                                                     |
| hexiom                    | 3.72 ms                                                         | 4.34 ms: 1.17x slower                                                      |
| pprint_safe_repr          | 474 ms                                                          | 557 ms: 1.18x slower                                                       |
| mako                      | 6.36 ms                                                         | 7.52 ms: 1.18x slower                                                      |
| logging_silent            | 52.9 ns                                                         | 62.7 ns: 1.18x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 67.2 ms: 1.19x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 891 us: 1.19x slower                                                       |
| fannkuch                  | 243 ms                                                          | 290 ms: 1.19x slower                                                       |
| scimark_fft               | 171 ms                                                          | 207 ms: 1.21x slower                                                       |
| pickle_pure_python        | 175 us                                                          | 213 us: 1.22x slower                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 48.6 ms: 1.24x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 152 us: 1.25x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (11): regex_v8, json, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none, gc_traversal, pidigits, create_gc_cycles, async_tree_cpu_io_mixed_tg, pylint, asyncio_tcp_ssl
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown
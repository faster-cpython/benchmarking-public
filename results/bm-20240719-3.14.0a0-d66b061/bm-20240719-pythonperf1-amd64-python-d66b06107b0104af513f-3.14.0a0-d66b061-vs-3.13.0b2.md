# Results vs. 3.13.0b2

- fork: python
- ref: d66b06107b0104af513f
- machine: windows-amd64
- commit hash: d66b061
- commit date: 2024-07-19
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 224 ms: 1.08x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.67 sec: 1.03x slower                                                     |
| html5lib       | 35.0 ms                                                         | 40.4 ms: 1.15x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 91.2 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 532 ms: 1.14x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 189 ms: 1.07x faster                                                       |
| async_tree_io             | 588 ms                                                          | 552 ms: 1.06x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 244 ms: 1.06x faster                                                       |
| async_tree_none           | 218 ms                                                          | 210 ms: 1.04x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.05x faster                                                               |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| float          | 49.7 ms                                                         | 55.4 ms: 1.11x slower                                                      |
| nbody          | 67.6 ms                                                         | 78.2 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.6 ms: 1.08x faster                                                      |
| regex_compile  | 78.0 ms                                                         | 85.8 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                           | 1.00x slower                                                               |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 90.9 ms                                                         | 93.0 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 64.3 ms: 1.03x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.90 ms: 1.05x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 57.2 ms: 1.08x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 39.5 ms: 1.08x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.50 sec: 1.11x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 199 us: 1.13x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 139 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.07x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.4 ms: 1.06x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.5 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 31.6 ms                                                         | 33.8 ms: 1.07x slower                                                      |
| django_template | 21.7 ms                                                         | 23.2 ms: 1.07x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 15.8 ms: 1.10x slower                                                      |
| mako            | 6.36 ms                                                         | 7.08 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.09x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 525 us: 15.45x faster                                                      |
| deepcopy                  | 220 us                                                          | 174 us: 1.26x faster                                                       |
| async_tree_io_tg          | 605 ms                                                          | 532 ms: 1.14x faster                                                       |
| deepcopy_memo             | 22.1 us                                                         | 19.6 us: 1.13x faster                                                      |
| deepcopy_reduce           | 1.99 us                                                         | 1.80 us: 1.11x faster                                                      |
| json                      | 3.19 ms                                                         | 2.94 ms: 1.09x faster                                                      |
| regex_v8                  | 15.8 ms                                                         | 14.6 ms: 1.08x faster                                                      |
| async_tree_none_tg        | 202 ms                                                          | 189 ms: 1.07x faster                                                       |
| async_tree_io             | 588 ms                                                          | 552 ms: 1.06x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 244 ms: 1.06x faster                                                       |
| async_tree_none           | 218 ms                                                          | 210 ms: 1.04x faster                                                       |
| pidigits                  | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| create_gc_cycles          | 888 us                                                          | 903 us: 1.02x slower                                                       |
| xml_etree_parse           | 90.9 ms                                                         | 93.0 ms: 1.02x slower                                                      |
| docutils                  | 1.63 sec                                                        | 1.67 sec: 1.03x slower                                                     |
| xml_etree_iterparse       | 62.3 ms                                                         | 64.3 ms: 1.03x slower                                                      |
| telco                     | 4.67 ms                                                         | 4.82 ms: 1.03x slower                                                      |
| logging_simple            | 5.78 us                                                         | 5.98 us: 1.03x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 58.6 ms: 1.03x slower                                                      |
| bench_mp_pool             | 64.8 ms                                                         | 67.1 ms: 1.04x slower                                                      |
| logging_format            | 6.22 us                                                         | 6.46 us: 1.04x slower                                                      |
| coroutines                | 12.8 ms                                                         | 13.3 ms: 1.04x slower                                                      |
| bench_thread_pool         | 768 us                                                          | 800 us: 1.04x slower                                                       |
| typing_runtime_protocols  | 101 us                                                          | 105 us: 1.04x slower                                                       |
| sqlglot_normalize         | 173 ms                                                          | 181 ms: 1.05x slower                                                       |
| sympy_integrate           | 12.2 ms                                                         | 12.8 ms: 1.05x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 5.90 ms: 1.05x slower                                                      |
| sympy_sum                 | 84.4 ms                                                         | 88.7 ms: 1.05x slower                                                      |
| python_startup            | 20.3 ms                                                         | 21.4 ms: 1.06x slower                                                      |
| meteor_contest            | 69.9 ms                                                         | 73.8 ms: 1.06x slower                                                      |
| sqlglot_optimize          | 32.7 ms                                                         | 34.6 ms: 1.06x slower                                                      |
| generators                | 19.6 ms                                                         | 20.7 ms: 1.06x slower                                                      |
| pathlib                   | 75.9 ms                                                         | 80.3 ms: 1.06x slower                                                      |
| raytrace                  | 162 ms                                                          | 172 ms: 1.06x slower                                                       |
| genshi_xml                | 31.6 ms                                                         | 33.8 ms: 1.07x slower                                                      |
| crypto_pyaes              | 45.5 ms                                                         | 48.6 ms: 1.07x slower                                                      |
| django_template           | 21.7 ms                                                         | 23.2 ms: 1.07x slower                                                      |
| nqueens                   | 56.7 ms                                                         | 60.7 ms: 1.07x slower                                                      |
| richards                  | 26.7 ms                                                         | 28.6 ms: 1.07x slower                                                      |
| comprehensions            | 10.4 us                                                         | 11.1 us: 1.07x slower                                                      |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.59 sec: 1.07x slower                                                     |
| xml_etree_generate        | 53.2 ms                                                         | 57.2 ms: 1.08x slower                                                      |
| async_generators          | 223 ms                                                          | 241 ms: 1.08x slower                                                       |
| spectral_norm             | 63.7 ms                                                         | 68.9 ms: 1.08x slower                                                      |
| sympy_str                 | 159 ms                                                          | 172 ms: 1.08x slower                                                       |
| chaos                     | 38.4 ms                                                         | 41.5 ms: 1.08x slower                                                      |
| python_startup_no_site    | 16.2 ms                                                         | 17.5 ms: 1.08x slower                                                      |
| 2to3                      | 207 ms                                                          | 224 ms: 1.08x slower                                                       |
| xml_etree_process         | 36.4 ms                                                         | 39.5 ms: 1.08x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 2.04 ms: 1.08x slower                                                      |
| pyflate                   | 279 ms                                                          | 302 ms: 1.08x slower                                                       |
| richards_super            | 30.2 ms                                                         | 32.7 ms: 1.09x slower                                                      |
| sympy_expand              | 271 ms                                                          | 294 ms: 1.09x slower                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.73 ms: 1.09x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 15.8 ms: 1.10x slower                                                      |
| regex_compile             | 78.0 ms                                                         | 85.8 ms: 1.10x slower                                                      |
| pprint_safe_repr          | 474 ms                                                          | 523 ms: 1.10x slower                                                       |
| logging_silent            | 52.9 ns                                                         | 58.4 ns: 1.10x slower                                                      |
| pprint_pformat            | 966 ms                                                          | 1.07 sec: 1.10x slower                                                     |
| sqlglot_transpile         | 955 us                                                          | 1.06 ms: 1.11x slower                                                      |
| tomli_loads               | 1.35 sec                                                        | 1.50 sec: 1.11x slower                                                     |
| go                        | 82.1 ms                                                         | 91.0 ms: 1.11x slower                                                      |
| mdp                       | 1.31 sec                                                        | 1.46 sec: 1.11x slower                                                     |
| hexiom                    | 3.72 ms                                                         | 4.14 ms: 1.11x slower                                                      |
| mako                      | 6.36 ms                                                         | 7.08 ms: 1.11x slower                                                      |
| tornado_http              | 81.8 ms                                                         | 91.2 ms: 1.11x slower                                                      |
| float                     | 49.7 ms                                                         | 55.4 ms: 1.11x slower                                                      |
| scimark_sor               | 75.3 ms                                                         | 84.4 ms: 1.12x slower                                                      |
| coverage                  | 42.1 ms                                                         | 47.3 ms: 1.12x slower                                                      |
| pycparser                 | 754 ms                                                          | 848 ms: 1.12x slower                                                       |
| pickle_pure_python        | 175 us                                                          | 199 us: 1.13x slower                                                       |
| asyncio_tcp               | 471 ms                                                          | 534 ms: 1.13x slower                                                       |
| unpickle_pure_python      | 122 us                                                          | 139 us: 1.14x slower                                                       |
| sqlglot_parse             | 748 us                                                          | 854 us: 1.14x slower                                                       |
| fannkuch                  | 243 ms                                                          | 280 ms: 1.15x slower                                                       |
| html5lib                  | 35.0 ms                                                         | 40.4 ms: 1.15x slower                                                      |
| nbody                     | 67.6 ms                                                         | 78.2 ms: 1.16x slower                                                      |
| scimark_fft               | 171 ms                                                          | 199 ms: 1.17x slower                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 46.4 ms: 1.19x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_cpu_io_mixed, regex_effbot, regex_dna, json_loads, gc_traversal, async_tree_cpu_io_mixed_tg, pylint
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown
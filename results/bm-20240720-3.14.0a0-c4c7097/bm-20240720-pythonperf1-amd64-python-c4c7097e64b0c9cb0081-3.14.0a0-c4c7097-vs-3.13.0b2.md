# Results vs. 3.13.0b2

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: windows-amd64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 223 ms: 1.08x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.68 sec: 1.04x slower                                                     |
| html5lib       | 35.0 ms                                                         | 40.2 ms: 1.15x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 91.3 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 541 ms: 1.12x faster                                                       |
| async_tree_io             | 588 ms                                                          | 556 ms: 1.06x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 245 ms: 1.06x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.03x faster                                                               |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 49.7 ms                                                         | 55.4 ms: 1.11x slower                                                      |
| nbody          | 67.6 ms                                                         | 77.3 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                           | 1.08x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                                      |
| regex_dna      | 119 ms                                                          | 126 ms: 1.06x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 86.8 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                           | 1.06x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 92.8 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 64.7 ms: 1.04x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.92 ms: 1.05x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 56.5 ms: 1.06x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 39.3 ms: 1.08x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.51 sec: 1.12x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 199 us: 1.14x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 141 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.07x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.4 ms: 1.05x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.6 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 23.0 ms: 1.06x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 16.0 ms: 1.11x slower                                                      |
| mako            | 6.36 ms                                                         | 7.11 ms: 1.12x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 36.6 ms: 1.16x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.11x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 514 us: 15.77x faster                                                      |
| deepcopy                  | 220 us                                                          | 175 us: 1.26x faster                                                       |
| deepcopy_memo             | 22.1 us                                                         | 19.6 us: 1.13x faster                                                      |
| async_tree_io_tg          | 605 ms                                                          | 541 ms: 1.12x faster                                                       |
| deepcopy_reduce           | 1.99 us                                                         | 1.81 us: 1.10x faster                                                      |
| async_tree_io             | 588 ms                                                          | 556 ms: 1.06x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 245 ms: 1.06x faster                                                       |
| json_loads                | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| create_gc_cycles          | 888 us                                                          | 903 us: 1.02x slower                                                       |
| xml_etree_parse           | 90.9 ms                                                         | 92.8 ms: 1.02x slower                                                      |
| regex_effbot              | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                                      |
| telco                     | 4.67 ms                                                         | 4.81 ms: 1.03x slower                                                      |
| docutils                  | 1.63 sec                                                        | 1.68 sec: 1.04x slower                                                     |
| logging_simple            | 5.78 us                                                         | 5.99 us: 1.04x slower                                                      |
| bench_mp_pool             | 64.8 ms                                                         | 67.1 ms: 1.04x slower                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 64.7 ms: 1.04x slower                                                      |
| sqlglot_normalize         | 173 ms                                                          | 180 ms: 1.04x slower                                                       |
| bench_thread_pool         | 768 us                                                          | 799 us: 1.04x slower                                                       |
| logging_format            | 6.22 us                                                         | 6.48 us: 1.04x slower                                                      |
| raytrace                  | 162 ms                                                          | 169 ms: 1.04x slower                                                       |
| typing_runtime_protocols  | 101 us                                                          | 105 us: 1.04x slower                                                       |
| sqlglot_optimize          | 32.7 ms                                                         | 34.2 ms: 1.04x slower                                                      |
| sympy_integrate           | 12.2 ms                                                         | 12.8 ms: 1.05x slower                                                      |
| meteor_contest            | 69.9 ms                                                         | 73.3 ms: 1.05x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 5.92 ms: 1.05x slower                                                      |
| python_startup            | 20.3 ms                                                         | 21.4 ms: 1.05x slower                                                      |
| sympy_sum                 | 84.4 ms                                                         | 89.0 ms: 1.05x slower                                                      |
| pathlib                   | 75.9 ms                                                         | 80.3 ms: 1.06x slower                                                      |
| django_template           | 21.7 ms                                                         | 23.0 ms: 1.06x slower                                                      |
| regex_dna                 | 119 ms                                                          | 126 ms: 1.06x slower                                                       |
| xml_etree_generate        | 53.2 ms                                                         | 56.5 ms: 1.06x slower                                                      |
| nqueens                   | 56.7 ms                                                         | 60.2 ms: 1.06x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 60.3 ms: 1.07x slower                                                      |
| comprehensions            | 10.4 us                                                         | 11.1 us: 1.07x slower                                                      |
| coroutines                | 12.8 ms                                                         | 13.6 ms: 1.07x slower                                                      |
| generators                | 19.6 ms                                                         | 20.9 ms: 1.07x slower                                                      |
| chaos                     | 38.4 ms                                                         | 41.1 ms: 1.07x slower                                                      |
| crypto_pyaes              | 45.5 ms                                                         | 48.9 ms: 1.07x slower                                                      |
| async_generators          | 223 ms                                                          | 240 ms: 1.07x slower                                                       |
| xml_etree_process         | 36.4 ms                                                         | 39.3 ms: 1.08x slower                                                      |
| 2to3                      | 207 ms                                                          | 223 ms: 1.08x slower                                                       |
| sympy_str                 | 159 ms                                                          | 172 ms: 1.08x slower                                                       |
| richards                  | 26.7 ms                                                         | 28.9 ms: 1.08x slower                                                      |
| python_startup_no_site    | 16.2 ms                                                         | 17.6 ms: 1.08x slower                                                      |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.72 ms: 1.09x slower                                                      |
| spectral_norm             | 63.7 ms                                                         | 69.5 ms: 1.09x slower                                                      |
| pyflate                   | 279 ms                                                          | 304 ms: 1.09x slower                                                       |
| richards_super            | 30.2 ms                                                         | 33.0 ms: 1.09x slower                                                      |
| logging_silent            | 52.9 ns                                                         | 57.9 ns: 1.09x slower                                                      |
| sympy_expand              | 271 ms                                                          | 298 ms: 1.10x slower                                                       |
| sqlglot_transpile         | 955 us                                                          | 1.05 ms: 1.10x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 2.07 ms: 1.10x slower                                                      |
| pprint_safe_repr          | 474 ms                                                          | 524 ms: 1.11x slower                                                       |
| hexiom                    | 3.72 ms                                                         | 4.12 ms: 1.11x slower                                                      |
| pprint_pformat            | 966 ms                                                          | 1.07 sec: 1.11x slower                                                     |
| go                        | 82.1 ms                                                         | 91.0 ms: 1.11x slower                                                      |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.64 sec: 1.11x slower                                                     |
| asyncio_tcp               | 471 ms                                                          | 524 ms: 1.11x slower                                                       |
| genshi_text               | 14.4 ms                                                         | 16.0 ms: 1.11x slower                                                      |
| regex_compile             | 78.0 ms                                                         | 86.8 ms: 1.11x slower                                                      |
| float                     | 49.7 ms                                                         | 55.4 ms: 1.11x slower                                                      |
| tornado_http              | 81.8 ms                                                         | 91.3 ms: 1.12x slower                                                      |
| tomli_loads               | 1.35 sec                                                        | 1.51 sec: 1.12x slower                                                     |
| mdp                       | 1.31 sec                                                        | 1.47 sec: 1.12x slower                                                     |
| mako                      | 6.36 ms                                                         | 7.11 ms: 1.12x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 847 us: 1.13x slower                                                       |
| pickle_pure_python        | 175 us                                                          | 199 us: 1.14x slower                                                       |
| nbody                     | 67.6 ms                                                         | 77.3 ms: 1.14x slower                                                      |
| html5lib                  | 35.0 ms                                                         | 40.2 ms: 1.15x slower                                                      |
| fannkuch                  | 243 ms                                                          | 280 ms: 1.15x slower                                                       |
| scimark_sor               | 75.3 ms                                                         | 86.8 ms: 1.15x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 141 us: 1.15x slower                                                       |
| genshi_xml                | 31.6 ms                                                         | 36.6 ms: 1.16x slower                                                      |
| scimark_fft               | 171 ms                                                          | 198 ms: 1.16x slower                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 47.9 ms: 1.22x slower                                                      |
| coverage                  | 42.1 ms                                                         | 79.8 ms: 1.90x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (11): json, async_tree_none_tg, async_tree_memoization, async_tree_none, pidigits, gc_traversal, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, pycparser, pylint, regex_v8
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown
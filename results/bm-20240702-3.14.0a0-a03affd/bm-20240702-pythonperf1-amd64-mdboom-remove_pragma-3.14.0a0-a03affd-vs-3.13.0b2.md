# Results vs. 3.13.0b2

- fork: mdboom
- ref: remove_pragma
- machine: windows-amd64
- commit hash: a03affd
- commit date: 2024-07-02
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 227 ms: 1.10x slower                                                |
| docutils       | 1.63 sec                                                        | 1.70 sec: 1.05x slower                                              |
| html5lib       | 35.0 ms                                                         | 40.8 ms: 1.16x slower                                               |
| tornado_http   | 81.8 ms                                                         | 82.5 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                           | 1.08x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 540 ms: 1.12x faster                                                |
| async_tree_memoization_tg | 258 ms                                                          | 245 ms: 1.05x faster                                                |
| async_tree_io             | 588 ms                                                          | 565 ms: 1.04x faster                                                |
| Geometric mean            | (ref)                                                           | 1.03x faster                                                        |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 49.7 ms                                                         | 57.8 ms: 1.16x slower                                               |
| nbody          | 67.6 ms                                                         | 86.1 ms: 1.27x slower                                               |
| Geometric mean | (ref)                                                           | 1.14x slower                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 115 ms: 1.03x faster                                                |
| regex_compile  | 78.0 ms                                                         | 92.2 ms: 1.18x slower                                               |
| Geometric mean | (ref)                                                           | 1.04x slower                                                        |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.0 us: 1.01x faster                                               |
| xml_etree_parse      | 90.9 ms                                                         | 95.6 ms: 1.05x slower                                               |
| xml_etree_iterparse  | 62.3 ms                                                         | 67.2 ms: 1.08x slower                                               |
| json_dumps           | 5.61 ms                                                         | 6.13 ms: 1.09x slower                                               |
| xml_etree_generate   | 53.2 ms                                                         | 60.2 ms: 1.13x slower                                               |
| xml_etree_process    | 36.4 ms                                                         | 41.8 ms: 1.15x slower                                               |
| tomli_loads          | 1.35 sec                                                        | 1.61 sec: 1.20x slower                                              |
| pickle_pure_python   | 175 us                                                          | 214 us: 1.22x slower                                                |
| unpickle_pure_python | 122 us                                                          | 154 us: 1.26x slower                                                |
| Geometric mean       | (ref)                                                           | 1.13x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.8 ms: 1.02x slower                                               |
| python_startup_no_site | 16.2 ms                                                         | 17.2 ms: 1.06x slower                                               |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 25.1 ms: 1.16x slower                                               |
| genshi_text     | 14.4 ms                                                         | 16.9 ms: 1.18x slower                                               |
| genshi_xml      | 31.6 ms                                                         | 38.6 ms: 1.22x slower                                               |
| mako            | 6.36 ms                                                         | 7.84 ms: 1.23x slower                                               |
| Geometric mean  | (ref)                                                           | 1.20x slower                                                        |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 546 us: 14.84x faster                                               |
| deepcopy                  | 220 us                                                          | 187 us: 1.17x faster                                                |
| async_tree_io_tg          | 605 ms                                                          | 540 ms: 1.12x faster                                                |
| json                      | 3.19 ms                                                         | 2.98 ms: 1.07x faster                                               |
| async_tree_memoization_tg | 258 ms                                                          | 245 ms: 1.05x faster                                                |
| deepcopy_reduce           | 1.99 us                                                         | 1.92 us: 1.04x faster                                               |
| async_tree_io             | 588 ms                                                          | 565 ms: 1.04x faster                                                |
| regex_dna                 | 119 ms                                                          | 115 ms: 1.03x faster                                                |
| deepcopy_memo             | 22.1 us                                                         | 21.5 us: 1.03x faster                                               |
| json_loads                | 14.2 us                                                         | 14.0 us: 1.01x faster                                               |
| gc_traversal              | 1.55 ms                                                         | 1.54 ms: 1.01x faster                                               |
| tornado_http              | 81.8 ms                                                         | 82.5 ms: 1.01x slower                                               |
| create_gc_cycles          | 888 us                                                          | 899 us: 1.01x slower                                                |
| bench_mp_pool             | 64.8 ms                                                         | 65.8 ms: 1.02x slower                                               |
| python_startup            | 20.3 ms                                                         | 20.8 ms: 1.02x slower                                               |
| asyncio_tcp               | 471 ms                                                          | 486 ms: 1.03x slower                                                |
| docutils                  | 1.63 sec                                                        | 1.70 sec: 1.05x slower                                              |
| xml_etree_parse           | 90.9 ms                                                         | 95.6 ms: 1.05x slower                                               |
| python_startup_no_site    | 16.2 ms                                                         | 17.2 ms: 1.06x slower                                               |
| telco                     | 4.67 ms                                                         | 4.97 ms: 1.06x slower                                               |
| sympy_integrate           | 12.2 ms                                                         | 13.2 ms: 1.08x slower                                               |
| xml_etree_iterparse       | 62.3 ms                                                         | 67.2 ms: 1.08x slower                                               |
| sympy_sum                 | 84.4 ms                                                         | 91.2 ms: 1.08x slower                                               |
| json_dumps                | 5.61 ms                                                         | 6.13 ms: 1.09x slower                                               |
| sqlglot_optimize          | 32.7 ms                                                         | 35.8 ms: 1.09x slower                                               |
| logging_format            | 6.22 us                                                         | 6.83 us: 1.10x slower                                               |
| 2to3                      | 207 ms                                                          | 227 ms: 1.10x slower                                                |
| sqlglot_normalize         | 173 ms                                                          | 190 ms: 1.10x slower                                                |
| logging_simple            | 5.78 us                                                         | 6.38 us: 1.10x slower                                               |
| coverage                  | 42.1 ms                                                         | 46.5 ms: 1.11x slower                                               |
| pycparser                 | 754 ms                                                          | 839 ms: 1.11x slower                                                |
| typing_runtime_protocols  | 101 us                                                          | 113 us: 1.12x slower                                                |
| meteor_contest            | 69.9 ms                                                         | 78.0 ms: 1.12x slower                                               |
| raytrace                  | 162 ms                                                          | 182 ms: 1.12x slower                                                |
| mdp                       | 1.31 sec                                                        | 1.47 sec: 1.12x slower                                              |
| sympy_str                 | 159 ms                                                          | 180 ms: 1.13x slower                                                |
| richards_super            | 30.2 ms                                                         | 34.1 ms: 1.13x slower                                               |
| xml_etree_generate        | 53.2 ms                                                         | 60.2 ms: 1.13x slower                                               |
| spectral_norm             | 63.7 ms                                                         | 72.2 ms: 1.13x slower                                               |
| richards                  | 26.7 ms                                                         | 30.3 ms: 1.13x slower                                               |
| sympy_expand              | 271 ms                                                          | 308 ms: 1.14x slower                                                |
| nqueens                   | 56.7 ms                                                         | 64.8 ms: 1.14x slower                                               |
| xml_etree_process         | 36.4 ms                                                         | 41.8 ms: 1.15x slower                                               |
| comprehensions            | 10.4 us                                                         | 11.9 us: 1.15x slower                                               |
| async_generators          | 223 ms                                                          | 257 ms: 1.15x slower                                                |
| django_template           | 21.7 ms                                                         | 25.1 ms: 1.16x slower                                               |
| coroutines                | 12.8 ms                                                         | 14.8 ms: 1.16x slower                                               |
| pyflate                   | 279 ms                                                          | 323 ms: 1.16x slower                                                |
| float                     | 49.7 ms                                                         | 57.8 ms: 1.16x slower                                               |
| chaos                     | 38.4 ms                                                         | 44.6 ms: 1.16x slower                                               |
| html5lib                  | 35.0 ms                                                         | 40.8 ms: 1.16x slower                                               |
| crypto_pyaes              | 45.5 ms                                                         | 53.0 ms: 1.16x slower                                               |
| sqlglot_transpile         | 955 us                                                          | 1.12 ms: 1.18x slower                                               |
| genshi_text               | 14.4 ms                                                         | 16.9 ms: 1.18x slower                                               |
| generators                | 19.6 ms                                                         | 23.1 ms: 1.18x slower                                               |
| regex_compile             | 78.0 ms                                                         | 92.2 ms: 1.18x slower                                               |
| deltablue                 | 1.88 ms                                                         | 2.23 ms: 1.18x slower                                               |
| pprint_pformat            | 966 ms                                                          | 1.15 sec: 1.19x slower                                              |
| pprint_safe_repr          | 474 ms                                                          | 565 ms: 1.19x slower                                                |
| go                        | 82.1 ms                                                         | 97.9 ms: 1.19x slower                                               |
| tomli_loads               | 1.35 sec                                                        | 1.61 sec: 1.20x slower                                              |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.99 ms: 1.20x slower                                               |
| logging_silent            | 52.9 ns                                                         | 63.4 ns: 1.20x slower                                               |
| scimark_lu                | 56.6 ms                                                         | 67.8 ms: 1.20x slower                                               |
| scimark_sor               | 75.3 ms                                                         | 90.4 ms: 1.20x slower                                               |
| hexiom                    | 3.72 ms                                                         | 4.48 ms: 1.20x slower                                               |
| pickle_pure_python        | 175 us                                                          | 214 us: 1.22x slower                                                |
| genshi_xml                | 31.6 ms                                                         | 38.6 ms: 1.22x slower                                               |
| sqlglot_parse             | 748 us                                                          | 919 us: 1.23x slower                                                |
| mako                      | 6.36 ms                                                         | 7.84 ms: 1.23x slower                                               |
| fannkuch                  | 243 ms                                                          | 305 ms: 1.25x slower                                                |
| unpickle_pure_python      | 122 us                                                          | 154 us: 1.26x slower                                                |
| nbody                     | 67.6 ms                                                         | 86.1 ms: 1.27x slower                                               |
| scimark_fft               | 171 ms                                                          | 220 ms: 1.29x slower                                                |
| scimark_monte_carlo       | 39.1 ms                                                         | 51.2 ms: 1.31x slower                                               |
| Geometric mean            | (ref)                                                           | 1.06x slower                                                        |

Benchmark hidden because not significant (12): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization, regex_effbot, pidigits, async_tree_none, bench_thread_pool, pathlib, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, regex_v8, pylint
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown
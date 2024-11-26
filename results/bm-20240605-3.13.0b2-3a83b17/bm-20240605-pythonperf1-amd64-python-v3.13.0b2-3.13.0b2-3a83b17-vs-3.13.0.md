# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: windows-amd64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.043x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 207 ms: 1.07x faster                                            |
| docutils       | 1.57 sec                                                    | 1.63 sec: 1.03x slower                                          |
| html5lib       | 38.9 ms                                                     | 35.0 ms: 1.11x faster                                           |
| tornado_http   | 93.0 ms                                                     | 81.8 ms: 1.14x faster                                           |
| Geometric mean | (ref)                                                       | 1.06x faster                                                    |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|---------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg | 288 ms                                                      | 258 ms: 1.12x faster                                            |
| async_tree_memoization    | 276 ms                                                      | 264 ms: 1.04x faster                                            |
| async_tree_none           | 226 ms                                                      | 218 ms: 1.04x faster                                            |
| async_tree_none_tg        | 209 ms                                                      | 202 ms: 1.03x faster                                            |
| async_tree_cpu_io_mixed   | 383 ms                                                      | 389 ms: 1.02x slower                                            |
| async_tree_io             | 521 ms                                                      | 588 ms: 1.13x slower                                            |
| async_tree_io_tg          | 518 ms                                                      | 605 ms: 1.17x slower                                            |
| Geometric mean            | (ref)                                                       | 1.01x slower                                                    |

Benchmark hidden because not significant (3): coroutines, async_generators, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 67.6 ms: 1.01x faster                                           |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                       | 1.00x faster                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.8 ms: 1.36x faster                                           |
| regex_compile  | 80.5 ms                                                     | 78.0 ms: 1.03x faster                                           |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                       | 1.08x faster                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 122 us: 1.10x faster                                            |
| pickle_pure_python   | 190 us                                                      | 175 us: 1.08x faster                                            |
| json_loads           | 15.1 us                                                     | 14.2 us: 1.07x faster                                           |
| json_dumps           | 5.92 ms                                                     | 5.61 ms: 1.05x faster                                           |
| tomli_loads          | 1.39 sec                                                    | 1.35 sec: 1.03x faster                                          |
| xml_etree_parse      | 93.6 ms                                                     | 90.9 ms: 1.03x faster                                           |
| xml_etree_process    | 37.0 ms                                                     | 36.4 ms: 1.02x faster                                           |
| xml_etree_generate   | 54.0 ms                                                     | 53.2 ms: 1.02x faster                                           |
| xml_etree_iterparse  | 61.8 ms                                                     | 62.3 ms: 1.01x slower                                           |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 20.3 ms: 1.25x faster                                           |
| python_startup_no_site | 18.1 ms                                                     | 16.2 ms: 1.12x faster                                           |
| Geometric mean         | (ref)                                                       | 1.18x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 31.6 ms: 1.12x faster                                           |
| genshi_text     | 15.6 ms                                                     | 14.4 ms: 1.08x faster                                           |
| django_template | 22.4 ms                                                     | 21.7 ms: 1.03x faster                                           |
| Geometric mean  | (ref)                                                       | 1.06x faster                                                    |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|---------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mypy2                     | 679 ms                                                      | 418 ms: 1.62x faster                                            |
| create_gc_cycles          | 1.26 ms                                                     | 888 us: 1.42x faster                                            |
| regex_v8                  | 21.4 ms                                                     | 15.8 ms: 1.36x faster                                           |
| bench_mp_pool             | 86.4 ms                                                     | 64.8 ms: 1.33x faster                                           |
| gc_traversal              | 1.97 ms                                                     | 1.55 ms: 1.27x faster                                           |
| python_startup            | 25.4 ms                                                     | 20.3 ms: 1.25x faster                                           |
| tornado_http              | 93.0 ms                                                     | 81.8 ms: 1.14x faster                                           |
| genshi_xml                | 35.5 ms                                                     | 31.6 ms: 1.12x faster                                           |
| python_startup_no_site    | 18.1 ms                                                     | 16.2 ms: 1.12x faster                                           |
| async_tree_memoization_tg | 288 ms                                                      | 258 ms: 1.12x faster                                            |
| html5lib                  | 38.9 ms                                                     | 35.0 ms: 1.11x faster                                           |
| bench_thread_pool         | 847 us                                                      | 768 us: 1.10x faster                                            |
| unpickle_pure_python      | 133 us                                                      | 122 us: 1.10x faster                                            |
| thrift                    | 8.80 ms                                                     | 8.11 ms: 1.08x faster                                           |
| genshi_text               | 15.6 ms                                                     | 14.4 ms: 1.08x faster                                           |
| coverage                  | 45.6 ms                                                     | 42.1 ms: 1.08x faster                                           |
| pickle_pure_python        | 190 us                                                      | 175 us: 1.08x faster                                            |
| sympy_expand              | 291 ms                                                      | 271 ms: 1.08x faster                                            |
| dulwich_log               | 40.8 ms                                                     | 38.0 ms: 1.07x faster                                           |
| 2to3                      | 221 ms                                                      | 207 ms: 1.07x faster                                            |
| json_loads                | 15.1 us                                                     | 14.2 us: 1.07x faster                                           |
| pathlib                   | 80.9 ms                                                     | 75.9 ms: 1.07x faster                                           |
| sympy_str                 | 169 ms                                                      | 159 ms: 1.06x faster                                            |
| go                        | 87.0 ms                                                     | 82.1 ms: 1.06x faster                                           |
| mdp                       | 1.39 sec                                                    | 1.31 sec: 1.06x faster                                          |
| deepcopy_memo             | 23.3 us                                                     | 22.1 us: 1.05x faster                                           |
| json_dumps                | 5.92 ms                                                     | 5.61 ms: 1.05x faster                                           |
| meteor_contest            | 73.5 ms                                                     | 69.9 ms: 1.05x faster                                           |
| typing_runtime_protocols  | 105 us                                                      | 101 us: 1.05x faster                                            |
| hexiom                    | 3.89 ms                                                     | 3.72 ms: 1.04x faster                                           |
| async_tree_memoization    | 276 ms                                                      | 264 ms: 1.04x faster                                            |
| scimark_monte_carlo       | 40.8 ms                                                     | 39.1 ms: 1.04x faster                                           |
| pprint_safe_repr          | 494 ms                                                      | 474 ms: 1.04x faster                                            |
| fannkuch                  | 253 ms                                                      | 243 ms: 1.04x faster                                            |
| async_tree_none           | 226 ms                                                      | 218 ms: 1.04x faster                                            |
| async_tree_none_tg        | 209 ms                                                      | 202 ms: 1.03x faster                                            |
| pprint_pformat            | 999 ms                                                      | 966 ms: 1.03x faster                                            |
| tomli_loads               | 1.39 sec                                                    | 1.35 sec: 1.03x faster                                          |
| deepcopy_reduce           | 2.06 us                                                     | 1.99 us: 1.03x faster                                           |
| regex_compile             | 80.5 ms                                                     | 78.0 ms: 1.03x faster                                           |
| logging_silent            | 54.6 ns                                                     | 52.9 ns: 1.03x faster                                           |
| django_template           | 22.4 ms                                                     | 21.7 ms: 1.03x faster                                           |
| deepcopy                  | 226 us                                                      | 220 us: 1.03x faster                                            |
| sympy_sum                 | 86.9 ms                                                     | 84.4 ms: 1.03x faster                                           |
| logging_simple            | 5.96 us                                                     | 5.78 us: 1.03x faster                                           |
| sqlglot_parse             | 771 us                                                      | 748 us: 1.03x faster                                            |
| xml_etree_parse           | 93.6 ms                                                     | 90.9 ms: 1.03x faster                                           |
| telco                     | 4.79 ms                                                     | 4.67 ms: 1.03x faster                                           |
| richards_super            | 30.9 ms                                                     | 30.2 ms: 1.02x faster                                           |
| richards                  | 27.3 ms                                                     | 26.7 ms: 1.02x faster                                           |
| sympy_integrate           | 12.5 ms                                                     | 12.2 ms: 1.02x faster                                           |
| deltablue                 | 1.92 ms                                                     | 1.88 ms: 1.02x faster                                           |
| xml_etree_process         | 37.0 ms                                                     | 36.4 ms: 1.02x faster                                           |
| pyflate                   | 283 ms                                                      | 279 ms: 1.02x faster                                            |
| xml_etree_generate        | 54.0 ms                                                     | 53.2 ms: 1.02x faster                                           |
| nbody                     | 68.4 ms                                                     | 67.6 ms: 1.01x faster                                           |
| scimark_sor               | 76.2 ms                                                     | 75.3 ms: 1.01x faster                                           |
| sqlglot_normalize         | 175 ms                                                      | 173 ms: 1.01x faster                                            |
| scimark_fft               | 172 ms                                                      | 171 ms: 1.01x faster                                            |
| sqlglot_optimize          | 32.9 ms                                                     | 32.7 ms: 1.01x faster                                           |
| logging_format            | 6.26 us                                                     | 6.22 us: 1.01x faster                                           |
| chaos                     | 38.5 ms                                                     | 38.4 ms: 1.00x faster                                           |
| xml_etree_iterparse       | 61.8 ms                                                     | 62.3 ms: 1.01x slower                                           |
| comprehensions            | 10.3 us                                                     | 10.4 us: 1.01x slower                                           |
| raytrace                  | 160 ms                                                      | 162 ms: 1.01x slower                                            |
| pidigits                  | 148 ms                                                      | 150 ms: 1.01x slower                                            |
| spectral_norm             | 62.8 ms                                                     | 63.7 ms: 1.02x slower                                           |
| async_tree_cpu_io_mixed   | 383 ms                                                      | 389 ms: 1.02x slower                                            |
| scimark_sparse_mat_mult   | 2.46 ms                                                     | 2.50 ms: 1.02x slower                                           |
| regex_dna                 | 115 ms                                                      | 119 ms: 1.03x slower                                            |
| docutils                  | 1.57 sec                                                    | 1.63 sec: 1.03x slower                                          |
| scimark_lu                | 53.0 ms                                                     | 56.6 ms: 1.07x slower                                           |
| pycparser                 | 683 ms                                                      | 754 ms: 1.10x slower                                            |
| async_tree_io             | 521 ms                                                      | 588 ms: 1.13x slower                                            |
| async_tree_io_tg          | 518 ms                                                      | 605 ms: 1.17x slower                                            |
| Geometric mean            | (ref)                                                       | 1.05x faster                                                    |

Benchmark hidden because not significant (13): pylint, float, chameleon, sqlglot_transpile, coroutines, json, nqueens, async_generators, mako, crypto_pyaes, generators, regex_effbot, async_tree_cpu_io_mixed_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.043x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown
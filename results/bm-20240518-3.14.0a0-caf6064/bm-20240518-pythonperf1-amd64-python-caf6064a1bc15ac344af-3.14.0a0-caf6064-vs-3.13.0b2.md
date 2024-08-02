# Results vs. 3.13.0b2

- fork: python
- ref: caf6064a1bc15ac344af
- machine: windows-amd64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.02x faster
- HPT reliability: 97.39%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.63 sec                                                        | 1.60 sec: 1.01x faster                                                     |
| html5lib       | 35.0 ms                                                         | 35.6 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                           | 1.00x slower                                                               |

Benchmark hidden because not significant (3): 2to3, chameleon, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_io, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 69.4 ms: 1.03x slower                                                      |
| float          | 49.7 ms                                                         | 51.2 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_v8, regex_effbot, regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 13.9 us: 1.02x faster                                                      |
| json_dumps           | 5.61 ms                                                         | 5.57 ms: 1.01x faster                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 52.9 ms: 1.01x faster                                                      |
| pickle_dict          | 18.1 us                                                         | 18.2 us: 1.00x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 176 us: 1.00x slower                                                       |
| tomli_loads          | 1.35 sec                                                        | 1.36 sec: 1.01x slower                                                     |
| xml_etree_iterparse  | 62.3 ms                                                         | 62.8 ms: 1.01x slower                                                      |
| unpickle             | 8.40 us                                                         | 8.56 us: 1.02x slower                                                      |
| pickle               | 7.11 us                                                         | 7.25 us: 1.02x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 126 us: 1.03x slower                                                       |
| unpickle_list        | 2.62 us                                                         | 2.81 us: 1.07x slower                                                      |
| pickle_list          | 2.90 us                                                         | 3.23 us: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.0 ms: 1.02x faster                                                      |
| python_startup_no_site | 16.2 ms                                                         | 16.4 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.00x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 21.8 ms: 1.01x slower                                                      |
| mako            | 6.36 ms                                                         | 6.53 ms: 1.03x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 14.8 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 489 us: 16.59x faster                                                      |
| json                     | 3.19 ms                                                         | 3.01 ms: 1.06x faster                                                      |
| logging_format           | 6.22 us                                                         | 6.08 us: 1.02x faster                                                      |
| logging_simple           | 5.78 us                                                         | 5.67 us: 1.02x faster                                                      |
| json_loads               | 14.2 us                                                         | 13.9 us: 1.02x faster                                                      |
| python_startup           | 20.3 ms                                                         | 20.0 ms: 1.02x faster                                                      |
| deepcopy_reduce          | 1.99 us                                                         | 1.97 us: 1.02x faster                                                      |
| scimark_lu               | 56.6 ms                                                         | 55.8 ms: 1.01x faster                                                      |
| docutils                 | 1.63 sec                                                        | 1.60 sec: 1.01x faster                                                     |
| richards_super           | 30.2 ms                                                         | 29.8 ms: 1.01x faster                                                      |
| typing_runtime_protocols | 101 us                                                          | 99.7 us: 1.01x faster                                                      |
| json_dumps               | 5.61 ms                                                         | 5.57 ms: 1.01x faster                                                      |
| xml_etree_generate       | 53.2 ms                                                         | 52.9 ms: 1.01x faster                                                      |
| sympy_sum                | 84.4 ms                                                         | 83.9 ms: 1.01x faster                                                      |
| richards                 | 26.7 ms                                                         | 26.6 ms: 1.01x faster                                                      |
| pickle_dict              | 18.1 us                                                         | 18.2 us: 1.00x slower                                                      |
| pickle_pure_python       | 175 us                                                          | 176 us: 1.00x slower                                                       |
| sympy_integrate          | 12.2 ms                                                         | 12.3 ms: 1.00x slower                                                      |
| django_template          | 21.7 ms                                                         | 21.8 ms: 1.01x slower                                                      |
| tomli_loads              | 1.35 sec                                                        | 1.36 sec: 1.01x slower                                                     |
| xml_etree_iterparse      | 62.3 ms                                                         | 62.8 ms: 1.01x slower                                                      |
| sqlglot_parse            | 748 us                                                          | 754 us: 1.01x slower                                                       |
| nqueens                  | 56.7 ms                                                         | 57.1 ms: 1.01x slower                                                      |
| sqlglot_transpile        | 955 us                                                          | 963 us: 1.01x slower                                                       |
| chaos                    | 38.4 ms                                                         | 38.7 ms: 1.01x slower                                                      |
| logging_silent           | 52.9 ns                                                         | 53.6 ns: 1.01x slower                                                      |
| hexiom                   | 3.72 ms                                                         | 3.77 ms: 1.01x slower                                                      |
| python_startup_no_site   | 16.2 ms                                                         | 16.4 ms: 1.01x slower                                                      |
| sqlite_synth             | 1.60 us                                                         | 1.62 us: 1.01x slower                                                      |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.54 ms: 1.02x slower                                                      |
| sympy_str                | 159 ms                                                          | 162 ms: 1.02x slower                                                       |
| html5lib                 | 35.0 ms                                                         | 35.6 ms: 1.02x slower                                                      |
| bench_mp_pool            | 64.8 ms                                                         | 66.0 ms: 1.02x slower                                                      |
| unpickle                 | 8.40 us                                                         | 8.56 us: 1.02x slower                                                      |
| pickle                   | 7.11 us                                                         | 7.25 us: 1.02x slower                                                      |
| spectral_norm            | 63.7 ms                                                         | 65.1 ms: 1.02x slower                                                      |
| async_generators         | 223 ms                                                          | 228 ms: 1.02x slower                                                       |
| crypto_pyaes             | 45.5 ms                                                         | 46.5 ms: 1.02x slower                                                      |
| pprint_safe_repr         | 474 ms                                                          | 485 ms: 1.02x slower                                                       |
| pprint_pformat           | 966 ms                                                          | 989 ms: 1.02x slower                                                       |
| pyflate                  | 279 ms                                                          | 286 ms: 1.02x slower                                                       |
| scimark_sor              | 75.3 ms                                                         | 77.3 ms: 1.03x slower                                                      |
| nbody                    | 67.6 ms                                                         | 69.4 ms: 1.03x slower                                                      |
| mako                     | 6.36 ms                                                         | 6.53 ms: 1.03x slower                                                      |
| go                       | 82.1 ms                                                         | 84.3 ms: 1.03x slower                                                      |
| mdp                      | 1.31 sec                                                        | 1.35 sec: 1.03x slower                                                     |
| generators               | 19.6 ms                                                         | 20.1 ms: 1.03x slower                                                      |
| deltablue                | 1.88 ms                                                         | 1.94 ms: 1.03x slower                                                      |
| unpickle_pure_python     | 122 us                                                          | 126 us: 1.03x slower                                                       |
| float                    | 49.7 ms                                                         | 51.2 ms: 1.03x slower                                                      |
| genshi_text              | 14.4 ms                                                         | 14.8 ms: 1.03x slower                                                      |
| deepcopy_memo            | 22.1 us                                                         | 23.0 us: 1.04x slower                                                      |
| pathlib                  | 75.9 ms                                                         | 79.2 ms: 1.04x slower                                                      |
| bench_thread_pool        | 768 us                                                          | 804 us: 1.05x slower                                                       |
| meteor_contest           | 69.9 ms                                                         | 73.4 ms: 1.05x slower                                                      |
| scimark_monte_carlo      | 39.1 ms                                                         | 41.1 ms: 1.05x slower                                                      |
| fannkuch                 | 243 ms                                                          | 256 ms: 1.05x slower                                                       |
| coverage                 | 42.1 ms                                                         | 44.5 ms: 1.06x slower                                                      |
| scimark_fft              | 171 ms                                                          | 181 ms: 1.06x slower                                                       |
| unpickle_list            | 2.62 us                                                         | 2.81 us: 1.07x slower                                                      |
| pickle_list              | 2.90 us                                                         | 3.23 us: 1.11x slower                                                      |
| Geometric mean           | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (34): regex_v8, pycparser, async_tree_memoization_tg, async_tree_io, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io_tg, raytrace, xml_etree_parse, genshi_xml, deepcopy, regex_effbot, gc_traversal, sqlglot_normalize, chameleon, regex_dna, flaskblogging, sympy_expand, regex_compile, xml_etree_process, create_gc_cycles, sqlglot_optimize, 2to3, telco, pidigits, coroutines, pylint, async_tree_cpu_io_mixed_tg, comprehensions, tornado_http, asyncio_tcp_ssl, asyncio_tcp, async_tree_none_tg
Ignored benchmarks (3) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, dulwich_log, mypy2

# HPT report

- Reliability score: 97.39% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
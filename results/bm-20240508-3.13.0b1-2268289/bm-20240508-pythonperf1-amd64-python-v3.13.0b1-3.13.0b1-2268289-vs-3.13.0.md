# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b1
- machine: windows-amd64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.039x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 212 ms: 1.04x faster                                            |
| chameleon      | 4.82 ms                                                     | 4.75 ms: 1.01x faster                                           |
| docutils       | 1.57 sec                                                    | 1.64 sec: 1.04x slower                                          |
| html5lib       | 38.9 ms                                                     | 35.0 ms: 1.11x faster                                           |
| tornado_http   | 93.0 ms                                                     | 82.5 ms: 1.13x faster                                           |
| Geometric mean | (ref)                                                       | 1.05x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|---------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg | 288 ms                                                      | 267 ms: 1.08x faster                                            |
| async_tree_memoization    | 276 ms                                                      | 266 ms: 1.04x faster                                            |
| async_tree_none           | 226 ms                                                      | 219 ms: 1.03x faster                                            |
| coroutines                | 12.8 ms                                                     | 12.6 ms: 1.01x faster                                           |
| async_generators          | 223 ms                                                      | 225 ms: 1.01x slower                                            |
| async_tree_io             | 521 ms                                                      | 582 ms: 1.12x slower                                            |
| async_tree_io_tg          | 518 ms                                                      | 604 ms: 1.17x slower                                            |
| Geometric mean            | (ref)                                                       | 1.02x slower                                                    |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 49.9 ms                                                     | 48.5 ms: 1.03x faster                                           |
| nbody          | 68.4 ms                                                     | 67.1 ms: 1.02x faster                                           |
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                       | 1.02x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.3 ms: 1.50x faster                                           |
| regex_compile  | 80.5 ms                                                     | 78.5 ms: 1.03x faster                                           |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                       | 1.11x faster                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 13.7 us: 1.10x faster                                           |
| pickle_pure_python   | 190 us                                                      | 177 us: 1.07x faster                                            |
| json_dumps           | 5.92 ms                                                     | 5.59 ms: 1.06x faster                                           |
| unpickle_pure_python | 133 us                                                      | 127 us: 1.05x faster                                            |
| xml_etree_parse      | 93.6 ms                                                     | 90.0 ms: 1.04x faster                                           |
| tomli_loads          | 1.39 sec                                                    | 1.37 sec: 1.02x faster                                          |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                    |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 20.4 ms: 1.25x faster                                           |
| python_startup_no_site | 18.1 ms                                                     | 16.5 ms: 1.10x faster                                           |
| Geometric mean         | (ref)                                                       | 1.17x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 32.2 ms: 1.10x faster                                           |
| genshi_text     | 15.6 ms                                                     | 14.7 ms: 1.06x faster                                           |
| django_template | 22.4 ms                                                     | 21.5 ms: 1.04x faster                                           |
| mako            | 6.35 ms                                                     | 6.28 ms: 1.01x faster                                           |
| Geometric mean  | (ref)                                                       | 1.05x faster                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|---------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mypy2                     | 679 ms                                                      | 427 ms: 1.59x faster                                            |
| regex_v8                  | 21.4 ms                                                     | 14.3 ms: 1.50x faster                                           |
| create_gc_cycles          | 1.26 ms                                                     | 893 us: 1.41x faster                                            |
| bench_mp_pool             | 86.4 ms                                                     | 65.3 ms: 1.32x faster                                           |
| gc_traversal              | 1.97 ms                                                     | 1.55 ms: 1.27x faster                                           |
| python_startup            | 25.4 ms                                                     | 20.4 ms: 1.25x faster                                           |
| tornado_http              | 93.0 ms                                                     | 82.5 ms: 1.13x faster                                           |
| html5lib                  | 38.9 ms                                                     | 35.0 ms: 1.11x faster                                           |
| json_loads                | 15.1 us                                                     | 13.7 us: 1.10x faster                                           |
| python_startup_no_site    | 18.1 ms                                                     | 16.5 ms: 1.10x faster                                           |
| genshi_xml                | 35.5 ms                                                     | 32.2 ms: 1.10x faster                                           |
| json                      | 3.19 ms                                                     | 2.93 ms: 1.09x faster                                           |
| async_tree_memoization_tg | 288 ms                                                      | 267 ms: 1.08x faster                                            |
| pickle_pure_python        | 190 us                                                      | 177 us: 1.07x faster                                            |
| thrift                    | 8.80 ms                                                     | 8.23 ms: 1.07x faster                                           |
| bench_thread_pool         | 847 us                                                      | 793 us: 1.07x faster                                            |
| sympy_expand              | 291 ms                                                      | 275 ms: 1.06x faster                                            |
| genshi_text               | 15.6 ms                                                     | 14.7 ms: 1.06x faster                                           |
| json_dumps                | 5.92 ms                                                     | 5.59 ms: 1.06x faster                                           |
| mdp                       | 1.39 sec                                                    | 1.31 sec: 1.06x faster                                          |
| logging_silent            | 54.6 ns                                                     | 51.7 ns: 1.06x faster                                           |
| unpickle_pure_python      | 133 us                                                      | 127 us: 1.05x faster                                            |
| generators                | 19.5 ms                                                     | 18.6 ms: 1.05x faster                                           |
| 2to3                      | 221 ms                                                      | 212 ms: 1.04x faster                                            |
| django_template           | 22.4 ms                                                     | 21.5 ms: 1.04x faster                                           |
| raytrace                  | 160 ms                                                      | 154 ms: 1.04x faster                                            |
| deepcopy_reduce           | 2.06 us                                                     | 1.98 us: 1.04x faster                                           |
| sympy_str                 | 169 ms                                                      | 162 ms: 1.04x faster                                            |
| xml_etree_parse           | 93.6 ms                                                     | 90.0 ms: 1.04x faster                                           |
| fannkuch                  | 253 ms                                                      | 244 ms: 1.04x faster                                            |
| async_tree_memoization    | 276 ms                                                      | 266 ms: 1.04x faster                                            |
| hexiom                    | 3.89 ms                                                     | 3.76 ms: 1.04x faster                                           |
| richards_super            | 30.9 ms                                                     | 29.9 ms: 1.03x faster                                           |
| go                        | 87.0 ms                                                     | 84.3 ms: 1.03x faster                                           |
| meteor_contest            | 73.5 ms                                                     | 71.3 ms: 1.03x faster                                           |
| dulwich_log               | 40.8 ms                                                     | 39.6 ms: 1.03x faster                                           |
| float                     | 49.9 ms                                                     | 48.5 ms: 1.03x faster                                           |
| async_tree_none           | 226 ms                                                      | 219 ms: 1.03x faster                                            |
| richards                  | 27.3 ms                                                     | 26.6 ms: 1.03x faster                                           |
| logging_simple            | 5.96 us                                                     | 5.80 us: 1.03x faster                                           |
| pprint_safe_repr          | 494 ms                                                      | 481 ms: 1.03x faster                                            |
| regex_compile             | 80.5 ms                                                     | 78.5 ms: 1.03x faster                                           |
| typing_runtime_protocols  | 105 us                                                      | 103 us: 1.02x faster                                            |
| sqlglot_parse             | 771 us                                                      | 754 us: 1.02x faster                                            |
| nbody                     | 68.4 ms                                                     | 67.1 ms: 1.02x faster                                           |
| sympy_sum                 | 86.9 ms                                                     | 85.2 ms: 1.02x faster                                           |
| pprint_pformat            | 999 ms                                                      | 982 ms: 1.02x faster                                            |
| tomli_loads               | 1.39 sec                                                    | 1.37 sec: 1.02x faster                                          |
| sqlglot_normalize         | 175 ms                                                      | 172 ms: 1.02x faster                                            |
| spectral_norm             | 62.8 ms                                                     | 61.9 ms: 1.01x faster                                           |
| chameleon                 | 4.82 ms                                                     | 4.75 ms: 1.01x faster                                           |
| telco                     | 4.79 ms                                                     | 4.72 ms: 1.01x faster                                           |
| deepcopy                  | 226 us                                                      | 223 us: 1.01x faster                                            |
| mako                      | 6.35 ms                                                     | 6.28 ms: 1.01x faster                                           |
| coroutines                | 12.8 ms                                                     | 12.6 ms: 1.01x faster                                           |
| pathlib                   | 80.9 ms                                                     | 80.1 ms: 1.01x faster                                           |
| pyflate                   | 283 ms                                                      | 280 ms: 1.01x faster                                            |
| nqueens                   | 56.7 ms                                                     | 56.2 ms: 1.01x faster                                           |
| deltablue                 | 1.92 ms                                                     | 1.90 ms: 1.01x faster                                           |
| deepcopy_memo             | 23.3 us                                                     | 23.1 us: 1.01x faster                                           |
| pidigits                  | 148 ms                                                      | 147 ms: 1.01x faster                                            |
| scimark_monte_carlo       | 40.8 ms                                                     | 40.5 ms: 1.01x faster                                           |
| chaos                     | 38.5 ms                                                     | 38.3 ms: 1.01x faster                                           |
| logging_format            | 6.26 us                                                     | 6.22 us: 1.01x faster                                           |
| coverage                  | 45.6 ms                                                     | 45.3 ms: 1.01x faster                                           |
| scimark_sor               | 76.2 ms                                                     | 75.9 ms: 1.00x faster                                           |
| async_generators          | 223 ms                                                      | 225 ms: 1.01x slower                                            |
| sqlglot_transpile         | 956 us                                                      | 962 us: 1.01x slower                                            |
| scimark_fft               | 172 ms                                                      | 175 ms: 1.01x slower                                            |
| regex_dna                 | 115 ms                                                      | 118 ms: 1.02x slower                                            |
| scimark_sparse_mat_mult   | 2.46 ms                                                     | 2.53 ms: 1.03x slower                                           |
| crypto_pyaes              | 45.4 ms                                                     | 46.9 ms: 1.03x slower                                           |
| docutils                  | 1.57 sec                                                    | 1.64 sec: 1.04x slower                                          |
| scimark_lu                | 53.0 ms                                                     | 56.8 ms: 1.07x slower                                           |
| async_tree_io             | 521 ms                                                      | 582 ms: 1.12x slower                                            |
| async_tree_io_tg          | 518 ms                                                      | 604 ms: 1.17x slower                                            |
| Geometric mean            | (ref)                                                       | 1.04x faster                                                    |

Benchmark hidden because not significant (12): pycparser, pylint, xml_etree_process, xml_etree_generate, comprehensions, sympy_integrate, sqlglot_optimize, regex_effbot, xml_etree_iterparse, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (11) of results/bm-20240508-3.13.0b1-2268289/bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.039x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown
# Results vs. 3.12.0

- fork: faster-cpython
- ref: make_decref_a_call
- machine: windows-amd64
- commit hash: bdf907f
- commit date: 2025-05-08
- overall geometric mean: 1.051x faster
- HPT reliability: 79.44%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 238 ms: 1.09x slower                                                               |
| docutils       | 1.66 sec                                                    | 1.72 sec: 1.04x slower                                                             |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 418 ms: 1.84x faster                                                               |
| async_tree_io              | 731 ms                                                      | 418 ms: 1.75x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                                               |
| async_tree_none            | 291 ms                                                      | 180 ms: 1.62x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 178 ms: 1.60x faster                                                               |
| async_tree_memoization     | 339 ms                                                      | 217 ms: 1.57x faster                                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 338 ms: 1.45x faster                                                               |
| Geometric mean             | (ref)                                                       | 1.62x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.9 ms: 1.26x faster                                                              |
| nbody          | 71.9 ms                                                     | 62.7 ms: 1.15x faster                                                              |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                               |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 82.7 ms: 1.06x faster                                                              |
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                               |
| regex_v8       | 14.2 ms                                                     | 14.3 ms: 1.01x slower                                                              |
| regex_effbot   | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 136 us: 1.02x slower                                                               |
| tomli_loads          | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                             |
| xml_etree_parse      | 93.0 ms                                                     | 96.9 ms: 1.04x slower                                                              |
| xml_etree_iterparse  | 65.2 ms                                                     | 68.0 ms: 1.04x slower                                                              |
| xml_etree_generate   | 55.8 ms                                                     | 60.5 ms: 1.08x slower                                                              |
| pickle_pure_python   | 195 us                                                      | 216 us: 1.10x slower                                                               |
| json_loads           | 13.9 us                                                     | 15.4 us: 1.11x slower                                                              |
| xml_etree_process    | 37.7 ms                                                     | 42.2 ms: 1.12x slower                                                              |
| json_dumps           | 5.70 ms                                                     | 7.19 ms: 1.26x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.0 ms: 1.23x slower                                                              |
| python_startup         | 19.5 ms                                                     | 26.7 ms: 1.37x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.57 ms: 1.08x faster                                                              |
| django_template | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.4 ms: 2.48x faster                                                              |
| async_tree_io_tg           | 771 ms                                                      | 418 ms: 1.84x faster                                                               |
| async_tree_io              | 731 ms                                                      | 418 ms: 1.75x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                                               |
| async_tree_none            | 291 ms                                                      | 180 ms: 1.62x faster                                                               |
| mdp                        | 1.37 sec                                                    | 855 ms: 1.61x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 178 ms: 1.60x faster                                                               |
| async_tree_memoization     | 339 ms                                                      | 217 ms: 1.57x faster                                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 338 ms: 1.45x faster                                                               |
| deepcopy                   | 238 us                                                      | 183 us: 1.30x faster                                                               |
| float                      | 56.8 ms                                                     | 44.9 ms: 1.26x faster                                                              |
| deepcopy_memo              | 23.7 us                                                     | 19.0 us: 1.25x faster                                                              |
| comprehensions             | 14.1 us                                                     | 12.0 us: 1.18x faster                                                              |
| go                         | 91.6 ms                                                     | 78.2 ms: 1.17x faster                                                              |
| nbody                      | 71.9 ms                                                     | 62.7 ms: 1.15x faster                                                              |
| generators                 | 22.5 ms                                                     | 19.9 ms: 1.13x faster                                                              |
| spectral_norm              | 66.9 ms                                                     | 59.4 ms: 1.13x faster                                                              |
| chaos                      | 43.3 ms                                                     | 39.3 ms: 1.10x faster                                                              |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.2 ms: 1.09x faster                                                              |
| deepcopy_reduce            | 2.09 us                                                     | 1.93 us: 1.08x faster                                                              |
| mako                       | 7.09 ms                                                     | 6.57 ms: 1.08x faster                                                              |
| raytrace                   | 192 ms                                                      | 181 ms: 1.07x faster                                                               |
| regex_compile              | 87.5 ms                                                     | 82.7 ms: 1.06x faster                                                              |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                               |
| sqlite_synth               | 1.76 us                                                     | 1.67 us: 1.05x faster                                                              |
| dulwich_log                | 44.3 ms                                                     | 42.9 ms: 1.03x faster                                                              |
| logging_silent             | 60.5 ns                                                     | 58.6 ns: 1.03x faster                                                              |
| scimark_sor                | 78.8 ms                                                     | 77.6 ms: 1.01x faster                                                              |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                               |
| sympy_integrate            | 13.0 ms                                                     | 12.8 ms: 1.01x faster                                                              |
| richards                   | 28.4 ms                                                     | 28.2 ms: 1.01x faster                                                              |
| regex_v8                   | 14.2 ms                                                     | 14.3 ms: 1.01x slower                                                              |
| json                       | 3.05 ms                                                     | 3.07 ms: 1.01x slower                                                              |
| regex_effbot               | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                              |
| coroutines                 | 14.3 ms                                                     | 14.5 ms: 1.01x slower                                                              |
| logging_format             | 6.72 us                                                     | 6.82 us: 1.02x slower                                                              |
| deltablue                  | 2.16 ms                                                     | 2.20 ms: 1.02x slower                                                              |
| unpickle_pure_python       | 133 us                                                      | 136 us: 1.02x slower                                                               |
| nqueens                    | 62.8 ms                                                     | 64.2 ms: 1.02x slower                                                              |
| bench_thread_pool          | 857 us                                                      | 876 us: 1.02x slower                                                               |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                                               |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.63 ms: 1.03x slower                                                              |
| docutils                   | 1.66 sec                                                    | 1.72 sec: 1.04x slower                                                             |
| tomli_loads                | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                             |
| xml_etree_parse            | 93.0 ms                                                     | 96.9 ms: 1.04x slower                                                              |
| xml_etree_iterparse        | 65.2 ms                                                     | 68.0 ms: 1.04x slower                                                              |
| meteor_contest             | 74.6 ms                                                     | 78.0 ms: 1.05x slower                                                              |
| pyflate                    | 295 ms                                                      | 308 ms: 1.05x slower                                                               |
| pycparser                  | 699 ms                                                      | 733 ms: 1.05x slower                                                               |
| async_generators           | 239 ms                                                      | 256 ms: 1.07x slower                                                               |
| django_template            | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                              |
| xml_etree_generate         | 55.8 ms                                                     | 60.5 ms: 1.08x slower                                                              |
| 2to3                       | 218 ms                                                      | 238 ms: 1.09x slower                                                               |
| sympy_expand               | 284 ms                                                      | 310 ms: 1.09x slower                                                               |
| pickle_pure_python         | 195 us                                                      | 216 us: 1.10x slower                                                               |
| json_loads                 | 13.9 us                                                     | 15.4 us: 1.11x slower                                                              |
| xml_etree_process          | 37.7 ms                                                     | 42.2 ms: 1.12x slower                                                              |
| fannkuch                   | 247 ms                                                      | 279 ms: 1.13x slower                                                               |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                                               |
| python_startup_no_site     | 16.2 ms                                                     | 20.0 ms: 1.23x slower                                                              |
| telco                      | 4.13 ms                                                     | 5.11 ms: 1.24x slower                                                              |
| json_dumps                 | 5.70 ms                                                     | 7.19 ms: 1.26x slower                                                              |
| coverage                   | 40.8 ms                                                     | 55.9 ms: 1.37x slower                                                              |
| python_startup             | 19.5 ms                                                     | 26.7 ms: 1.37x slower                                                              |
| gc_traversal               | 1.52 ms                                                     | 2.15 ms: 1.41x slower                                                              |
| bench_mp_pool              | 69.2 ms                                                     | 98.1 ms: 1.42x slower                                                              |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.77x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                       |

Benchmark hidden because not significant (9): sympy_sum, pprint_pformat, hexiom, scimark_fft, scimark_lu, pprint_safe_repr, richards_super, crypto_pyaes, logging_simple
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250508-3.15.0a0-bdf907f/bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 79.44% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
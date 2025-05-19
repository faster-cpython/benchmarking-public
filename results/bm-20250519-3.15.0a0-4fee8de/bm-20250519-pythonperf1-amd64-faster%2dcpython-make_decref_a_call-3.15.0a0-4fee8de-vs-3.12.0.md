# Results vs. 3.12.0

- fork: faster-cpython
- ref: make_decref_a_call
- machine: windows-amd64
- commit hash: 4fee8de
- commit date: 2025-05-19
- overall geometric mean: 1.064x faster
- HPT reliability: 90.88%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 225 ms: 1.03x slower                                                               |
| docutils       | 1.66 sec                                                    | 1.67 sec: 1.01x slower                                                             |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 408 ms: 1.89x faster                                                               |
| async_tree_io              | 731 ms                                                      | 409 ms: 1.79x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 213 ms: 1.72x faster                                                               |
| async_tree_none            | 291 ms                                                      | 176 ms: 1.65x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                               |
| async_tree_memoization     | 339 ms                                                      | 213 ms: 1.59x faster                                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 335 ms: 1.46x faster                                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                                               |
| Geometric mean             | (ref)                                                       | 1.64x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.1 ms: 1.32x faster                                                              |
| nbody          | 71.9 ms                                                     | 60.7 ms: 1.18x faster                                                              |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                               |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                               |
| regex_effbot   | 1.62 ms                                                     | 1.50 ms: 1.08x faster                                                              |
| regex_compile  | 87.5 ms                                                     | 82.0 ms: 1.07x faster                                                              |
| regex_v8       | 14.2 ms                                                     | 13.6 ms: 1.05x faster                                                              |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 94.2 ms: 1.01x slower                                                              |
| xml_etree_iterparse  | 65.2 ms                                                     | 66.6 ms: 1.02x slower                                                              |
| tomli_loads          | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                             |
| unpickle_pure_python | 133 us                                                      | 137 us: 1.03x slower                                                               |
| xml_etree_generate   | 55.8 ms                                                     | 60.7 ms: 1.09x slower                                                              |
| pickle_pure_python   | 195 us                                                      | 213 us: 1.09x slower                                                               |
| xml_etree_process    | 37.7 ms                                                     | 42.3 ms: 1.12x slower                                                              |
| json_loads           | 13.9 us                                                     | 15.6 us: 1.12x slower                                                              |
| json_dumps           | 5.70 ms                                                     | 6.66 ms: 1.17x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.8 ms: 1.15x slower                                                              |
| python_startup         | 19.5 ms                                                     | 24.9 ms: 1.28x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.49 ms: 1.09x faster                                                              |
| django_template | 22.9 ms                                                     | 25.4 ms: 1.11x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.9 ms: 2.69x faster                                                              |
| async_tree_io_tg           | 771 ms                                                      | 408 ms: 1.89x faster                                                               |
| async_tree_io              | 731 ms                                                      | 409 ms: 1.79x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 213 ms: 1.72x faster                                                               |
| async_tree_none            | 291 ms                                                      | 176 ms: 1.65x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                               |
| mdp                        | 1.37 sec                                                    | 841 ms: 1.63x faster                                                               |
| async_tree_memoization     | 339 ms                                                      | 213 ms: 1.59x faster                                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 335 ms: 1.46x faster                                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                                               |
| float                      | 56.8 ms                                                     | 43.1 ms: 1.32x faster                                                              |
| deepcopy                   | 238 us                                                      | 182 us: 1.31x faster                                                               |
| deepcopy_memo              | 23.7 us                                                     | 19.6 us: 1.21x faster                                                              |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.19x faster                                                              |
| nbody                      | 71.9 ms                                                     | 60.7 ms: 1.18x faster                                                              |
| go                         | 91.6 ms                                                     | 78.6 ms: 1.17x faster                                                              |
| spectral_norm              | 66.9 ms                                                     | 59.6 ms: 1.12x faster                                                              |
| chaos                      | 43.3 ms                                                     | 39.0 ms: 1.11x faster                                                              |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.5 ms: 1.11x faster                                                              |
| mako                       | 7.09 ms                                                     | 6.49 ms: 1.09x faster                                                              |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                               |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.09x faster                                                              |
| deepcopy_reduce            | 2.09 us                                                     | 1.93 us: 1.08x faster                                                              |
| dulwich_log                | 44.3 ms                                                     | 40.9 ms: 1.08x faster                                                              |
| generators                 | 22.5 ms                                                     | 20.9 ms: 1.08x faster                                                              |
| regex_effbot               | 1.62 ms                                                     | 1.50 ms: 1.08x faster                                                              |
| regex_compile              | 87.5 ms                                                     | 82.0 ms: 1.07x faster                                                              |
| raytrace                   | 192 ms                                                      | 182 ms: 1.06x faster                                                               |
| regex_v8                   | 14.2 ms                                                     | 13.6 ms: 1.05x faster                                                              |
| richards                   | 28.4 ms                                                     | 27.6 ms: 1.03x faster                                                              |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                               |
| richards_super             | 32.1 ms                                                     | 31.4 ms: 1.02x faster                                                              |
| crypto_pyaes               | 48.5 ms                                                     | 47.6 ms: 1.02x faster                                                              |
| sympy_integrate            | 13.0 ms                                                     | 12.8 ms: 1.01x faster                                                              |
| sympy_sum                  | 91.5 ms                                                     | 90.6 ms: 1.01x faster                                                              |
| pprint_pformat             | 1.05 sec                                                    | 1.04 sec: 1.01x faster                                                             |
| pprint_safe_repr           | 513 ms                                                      | 510 ms: 1.01x faster                                                               |
| deltablue                  | 2.16 ms                                                     | 2.17 ms: 1.01x slower                                                              |
| docutils                   | 1.66 sec                                                    | 1.67 sec: 1.01x slower                                                             |
| hexiom                     | 4.10 ms                                                     | 4.14 ms: 1.01x slower                                                              |
| scimark_fft                | 184 ms                                                      | 186 ms: 1.01x slower                                                               |
| json                       | 3.05 ms                                                     | 3.08 ms: 1.01x slower                                                              |
| xml_etree_parse            | 93.0 ms                                                     | 94.2 ms: 1.01x slower                                                              |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                               |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.6 ms: 1.02x slower                                                              |
| pyflate                    | 295 ms                                                      | 301 ms: 1.02x slower                                                               |
| tomli_loads                | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                             |
| coroutines                 | 14.3 ms                                                     | 14.6 ms: 1.02x slower                                                              |
| pycparser                  | 699 ms                                                      | 717 ms: 1.03x slower                                                               |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.62 ms: 1.03x slower                                                              |
| unpickle_pure_python       | 133 us                                                      | 137 us: 1.03x slower                                                               |
| 2to3                       | 218 ms                                                      | 225 ms: 1.03x slower                                                               |
| scimark_lu                 | 58.9 ms                                                     | 60.7 ms: 1.03x slower                                                              |
| meteor_contest             | 74.6 ms                                                     | 77.4 ms: 1.04x slower                                                              |
| logging_simple             | 6.28 us                                                     | 6.55 us: 1.04x slower                                                              |
| logging_format             | 6.72 us                                                     | 7.03 us: 1.05x slower                                                              |
| async_generators           | 239 ms                                                      | 252 ms: 1.05x slower                                                               |
| sympy_expand               | 284 ms                                                      | 308 ms: 1.09x slower                                                               |
| xml_etree_generate         | 55.8 ms                                                     | 60.7 ms: 1.09x slower                                                              |
| pickle_pure_python         | 195 us                                                      | 213 us: 1.09x slower                                                               |
| django_template            | 22.9 ms                                                     | 25.4 ms: 1.11x slower                                                              |
| xml_etree_process          | 37.7 ms                                                     | 42.3 ms: 1.12x slower                                                              |
| json_loads                 | 13.9 us                                                     | 15.6 us: 1.12x slower                                                              |
| fannkuch                   | 247 ms                                                      | 280 ms: 1.14x slower                                                               |
| python_startup_no_site     | 16.2 ms                                                     | 18.8 ms: 1.15x slower                                                              |
| json_dumps                 | 5.70 ms                                                     | 6.66 ms: 1.17x slower                                                              |
| typing_runtime_protocols   | 95.1 us                                                     | 115 us: 1.21x slower                                                               |
| telco                      | 4.13 ms                                                     | 5.09 ms: 1.23x slower                                                              |
| python_startup             | 19.5 ms                                                     | 24.9 ms: 1.28x slower                                                              |
| bench_mp_pool              | 69.2 ms                                                     | 92.7 ms: 1.34x slower                                                              |
| gc_traversal               | 1.52 ms                                                     | 2.08 ms: 1.37x slower                                                              |
| coverage                   | 40.8 ms                                                     | 56.9 ms: 1.39x slower                                                              |
| create_gc_cycles           | 752 us                                                      | 1.29 ms: 1.72x slower                                                              |
| logging_silent             | 60.5 ns                                                     | 342 ns: 5.65x slower                                                               |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                       |

Benchmark hidden because not significant (3): scimark_sor, nqueens, bench_thread_pool
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250519-3.15.0a0-4fee8de/bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 90.88% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
# Results vs. 3.12.0

- fork: faster-cpython
- ref: fast_side_exits
- machine: windows-amd64
- commit hash: 73832b2
- commit date: 2025-07-08
- overall geometric mean: 1.120x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                          |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 395 ms: 1.95x faster                                                            |
| async_tree_io              | 731 ms                                                      | 396 ms: 1.85x faster                                                            |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                            |
| async_tree_none            | 291 ms                                                      | 168 ms: 1.73x faster                                                            |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                            |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.65x faster                                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                            |
| Geometric mean             | (ref)                                                       | 1.70x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 53.5 ms: 1.34x faster                                                           |
| float          | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                           |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.1 ms: 1.11x faster                                                           |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                            |
| regex_v8       | 14.2 ms                                                     | 13.4 ms: 1.06x faster                                                           |
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 108 us: 1.24x faster                                                            |
| tomli_loads          | 1.37 sec                                                    | 1.13 sec: 1.22x faster                                                          |
| xml_etree_generate   | 55.8 ms                                                     | 50.9 ms: 1.10x faster                                                           |
| xml_etree_process    | 37.7 ms                                                     | 34.9 ms: 1.08x faster                                                           |
| xml_etree_parse      | 93.0 ms                                                     | 88.1 ms: 1.06x faster                                                           |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.2 ms: 1.02x faster                                                           |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.05x slower                                                           |
| pickle_pure_python   | 195 us                                                      | 205 us: 1.05x slower                                                            |
| json_dumps           | 5.70 ms                                                     | 6.26 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                           |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                           |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.36 ms: 1.32x faster                                                           |
| django_template | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.0 ms: 2.51x faster                                                           |
| async_tree_io_tg           | 771 ms                                                      | 395 ms: 1.95x faster                                                            |
| async_tree_io              | 731 ms                                                      | 396 ms: 1.85x faster                                                            |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                            |
| async_tree_none            | 291 ms                                                      | 168 ms: 1.73x faster                                                            |
| mdp                        | 1.37 sec                                                    | 804 ms: 1.71x faster                                                            |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                            |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.65x faster                                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                            |
| deepcopy                   | 238 us                                                      | 171 us: 1.39x faster                                                            |
| comprehensions             | 14.1 us                                                     | 10.4 us: 1.35x faster                                                           |
| nbody                      | 71.9 ms                                                     | 53.5 ms: 1.34x faster                                                           |
| mako                       | 7.09 ms                                                     | 5.36 ms: 1.32x faster                                                           |
| float                      | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                           |
| deepcopy_memo              | 23.7 us                                                     | 18.5 us: 1.28x faster                                                           |
| unpickle_pure_python       | 133 us                                                      | 108 us: 1.24x faster                                                            |
| tomli_loads                | 1.37 sec                                                    | 1.13 sec: 1.22x faster                                                          |
| scimark_fft                | 184 ms                                                      | 156 ms: 1.19x faster                                                            |
| go                         | 91.6 ms                                                     | 77.5 ms: 1.18x faster                                                           |
| pyflate                    | 295 ms                                                      | 253 ms: 1.16x faster                                                            |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                           |
| deepcopy_reduce            | 2.09 us                                                     | 1.83 us: 1.15x faster                                                           |
| pprint_pformat             | 1.05 sec                                                    | 920 ms: 1.14x faster                                                            |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.13x faster                                                           |
| logging_silent             | 60.5 ns                                                     | 54.0 ns: 1.12x faster                                                           |
| regex_compile              | 87.5 ms                                                     | 79.1 ms: 1.11x faster                                                           |
| pprint_safe_repr           | 513 ms                                                      | 467 ms: 1.10x faster                                                            |
| xml_etree_generate         | 55.8 ms                                                     | 50.9 ms: 1.10x faster                                                           |
| raytrace                   | 192 ms                                                      | 177 ms: 1.08x faster                                                            |
| chaos                      | 43.3 ms                                                     | 40.1 ms: 1.08x faster                                                           |
| xml_etree_process          | 37.7 ms                                                     | 34.9 ms: 1.08x faster                                                           |
| dulwich_log                | 44.3 ms                                                     | 41.0 ms: 1.08x faster                                                           |
| richards                   | 28.4 ms                                                     | 26.3 ms: 1.08x faster                                                           |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                            |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.1 ms: 1.07x faster                                                           |
| richards_super             | 32.1 ms                                                     | 30.2 ms: 1.06x faster                                                           |
| crypto_pyaes               | 48.5 ms                                                     | 45.6 ms: 1.06x faster                                                           |
| regex_v8                   | 14.2 ms                                                     | 13.4 ms: 1.06x faster                                                           |
| xml_etree_parse            | 93.0 ms                                                     | 88.1 ms: 1.06x faster                                                           |
| nqueens                    | 62.8 ms                                                     | 59.7 ms: 1.05x faster                                                           |
| fannkuch                   | 247 ms                                                      | 235 ms: 1.05x faster                                                            |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                           |
| sympy_sum                  | 91.5 ms                                                     | 87.4 ms: 1.05x faster                                                           |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                            |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                            |
| meteor_contest             | 74.6 ms                                                     | 72.4 ms: 1.03x faster                                                           |
| logging_simple             | 6.28 us                                                     | 6.15 us: 1.02x faster                                                           |
| scimark_lu                 | 58.9 ms                                                     | 57.7 ms: 1.02x faster                                                           |
| spectral_norm              | 66.9 ms                                                     | 65.7 ms: 1.02x faster                                                           |
| logging_format             | 6.72 us                                                     | 6.61 us: 1.02x faster                                                           |
| sympy_integrate            | 13.0 ms                                                     | 12.8 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.2 ms: 1.02x faster                                                           |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                          |
| scimark_sor                | 78.8 ms                                                     | 78.1 ms: 1.01x faster                                                           |
| hexiom                     | 4.10 ms                                                     | 4.09 ms: 1.00x faster                                                           |
| coroutines                 | 14.3 ms                                                     | 14.4 ms: 1.01x slower                                                           |
| deltablue                  | 2.16 ms                                                     | 2.20 ms: 1.02x slower                                                           |
| async_generators           | 239 ms                                                      | 244 ms: 1.02x slower                                                            |
| sympy_expand               | 284 ms                                                      | 293 ms: 1.03x slower                                                            |
| telco                      | 4.13 ms                                                     | 4.29 ms: 1.04x slower                                                           |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.05x slower                                                           |
| pickle_pure_python         | 195 us                                                      | 205 us: 1.05x slower                                                            |
| django_template            | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                           |
| typing_runtime_protocols   | 95.1 us                                                     | 102 us: 1.07x slower                                                            |
| json_dumps                 | 5.70 ms                                                     | 6.26 ms: 1.10x slower                                                           |
| python_startup_no_site     | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                           |
| coverage                   | 40.8 ms                                                     | 49.2 ms: 1.21x slower                                                           |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                           |
| gc_traversal               | 1.52 ms                                                     | 2.17 ms: 1.43x slower                                                           |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.76x slower                                                           |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                                    |

Benchmark hidden because not significant (4): scimark_sparse_mat_mult, pycparser, 2to3, json
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250708-3.15.0a0-73832b2-JIT/bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.120x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown
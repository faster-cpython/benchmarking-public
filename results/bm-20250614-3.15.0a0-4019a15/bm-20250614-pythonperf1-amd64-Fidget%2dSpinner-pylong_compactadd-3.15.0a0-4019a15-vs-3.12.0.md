# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: pylong_compactadd
- machine: windows-amd64
- commit hash: 4019a15
- commit date: 2025-06-14
- overall geometric mean: 1.068x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                              |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                            |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 392 ms: 1.97x faster                                                              |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                              |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                              |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                              |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                              |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 327 ms: 1.50x faster                                                              |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                              |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                             |
| nbody          | 71.9 ms                                                     | 62.0 ms: 1.16x faster                                                             |
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                              |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.3 ms: 1.10x faster                                                             |
| regex_effbot   | 1.62 ms                                                     | 1.51 ms: 1.07x faster                                                             |
| regex_dna      | 126 ms                                                      | 122 ms: 1.04x faster                                                              |
| regex_v8       | 14.2 ms                                                     | 14.0 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 87.9 ms: 1.06x faster                                                             |
| unpickle_pure_python | 133 us                                                      | 131 us: 1.02x faster                                                              |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.5 ms: 1.01x faster                                                             |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                             |
| xml_etree_process    | 37.7 ms                                                     | 39.2 ms: 1.04x slower                                                             |
| pickle_pure_python   | 195 us                                                      | 208 us: 1.07x slower                                                              |
| json_dumps           | 5.70 ms                                                     | 6.36 ms: 1.12x slower                                                             |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                      |

Benchmark hidden because not significant (2): xml_etree_generate, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                             |
| python_startup         | 19.5 ms                                                     | 26.2 ms: 1.34x slower                                                             |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.54 ms: 1.08x faster                                                             |
| django_template | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                             |
| Geometric mean  | (ref)                                                       | 1.02x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.5 ms: 2.55x faster                                                             |
| async_tree_io_tg           | 771 ms                                                      | 392 ms: 1.97x faster                                                              |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                              |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                              |
| mdp                        | 1.37 sec                                                    | 795 ms: 1.73x faster                                                              |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                              |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                              |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 327 ms: 1.50x faster                                                              |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                              |
| deepcopy                   | 238 us                                                      | 171 us: 1.39x faster                                                              |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.33x faster                                                             |
| float                      | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                             |
| deepcopy_memo              | 23.7 us                                                     | 19.5 us: 1.22x faster                                                             |
| go                         | 91.6 ms                                                     | 75.8 ms: 1.21x faster                                                             |
| generators                 | 22.5 ms                                                     | 19.3 ms: 1.17x faster                                                             |
| nbody                      | 71.9 ms                                                     | 62.0 ms: 1.16x faster                                                             |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.16x faster                                                             |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                             |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.4 ms: 1.11x faster                                                             |
| regex_compile              | 87.5 ms                                                     | 79.3 ms: 1.10x faster                                                             |
| spectral_norm              | 66.9 ms                                                     | 61.6 ms: 1.09x faster                                                             |
| mako                       | 7.09 ms                                                     | 6.54 ms: 1.08x faster                                                             |
| chaos                      | 43.3 ms                                                     | 40.2 ms: 1.08x faster                                                             |
| dulwich_log                | 44.3 ms                                                     | 41.2 ms: 1.07x faster                                                             |
| regex_effbot               | 1.62 ms                                                     | 1.51 ms: 1.07x faster                                                             |
| raytrace                   | 192 ms                                                      | 182 ms: 1.06x faster                                                              |
| xml_etree_parse            | 93.0 ms                                                     | 87.9 ms: 1.06x faster                                                             |
| richards_super             | 32.1 ms                                                     | 30.5 ms: 1.05x faster                                                             |
| pyflate                    | 295 ms                                                      | 280 ms: 1.05x faster                                                              |
| scimark_fft                | 184 ms                                                      | 176 ms: 1.05x faster                                                              |
| richards                   | 28.4 ms                                                     | 27.1 ms: 1.05x faster                                                             |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                              |
| nqueens                    | 62.8 ms                                                     | 60.2 ms: 1.04x faster                                                             |
| sympy_sum                  | 91.5 ms                                                     | 87.7 ms: 1.04x faster                                                             |
| scimark_sor                | 78.8 ms                                                     | 75.5 ms: 1.04x faster                                                             |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.04x faster                                                             |
| sympy_str                  | 175 ms                                                      | 168 ms: 1.04x faster                                                              |
| regex_dna                  | 126 ms                                                      | 122 ms: 1.04x faster                                                              |
| async_generators           | 239 ms                                                      | 231 ms: 1.04x faster                                                              |
| crypto_pyaes               | 48.5 ms                                                     | 47.0 ms: 1.03x faster                                                             |
| meteor_contest             | 74.6 ms                                                     | 72.5 ms: 1.03x faster                                                             |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                            |
| unpickle_pure_python       | 133 us                                                      | 131 us: 1.02x faster                                                              |
| hexiom                     | 4.10 ms                                                     | 4.03 ms: 1.02x faster                                                             |
| regex_v8                   | 14.2 ms                                                     | 14.0 ms: 1.01x faster                                                             |
| scimark_lu                 | 58.9 ms                                                     | 58.1 ms: 1.01x faster                                                             |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                             |
| json                       | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                                             |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.5 ms: 1.01x faster                                                             |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                             |
| deltablue                  | 2.16 ms                                                     | 2.19 ms: 1.01x slower                                                             |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                              |
| logging_simple             | 6.28 us                                                     | 6.40 us: 1.02x slower                                                             |
| sympy_expand               | 284 ms                                                      | 290 ms: 1.02x slower                                                              |
| logging_format             | 6.72 us                                                     | 6.92 us: 1.03x slower                                                             |
| pycparser                  | 699 ms                                                      | 725 ms: 1.04x slower                                                              |
| xml_etree_process          | 37.7 ms                                                     | 39.2 ms: 1.04x slower                                                             |
| django_template            | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                             |
| fannkuch                   | 247 ms                                                      | 258 ms: 1.05x slower                                                              |
| pprint_safe_repr           | 513 ms                                                      | 537 ms: 1.05x slower                                                              |
| pprint_pformat             | 1.05 sec                                                    | 1.10 sec: 1.05x slower                                                            |
| typing_runtime_protocols   | 95.1 us                                                     | 101 us: 1.06x slower                                                              |
| pickle_pure_python         | 195 us                                                      | 208 us: 1.07x slower                                                              |
| telco                      | 4.13 ms                                                     | 4.49 ms: 1.09x slower                                                             |
| json_dumps                 | 5.70 ms                                                     | 6.36 ms: 1.12x slower                                                             |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                             |
| python_startup             | 19.5 ms                                                     | 26.2 ms: 1.34x slower                                                             |
| gc_traversal               | 1.52 ms                                                     | 2.16 ms: 1.42x slower                                                             |
| create_gc_cycles           | 752 us                                                      | 1.34 ms: 1.78x slower                                                             |
| logging_silent             | 60.5 ns                                                     | 321 ns: 5.32x slower                                                              |
| coverage                   | 40.8 ms                                                     | 294 ms: 7.19x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                      |

Benchmark hidden because not significant (3): xml_etree_generate, scimark_sparse_mat_mult, tomli_loads
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250614-3.15.0a0-4019a15/bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.068x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown
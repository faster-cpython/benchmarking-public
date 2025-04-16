# Results vs. 3.12.0

- fork: python
- ref: 844596c09fc812a58ac1
- machine: windows-amd64
- commit hash: 844596c
- commit date: 2025-04-14
- overall geometric mean: 1.095x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.01x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 394 ms: 1.96x faster                                                        |
| async_tree_io              | 731 ms                                                      | 409 ms: 1.79x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                        |
| async_tree_none            | 291 ms                                                      | 178 ms: 1.64x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 42.9 ms: 1.32x faster                                                       |
| nbody          | 71.9 ms                                                     | 61.3 ms: 1.17x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.5 ms: 1.10x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.49 ms: 1.08x faster                                                       |
| regex_dna      | 126 ms                                                      | 120 ms: 1.06x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|---------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse     | 93.0 ms                                                     | 89.8 ms: 1.04x faster                                                       |
| xml_etree_iterparse | 65.2 ms                                                     | 64.0 ms: 1.02x faster                                                       |
| tomli_loads         | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                      |
| xml_etree_process   | 37.7 ms                                                     | 39.9 ms: 1.06x slower                                                       |
| pickle_pure_python  | 195 us                                                      | 210 us: 1.07x slower                                                        |
| json_loads          | 13.9 us                                                     | 15.5 us: 1.12x slower                                                       |
| json_dumps          | 5.70 ms                                                     | 6.79 ms: 1.19x slower                                                       |
| Geometric mean      | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.9 ms: 1.29x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.4 ms: 1.36x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.62 ms: 1.07x faster                                                       |
| django_template | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.3 ms: 2.49x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 394 ms: 1.96x faster                                                        |
| async_tree_io              | 731 ms                                                      | 409 ms: 1.79x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                        |
| mdp                        | 1.37 sec                                                    | 813 ms: 1.69x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                        |
| async_tree_none            | 291 ms                                                      | 178 ms: 1.64x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                        |
| deepcopy                   | 238 us                                                      | 171 us: 1.39x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 17.7 us: 1.34x faster                                                       |
| float                      | 56.8 ms                                                     | 42.9 ms: 1.32x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.2 us: 1.26x faster                                                       |
| go                         | 91.6 ms                                                     | 76.4 ms: 1.20x faster                                                       |
| nbody                      | 71.9 ms                                                     | 61.3 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.80 us: 1.17x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 57.5 ms: 1.16x faster                                                       |
| chaos                      | 43.3 ms                                                     | 37.9 ms: 1.14x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.3 ms: 1.14x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 54.2 ns: 1.11x faster                                                       |
| raytrace                   | 192 ms                                                      | 174 ms: 1.10x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 79.5 ms: 1.10x faster                                                       |
| generators                 | 22.5 ms                                                     | 20.6 ms: 1.10x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.49 ms: 1.08x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.3 ms: 1.07x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.62 ms: 1.07x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.7 ms: 1.06x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 74.5 ms: 1.06x faster                                                       |
| scimark_fft                | 184 ms                                                      | 174 ms: 1.06x faster                                                        |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.06x faster                                                        |
| pyflate                    | 295 ms                                                      | 279 ms: 1.06x faster                                                        |
| async_generators           | 239 ms                                                      | 228 ms: 1.05x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 46.4 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.45 ms: 1.04x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 3.94 ms: 1.04x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 56.6 ms: 1.04x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.00 sec: 1.04x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 494 ms: 1.04x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 89.8 ms: 1.04x faster                                                       |
| richards_super             | 32.1 ms                                                     | 31.0 ms: 1.03x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.03x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 88.7 ms: 1.03x faster                                                       |
| richards                   | 28.4 ms                                                     | 27.5 ms: 1.03x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.10 ms: 1.03x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 73.1 ms: 1.02x faster                                                       |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.0 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| nqueens                    | 62.8 ms                                                     | 61.9 ms: 1.01x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                      |
| 2to3                       | 218 ms                                                      | 221 ms: 1.01x slower                                                        |
| logging_format             | 6.72 us                                                     | 6.84 us: 1.02x slower                                                       |
| pycparser                  | 699 ms                                                      | 717 ms: 1.03x slower                                                        |
| bench_thread_pool          | 857 us                                                      | 882 us: 1.03x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                       |
| sympy_expand               | 284 ms                                                      | 295 ms: 1.04x slower                                                        |
| django_template            | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.9 ms: 1.06x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 210 us: 1.07x slower                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 106 us: 1.11x slower                                                        |
| json_loads                 | 13.9 us                                                     | 15.5 us: 1.12x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.64 ms: 1.12x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.79 ms: 1.19x slower                                                       |
| coverage                   | 40.8 ms                                                     | 50.4 ms: 1.23x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 89.0 ms: 1.29x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.9 ms: 1.29x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.4 ms: 1.36x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.07 ms: 1.36x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.26 ms: 1.67x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (5): json, xml_etree_generate, fannkuch, unpickle_pure_python, logging_simple
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250414-3.14.0a7+-844596c/bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.095x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown
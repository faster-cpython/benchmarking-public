# Results vs. 3.12.0

- fork: zooba
- ref: gh_91349
- machine: windows-amd64
- commit hash: 548daa7
- commit date: 2025-03-19
- overall geometric mean: 1.025x faster
- HPT reliability: 87.07%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 230 ms: 1.05x slower                                           |
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                         |
| Geometric mean | (ref)                                                       | 1.04x slower                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 418 ms: 1.85x faster                                           |
| async_tree_io              | 731 ms                                                      | 430 ms: 1.70x faster                                           |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.68x faster                                           |
| async_tree_none_tg         | 285 ms                                                      | 180 ms: 1.59x faster                                           |
| async_tree_none            | 291 ms                                                      | 192 ms: 1.52x faster                                           |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.51x faster                                           |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 347 ms: 1.41x faster                                           |
| Geometric mean             | (ref)                                                       | 1.58x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.8 ms: 1.21x faster                                          |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                           |
| Geometric mean | (ref)                                                       | 1.07x faster                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.44 ms: 1.13x faster                                          |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                           |
| regex_v8       | 14.2 ms                                                     | 13.9 ms: 1.02x faster                                          |
| regex_compile  | 87.5 ms                                                     | 89.0 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                       | 1.05x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 90.3 ms: 1.03x faster                                          |
| xml_etree_generate   | 55.8 ms                                                     | 58.9 ms: 1.06x slower                                          |
| tomli_loads          | 1.37 sec                                                    | 1.49 sec: 1.09x slower                                         |
| json_loads           | 13.9 us                                                     | 15.4 us: 1.10x slower                                          |
| xml_etree_process    | 37.7 ms                                                     | 42.3 ms: 1.12x slower                                          |
| unpickle_pure_python | 133 us                                                      | 152 us: 1.14x slower                                           |
| pickle_pure_python   | 195 us                                                      | 236 us: 1.21x slower                                           |
| json_dumps           | 5.70 ms                                                     | 6.99 ms: 1.23x slower                                          |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                   |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.4 ms: 1.26x slower                                          |
| python_startup         | 19.5 ms                                                     | 26.4 ms: 1.36x slower                                          |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.86 ms: 1.03x faster                                          |
| django_template | 22.9 ms                                                     | 26.7 ms: 1.16x slower                                          |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.8 ms: 2.45x faster                                          |
| async_tree_io_tg           | 771 ms                                                      | 418 ms: 1.85x faster                                           |
| async_tree_io              | 731 ms                                                      | 430 ms: 1.70x faster                                           |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.68x faster                                           |
| async_tree_none_tg         | 285 ms                                                      | 180 ms: 1.59x faster                                           |
| async_tree_none            | 291 ms                                                      | 192 ms: 1.52x faster                                           |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.51x faster                                           |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 347 ms: 1.41x faster                                           |
| deepcopy                   | 238 us                                                      | 187 us: 1.27x faster                                           |
| float                      | 56.8 ms                                                     | 46.8 ms: 1.21x faster                                          |
| deepcopy_memo              | 23.7 us                                                     | 19.7 us: 1.21x faster                                          |
| generators                 | 22.5 ms                                                     | 19.3 ms: 1.17x faster                                          |
| comprehensions             | 14.1 us                                                     | 12.1 us: 1.16x faster                                          |
| spectral_norm              | 66.9 ms                                                     | 57.9 ms: 1.16x faster                                          |
| regex_effbot               | 1.62 ms                                                     | 1.44 ms: 1.13x faster                                          |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                          |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                           |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.06x faster                                          |
| deepcopy_reduce            | 2.09 us                                                     | 2.00 us: 1.05x faster                                          |
| async_generators           | 239 ms                                                      | 232 ms: 1.03x faster                                           |
| mako                       | 7.09 ms                                                     | 6.86 ms: 1.03x faster                                          |
| xml_etree_parse            | 93.0 ms                                                     | 90.3 ms: 1.03x faster                                          |
| dulwich_log                | 44.3 ms                                                     | 43.1 ms: 1.03x faster                                          |
| logging_silent             | 60.5 ns                                                     | 59.2 ns: 1.02x faster                                          |
| regex_v8                   | 14.2 ms                                                     | 13.9 ms: 1.02x faster                                          |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                           |
| go                         | 91.6 ms                                                     | 90.4 ms: 1.01x faster                                          |
| scimark_fft                | 184 ms                                                      | 187 ms: 1.01x slower                                           |
| regex_compile              | 87.5 ms                                                     | 89.0 ms: 1.02x slower                                          |
| json                       | 3.05 ms                                                     | 3.11 ms: 1.02x slower                                          |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                           |
| chaos                      | 43.3 ms                                                     | 44.4 ms: 1.02x slower                                          |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                         |
| crypto_pyaes               | 48.5 ms                                                     | 49.9 ms: 1.03x slower                                          |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.04x slower                                          |
| scimark_lu                 | 58.9 ms                                                     | 61.4 ms: 1.04x slower                                          |
| meteor_contest             | 74.6 ms                                                     | 77.8 ms: 1.04x slower                                          |
| 2to3                       | 218 ms                                                      | 230 ms: 1.05x slower                                           |
| deltablue                  | 2.16 ms                                                     | 2.28 ms: 1.05x slower                                          |
| xml_etree_generate         | 55.8 ms                                                     | 58.9 ms: 1.06x slower                                          |
| richards_super             | 32.1 ms                                                     | 33.9 ms: 1.06x slower                                          |
| raytrace                   | 192 ms                                                      | 204 ms: 1.06x slower                                           |
| logging_simple             | 6.28 us                                                     | 6.66 us: 1.06x slower                                          |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.07x slower                                         |
| pprint_safe_repr           | 513 ms                                                      | 548 ms: 1.07x slower                                           |
| logging_format             | 6.72 us                                                     | 7.22 us: 1.07x slower                                          |
| scimark_sor                | 78.8 ms                                                     | 84.7 ms: 1.08x slower                                          |
| nqueens                    | 62.8 ms                                                     | 67.8 ms: 1.08x slower                                          |
| richards                   | 28.4 ms                                                     | 30.8 ms: 1.08x slower                                          |
| sympy_expand               | 284 ms                                                      | 308 ms: 1.08x slower                                           |
| pyflate                    | 295 ms                                                      | 321 ms: 1.09x slower                                           |
| tomli_loads                | 1.37 sec                                                    | 1.49 sec: 1.09x slower                                         |
| hexiom                     | 4.10 ms                                                     | 4.48 ms: 1.09x slower                                          |
| pycparser                  | 699 ms                                                      | 765 ms: 1.10x slower                                           |
| json_loads                 | 13.9 us                                                     | 15.4 us: 1.10x slower                                          |
| fannkuch                   | 247 ms                                                      | 275 ms: 1.12x slower                                           |
| mdp                        | 1.37 sec                                                    | 1.54 sec: 1.12x slower                                         |
| xml_etree_process          | 37.7 ms                                                     | 42.3 ms: 1.12x slower                                          |
| unpickle_pure_python       | 133 us                                                      | 152 us: 1.14x slower                                           |
| django_template            | 22.9 ms                                                     | 26.7 ms: 1.16x slower                                          |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                           |
| coverage                   | 40.8 ms                                                     | 49.1 ms: 1.20x slower                                          |
| pickle_pure_python         | 195 us                                                      | 236 us: 1.21x slower                                           |
| telco                      | 4.13 ms                                                     | 5.03 ms: 1.22x slower                                          |
| json_dumps                 | 5.70 ms                                                     | 6.99 ms: 1.23x slower                                          |
| python_startup_no_site     | 16.2 ms                                                     | 20.4 ms: 1.26x slower                                          |
| bench_mp_pool              | 69.2 ms                                                     | 89.3 ms: 1.29x slower                                          |
| python_startup             | 19.5 ms                                                     | 26.4 ms: 1.36x slower                                          |
| gc_traversal               | 1.52 ms                                                     | 2.08 ms: 1.36x slower                                          |
| create_gc_cycles           | 752 us                                                      | 1.23 ms: 1.64x slower                                          |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                   |

Benchmark hidden because not significant (6): sympy_sum, scimark_sparse_mat_mult, xml_etree_iterparse, scimark_monte_carlo, nbody, bench_thread_pool
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250319-3.14.0a6+-548daa7/bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.025x faster

# HPT report

- Reliability score: 87.07% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
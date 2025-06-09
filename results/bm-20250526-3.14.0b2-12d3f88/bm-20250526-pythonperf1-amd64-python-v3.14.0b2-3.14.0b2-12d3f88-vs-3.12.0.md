# Results vs. 3.12.0

- fork: python
- ref: v3.14.0b2
- machine: windows-amd64
- commit hash: 12d3f88
- commit date: 2025-05-26
- overall geometric mean: 1.077x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                            |
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                          |
| Geometric mean | (ref)                                                       | 1.01x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 402 ms: 1.92x faster                                            |
| async_tree_io              | 731 ms                                                      | 408 ms: 1.79x faster                                            |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                            |
| async_tree_none            | 291 ms                                                      | 176 ms: 1.66x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.65x faster                                            |
| async_tree_memoization     | 339 ms                                                      | 210 ms: 1.62x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.47x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.46x faster                                            |
| Geometric mean             | (ref)                                                       | 1.66x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.3 ms: 1.28x faster                                           |
| nbody          | 71.9 ms                                                     | 64.3 ms: 1.12x faster                                           |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                            |
| Geometric mean | (ref)                                                       | 1.14x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 81.8 ms: 1.07x faster                                           |
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                            |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                       | 1.03x faster                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 90.4 ms: 1.03x faster                                           |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.2 ms: 1.02x faster                                           |
| unpickle_pure_python | 133 us                                                      | 136 us: 1.02x slower                                            |
| xml_etree_generate   | 55.8 ms                                                     | 57.4 ms: 1.03x slower                                           |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                          |
| xml_etree_process    | 37.7 ms                                                     | 39.7 ms: 1.05x slower                                           |
| json_loads           | 13.9 us                                                     | 14.8 us: 1.07x slower                                           |
| pickle_pure_python   | 195 us                                                      | 212 us: 1.08x slower                                            |
| json_dumps           | 5.70 ms                                                     | 6.38 ms: 1.12x slower                                           |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.1 ms: 1.24x slower                                           |
| python_startup         | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                           |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.71 ms: 1.06x faster                                           |
| django_template | 22.9 ms                                                     | 25.0 ms: 1.09x slower                                           |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.3 ms: 2.49x faster                                           |
| async_tree_io_tg           | 771 ms                                                      | 402 ms: 1.92x faster                                            |
| async_tree_io              | 731 ms                                                      | 408 ms: 1.79x faster                                            |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                            |
| mdp                        | 1.37 sec                                                    | 820 ms: 1.67x faster                                            |
| async_tree_none            | 291 ms                                                      | 176 ms: 1.66x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.65x faster                                            |
| async_tree_memoization     | 339 ms                                                      | 210 ms: 1.62x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.47x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.46x faster                                            |
| deepcopy                   | 238 us                                                      | 172 us: 1.38x faster                                            |
| deepcopy_memo              | 23.7 us                                                     | 18.3 us: 1.29x faster                                           |
| float                      | 56.8 ms                                                     | 44.3 ms: 1.28x faster                                           |
| comprehensions             | 14.1 us                                                     | 11.5 us: 1.23x faster                                           |
| go                         | 91.6 ms                                                     | 78.2 ms: 1.17x faster                                           |
| generators                 | 22.5 ms                                                     | 19.9 ms: 1.13x faster                                           |
| nbody                      | 71.9 ms                                                     | 64.3 ms: 1.12x faster                                           |
| deepcopy_reduce            | 2.09 us                                                     | 1.88 us: 1.12x faster                                           |
| chaos                      | 43.3 ms                                                     | 39.0 ms: 1.11x faster                                           |
| spectral_norm              | 66.9 ms                                                     | 60.4 ms: 1.11x faster                                           |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                           |
| regex_compile              | 87.5 ms                                                     | 81.8 ms: 1.07x faster                                           |
| dulwich_log                | 44.3 ms                                                     | 41.8 ms: 1.06x faster                                           |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.4 ms: 1.06x faster                                           |
| mako                       | 7.09 ms                                                     | 6.71 ms: 1.06x faster                                           |
| pyflate                    | 295 ms                                                      | 281 ms: 1.05x faster                                            |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                            |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.03x faster                                           |
| sympy_sum                  | 91.5 ms                                                     | 88.8 ms: 1.03x faster                                           |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                            |
| xml_etree_parse            | 93.0 ms                                                     | 90.4 ms: 1.03x faster                                           |
| raytrace                   | 192 ms                                                      | 187 ms: 1.03x faster                                            |
| coroutines                 | 14.3 ms                                                     | 13.9 ms: 1.02x faster                                           |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.02x faster                                            |
| richards                   | 28.4 ms                                                     | 27.8 ms: 1.02x faster                                           |
| pprint_pformat             | 1.05 sec                                                    | 1.02 sec: 1.02x faster                                          |
| crypto_pyaes               | 48.5 ms                                                     | 47.6 ms: 1.02x faster                                           |
| scimark_sor                | 78.8 ms                                                     | 77.5 ms: 1.02x faster                                           |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.2 ms: 1.02x faster                                           |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                           |
| json                       | 3.05 ms                                                     | 3.00 ms: 1.01x faster                                           |
| async_generators           | 239 ms                                                      | 236 ms: 1.01x faster                                            |
| richards_super             | 32.1 ms                                                     | 31.7 ms: 1.01x faster                                           |
| pprint_safe_repr           | 513 ms                                                      | 507 ms: 1.01x faster                                            |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                          |
| meteor_contest             | 74.6 ms                                                     | 74.1 ms: 1.01x faster                                           |
| deltablue                  | 2.16 ms                                                     | 2.18 ms: 1.01x slower                                           |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.59 ms: 1.01x slower                                           |
| unpickle_pure_python       | 133 us                                                      | 136 us: 1.02x slower                                            |
| scimark_lu                 | 58.9 ms                                                     | 60.1 ms: 1.02x slower                                           |
| hexiom                     | 4.10 ms                                                     | 4.19 ms: 1.02x slower                                           |
| pycparser                  | 699 ms                                                      | 716 ms: 1.03x slower                                            |
| xml_etree_generate         | 55.8 ms                                                     | 57.4 ms: 1.03x slower                                           |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                            |
| logging_simple             | 6.28 us                                                     | 6.49 us: 1.03x slower                                           |
| logging_format             | 6.72 us                                                     | 6.98 us: 1.04x slower                                           |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                          |
| sympy_expand               | 284 ms                                                      | 297 ms: 1.05x slower                                            |
| fannkuch                   | 247 ms                                                      | 259 ms: 1.05x slower                                            |
| xml_etree_process          | 37.7 ms                                                     | 39.7 ms: 1.05x slower                                           |
| json_loads                 | 13.9 us                                                     | 14.8 us: 1.07x slower                                           |
| pickle_pure_python         | 195 us                                                      | 212 us: 1.08x slower                                            |
| django_template            | 22.9 ms                                                     | 25.0 ms: 1.09x slower                                           |
| telco                      | 4.13 ms                                                     | 4.61 ms: 1.12x slower                                           |
| json_dumps                 | 5.70 ms                                                     | 6.38 ms: 1.12x slower                                           |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.18x slower                                            |
| coverage                   | 40.8 ms                                                     | 49.5 ms: 1.21x slower                                           |
| python_startup_no_site     | 16.2 ms                                                     | 20.1 ms: 1.24x slower                                           |
| python_startup             | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                           |
| gc_traversal               | 1.52 ms                                                     | 2.11 ms: 1.39x slower                                           |
| create_gc_cycles           | 752 us                                                      | 1.31 ms: 1.74x slower                                           |
| logging_silent             | 60.5 ns                                                     | 325 ns: 5.37x slower                                            |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                    |

Benchmark hidden because not significant (3): scimark_fft, nqueens, regex_v8
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250526-3.14.0b2-12d3f88/bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.077x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown
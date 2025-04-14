# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: windows-amd64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.053x faster
- HPT reliability: 80.82%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 229 ms: 1.05x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.75 sec: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 412 ms: 1.87x faster                                                        |
| async_tree_io              | 731 ms                                                      | 417 ms: 1.75x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                                        |
| async_tree_none            | 291 ms                                                      | 188 ms: 1.55x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 221 ms: 1.53x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 336 ms: 1.46x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.62x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 59.7 ms: 1.20x faster                                                       |
| float          | 56.8 ms                                                     | 48.3 ms: 1.18x faster                                                       |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.45 ms: 1.12x faster                                                       |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 13.8 ms: 1.03x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 86.5 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 123 us: 1.08x faster                                                        |
| xml_etree_parse      | 93.0 ms                                                     | 89.0 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.4 ms: 1.04x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 54.2 ms: 1.03x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 38.3 ms: 1.02x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 2.89 us: 1.05x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.60 us: 1.05x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 19.8 us: 1.08x slower                                                       |
| json_loads           | 13.9 us                                                     | 15.1 us: 1.08x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 217 us: 1.11x slower                                                        |
| pickle               | 7.43 us                                                     | 8.49 us: 1.14x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.38 us: 1.20x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 7.04 ms: 1.24x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.2 ms: 1.24x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.88 ms: 1.20x faster                                                       |
| django_template | 22.9 ms                                                     | 26.6 ms: 1.16x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 33.1 ms: 2.43x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 412 ms: 1.87x faster                                                        |
| async_tree_io              | 731 ms                                                      | 417 ms: 1.75x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                                        |
| async_tree_none            | 291 ms                                                      | 188 ms: 1.55x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 221 ms: 1.53x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 336 ms: 1.46x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.45 sec: 1.44x faster                                                      |
| deepcopy                   | 238 us                                                      | 188 us: 1.26x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.88 ms: 1.20x faster                                                       |
| nbody                      | 71.9 ms                                                     | 59.7 ms: 1.20x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.19x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.0 us: 1.19x faster                                                       |
| float                      | 56.8 ms                                                     | 48.3 ms: 1.18x faster                                                       |
| scimark_fft                | 184 ms                                                      | 158 ms: 1.16x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.54 us: 1.14x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.27 ms: 1.13x faster                                                       |
| generators                 | 22.5 ms                                                     | 20.1 ms: 1.12x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.45 ms: 1.12x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 60.2 ms: 1.11x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 123 us: 1.08x faster                                                        |
| pyflate                    | 295 ms                                                      | 276 ms: 1.07x faster                                                        |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 89.0 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.4 ms: 1.04x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.8 ms: 1.03x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 54.2 ms: 1.03x faster                                                       |
| unpack_sequence            | 37.5 ns                                                     | 36.4 ns: 1.03x faster                                                       |
| go                         | 91.6 ms                                                     | 89.2 ms: 1.03x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.04 us: 1.03x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.9 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 86.5 ms: 1.01x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 62.3 ms: 1.01x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 43.9 ms: 1.01x faster                                                       |
| json                       | 3.05 ms                                                     | 3.08 ms: 1.01x slower                                                       |
| chaos                      | 43.3 ms                                                     | 43.8 ms: 1.01x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 520 ms: 1.01x slower                                                        |
| xml_etree_process          | 37.7 ms                                                     | 38.3 ms: 1.02x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 49.5 ms: 1.02x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 61.8 ns: 1.02x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 76.3 ms: 1.02x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 80.6 ms: 1.02x slower                                                       |
| fannkuch                   | 247 ms                                                      | 253 ms: 1.02x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 60.5 ms: 1.03x slower                                                       |
| raytrace                   | 192 ms                                                      | 199 ms: 1.04x slower                                                        |
| async_generators           | 239 ms                                                      | 249 ms: 1.04x slower                                                        |
| sympy_str                  | 175 ms                                                      | 182 ms: 1.04x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.05x slower                                                       |
| 2to3                       | 218 ms                                                      | 229 ms: 1.05x slower                                                        |
| unpickle_list              | 2.75 us                                                     | 2.89 us: 1.05x slower                                                       |
| richards                   | 28.4 ms                                                     | 29.8 ms: 1.05x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.60 us: 1.05x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.61 us: 1.05x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.75 sec: 1.05x slower                                                      |
| richards_super             | 32.1 ms                                                     | 33.9 ms: 1.06x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 518 ms: 1.06x slower                                                        |
| pycparser                  | 699 ms                                                      | 746 ms: 1.07x slower                                                        |
| logging_format             | 6.72 us                                                     | 7.18 us: 1.07x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 19.8 us: 1.08x slower                                                       |
| json_loads                 | 13.9 us                                                     | 15.1 us: 1.08x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.50 sec: 1.10x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 217 us: 1.11x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.41 ms: 1.11x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.63 ms: 1.12x slower                                                       |
| sympy_expand               | 284 ms                                                      | 322 ms: 1.13x slower                                                        |
| pickle                     | 7.43 us                                                     | 8.49 us: 1.14x slower                                                       |
| django_template            | 22.9 ms                                                     | 26.6 ms: 1.16x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.82 ms: 1.18x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.38 us: 1.20x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 115 us: 1.21x slower                                                        |
| coverage                   | 40.8 ms                                                     | 50.4 ms: 1.23x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 7.04 ms: 1.24x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.2 ms: 1.24x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.7 ms: 1.28x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.04 ms: 1.34x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.24 ms: 1.64x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (4): pprint_pformat, sympy_sum, scimark_monte_carlo, bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 80.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
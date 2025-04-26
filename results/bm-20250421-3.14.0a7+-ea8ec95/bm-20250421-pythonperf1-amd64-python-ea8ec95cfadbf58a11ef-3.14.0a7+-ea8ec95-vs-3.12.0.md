# Results vs. 3.12.0

- fork: python
- ref: ea8ec95cfadbf58a11ef
- machine: windows-amd64
- commit hash: ea8ec95
- commit date: 2025-04-21
- overall geometric mean: 1.100x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 397 ms: 1.94x faster                                                        |
| async_tree_io              | 731 ms                                                      | 408 ms: 1.79x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                        |
| async_tree_none            | 291 ms                                                      | 180 ms: 1.62x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 336 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.67x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 42.3 ms: 1.34x faster                                                       |
| nbody          | 71.9 ms                                                     | 62.2 ms: 1.16x faster                                                       |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.41 ms: 1.15x faster                                                       |
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 79.6 ms: 1.10x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.4 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.4 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.7 ms: 1.02x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 134 us: 1.01x slower                                                        |
| xml_etree_process    | 37.7 ms                                                     | 39.5 ms: 1.05x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 209 us: 1.07x slower                                                        |
| json_loads           | 13.9 us                                                     | 14.9 us: 1.07x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.80 ms: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.5 ms: 1.26x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.3 ms: 1.35x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.61 ms: 1.07x faster                                                       |
| django_template | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.4 ms: 2.48x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 397 ms: 1.94x faster                                                        |
| async_tree_io              | 731 ms                                                      | 408 ms: 1.79x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                        |
| mdp                        | 1.37 sec                                                    | 785 ms: 1.75x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                        |
| async_tree_none            | 291 ms                                                      | 180 ms: 1.62x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 336 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                        |
| deepcopy                   | 238 us                                                      | 170 us: 1.40x faster                                                        |
| float                      | 56.8 ms                                                     | 42.3 ms: 1.34x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.2 us: 1.30x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.1 us: 1.27x faster                                                       |
| go                         | 91.6 ms                                                     | 75.8 ms: 1.21x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 56.4 ms: 1.19x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.79 us: 1.17x faster                                                       |
| nbody                      | 71.9 ms                                                     | 62.2 ms: 1.16x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.41 ms: 1.15x faster                                                       |
| chaos                      | 43.3 ms                                                     | 37.9 ms: 1.14x faster                                                       |
| generators                 | 22.5 ms                                                     | 20.1 ms: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                       |
| raytrace                   | 192 ms                                                      | 174 ms: 1.10x faster                                                        |
| logging_silent             | 60.5 ns                                                     | 54.9 ns: 1.10x faster                                                       |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 79.6 ms: 1.10x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.9 ms: 1.10x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.61 ms: 1.07x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.4 ms: 1.07x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 59.0 ms: 1.06x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.4 ms: 1.06x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.9 ms: 1.06x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 486 ms: 1.06x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 991 ms: 1.05x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 75.0 ms: 1.05x faster                                                       |
| pyflate                    | 295 ms                                                      | 281 ms: 1.05x faster                                                        |
| async_generators           | 239 ms                                                      | 229 ms: 1.05x faster                                                        |
| sympy_sum                  | 91.5 ms                                                     | 87.8 ms: 1.04x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 3.94 ms: 1.04x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 89.4 ms: 1.04x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.04x faster                                                       |
| scimark_fft                | 184 ms                                                      | 178 ms: 1.04x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 46.7 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.47 ms: 1.03x faster                                                       |
| richards                   | 28.4 ms                                                     | 27.6 ms: 1.03x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.10 ms: 1.03x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 72.7 ms: 1.03x faster                                                       |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.7 ms: 1.02x faster                                                       |
| richards_super             | 32.1 ms                                                     | 31.4 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                                       |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 134 us: 1.01x slower                                                        |
| logging_format             | 6.72 us                                                     | 6.80 us: 1.01x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.35 us: 1.01x slower                                                       |
| fannkuch                   | 247 ms                                                      | 250 ms: 1.01x slower                                                        |
| json                       | 3.05 ms                                                     | 3.10 ms: 1.02x slower                                                       |
| sympy_expand               | 284 ms                                                      | 295 ms: 1.04x slower                                                        |
| django_template            | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.5 ms: 1.05x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 209 us: 1.07x slower                                                        |
| json_loads                 | 13.9 us                                                     | 14.9 us: 1.07x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.53 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.11x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.80 ms: 1.19x slower                                                       |
| coverage                   | 40.8 ms                                                     | 49.8 ms: 1.22x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.5 ms: 1.26x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 89.4 ms: 1.29x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.3 ms: 1.35x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.11 ms: 1.38x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.26 ms: 1.67x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (3): scimark_lu, pycparser, bench_thread_pool
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250421-3.14.0a7+-ea8ec95/bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.100x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown
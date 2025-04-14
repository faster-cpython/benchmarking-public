# Results vs. 3.12.0

- fork: python
- ref: 85bc489b649fe261f962
- machine: windows-amd64
- commit hash: 85bc489
- commit date: 2025-04-05
- overall geometric mean: 1.103x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.70 sec: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 393 ms: 1.96x faster                                                        |
| async_tree_io              | 731 ms                                                      | 408 ms: 1.79x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.69x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                        |
| async_tree_none            | 291 ms                                                      | 179 ms: 1.62x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 336 ms: 1.50x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.3 ms: 1.31x faster                                                       |
| nbody          | 71.9 ms                                                     | 57.0 ms: 1.26x faster                                                       |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                       |
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 80.6 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 119 us: 1.12x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 51.4 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.2 ms: 1.03x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.9 ms: 1.02x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 92.1 ms: 1.01x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.78 us: 1.01x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 19.5 us: 1.06x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.70 us: 1.06x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 208 us: 1.06x slower                                                        |
| json_loads           | 13.9 us                                                     | 15.2 us: 1.09x slower                                                       |
| pickle               | 7.43 us                                                     | 8.18 us: 1.10x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.76 ms: 1.19x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.39 us: 1.20x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.5 ms: 1.26x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.3 ms: 1.35x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.67 ms: 1.25x faster                                                       |
| django_template | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.3 ms: 2.49x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 393 ms: 1.96x faster                                                        |
| async_tree_io              | 731 ms                                                      | 408 ms: 1.79x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                        |
| mdp                        | 1.37 sec                                                    | 797 ms: 1.72x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.69x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                        |
| async_tree_none            | 291 ms                                                      | 179 ms: 1.62x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 336 ms: 1.50x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.46 sec: 1.44x faster                                                      |
| deepcopy                   | 238 us                                                      | 177 us: 1.35x faster                                                        |
| float                      | 56.8 ms                                                     | 43.3 ms: 1.31x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.4 us: 1.29x faster                                                       |
| nbody                      | 71.9 ms                                                     | 57.0 ms: 1.26x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.67 ms: 1.25x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 56.5 ms: 1.19x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.0 us: 1.18x faster                                                       |
| scimark_fft                | 184 ms                                                      | 157 ms: 1.18x faster                                                        |
| generators                 | 22.5 ms                                                     | 19.2 ms: 1.17x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                      |
| go                         | 91.6 ms                                                     | 80.3 ms: 1.14x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.13x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.85 us: 1.13x faster                                                       |
| raytrace                   | 192 ms                                                      | 171 ms: 1.13x faster                                                        |
| pyflate                    | 295 ms                                                      | 262 ms: 1.13x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 119 us: 1.12x faster                                                        |
| chaos                      | 43.3 ms                                                     | 39.0 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.32 ms: 1.10x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 55.0 ns: 1.10x faster                                                       |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 51.4 ms: 1.09x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 963 ms: 1.09x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 80.6 ms: 1.09x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.5 ms: 1.08x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 482 ms: 1.07x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 74.2 ms: 1.06x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 45.8 ms: 1.06x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.7 ms: 1.04x faster                                                       |
| richards                   | 28.4 ms                                                     | 27.4 ms: 1.04x faster                                                       |
| fannkuch                   | 247 ms                                                      | 238 ms: 1.04x faster                                                        |
| nqueens                    | 62.8 ms                                                     | 60.8 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.2 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| xml_etree_process          | 37.7 ms                                                     | 36.9 ms: 1.02x faster                                                       |
| richards_super             | 32.1 ms                                                     | 31.5 ms: 1.02x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.9 ms: 1.02x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.21 us: 1.01x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 58.3 ms: 1.01x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 92.1 ms: 1.01x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 4.12 ms: 1.01x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.1 ms: 1.01x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.78 us: 1.01x slower                                                       |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                        |
| pycparser                  | 699 ms                                                      | 715 ms: 1.02x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.70 sec: 1.03x slower                                                      |
| json                       | 3.05 ms                                                     | 3.15 ms: 1.03x slower                                                       |
| async_generators           | 239 ms                                                      | 248 ms: 1.04x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.35 ms: 1.05x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 19.5 us: 1.06x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 517 ms: 1.06x slower                                                        |
| unpickle                   | 8.18 us                                                     | 8.70 us: 1.06x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 208 us: 1.06x slower                                                        |
| sympy_expand               | 284 ms                                                      | 305 ms: 1.07x slower                                                        |
| json_loads                 | 13.9 us                                                     | 15.2 us: 1.09x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                       |
| pickle                     | 7.43 us                                                     | 8.18 us: 1.10x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.76 ms: 1.19x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.39 us: 1.20x slower                                                       |
| coverage                   | 40.8 ms                                                     | 51.1 ms: 1.25x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.5 ms: 1.26x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.3 ms: 1.28x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.3 ms: 1.35x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.09 ms: 1.37x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.24 ms: 1.64x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (8): bench_thread_pool, coroutines, meteor_contest, sympy_str, regex_v8, deltablue, logging_format, unpack_sequence
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250405-3.14.0a6+-85bc489-JIT/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.103x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown
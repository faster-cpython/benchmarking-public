# Results vs. 3.12.0

- fork: JelleZijlstra
- ref: sunder_io
- machine: windows-amd64
- commit hash: dac50cc
- commit date: 2025-04-25
- overall geometric mean: 1.088x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                       | 1.01x slower                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 395 ms: 1.95x faster                                                    |
| async_tree_io              | 731 ms                                                      | 413 ms: 1.77x faster                                                    |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.74x faster                                                    |
| async_tree_none_tg         | 285 ms                                                      | 172 ms: 1.66x faster                                                    |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                    |
| async_tree_none            | 291 ms                                                      | 183 ms: 1.60x faster                                                    |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 338 ms: 1.48x faster                                                    |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                    |
| Geometric mean             | (ref)                                                       | 1.66x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 42.8 ms: 1.33x faster                                                   |
| nbody          | 71.9 ms                                                     | 63.0 ms: 1.14x faster                                                   |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                       | 1.16x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.43 ms: 1.13x faster                                                   |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                    |
| regex_compile  | 87.5 ms                                                     | 81.5 ms: 1.07x faster                                                   |
| regex_v8       | 14.2 ms                                                     | 13.9 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                       | 1.08x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.9 ms: 1.05x faster                                                   |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.3 ms: 1.01x faster                                                   |
| unpickle_pure_python | 133 us                                                      | 135 us: 1.02x slower                                                    |
| tomli_loads          | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                  |
| xml_etree_process    | 37.7 ms                                                     | 40.0 ms: 1.06x slower                                                   |
| pickle_pure_python   | 195 us                                                      | 210 us: 1.08x slower                                                    |
| json_loads           | 13.9 us                                                     | 15.4 us: 1.10x slower                                                   |
| json_dumps           | 5.70 ms                                                     | 6.90 ms: 1.21x slower                                                   |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                   |
| python_startup         | 19.5 ms                                                     | 26.6 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.68 ms: 1.06x faster                                                   |
| django_template | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.5 ms: 2.47x faster                                                   |
| async_tree_io_tg           | 771 ms                                                      | 395 ms: 1.95x faster                                                    |
| async_tree_io              | 731 ms                                                      | 413 ms: 1.77x faster                                                    |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.74x faster                                                    |
| mdp                        | 1.37 sec                                                    | 789 ms: 1.74x faster                                                    |
| async_tree_none_tg         | 285 ms                                                      | 172 ms: 1.66x faster                                                    |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                    |
| async_tree_none            | 291 ms                                                      | 183 ms: 1.60x faster                                                    |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 338 ms: 1.48x faster                                                    |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                    |
| deepcopy                   | 238 us                                                      | 175 us: 1.36x faster                                                    |
| float                      | 56.8 ms                                                     | 42.8 ms: 1.33x faster                                                   |
| deepcopy_memo              | 23.7 us                                                     | 18.6 us: 1.28x faster                                                   |
| comprehensions             | 14.1 us                                                     | 11.2 us: 1.26x faster                                                   |
| generators                 | 22.5 ms                                                     | 19.1 ms: 1.18x faster                                                   |
| deepcopy_reduce            | 2.09 us                                                     | 1.80 us: 1.16x faster                                                   |
| go                         | 91.6 ms                                                     | 79.0 ms: 1.16x faster                                                   |
| spectral_norm              | 66.9 ms                                                     | 57.8 ms: 1.16x faster                                                   |
| nbody                      | 71.9 ms                                                     | 63.0 ms: 1.14x faster                                                   |
| regex_effbot               | 1.62 ms                                                     | 1.43 ms: 1.13x faster                                                   |
| chaos                      | 43.3 ms                                                     | 38.6 ms: 1.12x faster                                                   |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                   |
| raytrace                   | 192 ms                                                      | 175 ms: 1.10x faster                                                    |
| logging_silent             | 60.5 ns                                                     | 55.1 ns: 1.10x faster                                                   |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.3 ms: 1.08x faster                                                   |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                    |
| regex_compile              | 87.5 ms                                                     | 81.5 ms: 1.07x faster                                                   |
| mako                       | 7.09 ms                                                     | 6.68 ms: 1.06x faster                                                   |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.05x faster                                                   |
| scimark_fft                | 184 ms                                                      | 176 ms: 1.05x faster                                                    |
| xml_etree_parse            | 93.0 ms                                                     | 88.9 ms: 1.05x faster                                                   |
| async_generators           | 239 ms                                                      | 230 ms: 1.04x faster                                                    |
| dulwich_log                | 44.3 ms                                                     | 42.6 ms: 1.04x faster                                                   |
| sympy_sum                  | 91.5 ms                                                     | 88.3 ms: 1.04x faster                                                   |
| pprint_pformat             | 1.05 sec                                                    | 1.01 sec: 1.04x faster                                                  |
| pyflate                    | 295 ms                                                      | 285 ms: 1.03x faster                                                    |
| sympy_integrate            | 13.0 ms                                                     | 12.6 ms: 1.03x faster                                                   |
| pprint_safe_repr           | 513 ms                                                      | 499 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.49 ms: 1.03x faster                                                   |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                    |
| richards                   | 28.4 ms                                                     | 27.7 ms: 1.03x faster                                                   |
| regex_v8                   | 14.2 ms                                                     | 13.9 ms: 1.02x faster                                                   |
| nqueens                    | 62.8 ms                                                     | 61.5 ms: 1.02x faster                                                   |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                    |
| richards_super             | 32.1 ms                                                     | 31.5 ms: 1.02x faster                                                   |
| crypto_pyaes               | 48.5 ms                                                     | 47.7 ms: 1.02x faster                                                   |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.3 ms: 1.01x faster                                                   |
| scimark_sor                | 78.8 ms                                                     | 78.1 ms: 1.01x faster                                                   |
| meteor_contest             | 74.6 ms                                                     | 74.1 ms: 1.01x faster                                                   |
| scimark_lu                 | 58.9 ms                                                     | 59.1 ms: 1.00x slower                                                   |
| logging_simple             | 6.28 us                                                     | 6.32 us: 1.01x slower                                                   |
| hexiom                     | 4.10 ms                                                     | 4.13 ms: 1.01x slower                                                   |
| deltablue                  | 2.16 ms                                                     | 2.19 ms: 1.01x slower                                                   |
| logging_format             | 6.72 us                                                     | 6.81 us: 1.01x slower                                                   |
| 2to3                       | 218 ms                                                      | 221 ms: 1.02x slower                                                    |
| unpickle_pure_python       | 133 us                                                      | 135 us: 1.02x slower                                                    |
| pycparser                  | 699 ms                                                      | 714 ms: 1.02x slower                                                    |
| fannkuch                   | 247 ms                                                      | 255 ms: 1.04x slower                                                    |
| tomli_loads                | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                  |
| sympy_expand               | 284 ms                                                      | 295 ms: 1.04x slower                                                    |
| bench_thread_pool          | 857 us                                                      | 894 us: 1.04x slower                                                    |
| django_template            | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                   |
| xml_etree_process          | 37.7 ms                                                     | 40.0 ms: 1.06x slower                                                   |
| pickle_pure_python         | 195 us                                                      | 210 us: 1.08x slower                                                    |
| json_loads                 | 13.9 us                                                     | 15.4 us: 1.10x slower                                                   |
| telco                      | 4.13 ms                                                     | 4.60 ms: 1.11x slower                                                   |
| typing_runtime_protocols   | 95.1 us                                                     | 107 us: 1.12x slower                                                    |
| python_startup_no_site     | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                   |
| json_dumps                 | 5.70 ms                                                     | 6.90 ms: 1.21x slower                                                   |
| coverage                   | 40.8 ms                                                     | 51.5 ms: 1.26x slower                                                   |
| bench_mp_pool              | 69.2 ms                                                     | 89.4 ms: 1.29x slower                                                   |
| gc_traversal               | 1.52 ms                                                     | 2.07 ms: 1.36x slower                                                   |
| python_startup             | 19.5 ms                                                     | 26.6 ms: 1.36x slower                                                   |
| create_gc_cycles           | 752 us                                                      | 1.24 ms: 1.65x slower                                                   |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                            |

Benchmark hidden because not significant (3): xml_etree_generate, docutils, json
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250425-3.14.0a7+-dac50cc/bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.088x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown
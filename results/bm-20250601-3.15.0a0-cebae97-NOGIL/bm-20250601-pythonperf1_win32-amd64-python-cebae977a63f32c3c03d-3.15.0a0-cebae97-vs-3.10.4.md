# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.229x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 338 ms: 1.27x slower                                                             |
| docutils       | 1.95 sec                                                        | 4.13 sec: 2.12x slower                                                           |
| html5lib       | 52.1 ms                                                         | 63.6 ms: 1.22x slower                                                            |
| Geometric mean | (ref)                                                           | 1.49x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 488 ms: 1.89x faster                                                             |
| async_tree_io           | 940 ms                                                          | 574 ms: 1.64x faster                                                             |
| async_tree_none         | 394 ms                                                          | 272 ms: 1.45x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 337 ms: 1.38x faster                                                             |
| Geometric mean          | (ref)                                                           | 1.58x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 140 ms: 3.60x faster                                                             |
| float          | 69.6 ms                                                         | 96.6 ms: 1.39x slower                                                            |
| nbody          | 79.1 ms                                                         | 181 ms: 2.28x slower                                                             |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 113 ms: 1.15x faster                                                             |
| regex_v8       | 15.8 ms                                                         | 16.9 ms: 1.07x slower                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.83 ms: 1.10x slower                                                            |
| regex_compile  | 117 ms                                                          | 160 ms: 1.37x slower                                                             |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 111 ms: 1.08x faster                                                             |
| json_dumps           | 9.82 ms                                                         | 9.50 ms: 1.03x faster                                                            |
| json_loads           | 22.4 us                                                         | 22.1 us: 1.01x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 3.42 us: 1.15x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.76 us: 1.17x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 21.5 us: 1.18x slower                                                            |
| pickle               | 7.83 us                                                         | 9.63 us: 1.23x slower                                                            |
| unpickle             | 9.82 us                                                         | 12.6 us: 1.28x slower                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 92.3 ms: 1.30x slower                                                            |
| pickle_pure_python   | 280 us                                                          | 453 us: 1.62x slower                                                             |
| xml_etree_process    | 48.1 ms                                                         | 79.8 ms: 1.66x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 107 ms: 1.74x slower                                                             |
| unpickle_pure_python | 189 us                                                          | 360 us: 1.90x slower                                                             |
| tomli_loads          | 1.91 sec                                                        | 5.09 sec: 2.67x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.35x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                            |
| python_startup         | 22.9 ms                                                         | 27.8 ms: 1.21x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.17x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 45.8 ms: 1.27x slower                                                            |
| genshi_xml      | 46.6 ms                                                         | 66.2 ms: 1.42x slower                                                            |
| genshi_text     | 21.0 ms                                                         | 33.3 ms: 1.59x slower                                                            |
| mako            | 9.10 ms                                                         | 16.8 ms: 1.85x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.52x slower                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 2.56 sec: 6.63x faster                                                           |
| pidigits                 | 502 ms                                                          | 140 ms: 3.60x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 35.5 ms: 2.29x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 201 us: 1.97x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 488 ms: 1.89x faster                                                             |
| async_tree_io            | 940 ms                                                          | 574 ms: 1.64x faster                                                             |
| async_tree_none          | 394 ms                                                          | 272 ms: 1.45x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 529 ms: 1.41x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 337 ms: 1.38x faster                                                             |
| pylint                   | 384 ms                                                          | 279 ms: 1.38x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.70 us: 1.35x faster                                                            |
| regex_dna                | 131 ms                                                          | 113 ms: 1.15x faster                                                             |
| json                     | 4.76 ms                                                         | 4.17 ms: 1.14x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 111 ms: 1.08x faster                                                             |
| thrift                   | 902 us                                                          | 842 us: 1.07x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 56.0 ms: 1.04x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 9.50 ms: 1.03x faster                                                            |
| json_loads               | 22.4 us                                                         | 22.1 us: 1.01x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 16.9 ms: 1.07x slower                                                            |
| deepcopy                 | 310 us                                                          | 334 us: 1.08x slower                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.83 ms: 1.10x slower                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.25 ms: 1.12x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                            |
| unpickle_list            | 2.98 us                                                         | 3.42 us: 1.15x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.76 us: 1.17x slower                                                            |
| sympy_sum                | 122 ms                                                          | 144 ms: 1.18x slower                                                             |
| pickle_dict              | 18.2 us                                                         | 21.5 us: 1.18x slower                                                            |
| python_startup           | 22.9 ms                                                         | 27.8 ms: 1.21x slower                                                            |
| html5lib                 | 52.1 ms                                                         | 63.6 ms: 1.22x slower                                                            |
| pickle                   | 7.83 us                                                         | 9.63 us: 1.23x slower                                                            |
| generators               | 31.6 ms                                                         | 39.4 ms: 1.25x slower                                                            |
| sympy_expand             | 391 ms                                                          | 493 ms: 1.26x slower                                                             |
| sympy_integrate          | 16.6 ms                                                         | 21.0 ms: 1.26x slower                                                            |
| mdp                      | 1.83 sec                                                        | 2.31 sec: 1.26x slower                                                           |
| django_template          | 36.0 ms                                                         | 45.8 ms: 1.27x slower                                                            |
| 2to3                     | 265 ms                                                          | 338 ms: 1.27x slower                                                             |
| sympy_str                | 229 ms                                                          | 293 ms: 1.28x slower                                                             |
| unpickle                 | 9.82 us                                                         | 12.6 us: 1.28x slower                                                            |
| chaos                    | 74.4 ms                                                         | 95.9 ms: 1.29x slower                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 3.48 us: 1.30x slower                                                            |
| go                       | 146 ms                                                          | 190 ms: 1.30x slower                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 92.3 ms: 1.30x slower                                                            |
| raytrace                 | 303 ms                                                          | 403 ms: 1.33x slower                                                             |
| bench_mp_pool            | 66.4 ms                                                         | 88.5 ms: 1.33x slower                                                            |
| regex_compile            | 117 ms                                                          | 160 ms: 1.37x slower                                                             |
| gc_traversal             | 1.28 ms                                                         | 1.78 ms: 1.39x slower                                                            |
| float                    | 69.6 ms                                                         | 96.6 ms: 1.39x slower                                                            |
| genshi_xml               | 46.6 ms                                                         | 66.2 ms: 1.42x slower                                                            |
| deltablue                | 4.04 ms                                                         | 5.83 ms: 1.44x slower                                                            |
| deepcopy_memo            | 29.6 us                                                         | 43.3 us: 1.46x slower                                                            |
| nqueens                  | 87.1 ms                                                         | 128 ms: 1.47x slower                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 120 ms: 1.47x slower                                                             |
| logging_format           | 7.91 us                                                         | 11.7 us: 1.48x slower                                                            |
| comprehensions           | 17.7 us                                                         | 26.2 us: 1.48x slower                                                            |
| pyflate                  | 422 ms                                                          | 631 ms: 1.50x slower                                                             |
| meteor_contest           | 80.0 ms                                                         | 120 ms: 1.51x slower                                                             |
| logging_simple           | 7.29 us                                                         | 11.1 us: 1.53x slower                                                            |
| genshi_text              | 21.0 ms                                                         | 33.3 ms: 1.59x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.10 ms: 1.59x slower                                                            |
| richards_super           | 49.9 ms                                                         | 79.3 ms: 1.59x slower                                                            |
| pickle_pure_python       | 280 us                                                          | 453 us: 1.62x slower                                                             |
| pycparser                | 1.04 sec                                                        | 1.71 sec: 1.64x slower                                                           |
| scimark_sor              | 115 ms                                                          | 190 ms: 1.65x slower                                                             |
| xml_etree_process        | 48.1 ms                                                         | 79.8 ms: 1.66x slower                                                            |
| telco                    | 4.83 ms                                                         | 8.03 ms: 1.66x slower                                                            |
| async_generators         | 241 ms                                                          | 408 ms: 1.69x slower                                                             |
| scimark_monte_carlo      | 61.9 ms                                                         | 107 ms: 1.73x slower                                                             |
| richards                 | 40.3 ms                                                         | 69.8 ms: 1.74x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 107 ms: 1.74x slower                                                             |
| hexiom                   | 6.13 ms                                                         | 10.7 ms: 1.75x slower                                                            |
| coroutines               | 17.9 ms                                                         | 32.5 ms: 1.82x slower                                                            |
| coverage                 | 46.6 ms                                                         | 84.7 ms: 1.82x slower                                                            |
| mako                     | 9.10 ms                                                         | 16.8 ms: 1.85x slower                                                            |
| scimark_lu               | 89.8 ms                                                         | 168 ms: 1.87x slower                                                             |
| fannkuch                 | 317 ms                                                          | 593 ms: 1.87x slower                                                             |
| unpickle_pure_python     | 189 us                                                          | 360 us: 1.90x slower                                                             |
| scimark_fft              | 216 ms                                                          | 416 ms: 1.92x slower                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 6.40 ms: 1.98x slower                                                            |
| unpack_sequence          | 40.0 ns                                                         | 83.0 ns: 2.07x slower                                                            |
| spectral_norm            | 80.2 ms                                                         | 170 ms: 2.12x slower                                                             |
| docutils                 | 1.95 sec                                                        | 4.13 sec: 2.12x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 1.49 sec: 2.26x slower                                                           |
| nbody                    | 79.1 ms                                                         | 181 ms: 2.28x slower                                                             |
| tomli_loads              | 1.91 sec                                                        | 5.09 sec: 2.67x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 4.23 sec: 3.09x slower                                                           |
| logging_silent           | 97.9 ns                                                         | 574 ns: 5.86x slower                                                             |
| Geometric mean           | (ref)                                                           | 1.28x slower                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.229x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.32x
- 95% likely to have a slowdown of 1.29x
- 99% likely to have a slowdown of 1.27x

# Memory
- memory change: unknown
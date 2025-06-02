# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.369x faster
- HPT reliability: 77.82%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 285 ms: 1.08x slower                                                             |
| docutils       | 1.95 sec                                                        | 2.06 sec: 1.06x slower                                                           |
| html5lib       | 52.1 ms                                                         | 51.3 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 426 ms: 2.16x faster                                                             |
| async_tree_io           | 940 ms                                                          | 535 ms: 1.76x faster                                                             |
| async_tree_none         | 394 ms                                                          | 230 ms: 1.71x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 281 ms: 1.66x faster                                                             |
| Geometric mean          | (ref)                                                           | 1.81x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 145 ms: 3.46x faster                                                             |
| nbody          | 79.1 ms                                                         | 55.8 ms: 1.42x faster                                                            |
| float          | 69.6 ms                                                         | 78.1 ms: 1.12x slower                                                            |
| Geometric mean | (ref)                                                           | 1.64x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 117 ms: 1.11x faster                                                             |
| regex_compile  | 117 ms                                                          | 112 ms: 1.04x faster                                                             |
| regex_v8       | 15.8 ms                                                         | 16.4 ms: 1.04x slower                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.78 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.55 sec: 1.23x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 155 us: 1.22x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 103 ms: 1.16x faster                                                             |
| json_dumps           | 9.82 ms                                                         | 8.76 ms: 1.12x faster                                                            |
| json_loads           | 22.4 us                                                         | 20.3 us: 1.10x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 3.05 us: 1.02x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 50.9 ms: 1.06x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 69.5 ms: 1.13x slower                                                            |
| unpickle             | 9.82 us                                                         | 11.2 us: 1.14x slower                                                            |
| pickle_pure_python   | 280 us                                                          | 318 us: 1.14x slower                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 84.8 ms: 1.20x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 22.0 us: 1.20x slower                                                            |
| pickle               | 7.83 us                                                         | 9.45 us: 1.21x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.93 us: 1.22x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                            |
| python_startup         | 22.9 ms                                                         | 27.2 ms: 1.19x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.11 ms: 1.28x faster                                                            |
| django_template | 36.0 ms                                                         | 37.3 ms: 1.04x slower                                                            |
| genshi_xml      | 46.6 ms                                                         | 49.0 ms: 1.05x slower                                                            |
| genshi_text     | 21.0 ms                                                         | 24.1 ms: 1.15x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.01x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pprint_pformat           | 1.37 sec                                                        | 1.56 us: 875792.72x faster                                                       |
| pprint_safe_repr         | 658 ms                                                          | 900 ns: 731610.62x faster                                                        |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.49 sec: 11.43x faster                                                          |
| pidigits                 | 502 ms                                                          | 145 ms: 3.46x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 144 us: 2.74x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 33.8 ms: 2.40x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 426 ms: 2.16x faster                                                             |
| async_tree_io            | 940 ms                                                          | 535 ms: 1.76x faster                                                             |
| async_tree_none          | 394 ms                                                          | 230 ms: 1.71x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 281 ms: 1.66x faster                                                             |
| pylint                   | 384 ms                                                          | 247 ms: 1.55x faster                                                             |
| mdp                      | 1.83 sec                                                        | 1.20 sec: 1.53x faster                                                           |
| nbody                    | 79.1 ms                                                         | 55.8 ms: 1.42x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 557 ms: 1.34x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.73 us: 1.32x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 62.0 ms: 1.31x faster                                                            |
| mako                     | 9.10 ms                                                         | 7.11 ms: 1.28x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.61 ms: 1.24x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.55 sec: 1.23x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 155 us: 1.22x faster                                                             |
| json                     | 4.76 ms                                                         | 4.01 ms: 1.19x faster                                                            |
| scimark_fft              | 216 ms                                                          | 184 ms: 1.17x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 103 ms: 1.16x faster                                                             |
| comprehensions           | 17.7 us                                                         | 15.4 us: 1.15x faster                                                            |
| deepcopy                 | 310 us                                                          | 269 us: 1.15x faster                                                             |
| chaos                    | 74.4 ms                                                         | 64.9 ms: 1.15x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 981 us: 1.14x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 8.76 ms: 1.12x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 52.2 ms: 1.12x faster                                                            |
| pycparser                | 1.04 sec                                                        | 930 ms: 1.12x faster                                                             |
| regex_dna                | 131 ms                                                          | 117 ms: 1.11x faster                                                             |
| fannkuch                 | 317 ms                                                          | 285 ms: 1.11x faster                                                             |
| pyflate                  | 422 ms                                                          | 383 ms: 1.10x faster                                                             |
| json_loads               | 22.4 us                                                         | 20.3 us: 1.10x faster                                                            |
| go                       | 146 ms                                                          | 132 ms: 1.10x faster                                                             |
| sympy_sum                | 122 ms                                                          | 113 ms: 1.09x faster                                                             |
| regex_compile            | 117 ms                                                          | 112 ms: 1.04x faster                                                             |
| html5lib                 | 52.1 ms                                                         | 51.3 ms: 1.02x faster                                                            |
| raytrace                 | 303 ms                                                          | 299 ms: 1.01x faster                                                             |
| sympy_str                | 229 ms                                                          | 231 ms: 1.01x slower                                                             |
| unpickle_list            | 2.98 us                                                         | 3.05 us: 1.02x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 82.2 ms: 1.03x slower                                                            |
| sympy_expand             | 391 ms                                                          | 403 ms: 1.03x slower                                                             |
| django_template          | 36.0 ms                                                         | 37.3 ms: 1.04x slower                                                            |
| regex_v8                 | 15.8 ms                                                         | 16.4 ms: 1.04x slower                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.80 us: 1.04x slower                                                            |
| nqueens                  | 87.1 ms                                                         | 91.1 ms: 1.05x slower                                                            |
| genshi_xml               | 46.6 ms                                                         | 49.0 ms: 1.05x slower                                                            |
| xml_etree_process        | 48.1 ms                                                         | 50.9 ms: 1.06x slower                                                            |
| docutils                 | 1.95 sec                                                        | 2.06 sec: 1.06x slower                                                           |
| telco                    | 4.83 ms                                                         | 5.13 ms: 1.06x slower                                                            |
| deltablue                | 4.04 ms                                                         | 4.30 ms: 1.07x slower                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.78 ms: 1.07x slower                                                            |
| 2to3                     | 265 ms                                                          | 285 ms: 1.08x slower                                                             |
| python_startup_no_site   | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                            |
| float                    | 69.6 ms                                                         | 78.1 ms: 1.12x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 69.5 ms: 1.13x slower                                                            |
| unpickle                 | 9.82 us                                                         | 11.2 us: 1.14x slower                                                            |
| pickle_pure_python       | 280 us                                                          | 318 us: 1.14x slower                                                             |
| scimark_sor              | 115 ms                                                          | 131 ms: 1.14x slower                                                             |
| genshi_text              | 21.0 ms                                                         | 24.1 ms: 1.15x slower                                                            |
| generators               | 31.6 ms                                                         | 36.3 ms: 1.15x slower                                                            |
| deepcopy_memo            | 29.6 us                                                         | 34.2 us: 1.16x slower                                                            |
| richards_super           | 49.9 ms                                                         | 58.2 ms: 1.17x slower                                                            |
| python_startup           | 22.9 ms                                                         | 27.2 ms: 1.19x slower                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 73.8 ms: 1.19x slower                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 84.8 ms: 1.20x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 22.0 us: 1.20x slower                                                            |
| pickle                   | 7.83 us                                                         | 9.45 us: 1.21x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.93 us: 1.22x slower                                                            |
| logging_format           | 7.91 us                                                         | 9.89 us: 1.25x slower                                                            |
| hexiom                   | 6.13 ms                                                         | 7.69 ms: 1.25x slower                                                            |
| richards                 | 40.3 ms                                                         | 51.4 ms: 1.28x slower                                                            |
| logging_simple           | 7.29 us                                                         | 9.40 us: 1.29x slower                                                            |
| scimark_lu               | 89.8 ms                                                         | 120 ms: 1.34x slower                                                             |
| coroutines               | 17.9 ms                                                         | 25.1 ms: 1.40x slower                                                            |
| spectral_norm            | 80.2 ms                                                         | 116 ms: 1.44x slower                                                             |
| async_generators         | 241 ms                                                          | 352 ms: 1.46x slower                                                             |
| bench_mp_pool            | 66.4 ms                                                         | 103 ms: 1.55x slower                                                             |
| unpack_sequence          | 40.0 ns                                                         | 73.7 ns: 1.84x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.41 ms: 2.03x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.72 ms: 2.12x slower                                                            |
| logging_silent           | 97.9 ns                                                         | 498 ns: 5.08x slower                                                             |
| coverage                 | 46.6 ms                                                         | 479 ms: 10.30x slower                                                            |
| thrift                   | 902 us                                                          | 98.5 ms: 109.15x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.31x faster                                                                     |

Benchmark hidden because not significant (1): sympy_integrate
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.369x faster

# HPT report

- Reliability score: 77.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown
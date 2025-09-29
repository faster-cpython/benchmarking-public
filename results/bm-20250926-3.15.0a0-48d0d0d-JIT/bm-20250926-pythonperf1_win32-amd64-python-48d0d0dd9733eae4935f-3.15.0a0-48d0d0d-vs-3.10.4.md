# Results vs. 3.10.4

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.516x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.42x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 214 ms: 1.24x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.62 sec: 1.20x faster                                                           |
| html5lib       | 52.1 ms                                                         | 37.3 ms: 1.40x faster                                                            |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 330 ms: 2.79x faster                                                             |
| async_tree_io           | 940 ms                                                          | 383 ms: 2.45x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 201 ms: 2.32x faster                                                             |
| async_tree_none         | 394 ms                                                          | 170 ms: 2.31x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.46x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 147 ms: 3.43x faster                                                             |
| float          | 69.6 ms                                                         | 39.7 ms: 1.75x faster                                                            |
| nbody          | 79.1 ms                                                         | 53.8 ms: 1.47x faster                                                            |
| Geometric mean | (ref)                                                           | 2.07x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 76.8 ms: 1.52x faster                                                            |
| regex_dna      | 131 ms                                                          | 118 ms: 1.11x faster                                                             |
| regex_v8       | 15.8 ms                                                         | 14.4 ms: 1.09x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 189 us                                                          | 104 us: 1.82x faster                                                             |
| json_dumps           | 9.82 ms                                                         | 5.41 ms: 1.82x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.09 sec: 1.75x faster                                                           |
| json_loads           | 22.4 us                                                         | 14.0 us: 1.59x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 196 us: 1.43x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 86.0 ms: 1.39x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 34.7 ms: 1.39x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 49.7 ms: 1.24x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 60.9 ms: 1.16x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.71 us: 1.13x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.78 us: 1.07x faster                                                            |
| pickle               | 7.83 us                                                         | 8.01 us: 1.02x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.32 us: 1.03x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.8 us: 1.09x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.30x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 18.9 ms: 1.05x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.2 ms: 1.10x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.31 ms: 1.72x faster                                                            |
| django_template | 36.0 ms                                                         | 24.0 ms: 1.50x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.2 ms: 1.36x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.7 ms: 1.34x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.38 sec: 12.29x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 102 us: 3.88x faster                                                             |
| pidigits                 | 502 ms                                                          | 147 ms: 3.43x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 330 ms: 2.79x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 29.3 ms: 2.78x faster                                                            |
| async_tree_io            | 940 ms                                                          | 383 ms: 2.45x faster                                                             |
| mdp                      | 1.83 sec                                                        | 787 ms: 2.32x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 201 ms: 2.32x faster                                                             |
| async_tree_none          | 394 ms                                                          | 170 ms: 2.31x faster                                                             |
| pylint                   | 384 ms                                                          | 193 ms: 1.99x faster                                                             |
| go                       | 146 ms                                                          | 75.5 ms: 1.93x faster                                                            |
| deepcopy                 | 310 us                                                          | 163 us: 1.91x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.14 ms: 1.88x faster                                                            |
| chaos                    | 74.4 ms                                                         | 40.0 ms: 1.86x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 104 us: 1.82x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 5.41 ms: 1.82x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 44.8 ms: 1.81x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 54.3 ns: 1.80x faster                                                            |
| thrift                   | 902 us                                                          | 501 us: 1.80x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 16.7 us: 1.77x faster                                                            |
| float                    | 69.6 ms                                                         | 39.7 ms: 1.75x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.09 sec: 1.75x faster                                                           |
| raytrace                 | 303 ms                                                          | 173 ms: 1.75x faster                                                             |
| mako                     | 9.10 ms                                                         | 5.31 ms: 1.72x faster                                                            |
| pyflate                  | 422 ms                                                          | 247 ms: 1.71x faster                                                             |
| comprehensions           | 17.7 us                                                         | 10.7 us: 1.65x faster                                                            |
| json                     | 4.76 ms                                                         | 2.89 ms: 1.65x faster                                                            |
| richards_super           | 49.9 ms                                                         | 30.3 ms: 1.64x faster                                                            |
| generators               | 31.6 ms                                                         | 19.2 ms: 1.64x faster                                                            |
| scimark_fft              | 216 ms                                                          | 135 ms: 1.61x faster                                                             |
| pprint_pformat           | 1.37 sec                                                        | 856 ms: 1.60x faster                                                             |
| json_loads               | 22.4 us                                                         | 14.0 us: 1.59x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 416 ms: 1.58x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 3.93 ms: 1.56x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 40.0 ms: 1.55x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 58.6 ms: 1.53x faster                                                            |
| pycparser                | 1.04 sec                                                        | 683 ms: 1.53x faster                                                             |
| fannkuch                 | 317 ms                                                          | 209 ms: 1.52x faster                                                             |
| regex_compile            | 117 ms                                                          | 76.8 ms: 1.52x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 491 ms: 1.52x faster                                                             |
| deepcopy_reduce          | 2.68 us                                                         | 1.78 us: 1.51x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 38.9 ms: 1.51x faster                                                            |
| richards                 | 40.3 ms                                                         | 26.8 ms: 1.50x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.52 us: 1.50x faster                                                            |
| django_template          | 36.0 ms                                                         | 24.0 ms: 1.50x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.16 ms: 1.50x faster                                                            |
| nbody                    | 79.1 ms                                                         | 53.8 ms: 1.47x faster                                                            |
| scimark_sor              | 115 ms                                                          | 78.6 ms: 1.46x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 59.5 ms: 1.46x faster                                                            |
| sympy_sum                | 122 ms                                                          | 84.7 ms: 1.45x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 196 us: 1.43x faster                                                             |
| html5lib                 | 52.1 ms                                                         | 37.3 ms: 1.40x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 86.0 ms: 1.39x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 34.7 ms: 1.39x faster                                                            |
| sympy_str                | 229 ms                                                          | 166 ms: 1.38x faster                                                             |
| genshi_xml               | 46.6 ms                                                         | 34.2 ms: 1.36x faster                                                            |
| sympy_expand             | 391 ms                                                          | 288 ms: 1.36x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.3 ms: 1.35x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.7 ms: 1.34x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 840 us: 1.33x faster                                                             |
| 2to3                     | 265 ms                                                          | 214 ms: 1.24x faster                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 49.7 ms: 1.24x faster                                                            |
| telco                    | 4.83 ms                                                         | 3.91 ms: 1.23x faster                                                            |
| logging_format           | 7.91 us                                                         | 6.43 us: 1.23x faster                                                            |
| logging_simple           | 7.29 us                                                         | 5.94 us: 1.23x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 65.8 ms: 1.22x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.62 sec: 1.20x faster                                                           |
| unpack_sequence          | 40.0 ns                                                         | 33.3 ns: 1.20x faster                                                            |
| coroutines               | 17.9 ms                                                         | 15.0 ms: 1.20x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 60.9 ms: 1.16x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.71 us: 1.13x faster                                                            |
| regex_dna                | 131 ms                                                          | 118 ms: 1.11x faster                                                             |
| meteor_contest           | 80.0 ms                                                         | 72.5 ms: 1.10x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 14.4 ms: 1.09x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.78 us: 1.07x faster                                                            |
| async_generators         | 241 ms                                                          | 238 ms: 1.01x faster                                                             |
| pickle                   | 7.83 us                                                         | 8.01 us: 1.02x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.32 us: 1.03x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 18.9 ms: 1.05x slower                                                            |
| coverage                 | 46.6 ms                                                         | 49.0 ms: 1.05x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.8 us: 1.09x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.2 ms: 1.10x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 89.3 ms: 1.35x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.10 ms: 1.64x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.27 ms: 1.84x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.50x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.516x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.47x
- 95% likely to have a speedup of 1.45x
- 99% likely to have a speedup of 1.42x

# Memory
- memory change: unknown
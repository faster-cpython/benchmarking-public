# Results vs. 3.10.4

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.435x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 214 ms: 1.24x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.62 sec: 1.20x faster                                                           |
| html5lib       | 52.1 ms                                                         | 38.7 ms: 1.35x faster                                                            |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 326 ms: 2.82x faster                                                             |
| async_tree_io           | 940 ms                                                          | 381 ms: 2.47x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| async_tree_none         | 394 ms                                                          | 173 ms: 2.27x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.45x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 151 ms: 3.33x faster                                                             |
| float          | 69.6 ms                                                         | 44.7 ms: 1.56x faster                                                            |
| nbody          | 79.1 ms                                                         | 68.5 ms: 1.15x faster                                                            |
| Geometric mean | (ref)                                                           | 1.82x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 81.4 ms: 1.43x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 14.3 ms: 1.10x faster                                                            |
| regex_dna      | 131 ms                                                          | 121 ms: 1.08x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.41 ms: 1.81x faster                                                            |
| json_loads           | 22.4 us                                                         | 14.4 us: 1.55x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 138 us: 1.37x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.41 sec: 1.36x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 90.2 ms: 1.33x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 218 us: 1.29x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 39.5 ms: 1.22x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.68 us: 1.13x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.9 ms: 1.09x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 56.8 ms: 1.09x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.81 us: 1.06x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.31 us: 1.03x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.4 us: 1.07x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.21x faster                                                                     |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.0 ms: 1.05x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.4 ms: 1.11x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 24.7 ms: 1.46x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.5 ms: 1.35x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.7 ms: 1.34x faster                                                            |
| mako            | 9.10 ms                                                         | 6.89 ms: 1.32x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.37x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.31 sec: 12.98x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 106 us: 3.73x faster                                                             |
| pidigits                 | 502 ms                                                          | 151 ms: 3.33x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 326 ms: 2.82x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 29.7 ms: 2.73x faster                                                            |
| async_tree_io            | 940 ms                                                          | 381 ms: 2.47x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| async_tree_none          | 394 ms                                                          | 173 ms: 2.27x faster                                                             |
| mdp                      | 1.83 sec                                                        | 814 ms: 2.24x faster                                                             |
| pylint                   | 384 ms                                                          | 197 ms: 1.94x faster                                                             |
| deepcopy                 | 310 us                                                          | 167 us: 1.85x faster                                                             |
| go                       | 146 ms                                                          | 78.8 ms: 1.85x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 5.41 ms: 1.81x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.23 ms: 1.81x faster                                                            |
| thrift                   | 902 us                                                          | 501 us: 1.80x faster                                                             |
| chaos                    | 74.4 ms                                                         | 41.8 ms: 1.78x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 435 ms: 1.71x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 47.8 ms: 1.70x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 17.5 us: 1.69x faster                                                            |
| raytrace                 | 303 ms                                                          | 180 ms: 1.68x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 58.4 ns: 1.68x faster                                                            |
| json                     | 4.76 ms                                                         | 2.92 ms: 1.63x faster                                                            |
| generators               | 31.6 ms                                                         | 19.7 ms: 1.60x faster                                                            |
| richards_super           | 49.9 ms                                                         | 31.3 ms: 1.59x faster                                                            |
| comprehensions           | 17.7 us                                                         | 11.3 us: 1.56x faster                                                            |
| float                    | 69.6 ms                                                         | 44.7 ms: 1.56x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.4 us: 1.55x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.2 ms: 1.50x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 60.3 ms: 1.49x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.81 us: 1.48x faster                                                            |
| pycparser                | 1.04 sec                                                        | 702 ms: 1.48x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 4.14 ms: 1.48x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 39.6 ms: 1.48x faster                                                            |
| scimark_sor              | 115 ms                                                          | 78.5 ms: 1.47x faster                                                            |
| django_template          | 36.0 ms                                                         | 24.7 ms: 1.46x faster                                                            |
| pyflate                  | 422 ms                                                          | 290 ms: 1.45x faster                                                             |
| richards                 | 40.3 ms                                                         | 27.9 ms: 1.44x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.59 us: 1.44x faster                                                            |
| regex_compile            | 117 ms                                                          | 81.4 ms: 1.43x faster                                                            |
| sympy_sum                | 122 ms                                                          | 87.4 ms: 1.40x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 63.0 ms: 1.38x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 138 us: 1.37x faster                                                             |
| sympy_expand             | 391 ms                                                          | 286 ms: 1.37x faster                                                             |
| sympy_str                | 229 ms                                                          | 168 ms: 1.36x faster                                                             |
| tomli_loads              | 1.91 sec                                                        | 1.41 sec: 1.36x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 34.5 ms: 1.35x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 38.7 ms: 1.35x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.7 ms: 1.34x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.02 sec: 1.34x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 90.2 ms: 1.33x faster                                                            |
| mako                     | 9.10 ms                                                         | 6.89 ms: 1.32x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 12.6 ms: 1.32x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 852 us: 1.31x faster                                                             |
| pprint_safe_repr         | 658 ms                                                          | 501 ms: 1.31x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 218 us: 1.29x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.53 ms: 1.28x faster                                                            |
| 2to3                     | 265 ms                                                          | 214 ms: 1.24x faster                                                             |
| coroutines               | 17.9 ms                                                         | 14.5 ms: 1.23x faster                                                            |
| logging_format           | 7.91 us                                                         | 6.45 us: 1.23x faster                                                            |
| scimark_fft              | 216 ms                                                          | 177 ms: 1.22x faster                                                             |
| xml_etree_process        | 48.1 ms                                                         | 39.5 ms: 1.22x faster                                                            |
| logging_simple           | 7.29 us                                                         | 5.99 us: 1.22x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.62 sec: 1.20x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 67.1 ms: 1.20x faster                                                            |
| fannkuch                 | 317 ms                                                          | 268 ms: 1.19x faster                                                             |
| nbody                    | 79.1 ms                                                         | 68.5 ms: 1.15x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.68 us: 1.13x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.29 ms: 1.13x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 35.8 ns: 1.12x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 14.3 ms: 1.10x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.9 ms: 1.09x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 56.8 ms: 1.09x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 73.9 ms: 1.08x faster                                                            |
| regex_dna                | 131 ms                                                          | 121 ms: 1.08x faster                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.81 us: 1.06x faster                                                            |
| async_generators         | 241 ms                                                          | 230 ms: 1.05x faster                                                             |
| pickle_list              | 3.22 us                                                         | 3.31 us: 1.03x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.0 ms: 1.05x slower                                                            |
| coverage                 | 46.6 ms                                                         | 49.3 ms: 1.06x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.4 us: 1.07x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.4 ms: 1.11x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 90.6 ms: 1.37x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.10 ms: 1.64x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.28 ms: 1.85x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.43x faster                                                                     |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.435x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: unknown
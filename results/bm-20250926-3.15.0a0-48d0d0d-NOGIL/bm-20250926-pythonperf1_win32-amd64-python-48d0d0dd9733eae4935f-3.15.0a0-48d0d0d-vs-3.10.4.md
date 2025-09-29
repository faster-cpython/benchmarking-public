# Results vs. 3.10.4

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.343x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 218 ms: 1.22x faster                                                             |
| docutils       | 1.95 sec                                                        | 2.78 sec: 1.43x slower                                                           |
| html5lib       | 52.1 ms                                                         | 40.1 ms: 1.30x faster                                                            |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 327 ms: 2.82x faster                                                             |
| async_tree_io           | 940 ms                                                          | 341 ms: 2.76x faster                                                             |
| async_tree_none         | 394 ms                                                          | 169 ms: 2.33x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.54x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 135 ms: 3.73x faster                                                             |
| float          | 69.6 ms                                                         | 45.0 ms: 1.55x faster                                                            |
| nbody          | 79.1 ms                                                         | 76.9 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                           | 1.81x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 88.2 ms: 1.32x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.0 ms: 1.21x faster                                                            |
| regex_dna      | 131 ms                                                          | 113 ms: 1.15x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.58 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.03 ms: 1.63x faster                                                            |
| json_loads           | 22.4 us                                                         | 15.8 us: 1.41x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 89.3 ms: 1.34x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 149 us: 1.27x faster                                                             |
| pickle_pure_python   | 280 us                                                          | 223 us: 1.26x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 59.1 ms: 1.20x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 43.5 ms: 1.11x faster                                                            |
| pickle_list          | 3.22 us                                                         | 2.93 us: 1.10x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 3.01 us: 1.01x slower                                                            |
| unpickle             | 9.82 us                                                         | 10.5 us: 1.07x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.6 us: 1.08x slower                                                            |
| tomli_loads          | 1.91 sec                                                        | 2.19 sec: 1.15x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                     |

Benchmark hidden because not significant (2): xml_etree_generate, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.2 ms: 1.10x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 25.8 ms: 1.40x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 38.5 ms: 1.21x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 18.9 ms: 1.11x faster                                                            |
| mako            | 9.10 ms                                                         | 9.65 ms: 1.06x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 2.16 sec: 7.84x faster                                                           |
| pidigits                 | 502 ms                                                          | 135 ms: 3.73x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 123 us: 3.22x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 28.7 ms: 2.83x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 327 ms: 2.82x faster                                                             |
| async_tree_io            | 940 ms                                                          | 341 ms: 2.76x faster                                                             |
| async_tree_none          | 394 ms                                                          | 169 ms: 2.33x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| pylint                   | 384 ms                                                          | 199 ms: 1.93x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 432 ms: 1.72x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.34 us: 1.72x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.07 sec: 1.71x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.37 ms: 1.71x faster                                                            |
| deepcopy                 | 310 us                                                          | 184 us: 1.69x faster                                                             |
| thrift                   | 902 us                                                          | 550 us: 1.64x faster                                                             |
| chaos                    | 74.4 ms                                                         | 45.5 ms: 1.64x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.03 ms: 1.63x faster                                                            |
| go                       | 146 ms                                                          | 90.7 ms: 1.61x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 61.0 ns: 1.60x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 18.7 us: 1.58x faster                                                            |
| json                     | 4.76 ms                                                         | 3.04 ms: 1.57x faster                                                            |
| comprehensions           | 17.7 us                                                         | 11.4 us: 1.55x faster                                                            |
| float                    | 69.6 ms                                                         | 45.0 ms: 1.55x faster                                                            |
| pycparser                | 1.04 sec                                                        | 680 ms: 1.53x faster                                                             |
| raytrace                 | 303 ms                                                          | 203 ms: 1.49x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 56.3 ms: 1.44x faster                                                            |
| generators               | 31.6 ms                                                         | 22.0 ms: 1.44x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 63.2 ms: 1.42x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 41.3 ms: 1.42x faster                                                            |
| json_loads               | 22.4 us                                                         | 15.8 us: 1.41x faster                                                            |
| pyflate                  | 422 ms                                                          | 300 ms: 1.40x faster                                                             |
| django_template          | 36.0 ms                                                         | 25.8 ms: 1.40x faster                                                            |
| scimark_sor              | 115 ms                                                          | 84.1 ms: 1.37x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.49 ms: 1.37x faster                                                            |
| richards_super           | 49.9 ms                                                         | 36.6 ms: 1.36x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 89.3 ms: 1.34x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.01 us: 1.34x faster                                                            |
| sympy_sum                | 122 ms                                                          | 92.5 ms: 1.32x faster                                                            |
| regex_compile            | 117 ms                                                          | 88.2 ms: 1.32x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 40.1 ms: 1.30x faster                                                            |
| richards                 | 40.3 ms                                                         | 31.3 ms: 1.28x faster                                                            |
| sympy_expand             | 391 ms                                                          | 305 ms: 1.28x faster                                                             |
| scimark_monte_carlo      | 61.9 ms                                                         | 48.6 ms: 1.27x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 149 us: 1.27x faster                                                             |
| sympy_str                | 229 ms                                                          | 180 ms: 1.27x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 223 us: 1.26x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 69.7 ms: 1.25x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 527 ms: 1.25x faster                                                             |
| coroutines               | 17.9 ms                                                         | 14.4 ms: 1.24x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 13.5 ms: 1.23x faster                                                            |
| 2to3                     | 265 ms                                                          | 218 ms: 1.22x faster                                                             |
| genshi_xml               | 46.6 ms                                                         | 38.5 ms: 1.21x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 13.0 ms: 1.21x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 59.1 ms: 1.20x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 68.8 ms: 1.17x faster                                                            |
| regex_dna                | 131 ms                                                          | 113 ms: 1.15x faster                                                             |
| unpack_sequence          | 40.0 ns                                                         | 34.8 ns: 1.15x faster                                                            |
| scimark_fft              | 216 ms                                                          | 191 ms: 1.13x faster                                                             |
| logging_format           | 7.91 us                                                         | 7.08 us: 1.12x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.55 us: 1.11x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 18.9 ms: 1.11x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 43.5 ms: 1.11x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.10x faster                                                            |
| pickle_list              | 3.22 us                                                         | 2.93 us: 1.10x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.00 ms: 1.08x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.58 ms: 1.06x faster                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.22 ms: 1.05x faster                                                            |
| fannkuch                 | 317 ms                                                          | 306 ms: 1.04x faster                                                             |
| nbody                    | 79.1 ms                                                         | 76.9 ms: 1.03x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.78 ms: 1.01x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 3.01 us: 1.01x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 83.4 ms: 1.04x slower                                                            |
| async_generators         | 241 ms                                                          | 254 ms: 1.05x slower                                                             |
| mako                     | 9.10 ms                                                         | 9.65 ms: 1.06x slower                                                            |
| unpickle                 | 9.82 us                                                         | 10.5 us: 1.07x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.6 us: 1.08x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.2 ms: 1.10x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.51 sec: 1.10x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 74.5 ms: 1.12x slower                                                            |
| tomli_loads              | 1.91 sec                                                        | 2.19 sec: 1.15x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.78 sec: 1.43x slower                                                           |
| coverage                 | 46.6 ms                                                         | 68.5 ms: 1.47x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.03 ms: 1.48x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.34x faster                                                                     |

Benchmark hidden because not significant (2): xml_etree_generate, pickle
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250926-3.15.0a0-48d0d0d-NOGIL/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.343x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: unknown
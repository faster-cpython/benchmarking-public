# Results vs. 3.10.4

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.450x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 219 ms: 1.21x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.60 sec: 1.22x faster                                                           |
| html5lib       | 52.1 ms                                                         | 37.6 ms: 1.38x faster                                                            |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 331 ms: 2.79x faster                                                             |
| async_tree_io           | 940 ms                                                          | 399 ms: 2.36x faster                                                             |
| async_tree_none         | 394 ms                                                          | 172 ms: 2.29x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 209 ms: 2.24x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.41x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 145 ms: 3.47x faster                                                             |
| float          | 69.6 ms                                                         | 43.1 ms: 1.62x faster                                                            |
| nbody          | 79.1 ms                                                         | 62.4 ms: 1.27x faster                                                            |
| Geometric mean | (ref)                                                           | 1.92x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 78.9 ms: 1.48x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 14.1 ms: 1.12x faster                                                            |
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.58 ms: 1.05x faster                                                            |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 22.4 us                                                         | 14.2 us: 1.58x faster                                                            |
| json_dumps           | 9.82 ms                                                         | 6.29 ms: 1.56x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 133 us: 1.42x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.36 sec: 1.40x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 89.0 ms: 1.35x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 208 us: 1.35x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 38.0 ms: 1.27x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.55 us: 1.15x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 55.3 ms: 1.11x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.8 ms: 1.09x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.85 us: 1.05x faster                                                            |
| pickle               | 7.83 us                                                         | 7.96 us: 1.02x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.38 us: 1.05x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.5 us: 1.07x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.21x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.6 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 24.4 ms: 1.48x faster                                                            |
| mako            | 9.10 ms                                                         | 6.48 ms: 1.40x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.1 ms: 1.39x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.0 ms: 1.37x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.41x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.38 sec: 12.26x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 101 us: 3.92x faster                                                             |
| pidigits                 | 502 ms                                                          | 145 ms: 3.47x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 331 ms: 2.79x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 32.1 ms: 2.53x faster                                                            |
| async_tree_io            | 940 ms                                                          | 399 ms: 2.36x faster                                                             |
| async_tree_none          | 394 ms                                                          | 172 ms: 2.29x faster                                                             |
| mdp                      | 1.83 sec                                                        | 805 ms: 2.27x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 209 ms: 2.24x faster                                                             |
| pylint                   | 384 ms                                                          | 197 ms: 1.95x faster                                                             |
| go                       | 146 ms                                                          | 75.9 ms: 1.92x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.12 ms: 1.90x faster                                                            |
| chaos                    | 74.4 ms                                                         | 39.7 ms: 1.87x faster                                                            |
| deepcopy                 | 310 us                                                          | 169 us: 1.84x faster                                                             |
| thrift                   | 902 us                                                          | 496 us: 1.82x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 55.1 ns: 1.78x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 47.1 ms: 1.73x faster                                                            |
| raytrace                 | 303 ms                                                          | 177 ms: 1.71x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 17.4 us: 1.70x faster                                                            |
| comprehensions           | 17.7 us                                                         | 10.6 us: 1.67x faster                                                            |
| richards_super           | 49.9 ms                                                         | 30.5 ms: 1.63x faster                                                            |
| generators               | 31.6 ms                                                         | 19.5 ms: 1.62x faster                                                            |
| float                    | 69.6 ms                                                         | 43.1 ms: 1.62x faster                                                            |
| json                     | 4.76 ms                                                         | 2.96 ms: 1.61x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.2 us: 1.58x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 39.3 ms: 1.58x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 57.2 ms: 1.57x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 475 ms: 1.57x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 6.29 ms: 1.56x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.01 ms: 1.53x faster                                                            |
| scimark_sor              | 115 ms                                                          | 75.7 ms: 1.52x faster                                                            |
| richards                 | 40.3 ms                                                         | 26.9 ms: 1.50x faster                                                            |
| pycparser                | 1.04 sec                                                        | 700 ms: 1.49x faster                                                             |
| django_template          | 36.0 ms                                                         | 24.4 ms: 1.48x faster                                                            |
| regex_compile            | 117 ms                                                          | 78.9 ms: 1.48x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.83 us: 1.47x faster                                                            |
| pyflate                  | 422 ms                                                          | 292 ms: 1.45x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.59 us: 1.44x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 40.8 ms: 1.43x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 61.0 ms: 1.43x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 133 us: 1.42x faster                                                             |
| sympy_sum                | 122 ms                                                          | 86.6 ms: 1.41x faster                                                            |
| mako                     | 9.10 ms                                                         | 6.48 ms: 1.40x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.36 sec: 1.40x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 980 ms: 1.40x faster                                                             |
| genshi_text              | 21.0 ms                                                         | 15.1 ms: 1.39x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 37.6 ms: 1.38x faster                                                            |
| sympy_str                | 229 ms                                                          | 167 ms: 1.38x faster                                                             |
| genshi_xml               | 46.6 ms                                                         | 34.0 ms: 1.37x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 481 ms: 1.37x faster                                                             |
| sympy_expand             | 391 ms                                                          | 286 ms: 1.37x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.3 ms: 1.35x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 89.0 ms: 1.35x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 208 us: 1.35x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 837 us: 1.34x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.54 ms: 1.28x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 62.9 ms: 1.28x faster                                                            |
| nbody                    | 79.1 ms                                                         | 62.4 ms: 1.27x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 38.0 ms: 1.27x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.6 ms: 1.23x faster                                                            |
| fannkuch                 | 317 ms                                                          | 260 ms: 1.22x faster                                                             |
| docutils                 | 1.95 sec                                                        | 1.60 sec: 1.22x faster                                                           |
| 2to3                     | 265 ms                                                          | 219 ms: 1.21x faster                                                             |
| scimark_fft              | 216 ms                                                          | 180 ms: 1.20x faster                                                             |
| logging_format           | 7.91 us                                                         | 6.62 us: 1.19x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.15 us: 1.19x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.55 us: 1.15x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 14.1 ms: 1.12x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 71.5 ms: 1.12x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 55.3 ms: 1.11x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.8 ms: 1.09x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 36.8 ns: 1.09x faster                                                            |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                             |
| telco                    | 4.83 ms                                                         | 4.54 ms: 1.06x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.58 ms: 1.05x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.85 us: 1.05x faster                                                            |
| async_generators         | 241 ms                                                          | 231 ms: 1.04x faster                                                             |
| pickle                   | 7.83 us                                                         | 7.96 us: 1.02x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.38 us: 1.05x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.5 us: 1.07x slower                                                            |
| coverage                 | 46.6 ms                                                         | 49.9 ms: 1.07x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.6 ms: 1.12x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 95.1 ms: 1.43x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.14 ms: 1.67x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.32 ms: 1.90x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.44x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.450x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: unknown
# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: windows-x86
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 260 ms: 1.02x faster                                                             |
| docutils       | 1.95 sec                                                        | 2.00 sec: 1.03x slower                                                           |
| html5lib       | 52.1 ms                                                         | 47.0 ms: 1.11x faster                                                            |
| tornado_http   | 118 ms                                                          | 110 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 474 ms: 1.95x faster                                                             |
| async_tree_none         | 394 ms                                                          | 221 ms: 1.78x faster                                                             |
| async_tree_io           | 940 ms                                                          | 548 ms: 1.71x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 280 ms: 1.67x faster                                                             |
| Geometric mean          | (ref)                                                           | 1.77x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 195 ms: 2.57x faster                                                             |
| nbody          | 79.1 ms                                                         | 48.6 ms: 1.63x faster                                                            |
| float          | 69.6 ms                                                         | 43.3 ms: 1.61x faster                                                            |
| Geometric mean | (ref)                                                           | 1.89x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 103 ms: 1.13x faster                                                             |
| regex_dna      | 131 ms                                                          | 119 ms: 1.09x faster                                                             |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.96 ms: 1.18x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.85 ms: 1.43x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.56 sec: 1.23x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 40.6 ms: 1.18x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.16x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.8 ms: 1.15x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 54.0 ms: 1.14x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 168 us: 1.13x faster                                                             |
| pickle_pure_python   | 280 us                                                          | 255 us: 1.10x faster                                                             |
| unpickle_list        | 2.98 us                                                         | 2.75 us: 1.09x faster                                                            |
| json_loads           | 22.4 us                                                         | 21.2 us: 1.05x faster                                                            |
| pickle               | 7.83 us                                                         | 8.02 us: 1.02x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.38 us: 1.05x slower                                                            |
| unpickle             | 9.82 us                                                         | 10.5 us: 1.07x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 20.0 us: 1.10x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.5 ms: 1.07x slower                                                            |
| python_startup_no_site | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.48 ms: 1.66x faster                                                            |
| django_template | 36.0 ms                                                         | 34.7 ms: 1.04x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 24.5 ms: 1.17x slower                                                            |
| genshi_xml      | 46.6 ms                                                         | 56.6 ms: 1.21x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.05x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 148 us: 2.68x faster                                                             |
| pidigits                 | 502 ms                                                          | 195 ms: 2.57x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 474 ms: 1.95x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 15.5 us: 1.90x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.12 ms: 1.90x faster                                                            |
| async_tree_none          | 394 ms                                                          | 221 ms: 1.78x faster                                                             |
| async_tree_io            | 940 ms                                                          | 548 ms: 1.71x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 47.6 ms: 1.71x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 47.0 ms: 1.71x faster                                                            |
| scimark_sor              | 115 ms                                                          | 68.2 ms: 1.69x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 280 ms: 1.67x faster                                                             |
| mako                     | 9.10 ms                                                         | 5.48 ms: 1.66x faster                                                            |
| nbody                    | 79.1 ms                                                         | 48.6 ms: 1.63x faster                                                            |
| float                    | 69.6 ms                                                         | 43.3 ms: 1.61x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 62.2 ns: 1.57x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 59.8 ms: 1.50x faster                                                            |
| comprehensions           | 17.7 us                                                         | 11.9 us: 1.50x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.85 ms: 1.43x faster                                                            |
| pyflate                  | 422 ms                                                          | 297 ms: 1.42x faster                                                             |
| pylint                   | 384 ms                                                          | 271 ms: 1.42x faster                                                             |
| go                       | 146 ms                                                          | 104 ms: 1.39x faster                                                             |
| generators               | 31.6 ms                                                         | 22.7 ms: 1.39x faster                                                            |
| richards_super           | 49.9 ms                                                         | 35.9 ms: 1.39x faster                                                            |
| chaos                    | 74.4 ms                                                         | 53.9 ms: 1.38x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.36 ms: 1.37x faster                                                            |
| fannkuch                 | 317 ms                                                          | 235 ms: 1.35x faster                                                             |
| deepcopy                 | 310 us                                                          | 239 us: 1.30x faster                                                             |
| scimark_monte_carlo      | 61.9 ms                                                         | 48.2 ms: 1.28x faster                                                            |
| pycparser                | 1.04 sec                                                        | 818 ms: 1.27x faster                                                             |
| sqlglot_parse            | 1.33 ms                                                         | 1.06 ms: 1.26x faster                                                            |
| scimark_fft              | 216 ms                                                          | 173 ms: 1.25x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 4.96 ms: 1.24x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.56 sec: 1.23x faster                                                           |
| richards                 | 40.3 ms                                                         | 33.0 ms: 1.22x faster                                                            |
| raytrace                 | 303 ms                                                          | 249 ms: 1.22x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.91 us: 1.20x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 40.6 ms: 1.18x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 49.7 ms: 1.18x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 74.5 ms: 1.17x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.36 ms: 1.16x faster                                                            |
| json                     | 4.76 ms                                                         | 4.11 ms: 1.16x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.16x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.8 ms: 1.15x faster                                                            |
| thrift                   | 902 us                                                          | 788 us: 1.14x faster                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 54.0 ms: 1.14x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 168 us: 1.13x faster                                                             |
| regex_compile            | 117 ms                                                          | 103 ms: 1.13x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 995 us: 1.13x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 668 ms: 1.11x faster                                                             |
| meteor_contest           | 80.0 ms                                                         | 72.2 ms: 1.11x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 47.0 ms: 1.11x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 599 ms: 1.10x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 255 us: 1.10x faster                                                             |
| regex_dna                | 131 ms                                                          | 119 ms: 1.09x faster                                                             |
| pprint_pformat           | 1.37 sec                                                        | 1.26 sec: 1.09x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.75 us: 1.09x faster                                                            |
| sympy_sum                | 122 ms                                                          | 114 ms: 1.08x faster                                                             |
| tornado_http             | 118 ms                                                          | 110 ms: 1.06x faster                                                             |
| mdp                      | 1.83 sec                                                        | 1.72 sec: 1.06x faster                                                           |
| json_loads               | 22.4 us                                                         | 21.2 us: 1.05x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.56 us: 1.05x faster                                                            |
| django_template          | 36.0 ms                                                         | 34.7 ms: 1.04x faster                                                            |
| sympy_str                | 229 ms                                                          | 222 ms: 1.03x faster                                                             |
| 2to3                     | 265 ms                                                          | 260 ms: 1.02x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 16.8 ms: 1.01x slower                                                            |
| coroutines               | 17.9 ms                                                         | 18.2 ms: 1.02x slower                                                            |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                            |
| pickle                   | 7.83 us                                                         | 8.02 us: 1.02x slower                                                            |
| sympy_expand             | 391 ms                                                          | 400 ms: 1.03x slower                                                             |
| docutils                 | 1.95 sec                                                        | 2.00 sec: 1.03x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 46.9 ms: 1.05x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.38 us: 1.05x slower                                                            |
| python_startup           | 22.9 ms                                                         | 24.5 ms: 1.07x slower                                                            |
| unpickle                 | 9.82 us                                                         | 10.5 us: 1.07x slower                                                            |
| pathlib                  | 81.2 ms                                                         | 87.5 ms: 1.08x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 754 us: 1.09x slower                                                             |
| logging_format           | 7.91 us                                                         | 8.65 us: 1.09x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 20.0 us: 1.10x slower                                                            |
| logging_simple           | 7.29 us                                                         | 8.05 us: 1.10x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.13x slower                                                            |
| unpack_sequence          | 40.0 ns                                                         | 45.6 ns: 1.14x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 77.5 ms: 1.17x slower                                                            |
| genshi_text              | 21.0 ms                                                         | 24.5 ms: 1.17x slower                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.96 ms: 1.18x slower                                                            |
| coverage                 | 46.6 ms                                                         | 54.9 ms: 1.18x slower                                                            |
| genshi_xml               | 46.6 ms                                                         | 56.6 ms: 1.21x slower                                                            |
| telco                    | 4.83 ms                                                         | 6.08 ms: 1.26x slower                                                            |
| async_generators         | 241 ms                                                          | 322 ms: 1.34x slower                                                             |
| Geometric mean           | (ref)                                                           | 1.18x faster                                                                     |

Benchmark hidden because not significant (2): sqlglot_normalize, asyncio_tcp_ssl
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown
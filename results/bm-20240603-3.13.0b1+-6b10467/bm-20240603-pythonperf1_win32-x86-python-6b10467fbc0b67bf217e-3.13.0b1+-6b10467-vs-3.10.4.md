# Results vs. 3.10.4

- fork: python
- ref: 6b10467fbc0b67bf217e
- machine: windows-x86
- commit hash: 6b10467
- commit date: 2024-06-03
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 230 ms: 1.16x faster                                                            |
| chameleon      | 6.42 ms                                                         | 5.70 ms: 1.13x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.81 sec: 1.08x faster                                                          |
| html5lib       | 52.1 ms                                                         | 43.9 ms: 1.19x faster                                                           |
| tornado_http   | 118 ms                                                          | 94.1 ms: 1.25x faster                                                           |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 486 ms: 1.90x faster                                                            |
| async_tree_io           | 940 ms                                                          | 529 ms: 1.78x faster                                                            |
| async_tree_none         | 394 ms                                                          | 224 ms: 1.76x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 273 ms: 1.71x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.78x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.57x faster                                                            |
| float          | 69.6 ms                                                         | 52.8 ms: 1.32x faster                                                           |
| nbody          | 79.1 ms                                                         | 75.9 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                           | 1.52x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 97.2 ms: 1.20x faster                                                           |
| regex_dna      | 131 ms                                                          | 119 ms: 1.09x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.88 ms: 1.13x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.84 ms: 1.44x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 147 us: 1.29x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 221 us: 1.27x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.58 sec: 1.21x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 103 ms: 1.17x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 41.6 ms: 1.16x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.4 ms: 1.12x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.8 us: 1.08x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 59.1 ms: 1.04x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.88 us: 1.04x faster                                                           |
| pickle               | 7.83 us                                                         | 7.95 us: 1.02x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.1 us: 1.02x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.54 us: 1.10x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 20.6 us: 1.13x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.4 ms: 1.02x faster                                                           |
| python_startup_no_site | 18.1 ms                                                         | 18.3 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.95 ms: 1.31x faster                                                           |
| django_template | 36.0 ms                                                         | 29.1 ms: 1.24x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 18.9 ms: 1.11x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 42.8 ms: 1.09x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.18x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 135 us: 2.93x faster                                                            |
| pidigits                 | 502 ms                                                          | 196 ms: 2.57x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 486 ms: 1.90x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.22 ms: 1.82x faster                                                           |
| async_tree_io            | 940 ms                                                          | 529 ms: 1.78x faster                                                            |
| pylint                   | 384 ms                                                          | 217 ms: 1.76x faster                                                            |
| async_tree_none          | 394 ms                                                          | 224 ms: 1.76x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 273 ms: 1.71x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 58.1 ns: 1.68x faster                                                           |
| raytrace                 | 303 ms                                                          | 186 ms: 1.63x faster                                                            |
| chaos                    | 74.4 ms                                                         | 47.1 ms: 1.58x faster                                                           |
| generators               | 31.6 ms                                                         | 21.4 ms: 1.48x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 55.6 ms: 1.46x faster                                                           |
| comprehensions           | 17.7 us                                                         | 12.1 us: 1.46x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 61.7 ms: 1.45x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 6.84 ms: 1.44x faster                                                           |
| go                       | 146 ms                                                          | 102 ms: 1.43x faster                                                            |
| richards_super           | 49.9 ms                                                         | 35.0 ms: 1.42x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 940 us: 1.42x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.38 ms: 1.40x faster                                                           |
| scimark_sor              | 115 ms                                                          | 84.1 ms: 1.37x faster                                                           |
| pyflate                  | 422 ms                                                          | 308 ms: 1.37x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.17 ms: 1.35x faster                                                           |
| pycparser                | 1.04 sec                                                        | 776 ms: 1.34x faster                                                            |
| float                    | 69.6 ms                                                         | 52.8 ms: 1.32x faster                                                           |
| mako                     | 9.10 ms                                                         | 6.95 ms: 1.31x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 47.5 ms: 1.30x faster                                                           |
| richards                 | 40.3 ms                                                         | 31.0 ms: 1.30x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 147 us: 1.29x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 68.1 ms: 1.28x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 221 us: 1.27x faster                                                            |
| tornado_http             | 118 ms                                                          | 94.1 ms: 1.25x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 23.8 us: 1.24x faster                                                           |
| django_template          | 36.0 ms                                                         | 29.1 ms: 1.24x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.58 sec: 1.21x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 66.6 ms: 1.20x faster                                                           |
| regex_compile            | 117 ms                                                          | 97.2 ms: 1.20x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.93 us: 1.19x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 43.9 ms: 1.19x faster                                                           |
| sympy_sum                | 122 ms                                                          | 104 ms: 1.18x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 103 ms: 1.17x faster                                                            |
| json                     | 4.76 ms                                                         | 4.11 ms: 1.16x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 41.6 ms: 1.16x faster                                                           |
| fannkuch                 | 317 ms                                                          | 274 ms: 1.16x faster                                                            |
| 2to3                     | 265 ms                                                          | 230 ms: 1.16x faster                                                            |
| coroutines               | 17.9 ms                                                         | 15.5 ms: 1.16x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 14.5 ms: 1.15x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.19 sec: 1.15x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 982 us: 1.14x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 583 ms: 1.13x faster                                                            |
| chameleon                | 6.42 ms                                                         | 5.70 ms: 1.13x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 39.7 ms: 1.13x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.63 sec: 1.12x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.4 ms: 1.12x faster                                                           |
| deepcopy                 | 310 us                                                          | 278 us: 1.11x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 18.9 ms: 1.11x faster                                                           |
| sympy_str                | 229 ms                                                          | 207 ms: 1.11x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 209 ms: 1.10x faster                                                            |
| regex_dna                | 131 ms                                                          | 119 ms: 1.09x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 681 ms: 1.09x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 42.8 ms: 1.09x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.98 ms: 1.09x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.81 sec: 1.08x faster                                                          |
| sympy_expand             | 391 ms                                                          | 363 ms: 1.08x faster                                                            |
| json_loads               | 22.4 us                                                         | 20.8 us: 1.08x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 74.4 ms: 1.08x faster                                                           |
| scimark_fft              | 216 ms                                                          | 207 ms: 1.04x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 59.1 ms: 1.04x faster                                                           |
| nbody                    | 79.1 ms                                                         | 75.9 ms: 1.04x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.88 us: 1.04x faster                                                           |
| python_startup           | 22.9 ms                                                         | 22.4 ms: 1.02x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.66 us: 1.01x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.9 sec: 1.01x faster                                                          |
| flaskblogging            | 2.03 sec                                                        | 2.03 sec: 1.00x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 18.3 ms: 1.01x slower                                                           |
| pickle                   | 7.83 us                                                         | 7.95 us: 1.02x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 83.1 ms: 1.02x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.1 us: 1.02x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 69.1 ms: 1.04x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 756 us: 1.09x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.54 us: 1.10x slower                                                           |
| async_generators         | 241 ms                                                          | 269 ms: 1.12x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.12x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.88 ms: 1.13x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 20.6 us: 1.13x slower                                                           |
| telco                    | 4.83 ms                                                         | 5.75 ms: 1.19x slower                                                           |
| coverage                 | 46.6 ms                                                         | 308 ms: 6.61x slower                                                            |
| thrift                   | 902 us                                                          | 9.80 ms: 10.86x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.15x faster                                                                    |

Benchmark hidden because not significant (3): regex_v8, logging_format, logging_simple
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240603-3.13.0b1+-6b10467/bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown
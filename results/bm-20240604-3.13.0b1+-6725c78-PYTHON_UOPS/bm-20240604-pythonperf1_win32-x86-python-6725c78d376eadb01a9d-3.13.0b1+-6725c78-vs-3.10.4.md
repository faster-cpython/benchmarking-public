# Results vs. 3.10.4

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: windows-x86
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 254 ms: 1.05x faster                                                            |
| chameleon      | 6.42 ms                                                         | 6.33 ms: 1.01x faster                                                           |
| docutils       | 1.95 sec                                                        | 2.00 sec: 1.03x slower                                                          |
| html5lib       | 52.1 ms                                                         | 50.7 ms: 1.03x faster                                                           |
| tornado_http   | 118 ms                                                          | 99.7 ms: 1.18x faster                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 486 ms: 1.90x faster                                                            |
| async_tree_io           | 940 ms                                                          | 545 ms: 1.73x faster                                                            |
| async_tree_none         | 394 ms                                                          | 236 ms: 1.67x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 295 ms: 1.58x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.72x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.54x faster                                                            |
| float          | 69.6 ms                                                         | 52.9 ms: 1.32x faster                                                           |
| nbody          | 79.1 ms                                                         | 75.2 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                           | 1.52x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 119 ms: 1.09x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                           |
| regex_compile  | 117 ms                                                          | 124 ms: 1.06x slower                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.74 ms: 1.46x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.62 sec: 1.18x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.16x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 247 us: 1.14x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 43.1 ms: 1.12x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 172 us: 1.10x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.2 ms: 1.10x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.9 us: 1.07x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 60.0 ms: 1.03x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.95 us: 1.01x faster                                                           |
| pickle               | 7.83 us                                                         | 8.25 us: 1.05x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.4 us: 1.06x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 20.6 us: 1.13x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.65 us: 1.14x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.6 ms: 1.02x faster                                                           |
| python_startup_no_site | 18.1 ms                                                         | 18.3 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.24 ms: 1.26x faster                                                           |
| django_template | 36.0 ms                                                         | 32.4 ms: 1.11x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 21.2 ms: 1.01x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 50.1 ms: 1.08x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.07x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 147 us: 2.69x faster                                                            |
| pidigits                 | 502 ms                                                          | 198 ms: 2.54x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 486 ms: 1.90x faster                                                            |
| async_tree_io            | 940 ms                                                          | 545 ms: 1.73x faster                                                            |
| async_tree_none          | 394 ms                                                          | 236 ms: 1.67x faster                                                            |
| pylint                   | 384 ms                                                          | 242 ms: 1.59x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 295 ms: 1.58x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.74 ms: 1.46x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 56.6 ms: 1.44x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.83 ms: 1.43x faster                                                           |
| raytrace                 | 303 ms                                                          | 212 ms: 1.42x faster                                                            |
| richards_super           | 49.9 ms                                                         | 35.4 ms: 1.41x faster                                                           |
| chaos                    | 74.4 ms                                                         | 53.0 ms: 1.40x faster                                                           |
| generators               | 31.6 ms                                                         | 23.6 ms: 1.34x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 74.2 ns: 1.32x faster                                                           |
| float                    | 69.6 ms                                                         | 52.9 ms: 1.32x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.02 ms: 1.30x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.7 us: 1.30x faster                                                           |
| richards                 | 40.3 ms                                                         | 31.3 ms: 1.29x faster                                                           |
| go                       | 146 ms                                                          | 113 ms: 1.29x faster                                                            |
| mako                     | 9.10 ms                                                         | 7.24 ms: 1.26x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 49.5 ms: 1.25x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.28 ms: 1.24x faster                                                           |
| scimark_sor              | 115 ms                                                          | 93.0 ms: 1.24x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 615 ms: 1.21x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.93 us: 1.19x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 73.6 ms: 1.18x faster                                                           |
| pycparser                | 1.04 sec                                                        | 882 ms: 1.18x faster                                                            |
| tornado_http             | 118 ms                                                          | 99.7 ms: 1.18x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.62 sec: 1.18x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.16x faster                                                            |
| coroutines               | 17.9 ms                                                         | 15.6 ms: 1.15x faster                                                           |
| fannkuch                 | 317 ms                                                          | 277 ms: 1.14x faster                                                            |
| json                     | 4.76 ms                                                         | 4.18 ms: 1.14x faster                                                           |
| pyflate                  | 422 ms                                                          | 371 ms: 1.14x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 247 us: 1.14x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 80.0 ms: 1.12x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 71.5 ms: 1.12x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 43.1 ms: 1.12x faster                                                           |
| django_template          | 36.0 ms                                                         | 32.4 ms: 1.11x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 172 us: 1.10x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.2 ms: 1.10x faster                                                           |
| regex_dna                | 131 ms                                                          | 119 ms: 1.09x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 5.66 ms: 1.08x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.27 sec: 1.08x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.01 ms: 1.08x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.70 sec: 1.08x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 27.6 us: 1.07x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 615 ms: 1.07x faster                                                            |
| json_loads               | 22.4 us                                                         | 20.9 us: 1.07x faster                                                           |
| nbody                    | 79.1 ms                                                         | 75.2 ms: 1.05x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 76.4 ms: 1.05x faster                                                           |
| 2to3                     | 265 ms                                                          | 254 ms: 1.05x faster                                                            |
| scimark_fft              | 216 ms                                                          | 207 ms: 1.04x faster                                                            |
| sympy_sum                | 122 ms                                                          | 118 ms: 1.04x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 60.0 ms: 1.03x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 50.7 ms: 1.03x faster                                                           |
| python_startup           | 22.9 ms                                                         | 22.6 ms: 1.02x faster                                                           |
| chameleon                | 6.42 ms                                                         | 6.33 ms: 1.01x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 16.4 ms: 1.01x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 44.1 ms: 1.01x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.95 us: 1.01x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.9 sec: 1.01x faster                                                          |
| deepcopy                 | 310 us                                                          | 308 us: 1.01x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 229 ms: 1.01x faster                                                            |
| flaskblogging            | 2.03 sec                                                        | 2.04 sec: 1.00x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 21.2 ms: 1.01x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 18.3 ms: 1.02x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.00 sec: 1.03x slower                                                          |
| sympy_str                | 229 ms                                                          | 237 ms: 1.03x slower                                                            |
| pathlib                  | 81.2 ms                                                         | 83.9 ms: 1.03x slower                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.79 us: 1.04x slower                                                           |
| pickle                   | 7.83 us                                                         | 8.25 us: 1.05x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.69 us: 1.06x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.4 us: 1.06x slower                                                           |
| regex_compile            | 117 ms                                                          | 124 ms: 1.06x slower                                                            |
| logging_format           | 7.91 us                                                         | 8.41 us: 1.06x slower                                                           |
| sympy_expand             | 391 ms                                                          | 419 ms: 1.07x slower                                                            |
| genshi_xml               | 46.6 ms                                                         | 50.1 ms: 1.08x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 71.4 ms: 1.08x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 766 us: 1.10x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.12x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 20.6 us: 1.13x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.65 us: 1.14x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                                           |
| async_generators         | 241 ms                                                          | 285 ms: 1.18x slower                                                            |
| telco                    | 4.83 ms                                                         | 5.80 ms: 1.20x slower                                                           |
| coverage                 | 46.6 ms                                                         | 325 ms: 6.97x slower                                                            |
| thrift                   | 902 us                                                          | 11.6 ms: 12.83x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.08x faster                                                                    |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240604-3.13.0b1+-6725c78-PYTHON_UOPS/bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown
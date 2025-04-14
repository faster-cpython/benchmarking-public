# Results vs. 3.10.4

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-x86_64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.352x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                                       |
| html5lib       | 94.6 ms                                                      | 68.4 ms: 1.38x faster                                                        |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 642 ms: 2.49x faster                                                         |
| async_tree_none         | 692 ms                                                       | 285 ms: 2.43x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 345 ms: 2.38x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 514 ms: 1.82x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.26x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 70.3 ms: 1.58x faster                                                        |
| nbody          | 134 ms                                                       | 93.0 ms: 1.44x faster                                                        |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 135 ms: 1.40x faster                                                         |
| regex_dna      | 261 ms                                                       | 239 ms: 1.09x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 210 us: 1.49x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.06 sec: 1.41x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 331 us: 1.37x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 58.5 ms: 1.30x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.3 ms: 1.28x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.17x faster                                                         |
| json_loads           | 30.3 us                                                      | 25.9 us: 1.17x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 95.8 ms: 1.15x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 82.8 ms: 1.11x faster                                                        |
| unpickle             | 13.5 us                                                      | 14.0 us: 1.04x slower                                                        |
| unpickle_list        | 4.65 us                                                      | 4.96 us: 1.07x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.99 us: 1.21x slower                                                        |
| pickle               | 9.89 us                                                      | 12.1 us: 1.22x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 36.2 us: 1.23x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 36.0 ms: 1.40x faster                                                        |
| mako            | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 24.5 ms: 1.28x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 55.0 ms: 1.15x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.30x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 172 us: 3.12x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 642 ms: 2.49x faster                                                         |
| async_tree_none          | 692 ms                                                       | 285 ms: 2.43x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 345 ms: 2.38x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.31 ms: 2.27x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 372 ms: 2.09x faster                                                         |
| generators               | 57.3 ms                                                      | 28.1 ms: 2.04x faster                                                        |
| go                       | 262 ms                                                       | 132 ms: 1.99x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 514 ms: 1.82x faster                                                         |
| chaos                    | 109 ms                                                       | 60.4 ms: 1.80x faster                                                        |
| pylint                   | 566 ms                                                       | 315 ms: 1.80x faster                                                         |
| raytrace                 | 489 ms                                                       | 275 ms: 1.78x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 61.2 ms: 1.76x faster                                                        |
| richards_super           | 90.6 ms                                                      | 51.8 ms: 1.75x faster                                                        |
| logging_silent           | 167 ns                                                       | 96.4 ns: 1.74x faster                                                        |
| pyflate                  | 733 ms                                                       | 430 ms: 1.70x faster                                                         |
| scimark_lu               | 167 ms                                                       | 98.1 ms: 1.70x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.5 us: 1.69x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.34 ms: 1.66x faster                                                        |
| spectral_norm            | 139 ms                                                       | 83.8 ms: 1.66x faster                                                        |
| richards                 | 75.1 ms                                                      | 45.9 ms: 1.63x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 73.8 ms: 1.61x faster                                                        |
| deepcopy                 | 468 us                                                       | 290 us: 1.61x faster                                                         |
| scimark_sor              | 180 ms                                                       | 113 ms: 1.60x faster                                                         |
| float                    | 111 ms                                                       | 70.3 ms: 1.58x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.1 us: 1.56x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.73 ms: 1.55x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.13 ms: 1.54x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 210 us: 1.49x faster                                                         |
| nbody                    | 134 ms                                                       | 93.0 ms: 1.44x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.06 sec: 1.41x faster                                                       |
| regex_compile            | 190 ms                                                       | 135 ms: 1.40x faster                                                         |
| django_template          | 50.2 ms                                                      | 36.0 ms: 1.40x faster                                                        |
| thrift                   | 1.18 ms                                                      | 842 us: 1.40x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 68.4 ms: 1.38x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.45 us: 1.38x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 331 us: 1.37x faster                                                         |
| mako                     | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.04 us: 1.37x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.95 us: 1.36x faster                                                        |
| fannkuch                 | 483 ms                                                       | 358 ms: 1.35x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.60 sec: 1.34x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                       |
| sqlalchemy_declarative   | 190 ms                                                       | 142 ms: 1.34x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 789 ms: 1.33x faster                                                         |
| nqueens                  | 115 ms                                                       | 87.9 ms: 1.31x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 58.5 ms: 1.30x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.6 ms: 1.29x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 24.5 ms: 1.28x faster                                                        |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.28x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.3 ms: 1.28x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.9 ms: 1.27x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 114 ms: 1.26x faster                                                         |
| sympy_str                | 360 ms                                                       | 287 ms: 1.26x faster                                                         |
| 2to3                     | 350 ms                                                       | 284 ms: 1.23x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 22.8 ms: 1.23x faster                                                        |
| sympy_expand             | 600 ms                                                       | 487 ms: 1.23x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 57.2 ms: 1.23x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.45 sec: 1.23x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 939 us: 1.22x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 67.2 ms: 1.21x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 49.7 ns: 1.21x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.17x faster                                                         |
| json_loads               | 30.3 us                                                      | 25.9 us: 1.17x faster                                                        |
| scimark_fft              | 361 ms                                                       | 312 ms: 1.16x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 95.8 ms: 1.15x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 55.0 ms: 1.15x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 82.8 ms: 1.11x faster                                                        |
| meteor_contest           | 138 ms                                                       | 125 ms: 1.11x faster                                                         |
| json                     | 5.86 ms                                                      | 5.33 ms: 1.10x faster                                                        |
| regex_dna                | 261 ms                                                       | 239 ms: 1.09x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.79 us: 1.07x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.78 ms: 1.06x faster                                                        |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                         |
| async_generators         | 421 ms                                                       | 412 ms: 1.02x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                         |
| unpickle                 | 13.5 us                                                      | 14.0 us: 1.04x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 4.96 us: 1.07x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.95 ms: 1.10x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.99 us: 1.21x slower                                                        |
| pickle                   | 9.89 us                                                      | 12.1 us: 1.22x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 36.2 us: 1.23x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                                        |
| coverage                 | 63.3 ms                                                      | 78.9 ms: 1.25x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.79 ms: 1.58x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.32 ms: 1.85x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 854 ms: 133.95x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                 |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (11) of results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.352x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.28x
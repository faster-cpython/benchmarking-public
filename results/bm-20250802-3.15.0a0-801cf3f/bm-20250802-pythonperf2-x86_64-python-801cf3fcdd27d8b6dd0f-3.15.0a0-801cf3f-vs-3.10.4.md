# Results vs. 3.10.4

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-x86_64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.325x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 280 ms: 1.25x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                                      |
| html5lib       | 94.6 ms                                                      | 65.1 ms: 1.45x faster                                                       |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 628 ms: 2.55x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 328 ms: 2.50x faster                                                        |
| async_tree_none         | 692 ms                                                       | 278 ms: 2.48x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 502 ms: 1.87x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 67.7 ms: 1.64x faster                                                       |
| nbody          | 134 ms                                                       | 92.0 ms: 1.46x faster                                                       |
| pidigits       | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.36x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 131 ms: 1.45x faster                                                        |
| regex_dna      | 261 ms                                                       | 219 ms: 1.19x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.9 ms: 1.14x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.54 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.14x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 207 us: 1.51x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.02 sec: 1.44x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 331 us: 1.37x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 58.6 ms: 1.30x faster                                                       |
| json_loads           | 30.3 us                                                      | 26.4 us: 1.15x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 96.9 ms: 1.14x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 142 ms: 1.13x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 84.6 ms: 1.09x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 5.16 us: 1.11x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.0 us: 1.12x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 33.7 us: 1.14x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.86 us: 1.18x slower                                                       |
| pickle               | 9.89 us                                                      | 12.4 us: 1.25x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.10x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.80 ms: 1.20x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.4 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.2 ms: 1.43x faster                                                       |
| mako            | 14.7 ms                                                      | 10.6 ms: 1.38x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.2 ms: 1.36x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 53.1 ms: 1.19x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.34x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 165 us: 3.25x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 628 ms: 2.55x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 328 ms: 2.50x faster                                                        |
| async_tree_none          | 692 ms                                                       | 278 ms: 2.48x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.15 ms: 2.38x faster                                                       |
| mdp                      | 3.01 sec                                                     | 1.29 sec: 2.33x faster                                                      |
| go                       | 262 ms                                                       | 118 ms: 2.22x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 368 ms: 2.12x faster                                                        |
| generators               | 57.3 ms                                                      | 28.2 ms: 2.03x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| chaos                    | 109 ms                                                       | 58.0 ms: 1.87x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 502 ms: 1.87x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 27.4 us: 1.81x faster                                                       |
| logging_silent           | 167 ns                                                       | 92.7 ns: 1.80x faster                                                       |
| scimark_lu               | 167 ms                                                       | 93.3 ms: 1.79x faster                                                       |
| richards_super           | 90.6 ms                                                      | 50.8 ms: 1.79x faster                                                       |
| raytrace                 | 489 ms                                                       | 275 ms: 1.78x faster                                                        |
| pylint                   | 566 ms                                                       | 320 ms: 1.77x faster                                                        |
| scimark_sor              | 180 ms                                                       | 102 ms: 1.76x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 61.6 ms: 1.74x faster                                                       |
| pyflate                  | 733 ms                                                       | 424 ms: 1.73x faster                                                        |
| deepcopy                 | 468 us                                                       | 271 us: 1.73x faster                                                        |
| richards                 | 75.1 ms                                                      | 44.9 ms: 1.67x faster                                                       |
| comprehensions           | 26.7 us                                                      | 16.2 us: 1.65x faster                                                       |
| float                    | 111 ms                                                       | 67.7 ms: 1.64x faster                                                       |
| spectral_norm            | 139 ms                                                       | 85.8 ms: 1.62x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.01 ms: 1.57x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 76.6 ms: 1.56x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 207 us: 1.51x faster                                                        |
| logging_simple           | 8.88 us                                                      | 5.98 us: 1.48x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.61 us: 1.46x faster                                                       |
| nbody                    | 134 ms                                                       | 92.0 ms: 1.46x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 65.1 ms: 1.45x faster                                                       |
| regex_compile            | 190 ms                                                       | 131 ms: 1.45x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.02 sec: 1.44x faster                                                      |
| unpack_sequence          | 59.9 ns                                                      | 41.7 ns: 1.44x faster                                                       |
| django_template          | 50.2 ms                                                      | 35.2 ms: 1.43x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.54 sec: 1.40x faster                                                      |
| mako                     | 14.7 ms                                                      | 10.6 ms: 1.38x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.90 us: 1.38x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 760 ms: 1.38x faster                                                        |
| coroutines               | 30.3 ms                                                      | 22.1 ms: 1.37x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 331 us: 1.37x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 59.5 ms: 1.36x faster                                                       |
| thrift                   | 1.18 ms                                                      | 867 us: 1.36x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 23.2 ms: 1.36x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 58.6 ms: 1.30x faster                                                       |
| fannkuch                 | 483 ms                                                       | 375 ms: 1.29x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.6 ms: 1.29x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 22.0 ms: 1.28x faster                                                       |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                        |
| sympy_str                | 360 ms                                                       | 284 ms: 1.27x faster                                                        |
| nqueens                  | 115 ms                                                       | 91.9 ms: 1.25x faster                                                       |
| 2to3                     | 350 ms                                                       | 280 ms: 1.25x faster                                                        |
| sympy_expand             | 600 ms                                                       | 484 ms: 1.24x faster                                                        |
| regex_dna                | 261 ms                                                       | 219 ms: 1.19x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 53.1 ms: 1.19x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                                      |
| scimark_fft              | 361 ms                                                       | 306 ms: 1.18x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 973 us: 1.17x faster                                                        |
| meteor_contest           | 138 ms                                                       | 120 ms: 1.15x faster                                                        |
| json_loads               | 30.3 us                                                      | 26.4 us: 1.15x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 96.9 ms: 1.14x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 23.9 ms: 1.14x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 142 ms: 1.13x faster                                                        |
| json                     | 5.86 ms                                                      | 5.37 ms: 1.09x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 84.6 ms: 1.09x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.70 ms: 1.08x faster                                                       |
| pidigits                 | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.85 us: 1.05x faster                                                       |
| unpickle_list            | 4.65 us                                                      | 5.16 us: 1.11x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.0 us: 1.12x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 33.7 us: 1.14x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.54 ms: 1.15x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.86 us: 1.18x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.80 ms: 1.20x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.4 us: 1.25x slower                                                       |
| coverage                 | 63.3 ms                                                      | 82.0 ms: 1.30x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.4 ms: 1.33x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.93 ms: 1.66x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.67 ms: 1.95x slower                                                       |
| telco                    | 7.23 ms                                                      | 161 ms: 22.25x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 1.37 sec: 215.30x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                |

Benchmark hidden because not significant (2): asyncio_websockets, async_generators
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.325x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.38x
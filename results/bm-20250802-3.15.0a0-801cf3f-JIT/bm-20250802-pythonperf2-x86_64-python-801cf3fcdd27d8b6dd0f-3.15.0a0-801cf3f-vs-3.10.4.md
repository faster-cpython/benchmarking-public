# Results vs. 3.10.4

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-x86_64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.332x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| html5lib       | 94.6 ms                                                      | 67.5 ms: 1.40x faster                                                       |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 627 ms: 2.55x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 330 ms: 2.49x faster                                                        |
| async_tree_none         | 692 ms                                                       | 283 ms: 2.44x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 507 ms: 1.85x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 63.9 ms: 1.74x faster                                                       |
| nbody          | 134 ms                                                       | 98.1 ms: 1.37x faster                                                       |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.36x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 132 ms: 1.44x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.1 ms: 1.17x faster                                                       |
| regex_dna      | 261 ms                                                       | 227 ms: 1.15x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.70 ms: 1.20x slower                                                       |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 195 us: 1.60x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.90 sec: 1.54x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 332 us: 1.37x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 56.6 ms: 1.34x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.22x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 81.9 ms: 1.13x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.10x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.99 us: 1.07x slower                                                       |
| unpickle             | 13.5 us                                                      | 14.7 us: 1.09x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 34.2 us: 1.16x slower                                                       |
| pickle_list          | 4.12 us                                                      | 5.00 us: 1.21x slower                                                       |
| pickle               | 9.89 us                                                      | 12.7 us: 1.29x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.81 ms: 1.20x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.79 ms: 1.50x faster                                                       |
| django_template | 50.2 ms                                                      | 34.8 ms: 1.44x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.3 ms: 1.35x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.36x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 172 us: 3.13x faster                                                        |
| deltablue                | 7.50 ms                                                      | 2.88 ms: 2.60x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 627 ms: 2.55x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 330 ms: 2.49x faster                                                        |
| async_tree_none          | 692 ms                                                       | 283 ms: 2.44x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.29 sec: 2.33x faster                                                      |
| richards_super           | 90.6 ms                                                      | 41.2 ms: 2.20x faster                                                       |
| richards                 | 75.1 ms                                                      | 35.6 ms: 2.11x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 370 ms: 2.11x faster                                                        |
| go                       | 262 ms                                                       | 128 ms: 2.05x faster                                                        |
| generators               | 57.3 ms                                                      | 29.2 ms: 1.96x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 507 ms: 1.85x faster                                                        |
| chaos                    | 109 ms                                                       | 59.0 ms: 1.84x faster                                                       |
| scimark_sor              | 180 ms                                                       | 102 ms: 1.77x faster                                                        |
| logging_silent           | 167 ns                                                       | 94.5 ns: 1.77x faster                                                       |
| scimark_lu               | 167 ms                                                       | 95.2 ms: 1.75x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 28.4 us: 1.75x faster                                                       |
| pylint                   | 566 ms                                                       | 325 ms: 1.74x faster                                                        |
| float                    | 111 ms                                                       | 63.9 ms: 1.74x faster                                                       |
| pyflate                  | 733 ms                                                       | 423 ms: 1.73x faster                                                        |
| raytrace                 | 489 ms                                                       | 282 ms: 1.73x faster                                                        |
| spectral_norm            | 139 ms                                                       | 81.2 ms: 1.71x faster                                                       |
| deepcopy                 | 468 us                                                       | 276 us: 1.69x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 64.2 ms: 1.67x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 195 us: 1.60x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 77.3 ms: 1.54x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.54x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.90 sec: 1.54x faster                                                      |
| hexiom                   | 9.42 ms                                                      | 6.20 ms: 1.52x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.79 ms: 1.50x faster                                                       |
| logging_simple           | 8.88 us                                                      | 5.91 us: 1.50x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.50 us: 1.48x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.49 sec: 1.45x faster                                                      |
| django_template          | 50.2 ms                                                      | 34.8 ms: 1.44x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 729 ms: 1.44x faster                                                        |
| regex_compile            | 190 ms                                                       | 132 ms: 1.44x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 67.5 ms: 1.40x faster                                                       |
| thrift                   | 1.18 ms                                                      | 852 us: 1.38x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 332 us: 1.37x faster                                                        |
| nbody                    | 134 ms                                                       | 98.1 ms: 1.37x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 59.7 ms: 1.36x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                      |
| deepcopy_reduce          | 4.01 us                                                      | 2.96 us: 1.35x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 23.3 ms: 1.35x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 56.6 ms: 1.34x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.6 ms: 1.34x faster                                                       |
| fannkuch                 | 483 ms                                                       | 362 ms: 1.33x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.7 ms: 1.28x faster                                                       |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.27x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.4 ms: 1.26x faster                                                       |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                        |
| nqueens                  | 115 ms                                                       | 93.3 ms: 1.23x faster                                                       |
| 2to3                     | 350 ms                                                       | 287 ms: 1.22x faster                                                        |
| scimark_fft              | 361 ms                                                       | 297 ms: 1.22x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.22x faster                                                       |
| sympy_expand             | 600 ms                                                       | 497 ms: 1.21x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 50.9 ns: 1.18x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 23.1 ms: 1.17x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 987 us: 1.16x faster                                                        |
| regex_dna                | 261 ms                                                       | 227 ms: 1.15x faster                                                        |
| meteor_contest           | 138 ms                                                       | 121 ms: 1.14x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 81.9 ms: 1.13x faster                                                       |
| json                     | 5.86 ms                                                      | 5.32 ms: 1.10x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 146 ms: 1.10x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.10x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.79 us: 1.07x faster                                                       |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.83 ms: 1.05x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 383 ms: 1.02x faster                                                        |
| async_generators         | 421 ms                                                       | 448 ms: 1.06x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 4.99 us: 1.07x slower                                                       |
| unpickle                 | 13.5 us                                                      | 14.7 us: 1.09x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 34.2 us: 1.16x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.70 ms: 1.20x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.81 ms: 1.20x slower                                                       |
| pickle_list              | 4.12 us                                                      | 5.00 us: 1.21x slower                                                       |
| coverage                 | 63.3 ms                                                      | 79.7 ms: 1.26x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.7 us: 1.29x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.85 ms: 1.62x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.28 ms: 1.84x slower                                                       |
| telco                    | 7.23 ms                                                      | 158 ms: 21.85x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 1.38 sec: 217.17x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.332x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.40x
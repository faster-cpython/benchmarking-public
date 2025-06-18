# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.125x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 314 ms: 1.11x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.09 sec: 1.10x faster                                                      |
| html5lib       | 94.6 ms                                                      | 70.8 ms: 1.34x faster                                                       |
| Geometric mean | (ref)                                                        | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 688 ms: 2.32x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 358 ms: 2.29x faster                                                        |
| async_tree_none         | 692 ms                                                       | 305 ms: 2.27x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 655 ms: 1.43x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.04x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 81.8 ms: 1.36x faster                                                       |
| nbody          | 134 ms                                                       | 99.2 ms: 1.35x faster                                                       |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 153 ms: 1.24x faster                                                        |
| regex_dna      | 261 ms                                                       | 239 ms: 1.09x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 27.2 ms: 1.00x slower                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.24 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 241 us: 1.29x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.34 sec: 1.25x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 380 us: 1.20x faster                                                        |
| json_loads           | 30.3 us                                                      | 29.2 us: 1.04x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 73.8 ms: 1.03x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 14.2 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 114 ms: 1.04x slower                                                        |
| xml_etree_parse      | 160 ms                                                       | 168 ms: 1.05x slower                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 108 ms: 1.17x slower                                                        |
| unpickle_list        | 4.65 us                                                      | 5.50 us: 1.18x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 35.4 us: 1.20x slower                                                       |
| unpickle             | 13.5 us                                                      | 18.0 us: 1.33x slower                                                       |
| pickle_list          | 4.12 us                                                      | 5.91 us: 1.44x slower                                                       |
| pickle               | 9.89 us                                                      | 14.8 us: 1.50x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.41 ms: 1.28x slower                                                       |
| python_startup         | 11.5 ms                                                      | 16.4 ms: 1.43x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.35x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 42.5 ms: 1.18x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 27.5 ms: 1.14x faster                                                       |
| mako            | 14.7 ms                                                      | 13.2 ms: 1.11x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 59.8 ms: 1.06x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.12x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 208 us: 2.58x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 688 ms: 2.32x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 358 ms: 2.29x faster                                                        |
| async_tree_none          | 692 ms                                                       | 305 ms: 2.27x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.47 ms: 2.16x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 371 ms: 2.10x faster                                                        |
| go                       | 262 ms                                                       | 129 ms: 2.03x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| mdp                      | 3.01 sec                                                     | 1.56 sec: 1.93x faster                                                      |
| generators               | 57.3 ms                                                      | 32.4 ms: 1.77x faster                                                       |
| pylint                   | 566 ms                                                       | 349 ms: 1.62x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 31.5 us: 1.58x faster                                                       |
| pyflate                  | 733 ms                                                       | 467 ms: 1.57x faster                                                        |
| chaos                    | 109 ms                                                       | 71.0 ms: 1.53x faster                                                       |
| richards_super           | 90.6 ms                                                      | 59.4 ms: 1.53x faster                                                       |
| scimark_sor              | 180 ms                                                       | 119 ms: 1.51x faster                                                        |
| deepcopy                 | 468 us                                                       | 320 us: 1.46x faster                                                        |
| raytrace                 | 489 ms                                                       | 335 ms: 1.46x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.54 ms: 1.44x faster                                                       |
| richards                 | 75.1 ms                                                      | 52.3 ms: 1.44x faster                                                       |
| scimark_lu               | 167 ms                                                       | 116 ms: 1.44x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 655 ms: 1.43x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 76.0 ms: 1.41x faster                                                       |
| comprehensions           | 26.7 us                                                      | 18.9 us: 1.41x faster                                                       |
| float                    | 111 ms                                                       | 81.8 ms: 1.36x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 87.9 ms: 1.36x faster                                                       |
| nbody                    | 134 ms                                                       | 99.2 ms: 1.35x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 70.8 ms: 1.34x faster                                                       |
| coroutines               | 30.3 ms                                                      | 23.1 ms: 1.31x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 241 us: 1.29x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 63.9 ms: 1.27x faster                                                       |
| spectral_norm            | 139 ms                                                       | 111 ms: 1.26x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.34 sec: 1.25x faster                                                      |
| tomli_loads              | 2.92 sec                                                     | 2.34 sec: 1.25x faster                                                      |
| regex_compile            | 190 ms                                                       | 153 ms: 1.24x faster                                                        |
| logging_simple           | 8.88 us                                                      | 7.41 us: 1.20x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 380 us: 1.20x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.6 ms: 1.19x faster                                                       |
| django_template          | 50.2 ms                                                      | 42.5 ms: 1.18x faster                                                       |
| logging_format           | 9.64 us                                                      | 8.27 us: 1.17x faster                                                       |
| sympy_sum                | 193 ms                                                       | 168 ms: 1.15x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 27.5 ms: 1.14x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.53 us: 1.14x faster                                                       |
| thrift                   | 1.18 ms                                                      | 1.04 ms: 1.13x faster                                                       |
| 2to3                     | 350 ms                                                       | 314 ms: 1.11x faster                                                        |
| mako                     | 14.7 ms                                                      | 13.2 ms: 1.11x faster                                                       |
| docutils                 | 3.41 sec                                                     | 3.09 sec: 1.10x faster                                                      |
| bench_thread_pool        | 1.14 ms                                                      | 1.04 ms: 1.09x faster                                                       |
| regex_dna                | 261 ms                                                       | 239 ms: 1.09x faster                                                        |
| sympy_str                | 360 ms                                                       | 330 ms: 1.09x faster                                                        |
| fannkuch                 | 483 ms                                                       | 444 ms: 1.09x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 19.8 ms: 1.08x faster                                                       |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                        |
| nqueens                  | 115 ms                                                       | 108 ms: 1.06x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 56.6 ns: 1.06x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 59.8 ms: 1.06x faster                                                       |
| sympy_expand             | 600 ms                                                       | 571 ms: 1.05x faster                                                        |
| json_loads               | 30.3 us                                                      | 29.2 us: 1.04x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 73.8 ms: 1.03x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 14.2 ms: 1.03x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 27.2 ms: 1.00x slower                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 1.06 sec: 1.01x slower                                                      |
| meteor_contest           | 138 ms                                                       | 140 ms: 1.01x slower                                                        |
| json                     | 5.86 ms                                                      | 6.02 ms: 1.03x slower                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 114 ms: 1.04x slower                                                        |
| xml_etree_parse          | 160 ms                                                       | 168 ms: 1.05x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.24 ms: 1.05x slower                                                       |
| async_generators         | 421 ms                                                       | 449 ms: 1.07x slower                                                        |
| scimark_fft              | 361 ms                                                       | 386 ms: 1.07x slower                                                        |
| sqlite_synth             | 2.99 us                                                      | 3.40 us: 1.14x slower                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 108 ms: 1.17x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 5.50 us: 1.18x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 35.4 us: 1.20x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.41 ms: 1.28x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 6.53 ms: 1.29x slower                                                       |
| telco                    | 7.23 ms                                                      | 9.52 ms: 1.32x slower                                                       |
| unpickle                 | 13.5 us                                                      | 18.0 us: 1.33x slower                                                       |
| python_startup           | 11.5 ms                                                      | 16.4 ms: 1.43x slower                                                       |
| pickle_list              | 4.12 us                                                      | 5.91 us: 1.44x slower                                                       |
| pickle                   | 9.89 us                                                      | 14.8 us: 1.50x slower                                                       |
| coverage                 | 63.3 ms                                                      | 101 ms: 1.60x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 5.73 ms: 1.68x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 3.00 ms: 1.70x slower                                                       |
| logging_silent           | 167 ns                                                       | 689 ns: 4.12x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.46 sec: 228.41x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.08x faster                                                                |

Benchmark hidden because not significant (1): pprint_pformat
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.125x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.37x
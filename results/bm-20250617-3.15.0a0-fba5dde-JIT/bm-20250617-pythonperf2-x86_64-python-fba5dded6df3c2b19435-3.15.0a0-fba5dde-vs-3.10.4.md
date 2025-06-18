# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.122x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 322 ms: 1.09x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.17 sec: 1.08x faster                                                      |
| html5lib       | 94.6 ms                                                      | 71.1 ms: 1.33x faster                                                       |
| Geometric mean | (ref)                                                        | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 699 ms: 2.29x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 363 ms: 2.26x faster                                                        |
| async_tree_none         | 692 ms                                                       | 312 ms: 2.21x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 631 ms: 1.48x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.03x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 75.3 ms: 1.48x faster                                                       |
| nbody          | 134 ms                                                       | 109 ms: 1.23x faster                                                        |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 156 ms: 1.22x faster                                                        |
| regex_dna      | 261 ms                                                       | 239 ms: 1.10x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.34 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.92 sec                                                     | 2.27 sec: 1.28x faster                                                      |
| unpickle_pure_python | 312 us                                                       | 244 us: 1.28x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 391 us: 1.16x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 71.5 ms: 1.06x faster                                                       |
| json_loads           | 30.3 us                                                      | 29.4 us: 1.03x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 14.2 ms: 1.02x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 164 ms: 1.02x slower                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 116 ms: 1.05x slower                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 106 ms: 1.15x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 35.5 us: 1.20x slower                                                       |
| unpickle_list        | 4.65 us                                                      | 5.59 us: 1.20x slower                                                       |
| unpickle             | 13.5 us                                                      | 18.6 us: 1.38x slower                                                       |
| pickle_list          | 4.12 us                                                      | 5.93 us: 1.44x slower                                                       |
| pickle               | 9.89 us                                                      | 14.9 us: 1.51x slower                                                       |
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
| django_template | 50.2 ms                                                      | 43.2 ms: 1.16x faster                                                       |
| mako            | 14.7 ms                                                      | 12.9 ms: 1.14x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 28.1 ms: 1.12x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 61.2 ms: 1.03x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.11x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 213 us: 2.52x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 699 ms: 2.29x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 363 ms: 2.26x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.34 ms: 2.25x faster                                                       |
| async_tree_none          | 692 ms                                                       | 312 ms: 2.21x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 374 ms: 2.08x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.59 sec: 1.95x faster                                                      |
| mdp                      | 3.01 sec                                                     | 1.56 sec: 1.92x faster                                                      |
| richards_super           | 90.6 ms                                                      | 48.5 ms: 1.87x faster                                                       |
| go                       | 262 ms                                                       | 143 ms: 1.83x faster                                                        |
| richards                 | 75.1 ms                                                      | 41.2 ms: 1.82x faster                                                       |
| generators               | 57.3 ms                                                      | 34.9 ms: 1.64x faster                                                       |
| pylint                   | 566 ms                                                       | 355 ms: 1.59x faster                                                        |
| pyflate                  | 733 ms                                                       | 471 ms: 1.56x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 32.9 us: 1.51x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 631 ms: 1.48x faster                                                        |
| float                    | 111 ms                                                       | 75.3 ms: 1.48x faster                                                       |
| chaos                    | 109 ms                                                       | 73.6 ms: 1.47x faster                                                       |
| raytrace                 | 489 ms                                                       | 339 ms: 1.44x faster                                                        |
| scimark_sor              | 180 ms                                                       | 126 ms: 1.43x faster                                                        |
| deepcopy                 | 468 us                                                       | 328 us: 1.43x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 77.2 ms: 1.39x faster                                                       |
| scimark_lu               | 167 ms                                                       | 120 ms: 1.39x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.94 ms: 1.36x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 71.1 ms: 1.33x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 91.2 ms: 1.31x faster                                                       |
| coroutines               | 30.3 ms                                                      | 23.2 ms: 1.30x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.27 sec: 1.28x faster                                                      |
| unpickle_pure_python     | 312 us                                                       | 244 us: 1.28x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 63.8 ms: 1.27x faster                                                       |
| comprehensions           | 26.7 us                                                      | 21.2 us: 1.26x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.33 sec: 1.26x faster                                                      |
| nbody                    | 134 ms                                                       | 109 ms: 1.23x faster                                                        |
| regex_compile            | 190 ms                                                       | 156 ms: 1.22x faster                                                        |
| spectral_norm            | 139 ms                                                       | 118 ms: 1.18x faster                                                        |
| logging_simple           | 8.88 us                                                      | 7.58 us: 1.17x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 391 us: 1.16x faster                                                        |
| django_template          | 50.2 ms                                                      | 43.2 ms: 1.16x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 24.3 ms: 1.16x faster                                                       |
| logging_format           | 9.64 us                                                      | 8.33 us: 1.16x faster                                                       |
| mako                     | 14.7 ms                                                      | 12.9 ms: 1.14x faster                                                       |
| thrift                   | 1.18 ms                                                      | 1.04 ms: 1.13x faster                                                       |
| sympy_sum                | 193 ms                                                       | 171 ms: 1.13x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.58 us: 1.12x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 28.1 ms: 1.12x faster                                                       |
| regex_dna                | 261 ms                                                       | 239 ms: 1.10x faster                                                        |
| 2to3                     | 350 ms                                                       | 322 ms: 1.09x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.17 sec: 1.08x faster                                                      |
| bench_thread_pool        | 1.14 ms                                                      | 1.06 ms: 1.07x faster                                                       |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| sympy_str                | 360 ms                                                       | 337 ms: 1.07x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 20.1 ms: 1.06x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 71.5 ms: 1.06x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                                       |
| nqueens                  | 115 ms                                                       | 111 ms: 1.04x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 61.2 ms: 1.03x faster                                                       |
| json_loads               | 30.3 us                                                      | 29.4 us: 1.03x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 2.10 sec: 1.03x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 14.2 ms: 1.02x faster                                                       |
| sympy_expand             | 600 ms                                                       | 592 ms: 1.01x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                        |
| fannkuch                 | 483 ms                                                       | 486 ms: 1.01x slower                                                        |
| xml_etree_parse          | 160 ms                                                       | 164 ms: 1.02x slower                                                        |
| meteor_contest           | 138 ms                                                       | 142 ms: 1.02x slower                                                        |
| json                     | 5.86 ms                                                      | 6.02 ms: 1.03x slower                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 116 ms: 1.05x slower                                                        |
| scimark_fft              | 361 ms                                                       | 383 ms: 1.06x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.34 ms: 1.08x slower                                                       |
| async_generators         | 421 ms                                                       | 472 ms: 1.12x slower                                                        |
| sqlite_synth             | 2.99 us                                                      | 3.36 us: 1.13x slower                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 106 ms: 1.15x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 35.5 us: 1.20x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 5.59 us: 1.20x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 6.40 ms: 1.26x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.41 ms: 1.28x slower                                                       |
| telco                    | 7.23 ms                                                      | 9.68 ms: 1.34x slower                                                       |
| unpickle                 | 13.5 us                                                      | 18.6 us: 1.38x slower                                                       |
| python_startup           | 11.5 ms                                                      | 16.4 ms: 1.43x slower                                                       |
| pickle_list              | 4.12 us                                                      | 5.93 us: 1.44x slower                                                       |
| pickle                   | 9.89 us                                                      | 14.9 us: 1.51x slower                                                       |
| coverage                 | 63.3 ms                                                      | 99.8 ms: 1.58x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 5.62 ms: 1.64x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.94 ms: 1.67x slower                                                       |
| logging_silent           | 167 ns                                                       | 685 ns: 4.09x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.57 sec: 246.87x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.07x faster                                                                |

Benchmark hidden because not significant (2): pprint_safe_repr, unpack_sequence
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.122x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.40x
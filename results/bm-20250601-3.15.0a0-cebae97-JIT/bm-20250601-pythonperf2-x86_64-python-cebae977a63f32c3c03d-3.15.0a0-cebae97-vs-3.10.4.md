# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.627x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 320 ms: 1.09x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.17 sec: 1.08x faster                                                      |
| html5lib       | 94.6 ms                                                      | 70.9 ms: 1.34x faster                                                       |
| Geometric mean | (ref)                                                        | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 696 ms: 2.30x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 365 ms: 2.25x faster                                                        |
| async_tree_none         | 692 ms                                                       | 314 ms: 2.20x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 677 ms: 1.38x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.99x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 72.7 ms: 1.53x faster                                                       |
| nbody          | 134 ms                                                       | 107 ms: 1.25x faster                                                        |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 243 ms: 1.08x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 27.3 ms: 1.01x slower                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.32 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 239 us: 1.30x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.31 sec: 1.26x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 380 us: 1.20x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 70.1 ms: 1.08x faster                                                       |
| json_loads           | 30.3 us                                                      | 29.4 us: 1.03x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 14.2 ms: 1.03x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 164 ms: 1.02x slower                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 115 ms: 1.04x slower                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 104 ms: 1.13x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 35.3 us: 1.19x slower                                                       |
| unpickle_list        | 4.65 us                                                      | 5.59 us: 1.20x slower                                                       |
| unpickle             | 13.5 us                                                      | 17.7 us: 1.31x slower                                                       |
| pickle_list          | 4.12 us                                                      | 5.97 us: 1.45x slower                                                       |
| pickle               | 9.89 us                                                      | 14.6 us: 1.48x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.44 ms: 1.29x slower                                                       |
| python_startup         | 11.5 ms                                                      | 16.5 ms: 1.43x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.36x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 42.4 ms: 1.18x faster                                                       |
| mako            | 14.7 ms                                                      | 13.5 ms: 1.09x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 29.2 ms: 1.08x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.09x faster                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pprint_pformat           | 2.15 sec                                                     | 1.83 us: 1178432.50x faster                                                 |
| pprint_safe_repr         | 1.05 sec                                                     | 1.12 us: 937093.67x faster                                                  |
| typing_runtime_protocols | 537 us                                                       | 216 us: 2.48x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.20 ms: 2.34x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 696 ms: 2.30x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 365 ms: 2.25x faster                                                        |
| async_tree_none          | 692 ms                                                       | 314 ms: 2.20x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 376 ms: 2.07x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.59 sec: 1.95x faster                                                      |
| mdp                      | 3.01 sec                                                     | 1.57 sec: 1.92x faster                                                      |
| richards_super           | 90.6 ms                                                      | 47.9 ms: 1.89x faster                                                       |
| go                       | 262 ms                                                       | 141 ms: 1.86x faster                                                        |
| richards                 | 75.1 ms                                                      | 40.6 ms: 1.85x faster                                                       |
| generators               | 57.3 ms                                                      | 33.0 ms: 1.74x faster                                                       |
| pylint                   | 566 ms                                                       | 356 ms: 1.59x faster                                                        |
| pyflate                  | 733 ms                                                       | 462 ms: 1.59x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 32.0 us: 1.56x faster                                                       |
| float                    | 111 ms                                                       | 72.7 ms: 1.53x faster                                                       |
| chaos                    | 109 ms                                                       | 73.4 ms: 1.48x faster                                                       |
| scimark_sor              | 180 ms                                                       | 123 ms: 1.46x faster                                                        |
| deepcopy                 | 468 us                                                       | 320 us: 1.46x faster                                                        |
| raytrace                 | 489 ms                                                       | 339 ms: 1.44x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 76.3 ms: 1.41x faster                                                       |
| scimark_lu               | 167 ms                                                       | 121 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 677 ms: 1.38x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.93 ms: 1.36x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 70.9 ms: 1.34x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 239 us: 1.30x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 93.9 ms: 1.27x faster                                                       |
| coroutines               | 30.3 ms                                                      | 23.9 ms: 1.27x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 64.0 ms: 1.27x faster                                                       |
| comprehensions           | 26.7 us                                                      | 21.1 us: 1.26x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.31 sec: 1.26x faster                                                      |
| pycparser                | 1.67 sec                                                     | 1.34 sec: 1.25x faster                                                      |
| nbody                    | 134 ms                                                       | 107 ms: 1.25x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 380 us: 1.20x faster                                                        |
| django_template          | 50.2 ms                                                      | 42.4 ms: 1.18x faster                                                       |
| spectral_norm            | 139 ms                                                       | 118 ms: 1.18x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 24.3 ms: 1.16x faster                                                       |
| logging_simple           | 8.88 us                                                      | 7.73 us: 1.15x faster                                                       |
| thrift                   | 1.18 ms                                                      | 1.04 ms: 1.13x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.54 us: 1.13x faster                                                       |
| logging_format           | 9.64 us                                                      | 8.59 us: 1.12x faster                                                       |
| sympy_sum                | 193 ms                                                       | 172 ms: 1.12x faster                                                        |
| 2to3                     | 350 ms                                                       | 320 ms: 1.09x faster                                                        |
| mako                     | 14.7 ms                                                      | 13.5 ms: 1.09x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 70.1 ms: 1.08x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 1.05 ms: 1.08x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 19.8 ms: 1.08x faster                                                       |
| regex_dna                | 261 ms                                                       | 243 ms: 1.08x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.17 sec: 1.08x faster                                                      |
| genshi_text              | 31.4 ms                                                      | 29.2 ms: 1.08x faster                                                       |
| sympy_str                | 360 ms                                                       | 336 ms: 1.07x faster                                                        |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                        |
| nqueens                  | 115 ms                                                       | 111 ms: 1.04x faster                                                        |
| json_loads               | 30.3 us                                                      | 29.4 us: 1.03x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 14.2 ms: 1.03x faster                                                       |
| sympy_expand             | 600 ms                                                       | 586 ms: 1.02x faster                                                        |
| fannkuch                 | 483 ms                                                       | 479 ms: 1.01x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 27.3 ms: 1.01x slower                                                       |
| json                     | 5.86 ms                                                      | 5.98 ms: 1.02x slower                                                       |
| xml_etree_parse          | 160 ms                                                       | 164 ms: 1.02x slower                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 115 ms: 1.04x slower                                                        |
| meteor_contest           | 138 ms                                                       | 146 ms: 1.05x slower                                                        |
| unpack_sequence          | 59.9 ns                                                      | 63.1 ns: 1.05x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.32 ms: 1.07x slower                                                       |
| scimark_fft              | 361 ms                                                       | 397 ms: 1.10x slower                                                        |
| async_generators         | 421 ms                                                       | 468 ms: 1.11x slower                                                        |
| sqlite_synth             | 2.99 us                                                      | 3.36 us: 1.13x slower                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 104 ms: 1.13x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 35.3 us: 1.19x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 5.59 us: 1.20x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 6.30 ms: 1.24x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.44 ms: 1.29x slower                                                       |
| unpickle                 | 13.5 us                                                      | 17.7 us: 1.31x slower                                                       |
| telco                    | 7.23 ms                                                      | 9.67 ms: 1.34x slower                                                       |
| python_startup           | 11.5 ms                                                      | 16.5 ms: 1.43x slower                                                       |
| pickle_list              | 4.12 us                                                      | 5.97 us: 1.45x slower                                                       |
| pickle                   | 9.89 us                                                      | 14.6 us: 1.48x slower                                                       |
| coverage                 | 63.3 ms                                                      | 96.4 ms: 1.52x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 5.70 ms: 1.67x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.99 ms: 1.70x slower                                                       |
| logging_silent           | 167 ns                                                       | 668 ns: 3.99x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 2.17 sec: 340.84x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.48x faster                                                                |

Benchmark hidden because not significant (2): genshi_xml, asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.627x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.37x
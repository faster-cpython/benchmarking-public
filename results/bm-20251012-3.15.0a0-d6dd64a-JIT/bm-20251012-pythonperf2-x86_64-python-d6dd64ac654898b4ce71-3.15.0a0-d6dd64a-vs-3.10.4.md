# Results vs. 3.10.4

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: linux-x86_64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.338x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.25x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| html5lib       | 94.6 ms                                                      | 66.6 ms: 1.42x faster                                                       |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 616 ms: 2.59x faster                                                        |
| async_tree_none         | 692 ms                                                       | 272 ms: 2.54x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 328 ms: 2.50x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 502 ms: 1.87x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 67.8 ms: 1.64x faster                                                       |
| nbody          | 134 ms                                                       | 103 ms: 1.30x faster                                                        |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 132 ms: 1.44x faster                                                        |
| regex_dna      | 261 ms                                                       | 225 ms: 1.16x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 24.2 ms: 1.12x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.30 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                        | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 194 us: 1.61x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.90 sec: 1.53x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.1 ms: 1.45x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 329 us: 1.38x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 55.5 ms: 1.37x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 80.1 ms: 1.15x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 96.5 ms: 1.14x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 5.07 us: 1.09x slower                                                       |
| unpickle             | 13.5 us                                                      | 14.8 us: 1.10x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 33.5 us: 1.13x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.98 us: 1.21x slower                                                       |
| pickle               | 9.89 us                                                      | 12.2 us: 1.24x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.83 ms: 1.20x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.85 ms: 1.49x faster                                                       |
| django_template | 50.2 ms                                                      | 34.9 ms: 1.44x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.2 ms: 1.35x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 53.8 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.36x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 171 us: 3.14x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 616 ms: 2.59x faster                                                        |
| async_tree_none          | 692 ms                                                       | 272 ms: 2.54x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 328 ms: 2.50x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.27 sec: 2.38x faster                                                      |
| deltablue                | 7.50 ms                                                      | 3.19 ms: 2.35x faster                                                       |
| go                       | 262 ms                                                       | 119 ms: 2.20x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 371 ms: 2.10x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| generators               | 57.3 ms                                                      | 30.1 ms: 1.91x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 26.2 us: 1.90x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 502 ms: 1.87x faster                                                        |
| chaos                    | 109 ms                                                       | 58.4 ms: 1.86x faster                                                       |
| pyflate                  | 733 ms                                                       | 395 ms: 1.85x faster                                                        |
| logging_silent           | 167 ns                                                       | 92.4 ns: 1.81x faster                                                       |
| deepcopy                 | 468 us                                                       | 262 us: 1.78x faster                                                        |
| pylint                   | 566 ms                                                       | 320 ms: 1.77x faster                                                        |
| richards_super           | 90.6 ms                                                      | 51.3 ms: 1.77x faster                                                       |
| scimark_lu               | 167 ms                                                       | 94.6 ms: 1.76x faster                                                       |
| scimark_sor              | 180 ms                                                       | 103 ms: 1.75x faster                                                        |
| raytrace                 | 489 ms                                                       | 280 ms: 1.75x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 63.9 ms: 1.68x faster                                                       |
| richards                 | 75.1 ms                                                      | 45.3 ms: 1.66x faster                                                       |
| float                    | 111 ms                                                       | 67.8 ms: 1.64x faster                                                       |
| spectral_norm            | 139 ms                                                       | 86.2 ms: 1.61x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 194 us: 1.61x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 5.94 ms: 1.59x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 76.9 ms: 1.55x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.54x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.90 sec: 1.53x faster                                                      |
| logging_simple           | 8.88 us                                                      | 5.89 us: 1.51x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.85 ms: 1.49x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.49 us: 1.49x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.47 sec: 1.47x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 10.1 ms: 1.45x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 727 ms: 1.44x faster                                                        |
| regex_compile            | 190 ms                                                       | 132 ms: 1.44x faster                                                        |
| django_template          | 50.2 ms                                                      | 34.9 ms: 1.44x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 66.6 ms: 1.42x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.2 ms: 1.40x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.87 us: 1.40x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.20 sec: 1.39x faster                                                      |
| pickle_pure_python       | 455 us                                                       | 329 us: 1.38x faster                                                        |
| thrift                   | 1.18 ms                                                      | 851 us: 1.38x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 55.5 ms: 1.37x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 59.6 ms: 1.36x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 23.2 ms: 1.35x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.6 ms: 1.34x faster                                                       |
| fannkuch                 | 483 ms                                                       | 363 ms: 1.33x faster                                                        |
| scimark_fft              | 361 ms                                                       | 273 ms: 1.32x faster                                                        |
| nbody                    | 134 ms                                                       | 103 ms: 1.30x faster                                                        |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.29x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.2 ms: 1.27x faster                                                       |
| nqueens                  | 115 ms                                                       | 92.0 ms: 1.25x faster                                                       |
| 2to3                     | 350 ms                                                       | 281 ms: 1.25x faster                                                        |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 930 us: 1.23x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| sympy_expand             | 600 ms                                                       | 502 ms: 1.20x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 53.8 ms: 1.18x faster                                                       |
| regex_dna                | 261 ms                                                       | 225 ms: 1.16x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 80.1 ms: 1.15x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 96.5 ms: 1.14x faster                                                       |
| meteor_contest           | 138 ms                                                       | 121 ms: 1.14x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 52.9 ns: 1.13x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 24.2 ms: 1.12x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.77 us: 1.08x faster                                                       |
| json                     | 5.86 ms                                                      | 5.44 ms: 1.08x faster                                                       |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.78 ms: 1.06x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                        |
| async_generators         | 421 ms                                                       | 442 ms: 1.05x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.30 ms: 1.07x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 5.07 us: 1.09x slower                                                       |
| unpickle                 | 13.5 us                                                      | 14.8 us: 1.10x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 33.5 us: 1.13x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.83 ms: 1.20x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.98 us: 1.21x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.2 us: 1.24x slower                                                       |
| coverage                 | 63.3 ms                                                      | 80.3 ms: 1.27x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.90 ms: 1.64x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.51 ms: 1.90x slower                                                       |
| telco                    | 7.23 ms                                                      | 154 ms: 21.26x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 2.57 sec: 402.50x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.338x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.41x
# Results vs. 3.10.4

- fork: python
- ref: 9c7b2af73dee2b997936
- machine: linux-x86_64
- commit hash: 9c7b2af
- commit date: 2025-07-21
- overall geometric mean: 1.334x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.22x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| html5lib       | 94.6 ms                                                      | 67.5 ms: 1.40x faster                                                       |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 625 ms: 2.56x faster                                                        |
| async_tree_none         | 692 ms                                                       | 274 ms: 2.53x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 329 ms: 2.49x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 500 ms: 1.87x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.34x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 64.2 ms: 1.73x faster                                                       |
| nbody          | 134 ms                                                       | 98.4 ms: 1.36x faster                                                       |
| pidigits       | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.36x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 132 ms: 1.44x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 22.9 ms: 1.18x faster                                                       |
| regex_dna      | 261 ms                                                       | 228 ms: 1.15x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.71 ms: 1.20x slower                                                       |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 197 us: 1.59x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.92 sec: 1.52x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 334 us: 1.36x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 56.6 ms: 1.34x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.9 us: 1.22x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 96.9 ms: 1.14x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 81.6 ms: 1.13x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.72 ms: 1.19x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.65 ms: 1.52x faster                                                       |
| django_template | 50.2 ms                                                      | 35.5 ms: 1.42x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.0 ms: 1.36x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 54.4 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.36x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 171 us: 3.15x faster                                                        |
| deltablue                | 7.50 ms                                                      | 2.90 ms: 2.59x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 625 ms: 2.56x faster                                                        |
| async_tree_none          | 692 ms                                                       | 274 ms: 2.53x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 329 ms: 2.49x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.28 sec: 2.34x faster                                                      |
| richards_super           | 90.6 ms                                                      | 40.8 ms: 2.22x faster                                                       |
| richards                 | 75.1 ms                                                      | 35.0 ms: 2.15x faster                                                       |
| go                       | 262 ms                                                       | 128 ms: 2.05x faster                                                        |
| generators               | 57.3 ms                                                      | 29.0 ms: 1.98x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 500 ms: 1.87x faster                                                        |
| chaos                    | 109 ms                                                       | 59.9 ms: 1.81x faster                                                       |
| logging_silent           | 167 ns                                                       | 93.8 ns: 1.78x faster                                                       |
| scimark_lu               | 167 ms                                                       | 95.0 ms: 1.76x faster                                                       |
| spectral_norm            | 139 ms                                                       | 79.2 ms: 1.76x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 28.3 us: 1.76x faster                                                       |
| scimark_sor              | 180 ms                                                       | 103 ms: 1.75x faster                                                        |
| pylint                   | 566 ms                                                       | 324 ms: 1.75x faster                                                        |
| pyflate                  | 733 ms                                                       | 421 ms: 1.74x faster                                                        |
| float                    | 111 ms                                                       | 64.2 ms: 1.73x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 62.5 ms: 1.72x faster                                                       |
| raytrace                 | 489 ms                                                       | 291 ms: 1.68x faster                                                        |
| deepcopy                 | 468 us                                                       | 280 us: 1.67x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 197 us: 1.59x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 77.3 ms: 1.54x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.54x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.65 ms: 1.52x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.92 sec: 1.52x faster                                                      |
| hexiom                   | 9.42 ms                                                      | 6.20 ms: 1.52x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.06 us: 1.46x faster                                                       |
| regex_compile            | 190 ms                                                       | 132 ms: 1.44x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.69 us: 1.44x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.50 sec: 1.43x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 741 ms: 1.42x faster                                                        |
| django_template          | 50.2 ms                                                      | 35.5 ms: 1.42x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 67.5 ms: 1.40x faster                                                       |
| thrift                   | 1.18 ms                                                      | 840 us: 1.40x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 58.4 ms: 1.39x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 23.0 ms: 1.36x faster                                                       |
| nbody                    | 134 ms                                                       | 98.4 ms: 1.36x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 334 us: 1.36x faster                                                        |
| coroutines               | 30.3 ms                                                      | 22.3 ms: 1.36x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 56.6 ms: 1.34x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                      |
| deepcopy_reduce          | 4.01 us                                                      | 3.03 us: 1.32x faster                                                       |
| fannkuch                 | 483 ms                                                       | 369 ms: 1.31x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                       |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.27x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.4 ms: 1.26x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 17.0 ms: 1.25x faster                                                       |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                        |
| nqueens                  | 115 ms                                                       | 93.2 ms: 1.23x faster                                                       |
| 2to3                     | 350 ms                                                       | 286 ms: 1.22x faster                                                        |
| json_loads               | 30.3 us                                                      | 24.9 us: 1.22x faster                                                       |
| scimark_fft              | 361 ms                                                       | 300 ms: 1.21x faster                                                        |
| sympy_expand             | 600 ms                                                       | 498 ms: 1.20x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 22.9 ms: 1.18x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 54.4 ms: 1.16x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| regex_dna                | 261 ms                                                       | 228 ms: 1.15x faster                                                        |
| meteor_contest           | 138 ms                                                       | 121 ms: 1.14x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 96.9 ms: 1.14x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 81.6 ms: 1.13x faster                                                       |
| json                     | 5.86 ms                                                      | 5.40 ms: 1.09x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.80 us: 1.07x faster                                                       |
| pidigits                 | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.81 ms: 1.06x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 381 ms: 1.02x faster                                                        |
| async_generators         | 421 ms                                                       | 448 ms: 1.07x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.72 ms: 1.19x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.71 ms: 1.20x slower                                                       |
| coverage                 | 63.3 ms                                                      | 81.7 ms: 1.29x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.91 ms: 1.65x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.53 ms: 1.91x slower                                                       |
| telco                    | 7.23 ms                                                      | 159 ms: 22.00x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.34x faster                                                                |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250721-3.15.0a0-9c7b2af-JIT/bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.334x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.41x
# Results vs. 3.10.4

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-x86_64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.360x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.25x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                      |
| html5lib       | 94.6 ms                                                      | 66.3 ms: 1.43x faster                                                       |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 629 ms: 2.54x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 329 ms: 2.49x faster                                                        |
| async_tree_none         | 692 ms                                                       | 286 ms: 2.42x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 503 ms: 1.86x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 70.1 ms: 1.58x faster                                                       |
| nbody          | 134 ms                                                       | 95.1 ms: 1.41x faster                                                       |
| pidigits       | 271 ms                                                       | 257 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 134 ms: 1.42x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 24.6 ms: 1.10x faster                                                       |
| regex_dna      | 261 ms                                                       | 240 ms: 1.09x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.43 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 215 us: 1.45x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 330 us: 1.38x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 58.8 ms: 1.29x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 11.9 ms: 1.23x faster                                                       |
| json_loads           | 30.3 us                                                      | 26.4 us: 1.15x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.14x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 98.2 ms: 1.13x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 85.0 ms: 1.09x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 4.91 us: 1.06x slower                                                       |
| unpickle             | 13.5 us                                                      | 14.4 us: 1.07x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 34.6 us: 1.17x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.96 us: 1.20x slower                                                       |
| pickle               | 9.89 us                                                      | 12.2 us: 1.24x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.10x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.6 ms: 1.18x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 8.77 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.8 ms: 1.40x faster                                                       |
| mako            | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.3 ms: 1.35x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 53.3 ms: 1.19x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 171 us: 3.13x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 629 ms: 2.54x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 329 ms: 2.49x faster                                                        |
| async_tree_none          | 692 ms                                                       | 286 ms: 2.42x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.13 ms: 2.40x faster                                                       |
| mdp                      | 3.01 sec                                                     | 1.29 sec: 2.33x faster                                                      |
| go                       | 262 ms                                                       | 125 ms: 2.10x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 373 ms: 2.09x faster                                                        |
| generators               | 57.3 ms                                                      | 28.3 ms: 2.03x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.59 sec: 1.96x faster                                                      |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 503 ms: 1.86x faster                                                        |
| chaos                    | 109 ms                                                       | 60.0 ms: 1.81x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 27.6 us: 1.80x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 60.0 ms: 1.79x faster                                                       |
| richards_super           | 90.6 ms                                                      | 51.1 ms: 1.77x faster                                                       |
| scimark_lu               | 167 ms                                                       | 95.2 ms: 1.75x faster                                                       |
| pylint                   | 566 ms                                                       | 324 ms: 1.75x faster                                                        |
| raytrace                 | 489 ms                                                       | 282 ms: 1.73x faster                                                        |
| scimark_sor              | 180 ms                                                       | 105 ms: 1.71x faster                                                        |
| deepcopy                 | 468 us                                                       | 278 us: 1.68x faster                                                        |
| richards                 | 75.1 ms                                                      | 44.9 ms: 1.67x faster                                                       |
| pyflate                  | 733 ms                                                       | 452 ms: 1.62x faster                                                        |
| float                    | 111 ms                                                       | 70.1 ms: 1.58x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.1 us: 1.56x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.08 ms: 1.55x faster                                                       |
| spectral_norm            | 139 ms                                                       | 92.6 ms: 1.50x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 79.8 ms: 1.49x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 215 us: 1.45x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 66.3 ms: 1.43x faster                                                       |
| regex_compile            | 190 ms                                                       | 134 ms: 1.42x faster                                                        |
| nbody                    | 134 ms                                                       | 95.1 ms: 1.41x faster                                                       |
| django_template          | 50.2 ms                                                      | 35.8 ms: 1.40x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                                      |
| thrift                   | 1.18 ms                                                      | 851 us: 1.38x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 330 us: 1.38x faster                                                        |
| coroutines               | 30.3 ms                                                      | 22.1 ms: 1.37x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.59 sec: 1.36x faster                                                      |
| deepcopy_reduce          | 4.01 us                                                      | 2.96 us: 1.35x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.13 us: 1.35x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 60.0 ms: 1.35x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 23.3 ms: 1.35x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.59 us: 1.35x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 782 ms: 1.34x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                                      |
| unpack_sequence          | 59.9 ns                                                      | 45.7 ns: 1.31x faster                                                       |
| fannkuch                 | 483 ms                                                       | 369 ms: 1.31x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 58.8 ms: 1.29x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 22.1 ms: 1.27x faster                                                       |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                        |
| sympy_str                | 360 ms                                                       | 289 ms: 1.25x faster                                                        |
| nqueens                  | 115 ms                                                       | 92.2 ms: 1.25x faster                                                       |
| 2to3                     | 350 ms                                                       | 281 ms: 1.25x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 17.4 ms: 1.23x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 11.9 ms: 1.23x faster                                                       |
| sympy_expand             | 600 ms                                                       | 497 ms: 1.21x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 53.3 ms: 1.19x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 986 us: 1.16x faster                                                        |
| scimark_fft              | 361 ms                                                       | 313 ms: 1.16x faster                                                        |
| json_loads               | 30.3 us                                                      | 26.4 us: 1.15x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 141 ms: 1.14x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 98.2 ms: 1.13x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 24.6 ms: 1.10x faster                                                       |
| regex_dna                | 261 ms                                                       | 240 ms: 1.09x faster                                                        |
| json                     | 5.86 ms                                                      | 5.39 ms: 1.09x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 85.0 ms: 1.09x faster                                                       |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.75 ms: 1.07x faster                                                       |
| pidigits                 | 271 ms                                                       | 257 ms: 1.05x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.89 us: 1.04x faster                                                       |
| async_generators         | 421 ms                                                       | 429 ms: 1.02x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 4.91 us: 1.06x slower                                                       |
| unpickle                 | 13.5 us                                                      | 14.4 us: 1.07x slower                                                       |
| telco                    | 7.23 ms                                                      | 7.91 ms: 1.09x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.43 ms: 1.11x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 34.6 us: 1.17x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.6 ms: 1.18x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.77 ms: 1.20x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.96 us: 1.20x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.2 us: 1.24x slower                                                       |
| coverage                 | 63.3 ms                                                      | 84.6 ms: 1.34x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.80 ms: 1.59x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.42 ms: 1.88x slower                                                       |
| logging_silent           | 167 ns                                                       | 517 ns: 3.09x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.32 sec: 207.31x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (8) of results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: bpe_tokeniser, djangocms, many_optionals, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.360x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.32x
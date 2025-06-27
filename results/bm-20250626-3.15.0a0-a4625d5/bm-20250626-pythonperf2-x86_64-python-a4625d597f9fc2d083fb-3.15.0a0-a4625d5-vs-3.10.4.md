# Results vs. 3.10.4

- fork: python
- ref: a4625d597f9fc2d083fb
- machine: linux-x86_64
- commit hash: a4625d5
- commit date: 2025-06-26
- overall geometric mean: 1.380x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 280 ms: 1.25x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.83 sec: 1.21x faster                                                      |
| html5lib       | 94.6 ms                                                      | 67.3 ms: 1.41x faster                                                       |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 631 ms: 2.53x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 331 ms: 2.48x faster                                                        |
| async_tree_none         | 692 ms                                                       | 283 ms: 2.45x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 504 ms: 1.86x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 70.6 ms: 1.57x faster                                                       |
| nbody          | 134 ms                                                       | 92.3 ms: 1.45x faster                                                       |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.43x faster                                                        |
| regex_dna      | 261 ms                                                       | 221 ms: 1.18x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.1 ms: 1.18x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.49 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 206 us: 1.51x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 330 us: 1.38x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.1 ms: 1.30x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 58.2 ms: 1.30x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.5 us: 1.19x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 140 ms: 1.14x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 97.4 ms: 1.13x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 83.4 ms: 1.11x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.80 ms: 1.20x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.3 ms: 1.42x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 22.8 ms: 1.38x faster                                                       |
| mako            | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 52.1 ms: 1.21x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.34x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 163 us: 3.28x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 631 ms: 2.53x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 331 ms: 2.48x faster                                                        |
| async_tree_none          | 692 ms                                                       | 283 ms: 2.45x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.18 ms: 2.36x faster                                                       |
| mdp                      | 3.01 sec                                                     | 1.29 sec: 2.33x faster                                                      |
| go                       | 262 ms                                                       | 119 ms: 2.20x faster                                                        |
| generators               | 57.3 ms                                                      | 30.1 ms: 1.90x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 504 ms: 1.86x faster                                                        |
| chaos                    | 109 ms                                                       | 58.8 ms: 1.85x faster                                                       |
| pyflate                  | 733 ms                                                       | 402 ms: 1.82x faster                                                        |
| logging_silent           | 167 ns                                                       | 93.8 ns: 1.78x faster                                                       |
| pylint                   | 566 ms                                                       | 319 ms: 1.77x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 60.6 ms: 1.77x faster                                                       |
| scimark_lu               | 167 ms                                                       | 95.0 ms: 1.76x faster                                                       |
| richards_super           | 90.6 ms                                                      | 51.7 ms: 1.75x faster                                                       |
| raytrace                 | 489 ms                                                       | 279 ms: 1.75x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 28.5 us: 1.75x faster                                                       |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.73x faster                                                        |
| deepcopy                 | 468 us                                                       | 273 us: 1.72x faster                                                        |
| richards                 | 75.1 ms                                                      | 45.4 ms: 1.65x faster                                                       |
| comprehensions           | 26.7 us                                                      | 16.3 us: 1.64x faster                                                       |
| spectral_norm            | 139 ms                                                       | 86.3 ms: 1.61x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 5.93 ms: 1.59x faster                                                       |
| float                    | 111 ms                                                       | 70.6 ms: 1.57x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 77.9 ms: 1.53x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 206 us: 1.51x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.01 us: 1.48x faster                                                       |
| nbody                    | 134 ms                                                       | 92.3 ms: 1.45x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.64 us: 1.45x faster                                                       |
| regex_compile            | 190 ms                                                       | 133 ms: 1.43x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                      |
| django_template          | 50.2 ms                                                      | 35.3 ms: 1.42x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 67.3 ms: 1.41x faster                                                       |
| thrift                   | 1.18 ms                                                      | 846 us: 1.39x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.9 ms: 1.38x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 330 us: 1.38x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 22.8 ms: 1.38x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.94 us: 1.36x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.58 sec: 1.36x faster                                                      |
| mako                     | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 59.6 ms: 1.36x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 779 ms: 1.35x faster                                                        |
| fannkuch                 | 483 ms                                                       | 363 ms: 1.33x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 11.1 ms: 1.30x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 58.2 ms: 1.30x faster                                                       |
| sympy_sum                | 193 ms                                                       | 149 ms: 1.29x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 21.9 ms: 1.29x faster                                                       |
| sympy_str                | 360 ms                                                       | 284 ms: 1.27x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.9 ms: 1.27x faster                                                       |
| nqueens                  | 115 ms                                                       | 90.8 ms: 1.27x faster                                                       |
| 2to3                     | 350 ms                                                       | 280 ms: 1.25x faster                                                        |
| sympy_expand             | 600 ms                                                       | 483 ms: 1.24x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 52.1 ms: 1.21x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.83 sec: 1.21x faster                                                      |
| json_loads               | 30.3 us                                                      | 25.5 us: 1.19x faster                                                       |
| regex_dna                | 261 ms                                                       | 221 ms: 1.18x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 23.1 ms: 1.18x faster                                                       |
| scimark_fft              | 361 ms                                                       | 307 ms: 1.18x faster                                                        |
| meteor_contest           | 138 ms                                                       | 119 ms: 1.16x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 140 ms: 1.14x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 97.4 ms: 1.13x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 83.4 ms: 1.11x faster                                                       |
| json                     | 5.86 ms                                                      | 5.37 ms: 1.09x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.77 ms: 1.06x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.84 us: 1.05x faster                                                       |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                                        |
| async_generators         | 421 ms                                                       | 427 ms: 1.01x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.64 ms: 1.06x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.49 ms: 1.13x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.80 ms: 1.20x slower                                                       |
| coverage                 | 63.3 ms                                                      | 82.8 ms: 1.31x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.83 ms: 1.60x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.47 ms: 1.89x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.38x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250626-3.15.0a0-a4625d5/bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.380x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.37x
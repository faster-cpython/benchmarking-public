# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.304x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 315 ms: 1.11x faster                                                     |
| docutils       | 3.41 sec                                                     | 3.17 sec: 1.08x faster                                                   |
| html5lib       | 94.6 ms                                                      | 73.1 ms: 1.29x faster                                                    |
| tornado_http   | 157 ms                                                       | 123 ms: 1.28x faster                                                     |
| Geometric mean | (ref)                                                        | 1.19x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 329 ms: 2.10x faster                                                     |
| async_tree_memoization  | 819 ms                                                       | 407 ms: 2.01x faster                                                     |
| async_tree_io           | 1.60 sec                                                     | 805 ms: 1.99x faster                                                     |
| async_tree_cpu_io_mixed | 936 ms                                                       | 580 ms: 1.61x faster                                                     |
| Geometric mean          | (ref)                                                        | 1.92x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 83.3 ms: 1.61x faster                                                    |
| float          | 111 ms                                                       | 75.3 ms: 1.48x faster                                                    |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                        | 1.37x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 150 ms: 1.26x faster                                                     |
| regex_dna      | 261 ms                                                       | 236 ms: 1.11x faster                                                     |
| regex_v8       | 27.2 ms                                                      | 24.8 ms: 1.09x faster                                                    |
| regex_effbot   | 3.09 ms                                                      | 3.60 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                        | 1.07x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 219 us: 1.42x faster                                                     |
| pickle_pure_python   | 455 us                                                       | 325 us: 1.40x faster                                                     |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.35x faster                                                    |
| xml_etree_process    | 75.9 ms                                                      | 56.4 ms: 1.35x faster                                                    |
| tomli_loads          | 2.92 sec                                                     | 2.20 sec: 1.33x faster                                                   |
| json_loads           | 30.3 us                                                      | 23.8 us: 1.28x faster                                                    |
| xml_etree_generate   | 92.3 ms                                                      | 78.8 ms: 1.17x faster                                                    |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                     |
| xml_etree_iterparse  | 110 ms                                                       | 99.8 ms: 1.11x faster                                                    |
| pickle_dict          | 29.5 us                                                      | 29.8 us: 1.01x slower                                                    |
| unpickle_list        | 4.65 us                                                      | 4.71 us: 1.01x slower                                                    |
| pickle               | 9.89 us                                                      | 10.3 us: 1.04x slower                                                    |
| pickle_list          | 4.12 us                                                      | 4.30 us: 1.04x slower                                                    |
| unpickle             | 13.5 us                                                      | 14.8 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                    |
| python_startup_no_site | 7.33 ms                                                      | 8.97 ms: 1.22x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.15 ms: 1.61x faster                                                    |
| django_template | 50.2 ms                                                      | 46.0 ms: 1.09x faster                                                    |
| genshi_text     | 31.4 ms                                                      | 29.8 ms: 1.05x faster                                                    |
| genshi_xml      | 63.3 ms                                                      | 66.2 ms: 1.05x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.15x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 176 us: 3.05x faster                                                     |
| deltablue                | 7.50 ms                                                      | 3.23 ms: 2.32x faster                                                    |
| async_tree_none          | 692 ms                                                       | 329 ms: 2.10x faster                                                     |
| asyncio_tcp              | 779 ms                                                       | 371 ms: 2.10x faster                                                     |
| async_tree_memoization   | 819 ms                                                       | 407 ms: 2.01x faster                                                     |
| async_tree_io            | 1.60 sec                                                     | 805 ms: 1.99x faster                                                     |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                   |
| deepcopy_memo            | 49.8 us                                                      | 27.3 us: 1.82x faster                                                    |
| scimark_lu               | 167 ms                                                       | 96.0 ms: 1.74x faster                                                    |
| scimark_sor              | 180 ms                                                       | 105 ms: 1.71x faster                                                     |
| logging_silent           | 167 ns                                                       | 98.1 ns: 1.71x faster                                                    |
| crypto_pyaes             | 119 ms                                                       | 70.0 ms: 1.70x faster                                                    |
| spectral_norm            | 139 ms                                                       | 82.8 ms: 1.68x faster                                                    |
| go                       | 262 ms                                                       | 158 ms: 1.65x faster                                                     |
| richards_super           | 90.6 ms                                                      | 55.4 ms: 1.64x faster                                                    |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 580 ms: 1.61x faster                                                     |
| nbody                    | 134 ms                                                       | 83.3 ms: 1.61x faster                                                    |
| pyflate                  | 733 ms                                                       | 456 ms: 1.61x faster                                                     |
| mako                     | 14.7 ms                                                      | 9.15 ms: 1.61x faster                                                    |
| chaos                    | 109 ms                                                       | 68.0 ms: 1.60x faster                                                    |
| richards                 | 75.1 ms                                                      | 47.3 ms: 1.59x faster                                                    |
| scimark_monte_carlo      | 107 ms                                                       | 68.8 ms: 1.56x faster                                                    |
| deepcopy                 | 468 us                                                       | 300 us: 1.56x faster                                                     |
| generators               | 57.3 ms                                                      | 37.3 ms: 1.54x faster                                                    |
| raytrace                 | 489 ms                                                       | 323 ms: 1.52x faster                                                     |
| sqlglot_parse            | 2.24 ms                                                      | 1.51 ms: 1.48x faster                                                    |
| float                    | 111 ms                                                       | 75.3 ms: 1.48x faster                                                    |
| comprehensions           | 26.7 us                                                      | 18.7 us: 1.43x faster                                                    |
| unpickle_pure_python     | 312 us                                                       | 219 us: 1.42x faster                                                     |
| pickle_pure_python       | 455 us                                                       | 325 us: 1.40x faster                                                     |
| fannkuch                 | 483 ms                                                       | 346 ms: 1.40x faster                                                     |
| pylint                   | 566 ms                                                       | 407 ms: 1.39x faster                                                     |
| sqlglot_transpile        | 2.68 ms                                                      | 1.94 ms: 1.38x faster                                                    |
| pprint_safe_repr         | 1.05 sec                                                     | 762 ms: 1.38x faster                                                     |
| coroutines               | 30.3 ms                                                      | 22.1 ms: 1.37x faster                                                    |
| deepcopy_reduce          | 4.01 us                                                      | 2.95 us: 1.36x faster                                                    |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.35x faster                                                    |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.35x faster                                                    |
| xml_etree_process        | 75.9 ms                                                      | 56.4 ms: 1.35x faster                                                    |
| pprint_pformat           | 2.15 sec                                                     | 1.60 sec: 1.35x faster                                                   |
| logging_simple           | 8.88 us                                                      | 6.63 us: 1.34x faster                                                    |
| hexiom                   | 9.42 ms                                                      | 7.09 ms: 1.33x faster                                                    |
| tomli_loads              | 2.92 sec                                                     | 2.20 sec: 1.33x faster                                                   |
| logging_format           | 9.64 us                                                      | 7.28 us: 1.32x faster                                                    |
| html5lib                 | 94.6 ms                                                      | 73.1 ms: 1.29x faster                                                    |
| scimark_fft              | 361 ms                                                       | 280 ms: 1.29x faster                                                     |
| thrift                   | 1.18 ms                                                      | 913 us: 1.29x faster                                                     |
| tornado_http             | 157 ms                                                       | 123 ms: 1.28x faster                                                     |
| json_loads               | 30.3 us                                                      | 23.8 us: 1.28x faster                                                    |
| pycparser                | 1.67 sec                                                     | 1.31 sec: 1.28x faster                                                   |
| regex_compile            | 190 ms                                                       | 150 ms: 1.26x faster                                                     |
| dulwich_log              | 81.1 ms                                                      | 64.8 ms: 1.25x faster                                                    |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.15 ms: 1.22x faster                                                    |
| bench_thread_pool        | 1.14 ms                                                      | 946 us: 1.21x faster                                                     |
| xml_etree_generate       | 92.3 ms                                                      | 78.8 ms: 1.17x faster                                                    |
| mdp                      | 3.01 sec                                                     | 2.60 sec: 1.16x faster                                                   |
| sympy_str                | 360 ms                                                       | 318 ms: 1.13x faster                                                     |
| json                     | 5.86 ms                                                      | 5.19 ms: 1.13x faster                                                    |
| nqueens                  | 115 ms                                                       | 102 ms: 1.13x faster                                                     |
| sympy_expand             | 600 ms                                                       | 534 ms: 1.12x faster                                                     |
| sympy_sum                | 193 ms                                                       | 172 ms: 1.12x faster                                                     |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                                     |
| 2to3                     | 350 ms                                                       | 315 ms: 1.11x faster                                                     |
| xml_etree_iterparse      | 110 ms                                                       | 99.8 ms: 1.11x faster                                                    |
| regex_dna                | 261 ms                                                       | 236 ms: 1.11x faster                                                     |
| async_generators         | 421 ms                                                       | 382 ms: 1.10x faster                                                     |
| sqlite_synth             | 2.99 us                                                      | 2.73 us: 1.10x faster                                                    |
| regex_v8                 | 27.2 ms                                                      | 24.8 ms: 1.09x faster                                                    |
| django_template          | 50.2 ms                                                      | 46.0 ms: 1.09x faster                                                    |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                     |
| docutils                 | 3.41 sec                                                     | 3.17 sec: 1.08x faster                                                   |
| sqlglot_normalize        | 144 ms                                                       | 136 ms: 1.06x faster                                                     |
| genshi_text              | 31.4 ms                                                      | 29.8 ms: 1.05x faster                                                    |
| sympy_integrate          | 28.2 ms                                                      | 27.0 ms: 1.04x faster                                                    |
| meteor_contest           | 138 ms                                                       | 134 ms: 1.03x faster                                                     |
| sqlglot_optimize         | 70.1 ms                                                      | 69.6 ms: 1.01x faster                                                    |
| pickle_dict              | 29.5 us                                                      | 29.8 us: 1.01x slower                                                    |
| unpickle_list            | 4.65 us                                                      | 4.71 us: 1.01x slower                                                    |
| pickle                   | 9.89 us                                                      | 10.3 us: 1.04x slower                                                    |
| pickle_list              | 4.12 us                                                      | 4.30 us: 1.04x slower                                                    |
| genshi_xml               | 63.3 ms                                                      | 66.2 ms: 1.05x slower                                                    |
| telco                    | 7.23 ms                                                      | 7.63 ms: 1.06x slower                                                    |
| create_gc_cycles         | 1.76 ms                                                      | 1.90 ms: 1.08x slower                                                    |
| unpickle                 | 13.5 us                                                      | 14.8 us: 1.10x slower                                                    |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                    |
| regex_effbot             | 3.09 ms                                                      | 3.60 ms: 1.16x slower                                                    |
| python_startup_no_site   | 7.33 ms                                                      | 8.97 ms: 1.22x slower                                                    |
| gc_traversal             | 3.42 ms                                                      | 4.31 ms: 1.26x slower                                                    |
| coverage                 | 63.3 ms                                                      | 82.6 ms: 1.31x slower                                                    |
| unpack_sequence          | 59.9 ns                                                      | 94.8 ns: 1.58x slower                                                    |
| bench_mp_pool            | 6.37 ms                                                      | 3.26 sec: 511.05x slower                                                 |
| Geometric mean           | (ref)                                                        | 1.20x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241007-3.14.0a0-0442576-JIT/bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.304x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.20x
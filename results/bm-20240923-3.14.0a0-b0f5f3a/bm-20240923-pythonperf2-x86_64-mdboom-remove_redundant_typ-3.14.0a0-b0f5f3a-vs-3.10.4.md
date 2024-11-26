# Results vs. 3.10.4

- fork: mdboom
- ref: remove_redundant_typ
- machine: linux-x86_64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.336x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.24x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| html5lib       | 94.6 ms                                                      | 71.8 ms: 1.32x faster                                                       |
| tornado_http   | 157 ms                                                       | 116 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 319 ms: 2.17x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 398 ms: 2.06x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 809 ms: 1.97x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 572 ms: 1.64x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.95x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 88.9 ms: 1.51x faster                                                       |
| float          | 111 ms                                                       | 78.7 ms: 1.41x faster                                                       |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.37x faster                                                        |
| regex_dna      | 261 ms                                                       | 235 ms: 1.11x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 315 us: 1.45x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 224 us: 1.39x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 59.1 ms: 1.28x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.13x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.59 sec: 1.12x faster                                                      |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 85.4 ms: 1.08x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 4.73 us: 1.02x slower                                                       |
| pickle               | 9.89 us                                                      | 10.7 us: 1.08x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 32.7 us: 1.11x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.0 us: 1.11x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.64 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 8.96 ms: 1.22x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 24.1 ms: 1.30x faster                                                       |
| django_template | 50.2 ms                                                      | 40.3 ms: 1.25x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 53.6 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 172 us: 3.13x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.38 ms: 2.22x faster                                                       |
| async_tree_none          | 692 ms                                                       | 319 ms: 2.17x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 374 ms: 2.08x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 398 ms: 2.06x faster                                                        |
| generators               | 57.3 ms                                                      | 28.9 ms: 1.98x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 809 ms: 1.97x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.57 sec: 1.97x faster                                                      |
| go                       | 262 ms                                                       | 136 ms: 1.92x faster                                                        |
| raytrace                 | 489 ms                                                       | 268 ms: 1.82x faster                                                        |
| scimark_lu               | 167 ms                                                       | 95.8 ms: 1.74x faster                                                       |
| chaos                    | 109 ms                                                       | 62.6 ms: 1.74x faster                                                       |
| logging_silent           | 167 ns                                                       | 100 ns: 1.67x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 30.0 us: 1.66x faster                                                       |
| deepcopy                 | 468 us                                                       | 284 us: 1.65x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 572 ms: 1.64x faster                                                        |
| pylint                   | 566 ms                                                       | 349 ms: 1.62x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 73.6 ms: 1.62x faster                                                       |
| richards_super           | 90.6 ms                                                      | 56.0 ms: 1.62x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 67.2 ms: 1.60x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.57x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.2 us: 1.55x faster                                                       |
| scimark_sor              | 180 ms                                                       | 117 ms: 1.54x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.19 ms: 1.52x faster                                                       |
| nbody                    | 134 ms                                                       | 88.9 ms: 1.51x faster                                                       |
| pyflate                  | 733 ms                                                       | 489 ms: 1.50x faster                                                        |
| richards                 | 75.1 ms                                                      | 50.2 ms: 1.49x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.81 ms: 1.48x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 315 us: 1.45x faster                                                        |
| spectral_norm            | 139 ms                                                       | 96.4 ms: 1.44x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                       |
| float                    | 111 ms                                                       | 78.7 ms: 1.41x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.86 us: 1.40x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.37 us: 1.39x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 224 us: 1.39x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.93 us: 1.39x faster                                                       |
| regex_compile            | 190 ms                                                       | 138 ms: 1.37x faster                                                        |
| coroutines               | 30.3 ms                                                      | 22.1 ms: 1.37x faster                                                       |
| tornado_http             | 157 ms                                                       | 116 ms: 1.36x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.35x faster                                                       |
| fannkuch                 | 483 ms                                                       | 359 ms: 1.35x faster                                                        |
| thrift                   | 1.18 ms                                                      | 874 us: 1.35x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                      |
| bench_mp_pool            | 6.37 ms                                                      | 4.80 ms: 1.33x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 71.8 ms: 1.32x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 867 us: 1.32x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 802 ms: 1.31x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 24.1 ms: 1.30x faster                                                       |
| nqueens                  | 115 ms                                                       | 88.3 ms: 1.30x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                                      |
| xml_etree_process        | 75.9 ms                                                      | 59.1 ms: 1.28x faster                                                       |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                        |
| django_template          | 50.2 ms                                                      | 40.3 ms: 1.25x faster                                                       |
| sympy_str                | 360 ms                                                       | 289 ms: 1.25x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 48.1 ns: 1.24x faster                                                       |
| 2to3                     | 350 ms                                                       | 283 ms: 1.24x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.9 ms: 1.23x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.23x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 66.1 ms: 1.23x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 57.9 ms: 1.21x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| sympy_expand             | 600 ms                                                       | 499 ms: 1.20x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.50 sec: 1.20x faster                                                      |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.26 ms: 1.19x faster                                                       |
| scimark_fft              | 361 ms                                                       | 304 ms: 1.19x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 53.6 ms: 1.18x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| async_generators         | 421 ms                                                       | 358 ms: 1.17x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 141 ms: 1.13x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.59 sec: 1.12x faster                                                      |
| regex_dna                | 261 ms                                                       | 235 ms: 1.11x faster                                                        |
| json                     | 5.86 ms                                                      | 5.29 ms: 1.11x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                        |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.76 us: 1.08x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 85.4 ms: 1.08x faster                                                       |
| pidigits                 | 271 ms                                                       | 252 ms: 1.08x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                       |
| unpickle_list            | 4.65 us                                                      | 4.73 us: 1.02x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.7 us: 1.08x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.91 ms: 1.08x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 32.7 us: 1.11x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.0 us: 1.11x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.11 ms: 1.12x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.64 us: 1.13x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.96 ms: 1.22x slower                                                       |
| coverage                 | 63.3 ms                                                      | 80.2 ms: 1.27x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.87 ms: 1.42x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.32x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.336x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.13x
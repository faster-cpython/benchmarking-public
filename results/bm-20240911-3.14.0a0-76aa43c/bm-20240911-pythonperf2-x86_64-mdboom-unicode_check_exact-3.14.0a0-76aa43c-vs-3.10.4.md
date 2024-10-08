# Results vs. 3.10.4

- fork: mdboom
- ref: unicode_check_exact
- machine: linux-x86_64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.25x faster                                                       |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                     |
| html5lib       | 94.6 ms                                                      | 72.7 ms: 1.30x faster                                                      |
| tornado_http   | 157 ms                                                       | 116 ms: 1.35x faster                                                       |
| Geometric mean | (ref)                                                        | 1.27x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 319 ms: 2.17x faster                                                       |
| async_tree_memoization  | 819 ms                                                       | 397 ms: 2.06x faster                                                       |
| async_tree_io           | 1.60 sec                                                     | 818 ms: 1.95x faster                                                       |
| async_tree_cpu_io_mixed | 936 ms                                                       | 572 ms: 1.64x faster                                                       |
| Geometric mean          | (ref)                                                        | 1.94x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 84.9 ms: 1.58x faster                                                      |
| float          | 111 ms                                                       | 80.7 ms: 1.38x faster                                                      |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                        | 1.33x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 141 ms: 1.35x faster                                                       |
| regex_dna      | 261 ms                                                       | 254 ms: 1.03x faster                                                       |
| regex_v8       | 27.2 ms                                                      | 26.7 ms: 1.02x faster                                                      |
| regex_effbot   | 3.09 ms                                                      | 3.66 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                        | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 315 us: 1.45x faster                                                       |
| unpickle_pure_python | 312 us                                                       | 216 us: 1.44x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 59.1 ms: 1.29x faster                                                      |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                      |
| tomli_loads          | 2.92 sec                                                     | 2.51 sec: 1.16x faster                                                     |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.10x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 84.4 ms: 1.09x faster                                                      |
| pickle_dict          | 29.5 us                                                      | 29.6 us: 1.00x slower                                                      |
| pickle_list          | 4.12 us                                                      | 4.18 us: 1.01x slower                                                      |
| unpickle_list        | 4.65 us                                                      | 4.76 us: 1.02x slower                                                      |
| pickle               | 9.89 us                                                      | 10.2 us: 1.03x slower                                                      |
| unpickle             | 13.5 us                                                      | 15.3 us: 1.14x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                      |
| python_startup_no_site | 7.33 ms                                                      | 8.95 ms: 1.22x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                      |
| genshi_text     | 31.4 ms                                                      | 24.1 ms: 1.31x faster                                                      |
| django_template | 50.2 ms                                                      | 38.6 ms: 1.30x faster                                                      |
| genshi_xml      | 63.3 ms                                                      | 53.0 ms: 1.19x faster                                                      |
| Geometric mean  | (ref)                                                        | 1.30x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 170 us: 3.15x faster                                                       |
| deltablue                | 7.50 ms                                                      | 3.44 ms: 2.18x faster                                                      |
| async_tree_none          | 692 ms                                                       | 319 ms: 2.17x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 367 ms: 2.12x faster                                                       |
| async_tree_memoization   | 819 ms                                                       | 397 ms: 2.06x faster                                                       |
| generators               | 57.3 ms                                                      | 29.1 ms: 1.97x faster                                                      |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.57 sec: 1.97x faster                                                     |
| async_tree_io            | 1.60 sec                                                     | 818 ms: 1.95x faster                                                       |
| go                       | 262 ms                                                       | 136 ms: 1.92x faster                                                       |
| raytrace                 | 489 ms                                                       | 269 ms: 1.82x faster                                                       |
| chaos                    | 109 ms                                                       | 61.2 ms: 1.77x faster                                                      |
| scimark_lu               | 167 ms                                                       | 95.2 ms: 1.75x faster                                                      |
| logging_silent           | 167 ns                                                       | 98.7 ns: 1.70x faster                                                      |
| deepcopy_memo            | 49.8 us                                                      | 29.7 us: 1.67x faster                                                      |
| deepcopy                 | 468 us                                                       | 280 us: 1.67x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 71.8 ms: 1.66x faster                                                      |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 572 ms: 1.64x faster                                                       |
| pylint                   | 566 ms                                                       | 348 ms: 1.63x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 66.2 ms: 1.62x faster                                                      |
| richards_super           | 90.6 ms                                                      | 56.1 ms: 1.62x faster                                                      |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.58x faster                                                      |
| nbody                    | 134 ms                                                       | 84.9 ms: 1.58x faster                                                      |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.54x faster                                                      |
| scimark_sor              | 180 ms                                                       | 118 ms: 1.53x faster                                                       |
| richards                 | 75.1 ms                                                      | 49.6 ms: 1.51x faster                                                      |
| hexiom                   | 9.42 ms                                                      | 6.29 ms: 1.50x faster                                                      |
| sqlglot_transpile        | 2.68 ms                                                      | 1.80 ms: 1.49x faster                                                      |
| pyflate                  | 733 ms                                                       | 497 ms: 1.47x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 315 us: 1.45x faster                                                       |
| spectral_norm            | 139 ms                                                       | 96.4 ms: 1.44x faster                                                      |
| unpickle_pure_python     | 312 us                                                       | 216 us: 1.44x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.21 us: 1.43x faster                                                      |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                      |
| logging_format           | 9.64 us                                                      | 6.82 us: 1.41x faster                                                      |
| coroutines               | 30.3 ms                                                      | 21.5 ms: 1.41x faster                                                      |
| deepcopy_reduce          | 4.01 us                                                      | 2.86 us: 1.40x faster                                                      |
| thrift                   | 1.18 ms                                                      | 853 us: 1.38x faster                                                       |
| float                    | 111 ms                                                       | 80.7 ms: 1.38x faster                                                      |
| pathlib                  | 21.4 ms                                                      | 15.6 ms: 1.37x faster                                                      |
| bench_mp_pool            | 6.37 ms                                                      | 4.66 ms: 1.37x faster                                                      |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.37x faster                                                     |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                      |
| fannkuch                 | 483 ms                                                       | 356 ms: 1.35x faster                                                       |
| tornado_http             | 157 ms                                                       | 116 ms: 1.35x faster                                                       |
| regex_compile            | 190 ms                                                       | 141 ms: 1.35x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 874 us: 1.31x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.31x faster                                                     |
| genshi_text              | 31.4 ms                                                      | 24.1 ms: 1.31x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 804 ms: 1.30x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 72.7 ms: 1.30x faster                                                      |
| django_template          | 50.2 ms                                                      | 38.6 ms: 1.30x faster                                                      |
| nqueens                  | 115 ms                                                       | 88.6 ms: 1.30x faster                                                      |
| xml_etree_process        | 75.9 ms                                                      | 59.1 ms: 1.29x faster                                                      |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                       |
| 2to3                     | 350 ms                                                       | 281 ms: 1.25x faster                                                       |
| sympy_str                | 360 ms                                                       | 292 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.12 ms: 1.23x faster                                                      |
| scimark_fft              | 361 ms                                                       | 295 ms: 1.22x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 23.0 ms: 1.22x faster                                                      |
| dulwich_log              | 81.1 ms                                                      | 66.6 ms: 1.22x faster                                                      |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                      |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.50 sec: 1.20x faster                                                     |
| sqlglot_optimize         | 70.1 ms                                                      | 58.4 ms: 1.20x faster                                                      |
| sympy_expand             | 600 ms                                                       | 500 ms: 1.20x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 53.0 ms: 1.19x faster                                                      |
| async_generators         | 421 ms                                                       | 354 ms: 1.19x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                     |
| tomli_loads              | 2.92 sec                                                     | 2.51 sec: 1.16x faster                                                     |
| unpack_sequence          | 59.9 ns                                                      | 51.6 ns: 1.16x faster                                                      |
| json                     | 5.86 ms                                                      | 5.25 ms: 1.12x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.10x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.10x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 84.4 ms: 1.09x faster                                                      |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.74 us: 1.09x faster                                                      |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                       |
| regex_dna                | 261 ms                                                       | 254 ms: 1.03x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 26.7 ms: 1.02x faster                                                      |
| pickle_dict              | 29.5 us                                                      | 29.6 us: 1.00x slower                                                      |
| pickle_list              | 4.12 us                                                      | 4.18 us: 1.01x slower                                                      |
| unpickle_list            | 4.65 us                                                      | 4.76 us: 1.02x slower                                                      |
| pickle                   | 9.89 us                                                      | 10.2 us: 1.03x slower                                                      |
| create_gc_cycles         | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                      |
| unpickle                 | 13.5 us                                                      | 15.3 us: 1.14x slower                                                      |
| telco                    | 7.23 ms                                                      | 8.24 ms: 1.14x slower                                                      |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                      |
| regex_effbot             | 3.09 ms                                                      | 3.66 ms: 1.19x slower                                                      |
| python_startup_no_site   | 7.33 ms                                                      | 8.95 ms: 1.22x slower                                                      |
| coverage                 | 63.3 ms                                                      | 85.2 ms: 1.35x slower                                                      |
| gc_traversal             | 3.42 ms                                                      | 4.89 ms: 1.43x slower                                                      |
| Geometric mean           | (ref)                                                        | 1.33x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.12x
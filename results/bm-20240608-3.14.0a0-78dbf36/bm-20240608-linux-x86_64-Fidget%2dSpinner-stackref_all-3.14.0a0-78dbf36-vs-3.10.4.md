# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: 78dbf36
- commit date: 2024-06-08
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 268 ms: 1.30x faster                                                    |
| docutils       | 3.30 sec                                               | 2.77 sec: 1.19x faster                                                  |
| html5lib       | 88.9 ms                                                | 67.3 ms: 1.32x faster                                                   |
| tornado_http   | 136 ms                                                 | 93.8 ms: 1.45x faster                                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 374 ms: 1.94x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 468 ms: 1.86x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 954 ms: 1.85x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 631 ms: 1.61x faster                                                    |
| Geometric mean          | (ref)                                                  | 1.81x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.3 ms: 1.78x faster                                                   |
| float          | 117 ms                                                 | 77.9 ms: 1.50x faster                                                   |
| pidigits       | 191 ms                                                 | 190 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                  | 1.39x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.42x faster                                                    |
| regex_v8       | 27.8 ms                                                | 26.0 ms: 1.07x faster                                                   |
| regex_dna      | 227 ms                                                 | 233 ms: 1.03x slower                                                    |
| regex_effbot   | 3.63 ms                                                | 3.80 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 299 us: 1.62x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                    |
| tomli_loads          | 3.14 sec                                               | 2.15 sec: 1.46x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 85.6 ms: 1.16x faster                                                   |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.07x faster                                                    |
| unpickle_list        | 5.20 us                                                | 5.31 us: 1.02x slower                                                   |
| pickle_list          | 5.08 us                                                | 5.18 us: 1.02x slower                                                   |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                                   |
| pickle               | 10.7 us                                                | 11.8 us: 1.10x slower                                                   |
| pickle_dict          | 29.6 us                                                | 35.2 us: 1.19x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                   |
| django_template | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                   |
| genshi_text     | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                    |
| generators               | 80.1 ms                                                | 29.0 ms: 2.76x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.40x faster                                                   |
| chaos                    | 115 ms                                                 | 59.3 ms: 1.95x faster                                                   |
| async_tree_none          | 728 ms                                                 | 374 ms: 1.94x faster                                                    |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 468 ms: 1.86x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 954 ms: 1.85x faster                                                    |
| asyncio_tcp              | 922 ms                                                 | 501 ms: 1.84x faster                                                    |
| logging_silent           | 190 ns                                                 | 105 ns: 1.80x faster                                                    |
| nbody                    | 154 ms                                                 | 86.3 ms: 1.78x faster                                                   |
| pylint                   | 551 ms                                                 | 314 ms: 1.76x faster                                                    |
| richards_super           | 94.7 ms                                                | 54.0 ms: 1.76x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 67.7 ms: 1.74x faster                                                   |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 75.2 ms: 1.70x faster                                                   |
| go                       | 240 ms                                                 | 142 ms: 1.70x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.19 ms: 1.68x faster                                                   |
| richards                 | 79.3 ms                                                | 47.4 ms: 1.67x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 299 us: 1.62x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 631 ms: 1.61x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                    |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                   |
| pyflate                  | 716 ms                                                 | 473 ms: 1.51x faster                                                    |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                    |
| float                    | 117 ms                                                 | 77.9 ms: 1.50x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 39.3 us: 1.49x faster                                                   |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                                   |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 2.15 sec: 1.46x faster                                                  |
| logging_format           | 9.09 us                                                | 6.24 us: 1.46x faster                                                   |
| tornado_http             | 136 ms                                                 | 93.8 ms: 1.45x faster                                                   |
| regex_compile            | 188 ms                                                 | 132 ms: 1.42x faster                                                    |
| django_template          | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.83 sec: 1.40x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.38x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                   |
| genshi_text              | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 744 ms: 1.37x faster                                                    |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                   |
| nqueens                  | 106 ms                                                 | 79.3 ms: 1.34x faster                                                   |
| fannkuch                 | 532 ms                                                 | 398 ms: 1.33x faster                                                    |
| thrift                   | 1.07 ms                                                | 806 us: 1.33x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                   |
| deepcopy                 | 479 us                                                 | 362 us: 1.32x faster                                                    |
| html5lib                 | 88.9 ms                                                | 67.3 ms: 1.32x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.32x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.92 ms: 1.31x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                    |
| 2to3                     | 348 ms                                                 | 268 ms: 1.30x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 65.1 ms: 1.30x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 3.24 us: 1.29x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                   |
| sympy_sum                | 196 ms                                                 | 154 ms: 1.27x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 20.3 ms: 1.27x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 54.8 ms: 1.26x faster                                                   |
| sympy_str                | 346 ms                                                 | 277 ms: 1.25x faster                                                    |
| scimark_fft              | 466 ms                                                 | 376 ms: 1.24x faster                                                    |
| sympy_expand             | 566 ms                                                 | 471 ms: 1.20x faster                                                    |
| dask                     | 441 ms                                                 | 369 ms: 1.19x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.77 sec: 1.19x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 833 us: 1.18x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 85.6 ms: 1.16x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                  |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                    |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.07x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 26.0 ms: 1.07x faster                                                   |
| json                     | 5.69 ms                                                | 5.36 ms: 1.06x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.93 us: 1.03x faster                                                   |
| bench_mp_pool            | 24.0 ms                                                | 23.8 ms: 1.01x faster                                                   |
| async_generators         | 444 ms                                                 | 441 ms: 1.01x faster                                                    |
| pidigits                 | 191 ms                                                 | 190 ms: 1.00x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                                    |
| unpickle_list            | 5.20 us                                                | 5.31 us: 1.02x slower                                                   |
| pickle_list              | 5.08 us                                                | 5.18 us: 1.02x slower                                                   |
| regex_dna                | 227 ms                                                 | 233 ms: 1.03x slower                                                    |
| regex_effbot             | 3.63 ms                                                | 3.80 ms: 1.05x slower                                                   |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 3.98 ms: 1.10x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                   |
| pickle                   | 10.7 us                                                | 11.8 us: 1.10x slower                                                   |
| telco                    | 7.27 ms                                                | 8.35 ms: 1.15x slower                                                   |
| coverage                 | 79.4 ms                                                | 92.1 ms: 1.16x slower                                                   |
| pickle_dict              | 29.6 us                                                | 35.2 us: 1.19x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                            |
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240608-3.14.0a0-78dbf36/bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.11x
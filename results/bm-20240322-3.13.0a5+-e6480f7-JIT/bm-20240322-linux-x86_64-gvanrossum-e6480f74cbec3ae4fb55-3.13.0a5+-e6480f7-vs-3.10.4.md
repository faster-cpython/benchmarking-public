# Results vs. 3.10.4

- fork: gvanrossum
- ref: e6480f74cbec3ae4fb55
- machine: linux-x86_64
- commit hash: e6480f7
- commit date: 2024-03-22
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.24x faster                                                       |
| chameleon      | 9.68 ms                                                | 7.11 ms: 1.36x faster                                                      |
| docutils       | 3.30 sec                                               | 2.80 sec: 1.18x faster                                                     |
| html5lib       | 88.9 ms                                                | 68.4 ms: 1.30x faster                                                      |
| tornado_http   | 136 ms                                                 | 99.3 ms: 1.37x faster                                                      |
| Geometric mean | (ref)                                                  | 1.29x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 453 ms: 1.61x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 581 ms: 1.50x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 1.23 sec: 1.44x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 728 ms: 1.40x faster                                                       |
| Geometric mean          | (ref)                                                  | 1.48x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 92.9 ms: 1.65x faster                                                      |
| float          | 117 ms                                                 | 80.6 ms: 1.45x faster                                                      |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.34x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.31x faster                                                       |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                      |
| regex_dna      | 227 ms                                                 | 233 ms: 1.03x slower                                                       |
| regex_effbot   | 3.63 ms                                                | 3.85 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 304 us: 1.59x faster                                                       |
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 239 us: 1.38x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 87.4 ms: 1.14x faster                                                      |
| json_loads           | 31.2 us                                                | 28.0 us: 1.11x faster                                                      |
| unpickle_list        | 5.20 us                                                | 4.85 us: 1.07x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 109 ms: 1.06x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 160 ms: 1.05x faster                                                       |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                                      |
| pickle_list          | 5.08 us                                                | 5.36 us: 1.06x slower                                                      |
| pickle               | 10.7 us                                                | 11.9 us: 1.11x slower                                                      |
| pickle_dict          | 29.6 us                                                | 35.6 us: 1.20x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.5 ms: 1.27x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 10.1 ms: 1.70x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                      |
| django_template | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                      |
| genshi_text     | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 54.8 ms: 1.20x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 112 us: 4.84x faster                                                       |
| generators               | 80.1 ms                                                | 29.5 ms: 2.71x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.49 ms: 2.27x faster                                                      |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                       |
| asyncio_tcp              | 922 ms                                                 | 509 ms: 1.81x faster                                                       |
| chaos                    | 115 ms                                                 | 63.9 ms: 1.81x faster                                                      |
| richards_super           | 94.7 ms                                                | 52.7 ms: 1.80x faster                                                      |
| richards                 | 79.3 ms                                                | 45.9 ms: 1.73x faster                                                      |
| raytrace                 | 507 ms                                                 | 294 ms: 1.72x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 75.3 ms: 1.70x faster                                                      |
| pylint                   | 551 ms                                                 | 327 ms: 1.69x faster                                                       |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.68x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 70.6 ms: 1.67x faster                                                      |
| nbody                    | 154 ms                                                 | 92.9 ms: 1.65x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                      |
| async_tree_none          | 728 ms                                                 | 453 ms: 1.61x faster                                                       |
| comprehensions           | 28.8 us                                                | 17.9 us: 1.60x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.59x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.66 ms: 1.55x faster                                                      |
| go                       | 240 ms                                                 | 155 ms: 1.55x faster                                                       |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 581 ms: 1.50x faster                                                       |
| hexiom                   | 10.4 ms                                                | 7.02 ms: 1.48x faster                                                      |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 39.8 us: 1.47x faster                                                      |
| pyflate                  | 716 ms                                                 | 489 ms: 1.47x faster                                                       |
| spectral_norm            | 170 ms                                                 | 116 ms: 1.46x faster                                                       |
| float                    | 117 ms                                                 | 80.6 ms: 1.45x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 1.23 sec: 1.44x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.86 us: 1.42x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 728 ms: 1.40x faster                                                       |
| logging_format           | 9.09 us                                                | 6.53 us: 1.39x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 239 us: 1.38x faster                                                       |
| tornado_http             | 136 ms                                                 | 99.3 ms: 1.37x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 743 ms: 1.37x faster                                                       |
| scimark_fft              | 466 ms                                                 | 341 ms: 1.37x faster                                                       |
| chameleon                | 9.68 ms                                                | 7.11 ms: 1.36x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.78 ms: 1.35x faster                                                      |
| deepcopy                 | 479 us                                                 | 355 us: 1.35x faster                                                       |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                      |
| scimark_lu               | 176 ms                                                 | 131 ms: 1.34x faster                                                       |
| fannkuch                 | 532 ms                                                 | 399 ms: 1.33x faster                                                       |
| django_template          | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                      |
| thrift                   | 1.07 ms                                                | 808 us: 1.33x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 3.15 us: 1.32x faster                                                      |
| regex_compile            | 188 ms                                                 | 143 ms: 1.31x faster                                                       |
| html5lib                 | 88.9 ms                                                | 68.4 ms: 1.30x faster                                                      |
| genshi_text              | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.23 sec: 1.28x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                                       |
| python_startup           | 14.6 ms                                                | 11.5 ms: 1.27x faster                                                      |
| 2to3                     | 348 ms                                                 | 280 ms: 1.24x faster                                                       |
| djangocms                | 38.4 us                                                | 31.5 us: 1.22x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 69.8 ms: 1.21x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 54.8 ms: 1.20x faster                                                      |
| sympy_str                | 346 ms                                                 | 288 ms: 1.20x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 57.7 ms: 1.20x faster                                                      |
| sympy_sum                | 196 ms                                                 | 164 ms: 1.20x faster                                                       |
| aiohttp                  | 1.44 ms                                                | 1.21 ms: 1.19x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 21.7 ms: 1.19x faster                                                      |
| nqueens                  | 106 ms                                                 | 89.8 ms: 1.18x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.80 sec: 1.18x faster                                                     |
| dask                     | 441 ms                                                 | 375 ms: 1.18x faster                                                       |
| gunicorn                 | 1.53 ms                                                | 1.31 ms: 1.17x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 850 us: 1.16x faster                                                       |
| sympy_expand             | 566 ms                                                 | 490 ms: 1.15x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 87.4 ms: 1.14x faster                                                      |
| json_loads               | 31.2 us                                                | 28.0 us: 1.11x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                      |
| pathlib                  | 20.5 ms                                                | 18.7 ms: 1.09x faster                                                      |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.64 sec: 1.08x faster                                                     |
| unpickle_list            | 5.20 us                                                | 4.85 us: 1.07x faster                                                      |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 109 ms: 1.06x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.53 ms: 1.06x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 160 ms: 1.05x faster                                                       |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 563 ms: 1.01x slower                                                       |
| regex_dna                | 227 ms                                                 | 233 ms: 1.03x slower                                                       |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                                      |
| pickle_list              | 5.08 us                                                | 5.36 us: 1.06x slower                                                      |
| regex_effbot             | 3.63 ms                                                | 3.85 ms: 1.06x slower                                                      |
| async_generators         | 444 ms                                                 | 475 ms: 1.07x slower                                                       |
| gc_traversal             | 3.62 ms                                                | 3.93 ms: 1.08x slower                                                      |
| pickle                   | 10.7 us                                                | 11.9 us: 1.11x slower                                                      |
| telco                    | 7.27 ms                                                | 8.57 ms: 1.18x slower                                                      |
| pickle_dict              | 29.6 us                                                | 35.6 us: 1.20x slower                                                      |
| coverage                 | 79.4 ms                                                | 98.2 ms: 1.24x slower                                                      |
| unpack_sequence          | 60.0 ns                                                | 89.0 ns: 1.48x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 10.1 ms: 1.70x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                               |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240322-3.13.0a5+-e6480f7-JIT/bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.20x


# Memory

- memory change: 1.22x
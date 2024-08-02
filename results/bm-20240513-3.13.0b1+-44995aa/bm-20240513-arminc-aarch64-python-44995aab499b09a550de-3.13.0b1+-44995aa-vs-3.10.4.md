# Results vs. 3.10.4

- fork: python
- ref: 44995aab499b09a550de
- machine: linux-aarch64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 302 ms: 1.26x faster                                                     |
| chameleon      | 10.8 ms                                                               | 9.02 ms: 1.20x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.13 sec: 1.13x faster                                                   |
| html5lib       | 86.5 ms                                                               | 68.4 ms: 1.26x faster                                                    |
| tornado_http   | 178 ms                                                                | 131 ms: 1.36x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 491 ms: 1.93x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.22 sec: 1.87x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 643 ms: 1.76x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 791 ms: 1.61x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.79x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 90.5 ms: 1.49x faster                                                    |
| nbody          | 166 ms                                                                | 112 ms: 1.48x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.37x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 31.2 ms: 1.03x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.94 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 361 us: 1.46x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 251 us: 1.46x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.54 sec: 1.33x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 81.0 ms: 1.23x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 191 ms: 1.11x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.46 us: 1.08x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                                     |
| pickle_list          | 5.24 us                                                               | 5.12 us: 1.02x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.6 us: 1.06x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 37.5 us: 1.07x slower                                                    |
| pickle               | 12.5 us                                                               | 13.6 us: 1.09x slower                                                    |
| unpickle             | 17.5 us                                                               | 19.7 us: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.6 ms: 1.12x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 8.47 ms: 1.23x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                    |
| django_template | 53.3 ms                                                               | 41.3 ms: 1.29x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.9 ms: 1.26x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 61.0 ms: 1.14x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 197 us: 3.35x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.88 ms: 2.31x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.16 ms: 2.03x faster                                                    |
| async_tree_none          | 950 ms                                                                | 491 ms: 1.93x faster                                                     |
| raytrace                 | 573 ms                                                                | 297 ms: 1.93x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.22 sec: 1.87x faster                                                   |
| generators               | 68.1 ms                                                               | 37.6 ms: 1.81x faster                                                    |
| chaos                    | 121 ms                                                                | 67.9 ms: 1.78x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 643 ms: 1.76x faster                                                     |
| richards_super           | 107 ms                                                                | 62.4 ms: 1.72x faster                                                    |
| logging_silent           | 222 ns                                                                | 133 ns: 1.67x faster                                                     |
| richards                 | 91.7 ms                                                               | 54.9 ms: 1.67x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 568 ms: 1.66x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.45 ms: 1.66x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.72 ms: 1.65x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 81.2 ms: 1.65x faster                                                    |
| scimark_lu               | 227 ms                                                                | 138 ms: 1.65x faster                                                     |
| comprehensions           | 33.1 us                                                               | 20.2 us: 1.64x faster                                                    |
| go                       | 264 ms                                                                | 162 ms: 1.63x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 791 ms: 1.61x faster                                                     |
| scimark_sor              | 246 ms                                                                | 158 ms: 1.56x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 7.01 ms: 1.56x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 82.3 ms: 1.55x faster                                                    |
| float                    | 135 ms                                                                | 90.5 ms: 1.49x faster                                                    |
| nbody                    | 166 ms                                                                | 112 ms: 1.48x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.22 sec: 1.48x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 361 us: 1.46x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 251 us: 1.46x faster                                                     |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                    |
| pylint                   | 485 ms                                                                | 340 ms: 1.43x faster                                                     |
| pyflate                  | 795 ms                                                                | 557 ms: 1.43x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.38x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.12 us: 1.37x faster                                                    |
| regex_compile            | 177 ms                                                                | 128 ms: 1.37x faster                                                     |
| tornado_http             | 178 ms                                                                | 131 ms: 1.36x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.88 us: 1.35x faster                                                    |
| spectral_norm            | 186 ms                                                                | 140 ms: 1.33x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.54 sec: 1.33x faster                                                   |
| thrift                   | 1.26 ms                                                               | 967 us: 1.30x faster                                                     |
| django_template          | 53.3 ms                                                               | 41.3 ms: 1.29x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.0 ms: 1.28x faster                                                    |
| sympy_sum                | 184 ms                                                                | 145 ms: 1.27x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 21.0 ms: 1.26x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 68.4 ms: 1.26x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.9 ms: 1.26x faster                                                    |
| 2to3                     | 381 ms                                                                | 302 ms: 1.26x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.27 ms: 1.25x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 58.7 ms: 1.25x faster                                                    |
| mypy2                    | 936 ms                                                                | 762 ms: 1.23x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 81.0 ms: 1.23x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 50.4 us: 1.22x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 128 ms: 1.22x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 1.93 sec: 1.22x faster                                                   |
| sympy_str                | 329 ms                                                                | 270 ms: 1.22x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 62.6 ms: 1.20x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 953 ms: 1.20x faster                                                     |
| chameleon                | 10.8 ms                                                               | 9.02 ms: 1.20x faster                                                    |
| dask                     | 450 ms                                                                | 377 ms: 1.19x faster                                                     |
| gunicorn                 | 1.45 ms                                                               | 1.21 ms: 1.19x faster                                                    |
| nqueens                  | 117 ms                                                                | 99.0 ms: 1.19x faster                                                    |
| fannkuch                 | 546 ms                                                                | 463 ms: 1.18x faster                                                     |
| sympy_expand             | 543 ms                                                                | 463 ms: 1.17x faster                                                     |
| aiohttp                  | 1.39 ms                                                               | 1.19 ms: 1.17x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.57 ms: 1.16x faster                                                    |
| deepcopy                 | 511 us                                                                | 443 us: 1.15x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 22.9 ms: 1.15x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 61.0 ms: 1.14x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.04 us: 1.14x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.13 sec: 1.13x faster                                                   |
| scimark_fft              | 500 ms                                                                | 446 ms: 1.12x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 191 ms: 1.11x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.35 sec: 1.11x faster                                                   |
| meteor_contest           | 126 ms                                                                | 114 ms: 1.10x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 6.46 us: 1.08x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.88 us: 1.06x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 31.2 ms: 1.03x faster                                                    |
| json                     | 5.88 ms                                                               | 5.73 ms: 1.03x faster                                                    |
| pickle_list              | 5.24 us                                                               | 5.12 us: 1.02x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 663 ms: 1.01x slower                                                     |
| json_loads               | 30.9 us                                                               | 32.6 us: 1.06x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.40 ms: 1.06x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 37.5 us: 1.07x slower                                                    |
| async_generators         | 452 ms                                                                | 488 ms: 1.08x slower                                                     |
| pickle                   | 12.5 us                                                               | 13.6 us: 1.09x slower                                                    |
| python_startup           | 11.2 ms                                                               | 12.6 ms: 1.12x slower                                                    |
| unpickle                 | 17.5 us                                                               | 19.7 us: 1.13x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.94 ms: 1.16x slower                                                    |
| coverage                 | 83.6 ms                                                               | 97.5 ms: 1.17x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.47 ms: 1.23x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.13 ms: 1.23x slower                                                    |
| telco                    | 8.49 ms                                                               | 164 ms: 19.31x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.24x faster                                                             |

Benchmark hidden because not significant (3): regex_dna, pidigits, flaskblogging
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.14x
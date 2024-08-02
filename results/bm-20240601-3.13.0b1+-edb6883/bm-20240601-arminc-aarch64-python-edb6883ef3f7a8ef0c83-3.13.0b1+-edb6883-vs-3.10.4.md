# Results vs. 3.10.4

- fork: python
- ref: edb6883ef3f7a8ef0c83
- machine: linux-aarch64
- commit hash: edb6883
- commit date: 2024-06-01
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 306 ms: 1.24x faster                                                     |
| chameleon      | 10.8 ms                                                               | 8.93 ms: 1.21x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.13 sec: 1.13x faster                                                   |
| html5lib       | 86.5 ms                                                               | 66.9 ms: 1.29x faster                                                    |
| tornado_http   | 178 ms                                                                | 131 ms: 1.36x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 492 ms: 1.93x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.20 sec: 1.91x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 642 ms: 1.77x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 783 ms: 1.63x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.80x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 111 ms: 1.49x faster                                                     |
| float          | 135 ms                                                                | 92.1 ms: 1.46x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.37x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 30.0 ms: 1.07x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.96 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 359 us: 1.47x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 251 us: 1.46x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 82.2 ms: 1.21x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 194 ms: 1.09x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.56 us: 1.07x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 116 ms: 1.06x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.04x faster                                                     |
| pickle_list          | 5.24 us                                                               | 5.30 us: 1.01x slower                                                    |
| json_loads           | 30.9 us                                                               | 32.6 us: 1.06x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 37.8 us: 1.08x slower                                                    |
| pickle               | 12.5 us                                                               | 13.8 us: 1.10x slower                                                    |
| unpickle             | 17.5 us                                                               | 20.0 us: 1.14x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 8.61 ms: 1.25x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.21x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.6 ms: 1.27x faster                                                    |
| django_template | 53.3 ms                                                               | 41.9 ms: 1.27x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 62.5 ms: 1.12x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 197 us: 3.35x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.82 ms: 2.34x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.16 ms: 2.03x faster                                                    |
| async_tree_none          | 950 ms                                                                | 492 ms: 1.93x faster                                                     |
| raytrace                 | 573 ms                                                                | 297 ms: 1.93x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.20 sec: 1.91x faster                                                   |
| generators               | 68.1 ms                                                               | 37.6 ms: 1.81x faster                                                    |
| chaos                    | 121 ms                                                                | 68.0 ms: 1.78x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 642 ms: 1.77x faster                                                     |
| richards_super           | 107 ms                                                                | 61.9 ms: 1.73x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.43 ms: 1.68x faster                                                    |
| logging_silent           | 222 ns                                                                | 133 ns: 1.67x faster                                                     |
| go                       | 264 ms                                                                | 160 ms: 1.65x faster                                                     |
| richards                 | 91.7 ms                                                               | 55.6 ms: 1.65x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.72 ms: 1.65x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.2 us: 1.64x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 82.1 ms: 1.63x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 783 ms: 1.63x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 585 ms: 1.61x faster                                                     |
| scimark_lu               | 227 ms                                                                | 142 ms: 1.60x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 7.03 ms: 1.55x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 82.9 ms: 1.54x faster                                                    |
| scimark_sor              | 246 ms                                                                | 160 ms: 1.54x faster                                                     |
| nbody                    | 166 ms                                                                | 111 ms: 1.49x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 359 us: 1.47x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.23 sec: 1.47x faster                                                   |
| float                    | 135 ms                                                                | 92.1 ms: 1.46x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 251 us: 1.46x faster                                                     |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                    |
| pylint                   | 485 ms                                                                | 339 ms: 1.43x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.38x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.10 us: 1.38x faster                                                    |
| regex_compile            | 177 ms                                                                | 128 ms: 1.37x faster                                                     |
| pyflate                  | 795 ms                                                                | 581 ms: 1.37x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.76 us: 1.37x faster                                                    |
| tornado_http             | 178 ms                                                                | 131 ms: 1.36x faster                                                     |
| spectral_norm            | 186 ms                                                                | 140 ms: 1.33x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                                   |
| thrift                   | 1.26 ms                                                               | 958 us: 1.32x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 66.9 ms: 1.29x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.0 ms: 1.28x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.6 ms: 1.27x faster                                                    |
| django_template          | 53.3 ms                                                               | 41.9 ms: 1.27x faster                                                    |
| sympy_sum                | 184 ms                                                                | 146 ms: 1.26x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 21.2 ms: 1.25x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.89 sec: 1.25x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.27 ms: 1.25x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                    |
| 2to3                     | 381 ms                                                                | 306 ms: 1.24x faster                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 928 ms: 1.24x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 59.8 ms: 1.23x faster                                                    |
| sympy_str                | 329 ms                                                                | 268 ms: 1.23x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 50.4 us: 1.22x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 128 ms: 1.22x faster                                                     |
| chameleon                | 10.8 ms                                                               | 8.93 ms: 1.21x faster                                                    |
| mypy2                    | 936 ms                                                                | 772 ms: 1.21x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 82.2 ms: 1.21x faster                                                    |
| dask                     | 450 ms                                                                | 373 ms: 1.21x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 62.8 ms: 1.20x faster                                                    |
| fannkuch                 | 546 ms                                                                | 457 ms: 1.19x faster                                                     |
| nqueens                  | 117 ms                                                                | 99.4 ms: 1.18x faster                                                    |
| sympy_expand             | 543 ms                                                                | 461 ms: 1.18x faster                                                     |
| aiohttp                  | 1.39 ms                                                               | 1.19 ms: 1.17x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.52 ms: 1.17x faster                                                    |
| gunicorn                 | 1.45 ms                                                               | 1.24 ms: 1.16x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 23.1 ms: 1.14x faster                                                    |
| deepcopy                 | 511 us                                                                | 448 us: 1.14x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.13 sec: 1.13x faster                                                   |
| scimark_fft              | 500 ms                                                                | 445 ms: 1.12x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 62.5 ms: 1.12x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.31 sec: 1.12x faster                                                   |
| meteor_contest           | 126 ms                                                                | 114 ms: 1.11x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 4.16 us: 1.11x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 194 ms: 1.09x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 30.0 ms: 1.07x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.56 us: 1.07x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 116 ms: 1.06x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.90 us: 1.05x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.04x faster                                                     |
| json                     | 5.88 ms                                                               | 5.71 ms: 1.03x faster                                                    |
| pickle_list              | 5.24 us                                                               | 5.30 us: 1.01x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.35 ms: 1.04x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.6 us: 1.06x slower                                                    |
| async_generators         | 452 ms                                                                | 483 ms: 1.07x slower                                                     |
| pickle_dict              | 35.1 us                                                               | 37.8 us: 1.08x slower                                                    |
| pickle                   | 12.5 us                                                               | 13.8 us: 1.10x slower                                                    |
| unpickle                 | 17.5 us                                                               | 20.0 us: 1.14x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.73 ms: 1.15x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.96 ms: 1.17x slower                                                    |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                    |
| coverage                 | 83.6 ms                                                               | 98.6 ms: 1.18x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.08 ms: 1.22x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.61 ms: 1.25x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.28x faster                                                             |

Benchmark hidden because not significant (4): pidigits, regex_dna, asyncio_websockets, flaskblogging
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240601-3.13.0b1+-edb6883/bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.13x
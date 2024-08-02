# Results vs. 3.10.4

- fork: python
- ref: 44995aab499b09a550de
- machine: linux-aarch64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 362 ms: 1.05x faster                                                     |
| chameleon      | 10.8 ms                                                               | 9.14 ms: 1.19x faster                                                    |
| html5lib       | 86.5 ms                                                               | 70.2 ms: 1.23x faster                                                    |
| tornado_http   | 178 ms                                                                | 141 ms: 1.27x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 496 ms: 1.92x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.25 sec: 1.83x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 654 ms: 1.73x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 806 ms: 1.58x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.76x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 89.8 ms: 1.50x faster                                                    |
| nbody          | 166 ms                                                                | 116 ms: 1.43x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.2 ms: 1.06x faster                                                    |
| regex_compile  | 177 ms                                                                | 167 ms: 1.05x faster                                                     |
| regex_dna      | 257 ms                                                                | 248 ms: 1.04x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.87 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 393 us: 1.35x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 277 us: 1.32x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 13.1 ms: 1.28x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.6 ms: 1.23x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 187 ms: 1.14x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.65 us: 1.05x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 118 ms: 1.05x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 151 ms: 1.03x faster                                                     |
| pickle_list          | 5.24 us                                                               | 5.20 us: 1.01x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.1 us: 1.04x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 38.2 us: 1.09x slower                                                    |
| pickle               | 12.5 us                                                               | 13.7 us: 1.10x slower                                                    |
| unpickle             | 17.5 us                                                               | 19.6 us: 1.12x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.8 ms: 1.56x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.45x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                    |
| django_template | 53.3 ms                                                               | 49.5 ms: 1.08x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 33.9 ms: 1.04x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 82.0 ms: 1.17x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.08x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.20x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.63 ms: 1.93x faster                                                    |
| async_tree_none          | 950 ms                                                                | 496 ms: 1.92x faster                                                     |
| bench_mp_pool            | 14.5 ms                                                               | 7.87 ms: 1.85x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.25 sec: 1.83x faster                                                   |
| generators               | 68.1 ms                                                               | 38.8 ms: 1.76x faster                                                    |
| raytrace                 | 573 ms                                                                | 327 ms: 1.76x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 654 ms: 1.73x faster                                                     |
| richards_super           | 107 ms                                                                | 62.3 ms: 1.72x faster                                                    |
| richards                 | 91.7 ms                                                               | 55.2 ms: 1.66x faster                                                    |
| logging_silent           | 222 ns                                                                | 140 ns: 1.59x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 806 ms: 1.58x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 86.6 ms: 1.55x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 624 ms: 1.51x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.59 ms: 1.51x faster                                                    |
| float                    | 135 ms                                                                | 89.8 ms: 1.50x faster                                                    |
| go                       | 264 ms                                                                | 178 ms: 1.48x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 87.6 ms: 1.46x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.27 sec: 1.45x faster                                                   |
| comprehensions           | 33.1 us                                                               | 23.1 us: 1.44x faster                                                    |
| nbody                    | 166 ms                                                                | 116 ms: 1.43x faster                                                     |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                    |
| scimark_sor              | 246 ms                                                                | 175 ms: 1.41x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 2.03 ms: 1.40x faster                                                    |
| chaos                    | 121 ms                                                                | 89.2 ms: 1.36x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 393 us: 1.35x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.33 us: 1.33x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 277 us: 1.32x faster                                                     |
| logging_format           | 10.6 us                                                               | 8.05 us: 1.32x faster                                                    |
| pyflate                  | 795 ms                                                                | 613 ms: 1.30x faster                                                     |
| thrift                   | 1.26 ms                                                               | 972 us: 1.30x faster                                                     |
| coroutines               | 37.2 ms                                                               | 28.8 ms: 1.29x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.1 ms: 1.28x faster                                                    |
| spectral_norm            | 186 ms                                                                | 146 ms: 1.28x faster                                                     |
| tornado_http             | 178 ms                                                                | 141 ms: 1.27x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.36 sec: 1.24x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 49.8 us: 1.24x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 80.6 ms: 1.23x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 70.2 ms: 1.23x faster                                                    |
| scimark_lu               | 227 ms                                                                | 184 ms: 1.23x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 8.97 ms: 1.22x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.32 ms: 1.20x faster                                                    |
| chameleon                | 10.8 ms                                                               | 9.14 ms: 1.19x faster                                                    |
| pylint                   | 485 ms                                                                | 411 ms: 1.18x faster                                                     |
| fannkuch                 | 546 ms                                                                | 479 ms: 1.14x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 187 ms: 1.14x faster                                                     |
| dask                     | 450 ms                                                                | 397 ms: 1.13x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 23.4 ms: 1.13x faster                                                    |
| gunicorn                 | 1.45 ms                                                               | 1.31 ms: 1.10x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.97 ms: 1.09x faster                                                    |
| scimark_fft              | 500 ms                                                                | 458 ms: 1.09x faster                                                     |
| django_template          | 53.3 ms                                                               | 49.5 ms: 1.08x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 68.7 ms: 1.07x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 146 ms: 1.07x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 30.2 ms: 1.06x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.87 us: 1.06x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.48 sec: 1.06x faster                                                   |
| meteor_contest           | 126 ms                                                                | 119 ms: 1.06x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 71.3 ms: 1.06x faster                                                    |
| regex_compile            | 177 ms                                                                | 167 ms: 1.05x faster                                                     |
| 2to3                     | 381 ms                                                                | 362 ms: 1.05x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 6.65 us: 1.05x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 118 ms: 1.05x faster                                                     |
| json                     | 5.88 ms                                                               | 5.65 ms: 1.04x faster                                                    |
| regex_dna                | 257 ms                                                                | 248 ms: 1.04x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 33.9 ms: 1.04x faster                                                    |
| aiohttp                  | 1.39 ms                                                               | 1.34 ms: 1.04x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.11 sec: 1.03x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 151 ms: 1.03x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 26.0 ms: 1.02x faster                                                    |
| deepcopy                 | 511 us                                                                | 502 us: 1.02x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 2.32 sec: 1.02x faster                                                   |
| sympy_str                | 329 ms                                                                | 324 ms: 1.01x faster                                                     |
| sympy_sum                | 184 ms                                                                | 182 ms: 1.01x faster                                                     |
| pickle_list              | 5.24 us                                                               | 5.20 us: 1.01x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 662 ms: 1.01x slower                                                     |
| sympy_expand             | 543 ms                                                                | 548 ms: 1.01x slower                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 4.66 us: 1.01x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.1 us: 1.04x slower                                                    |
| flaskblogging            | 4.83 ms                                                               | 5.06 ms: 1.05x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.45 ms: 1.08x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 38.2 us: 1.09x slower                                                    |
| pickle                   | 12.5 us                                                               | 13.7 us: 1.10x slower                                                    |
| unpickle                 | 17.5 us                                                               | 19.6 us: 1.12x slower                                                    |
| async_generators         | 452 ms                                                                | 514 ms: 1.14x slower                                                     |
| regex_effbot             | 4.25 ms                                                               | 4.87 ms: 1.15x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 82.0 ms: 1.17x slower                                                    |
| coverage                 | 83.6 ms                                                               | 99.1 ms: 1.19x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.30 ms: 1.28x slower                                                    |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.8 ms: 1.56x slower                                                    |
| telco                    | 8.49 ms                                                               | 167 ms: 19.66x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.15x faster                                                             |

Benchmark hidden because not significant (4): nqueens, pidigits, docutils, mypy2
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.25x
# Results vs. 3.10.4

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-aarch64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 362 ms: 1.05x faster                                                     |
| chameleon      | 10.8 ms                                                               | 9.09 ms: 1.19x faster                                                    |
| html5lib       | 86.5 ms                                                               | 72.6 ms: 1.19x faster                                                    |
| tornado_http   | 178 ms                                                                | 142 ms: 1.25x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 507 ms: 1.87x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.23 sec: 1.86x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 668 ms: 1.70x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 827 ms: 1.54x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.74x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 90.0 ms: 1.50x faster                                                    |
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.2 ms: 1.07x faster                                                    |
| regex_dna      | 257 ms                                                                | 260 ms: 1.01x slower                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.97 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 398 us: 1.33x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 277 us: 1.32x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 13.0 ms: 1.28x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 187 ms: 1.13x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.08x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.59 us: 1.06x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                                     |
| pickle_list          | 5.24 us                                                               | 5.30 us: 1.01x slower                                                    |
| json_loads           | 30.9 us                                                               | 32.3 us: 1.04x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 37.7 us: 1.07x slower                                                    |
| pickle               | 12.5 us                                                               | 13.4 us: 1.08x slower                                                    |
| unpickle             | 17.5 us                                                               | 19.7 us: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 15.5 ms: 1.39x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 11.1 ms: 1.62x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.50x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.0 ms: 1.46x faster                                                    |
| django_template | 53.3 ms                                                               | 50.5 ms: 1.06x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 33.9 ms: 1.04x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 82.6 ms: 1.18x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.08x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 209 us: 3.16x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.55 ms: 1.97x faster                                                    |
| async_tree_none          | 950 ms                                                                | 507 ms: 1.87x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.23 sec: 1.86x faster                                                   |
| raytrace                 | 573 ms                                                                | 322 ms: 1.78x faster                                                     |
| bench_mp_pool            | 14.5 ms                                                               | 8.22 ms: 1.77x faster                                                    |
| generators               | 68.1 ms                                                               | 39.7 ms: 1.71x faster                                                    |
| richards_super           | 107 ms                                                                | 62.8 ms: 1.71x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 668 ms: 1.70x faster                                                     |
| richards                 | 91.7 ms                                                               | 55.7 ms: 1.65x faster                                                    |
| logging_silent           | 222 ns                                                                | 139 ns: 1.59x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 827 ms: 1.54x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.58 ms: 1.52x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 88.8 ms: 1.51x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 630 ms: 1.50x faster                                                     |
| float                    | 135 ms                                                                | 90.0 ms: 1.50x faster                                                    |
| go                       | 264 ms                                                                | 179 ms: 1.47x faster                                                     |
| mako                     | 18.9 ms                                                               | 13.0 ms: 1.46x faster                                                    |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.28 sec: 1.44x faster                                                   |
| comprehensions           | 33.1 us                                                               | 23.1 us: 1.43x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 90.0 ms: 1.42x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.01 ms: 1.42x faster                                                    |
| scimark_sor              | 246 ms                                                                | 175 ms: 1.41x faster                                                     |
| chaos                    | 121 ms                                                                | 88.0 ms: 1.38x faster                                                    |
| pyflate                  | 795 ms                                                                | 596 ms: 1.33x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.35 us: 1.33x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.98 us: 1.33x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 398 us: 1.33x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 277 us: 1.32x faster                                                     |
| thrift                   | 1.26 ms                                                               | 974 us: 1.29x faster                                                     |
| coroutines               | 37.2 ms                                                               | 28.9 ms: 1.28x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.0 ms: 1.28x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                   |
| spectral_norm            | 186 ms                                                                | 147 ms: 1.26x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 49.2 us: 1.25x faster                                                    |
| tornado_http             | 178 ms                                                                | 142 ms: 1.25x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                                    |
| scimark_lu               | 227 ms                                                                | 184 ms: 1.24x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.38 sec: 1.23x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 9.05 ms: 1.21x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.20x faster                                                    |
| chameleon                | 10.8 ms                                                               | 9.09 ms: 1.19x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 72.6 ms: 1.19x faster                                                    |
| fannkuch                 | 546 ms                                                                | 462 ms: 1.18x faster                                                     |
| pylint                   | 485 ms                                                                | 421 ms: 1.15x faster                                                     |
| dask                     | 450 ms                                                                | 392 ms: 1.15x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 23.2 ms: 1.14x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 187 ms: 1.13x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.89 ms: 1.11x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 142 ms: 1.10x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 69.3 ms: 1.09x faster                                                    |
| scimark_fft              | 500 ms                                                                | 460 ms: 1.09x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.08x faster                                                     |
| meteor_contest           | 126 ms                                                                | 117 ms: 1.08x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.81 us: 1.08x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.45 sec: 1.07x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 30.2 ms: 1.07x faster                                                    |
| gunicorn                 | 1.45 ms                                                               | 1.36 ms: 1.06x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.59 us: 1.06x faster                                                    |
| django_template          | 53.3 ms                                                               | 50.5 ms: 1.06x faster                                                    |
| aiohttp                  | 1.39 ms                                                               | 1.32 ms: 1.05x faster                                                    |
| 2to3                     | 381 ms                                                                | 362 ms: 1.05x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 33.9 ms: 1.04x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 25.6 ms: 1.04x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.11 sec: 1.03x faster                                                   |
| deepcopy                 | 511 us                                                                | 495 us: 1.03x faster                                                     |
| json                     | 5.88 ms                                                               | 5.71 ms: 1.03x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 71.8 ms: 1.02x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.32 sec: 1.02x faster                                                   |
| sympy_str                | 329 ms                                                                | 323 ms: 1.02x faster                                                     |
| sympy_expand             | 543 ms                                                                | 547 ms: 1.01x slower                                                     |
| pickle_list              | 5.24 us                                                               | 5.30 us: 1.01x slower                                                    |
| regex_dna                | 257 ms                                                                | 260 ms: 1.01x slower                                                     |
| asyncio_websockets       | 657 ms                                                                | 666 ms: 1.01x slower                                                     |
| json_loads               | 30.9 us                                                               | 32.3 us: 1.04x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.39 ms: 1.06x slower                                                    |
| flaskblogging            | 4.83 ms                                                               | 5.14 ms: 1.06x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 37.7 us: 1.07x slower                                                    |
| pickle                   | 12.5 us                                                               | 13.4 us: 1.08x slower                                                    |
| unpickle                 | 17.5 us                                                               | 19.7 us: 1.13x slower                                                    |
| async_generators         | 452 ms                                                                | 522 ms: 1.15x slower                                                     |
| regex_effbot             | 4.25 ms                                                               | 4.97 ms: 1.17x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 82.6 ms: 1.18x slower                                                    |
| coverage                 | 83.6 ms                                                               | 99.5 ms: 1.19x slower                                                    |
| telco                    | 8.49 ms                                                               | 10.1 ms: 1.19x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.16 ms: 1.24x slower                                                    |
| python_startup           | 11.2 ms                                                               | 15.5 ms: 1.39x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 11.1 ms: 1.62x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.18x faster                                                             |

Benchmark hidden because not significant (7): nqueens, pidigits, deepcopy_reduce, docutils, sympy_sum, regex_compile, mypy2
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.25x
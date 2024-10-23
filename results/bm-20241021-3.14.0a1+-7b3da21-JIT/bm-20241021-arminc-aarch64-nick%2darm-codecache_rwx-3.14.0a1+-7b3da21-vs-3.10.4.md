# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-aarch64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.10x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 363 ms: 1.05x faster                                                  |
| docutils       | 3.53 sec                                                              | 3.48 sec: 1.01x faster                                                |
| html5lib       | 86.5 ms                                                               | 71.7 ms: 1.21x faster                                                 |
| tornado_http   | 178 ms                                                                | 143 ms: 1.25x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 473 ms: 2.01x faster                                                  |
| async_tree_io           | 2.28 sec                                                              | 1.20 sec: 1.91x faster                                                |
| async_tree_memoization  | 1.13 sec                                                              | 604 ms: 1.88x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 764 ms: 1.67x faster                                                  |
| Geometric mean          | (ref)                                                                 | 1.86x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                                  |
| float          | 135 ms                                                                | 97.0 ms: 1.39x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 162 ms: 1.09x faster                                                  |
| regex_v8       | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                 |
| regex_dna      | 257 ms                                                                | 252 ms: 1.02x faster                                                  |
| regex_effbot   | 4.25 ms                                                               | 4.92 ms: 1.16x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 267 us: 1.37x faster                                                  |
| pickle_pure_python   | 529 us                                                                | 392 us: 1.35x faster                                                  |
| tomli_loads          | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                                |
| xml_etree_process    | 99.5 ms                                                               | 81.2 ms: 1.23x faster                                                 |
| json_dumps           | 16.7 ms                                                               | 14.3 ms: 1.16x faster                                                 |
| xml_etree_parse      | 212 ms                                                                | 188 ms: 1.13x faster                                                  |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 156 ms                                                                | 153 ms: 1.02x faster                                                  |
| json_loads           | 30.9 us                                                               | 31.3 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.17x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.72 ms: 1.27x slower                                                 |
| python_startup         | 11.2 ms                                                               | 14.5 ms: 1.30x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.28x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                                 |
| genshi_text     | 35.2 ms                                                               | 32.6 ms: 1.08x faster                                                 |
| django_template | 53.3 ms                                                               | 50.6 ms: 1.05x faster                                                 |
| genshi_xml      | 69.8 ms                                                               | 78.6 ms: 1.13x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.10x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 210 us: 3.15x faster                                                  |
| async_tree_none          | 950 ms                                                                | 473 ms: 2.01x faster                                                  |
| deltablue                | 8.94 ms                                                               | 4.49 ms: 1.99x faster                                                 |
| async_tree_io            | 2.28 sec                                                              | 1.20 sec: 1.91x faster                                                |
| async_tree_memoization   | 1.13 sec                                                              | 604 ms: 1.88x faster                                                  |
| richards_super           | 107 ms                                                                | 63.9 ms: 1.68x faster                                                 |
| logging_silent           | 222 ns                                                                | 133 ns: 1.67x faster                                                  |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 764 ms: 1.67x faster                                                  |
| raytrace                 | 573 ms                                                                | 351 ms: 1.64x faster                                                  |
| scimark_sor              | 246 ms                                                                | 153 ms: 1.61x faster                                                  |
| deepcopy_memo            | 61.7 us                                                               | 38.9 us: 1.59x faster                                                 |
| richards                 | 91.7 ms                                                               | 59.7 ms: 1.54x faster                                                 |
| scimark_lu               | 227 ms                                                                | 152 ms: 1.49x faster                                                  |
| go                       | 264 ms                                                                | 177 ms: 1.49x faster                                                  |
| crypto_pyaes             | 134 ms                                                                | 90.5 ms: 1.48x faster                                                 |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                                  |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                                 |
| sqlglot_parse            | 2.40 ms                                                               | 1.68 ms: 1.43x faster                                                 |
| scimark_monte_carlo      | 128 ms                                                                | 90.0 ms: 1.42x faster                                                 |
| chaos                    | 121 ms                                                                | 85.4 ms: 1.42x faster                                                 |
| float                    | 135 ms                                                                | 97.0 ms: 1.39x faster                                                 |
| unpickle_pure_python     | 366 us                                                                | 267 us: 1.37x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 392 us: 1.35x faster                                                  |
| comprehensions           | 33.1 us                                                               | 24.6 us: 1.35x faster                                                 |
| deepcopy                 | 511 us                                                                | 379 us: 1.35x faster                                                  |
| thrift                   | 1.26 ms                                                               | 941 us: 1.34x faster                                                  |
| logging_format           | 10.6 us                                                               | 7.99 us: 1.33x faster                                                 |
| logging_simple           | 9.78 us                                                               | 7.38 us: 1.32x faster                                                 |
| sqlglot_transpile        | 2.84 ms                                                               | 2.15 ms: 1.32x faster                                                 |
| coroutines               | 37.2 ms                                                               | 28.7 ms: 1.29x faster                                                 |
| tomli_loads              | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                                |
| pyflate                  | 795 ms                                                                | 636 ms: 1.25x faster                                                  |
| tornado_http             | 178 ms                                                                | 143 ms: 1.25x faster                                                  |
| xml_etree_process        | 99.5 ms                                                               | 81.2 ms: 1.23x faster                                                 |
| html5lib                 | 86.5 ms                                                               | 71.7 ms: 1.21x faster                                                 |
| pathlib                  | 26.3 ms                                                               | 21.8 ms: 1.20x faster                                                 |
| deepcopy_reduce          | 4.60 us                                                               | 3.87 us: 1.19x faster                                                 |
| spectral_norm            | 186 ms                                                                | 159 ms: 1.18x faster                                                  |
| bench_thread_pool        | 1.59 ms                                                               | 1.36 ms: 1.17x faster                                                 |
| json_dumps               | 16.7 ms                                                               | 14.3 ms: 1.16x faster                                                 |
| generators               | 68.1 ms                                                               | 58.8 ms: 1.16x faster                                                 |
| pycparser                | 1.69 sec                                                              | 1.48 sec: 1.14x faster                                                |
| xml_etree_parse          | 212 ms                                                                | 188 ms: 1.13x faster                                                  |
| hexiom                   | 10.9 ms                                                               | 9.81 ms: 1.11x faster                                                 |
| scimark_fft              | 500 ms                                                                | 454 ms: 1.10x faster                                                  |
| pylint                   | 485 ms                                                                | 442 ms: 1.10x faster                                                  |
| regex_compile            | 177 ms                                                                | 162 ms: 1.09x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.08x faster                                                  |
| genshi_text              | 35.2 ms                                                               | 32.6 ms: 1.08x faster                                                 |
| mdp                      | 3.70 sec                                                              | 3.47 sec: 1.07x faster                                                |
| fannkuch                 | 546 ms                                                                | 513 ms: 1.06x faster                                                  |
| django_template          | 53.3 ms                                                               | 50.6 ms: 1.05x faster                                                 |
| 2to3                     | 381 ms                                                                | 363 ms: 1.05x faster                                                  |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.27 ms: 1.05x faster                                                 |
| sqlglot_normalize        | 156 ms                                                                | 150 ms: 1.04x faster                                                  |
| json                     | 5.88 ms                                                               | 5.64 ms: 1.04x faster                                                 |
| regex_v8                 | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                 |
| regex_dna                | 257 ms                                                                | 252 ms: 1.02x faster                                                  |
| xml_etree_iterparse      | 156 ms                                                                | 153 ms: 1.02x faster                                                  |
| meteor_contest           | 126 ms                                                                | 124 ms: 1.02x faster                                                  |
| docutils                 | 3.53 sec                                                              | 3.48 sec: 1.01x faster                                                |
| json_loads               | 30.9 us                                                               | 31.3 us: 1.01x slower                                                 |
| sqlglot_optimize         | 75.4 ms                                                               | 77.0 ms: 1.02x slower                                                 |
| dulwich_log              | 73.5 ms                                                               | 75.8 ms: 1.03x slower                                                 |
| sympy_expand             | 543 ms                                                                | 563 ms: 1.04x slower                                                  |
| sympy_str                | 329 ms                                                                | 343 ms: 1.04x slower                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.22 sec: 1.07x slower                                                |
| nqueens                  | 117 ms                                                                | 126 ms: 1.07x slower                                                  |
| sympy_integrate          | 26.5 ms                                                               | 28.9 ms: 1.09x slower                                                 |
| pprint_pformat           | 2.36 sec                                                              | 2.58 sec: 1.09x slower                                                |
| sympy_sum                | 184 ms                                                                | 205 ms: 1.11x slower                                                  |
| async_generators         | 452 ms                                                                | 506 ms: 1.12x slower                                                  |
| telco                    | 8.49 ms                                                               | 9.49 ms: 1.12x slower                                                 |
| genshi_xml               | 69.8 ms                                                               | 78.6 ms: 1.13x slower                                                 |
| regex_effbot             | 4.25 ms                                                               | 4.92 ms: 1.16x slower                                                 |
| coverage                 | 83.6 ms                                                               | 99.9 ms: 1.20x slower                                                 |
| python_startup_no_site   | 6.89 ms                                                               | 8.72 ms: 1.27x slower                                                 |
| python_startup           | 11.2 ms                                                               | 14.5 ms: 1.30x slower                                                 |
| gc_traversal             | 4.15 ms                                                               | 6.29 ms: 1.51x slower                                                 |
| create_gc_cycles         | 2.26 ms                                                               | 3.64 ms: 1.61x slower                                                 |
| bench_mp_pool            | 14.5 ms                                                               | 4.29 sec: 295.18x slower                                              |
| Geometric mean           | (ref)                                                                 | 1.10x faster                                                          |

Benchmark hidden because not significant (2): pidigits, asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241021-3.14.0a1+-7b3da21-JIT/bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.39x
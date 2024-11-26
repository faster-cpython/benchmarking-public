# Results vs. 3.10.4

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-aarch64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.316x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 294 ms: 1.30x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                   |
| html5lib       | 86.5 ms                                                               | 65.3 ms: 1.32x faster                                                    |
| tornado_http   | 178 ms                                                                | 125 ms: 1.42x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 445 ms: 2.14x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.13 sec: 2.02x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 578 ms: 1.96x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 743 ms: 1.71x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.95x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 95.1 ms: 1.42x faster                                                    |
| nbody          | 166 ms                                                                | 117 ms: 1.41x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.42x faster                                                     |
| regex_dna      | 257 ms                                                                | 253 ms: 1.02x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 31.9 ms: 1.01x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.96 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 371 us: 1.43x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 257 us: 1.42x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.9 ms: 1.23x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.1 ms: 1.18x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 186 ms: 1.14x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 147 ms: 1.06x faster                                                     |
| json_loads           | 30.9 us                                                               | 31.3 us: 1.01x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.19x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.67 ms: 1.26x slower                                                    |
| python_startup         | 11.2 ms                                                               | 15.6 ms: 1.39x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.6 ms: 1.28x faster                                                    |
| django_template | 53.3 ms                                                               | 41.9 ms: 1.27x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 60.1 ms: 1.16x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 194 us: 3.41x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.94 ms: 2.27x faster                                                    |
| async_tree_none          | 950 ms                                                                | 445 ms: 2.14x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.13 sec: 2.02x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 578 ms: 1.96x faster                                                     |
| generators               | 68.1 ms                                                               | 34.8 ms: 1.95x faster                                                    |
| go                       | 264 ms                                                                | 137 ms: 1.93x faster                                                     |
| raytrace                 | 573 ms                                                                | 310 ms: 1.85x faster                                                     |
| richards_super           | 107 ms                                                                | 60.0 ms: 1.79x faster                                                    |
| chaos                    | 121 ms                                                                | 70.3 ms: 1.72x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 743 ms: 1.71x faster                                                     |
| richards                 | 91.7 ms                                                               | 53.9 ms: 1.70x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.41 ms: 1.70x faster                                                    |
| logging_silent           | 222 ns                                                                | 132 ns: 1.68x faster                                                     |
| scimark_lu               | 227 ms                                                                | 135 ms: 1.68x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.74 ms: 1.63x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 82.7 ms: 1.62x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 38.4 us: 1.61x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.8 us: 1.59x faster                                                    |
| scimark_sor              | 246 ms                                                                | 160 ms: 1.54x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 7.11 ms: 1.53x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 83.3 ms: 1.53x faster                                                    |
| deepcopy                 | 511 us                                                                | 336 us: 1.52x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 371 us: 1.43x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 257 us: 1.42x faster                                                     |
| tornado_http             | 178 ms                                                                | 125 ms: 1.42x faster                                                     |
| float                    | 135 ms                                                                | 95.1 ms: 1.42x faster                                                    |
| logging_simple           | 9.78 us                                                               | 6.91 us: 1.42x faster                                                    |
| regex_compile            | 177 ms                                                                | 125 ms: 1.42x faster                                                     |
| nbody                    | 166 ms                                                                | 117 ms: 1.41x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 140 ms: 1.41x faster                                                     |
| mako                     | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.62 us: 1.39x faster                                                    |
| pylint                   | 485 ms                                                                | 352 ms: 1.38x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.24 sec: 1.37x faster                                                   |
| pyflate                  | 795 ms                                                                | 585 ms: 1.36x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.4 ms: 1.33x faster                                                    |
| thrift                   | 1.26 ms                                                               | 945 us: 1.33x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 65.3 ms: 1.32x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.6 ms: 1.30x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.54 us: 1.30x faster                                                    |
| 2to3                     | 381 ms                                                                | 294 ms: 1.30x faster                                                     |
| spectral_norm            | 186 ms                                                                | 144 ms: 1.29x faster                                                     |
| sympy_sum                | 184 ms                                                                | 142 ms: 1.29x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.6 ms: 1.28x faster                                                    |
| django_template          | 53.3 ms                                                               | 41.9 ms: 1.27x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 21.2 ms: 1.25x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 58.7 ms: 1.25x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.28 ms: 1.24x faster                                                    |
| sympy_str                | 329 ms                                                                | 264 ms: 1.24x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 80.9 ms: 1.23x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.92 sec: 1.23x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.5 ms: 1.22x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 128 ms: 1.22x faster                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 939 ms: 1.22x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 62.0 ms: 1.22x faster                                                    |
| nqueens                  | 117 ms                                                                | 98.9 ms: 1.19x faster                                                    |
| sympy_expand             | 543 ms                                                                | 459 ms: 1.18x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.1 ms: 1.18x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                   |
| fannkuch                 | 546 ms                                                                | 468 ms: 1.17x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 60.1 ms: 1.16x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.57 ms: 1.16x faster                                                    |
| scimark_fft              | 500 ms                                                                | 438 ms: 1.14x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 186 ms: 1.14x faster                                                     |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.11x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.35 sec: 1.10x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                     |
| json                     | 5.88 ms                                                               | 5.46 ms: 1.08x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 147 ms: 1.06x faster                                                     |
| regex_dna                | 257 ms                                                                | 253 ms: 1.02x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 31.9 ms: 1.01x faster                                                    |
| json_loads               | 30.9 us                                                               | 31.3 us: 1.01x slower                                                    |
| async_generators         | 452 ms                                                                | 477 ms: 1.05x slower                                                     |
| telco                    | 8.49 ms                                                               | 9.45 ms: 1.11x slower                                                    |
| coverage                 | 83.6 ms                                                               | 97.2 ms: 1.16x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.96 ms: 1.17x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.67 ms: 1.26x slower                                                    |
| python_startup           | 11.2 ms                                                               | 15.6 ms: 1.39x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.31 ms: 1.52x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.60 ms: 1.59x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 4.94 sec: 340.05x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.22x faster                                                             |

Benchmark hidden because not significant (2): pidigits, asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.316x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.28x
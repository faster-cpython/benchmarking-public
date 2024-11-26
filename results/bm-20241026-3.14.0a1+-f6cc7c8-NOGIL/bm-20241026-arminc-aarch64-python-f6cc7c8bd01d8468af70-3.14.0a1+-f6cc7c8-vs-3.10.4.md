# Results vs. 3.10.4

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-aarch64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.193x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x slower
- Memory change: 1.50x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 512 ms: 1.34x slower                                                     |
| docutils       | 3.53 sec                                                              | 4.09 sec: 1.16x slower                                                   |
| html5lib       | 86.5 ms                                                               | 119 ms: 1.38x slower                                                     |
| tornado_http   | 178 ms                                                                | 205 ms: 1.15x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.39 sec: 1.65x faster                                                   |
| async_tree_none         | 950 ms                                                                | 608 ms: 1.56x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 742 ms: 1.53x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 917 ms: 1.39x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.53x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 209 ms: 1.55x slower                                                     |
| nbody          | 166 ms                                                                | 286 ms: 1.73x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.39x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 251 ms: 1.02x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 32.9 ms: 1.02x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.48 ms: 1.05x slower                                                    |
| regex_compile  | 177 ms                                                                | 250 ms: 1.41x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 182 ms: 1.17x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 153 ms: 1.02x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 18.9 ms: 1.13x slower                                                    |
| json_loads           | 30.9 us                                                               | 37.3 us: 1.20x slower                                                    |
| tomli_loads          | 3.36 sec                                                              | 4.19 sec: 1.25x slower                                                   |
| xml_etree_process    | 99.5 ms                                                               | 127 ms: 1.28x slower                                                     |
| xml_etree_generate   | 123 ms                                                                | 158 ms: 1.29x slower                                                     |
| unpickle_pure_python | 366 us                                                                | 532 us: 1.46x slower                                                     |
| pickle_pure_python   | 529 us                                                                | 778 us: 1.47x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.20x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.1 ms: 1.76x slower                                                    |
| python_startup         | 11.2 ms                                                               | 20.4 ms: 1.82x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.79x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 69.8 ms                                                               | 101 ms: 1.45x slower                                                     |
| genshi_text     | 35.2 ms                                                               | 51.4 ms: 1.46x slower                                                    |
| django_template | 53.3 ms                                                               | 80.6 ms: 1.51x slower                                                    |
| mako            | 18.9 ms                                                               | 29.2 ms: 1.54x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.49x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 325 us: 2.03x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.39 sec: 1.65x faster                                                   |
| async_tree_none          | 950 ms                                                                | 608 ms: 1.56x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 742 ms: 1.53x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 917 ms: 1.39x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 182 ms: 1.17x faster                                                     |
| generators               | 68.1 ms                                                               | 59.3 ms: 1.15x faster                                                    |
| regex_dna                | 257 ms                                                                | 251 ms: 1.02x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 153 ms: 1.02x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 32.9 ms: 1.02x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 673 ms: 1.03x slower                                                     |
| pylint                   | 485 ms                                                                | 507 ms: 1.04x slower                                                     |
| crypto_pyaes             | 134 ms                                                                | 140 ms: 1.05x slower                                                     |
| deepcopy                 | 511 us                                                                | 536 us: 1.05x slower                                                     |
| regex_effbot             | 4.25 ms                                                               | 4.48 ms: 1.05x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 4.43 ms: 1.07x slower                                                    |
| coroutines               | 37.2 ms                                                               | 40.0 ms: 1.08x slower                                                    |
| deepcopy_memo            | 61.7 us                                                               | 69.5 us: 1.13x slower                                                    |
| json_dumps               | 16.7 ms                                                               | 18.9 ms: 1.13x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.56 ms: 1.13x slower                                                    |
| scimark_fft              | 500 ms                                                                | 569 ms: 1.14x slower                                                     |
| tornado_http             | 178 ms                                                                | 205 ms: 1.15x slower                                                     |
| json                     | 5.88 ms                                                               | 6.75 ms: 1.15x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.82 ms: 1.16x slower                                                    |
| docutils                 | 3.53 sec                                                              | 4.09 sec: 1.16x slower                                                   |
| mdp                      | 3.70 sec                                                              | 4.31 sec: 1.17x slower                                                   |
| json_loads               | 30.9 us                                                               | 37.3 us: 1.20x slower                                                    |
| pycparser                | 1.69 sec                                                              | 2.05 sec: 1.21x slower                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.96 ms: 1.23x slower                                                    |
| spectral_norm            | 186 ms                                                                | 231 ms: 1.24x slower                                                     |
| comprehensions           | 33.1 us                                                               | 41.2 us: 1.24x slower                                                    |
| tomli_loads              | 3.36 sec                                                              | 4.19 sec: 1.25x slower                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 5.84 us: 1.27x slower                                                    |
| xml_etree_process        | 99.5 ms                                                               | 127 ms: 1.28x slower                                                     |
| logging_silent           | 222 ns                                                                | 285 ns: 1.28x slower                                                     |
| richards                 | 91.7 ms                                                               | 118 ms: 1.29x slower                                                     |
| pyflate                  | 795 ms                                                                | 1.02 sec: 1.29x slower                                                   |
| xml_etree_generate       | 123 ms                                                                | 158 ms: 1.29x slower                                                     |
| nqueens                  | 117 ms                                                                | 153 ms: 1.30x slower                                                     |
| dulwich_log              | 73.5 ms                                                               | 95.8 ms: 1.30x slower                                                    |
| chaos                    | 121 ms                                                                | 159 ms: 1.31x slower                                                     |
| meteor_contest           | 126 ms                                                                | 166 ms: 1.32x slower                                                     |
| richards_super           | 107 ms                                                                | 141 ms: 1.32x slower                                                     |
| sympy_integrate          | 26.5 ms                                                               | 35.2 ms: 1.33x slower                                                    |
| thrift                   | 1.26 ms                                                               | 1.69 ms: 1.34x slower                                                    |
| 2to3                     | 381 ms                                                                | 512 ms: 1.34x slower                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 268 ms: 1.36x slower                                                     |
| fannkuch                 | 546 ms                                                                | 751 ms: 1.38x slower                                                     |
| html5lib                 | 86.5 ms                                                               | 119 ms: 1.38x slower                                                     |
| scimark_sor              | 246 ms                                                                | 346 ms: 1.40x slower                                                     |
| deltablue                | 8.94 ms                                                               | 12.6 ms: 1.41x slower                                                    |
| regex_compile            | 177 ms                                                                | 250 ms: 1.41x slower                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 181 ms: 1.42x slower                                                     |
| sqlglot_normalize        | 156 ms                                                                | 222 ms: 1.42x slower                                                     |
| raytrace                 | 573 ms                                                                | 821 ms: 1.43x slower                                                     |
| hexiom                   | 10.9 ms                                                               | 15.7 ms: 1.44x slower                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 29.7 ms: 1.45x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 101 ms: 1.45x slower                                                     |
| async_generators         | 452 ms                                                                | 658 ms: 1.46x slower                                                     |
| unpickle_pure_python     | 366 us                                                                | 532 us: 1.46x slower                                                     |
| genshi_text              | 35.2 ms                                                               | 51.4 ms: 1.46x slower                                                    |
| scimark_lu               | 227 ms                                                                | 333 ms: 1.47x slower                                                     |
| pickle_pure_python       | 529 us                                                                | 778 us: 1.47x slower                                                     |
| pprint_pformat           | 2.36 sec                                                              | 3.47 sec: 1.47x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.69 sec: 1.47x slower                                                   |
| logging_simple           | 9.78 us                                                               | 14.4 us: 1.48x slower                                                    |
| go                       | 264 ms                                                                | 391 ms: 1.48x slower                                                     |
| logging_format           | 10.6 us                                                               | 15.7 us: 1.48x slower                                                    |
| telco                    | 8.49 ms                                                               | 12.6 ms: 1.49x slower                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 113 ms: 1.49x slower                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 4.26 ms: 1.50x slower                                                    |
| django_template          | 53.3 ms                                                               | 80.6 ms: 1.51x slower                                                    |
| sympy_str                | 329 ms                                                                | 506 ms: 1.54x slower                                                     |
| mako                     | 18.9 ms                                                               | 29.2 ms: 1.54x slower                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 3.72 ms: 1.55x slower                                                    |
| float                    | 135 ms                                                                | 209 ms: 1.55x slower                                                     |
| coverage                 | 83.6 ms                                                               | 133 ms: 1.59x slower                                                     |
| sympy_sum                | 184 ms                                                                | 311 ms: 1.69x slower                                                     |
| nbody                    | 166 ms                                                                | 286 ms: 1.73x slower                                                     |
| sympy_expand             | 543 ms                                                                | 948 ms: 1.75x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 12.1 ms: 1.76x slower                                                    |
| python_startup           | 11.2 ms                                                               | 20.4 ms: 1.82x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 61.1 ms: 4.21x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.26x slower                                                             |

Benchmark hidden because not significant (2): pathlib, pidigits
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241026-3.14.0a1+-f6cc7c8-NOGIL/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.193x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.24x
- 95% likely to have a slowdown of 1.23x
- 99% likely to have a slowdown of 1.19x

# Memory
- memory change: 1.50x
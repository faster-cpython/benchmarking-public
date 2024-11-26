# Results vs. 3.10.4

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-aarch64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.157x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 389 ms: 1.02x slower                                                     |
| docutils       | 3.53 sec                                                              | 3.70 sec: 1.05x slower                                                   |
| html5lib       | 86.5 ms                                                               | 72.7 ms: 1.19x faster                                                    |
| tornado_http   | 178 ms                                                                | 148 ms: 1.20x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 468 ms: 2.03x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.18 sec: 1.94x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 597 ms: 1.90x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 769 ms: 1.66x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.88x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                                     |
| float          | 135 ms                                                                | 96.8 ms: 1.39x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.9 ms: 1.04x faster                                                    |
| regex_dna      | 257 ms                                                                | 250 ms: 1.03x faster                                                     |
| regex_compile  | 177 ms                                                                | 175 ms: 1.01x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 5.27 ms: 1.24x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 268 us: 1.37x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 391 us: 1.35x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.68 sec: 1.26x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 81.5 ms: 1.22x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.2 ms: 1.17x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 186 ms: 1.14x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                     |
| json_loads           | 30.9 us                                                               | 31.5 us: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.17x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.79 ms: 1.28x slower                                                    |
| python_startup         | 11.2 ms                                                               | 15.6 ms: 1.39x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.33x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                    |
| genshi_text    | 35.2 ms                                                               | 34.1 ms: 1.03x faster                                                    |
| genshi_xml     | 69.8 ms                                                               | 82.8 ms: 1.19x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 219 us: 3.02x faster                                                     |
| async_tree_none          | 950 ms                                                                | 468 ms: 2.03x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.54 ms: 1.97x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.18 sec: 1.94x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 597 ms: 1.90x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 769 ms: 1.66x faster                                                     |
| raytrace                 | 573 ms                                                                | 347 ms: 1.65x faster                                                     |
| logging_silent           | 222 ns                                                                | 135 ns: 1.65x faster                                                     |
| scimark_sor              | 246 ms                                                                | 155 ms: 1.59x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 39.3 us: 1.57x faster                                                    |
| richards_super           | 107 ms                                                                | 70.5 ms: 1.52x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 89.9 ms: 1.49x faster                                                    |
| scimark_lu               | 227 ms                                                                | 152 ms: 1.49x faster                                                     |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 88.7 ms: 1.44x faster                                                    |
| go                       | 264 ms                                                                | 185 ms: 1.43x faster                                                     |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                    |
| richards                 | 91.7 ms                                                               | 64.9 ms: 1.41x faster                                                    |
| chaos                    | 121 ms                                                                | 86.1 ms: 1.41x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.72 ms: 1.40x faster                                                    |
| float                    | 135 ms                                                                | 96.8 ms: 1.39x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 268 us: 1.37x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 391 us: 1.35x faster                                                     |
| deepcopy                 | 511 us                                                                | 383 us: 1.33x faster                                                     |
| comprehensions           | 33.1 us                                                               | 25.3 us: 1.31x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.19 ms: 1.30x faster                                                    |
| thrift                   | 1.26 ms                                                               | 976 us: 1.29x faster                                                     |
| coroutines               | 37.2 ms                                                               | 28.9 ms: 1.29x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.25 us: 1.29x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.62 us: 1.28x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.68 sec: 1.26x faster                                                   |
| pyflate                  | 795 ms                                                                | 643 ms: 1.24x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 21.5 ms: 1.22x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 81.5 ms: 1.22x faster                                                    |
| tornado_http             | 178 ms                                                                | 148 ms: 1.20x faster                                                     |
| spectral_norm            | 186 ms                                                                | 155 ms: 1.20x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 72.7 ms: 1.19x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.2 ms: 1.17x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.95 us: 1.16x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.37 ms: 1.16x faster                                                    |
| generators               | 68.1 ms                                                               | 58.8 ms: 1.16x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 186 ms: 1.14x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.51 sec: 1.12x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 18.8 ms: 1.09x faster                                                    |
| scimark_fft              | 500 ms                                                                | 461 ms: 1.09x faster                                                     |
| fannkuch                 | 546 ms                                                                | 505 ms: 1.08x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.14 ms: 1.07x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.51 sec: 1.05x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 10.5 ms: 1.04x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.9 ms: 1.04x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 190 ms: 1.04x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 34.1 ms: 1.03x faster                                                    |
| regex_dna                | 257 ms                                                                | 250 ms: 1.03x faster                                                     |
| json                     | 5.88 ms                                                               | 5.74 ms: 1.02x faster                                                    |
| meteor_contest           | 126 ms                                                                | 124 ms: 1.02x faster                                                     |
| regex_compile            | 177 ms                                                                | 175 ms: 1.01x faster                                                     |
| sqlglot_normalize        | 156 ms                                                                | 157 ms: 1.01x slower                                                     |
| asyncio_websockets       | 657 ms                                                                | 662 ms: 1.01x slower                                                     |
| json_loads               | 30.9 us                                                               | 31.5 us: 1.02x slower                                                    |
| 2to3                     | 381 ms                                                                | 389 ms: 1.02x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.19 sec: 1.04x slower                                                   |
| docutils                 | 3.53 sec                                                              | 3.70 sec: 1.05x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.51 sec: 1.06x slower                                                   |
| nqueens                  | 117 ms                                                                | 126 ms: 1.08x slower                                                     |
| sympy_str                | 329 ms                                                                | 362 ms: 1.10x slower                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 83.4 ms: 1.11x slower                                                    |
| sympy_expand             | 543 ms                                                                | 600 ms: 1.11x slower                                                     |
| dulwich_log              | 73.5 ms                                                               | 81.8 ms: 1.11x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.50 ms: 1.12x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 29.9 ms: 1.13x slower                                                    |
| async_generators         | 452 ms                                                                | 519 ms: 1.15x slower                                                     |
| coverage                 | 83.6 ms                                                               | 98.9 ms: 1.18x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 82.8 ms: 1.19x slower                                                    |
| sympy_sum                | 184 ms                                                                | 222 ms: 1.21x slower                                                     |
| regex_effbot             | 4.25 ms                                                               | 5.27 ms: 1.24x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.79 ms: 1.28x slower                                                    |
| python_startup           | 11.2 ms                                                               | 15.6 ms: 1.39x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.35 ms: 1.53x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.65 ms: 1.62x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.47 sec: 101.18x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.10x faster                                                             |

Benchmark hidden because not significant (3): django_template, pidigits, pylint
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.157x faster
# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.37x
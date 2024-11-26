# Results vs. 3.10.4

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: linux-aarch64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.204x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x slower
- Memory change: 1.55x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 538 ms: 1.41x slower                                                     |
| docutils       | 3.53 sec                                                              | 4.28 sec: 1.21x slower                                                   |
| html5lib       | 86.5 ms                                                               | 123 ms: 1.42x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.35x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.47 sec: 1.56x faster                                                   |
| async_tree_none         | 950 ms                                                                | 635 ms: 1.49x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 790 ms: 1.43x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 951 ms: 1.34x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.45x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 213 ms: 1.58x slower                                                     |
| nbody          | 166 ms                                                                | 280 ms: 1.69x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.40x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 271 ms: 1.05x slower                                                     |
| regex_v8       | 32.2 ms                                                               | 35.4 ms: 1.10x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.77 ms: 1.12x slower                                                    |
| regex_compile  | 177 ms                                                                | 256 ms: 1.45x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.17x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 187 ms: 1.14x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 20.2 ms: 1.21x slower                                                    |
| json_loads           | 30.9 us                                                               | 39.2 us: 1.27x slower                                                    |
| tomli_loads          | 3.36 sec                                                              | 4.28 sec: 1.27x slower                                                   |
| xml_etree_process    | 99.5 ms                                                               | 133 ms: 1.33x slower                                                     |
| xml_etree_generate   | 123 ms                                                                | 164 ms: 1.34x slower                                                     |
| unpickle_pure_python | 366 us                                                                | 567 us: 1.55x slower                                                     |
| pickle_pure_python   | 529 us                                                                | 842 us: 1.59x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.25x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.5 ms: 1.82x slower                                                    |
| python_startup         | 11.2 ms                                                               | 21.1 ms: 1.88x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.85x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 69.8 ms                                                               | 104 ms: 1.48x slower                                                     |
| mako            | 18.9 ms                                                               | 29.3 ms: 1.55x slower                                                    |
| django_template | 53.3 ms                                                               | 83.8 ms: 1.57x slower                                                    |
| genshi_text     | 35.2 ms                                                               | 56.6 ms: 1.61x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.55x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 348 us: 1.90x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.47 sec: 1.56x faster                                                   |
| async_tree_none          | 950 ms                                                                | 635 ms: 1.49x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 790 ms: 1.43x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 951 ms: 1.34x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 187 ms: 1.14x faster                                                     |
| generators               | 68.1 ms                                                               | 62.3 ms: 1.09x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 4.27 us: 1.04x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 687 ms: 1.05x slower                                                     |
| regex_dna                | 257 ms                                                                | 271 ms: 1.05x slower                                                     |
| deepcopy                 | 511 us                                                                | 547 us: 1.07x slower                                                     |
| crypto_pyaes             | 134 ms                                                                | 144 ms: 1.08x slower                                                     |
| pylint                   | 485 ms                                                                | 523 ms: 1.08x slower                                                     |
| gc_traversal             | 4.15 ms                                                               | 4.48 ms: 1.08x slower                                                    |
| pathlib                  | 26.3 ms                                                               | 28.4 ms: 1.08x slower                                                    |
| coroutines               | 37.2 ms                                                               | 40.6 ms: 1.09x slower                                                    |
| scimark_fft              | 500 ms                                                                | 549 ms: 1.10x slower                                                     |
| regex_v8                 | 32.2 ms                                                               | 35.4 ms: 1.10x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.77 ms: 1.12x slower                                                    |
| deepcopy_memo            | 61.7 us                                                               | 70.6 us: 1.14x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.93 ms: 1.17x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.65 ms: 1.17x slower                                                    |
| spectral_norm            | 186 ms                                                                | 219 ms: 1.17x slower                                                     |
| json                     | 5.88 ms                                                               | 7.01 ms: 1.19x slower                                                    |
| docutils                 | 3.53 sec                                                              | 4.28 sec: 1.21x slower                                                   |
| json_dumps               | 16.7 ms                                                               | 20.2 ms: 1.21x slower                                                    |
| mdp                      | 3.70 sec                                                              | 4.52 sec: 1.22x slower                                                   |
| pycparser                | 1.69 sec                                                              | 2.14 sec: 1.26x slower                                                   |
| json_loads               | 30.9 us                                                               | 39.2 us: 1.27x slower                                                    |
| tomli_loads              | 3.36 sec                                                              | 4.28 sec: 1.27x slower                                                   |
| comprehensions           | 33.1 us                                                               | 42.8 us: 1.29x slower                                                    |
| pyflate                  | 795 ms                                                                | 1.03 sec: 1.30x slower                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 2.07 ms: 1.30x slower                                                    |
| richards                 | 91.7 ms                                                               | 121 ms: 1.32x slower                                                     |
| logging_silent           | 222 ns                                                                | 292 ns: 1.32x slower                                                     |
| chaos                    | 121 ms                                                                | 159 ms: 1.32x slower                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 6.08 us: 1.32x slower                                                    |
| xml_etree_process        | 99.5 ms                                                               | 133 ms: 1.33x slower                                                     |
| xml_etree_generate       | 123 ms                                                                | 164 ms: 1.34x slower                                                     |
| nqueens                  | 117 ms                                                                | 159 ms: 1.35x slower                                                     |
| thrift                   | 1.26 ms                                                               | 1.72 ms: 1.36x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 36.3 ms: 1.37x slower                                                    |
| richards_super           | 107 ms                                                                | 147 ms: 1.37x slower                                                     |
| fannkuch                 | 546 ms                                                                | 751 ms: 1.38x slower                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 273 ms: 1.38x slower                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 177 ms: 1.39x slower                                                     |
| dulwich_log              | 73.5 ms                                                               | 102 ms: 1.39x slower                                                     |
| meteor_contest           | 126 ms                                                                | 177 ms: 1.41x slower                                                     |
| scimark_sor              | 246 ms                                                                | 346 ms: 1.41x slower                                                     |
| 2to3                     | 381 ms                                                                | 538 ms: 1.41x slower                                                     |
| html5lib                 | 86.5 ms                                                               | 123 ms: 1.42x slower                                                     |
| regex_compile            | 177 ms                                                                | 256 ms: 1.45x slower                                                     |
| raytrace                 | 573 ms                                                                | 835 ms: 1.46x slower                                                     |
| hexiom                   | 10.9 ms                                                               | 16.0 ms: 1.47x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 104 ms: 1.48x slower                                                     |
| deltablue                | 8.94 ms                                                               | 13.4 ms: 1.49x slower                                                    |
| sqlglot_normalize        | 156 ms                                                                | 236 ms: 1.51x slower                                                     |
| go                       | 264 ms                                                                | 402 ms: 1.52x slower                                                     |
| scimark_lu               | 227 ms                                                                | 346 ms: 1.53x slower                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 115 ms: 1.53x slower                                                     |
| pprint_pformat           | 2.36 sec                                                              | 3.61 sec: 1.53x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.76 sec: 1.53x slower                                                   |
| logging_simple           | 9.78 us                                                               | 15.0 us: 1.54x slower                                                    |
| telco                    | 8.49 ms                                                               | 13.0 ms: 1.54x slower                                                    |
| mako                     | 18.9 ms                                                               | 29.3 ms: 1.55x slower                                                    |
| unpickle_pure_python     | 366 us                                                                | 567 us: 1.55x slower                                                     |
| async_generators         | 452 ms                                                                | 703 ms: 1.55x slower                                                     |
| logging_format           | 10.6 us                                                               | 16.5 us: 1.56x slower                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 32.2 ms: 1.57x slower                                                    |
| django_template          | 53.3 ms                                                               | 83.8 ms: 1.57x slower                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 4.49 ms: 1.58x slower                                                    |
| float                    | 135 ms                                                                | 213 ms: 1.58x slower                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 3.81 ms: 1.59x slower                                                    |
| pickle_pure_python       | 529 us                                                                | 842 us: 1.59x slower                                                     |
| genshi_text              | 35.2 ms                                                               | 56.6 ms: 1.61x slower                                                    |
| sympy_str                | 329 ms                                                                | 532 ms: 1.62x slower                                                     |
| nbody                    | 166 ms                                                                | 280 ms: 1.69x slower                                                     |
| coverage                 | 83.6 ms                                                               | 142 ms: 1.70x slower                                                     |
| sympy_sum                | 184 ms                                                                | 329 ms: 1.79x slower                                                     |
| sympy_expand             | 543 ms                                                                | 988 ms: 1.82x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 12.5 ms: 1.82x slower                                                    |
| python_startup           | 11.2 ms                                                               | 21.1 ms: 1.88x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 63.5 ms: 4.37x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.31x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, pidigits
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241109-3.14.0a1+-9d08423-NOGIL/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.204x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.26x
- 95% likely to have a slowdown of 1.24x
- 99% likely to have a slowdown of 1.22x

# Memory
- memory change: 1.55x
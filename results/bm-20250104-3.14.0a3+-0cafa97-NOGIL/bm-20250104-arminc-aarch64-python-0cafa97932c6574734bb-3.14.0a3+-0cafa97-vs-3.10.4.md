# Results vs. 3.10.4

- fork: python
- ref: 0cafa97932c6574734bb
- machine: linux-aarch64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.059x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.55x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 468 ms: 1.23x slower                                                     |
| docutils       | 3.53 sec                                                              | 3.72 sec: 1.05x slower                                                   |
| html5lib       | 86.5 ms                                                               | 111 ms: 1.28x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.18x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.18 sec: 1.93x faster                                                   |
| async_tree_none         | 950 ms                                                                | 536 ms: 1.77x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 660 ms: 1.72x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 833 ms: 1.53x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.73x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 186 ms: 1.12x slower                                                     |
| float          | 135 ms                                                                | 154 ms: 1.14x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 187 ms: 1.06x slower                                                     |
| regex_dna      | 257 ms                                                                | 279 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 137 ms: 1.14x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 3.60 sec: 1.07x slower                                                   |
| xml_etree_process    | 99.5 ms                                                               | 109 ms: 1.10x slower                                                     |
| json_dumps           | 16.7 ms                                                               | 18.4 ms: 1.10x slower                                                    |
| xml_etree_generate   | 123 ms                                                                | 145 ms: 1.18x slower                                                     |
| json_loads           | 30.9 us                                                               | 37.4 us: 1.21x slower                                                    |
| unpickle_pure_python | 366 us                                                                | 453 us: 1.24x slower                                                     |
| pickle_pure_python   | 529 us                                                                | 701 us: 1.33x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.10x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.4 ms: 1.79x slower                                                    |
| python_startup         | 11.2 ms                                                               | 20.4 ms: 1.82x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.81x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 35.2 ms                                                               | 41.3 ms: 1.17x slower                                                    |
| django_template | 53.3 ms                                                               | 65.3 ms: 1.23x slower                                                    |
| genshi_xml      | 69.8 ms                                                               | 86.6 ms: 1.24x slower                                                    |
| mako            | 18.9 ms                                                               | 25.6 ms: 1.35x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.25x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 302 us: 2.19x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.18 sec: 1.93x faster                                                   |
| async_tree_none          | 950 ms                                                                | 536 ms: 1.77x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 660 ms: 1.72x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 833 ms: 1.53x faster                                                     |
| generators               | 68.1 ms                                                               | 56.1 ms: 1.21x faster                                                    |
| spectral_norm            | 186 ms                                                                | 154 ms: 1.21x faster                                                     |
| deepcopy                 | 511 us                                                                | 432 us: 1.18x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 137 ms: 1.14x faster                                                     |
| pylint                   | 485 ms                                                                | 438 ms: 1.11x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 121 ms: 1.11x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 23.9 ms: 1.10x faster                                                    |
| coroutines               | 37.2 ms                                                               | 33.8 ms: 1.10x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 56.6 us: 1.09x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.88 us: 1.06x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.73 sec: 1.02x slower                                                   |
| asyncio_websockets       | 657 ms                                                                | 682 ms: 1.04x slower                                                     |
| docutils                 | 3.53 sec                                                              | 3.72 sec: 1.05x slower                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 4.85 us: 1.06x slower                                                    |
| regex_compile            | 177 ms                                                                | 187 ms: 1.06x slower                                                     |
| richards                 | 91.7 ms                                                               | 97.6 ms: 1.06x slower                                                    |
| chaos                    | 121 ms                                                                | 129 ms: 1.07x slower                                                     |
| tomli_loads              | 3.36 sec                                                              | 3.60 sec: 1.07x slower                                                   |
| regex_dna                | 257 ms                                                                | 279 ms: 1.08x slower                                                     |
| mdp                      | 3.70 sec                                                              | 4.01 sec: 1.09x slower                                                   |
| thrift                   | 1.26 ms                                                               | 1.38 ms: 1.09x slower                                                    |
| xml_etree_process        | 99.5 ms                                                               | 109 ms: 1.10x slower                                                     |
| json_dumps               | 16.7 ms                                                               | 18.4 ms: 1.10x slower                                                    |
| json                     | 5.88 ms                                                               | 6.54 ms: 1.11x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.49 ms: 1.11x slower                                                    |
| nbody                    | 166 ms                                                                | 186 ms: 1.12x slower                                                     |
| dulwich_log              | 73.5 ms                                                               | 82.9 ms: 1.13x slower                                                    |
| sympy_sum                | 184 ms                                                                | 208 ms: 1.13x slower                                                     |
| sympy_integrate          | 26.5 ms                                                               | 30.1 ms: 1.13x slower                                                    |
| float                    | 135 ms                                                                | 154 ms: 1.14x slower                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 86.0 ms: 1.14x slower                                                    |
| pyflate                  | 795 ms                                                                | 911 ms: 1.15x slower                                                     |
| logging_simple           | 9.78 us                                                               | 11.2 us: 1.15x slower                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 227 ms: 1.15x slower                                                     |
| sqlglot_normalize        | 156 ms                                                                | 180 ms: 1.15x slower                                                     |
| logging_format           | 10.6 us                                                               | 12.3 us: 1.16x slower                                                    |
| scimark_sor              | 246 ms                                                                | 285 ms: 1.16x slower                                                     |
| comprehensions           | 33.1 us                                                               | 38.5 us: 1.16x slower                                                    |
| nqueens                  | 117 ms                                                                | 136 ms: 1.16x slower                                                     |
| raytrace                 | 573 ms                                                                | 666 ms: 1.16x slower                                                     |
| sympy_expand             | 543 ms                                                                | 635 ms: 1.17x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.34 sec: 1.17x slower                                                   |
| genshi_text              | 35.2 ms                                                               | 41.3 ms: 1.17x slower                                                    |
| logging_silent           | 222 ns                                                                | 261 ns: 1.18x slower                                                     |
| xml_etree_generate       | 123 ms                                                                | 145 ms: 1.18x slower                                                     |
| pprint_pformat           | 2.36 sec                                                              | 2.78 sec: 1.18x slower                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 154 ms: 1.21x slower                                                     |
| json_loads               | 30.9 us                                                               | 37.4 us: 1.21x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.03 ms: 1.21x slower                                                    |
| sympy_str                | 329 ms                                                                | 399 ms: 1.21x slower                                                     |
| django_template          | 53.3 ms                                                               | 65.3 ms: 1.23x slower                                                    |
| hexiom                   | 10.9 ms                                                               | 13.4 ms: 1.23x slower                                                    |
| 2to3                     | 381 ms                                                                | 468 ms: 1.23x slower                                                     |
| deltablue                | 8.94 ms                                                               | 11.1 ms: 1.24x slower                                                    |
| unpickle_pure_python     | 366 us                                                                | 453 us: 1.24x slower                                                     |
| genshi_xml               | 69.8 ms                                                               | 86.6 ms: 1.24x slower                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 25.7 ms: 1.25x slower                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 2.00 ms: 1.26x slower                                                    |
| fannkuch                 | 546 ms                                                                | 692 ms: 1.27x slower                                                     |
| create_gc_cycles         | 2.26 ms                                                               | 2.87 ms: 1.27x slower                                                    |
| meteor_contest           | 126 ms                                                                | 161 ms: 1.28x slower                                                     |
| go                       | 264 ms                                                                | 337 ms: 1.28x slower                                                     |
| html5lib                 | 86.5 ms                                                               | 111 ms: 1.28x slower                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 3.13 ms: 1.30x slower                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 3.73 ms: 1.31x slower                                                    |
| pickle_pure_python       | 529 us                                                                | 701 us: 1.33x slower                                                     |
| mako                     | 18.9 ms                                                               | 25.6 ms: 1.35x slower                                                    |
| async_generators         | 452 ms                                                                | 619 ms: 1.37x slower                                                     |
| telco                    | 8.49 ms                                                               | 12.4 ms: 1.46x slower                                                    |
| mypy2                    | 936 ms                                                                | 1.51 sec: 1.62x slower                                                   |
| coverage                 | 83.6 ms                                                               | 144 ms: 1.72x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 12.4 ms: 1.79x slower                                                    |
| python_startup           | 11.2 ms                                                               | 20.4 ms: 1.82x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 62.6 ms: 4.31x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.11x slower                                                             |

Benchmark hidden because not significant (6): regex_effbot, scimark_fft, scimark_lu, richards_super, regex_v8, pidigits
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250104-3.14.0a3+-0cafa97-NOGIL/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.059x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.55x
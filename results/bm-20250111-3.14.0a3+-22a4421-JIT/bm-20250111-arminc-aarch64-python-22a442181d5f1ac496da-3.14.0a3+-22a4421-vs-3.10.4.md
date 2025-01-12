# Results vs. 3.10.4

- fork: python
- ref: 22a442181d5f1ac496da
- machine: linux-aarch64
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.234x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 319 ms: 1.20x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.24 sec: 1.09x faster                                                   |
| html5lib       | 86.5 ms                                                               | 68.9 ms: 1.25x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.18x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 921 ms: 2.48x faster                                                     |
| async_tree_none         | 950 ms                                                                | 406 ms: 2.34x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 518 ms: 2.19x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 700 ms: 1.82x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.19x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 91.9 ms: 1.47x faster                                                    |
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 141 ms: 1.25x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.08 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 265 us: 1.38x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 403 us: 1.31x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 81.8 ms: 1.22x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 179 ms: 1.19x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.7 ms: 1.13x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.76 us: 1.03x faster                                                    |
| unpickle             | 17.5 us                                                               | 18.1 us: 1.04x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 39.0 us: 1.11x slower                                                    |
| pickle_list          | 5.24 us                                                               | 6.02 us: 1.15x slower                                                    |
| pickle               | 12.5 us                                                               | 16.1 us: 1.29x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.07x faster                                                             |

Benchmark hidden because not significant (2): xml_etree_generate, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.09 ms: 1.32x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.38x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                                    |
| django_template | 53.3 ms                                                               | 47.0 ms: 1.14x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 33.1 ms: 1.06x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 83.7 ms: 1.20x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.09x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 220 us: 3.00x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 921 ms: 2.48x faster                                                     |
| async_tree_none          | 950 ms                                                                | 406 ms: 2.34x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 518 ms: 2.19x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.42 ms: 2.02x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 700 ms: 1.82x faster                                                     |
| richards_super           | 107 ms                                                                | 62.8 ms: 1.71x faster                                                    |
| richards                 | 91.7 ms                                                               | 55.3 ms: 1.66x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 39.0 us: 1.58x faster                                                    |
| go                       | 264 ms                                                                | 168 ms: 1.57x faster                                                     |
| raytrace                 | 573 ms                                                                | 366 ms: 1.57x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 603 ms: 1.57x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.57 ms: 1.53x faster                                                    |
| scimark_sor              | 246 ms                                                                | 164 ms: 1.50x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 85.4 ms: 1.50x faster                                                    |
| logging_silent           | 222 ns                                                                | 150 ns: 1.48x faster                                                     |
| scimark_lu               | 227 ms                                                                | 154 ms: 1.47x faster                                                     |
| float                    | 135 ms                                                                | 91.9 ms: 1.47x faster                                                    |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.30 sec: 1.43x faster                                                   |
| mako                     | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.00 ms: 1.42x faster                                                    |
| pylint                   | 485 ms                                                                | 343 ms: 1.41x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 95.1 ms: 1.41x faster                                                    |
| chaos                    | 121 ms                                                                | 87.0 ms: 1.39x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 265 us: 1.38x faster                                                     |
| generators               | 68.1 ms                                                               | 50.8 ms: 1.34x faster                                                    |
| comprehensions           | 33.1 us                                                               | 24.9 us: 1.33x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 403 us: 1.31x faster                                                     |
| pyflate                  | 795 ms                                                                | 619 ms: 1.28x faster                                                     |
| deepcopy                 | 511 us                                                                | 402 us: 1.27x faster                                                     |
| spectral_norm            | 186 ms                                                                | 147 ms: 1.27x faster                                                     |
| coroutines               | 37.2 ms                                                               | 29.5 ms: 1.26x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 68.9 ms: 1.25x faster                                                    |
| regex_compile            | 177 ms                                                                | 141 ms: 1.25x faster                                                     |
| logging_format           | 10.6 us                                                               | 8.63 us: 1.23x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 161 ms: 1.23x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 81.8 ms: 1.22x faster                                                    |
| logging_simple           | 9.78 us                                                               | 8.04 us: 1.22x faster                                                    |
| thrift                   | 1.26 ms                                                               | 1.04 ms: 1.21x faster                                                    |
| 2to3                     | 381 ms                                                                | 319 ms: 1.20x faster                                                     |
| scimark_fft              | 500 ms                                                                | 420 ms: 1.19x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 179 ms: 1.19x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 17.4 ms: 1.18x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.52 ms: 1.17x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.46 sec: 1.16x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 9.47 ms: 1.15x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.00 us: 1.15x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.9 ms: 1.15x faster                                                    |
| sympy_sum                | 184 ms                                                                | 160 ms: 1.15x faster                                                     |
| django_template          | 53.3 ms                                                               | 47.0 ms: 1.14x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 23.4 ms: 1.13x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.7 ms: 1.13x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 139 ms: 1.12x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 68.9 ms: 1.09x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.24 sec: 1.09x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                     |
| sympy_str                | 329 ms                                                                | 305 ms: 1.08x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 33.1 ms: 1.06x faster                                                    |
| fannkuch                 | 546 ms                                                                | 517 ms: 1.06x faster                                                     |
| sympy_expand             | 543 ms                                                                | 518 ms: 1.05x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 70.2 ms: 1.05x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.08 ms: 1.04x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.55 sec: 1.04x faster                                                   |
| json                     | 5.88 ms                                                               | 5.67 ms: 1.04x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.76 us: 1.03x faster                                                    |
| unpickle                 | 17.5 us                                                               | 18.1 us: 1.04x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.23 sec: 1.07x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.57 sec: 1.09x slower                                                   |
| nqueens                  | 117 ms                                                                | 129 ms: 1.10x slower                                                     |
| pickle_dict              | 35.1 us                                                               | 39.0 us: 1.11x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.69 ms: 1.14x slower                                                    |
| pickle_list              | 5.24 us                                                               | 6.02 us: 1.15x slower                                                    |
| async_generators         | 452 ms                                                                | 521 ms: 1.15x slower                                                     |
| genshi_xml               | 69.8 ms                                                               | 83.7 ms: 1.20x slower                                                    |
| coverage                 | 83.6 ms                                                               | 103 ms: 1.23x slower                                                     |
| pickle                   | 12.5 us                                                               | 16.1 us: 1.29x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 9.09 ms: 1.32x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.64 ms: 1.61x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.95 ms: 1.67x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.33 sec: 91.46x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.14x faster                                                             |

Benchmark hidden because not significant (8): xml_etree_generate, meteor_contest, pidigits, regex_v8, json_loads, asyncio_websockets, sqlite_synth, regex_dna
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.234x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.32x
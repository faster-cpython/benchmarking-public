# Results vs. 3.10.4

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-aarch64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.304x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 306 ms: 1.24x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.05 sec: 1.16x faster                                                   |
| html5lib       | 86.5 ms                                                               | 64.6 ms: 1.34x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 922 ms: 2.48x faster                                                     |
| async_tree_none         | 950 ms                                                                | 401 ms: 2.37x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 512 ms: 2.21x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 686 ms: 1.86x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.22x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 97.1 ms: 1.39x faster                                                    |
| nbody          | 166 ms                                                                | 121 ms: 1.37x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.22x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 131 ms: 1.34x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.07 ms: 1.04x faster                                                    |
| regex_dna      | 257 ms                                                                | 266 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 266 us: 1.37x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 400 us: 1.32x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.70 sec: 1.24x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.8 ms: 1.13x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.08x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 115 ms: 1.07x faster                                                     |
| json_loads           | 30.9 us                                                               | 32.5 us: 1.05x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.17x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.3 ms: 1.46x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.3 ms: 1.33x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 28.1 ms: 1.25x faster                                                    |
| django_template | 53.3 ms                                                               | 42.7 ms: 1.25x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 62.2 ms: 1.12x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.24x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 209 us: 3.17x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 922 ms: 2.48x faster                                                     |
| async_tree_none          | 950 ms                                                                | 401 ms: 2.37x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.01 ms: 2.23x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 512 ms: 2.21x faster                                                     |
| generators               | 68.1 ms                                                               | 36.6 ms: 1.86x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 686 ms: 1.86x faster                                                     |
| go                       | 264 ms                                                                | 144 ms: 1.83x faster                                                     |
| raytrace                 | 573 ms                                                                | 324 ms: 1.77x faster                                                     |
| richards_super           | 107 ms                                                                | 61.7 ms: 1.74x faster                                                    |
| chaos                    | 121 ms                                                                | 73.7 ms: 1.64x faster                                                    |
| richards                 | 91.7 ms                                                               | 55.9 ms: 1.64x faster                                                    |
| scimark_lu               | 227 ms                                                                | 139 ms: 1.64x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.50 ms: 1.60x faster                                                    |
| pylint                   | 485 ms                                                                | 306 ms: 1.59x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 85.2 ms: 1.57x faster                                                    |
| logging_silent           | 222 ns                                                                | 142 ns: 1.57x faster                                                     |
| comprehensions           | 33.1 us                                                               | 21.2 us: 1.56x faster                                                    |
| scimark_sor              | 246 ms                                                                | 161 ms: 1.53x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.87 ms: 1.52x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 86.5 ms: 1.48x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.45 ms: 1.46x faster                                                    |
| deepcopy                 | 511 us                                                                | 353 us: 1.45x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 42.7 us: 1.44x faster                                                    |
| spectral_norm            | 186 ms                                                                | 130 ms: 1.43x faster                                                     |
| pyflate                  | 795 ms                                                                | 561 ms: 1.42x faster                                                     |
| float                    | 135 ms                                                                | 97.1 ms: 1.39x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 266 us: 1.37x faster                                                     |
| nbody                    | 166 ms                                                                | 121 ms: 1.37x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 145 ms: 1.36x faster                                                     |
| regex_compile            | 177 ms                                                                | 131 ms: 1.34x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.26 sec: 1.34x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 64.6 ms: 1.34x faster                                                    |
| mako                     | 18.9 ms                                                               | 14.3 ms: 1.33x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.5 ms: 1.32x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.02 us: 1.32x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 400 us: 1.32x faster                                                     |
| thrift                   | 1.26 ms                                                               | 967 us: 1.30x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.65 us: 1.28x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.2 ms: 1.27x faster                                                    |
| sympy_sum                | 184 ms                                                                | 145 ms: 1.27x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 3.65 us: 1.26x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 28.1 ms: 1.25x faster                                                    |
| django_template          | 53.3 ms                                                               | 42.7 ms: 1.25x faster                                                    |
| 2to3                     | 381 ms                                                                | 306 ms: 1.24x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.70 sec: 1.24x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.28 ms: 1.21x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.8 ms: 1.21x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 22.2 ms: 1.20x faster                                                    |
| scimark_fft              | 500 ms                                                                | 419 ms: 1.19x faster                                                     |
| sympy_str                | 329 ms                                                                | 278 ms: 1.18x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 62.3 ms: 1.18x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 132 ms: 1.18x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 64.6 ms: 1.17x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.05 sec: 1.16x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 997 ms: 1.15x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 2.05 sec: 1.15x faster                                                   |
| fannkuch                 | 546 ms                                                                | 477 ms: 1.14x faster                                                     |
| nqueens                  | 117 ms                                                                | 103 ms: 1.14x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.8 ms: 1.13x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 62.2 ms: 1.12x faster                                                    |
| sympy_expand             | 543 ms                                                                | 484 ms: 1.12x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.38 sec: 1.09x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.08x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 115 ms: 1.07x faster                                                     |
| meteor_contest           | 126 ms                                                                | 118 ms: 1.07x faster                                                     |
| json                     | 5.88 ms                                                               | 5.61 ms: 1.05x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.07 ms: 1.04x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 676 ms: 1.03x slower                                                     |
| regex_dna                | 257 ms                                                                | 266 ms: 1.03x slower                                                     |
| json_loads               | 30.9 us                                                               | 32.5 us: 1.05x slower                                                    |
| async_generators         | 452 ms                                                                | 501 ms: 1.11x slower                                                     |
| mypy2                    | 936 ms                                                                | 1.05 sec: 1.12x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.73 ms: 1.15x slower                                                    |
| coverage                 | 83.6 ms                                                               | 97.7 ms: 1.17x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.3 ms: 1.46x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.72 ms: 1.65x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.95 ms: 1.67x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 6.14 sec: 422.74x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                             |

Benchmark hidden because not significant (3): regex_v8, sqlite_synth, pidigits
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.304x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.30x
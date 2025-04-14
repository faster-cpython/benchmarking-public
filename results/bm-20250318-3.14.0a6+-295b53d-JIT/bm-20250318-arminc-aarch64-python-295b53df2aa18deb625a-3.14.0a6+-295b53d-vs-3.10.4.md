# Results vs. 3.10.4

- fork: python
- ref: 295b53df2aa18deb625a
- machine: linux-aarch64
- commit hash: 295b53d
- commit date: 2025-03-18
- overall geometric mean: 1.265x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 311 ms: 1.23x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.23 sec: 1.09x faster                                                   |
| html5lib       | 86.5 ms                                                               | 65.3 ms: 1.32x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.21x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 898 ms: 2.54x faster                                                     |
| async_tree_none         | 950 ms                                                                | 394 ms: 2.41x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 483 ms: 2.35x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 674 ms: 1.89x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.28x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.6 ms: 1.56x faster                                                    |
| nbody          | 166 ms                                                                | 129 ms: 1.28x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.38x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 28.0 ms: 1.15x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.99 ms: 1.06x faster                                                    |
| regex_dna      | 257 ms                                                                | 249 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.15x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 408 us: 1.30x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 286 us: 1.28x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 173 ms: 1.22x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 109 ms: 1.13x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.11x faster                                                     |
| json_loads           | 30.9 us                                                               | 34.0 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.19x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.46x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                    |
| django_template | 53.3 ms                                                               | 40.6 ms: 1.31x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.6 ms: 1.28x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 63.4 ms: 1.10x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.26x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 212 us: 3.12x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 898 ms: 2.54x faster                                                     |
| async_tree_none          | 950 ms                                                                | 394 ms: 2.41x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 483 ms: 2.35x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.17 ms: 2.14x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 674 ms: 1.89x faster                                                     |
| richards_super           | 107 ms                                                                | 56.8 ms: 1.89x faster                                                    |
| generators               | 68.1 ms                                                               | 36.6 ms: 1.86x faster                                                    |
| richards                 | 91.7 ms                                                               | 53.0 ms: 1.73x faster                                                    |
| raytrace                 | 573 ms                                                                | 338 ms: 1.70x faster                                                     |
| chaos                    | 121 ms                                                                | 72.5 ms: 1.67x faster                                                    |
| logging_silent           | 222 ns                                                                | 134 ns: 1.66x faster                                                     |
| scimark_sor              | 246 ms                                                                | 154 ms: 1.60x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 38.9 us: 1.59x faster                                                    |
| float                    | 135 ms                                                                | 86.6 ms: 1.56x faster                                                    |
| deepcopy                 | 511 us                                                                | 339 us: 1.51x faster                                                     |
| scimark_lu               | 227 ms                                                                | 153 ms: 1.48x faster                                                     |
| pylint                   | 485 ms                                                                | 332 ms: 1.46x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 89.3 ms: 1.43x faster                                                    |
| go                       | 264 ms                                                                | 185 ms: 1.43x faster                                                     |
| pyflate                  | 795 ms                                                                | 575 ms: 1.38x faster                                                     |
| regex_compile            | 177 ms                                                                | 128 ms: 1.38x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.15 us: 1.37x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                    |
| thrift                   | 1.26 ms                                                               | 929 us: 1.36x faster                                                     |
| spectral_norm            | 186 ms                                                                | 138 ms: 1.36x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.88 us: 1.35x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 65.3 ms: 1.32x faster                                                    |
| django_template          | 53.3 ms                                                               | 40.6 ms: 1.31x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 102 ms: 1.31x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 56.4 ms: 1.30x faster                                                    |
| comprehensions           | 33.1 us                                                               | 25.4 us: 1.30x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 152 ms: 1.30x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 408 us: 1.30x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 3.57 us: 1.29x faster                                                    |
| nbody                    | 166 ms                                                                | 129 ms: 1.28x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 286 us: 1.28x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 27.6 ms: 1.28x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 8.63 ms: 1.26x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.3 ms: 1.26x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.8 ms: 1.25x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                                    |
| sympy_sum                | 184 ms                                                                | 149 ms: 1.23x faster                                                     |
| 2to3                     | 381 ms                                                                | 311 ms: 1.23x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 173 ms: 1.22x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 22.0 ms: 1.21x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.42 sec: 1.19x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                    |
| sympy_str                | 329 ms                                                                | 279 ms: 1.18x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 22.5 ms: 1.17x faster                                                    |
| scimark_fft              | 500 ms                                                                | 431 ms: 1.16x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 28.0 ms: 1.15x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 109 ms: 1.13x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.11x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.35 sec: 1.10x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 63.4 ms: 1.10x faster                                                    |
| nqueens                  | 117 ms                                                                | 107 ms: 1.10x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.23 sec: 1.09x faster                                                   |
| sympy_expand             | 543 ms                                                                | 509 ms: 1.07x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 3.99 ms: 1.06x faster                                                    |
| fannkuch                 | 546 ms                                                                | 515 ms: 1.06x faster                                                     |
| regex_dna                | 257 ms                                                                | 249 ms: 1.03x faster                                                     |
| meteor_contest           | 126 ms                                                                | 122 ms: 1.03x faster                                                     |
| json                     | 5.88 ms                                                               | 5.81 ms: 1.01x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 666 ms: 1.01x slower                                                     |
| async_generators         | 452 ms                                                                | 488 ms: 1.08x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.25 sec: 1.09x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.59 sec: 1.10x slower                                                   |
| json_loads               | 30.9 us                                                               | 34.0 us: 1.10x slower                                                    |
| coverage                 | 83.6 ms                                                               | 97.5 ms: 1.17x slower                                                    |
| telco                    | 8.49 ms                                                               | 10.1 ms: 1.19x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.77 ms: 1.63x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.77 ms: 1.67x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.88 sec: 129.44x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.18x faster                                                             |

Benchmark hidden because not significant (3): scimark_sparse_mat_mult, sqlite_synth, pidigits
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250318-3.14.0a6+-295b53d-JIT/bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.265x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.33x
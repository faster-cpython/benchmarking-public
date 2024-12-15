# Results vs. 3.10.4

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-aarch64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.226x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 319 ms: 1.20x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.18 sec: 1.11x faster                                                   |
| html5lib       | 86.5 ms                                                               | 71.4 ms: 1.21x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.17x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 938 ms: 2.44x faster                                                     |
| async_tree_none         | 950 ms                                                                | 409 ms: 2.32x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 524 ms: 2.16x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 702 ms: 1.81x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.17x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 95.1 ms: 1.42x faster                                                    |
| nbody          | 166 ms                                                                | 118 ms: 1.40x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 145 ms: 1.22x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 3.98 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 267 us: 1.37x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.52 sec: 1.33x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 416 us: 1.27x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 81.3 ms: 1.22x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.08x faster                                                     |
| json_loads           | 30.9 us                                                               | 32.7 us: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.3 ms: 1.46x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.38x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                    |
| django_template | 53.3 ms                                                               | 49.1 ms: 1.09x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 80.3 ms: 1.15x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.07x faster                                                             |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 222 us: 2.98x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 938 ms: 2.44x faster                                                     |
| async_tree_none          | 950 ms                                                                | 409 ms: 2.32x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 524 ms: 2.16x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.30 ms: 2.08x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 702 ms: 1.81x faster                                                     |
| richards_super           | 107 ms                                                                | 64.6 ms: 1.66x faster                                                    |
| richards                 | 91.7 ms                                                               | 55.8 ms: 1.64x faster                                                    |
| raytrace                 | 573 ms                                                                | 363 ms: 1.58x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 40.1 us: 1.54x faster                                                    |
| go                       | 264 ms                                                                | 172 ms: 1.54x faster                                                     |
| scimark_sor              | 246 ms                                                                | 160 ms: 1.54x faster                                                     |
| logging_silent           | 222 ns                                                                | 145 ns: 1.53x faster                                                     |
| scimark_lu               | 227 ms                                                                | 149 ms: 1.53x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.59 ms: 1.52x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 85.8 ms: 1.49x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 92.9 ms: 1.44x faster                                                    |
| chaos                    | 121 ms                                                                | 84.6 ms: 1.43x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.00 ms: 1.42x faster                                                    |
| float                    | 135 ms                                                                | 95.1 ms: 1.42x faster                                                    |
| nbody                    | 166 ms                                                                | 118 ms: 1.40x faster                                                     |
| generators               | 68.1 ms                                                               | 49.7 ms: 1.37x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 267 us: 1.37x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 147 ms: 1.34x faster                                                     |
| mako                     | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.52 sec: 1.33x faster                                                   |
| deepcopy                 | 511 us                                                                | 383 us: 1.33x faster                                                     |
| pylint                   | 485 ms                                                                | 365 ms: 1.33x faster                                                     |
| pyflate                  | 795 ms                                                                | 603 ms: 1.32x faster                                                     |
| comprehensions           | 33.1 us                                                               | 25.5 us: 1.30x faster                                                    |
| spectral_norm            | 186 ms                                                                | 146 ms: 1.27x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 416 us: 1.27x faster                                                     |
| coroutines               | 37.2 ms                                                               | 29.6 ms: 1.26x faster                                                    |
| thrift                   | 1.26 ms                                                               | 1.02 ms: 1.24x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.92 us: 1.23x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 81.3 ms: 1.22x faster                                                    |
| regex_compile            | 177 ms                                                                | 145 ms: 1.22x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 71.4 ms: 1.21x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.79 us: 1.21x faster                                                    |
| 2to3                     | 381 ms                                                                | 319 ms: 1.20x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 17.4 ms: 1.18x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 9.28 ms: 1.18x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.44 sec: 1.18x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| scimark_fft              | 500 ms                                                                | 427 ms: 1.17x faster                                                     |
| sympy_sum                | 184 ms                                                                | 159 ms: 1.16x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 23.0 ms: 1.16x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.40 ms: 1.14x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.05 us: 1.14x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 140 ms: 1.11x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.18 sec: 1.11x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.95 ms: 1.10x faster                                                    |
| sympy_str                | 329 ms                                                                | 300 ms: 1.10x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 24.1 ms: 1.09x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                     |
| django_template          | 53.3 ms                                                               | 49.1 ms: 1.09x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 69.4 ms: 1.09x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.08x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 3.98 ms: 1.07x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 70.0 ms: 1.05x faster                                                    |
| sympy_expand             | 543 ms                                                                | 517 ms: 1.05x faster                                                     |
| fannkuch                 | 546 ms                                                                | 522 ms: 1.05x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.58 sec: 1.03x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 681 ms: 1.04x slower                                                     |
| json_loads               | 30.9 us                                                               | 32.7 us: 1.06x slower                                                    |
| nqueens                  | 117 ms                                                                | 131 ms: 1.12x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.31 sec: 1.14x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.69 sec: 1.14x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 80.3 ms: 1.15x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.82 ms: 1.16x slower                                                    |
| mypy2                    | 936 ms                                                                | 1.08 sec: 1.16x slower                                                   |
| async_generators         | 452 ms                                                                | 540 ms: 1.19x slower                                                     |
| coverage                 | 83.6 ms                                                               | 100 ms: 1.20x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.3 ms: 1.46x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.62 ms: 1.60x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.80 ms: 1.64x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.51 sec: 104.11x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.13x faster                                                             |

Benchmark hidden because not significant (7): genshi_text, meteor_contest, sqlite_synth, json, regex_v8, regex_dna, pidigits
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.226x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.33x
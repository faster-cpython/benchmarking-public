# Results vs. 3.10.4

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-aarch64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.109x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 1.55x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 472 ms: 1.24x slower                                                     |
| docutils       | 3.53 sec                                                              | 3.83 sec: 1.08x slower                                                   |
| html5lib       | 86.5 ms                                                               | 117 ms: 1.35x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.22x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.30 sec: 1.76x faster                                                   |
| async_tree_none         | 950 ms                                                                | 587 ms: 1.62x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 735 ms: 1.54x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 895 ms: 1.42x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.58x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 193 ms: 1.16x slower                                                     |
| float          | 135 ms                                                                | 194 ms: 1.44x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.19x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 33.9 ms: 1.05x slower                                                    |
| regex_dna      | 257 ms                                                                | 273 ms: 1.06x slower                                                     |
| regex_compile  | 177 ms                                                                | 201 ms: 1.14x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 183 ms: 1.15x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 138 ms: 1.13x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 3.59 sec: 1.07x slower                                                   |
| json_dumps           | 16.7 ms                                                               | 18.8 ms: 1.12x slower                                                    |
| xml_etree_process    | 99.5 ms                                                               | 113 ms: 1.14x slower                                                     |
| xml_etree_generate   | 123 ms                                                                | 144 ms: 1.17x slower                                                     |
| json_loads           | 30.9 us                                                               | 36.8 us: 1.19x slower                                                    |
| unpickle_pure_python | 366 us                                                                | 460 us: 1.26x slower                                                     |
| pickle_pure_python   | 529 us                                                                | 702 us: 1.33x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.10x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.7 ms: 1.84x slower                                                    |
| python_startup         | 11.2 ms                                                               | 21.5 ms: 1.92x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.88x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 35.2 ms                                                               | 42.4 ms: 1.20x slower                                                    |
| genshi_xml      | 69.8 ms                                                               | 85.6 ms: 1.23x slower                                                    |
| django_template | 53.3 ms                                                               | 66.9 ms: 1.25x slower                                                    |
| mako            | 18.9 ms                                                               | 25.7 ms: 1.36x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.26x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 305 us: 2.17x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.30 sec: 1.76x faster                                                   |
| async_tree_none          | 950 ms                                                                | 587 ms: 1.62x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 735 ms: 1.54x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 895 ms: 1.42x faster                                                     |
| generators               | 68.1 ms                                                               | 56.6 ms: 1.20x faster                                                    |
| spectral_norm            | 186 ms                                                                | 160 ms: 1.17x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 183 ms: 1.15x faster                                                     |
| deepcopy                 | 511 us                                                                | 444 us: 1.15x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 138 ms: 1.13x faster                                                     |
| coroutines               | 37.2 ms                                                               | 33.8 ms: 1.10x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 123 ms: 1.09x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 24.8 ms: 1.06x faster                                                    |
| pylint                   | 485 ms                                                                | 463 ms: 1.05x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 33.9 ms: 1.05x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 696 ms: 1.06x slower                                                     |
| regex_dna                | 257 ms                                                                | 273 ms: 1.06x slower                                                     |
| tomli_loads              | 3.36 sec                                                              | 3.59 sec: 1.07x slower                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.17 ms: 1.07x slower                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.94 us: 1.08x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.83 sec: 1.08x slower                                                   |
| mdp                      | 3.70 sec                                                              | 4.09 sec: 1.11x slower                                                   |
| json                     | 5.88 ms                                                               | 6.57 ms: 1.12x slower                                                    |
| json_dumps               | 16.7 ms                                                               | 18.8 ms: 1.12x slower                                                    |
| richards_super           | 107 ms                                                                | 121 ms: 1.12x slower                                                     |
| xml_etree_process        | 99.5 ms                                                               | 113 ms: 1.14x slower                                                     |
| regex_compile            | 177 ms                                                                | 201 ms: 1.14x slower                                                     |
| pycparser                | 1.69 sec                                                              | 1.95 sec: 1.15x slower                                                   |
| nbody                    | 166 ms                                                                | 193 ms: 1.16x slower                                                     |
| pyflate                  | 795 ms                                                                | 925 ms: 1.16x slower                                                     |
| nqueens                  | 117 ms                                                                | 137 ms: 1.17x slower                                                     |
| chaos                    | 121 ms                                                                | 142 ms: 1.17x slower                                                     |
| xml_etree_generate       | 123 ms                                                                | 144 ms: 1.17x slower                                                     |
| comprehensions           | 33.1 us                                                               | 38.9 us: 1.17x slower                                                    |
| scimark_lu               | 227 ms                                                                | 268 ms: 1.18x slower                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 89.1 ms: 1.18x slower                                                    |
| json_loads               | 30.9 us                                                               | 36.8 us: 1.19x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.38 sec: 1.20x slower                                                   |
| genshi_text              | 35.2 ms                                                               | 42.4 ms: 1.20x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.84 sec: 1.21x slower                                                   |
| sqlglot_normalize        | 156 ms                                                                | 189 ms: 1.21x slower                                                     |
| gc_traversal             | 4.15 ms                                                               | 5.03 ms: 1.21x slower                                                    |
| logging_silent           | 222 ns                                                                | 270 ns: 1.22x slower                                                     |
| logging_simple           | 9.78 us                                                               | 12.0 us: 1.23x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 85.6 ms: 1.23x slower                                                    |
| 2to3                     | 381 ms                                                                | 472 ms: 1.24x slower                                                     |
| dulwich_log              | 73.5 ms                                                               | 91.1 ms: 1.24x slower                                                    |
| meteor_contest           | 126 ms                                                                | 158 ms: 1.25x slower                                                     |
| sympy_integrate          | 26.5 ms                                                               | 33.2 ms: 1.25x slower                                                    |
| hexiom                   | 10.9 ms                                                               | 13.7 ms: 1.25x slower                                                    |
| django_template          | 53.3 ms                                                               | 66.9 ms: 1.25x slower                                                    |
| unpickle_pure_python     | 366 us                                                                | 460 us: 1.26x slower                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 248 ms: 1.26x slower                                                     |
| logging_format           | 10.6 us                                                               | 13.3 us: 1.26x slower                                                    |
| richards                 | 91.7 ms                                                               | 115 ms: 1.26x slower                                                     |
| scimark_sor              | 246 ms                                                                | 313 ms: 1.27x slower                                                     |
| thrift                   | 1.26 ms                                                               | 1.61 ms: 1.27x slower                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 2.03 ms: 1.28x slower                                                    |
| fannkuch                 | 546 ms                                                                | 698 ms: 1.28x slower                                                     |
| raytrace                 | 573 ms                                                                | 739 ms: 1.29x slower                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 166 ms: 1.30x slower                                                     |
| create_gc_cycles         | 2.26 ms                                                               | 2.95 ms: 1.30x slower                                                    |
| pickle_pure_python       | 529 us                                                                | 702 us: 1.33x slower                                                     |
| html5lib                 | 86.5 ms                                                               | 117 ms: 1.35x slower                                                     |
| mako                     | 18.9 ms                                                               | 25.7 ms: 1.36x slower                                                    |
| deltablue                | 8.94 ms                                                               | 12.2 ms: 1.37x slower                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 28.4 ms: 1.39x slower                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 3.34 ms: 1.39x slower                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 3.97 ms: 1.40x slower                                                    |
| async_generators         | 452 ms                                                                | 635 ms: 1.40x slower                                                     |
| sympy_str                | 329 ms                                                                | 465 ms: 1.42x slower                                                     |
| telco                    | 8.49 ms                                                               | 12.1 ms: 1.42x slower                                                    |
| go                       | 264 ms                                                                | 378 ms: 1.43x slower                                                     |
| float                    | 135 ms                                                                | 194 ms: 1.44x slower                                                     |
| sympy_sum                | 184 ms                                                                | 293 ms: 1.59x slower                                                     |
| sympy_expand             | 543 ms                                                                | 873 ms: 1.61x slower                                                     |
| mypy2                    | 936 ms                                                                | 1.65 sec: 1.76x slower                                                   |
| coverage                 | 83.6 ms                                                               | 147 ms: 1.76x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 12.7 ms: 1.84x slower                                                    |
| python_startup           | 11.2 ms                                                               | 21.5 ms: 1.92x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 62.8 ms: 4.32x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.17x slower                                                             |

Benchmark hidden because not significant (5): deepcopy_memo, sqlite_synth, pidigits, scimark_fft, regex_effbot
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.109x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 1.55x
# Results vs. 3.10.4

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: linux-aarch64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.371x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 288 ms: 1.32x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.90 sec: 1.22x faster                                                   |
| html5lib       | 86.5 ms                                                               | 59.5 ms: 1.45x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.33x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 884 ms: 2.58x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 455 ms: 2.49x faster                                                     |
| async_tree_none         | 950 ms                                                                | 387 ms: 2.45x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 721 ms: 1.76x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.30x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 84.1 ms: 1.60x faster                                                    |
| nbody          | 166 ms                                                                | 124 ms: 1.33x faster                                                     |
| pidigits       | 235 ms                                                                | 294 ms: 1.25x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 124 ms: 1.43x faster                                                     |
| regex_dna      | 257 ms                                                                | 239 ms: 1.08x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 30.1 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 249 us: 1.47x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.32 sec: 1.45x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 371 us: 1.43x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 74.0 ms: 1.35x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 104 ms: 1.19x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.2 ms: 1.18x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 151 ms: 1.03x faster                                                     |
| json_loads           | 30.9 us                                                               | 33.2 us: 1.07x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.21x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.46x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 38.4 ms: 1.39x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 25.5 ms: 1.38x faster                                                    |
| mako            | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 57.8 ms: 1.21x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.34x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 184 us: 3.59x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 884 ms: 2.58x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 455 ms: 2.49x faster                                                     |
| async_tree_none          | 950 ms                                                                | 387 ms: 2.45x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.75 ms: 2.39x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.61 sec: 2.30x faster                                                   |
| go                       | 264 ms                                                                | 129 ms: 2.05x faster                                                     |
| richards_super           | 107 ms                                                                | 54.3 ms: 1.98x faster                                                    |
| logging_silent           | 222 ns                                                                | 113 ns: 1.97x faster                                                     |
| generators               | 68.1 ms                                                               | 35.4 ms: 1.92x faster                                                    |
| richards                 | 91.7 ms                                                               | 48.6 ms: 1.89x faster                                                    |
| chaos                    | 121 ms                                                                | 65.8 ms: 1.84x faster                                                    |
| raytrace                 | 573 ms                                                                | 313 ms: 1.83x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 721 ms: 1.76x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 35.4 us: 1.74x faster                                                    |
| scimark_sor              | 246 ms                                                                | 143 ms: 1.72x faster                                                     |
| comprehensions           | 33.1 us                                                               | 19.8 us: 1.67x faster                                                    |
| deepcopy                 | 511 us                                                                | 311 us: 1.64x faster                                                     |
| pylint                   | 485 ms                                                                | 301 ms: 1.61x faster                                                     |
| scimark_lu               | 227 ms                                                                | 141 ms: 1.61x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 79.7 ms: 1.60x faster                                                    |
| float                    | 135 ms                                                                | 84.1 ms: 1.60x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 84.8 ms: 1.58x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 6.99 ms: 1.56x faster                                                    |
| spectral_norm            | 186 ms                                                                | 120 ms: 1.55x faster                                                     |
| pyflate                  | 795 ms                                                                | 520 ms: 1.53x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 249 us: 1.47x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 59.5 ms: 1.45x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.32 sec: 1.45x faster                                                   |
| logging_simple           | 9.78 us                                                               | 6.82 us: 1.43x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 51.3 ms: 1.43x faster                                                    |
| regex_compile            | 177 ms                                                                | 124 ms: 1.43x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 371 us: 1.43x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.44 us: 1.43x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.25 us: 1.42x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.20 sec: 1.41x faster                                                   |
| django_template          | 53.3 ms                                                               | 38.4 ms: 1.39x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 25.5 ms: 1.38x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 74.0 ms: 1.35x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 147 ms: 1.34x faster                                                     |
| nbody                    | 166 ms                                                                | 124 ms: 1.33x faster                                                     |
| coroutines               | 37.2 ms                                                               | 27.9 ms: 1.33x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.0 ms: 1.33x faster                                                    |
| 2to3                     | 381 ms                                                                | 288 ms: 1.32x faster                                                     |
| sympy_sum                | 184 ms                                                                | 141 ms: 1.30x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.9 ms: 1.29x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 902 ms: 1.27x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 1.86 sec: 1.27x faster                                                   |
| sympy_str                | 329 ms                                                                | 260 ms: 1.26x faster                                                     |
| scimark_fft              | 500 ms                                                                | 397 ms: 1.26x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 21.6 ms: 1.22x faster                                                    |
| docutils                 | 3.53 sec                                                              | 2.90 sec: 1.22x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 57.8 ms: 1.21x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.20x faster                                                    |
| sympy_expand             | 543 ms                                                                | 453 ms: 1.20x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 104 ms: 1.19x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.2 ms: 1.18x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.48 ms: 1.18x faster                                                    |
| nqueens                  | 117 ms                                                                | 101 ms: 1.17x faster                                                     |
| fannkuch                 | 546 ms                                                                | 484 ms: 1.13x faster                                                     |
| async_generators         | 452 ms                                                                | 409 ms: 1.11x faster                                                     |
| meteor_contest           | 126 ms                                                                | 114 ms: 1.10x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.76 us: 1.09x faster                                                    |
| regex_dna                | 257 ms                                                                | 239 ms: 1.08x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 30.1 ms: 1.07x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 151 ms: 1.03x faster                                                     |
| json                     | 5.88 ms                                                               | 5.79 ms: 1.02x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 671 ms: 1.02x slower                                                     |
| json_loads               | 30.9 us                                                               | 33.2 us: 1.07x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.44 ms: 1.11x slower                                                    |
| coverage                 | 83.6 ms                                                               | 95.0 ms: 1.14x slower                                                    |
| pidigits                 | 235 ms                                                                | 294 ms: 1.25x slower                                                     |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.53 ms: 1.56x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.52 ms: 1.57x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 2.23 sec: 153.34x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.27x faster                                                             |

Benchmark hidden because not significant (2): xml_etree_parse, regex_effbot
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-275056a-CLANG/bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.371x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.36x
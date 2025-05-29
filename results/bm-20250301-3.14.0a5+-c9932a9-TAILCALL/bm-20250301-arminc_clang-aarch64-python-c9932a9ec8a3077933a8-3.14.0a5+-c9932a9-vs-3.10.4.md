# Results vs. 3.10.4

- fork: python
- ref: c9932a9ec8a3077933a8
- machine: linux-aarch64
- commit hash: c9932a9
- commit date: 2025-03-01
- overall geometric mean: 1.353x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 303 ms: 1.26x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                   |
| html5lib       | 86.5 ms                                                               | 60.4 ms: 1.43x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 371 ms: 2.56x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 900 ms: 2.54x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 478 ms: 2.37x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 749 ms: 1.70x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.26x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 90.9 ms: 1.48x faster                                                    |
| nbody          | 166 ms                                                                | 116 ms: 1.43x faster                                                     |
| pidigits       | 235 ms                                                                | 293 ms: 1.25x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.19x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.41x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 34.4 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                             |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 265 us: 1.38x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 399 us: 1.33x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 76.3 ms: 1.30x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 5.89 us: 1.19x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 106 ms: 1.16x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.7 ms: 1.13x faster                                                    |
| pickle_dict          | 35.1 us                                                               | 37.2 us: 1.06x slower                                                    |
| pickle_list          | 5.24 us                                                               | 5.56 us: 1.06x slower                                                    |
| json_loads           | 30.9 us                                                               | 33.6 us: 1.09x slower                                                    |
| pickle               | 12.5 us                                                               | 15.0 us: 1.20x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                             |

Benchmark hidden because not significant (3): xml_etree_iterparse, unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.29 ms: 1.35x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.5 ms: 1.47x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.41x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 37.7 ms: 1.42x faster                                                    |
| mako            | 18.9 ms                                                               | 14.0 ms: 1.36x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 26.8 ms: 1.31x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 61.0 ms: 1.14x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.30x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 190 us: 3.48x faster                                                     |
| async_tree_none          | 950 ms                                                                | 371 ms: 2.56x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 900 ms: 2.54x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 478 ms: 2.37x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.93 ms: 2.28x faster                                                    |
| go                       | 264 ms                                                                | 135 ms: 1.96x faster                                                     |
| richards                 | 91.7 ms                                                               | 48.9 ms: 1.87x faster                                                    |
| logging_silent           | 222 ns                                                                | 119 ns: 1.87x faster                                                     |
| raytrace                 | 573 ms                                                                | 311 ms: 1.84x faster                                                     |
| richards_super           | 107 ms                                                                | 58.5 ms: 1.83x faster                                                    |
| generators               | 68.1 ms                                                               | 37.4 ms: 1.82x faster                                                    |
| chaos                    | 121 ms                                                                | 67.7 ms: 1.79x faster                                                    |
| scimark_sor              | 246 ms                                                                | 142 ms: 1.73x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.39 ms: 1.72x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 749 ms: 1.70x faster                                                     |
| comprehensions           | 33.1 us                                                               | 19.7 us: 1.68x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.70 ms: 1.67x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.0 us: 1.67x faster                                                    |
| spectral_norm            | 186 ms                                                                | 112 ms: 1.66x faster                                                     |
| scimark_lu               | 227 ms                                                                | 138 ms: 1.64x faster                                                     |
| pylint                   | 485 ms                                                                | 297 ms: 1.64x faster                                                     |
| deepcopy                 | 511 us                                                                | 313 us: 1.63x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 591 ms: 1.60x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 80.3 ms: 1.59x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 86.0 ms: 1.56x faster                                                    |
| float                    | 135 ms                                                                | 90.9 ms: 1.48x faster                                                    |
| pyflate                  | 795 ms                                                                | 537 ms: 1.48x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 7.41 ms: 1.47x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 60.4 ms: 1.43x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.29 sec: 1.43x faster                                                   |
| nbody                    | 166 ms                                                                | 116 ms: 1.43x faster                                                     |
| logging_simple           | 9.78 us                                                               | 6.90 us: 1.42x faster                                                    |
| django_template          | 53.3 ms                                                               | 37.7 ms: 1.42x faster                                                    |
| regex_compile            | 177 ms                                                                | 125 ms: 1.41x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.69 us: 1.38x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 265 us: 1.38x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 3.35 us: 1.37x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                                   |
| thrift                   | 1.26 ms                                                               | 921 us: 1.37x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.1 ms: 1.36x faster                                                    |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.36x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 146 ms: 1.35x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.26 sec: 1.34x faster                                                   |
| sympy_sum                | 184 ms                                                                | 138 ms: 1.33x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 399 us: 1.33x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 26.8 ms: 1.31x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.3 ms: 1.31x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 76.3 ms: 1.30x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.7 ms: 1.29x faster                                                    |
| scimark_fft              | 500 ms                                                                | 388 ms: 1.29x faster                                                     |
| 2to3                     | 381 ms                                                                | 303 ms: 1.26x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.07 ms: 1.26x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.28 ms: 1.24x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 59.2 ms: 1.24x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 126 ms: 1.24x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 21.3 ms: 1.23x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 937 ms: 1.22x faster                                                     |
| sympy_str                | 329 ms                                                                | 271 ms: 1.21x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 62.2 ms: 1.21x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.95 sec: 1.21x faster                                                   |
| sympy_expand             | 543 ms                                                                | 456 ms: 1.19x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 5.89 us: 1.19x faster                                                    |
| nqueens                  | 117 ms                                                                | 99.1 ms: 1.18x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 106 ms: 1.16x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 61.0 ms: 1.14x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.24 sec: 1.14x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 14.7 ms: 1.13x faster                                                    |
| fannkuch                 | 546 ms                                                                | 495 ms: 1.10x faster                                                     |
| async_generators         | 452 ms                                                                | 417 ms: 1.09x faster                                                     |
| asyncio_websockets       | 657 ms                                                                | 676 ms: 1.03x slower                                                     |
| pickle_dict              | 35.1 us                                                               | 37.2 us: 1.06x slower                                                    |
| pickle_list              | 5.24 us                                                               | 5.56 us: 1.06x slower                                                    |
| regex_v8                 | 32.2 ms                                                               | 34.4 ms: 1.07x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.13 ms: 1.08x slower                                                    |
| json_loads               | 30.9 us                                                               | 33.6 us: 1.09x slower                                                    |
| coverage                 | 83.6 ms                                                               | 96.4 ms: 1.15x slower                                                    |
| pickle                   | 12.5 us                                                               | 15.0 us: 1.20x slower                                                    |
| pidigits                 | 235 ms                                                                | 293 ms: 1.25x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 9.29 ms: 1.35x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.5 ms: 1.47x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.72 ms: 1.62x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.69 ms: 1.63x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 3.26 sec: 224.43x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.23x faster                                                             |

Benchmark hidden because not significant (8): meteor_contest, xml_etree_iterparse, sqlite_synth, unpickle, xml_etree_parse, regex_dna, regex_effbot, json
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250301-3.14.0a5+-c9932a9-CLANG/bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.353x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.35x
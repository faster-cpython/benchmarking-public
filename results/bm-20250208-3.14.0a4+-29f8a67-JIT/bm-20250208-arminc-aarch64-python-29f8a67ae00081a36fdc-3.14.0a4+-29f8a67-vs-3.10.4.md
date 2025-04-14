# Results vs. 3.10.4

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-aarch64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.273x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 318 ms: 1.20x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.27 sec: 1.08x faster                                                   |
| html5lib       | 86.5 ms                                                               | 63.9 ms: 1.35x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 958 ms: 2.38x faster                                                     |
| async_tree_none         | 950 ms                                                                | 402 ms: 2.36x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 505 ms: 2.24x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 698 ms: 1.82x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.19x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 84.1 ms: 1.60x faster                                                    |
| nbody          | 166 ms                                                                | 129 ms: 1.28x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 132 ms: 1.34x faster                                                     |
| regex_dna      | 257 ms                                                                | 250 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                             |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 273 us: 1.34x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.52 sec: 1.33x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 415 us: 1.28x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 80.4 ms: 1.24x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 183 ms: 1.16x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.8 ms: 1.13x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.11x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.39 us: 1.09x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 147 ms: 1.06x faster                                                     |
| json_loads           | 30.9 us                                                               | 35.8 us: 1.16x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 41.0 us: 1.17x slower                                                    |
| pickle_list          | 5.24 us                                                               | 6.16 us: 1.18x slower                                                    |
| pickle               | 12.5 us                                                               | 16.3 us: 1.31x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.00 ms: 1.31x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.4 ms: 1.46x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.38x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                    |
| django_template | 53.3 ms                                                               | 40.0 ms: 1.33x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 28.8 ms: 1.22x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 65.1 ms: 1.07x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.24x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 215 us: 3.08x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 958 ms: 2.38x faster                                                     |
| async_tree_none          | 950 ms                                                                | 402 ms: 2.36x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 505 ms: 2.24x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.27 ms: 2.10x faster                                                    |
| generators               | 68.1 ms                                                               | 37.1 ms: 1.83x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 698 ms: 1.82x faster                                                     |
| richards_super           | 107 ms                                                                | 61.6 ms: 1.74x faster                                                    |
| raytrace                 | 573 ms                                                                | 335 ms: 1.71x faster                                                     |
| richards                 | 91.7 ms                                                               | 53.8 ms: 1.70x faster                                                    |
| chaos                    | 121 ms                                                                | 71.1 ms: 1.70x faster                                                    |
| logging_silent           | 222 ns                                                                | 133 ns: 1.67x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 569 ms: 1.66x faster                                                     |
| scimark_lu               | 227 ms                                                                | 138 ms: 1.64x faster                                                     |
| float                    | 135 ms                                                                | 84.1 ms: 1.60x faster                                                    |
| scimark_sor              | 246 ms                                                                | 155 ms: 1.59x faster                                                     |
| go                       | 264 ms                                                                | 167 ms: 1.58x faster                                                     |
| spectral_norm            | 186 ms                                                                | 119 ms: 1.57x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.55 ms: 1.55x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 40.1 us: 1.54x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 84.8 ms: 1.51x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.90 ms: 1.50x faster                                                    |
| pylint                   | 485 ms                                                                | 333 ms: 1.46x faster                                                     |
| deepcopy                 | 511 us                                                                | 353 us: 1.45x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.27 sec: 1.45x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 95.2 ms: 1.41x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                    |
| pyflate                  | 795 ms                                                                | 587 ms: 1.35x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 63.9 ms: 1.35x faster                                                    |
| comprehensions           | 33.1 us                                                               | 24.6 us: 1.35x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 273 us: 1.34x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.93 us: 1.34x faster                                                    |
| regex_compile            | 177 ms                                                                | 132 ms: 1.34x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.32 us: 1.34x faster                                                    |
| django_template          | 53.3 ms                                                               | 40.0 ms: 1.33x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.52 sec: 1.33x faster                                                   |
| thrift                   | 1.26 ms                                                               | 967 us: 1.30x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 3.56 us: 1.29x faster                                                    |
| nbody                    | 166 ms                                                                | 129 ms: 1.28x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 155 ms: 1.28x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 415 us: 1.28x faster                                                     |
| coroutines               | 37.2 ms                                                               | 29.3 ms: 1.27x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 80.4 ms: 1.24x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 28.8 ms: 1.22x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 9.10 ms: 1.20x faster                                                    |
| 2to3                     | 381 ms                                                                | 318 ms: 1.20x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 17.1 ms: 1.20x faster                                                    |
| scimark_fft              | 500 ms                                                                | 423 ms: 1.18x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 22.5 ms: 1.18x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.44 sec: 1.17x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 133 ms: 1.17x faster                                                     |
| sympy_sum                | 184 ms                                                                | 158 ms: 1.17x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 22.6 ms: 1.17x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 183 ms: 1.16x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.39 ms: 1.14x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 66.0 ms: 1.14x faster                                                    |
| sympy_str                | 329 ms                                                                | 288 ms: 1.14x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.8 ms: 1.13x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.79 ms: 1.12x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.11x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 6.39 us: 1.09x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.27 sec: 1.08x faster                                                   |
| sympy_expand             | 543 ms                                                                | 503 ms: 1.08x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 68.4 ms: 1.07x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 65.1 ms: 1.07x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 147 ms: 1.06x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.55 sec: 1.04x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.99 us: 1.03x faster                                                    |
| regex_dna                | 257 ms                                                                | 250 ms: 1.03x faster                                                     |
| json                     | 5.88 ms                                                               | 6.22 ms: 1.06x slower                                                    |
| async_generators         | 452 ms                                                                | 483 ms: 1.07x slower                                                     |
| nqueens                  | 117 ms                                                                | 126 ms: 1.07x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.31 sec: 1.14x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.70 sec: 1.14x slower                                                   |
| json_loads               | 30.9 us                                                               | 35.8 us: 1.16x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 41.0 us: 1.17x slower                                                    |
| coverage                 | 83.6 ms                                                               | 98.1 ms: 1.17x slower                                                    |
| pickle_list              | 5.24 us                                                               | 6.16 us: 1.18x slower                                                    |
| telco                    | 8.49 ms                                                               | 10.0 ms: 1.18x slower                                                    |
| pickle                   | 12.5 us                                                               | 16.3 us: 1.31x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 9.00 ms: 1.31x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.4 ms: 1.46x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.54 ms: 1.57x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.75 ms: 1.62x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 2.46 sec: 169.25x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.16x faster                                                             |

Benchmark hidden because not significant (7): regex_effbot, fannkuch, regex_v8, meteor_contest, asyncio_websockets, pidigits, unpickle
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.273x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.32x
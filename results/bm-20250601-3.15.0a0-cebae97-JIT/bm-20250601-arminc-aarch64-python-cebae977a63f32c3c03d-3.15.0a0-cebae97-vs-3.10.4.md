# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-aarch64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.925x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 312 ms: 1.22x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.11 sec: 1.13x faster                                                  |
| html5lib       | 86.5 ms                                                               | 61.9 ms: 1.40x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 914 ms: 2.50x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 475 ms: 2.39x faster                                                    |
| async_tree_none         | 950 ms                                                                | 398 ms: 2.38x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 678 ms: 1.88x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.27x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 85.8 ms: 1.57x faster                                                   |
| nbody          | 166 ms                                                                | 119 ms: 1.39x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 27.7 ms: 1.16x faster                                                   |
| regex_dna      | 257 ms                                                                | 233 ms: 1.10x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.03 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.35 sec: 1.43x faster                                                  |
| unpickle_pure_python | 366 us                                                                | 256 us: 1.43x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 390 us: 1.36x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 78.0 ms: 1.28x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 186 ms: 1.14x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 110 ms: 1.11x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.0 us: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.21x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.56 ms: 1.24x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.1 ms: 1.44x faster                                                   |
| django_template | 53.3 ms                                                               | 40.2 ms: 1.33x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.4 ms: 1.29x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 64.0 ms: 1.09x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pprint_pformat           | 2.36 sec                                                              | 1.91 us: 1234577.35x faster                                             |
| pprint_safe_repr         | 1.15 sec                                                              | 1.05 us: 1091282.65x faster                                             |
| typing_runtime_protocols | 661 us                                                                | 206 us: 3.22x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 914 ms: 2.50x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 475 ms: 2.39x faster                                                    |
| async_tree_none          | 950 ms                                                                | 398 ms: 2.38x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.86 ms: 2.32x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.69 sec: 2.19x faster                                                  |
| richards_super           | 107 ms                                                                | 52.5 ms: 2.04x faster                                                   |
| richards                 | 91.7 ms                                                               | 45.4 ms: 2.02x faster                                                   |
| generators               | 68.1 ms                                                               | 36.1 ms: 1.88x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 678 ms: 1.88x faster                                                    |
| raytrace                 | 573 ms                                                                | 332 ms: 1.72x faster                                                    |
| chaos                    | 121 ms                                                                | 71.0 ms: 1.70x faster                                                   |
| scimark_sor              | 246 ms                                                                | 147 ms: 1.68x faster                                                    |
| go                       | 264 ms                                                                | 159 ms: 1.66x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.8 us: 1.63x faster                                                   |
| deepcopy                 | 511 us                                                                | 325 us: 1.57x faster                                                    |
| float                    | 135 ms                                                                | 85.8 ms: 1.57x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 82.3 ms: 1.55x faster                                                   |
| scimark_lu               | 227 ms                                                                | 149 ms: 1.53x faster                                                    |
| pylint                   | 485 ms                                                                | 323 ms: 1.51x faster                                                    |
| pyflate                  | 795 ms                                                                | 532 ms: 1.49x faster                                                    |
| comprehensions           | 33.1 us                                                               | 22.5 us: 1.47x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 91.9 ms: 1.46x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.54 ms: 1.45x faster                                                   |
| mako                     | 18.9 ms                                                               | 13.1 ms: 1.44x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.35 sec: 1.43x faster                                                  |
| spectral_norm            | 186 ms                                                                | 130 ms: 1.43x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 256 us: 1.43x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 61.9 ms: 1.40x faster                                                   |
| nbody                    | 166 ms                                                                | 119 ms: 1.39x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 53.3 ms: 1.38x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 390 us: 1.36x faster                                                    |
| django_template          | 53.3 ms                                                               | 40.2 ms: 1.33x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.4 ms: 1.29x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.26 us: 1.28x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 78.0 ms: 1.28x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.65 us: 1.26x faster                                                   |
| thrift                   | 1.26 ms                                                               | 1.00 ms: 1.26x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.77 us: 1.26x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.6 ms: 1.26x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 21.2 ms: 1.25x faster                                                   |
| 2to3                     | 381 ms                                                                | 312 ms: 1.22x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.39 sec: 1.22x faster                                                  |
| sympy_sum                | 184 ms                                                                | 152 ms: 1.21x faster                                                    |
| scimark_fft              | 500 ms                                                                | 423 ms: 1.18x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 27.7 ms: 1.16x faster                                                   |
| sympy_str                | 329 ms                                                                | 285 ms: 1.15x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 23.0 ms: 1.14x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 186 ms: 1.14x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.11 sec: 1.13x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 110 ms: 1.11x faster                                                    |
| fannkuch                 | 546 ms                                                                | 493 ms: 1.11x faster                                                    |
| regex_dna                | 257 ms                                                                | 233 ms: 1.10x faster                                                    |
| nqueens                  | 117 ms                                                                | 107 ms: 1.10x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.74 us: 1.10x faster                                                   |
| sympy_expand             | 543 ms                                                                | 494 ms: 1.10x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 64.0 ms: 1.09x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.12 ms: 1.07x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.03 ms: 1.06x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                                    |
| json                     | 5.88 ms                                                               | 5.71 ms: 1.03x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 674 ms: 1.03x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.0 us: 1.03x slower                                                   |
| async_generators         | 452 ms                                                                | 484 ms: 1.07x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.15 ms: 1.08x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.56 ms: 1.24x slower                                                   |
| coverage                 | 83.6 ms                                                               | 104 ms: 1.24x slower                                                    |
| python_startup           | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.85 ms: 1.65x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.77 ms: 1.67x slower                                                   |
| logging_silent           | 222 ns                                                                | 610 ns: 2.75x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.85x faster                                                            |

Benchmark hidden because not significant (2): meteor_contest, pidigits
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.925x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.37x
# Results vs. 3.10.4

- fork: python
- ref: 0cafa97932c6574734bb
- machine: linux-aarch64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.305x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 307 ms: 1.24x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.03 sec: 1.16x faster                                                   |
| html5lib       | 86.5 ms                                                               | 63.8 ms: 1.36x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 928 ms: 2.46x faster                                                     |
| async_tree_none         | 950 ms                                                                | 395 ms: 2.40x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 508 ms: 2.23x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 687 ms: 1.85x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.22x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 91.8 ms: 1.47x faster                                                    |
| nbody          | 166 ms                                                                | 125 ms: 1.33x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 130 ms: 1.36x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.07 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 270 us: 1.35x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 401 us: 1.32x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 85.7 ms: 1.16x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.5 ms: 1.15x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 187 ms: 1.13x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.06x faster                                                     |
| json_loads           | 30.9 us                                                               | 32.5 us: 1.05x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.15x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.38x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.2 ms: 1.33x faster                                                    |
| django_template | 53.3 ms                                                               | 41.4 ms: 1.29x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 29.4 ms: 1.20x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 63.7 ms: 1.10x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.23x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 210 us: 3.15x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 928 ms: 2.46x faster                                                     |
| async_tree_none          | 950 ms                                                                | 395 ms: 2.40x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 508 ms: 2.23x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.01 ms: 2.23x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 687 ms: 1.85x faster                                                     |
| generators               | 68.1 ms                                                               | 36.9 ms: 1.84x faster                                                    |
| richards_super           | 107 ms                                                                | 60.4 ms: 1.78x faster                                                    |
| raytrace                 | 573 ms                                                                | 324 ms: 1.77x faster                                                     |
| go                       | 264 ms                                                                | 150 ms: 1.76x faster                                                     |
| richards                 | 91.7 ms                                                               | 53.5 ms: 1.71x faster                                                    |
| chaos                    | 121 ms                                                                | 74.2 ms: 1.63x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.47 ms: 1.63x faster                                                    |
| scimark_lu               | 227 ms                                                                | 139 ms: 1.63x faster                                                     |
| logging_silent           | 222 ns                                                                | 140 ns: 1.59x faster                                                     |
| pylint                   | 485 ms                                                                | 306 ms: 1.58x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 84.8 ms: 1.58x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.80 ms: 1.58x faster                                                    |
| scimark_sor              | 246 ms                                                                | 162 ms: 1.52x faster                                                     |
| comprehensions           | 33.1 us                                                               | 21.9 us: 1.51x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 41.1 us: 1.50x faster                                                    |
| deepcopy                 | 511 us                                                                | 342 us: 1.49x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 7.39 ms: 1.48x faster                                                    |
| float                    | 135 ms                                                                | 91.8 ms: 1.47x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 87.4 ms: 1.46x faster                                                    |
| spectral_norm            | 186 ms                                                                | 132 ms: 1.41x faster                                                     |
| regex_compile            | 177 ms                                                                | 130 ms: 1.36x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 63.8 ms: 1.36x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 270 us: 1.35x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.23 us: 1.35x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.87 us: 1.35x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.3 ms: 1.34x faster                                                    |
| mako                     | 18.9 ms                                                               | 14.2 ms: 1.33x faster                                                    |
| pyflate                  | 795 ms                                                                | 597 ms: 1.33x faster                                                     |
| nbody                    | 166 ms                                                                | 125 ms: 1.33x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 401 us: 1.32x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.29 sec: 1.32x faster                                                   |
| sqlalchemy_declarative   | 197 ms                                                                | 152 ms: 1.30x faster                                                     |
| django_template          | 53.3 ms                                                               | 41.4 ms: 1.29x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.60 us: 1.28x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.2 ms: 1.27x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                   |
| thrift                   | 1.26 ms                                                               | 994 us: 1.27x faster                                                     |
| 2to3                     | 381 ms                                                                | 307 ms: 1.24x faster                                                     |
| sympy_sum                | 184 ms                                                                | 148 ms: 1.24x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 21.6 ms: 1.23x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.7 ms: 1.21x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.96 sec: 1.20x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.32 ms: 1.20x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 29.4 ms: 1.20x faster                                                    |
| sympy_str                | 329 ms                                                                | 275 ms: 1.20x faster                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 966 ms: 1.19x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 62.0 ms: 1.19x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.47 ms: 1.18x faster                                                    |
| scimark_fft              | 500 ms                                                                | 427 ms: 1.17x faster                                                     |
| sqlglot_normalize        | 156 ms                                                                | 134 ms: 1.17x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.03 sec: 1.16x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 85.7 ms: 1.16x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.5 ms: 1.15x faster                                                    |
| sympy_expand             | 543 ms                                                                | 473 ms: 1.15x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 187 ms: 1.13x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 66.7 ms: 1.13x faster                                                    |
| nqueens                  | 117 ms                                                                | 105 ms: 1.12x faster                                                     |
| fannkuch                 | 546 ms                                                                | 491 ms: 1.11x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 63.7 ms: 1.10x faster                                                    |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.09x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.45 sec: 1.07x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.06x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 4.07 ms: 1.04x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 679 ms: 1.03x slower                                                     |
| json_loads               | 30.9 us                                                               | 32.5 us: 1.05x slower                                                    |
| async_generators         | 452 ms                                                                | 486 ms: 1.07x slower                                                     |
| mypy2                    | 936 ms                                                                | 1.03 sec: 1.10x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.48 ms: 1.12x slower                                                    |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.61 ms: 1.60x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.83 ms: 1.64x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 4.34 sec: 298.58x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                             |

Benchmark hidden because not significant (6): json, sqlite_synth, xml_etree_generate, pidigits, regex_v8, regex_dna
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.305x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.31x
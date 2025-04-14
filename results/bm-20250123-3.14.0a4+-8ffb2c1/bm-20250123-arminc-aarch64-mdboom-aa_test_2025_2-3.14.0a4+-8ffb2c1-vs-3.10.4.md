# Results vs. 3.10.4

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-aarch64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.318x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 317 ms: 1.20x faster                                               |
| docutils       | 3.53 sec                                                              | 3.04 sec: 1.16x faster                                             |
| html5lib       | 86.5 ms                                                               | 64.5 ms: 1.34x faster                                              |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 897 ms: 2.55x faster                                               |
| async_tree_none         | 950 ms                                                                | 377 ms: 2.52x faster                                               |
| async_tree_memoization  | 1.13 sec                                                              | 490 ms: 2.31x faster                                               |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 681 ms: 1.87x faster                                               |
| Geometric mean          | (ref)                                                                 | 2.29x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 135 ms                                                                | 85.0 ms: 1.59x faster                                              |
| nbody          | 166 ms                                                                | 117 ms: 1.42x faster                                               |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 131 ms: 1.35x faster                                               |
| regex_effbot   | 4.25 ms                                                               | 4.03 ms: 1.05x faster                                              |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                       |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 404 us: 1.31x faster                                               |
| tomli_loads          | 3.36 sec                                                              | 2.60 sec: 1.29x faster                                             |
| unpickle_pure_python | 366 us                                                                | 290 us: 1.26x faster                                               |
| xml_etree_parse      | 212 ms                                                                | 180 ms: 1.17x faster                                               |
| xml_etree_process    | 99.5 ms                                                               | 85.3 ms: 1.17x faster                                              |
| json_dumps           | 16.7 ms                                                               | 14.8 ms: 1.13x faster                                              |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                               |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                               |
| json_loads           | 30.9 us                                                               | 32.5 us: 1.05x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.16x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                              |
| python_startup         | 11.2 ms                                                               | 16.5 ms: 1.47x slower                                              |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.4 ms: 1.32x faster                                              |
| django_template | 53.3 ms                                                               | 42.8 ms: 1.25x faster                                              |
| genshi_text     | 35.2 ms                                                               | 29.5 ms: 1.19x faster                                              |
| genshi_xml      | 69.8 ms                                                               | 64.1 ms: 1.09x faster                                              |
| Geometric mean  | (ref)                                                                 | 1.21x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.19x faster                                               |
| async_tree_io            | 2.28 sec                                                              | 897 ms: 2.55x faster                                               |
| async_tree_none          | 950 ms                                                                | 377 ms: 2.52x faster                                               |
| async_tree_memoization   | 1.13 sec                                                              | 490 ms: 2.31x faster                                               |
| deltablue                | 8.94 ms                                                               | 4.07 ms: 2.20x faster                                              |
| go                       | 264 ms                                                                | 141 ms: 1.88x faster                                               |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 681 ms: 1.87x faster                                               |
| richards_super           | 107 ms                                                                | 58.3 ms: 1.84x faster                                              |
| generators               | 68.1 ms                                                               | 37.3 ms: 1.83x faster                                              |
| raytrace                 | 573 ms                                                                | 315 ms: 1.82x faster                                               |
| richards                 | 91.7 ms                                                               | 51.2 ms: 1.79x faster                                              |
| chaos                    | 121 ms                                                                | 68.9 ms: 1.76x faster                                              |
| scimark_lu               | 227 ms                                                                | 137 ms: 1.65x faster                                               |
| sqlglot_parse            | 2.40 ms                                                               | 1.46 ms: 1.65x faster                                              |
| logging_silent           | 222 ns                                                                | 137 ns: 1.62x faster                                               |
| sqlglot_transpile        | 2.84 ms                                                               | 1.76 ms: 1.61x faster                                              |
| crypto_pyaes             | 134 ms                                                                | 84.5 ms: 1.59x faster                                              |
| float                    | 135 ms                                                                | 85.0 ms: 1.59x faster                                              |
| pylint                   | 485 ms                                                                | 307 ms: 1.58x faster                                               |
| scimark_sor              | 246 ms                                                                | 156 ms: 1.58x faster                                               |
| comprehensions           | 33.1 us                                                               | 21.6 us: 1.53x faster                                              |
| spectral_norm            | 186 ms                                                                | 122 ms: 1.53x faster                                               |
| deepcopy_memo            | 61.7 us                                                               | 40.8 us: 1.51x faster                                              |
| scimark_monte_carlo      | 128 ms                                                                | 84.5 ms: 1.51x faster                                              |
| hexiom                   | 10.9 ms                                                               | 7.44 ms: 1.47x faster                                              |
| deepcopy                 | 511 us                                                                | 351 us: 1.46x faster                                               |
| nbody                    | 166 ms                                                                | 117 ms: 1.42x faster                                               |
| regex_compile            | 177 ms                                                                | 131 ms: 1.35x faster                                               |
| pyflate                  | 795 ms                                                                | 589 ms: 1.35x faster                                               |
| html5lib                 | 86.5 ms                                                               | 64.5 ms: 1.34x faster                                              |
| thrift                   | 1.26 ms                                                               | 948 us: 1.33x faster                                               |
| sqlalchemy_declarative   | 197 ms                                                                | 150 ms: 1.32x faster                                               |
| mako                     | 18.9 ms                                                               | 14.4 ms: 1.32x faster                                              |
| pycparser                | 1.69 sec                                                              | 1.29 sec: 1.31x faster                                             |
| pickle_pure_python       | 529 us                                                                | 404 us: 1.31x faster                                               |
| logging_format           | 10.6 us                                                               | 8.17 us: 1.30x faster                                              |
| tomli_loads              | 3.36 sec                                                              | 2.60 sec: 1.29x faster                                             |
| logging_simple           | 9.78 us                                                               | 7.60 us: 1.29x faster                                              |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.29x faster                                               |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.1 ms: 1.28x faster                                              |
| coroutines               | 37.2 ms                                                               | 29.2 ms: 1.27x faster                                              |
| unpickle_pure_python     | 366 us                                                                | 290 us: 1.26x faster                                               |
| django_template          | 53.3 ms                                                               | 42.8 ms: 1.25x faster                                              |
| sympy_integrate          | 26.5 ms                                                               | 21.5 ms: 1.24x faster                                              |
| deepcopy_reduce          | 4.60 us                                                               | 3.72 us: 1.24x faster                                              |
| sympy_str                | 329 ms                                                                | 266 ms: 1.23x faster                                               |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.23 ms: 1.22x faster                                              |
| dulwich_log              | 73.5 ms                                                               | 61.0 ms: 1.21x faster                                              |
| 2to3                     | 381 ms                                                                | 317 ms: 1.20x faster                                               |
| genshi_text              | 35.2 ms                                                               | 29.5 ms: 1.19x faster                                              |
| bench_thread_pool        | 1.59 ms                                                               | 1.34 ms: 1.19x faster                                              |
| pprint_pformat           | 2.36 sec                                                              | 2.00 sec: 1.18x faster                                             |
| scimark_fft              | 500 ms                                                                | 424 ms: 1.18x faster                                               |
| pprint_safe_repr         | 1.15 sec                                                              | 974 ms: 1.18x faster                                               |
| xml_etree_parse          | 212 ms                                                                | 180 ms: 1.17x faster                                               |
| pathlib                  | 26.3 ms                                                               | 22.4 ms: 1.17x faster                                              |
| sqlglot_optimize         | 75.4 ms                                                               | 64.3 ms: 1.17x faster                                              |
| xml_etree_process        | 99.5 ms                                                               | 85.3 ms: 1.17x faster                                              |
| docutils                 | 3.53 sec                                                              | 3.04 sec: 1.16x faster                                             |
| sqlglot_normalize        | 156 ms                                                                | 135 ms: 1.16x faster                                               |
| nqueens                  | 117 ms                                                                | 101 ms: 1.16x faster                                               |
| sympy_expand             | 543 ms                                                                | 475 ms: 1.14x faster                                               |
| fannkuch                 | 546 ms                                                                | 480 ms: 1.14x faster                                               |
| json_dumps               | 16.7 ms                                                               | 14.8 ms: 1.13x faster                                              |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                               |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                               |
| genshi_xml               | 69.8 ms                                                               | 64.1 ms: 1.09x faster                                              |
| meteor_contest           | 126 ms                                                                | 117 ms: 1.08x faster                                               |
| mdp                      | 3.70 sec                                                              | 3.48 sec: 1.06x faster                                             |
| regex_effbot             | 4.25 ms                                                               | 4.03 ms: 1.05x faster                                              |
| asyncio_websockets       | 657 ms                                                                | 679 ms: 1.03x slower                                               |
| json_loads               | 30.9 us                                                               | 32.5 us: 1.05x slower                                              |
| telco                    | 8.49 ms                                                               | 9.60 ms: 1.13x slower                                              |
| coverage                 | 83.6 ms                                                               | 99.5 ms: 1.19x slower                                              |
| python_startup_no_site   | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                              |
| python_startup           | 11.2 ms                                                               | 16.5 ms: 1.47x slower                                              |
| create_gc_cycles         | 2.26 ms                                                               | 3.76 ms: 1.66x slower                                              |
| gc_traversal             | 4.15 ms                                                               | 7.01 ms: 1.69x slower                                              |
| bench_mp_pool            | 14.5 ms                                                               | 6.60 sec: 453.89x slower                                           |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                       |

Benchmark hidden because not significant (6): async_generators, sqlite_synth, json, regex_v8, pidigits, regex_dna
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250123-3.14.0a4+-8ffb2c1/bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.318x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.30x
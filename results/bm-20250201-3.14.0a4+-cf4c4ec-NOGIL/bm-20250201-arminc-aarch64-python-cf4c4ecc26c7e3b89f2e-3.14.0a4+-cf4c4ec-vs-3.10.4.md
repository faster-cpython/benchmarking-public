# Results vs. 3.10.4

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-aarch64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.109x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.57x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 3.53 sec                                                              | 3.38 sec: 1.04x faster                                                   |
| html5lib       | 86.5 ms                                                               | 75.6 ms: 1.14x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 966 ms: 2.37x faster                                                     |
| async_tree_none         | 950 ms                                                                | 443 ms: 2.14x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 549 ms: 2.07x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 722 ms: 1.76x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.07x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 103 ms: 1.31x faster                                                     |
| nbody          | 166 ms                                                                | 188 ms: 1.13x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 158 ms: 1.12x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.05 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 156 ms                                                                | 130 ms: 1.20x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 308 us: 1.19x faster                                                     |
| xml_etree_parse      | 212 ms                                                                | 184 ms: 1.15x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 484 us: 1.09x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 3.20 sec: 1.05x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 103 ms: 1.04x slower                                                     |
| unpickle_list        | 6.99 us                                                               | 7.45 us: 1.07x slower                                                    |
| unpickle             | 17.5 us                                                               | 19.9 us: 1.14x slower                                                    |
| pickle_list          | 5.24 us                                                               | 6.07 us: 1.16x slower                                                    |
| xml_etree_generate   | 123 ms                                                                | 143 ms: 1.16x slower                                                     |
| pickle_dict          | 35.1 us                                                               | 42.2 us: 1.20x slower                                                    |
| json_loads           | 30.9 us                                                               | 38.3 us: 1.24x slower                                                    |
| pickle               | 12.5 us                                                               | 15.9 us: 1.28x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.2 ms: 1.77x slower                                                    |
| python_startup         | 11.2 ms                                                               | 20.0 ms: 1.79x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.78x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 55.2 ms: 1.04x slower                                                    |
| genshi_text     | 35.2 ms                                                               | 37.1 ms: 1.05x slower                                                    |
| genshi_xml      | 69.8 ms                                                               | 78.9 ms: 1.13x slower                                                    |
| mako            | 18.9 ms                                                               | 23.5 ms: 1.24x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.11x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io            | 2.28 sec                                                              | 966 ms: 2.37x faster                                                     |
| typing_runtime_protocols | 661 us                                                                | 282 us: 2.34x faster                                                     |
| async_tree_none          | 950 ms                                                                | 443 ms: 2.14x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 549 ms: 2.07x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 722 ms: 1.76x faster                                                     |
| generators               | 68.1 ms                                                               | 42.4 ms: 1.61x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 611 ms: 1.54x faster                                                     |
| gc_traversal             | 4.15 ms                                                               | 2.70 ms: 1.54x faster                                                    |
| go                       | 264 ms                                                                | 180 ms: 1.47x faster                                                     |
| deltablue                | 8.94 ms                                                               | 6.17 ms: 1.45x faster                                                    |
| logging_silent           | 222 ns                                                                | 156 ns: 1.42x faster                                                     |
| raytrace                 | 573 ms                                                                | 415 ms: 1.38x faster                                                     |
| chaos                    | 121 ms                                                                | 88.7 ms: 1.36x faster                                                    |
| scimark_sor              | 246 ms                                                                | 182 ms: 1.35x faster                                                     |
| float                    | 135 ms                                                                | 103 ms: 1.31x faster                                                     |
| spectral_norm            | 186 ms                                                                | 144 ms: 1.30x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.56 sec: 1.28x faster                                                   |
| pylint                   | 485 ms                                                                | 385 ms: 1.26x faster                                                     |
| comprehensions           | 33.1 us                                                               | 26.7 us: 1.24x faster                                                    |
| coroutines               | 37.2 ms                                                               | 30.5 ms: 1.22x faster                                                    |
| richards                 | 91.7 ms                                                               | 75.1 ms: 1.22x faster                                                    |
| pyflate                  | 795 ms                                                                | 655 ms: 1.21x faster                                                     |
| richards_super           | 107 ms                                                                | 88.4 ms: 1.21x faster                                                    |
| deepcopy                 | 511 us                                                                | 421 us: 1.21x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 2.00 ms: 1.20x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 130 ms: 1.20x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 2.38 ms: 1.19x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 308 us: 1.19x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.43 sec: 1.18x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 52.5 us: 1.18x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 115 ms: 1.17x faster                                                     |
| scimark_lu               | 227 ms                                                                | 195 ms: 1.16x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 9.41 ms: 1.16x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.8 ms: 1.16x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 184 ms: 1.15x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 112 ms: 1.14x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 75.6 ms: 1.14x faster                                                    |
| regex_compile            | 177 ms                                                                | 158 ms: 1.12x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.71 us: 1.11x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 484 us: 1.09x faster                                                     |
| logging_simple           | 9.78 us                                                               | 8.99 us: 1.09x faster                                                    |
| logging_format           | 10.6 us                                                               | 9.96 us: 1.06x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 3.20 sec: 1.05x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.05 ms: 1.05x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.16 ms: 1.05x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.38 sec: 1.04x faster                                                   |
| scimark_fft              | 500 ms                                                                | 487 ms: 1.03x faster                                                     |
| django_template          | 53.3 ms                                                               | 55.2 ms: 1.04x slower                                                    |
| xml_etree_process        | 99.5 ms                                                               | 103 ms: 1.04x slower                                                     |
| asyncio_websockets       | 657 ms                                                                | 681 ms: 1.04x slower                                                     |
| mdp                      | 3.70 sec                                                              | 3.86 sec: 1.04x slower                                                   |
| genshi_text              | 35.2 ms                                                               | 37.1 ms: 1.05x slower                                                    |
| unpickle_list            | 6.99 us                                                               | 7.45 us: 1.07x slower                                                    |
| sympy_sum                | 184 ms                                                                | 197 ms: 1.07x slower                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 22.4 ms: 1.09x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 29.2 ms: 1.10x slower                                                    |
| sympy_str                | 329 ms                                                                | 368 ms: 1.12x slower                                                     |
| json                     | 5.88 ms                                                               | 6.59 ms: 1.12x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 78.9 ms: 1.13x slower                                                    |
| sympy_expand             | 543 ms                                                                | 614 ms: 1.13x slower                                                     |
| nbody                    | 166 ms                                                                | 188 ms: 1.13x slower                                                     |
| unpickle                 | 17.5 us                                                               | 19.9 us: 1.14x slower                                                    |
| pickle_list              | 5.24 us                                                               | 6.07 us: 1.16x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 143 ms: 1.16x slower                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.88 ms: 1.18x slower                                                    |
| nqueens                  | 117 ms                                                                | 139 ms: 1.18x slower                                                     |
| async_generators         | 452 ms                                                                | 542 ms: 1.20x slower                                                     |
| meteor_contest           | 126 ms                                                                | 152 ms: 1.20x slower                                                     |
| pickle_dict              | 35.1 us                                                               | 42.2 us: 1.20x slower                                                    |
| fannkuch                 | 546 ms                                                                | 672 ms: 1.23x slower                                                     |
| json_loads               | 30.9 us                                                               | 38.3 us: 1.24x slower                                                    |
| mako                     | 18.9 ms                                                               | 23.5 ms: 1.24x slower                                                    |
| pickle                   | 12.5 us                                                               | 15.9 us: 1.28x slower                                                    |
| telco                    | 8.49 ms                                                               | 11.4 ms: 1.35x slower                                                    |
| coverage                 | 83.6 ms                                                               | 140 ms: 1.67x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 12.2 ms: 1.77x slower                                                    |
| python_startup           | 11.2 ms                                                               | 20.0 ms: 1.79x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 54.9 ms: 3.77x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (14): dulwich_log, thrift, regex_v8, 2to3, sqlglot_normalize, pidigits, pprint_pformat, pprint_safe_repr, regex_dna, sqlalchemy_declarative, deepcopy_reduce, json_dumps, scimark_sparse_mat_mult, sqlglot_optimize
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250201-3.14.0a4+-cf4c4ec-NOGIL/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.109x faster

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.57x
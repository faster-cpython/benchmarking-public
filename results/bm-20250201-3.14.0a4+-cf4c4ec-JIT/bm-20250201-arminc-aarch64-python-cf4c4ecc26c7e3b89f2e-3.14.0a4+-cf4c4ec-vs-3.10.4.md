# Results vs. 3.10.4

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-aarch64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.217x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 321 ms: 1.19x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.30 sec: 1.07x faster                                                   |
| html5lib       | 86.5 ms                                                               | 75.6 ms: 1.14x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 965 ms: 2.37x faster                                                     |
| async_tree_none         | 950 ms                                                                | 425 ms: 2.23x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 528 ms: 2.15x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 722 ms: 1.76x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.11x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 89.5 ms: 1.51x faster                                                    |
| nbody          | 166 ms                                                                | 123 ms: 1.35x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 146 ms: 1.21x faster                                                     |
| regex_dna      | 257 ms                                                                | 272 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                             |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 275 us: 1.33x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 406 us: 1.30x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 79.4 ms: 1.25x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.11x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 147 ms: 1.06x faster                                                     |
| json_loads           | 30.9 us                                                               | 35.6 us: 1.15x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 41.2 us: 1.17x slower                                                    |
| pickle_list          | 5.24 us                                                               | 6.17 us: 1.18x slower                                                    |
| pickle               | 12.5 us                                                               | 15.9 us: 1.27x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.5 ms: 1.47x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                    |
| django_template | 53.3 ms                                                               | 48.3 ms: 1.11x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 33.8 ms: 1.04x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 85.8 ms: 1.23x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.06x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 227 us: 2.91x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 965 ms: 2.37x faster                                                     |
| async_tree_none          | 950 ms                                                                | 425 ms: 2.23x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 528 ms: 2.15x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.51 ms: 1.98x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 722 ms: 1.76x faster                                                     |
| richards_super           | 107 ms                                                                | 62.1 ms: 1.73x faster                                                    |
| richards                 | 91.7 ms                                                               | 56.6 ms: 1.62x faster                                                    |
| raytrace                 | 573 ms                                                                | 361 ms: 1.59x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 598 ms: 1.58x faster                                                     |
| scimark_sor              | 246 ms                                                                | 158 ms: 1.56x faster                                                     |
| go                       | 264 ms                                                                | 170 ms: 1.55x faster                                                     |
| float                    | 135 ms                                                                | 89.5 ms: 1.51x faster                                                    |
| logging_silent           | 222 ns                                                                | 149 ns: 1.49x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.62 ms: 1.48x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.96 ms: 1.45x faster                                                    |
| pylint                   | 485 ms                                                                | 337 ms: 1.44x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 43.1 us: 1.43x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 89.6 ms: 1.43x faster                                                    |
| scimark_lu               | 227 ms                                                                | 159 ms: 1.42x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.31 sec: 1.42x faster                                                   |
| chaos                    | 121 ms                                                                | 86.7 ms: 1.40x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                    |
| nbody                    | 166 ms                                                                | 123 ms: 1.35x faster                                                     |
| spectral_norm            | 186 ms                                                                | 138 ms: 1.35x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 275 us: 1.33x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 101 ms: 1.33x faster                                                     |
| comprehensions           | 33.1 us                                                               | 25.1 us: 1.32x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 150 ms: 1.32x faster                                                     |
| pyflate                  | 795 ms                                                                | 605 ms: 1.31x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 406 us: 1.30x faster                                                     |
| coroutines               | 37.2 ms                                                               | 29.5 ms: 1.26x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 79.4 ms: 1.25x faster                                                    |
| deepcopy                 | 511 us                                                                | 409 us: 1.25x faster                                                     |
| thrift                   | 1.26 ms                                                               | 1.01 ms: 1.24x faster                                                    |
| generators               | 68.1 ms                                                               | 55.5 ms: 1.23x faster                                                    |
| regex_compile            | 177 ms                                                                | 146 ms: 1.21x faster                                                     |
| logging_simple           | 9.78 us                                                               | 8.08 us: 1.21x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.83 us: 1.20x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 17.1 ms: 1.20x faster                                                    |
| scimark_fft              | 500 ms                                                                | 422 ms: 1.19x faster                                                     |
| 2to3                     | 381 ms                                                                | 321 ms: 1.19x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 22.2 ms: 1.18x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.36 ms: 1.17x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 23.1 ms: 1.15x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 75.6 ms: 1.14x faster                                                    |
| sympy_sum                | 184 ms                                                                | 162 ms: 1.14x faster                                                     |
| sqlglot_normalize        | 156 ms                                                                | 140 ms: 1.12x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.11x faster                                                     |
| django_template          | 53.3 ms                                                               | 48.3 ms: 1.11x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.54 sec: 1.10x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.93 ms: 1.10x faster                                                    |
| sympy_str                | 329 ms                                                                | 303 ms: 1.08x faster                                                     |
| fannkuch                 | 546 ms                                                                | 508 ms: 1.07x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.30 sec: 1.07x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 10.2 ms: 1.07x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 70.6 ms: 1.07x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 147 ms: 1.06x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 70.0 ms: 1.05x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.39 us: 1.05x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 33.8 ms: 1.04x faster                                                    |
| sympy_expand             | 543 ms                                                                | 521 ms: 1.04x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.55 sec: 1.04x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.98 us: 1.03x faster                                                    |
| regex_dna                | 257 ms                                                                | 272 ms: 1.06x slower                                                     |
| json                     | 5.88 ms                                                               | 6.28 ms: 1.07x slower                                                    |
| async_generators         | 452 ms                                                                | 491 ms: 1.08x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.30 sec: 1.13x slower                                                   |
| nqueens                  | 117 ms                                                                | 134 ms: 1.14x slower                                                     |
| pprint_pformat           | 2.36 sec                                                              | 2.69 sec: 1.14x slower                                                   |
| json_loads               | 30.9 us                                                               | 35.6 us: 1.15x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 41.2 us: 1.17x slower                                                    |
| pickle_list              | 5.24 us                                                               | 6.17 us: 1.18x slower                                                    |
| telco                    | 8.49 ms                                                               | 10.1 ms: 1.19x slower                                                    |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                     |
| genshi_xml               | 69.8 ms                                                               | 85.8 ms: 1.23x slower                                                    |
| pickle                   | 12.5 us                                                               | 15.9 us: 1.27x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.5 ms: 1.47x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.60 ms: 1.59x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.87 ms: 1.65x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.56 sec: 107.45x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.12x faster                                                             |

Benchmark hidden because not significant (7): unpickle_list, regex_effbot, meteor_contest, regex_v8, asyncio_websockets, pidigits, unpickle
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.217x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.32x
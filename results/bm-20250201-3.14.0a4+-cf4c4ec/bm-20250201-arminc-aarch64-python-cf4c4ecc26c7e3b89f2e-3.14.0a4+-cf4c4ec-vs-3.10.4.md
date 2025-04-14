# Results vs. 3.10.4

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-aarch64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.328x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 301 ms: 1.26x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.96 sec: 1.19x faster                                                   |
| html5lib       | 86.5 ms                                                               | 66.0 ms: 1.31x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 924 ms: 2.47x faster                                                     |
| async_tree_none         | 950 ms                                                                | 402 ms: 2.36x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 505 ms: 2.24x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 694 ms: 1.83x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.21x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 88.2 ms: 1.53x faster                                                    |
| nbody          | 166 ms                                                                | 123 ms: 1.35x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 127 ms: 1.39x faster                                                     |
| regex_dna      | 257 ms                                                                | 247 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                             |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 262 us: 1.40x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 398 us: 1.33x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 182 ms: 1.16x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.7 ms: 1.13x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 147 ms: 1.06x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 116 ms: 1.06x faster                                                     |
| json_loads           | 30.9 us                                                               | 34.5 us: 1.12x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 40.2 us: 1.15x slower                                                    |
| pickle_list          | 5.24 us                                                               | 6.13 us: 1.17x slower                                                    |
| pickle               | 12.5 us                                                               | 16.5 us: 1.32x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 40.1 ms: 1.33x faster                                                    |
| mako            | 18.9 ms                                                               | 14.5 ms: 1.31x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.2 ms: 1.29x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 62.4 ms: 1.12x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.26x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 193 us: 3.43x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 924 ms: 2.47x faster                                                     |
| async_tree_none          | 950 ms                                                                | 402 ms: 2.36x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.86 ms: 2.32x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 505 ms: 2.24x faster                                                     |
| go                       | 264 ms                                                                | 144 ms: 1.84x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 694 ms: 1.83x faster                                                     |
| raytrace                 | 573 ms                                                                | 315 ms: 1.82x faster                                                     |
| richards_super           | 107 ms                                                                | 59.4 ms: 1.80x faster                                                    |
| generators               | 68.1 ms                                                               | 37.8 ms: 1.80x faster                                                    |
| chaos                    | 121 ms                                                                | 68.4 ms: 1.77x faster                                                    |
| richards                 | 91.7 ms                                                               | 52.9 ms: 1.73x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 546 ms: 1.73x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.45 ms: 1.66x faster                                                    |
| scimark_lu               | 227 ms                                                                | 139 ms: 1.63x faster                                                     |
| logging_silent           | 222 ns                                                                | 136 ns: 1.63x faster                                                     |
| scimark_sor              | 246 ms                                                                | 152 ms: 1.62x faster                                                     |
| comprehensions           | 33.1 us                                                               | 21.3 us: 1.56x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.83 ms: 1.55x faster                                                    |
| float                    | 135 ms                                                                | 88.2 ms: 1.53x faster                                                    |
| spectral_norm            | 186 ms                                                                | 123 ms: 1.52x faster                                                     |
| pylint                   | 485 ms                                                                | 322 ms: 1.51x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 88.8 ms: 1.51x faster                                                    |
| deepcopy                 | 511 us                                                                | 344 us: 1.48x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 41.7 us: 1.48x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.38 ms: 1.48x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 87.3 ms: 1.46x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.26 sec: 1.45x faster                                                   |
| pyflate                  | 795 ms                                                                | 568 ms: 1.40x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 262 us: 1.40x faster                                                     |
| regex_compile            | 177 ms                                                                | 127 ms: 1.39x faster                                                     |
| nbody                    | 166 ms                                                                | 123 ms: 1.35x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.3 ms: 1.34x faster                                                    |
| django_template          | 53.3 ms                                                               | 40.1 ms: 1.33x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 148 ms: 1.33x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 398 us: 1.33x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.27 sec: 1.33x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.38 us: 1.32x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.07 us: 1.31x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 66.0 ms: 1.31x faster                                                    |
| mako                     | 18.9 ms                                                               | 14.5 ms: 1.31x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.2 ms: 1.29x faster                                                    |
| thrift                   | 1.26 ms                                                               | 982 us: 1.28x faster                                                     |
| 2to3                     | 381 ms                                                                | 301 ms: 1.26x faster                                                     |
| coroutines               | 37.2 ms                                                               | 29.5 ms: 1.26x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.1 ms: 1.25x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.29 ms: 1.23x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 21.5 ms: 1.23x faster                                                    |
| sympy_str                | 329 ms                                                                | 268 ms: 1.23x faster                                                     |
| sympy_sum                | 184 ms                                                                | 150 ms: 1.22x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 61.7 ms: 1.22x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.27 ms: 1.22x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 60.6 ms: 1.21x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.82 us: 1.20x faster                                                    |
| scimark_fft              | 500 ms                                                                | 419 ms: 1.19x faster                                                     |
| sqlglot_normalize        | 156 ms                                                                | 131 ms: 1.19x faster                                                     |
| docutils                 | 3.53 sec                                                              | 2.96 sec: 1.19x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.99 sec: 1.18x faster                                                   |
| nqueens                  | 117 ms                                                                | 101 ms: 1.17x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 182 ms: 1.16x faster                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 988 ms: 1.16x faster                                                     |
| fannkuch                 | 546 ms                                                                | 477 ms: 1.14x faster                                                     |
| sympy_expand             | 543 ms                                                                | 476 ms: 1.14x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.7 ms: 1.13x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 62.4 ms: 1.12x faster                                                    |
| meteor_contest           | 126 ms                                                                | 115 ms: 1.10x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.39 sec: 1.09x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 147 ms: 1.06x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 116 ms: 1.06x faster                                                     |
| regex_dna                | 257 ms                                                                | 247 ms: 1.04x faster                                                     |
| asyncio_websockets       | 657 ms                                                                | 672 ms: 1.02x slower                                                     |
| json_loads               | 30.9 us                                                               | 34.5 us: 1.12x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.52 ms: 1.12x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 40.2 us: 1.15x slower                                                    |
| pickle_list              | 5.24 us                                                               | 6.13 us: 1.17x slower                                                    |
| coverage                 | 83.6 ms                                                               | 100 ms: 1.20x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                    |
| pickle                   | 12.5 us                                                               | 16.5 us: 1.32x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.50 ms: 1.56x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.65 ms: 1.62x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 5.94 sec: 409.00x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                             |

Benchmark hidden because not significant (8): regex_effbot, unpickle_list, sqlite_synth, async_generators, pidigits, json, regex_v8, unpickle
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.328x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.30x
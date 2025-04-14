# Results vs. 3.10.4

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-aarch64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.327x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 307 ms: 1.24x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                   |
| html5lib       | 86.5 ms                                                               | 62.9 ms: 1.37x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 926 ms: 2.47x faster                                                     |
| async_tree_none         | 950 ms                                                                | 403 ms: 2.36x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 503 ms: 2.25x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 691 ms: 1.84x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.22x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.5 ms: 1.56x faster                                                    |
| nbody          | 166 ms                                                                | 120 ms: 1.38x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 127 ms: 1.40x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                             |

Benchmark hidden because not significant (3): regex_effbot, regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 266 us: 1.38x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 390 us: 1.36x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 82.5 ms: 1.21x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 185 ms: 1.14x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 15.0 ms: 1.11x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.44 us: 1.09x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.08x faster                                                     |
| pickle_dict          | 35.1 us                                                               | 38.8 us: 1.11x slower                                                    |
| pickle_list          | 5.24 us                                                               | 5.90 us: 1.13x slower                                                    |
| json_loads           | 30.9 us                                                               | 35.3 us: 1.14x slower                                                    |
| pickle               | 12.5 us                                                               | 16.4 us: 1.31x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.0 ms: 1.36x faster                                                    |
| django_template | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.4 ms: 1.28x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 64.4 ms: 1.09x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.26x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 196 us: 3.38x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 926 ms: 2.47x faster                                                     |
| async_tree_none          | 950 ms                                                                | 403 ms: 2.36x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.93 ms: 2.28x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 503 ms: 2.25x faster                                                     |
| go                       | 264 ms                                                                | 140 ms: 1.89x faster                                                     |
| generators               | 68.1 ms                                                               | 36.8 ms: 1.85x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 691 ms: 1.84x faster                                                     |
| richards_super           | 107 ms                                                                | 60.3 ms: 1.78x faster                                                    |
| raytrace                 | 573 ms                                                                | 323 ms: 1.78x faster                                                     |
| richards                 | 91.7 ms                                                               | 52.8 ms: 1.74x faster                                                    |
| chaos                    | 121 ms                                                                | 69.9 ms: 1.73x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 548 ms: 1.72x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.41 ms: 1.71x faster                                                    |
| logging_silent           | 222 ns                                                                | 136 ns: 1.63x faster                                                     |
| pylint                   | 485 ms                                                                | 304 ms: 1.60x faster                                                     |
| scimark_lu               | 227 ms                                                                | 142 ms: 1.59x faster                                                     |
| scimark_sor              | 246 ms                                                                | 156 ms: 1.58x faster                                                     |
| spectral_norm            | 186 ms                                                                | 119 ms: 1.57x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.82 ms: 1.56x faster                                                    |
| float                    | 135 ms                                                                | 86.5 ms: 1.56x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 86.6 ms: 1.55x faster                                                    |
| comprehensions           | 33.1 us                                                               | 21.5 us: 1.54x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 40.6 us: 1.52x faster                                                    |
| deepcopy                 | 511 us                                                                | 339 us: 1.50x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 86.5 ms: 1.48x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.46 ms: 1.46x faster                                                    |
| pyflate                  | 795 ms                                                                | 552 ms: 1.44x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.29 sec: 1.43x faster                                                   |
| regex_compile            | 177 ms                                                                | 127 ms: 1.40x faster                                                     |
| nbody                    | 166 ms                                                                | 120 ms: 1.38x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 266 us: 1.38x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 62.9 ms: 1.37x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 145 ms: 1.36x faster                                                     |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.36x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 390 us: 1.36x faster                                                     |
| django_template          | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.29 us: 1.34x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.4 ms: 1.34x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.28 sec: 1.32x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.09 us: 1.31x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.4 ms: 1.28x faster                                                    |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.28x faster                                                     |
| coroutines               | 37.2 ms                                                               | 29.3 ms: 1.27x faster                                                    |
| thrift                   | 1.26 ms                                                               | 994 us: 1.27x faster                                                     |
| sympy_str                | 329 ms                                                                | 261 ms: 1.26x faster                                                     |
| 2to3                     | 381 ms                                                                | 307 ms: 1.24x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 60.8 ms: 1.24x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.72 us: 1.23x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 21.6 ms: 1.23x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 59.9 ms: 1.23x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 82.5 ms: 1.21x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 953 ms: 1.20x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 21.9 ms: 1.20x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.97 sec: 1.20x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.20x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.38 ms: 1.19x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 131 ms: 1.19x faster                                                     |
| sympy_expand             | 543 ms                                                                | 462 ms: 1.17x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                   |
| nqueens                  | 117 ms                                                                | 101 ms: 1.16x faster                                                     |
| scimark_fft              | 500 ms                                                                | 434 ms: 1.15x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 185 ms: 1.14x faster                                                     |
| fannkuch                 | 546 ms                                                                | 486 ms: 1.12x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 15.0 ms: 1.11x faster                                                    |
| meteor_contest           | 126 ms                                                                | 114 ms: 1.11x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.35 sec: 1.10x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.44 us: 1.09x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 64.4 ms: 1.09x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.08x faster                                                     |
| json                     | 5.88 ms                                                               | 6.14 ms: 1.05x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 38.8 us: 1.11x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.46 ms: 1.11x slower                                                    |
| pickle_list              | 5.24 us                                                               | 5.90 us: 1.13x slower                                                    |
| json_loads               | 30.9 us                                                               | 35.3 us: 1.14x slower                                                    |
| coverage                 | 83.6 ms                                                               | 104 ms: 1.24x slower                                                     |
| pickle                   | 12.5 us                                                               | 16.4 us: 1.31x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.59 ms: 1.59x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 7.01 ms: 1.69x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 5.97 sec: 410.53x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                             |

Benchmark hidden because not significant (9): regex_effbot, sqlite_synth, async_generators, regex_v8, regex_dna, asyncio_websockets, xml_etree_iterparse, unpickle, pidigits
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.327x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.30x
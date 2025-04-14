# Results vs. 3.10.4

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-aarch64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.105x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.58x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 3.53 sec                                                              | 3.39 sec: 1.04x faster                                                   |
| html5lib       | 86.5 ms                                                               | 80.6 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 955 ms: 2.39x faster                                                     |
| async_tree_none         | 950 ms                                                                | 444 ms: 2.14x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 539 ms: 2.10x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 716 ms: 1.78x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.09x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 102 ms: 1.32x faster                                                     |
| nbody          | 166 ms                                                                | 183 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 161 ms: 1.10x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.07 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 156 ms                                                                | 131 ms: 1.19x faster                                                     |
| xml_etree_parse      | 212 ms                                                                | 180 ms: 1.18x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 333 us: 1.10x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 3.16 sec: 1.06x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 499 us: 1.06x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 7.44 us: 1.06x slower                                                    |
| xml_etree_generate   | 123 ms                                                                | 138 ms: 1.13x slower                                                     |
| pickle_list          | 5.24 us                                                               | 6.07 us: 1.16x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 41.2 us: 1.17x slower                                                    |
| unpickle             | 17.5 us                                                               | 20.9 us: 1.20x slower                                                    |
| json_loads           | 30.9 us                                                               | 39.9 us: 1.29x slower                                                    |
| pickle               | 12.5 us                                                               | 16.7 us: 1.33x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.3 ms: 1.78x slower                                                    |
| python_startup         | 11.2 ms                                                               | 20.1 ms: 1.80x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.79x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 35.2 ms                                                               | 37.0 ms: 1.05x slower                                                    |
| django_template | 53.3 ms                                                               | 60.0 ms: 1.12x slower                                                    |
| genshi_xml      | 69.8 ms                                                               | 81.1 ms: 1.16x slower                                                    |
| mako            | 18.9 ms                                                               | 23.4 ms: 1.24x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.14x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io            | 2.28 sec                                                              | 955 ms: 2.39x faster                                                     |
| typing_runtime_protocols | 661 us                                                                | 281 us: 2.36x faster                                                     |
| async_tree_none          | 950 ms                                                                | 444 ms: 2.14x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 539 ms: 2.10x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 716 ms: 1.78x faster                                                     |
| generators               | 68.1 ms                                                               | 42.5 ms: 1.60x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 608 ms: 1.55x faster                                                     |
| go                       | 264 ms                                                                | 174 ms: 1.52x faster                                                     |
| gc_traversal             | 4.15 ms                                                               | 2.75 ms: 1.51x faster                                                    |
| deltablue                | 8.94 ms                                                               | 6.09 ms: 1.47x faster                                                    |
| logging_silent           | 222 ns                                                                | 154 ns: 1.44x faster                                                     |
| scimark_sor              | 246 ms                                                                | 173 ms: 1.42x faster                                                     |
| chaos                    | 121 ms                                                                | 88.7 ms: 1.37x faster                                                    |
| raytrace                 | 573 ms                                                                | 423 ms: 1.36x faster                                                     |
| spectral_norm            | 186 ms                                                                | 142 ms: 1.32x faster                                                     |
| float                    | 135 ms                                                                | 102 ms: 1.32x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.54 sec: 1.29x faster                                                   |
| pylint                   | 485 ms                                                                | 385 ms: 1.26x faster                                                     |
| richards_super           | 107 ms                                                                | 85.9 ms: 1.25x faster                                                    |
| coroutines               | 37.2 ms                                                               | 30.1 ms: 1.23x faster                                                    |
| richards                 | 91.7 ms                                                               | 74.5 ms: 1.23x faster                                                    |
| comprehensions           | 33.1 us                                                               | 27.0 us: 1.23x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.96 ms: 1.22x faster                                                    |
| deepcopy                 | 511 us                                                                | 427 us: 1.20x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 131 ms: 1.19x faster                                                     |
| pyflate                  | 795 ms                                                                | 671 ms: 1.19x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 114 ms: 1.18x faster                                                     |
| scimark_lu               | 227 ms                                                                | 193 ms: 1.18x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 180 ms: 1.18x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 2.43 ms: 1.17x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.47 sec: 1.15x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 9.48 ms: 1.15x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 113 ms: 1.13x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 55.2 us: 1.12x faster                                                    |
| regex_compile            | 177 ms                                                                | 161 ms: 1.10x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 333 us: 1.10x faster                                                     |
| logging_format           | 10.6 us                                                               | 9.73 us: 1.09x faster                                                    |
| logging_simple           | 9.78 us                                                               | 8.97 us: 1.09x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.80 us: 1.08x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 24.3 ms: 1.08x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 80.6 ms: 1.07x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 3.16 sec: 1.06x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 499 us: 1.06x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 4.07 ms: 1.04x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.39 sec: 1.04x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.80 ms: 1.02x slower                                                    |
| mdp                      | 3.70 sec                                                              | 3.83 sec: 1.04x slower                                                   |
| sympy_sum                | 184 ms                                                                | 191 ms: 1.04x slower                                                     |
| asyncio_websockets       | 657 ms                                                                | 683 ms: 1.04x slower                                                     |
| genshi_text              | 35.2 ms                                                               | 37.0 ms: 1.05x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 28.0 ms: 1.06x slower                                                    |
| unpickle_list            | 6.99 us                                                               | 7.44 us: 1.06x slower                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 22.4 ms: 1.09x slower                                                    |
| nbody                    | 166 ms                                                                | 183 ms: 1.10x slower                                                     |
| nqueens                  | 117 ms                                                                | 130 ms: 1.11x slower                                                     |
| sympy_str                | 329 ms                                                                | 364 ms: 1.11x slower                                                     |
| django_template          | 53.3 ms                                                               | 60.0 ms: 1.12x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 138 ms: 1.13x slower                                                     |
| json                     | 5.88 ms                                                               | 6.66 ms: 1.13x slower                                                    |
| sympy_expand             | 543 ms                                                                | 616 ms: 1.14x slower                                                     |
| pickle_list              | 5.24 us                                                               | 6.07 us: 1.16x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 81.1 ms: 1.16x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 41.2 us: 1.17x slower                                                    |
| unpickle                 | 17.5 us                                                               | 20.9 us: 1.20x slower                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.90 ms: 1.20x slower                                                    |
| async_generators         | 452 ms                                                                | 542 ms: 1.20x slower                                                     |
| meteor_contest           | 126 ms                                                                | 154 ms: 1.22x slower                                                     |
| mako                     | 18.9 ms                                                               | 23.4 ms: 1.24x slower                                                    |
| fannkuch                 | 546 ms                                                                | 688 ms: 1.26x slower                                                     |
| json_loads               | 30.9 us                                                               | 39.9 us: 1.29x slower                                                    |
| pickle                   | 12.5 us                                                               | 16.7 us: 1.33x slower                                                    |
| telco                    | 8.49 ms                                                               | 11.7 ms: 1.38x slower                                                    |
| coverage                 | 83.6 ms                                                               | 135 ms: 1.61x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 12.3 ms: 1.78x slower                                                    |
| python_startup           | 11.2 ms                                                               | 20.1 ms: 1.80x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 58.5 ms: 4.03x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (16): create_gc_cycles, scimark_fft, dulwich_log, regex_v8, sqlalchemy_declarative, sqlglot_normalize, thrift, pprint_pformat, pprint_safe_repr, 2to3, deepcopy_reduce, sqlglot_optimize, xml_etree_process, regex_dna, pidigits, json_dumps
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250208-3.14.0a4+-29f8a67-NOGIL/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.105x faster

# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.58x
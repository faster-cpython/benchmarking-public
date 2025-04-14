# Results vs. 3.10.4

- fork: mdboom
- ref: aa_test_2025
- machine: linux-x86_64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.232x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.51x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 312 ms: 1.12x faster                                           |
| docutils       | 3.30 sec                                               | 2.87 sec: 1.15x faster                                         |
| html5lib       | 88.9 ms                                                | 70.3 ms: 1.26x faster                                          |
| Geometric mean | (ref)                                                  | 1.18x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 606 ms: 2.92x faster                                           |
| async_tree_none         | 728 ms                                                 | 292 ms: 2.50x faster                                           |
| async_tree_memoization  | 870 ms                                                 | 372 ms: 2.34x faster                                           |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 534 ms: 1.90x faster                                           |
| Geometric mean          | (ref)                                                  | 2.38x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 117 ms                                                 | 78.3 ms: 1.49x faster                                          |
| nbody          | 154 ms                                                 | 137 ms: 1.12x faster                                           |
| pidigits       | 191 ms                                                 | 181 ms: 1.05x faster                                           |
| Geometric mean | (ref)                                                  | 1.21x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 152 ms: 1.24x faster                                           |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                          |
| regex_effbot   | 3.63 ms                                                | 3.48 ms: 1.04x faster                                          |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                  | 1.09x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.43 sec: 1.29x faster                                         |
| pickle_pure_python   | 484 us                                                 | 385 us: 1.26x faster                                           |
| unpickle_pure_python | 331 us                                                 | 270 us: 1.22x faster                                           |
| xml_etree_iterparse  | 115 ms                                                 | 95.6 ms: 1.21x faster                                          |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.13x faster                                           |
| json_dumps           | 14.2 ms                                                | 12.8 ms: 1.11x faster                                          |
| xml_etree_process    | 79.1 ms                                                | 72.5 ms: 1.09x faster                                          |
| xml_etree_generate   | 99.4 ms                                                | 96.6 ms: 1.03x faster                                          |
| json_loads           | 31.2 us                                                | 31.8 us: 1.02x slower                                          |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 15.1 ms: 1.03x slower                                          |
| python_startup_no_site | 5.93 ms                                                | 9.35 ms: 1.58x slower                                          |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 41.6 ms: 1.16x faster                                          |
| genshi_text     | 31.8 ms                                                | 29.5 ms: 1.08x faster                                          |
| genshi_xml      | 66.0 ms                                                | 62.1 ms: 1.06x faster                                          |
| mako            | 16.3 ms                                                | 16.4 ms: 1.01x slower                                          |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 606 ms: 2.92x faster                                           |
| typing_runtime_protocols | 544 us                                                 | 215 us: 2.53x faster                                           |
| generators               | 80.1 ms                                                | 31.7 ms: 2.53x faster                                          |
| async_tree_none          | 728 ms                                                 | 292 ms: 2.50x faster                                           |
| async_tree_memoization   | 870 ms                                                 | 372 ms: 2.34x faster                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 534 ms: 1.90x faster                                           |
| pylint                   | 551 ms                                                 | 317 ms: 1.74x faster                                           |
| deltablue                | 7.91 ms                                                | 4.70 ms: 1.68x faster                                          |
| go                       | 240 ms                                                 | 144 ms: 1.67x faster                                           |
| logging_silent           | 190 ns                                                 | 117 ns: 1.61x faster                                           |
| scimark_sor              | 220 ms                                                 | 142 ms: 1.54x faster                                           |
| chaos                    | 115 ms                                                 | 75.0 ms: 1.54x faster                                          |
| deepcopy                 | 479 us                                                 | 317 us: 1.51x faster                                           |
| richards_super           | 94.7 ms                                                | 62.8 ms: 1.51x faster                                          |
| float                    | 117 ms                                                 | 78.3 ms: 1.49x faster                                          |
| deepcopy_memo            | 58.5 us                                                | 39.7 us: 1.47x faster                                          |
| spectral_norm            | 170 ms                                                 | 116 ms: 1.47x faster                                           |
| richards                 | 79.3 ms                                                | 54.2 ms: 1.46x faster                                          |
| raytrace                 | 507 ms                                                 | 356 ms: 1.42x faster                                           |
| crypto_pyaes             | 128 ms                                                 | 91.3 ms: 1.40x faster                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.56 ms: 1.39x faster                                          |
| comprehensions           | 28.8 us                                                | 20.9 us: 1.37x faster                                          |
| pyflate                  | 716 ms                                                 | 523 ms: 1.37x faster                                           |
| coroutines               | 35.1 ms                                                | 25.8 ms: 1.36x faster                                          |
| scimark_monte_carlo      | 118 ms                                                 | 87.8 ms: 1.35x faster                                          |
| hexiom                   | 10.4 ms                                                | 7.83 ms: 1.33x faster                                          |
| sqlglot_transpile        | 2.57 ms                                                | 1.96 ms: 1.31x faster                                          |
| tomli_loads              | 3.14 sec                                               | 2.43 sec: 1.29x faster                                         |
| deepcopy_reduce          | 4.17 us                                                | 3.27 us: 1.28x faster                                          |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                          |
| pycparser                | 1.58 sec                                               | 1.24 sec: 1.27x faster                                         |
| html5lib                 | 88.9 ms                                                | 70.3 ms: 1.26x faster                                          |
| pickle_pure_python       | 484 us                                                 | 385 us: 1.26x faster                                           |
| scimark_lu               | 176 ms                                                 | 140 ms: 1.25x faster                                           |
| regex_compile            | 188 ms                                                 | 152 ms: 1.24x faster                                           |
| unpickle_pure_python     | 331 us                                                 | 270 us: 1.22x faster                                           |
| xml_etree_iterparse      | 115 ms                                                 | 95.6 ms: 1.21x faster                                          |
| logging_simple           | 8.30 us                                                | 6.93 us: 1.20x faster                                          |
| dulwich_log              | 84.3 ms                                                | 70.4 ms: 1.20x faster                                          |
| sqlglot_normalize        | 143 ms                                                 | 121 ms: 1.18x faster                                           |
| pprint_pformat           | 2.10 sec                                               | 1.79 sec: 1.18x faster                                         |
| pprint_safe_repr         | 1.02 sec                                               | 869 ms: 1.17x faster                                           |
| logging_format           | 9.09 us                                                | 7.78 us: 1.17x faster                                          |
| django_template          | 48.2 ms                                                | 41.6 ms: 1.16x faster                                          |
| docutils                 | 3.30 sec                                               | 2.87 sec: 1.15x faster                                         |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.13x faster                                           |
| sqlglot_optimize         | 69.2 ms                                                | 61.0 ms: 1.13x faster                                          |
| nbody                    | 154 ms                                                 | 137 ms: 1.12x faster                                           |
| 2to3                     | 348 ms                                                 | 312 ms: 1.12x faster                                           |
| scimark_fft              | 466 ms                                                 | 419 ms: 1.11x faster                                           |
| thrift                   | 1.07 ms                                                | 968 us: 1.11x faster                                           |
| sqlalchemy_imperative    | 23.3 ms                                                | 21.1 ms: 1.11x faster                                          |
| json_dumps               | 14.2 ms                                                | 12.8 ms: 1.11x faster                                          |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                          |
| sympy_sum                | 196 ms                                                 | 180 ms: 1.09x faster                                           |
| xml_etree_process        | 79.1 ms                                                | 72.5 ms: 1.09x faster                                          |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                          |
| genshi_text              | 31.8 ms                                                | 29.5 ms: 1.08x faster                                          |
| sympy_str                | 346 ms                                                 | 322 ms: 1.07x faster                                           |
| sympy_integrate          | 25.8 ms                                                | 24.1 ms: 1.07x faster                                          |
| nqueens                  | 106 ms                                                 | 99.1 ms: 1.07x faster                                          |
| genshi_xml               | 66.0 ms                                                | 62.1 ms: 1.06x faster                                          |
| sympy_expand             | 566 ms                                                 | 534 ms: 1.06x faster                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.12 ms: 1.06x faster                                          |
| pidigits                 | 191 ms                                                 | 181 ms: 1.05x faster                                           |
| fannkuch                 | 532 ms                                                 | 507 ms: 1.05x faster                                           |
| regex_effbot             | 3.63 ms                                                | 3.48 ms: 1.04x faster                                          |
| sqlalchemy_declarative   | 172 ms                                                 | 165 ms: 1.04x faster                                           |
| mdp                      | 2.85 sec                                               | 2.75 sec: 1.04x faster                                         |
| xml_etree_generate       | 99.4 ms                                                | 96.6 ms: 1.03x faster                                          |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                           |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                           |
| json                     | 5.69 ms                                                | 5.63 ms: 1.01x faster                                          |
| mako                     | 16.3 ms                                                | 16.4 ms: 1.01x slower                                          |
| json_loads               | 31.2 us                                                | 31.8 us: 1.02x slower                                          |
| python_startup           | 14.6 ms                                                | 15.1 ms: 1.03x slower                                          |
| create_gc_cycles         | 1.62 ms                                                | 1.72 ms: 1.06x slower                                          |
| meteor_contest           | 120 ms                                                 | 134 ms: 1.12x slower                                           |
| gc_traversal             | 3.62 ms                                                | 4.45 ms: 1.23x slower                                          |
| telco                    | 7.27 ms                                                | 9.14 ms: 1.26x slower                                          |
| coverage                 | 79.4 ms                                                | 107 ms: 1.35x slower                                           |
| python_startup_no_site   | 5.93 ms                                                | 9.35 ms: 1.58x slower                                          |
| bench_thread_pool        | 986 us                                                 | 3.49 ms: 3.54x slower                                          |
| bench_mp_pool            | 24.0 ms                                                | 89.6 ms: 3.73x slower                                          |
| Geometric mean           | (ref)                                                  | 1.19x faster                                                   |

Benchmark hidden because not significant (1): async_generators
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250121-3.14.0a4+-4844db8-NOGIL/bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.232x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.51x
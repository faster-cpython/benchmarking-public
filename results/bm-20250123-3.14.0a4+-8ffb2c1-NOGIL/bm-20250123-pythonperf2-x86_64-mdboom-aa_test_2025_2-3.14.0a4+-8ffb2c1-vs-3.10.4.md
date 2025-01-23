# Results vs. 3.10.4

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-x86_64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.182x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.54x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 337 ms: 1.04x faster                                                   |
| docutils       | 3.41 sec                                                     | 2.96 sec: 1.15x faster                                                 |
| html5lib       | 94.6 ms                                                      | 73.5 ms: 1.29x faster                                                  |
| Geometric mean | (ref)                                                        | 1.16x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 608 ms: 2.63x faster                                                   |
| async_tree_none         | 692 ms                                                       | 289 ms: 2.39x faster                                                   |
| async_tree_memoization  | 819 ms                                                       | 357 ms: 2.30x faster                                                   |
| async_tree_cpu_io_mixed | 936 ms                                                       | 525 ms: 1.78x faster                                                   |
| Geometric mean          | (ref)                                                        | 2.25x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 111 ms                                                       | 76.0 ms: 1.46x faster                                                  |
| pidigits       | 271 ms                                                       | 249 ms: 1.09x faster                                                   |
| Geometric mean | (ref)                                                        | 1.17x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 155 ms: 1.22x faster                                                   |
| regex_dna      | 261 ms                                                       | 239 ms: 1.09x faster                                                   |
| regex_v8       | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                  |
| regex_effbot   | 3.09 ms                                                      | 3.27 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                        | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 254 us: 1.23x faster                                                   |
| tomli_loads          | 2.92 sec                                                     | 2.40 sec: 1.21x faster                                                 |
| xml_etree_iterparse  | 110 ms                                                       | 91.2 ms: 1.21x faster                                                  |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                   |
| pickle_pure_python   | 455 us                                                       | 392 us: 1.16x faster                                                   |
| json_dumps           | 14.5 ms                                                      | 13.4 ms: 1.09x faster                                                  |
| json_loads           | 30.3 us                                                      | 28.4 us: 1.07x faster                                                  |
| xml_etree_process    | 75.9 ms                                                      | 74.4 ms: 1.02x faster                                                  |
| xml_etree_generate   | 92.3 ms                                                      | 98.4 ms: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 11.7 ms: 1.60x slower                                                  |
| python_startup         | 11.5 ms                                                      | 18.7 ms: 1.62x slower                                                  |
| Geometric mean         | (ref)                                                        | 1.61x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 46.3 ms: 1.08x faster                                                  |
| genshi_text     | 31.4 ms                                                      | 30.6 ms: 1.03x faster                                                  |
| genshi_xml      | 63.3 ms                                                      | 65.2 ms: 1.03x slower                                                  |
| mako            | 14.7 ms                                                      | 17.7 ms: 1.20x slower                                                  |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 608 ms: 2.63x faster                                                   |
| async_tree_none          | 692 ms                                                       | 289 ms: 2.39x faster                                                   |
| typing_runtime_protocols | 537 us                                                       | 226 us: 2.38x faster                                                   |
| async_tree_memoization   | 819 ms                                                       | 357 ms: 2.30x faster                                                   |
| generators               | 57.3 ms                                                      | 31.4 ms: 1.82x faster                                                  |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 525 ms: 1.78x faster                                                   |
| go                       | 262 ms                                                       | 149 ms: 1.76x faster                                                   |
| deltablue                | 7.50 ms                                                      | 4.47 ms: 1.68x faster                                                  |
| pylint                   | 566 ms                                                       | 350 ms: 1.62x faster                                                   |
| chaos                    | 109 ms                                                       | 69.8 ms: 1.56x faster                                                  |
| scimark_sor              | 180 ms                                                       | 119 ms: 1.52x faster                                                   |
| logging_silent           | 167 ns                                                       | 110 ns: 1.51x faster                                                   |
| pyflate                  | 733 ms                                                       | 494 ms: 1.48x faster                                                   |
| float                    | 111 ms                                                       | 76.0 ms: 1.46x faster                                                  |
| raytrace                 | 489 ms                                                       | 341 ms: 1.44x faster                                                   |
| deepcopy                 | 468 us                                                       | 335 us: 1.40x faster                                                   |
| sqlglot_parse            | 2.24 ms                                                      | 1.60 ms: 1.40x faster                                                  |
| scimark_lu               | 167 ms                                                       | 120 ms: 1.39x faster                                                   |
| spectral_norm            | 139 ms                                                       | 101 ms: 1.38x faster                                                   |
| coroutines               | 30.3 ms                                                      | 22.2 ms: 1.37x faster                                                  |
| richards_super           | 90.6 ms                                                      | 67.0 ms: 1.35x faster                                                  |
| pathlib                  | 21.4 ms                                                      | 16.2 ms: 1.32x faster                                                  |
| deepcopy_memo            | 49.8 us                                                      | 37.9 us: 1.31x faster                                                  |
| richards                 | 75.1 ms                                                      | 57.5 ms: 1.31x faster                                                  |
| hexiom                   | 9.42 ms                                                      | 7.25 ms: 1.30x faster                                                  |
| pycparser                | 1.67 sec                                                     | 1.29 sec: 1.30x faster                                                 |
| sqlglot_transpile        | 2.68 ms                                                      | 2.08 ms: 1.29x faster                                                  |
| html5lib                 | 94.6 ms                                                      | 73.5 ms: 1.29x faster                                                  |
| crypto_pyaes             | 119 ms                                                       | 92.6 ms: 1.29x faster                                                  |
| scimark_monte_carlo      | 107 ms                                                       | 85.8 ms: 1.25x faster                                                  |
| comprehensions           | 26.7 us                                                      | 21.5 us: 1.24x faster                                                  |
| unpickle_pure_python     | 312 us                                                       | 254 us: 1.23x faster                                                   |
| regex_compile            | 190 ms                                                       | 155 ms: 1.22x faster                                                   |
| tomli_loads              | 2.92 sec                                                     | 2.40 sec: 1.21x faster                                                 |
| xml_etree_iterparse      | 110 ms                                                       | 91.2 ms: 1.21x faster                                                  |
| logging_simple           | 8.88 us                                                      | 7.43 us: 1.19x faster                                                  |
| logging_format           | 9.64 us                                                      | 8.15 us: 1.18x faster                                                  |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                   |
| pickle_pure_python       | 455 us                                                       | 392 us: 1.16x faster                                                   |
| dulwich_log              | 81.1 ms                                                      | 70.0 ms: 1.16x faster                                                  |
| sqlite_synth             | 2.99 us                                                      | 2.58 us: 1.16x faster                                                  |
| docutils                 | 3.41 sec                                                     | 2.96 sec: 1.15x faster                                                 |
| pprint_safe_repr         | 1.05 sec                                                     | 915 ms: 1.15x faster                                                   |
| pprint_pformat           | 2.15 sec                                                     | 1.89 sec: 1.14x faster                                                 |
| thrift                   | 1.18 ms                                                      | 1.05 ms: 1.12x faster                                                  |
| sqlglot_normalize        | 144 ms                                                       | 129 ms: 1.11x faster                                                   |
| deepcopy_reduce          | 4.01 us                                                      | 3.62 us: 1.11x faster                                                  |
| sympy_sum                | 193 ms                                                       | 177 ms: 1.09x faster                                                   |
| regex_dna                | 261 ms                                                       | 239 ms: 1.09x faster                                                   |
| json_dumps               | 14.5 ms                                                      | 13.4 ms: 1.09x faster                                                  |
| mdp                      | 3.01 sec                                                     | 2.76 sec: 1.09x faster                                                 |
| pidigits                 | 271 ms                                                       | 249 ms: 1.09x faster                                                   |
| sqlalchemy_imperative    | 22.7 ms                                                      | 20.9 ms: 1.09x faster                                                  |
| django_template          | 50.2 ms                                                      | 46.3 ms: 1.08x faster                                                  |
| scimark_fft              | 361 ms                                                       | 336 ms: 1.08x faster                                                   |
| sqlglot_optimize         | 70.1 ms                                                      | 65.3 ms: 1.07x faster                                                  |
| sqlalchemy_declarative   | 190 ms                                                       | 177 ms: 1.07x faster                                                   |
| json_loads               | 30.3 us                                                      | 28.4 us: 1.07x faster                                                  |
| sympy_expand             | 600 ms                                                       | 565 ms: 1.06x faster                                                   |
| sympy_str                | 360 ms                                                       | 339 ms: 1.06x faster                                                   |
| json                     | 5.86 ms                                                      | 5.58 ms: 1.05x faster                                                  |
| regex_v8                 | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                  |
| sympy_integrate          | 28.2 ms                                                      | 27.1 ms: 1.04x faster                                                  |
| 2to3                     | 350 ms                                                       | 337 ms: 1.04x faster                                                   |
| genshi_text              | 31.4 ms                                                      | 30.6 ms: 1.03x faster                                                  |
| nqueens                  | 115 ms                                                       | 112 ms: 1.03x faster                                                   |
| asyncio_websockets       | 390 ms                                                       | 382 ms: 1.02x faster                                                   |
| xml_etree_process        | 75.9 ms                                                      | 74.4 ms: 1.02x faster                                                  |
| fannkuch                 | 483 ms                                                       | 489 ms: 1.01x slower                                                   |
| genshi_xml               | 63.3 ms                                                      | 65.2 ms: 1.03x slower                                                  |
| regex_effbot             | 3.09 ms                                                      | 3.27 ms: 1.06x slower                                                  |
| xml_etree_generate       | 92.3 ms                                                      | 98.4 ms: 1.07x slower                                                  |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.43 ms: 1.07x slower                                                  |
| async_generators         | 421 ms                                                       | 466 ms: 1.11x slower                                                   |
| meteor_contest           | 138 ms                                                       | 153 ms: 1.11x slower                                                   |
| create_gc_cycles         | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                  |
| mako                     | 14.7 ms                                                      | 17.7 ms: 1.20x slower                                                  |
| telco                    | 7.23 ms                                                      | 9.13 ms: 1.26x slower                                                  |
| bench_thread_pool        | 1.14 ms                                                      | 1.46 ms: 1.28x slower                                                  |
| gc_traversal             | 3.42 ms                                                      | 4.95 ms: 1.45x slower                                                  |
| python_startup_no_site   | 7.33 ms                                                      | 11.7 ms: 1.60x slower                                                  |
| python_startup           | 11.5 ms                                                      | 18.7 ms: 1.62x slower                                                  |
| coverage                 | 63.3 ms                                                      | 103 ms: 1.63x slower                                                   |
| bench_mp_pool            | 6.37 ms                                                      | 48.9 ms: 7.68x slower                                                  |
| Geometric mean           | (ref)                                                        | 1.15x faster                                                           |

Benchmark hidden because not significant (1): nbody
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250123-3.14.0a4+-8ffb2c1-NOGIL/bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.182x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.54x
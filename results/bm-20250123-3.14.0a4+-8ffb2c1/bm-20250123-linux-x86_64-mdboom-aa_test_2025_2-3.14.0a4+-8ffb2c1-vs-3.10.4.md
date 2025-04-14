# Results vs. 3.10.4

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-x86_64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.439x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                             |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                           |
| html5lib       | 88.9 ms                                                | 62.2 ms: 1.43x faster                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 598 ms: 2.96x faster                                             |
| async_tree_none         | 728 ms                                                 | 254 ms: 2.87x faster                                             |
| async_tree_memoization  | 870 ms                                                 | 321 ms: 2.71x faster                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 490 ms: 2.07x faster                                             |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 117 ms                                                 | 71.9 ms: 1.63x faster                                            |
| nbody          | 154 ms                                                 | 96.2 ms: 1.60x faster                                            |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.39x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                             |
| regex_effbot   | 3.63 ms                                                | 3.24 ms: 1.12x faster                                            |
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                            |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                             |
| Geometric mean | (ref)                                                  | 1.18x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.99 sec: 1.58x faster                                           |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                             |
| unpickle_pure_python | 331 us                                                 | 226 us: 1.47x faster                                             |
| xml_etree_process    | 79.1 ms                                                | 61.4 ms: 1.29x faster                                            |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                             |
| json_dumps           | 14.2 ms                                                | 11.9 ms: 1.19x faster                                            |
| xml_etree_iterparse  | 115 ms                                                 | 97.1 ms: 1.19x faster                                            |
| xml_etree_generate   | 99.4 ms                                                | 84.5 ms: 1.18x faster                                            |
| json_loads           | 31.2 us                                                | 29.2 us: 1.07x faster                                            |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                            |
| python_startup_no_site | 5.93 ms                                                | 7.11 ms: 1.20x slower                                            |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.2 ms: 1.49x faster                                            |
| mako            | 16.3 ms                                                | 11.1 ms: 1.46x faster                                            |
| genshi_text     | 31.8 ms                                                | 21.9 ms: 1.45x faster                                            |
| genshi_xml      | 66.0 ms                                                | 49.7 ms: 1.33x faster                                            |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.35x faster                                             |
| async_tree_io            | 1.77 sec                                               | 598 ms: 2.96x faster                                             |
| generators               | 80.1 ms                                                | 27.7 ms: 2.89x faster                                            |
| async_tree_none          | 728 ms                                                 | 254 ms: 2.87x faster                                             |
| async_tree_memoization   | 870 ms                                                 | 321 ms: 2.71x faster                                             |
| deltablue                | 7.91 ms                                                | 3.16 ms: 2.50x faster                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 490 ms: 2.07x faster                                             |
| go                       | 240 ms                                                 | 116 ms: 2.06x faster                                             |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                             |
| chaos                    | 115 ms                                                 | 58.0 ms: 1.99x faster                                            |
| deepcopy_memo            | 58.5 us                                                | 30.8 us: 1.90x faster                                            |
| richards_super           | 94.7 ms                                                | 50.1 ms: 1.89x faster                                            |
| raytrace                 | 507 ms                                                 | 270 ms: 1.87x faster                                             |
| deepcopy                 | 479 us                                                 | 257 us: 1.86x faster                                             |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                             |
| richards                 | 79.3 ms                                                | 43.8 ms: 1.81x faster                                            |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.81x faster                                             |
| scimark_monte_carlo      | 118 ms                                                 | 67.0 ms: 1.76x faster                                            |
| crypto_pyaes             | 128 ms                                                 | 73.4 ms: 1.74x faster                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.25 ms: 1.73x faster                                            |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.55 ms: 1.66x faster                                            |
| hexiom                   | 10.4 ms                                                | 6.28 ms: 1.65x faster                                            |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                             |
| float                    | 117 ms                                                 | 71.9 ms: 1.63x faster                                            |
| nbody                    | 154 ms                                                 | 96.2 ms: 1.60x faster                                            |
| pyflate                  | 716 ms                                                 | 450 ms: 1.59x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.63 us: 1.59x faster                                            |
| tomli_loads              | 3.14 sec                                               | 1.99 sec: 1.58x faster                                           |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                             |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.49x faster                                            |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                             |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.47x faster                                            |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                             |
| unpickle_pure_python     | 331 us                                                 | 226 us: 1.47x faster                                             |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.46x faster                                            |
| genshi_text              | 31.8 ms                                                | 21.9 ms: 1.45x faster                                            |
| logging_simple           | 8.30 us                                                | 5.77 us: 1.44x faster                                            |
| html5lib                 | 88.9 ms                                                | 62.2 ms: 1.43x faster                                            |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                           |
| logging_format           | 9.09 us                                                | 6.44 us: 1.41x faster                                            |
| pprint_safe_repr         | 1.02 sec                                               | 724 ms: 1.41x faster                                             |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.40x faster                                            |
| thrift                   | 1.07 ms                                                | 769 us: 1.39x faster                                             |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.39x faster                                           |
| sqlglot_normalize        | 143 ms                                                 | 105 ms: 1.36x faster                                             |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                             |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                             |
| scimark_fft              | 466 ms                                                 | 349 ms: 1.33x faster                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.85 ms: 1.33x faster                                            |
| genshi_xml               | 66.0 ms                                                | 49.7 ms: 1.33x faster                                            |
| nqueens                  | 106 ms                                                 | 80.2 ms: 1.32x faster                                            |
| fannkuch                 | 532 ms                                                 | 404 ms: 1.32x faster                                             |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                             |
| sqlglot_optimize         | 69.2 ms                                                | 53.0 ms: 1.31x faster                                            |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                            |
| dulwich_log              | 84.3 ms                                                | 65.1 ms: 1.29x faster                                            |
| xml_etree_process        | 79.1 ms                                                | 61.4 ms: 1.29x faster                                            |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                             |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                           |
| sympy_expand             | 566 ms                                                 | 454 ms: 1.25x faster                                             |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.24x faster                                            |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                             |
| json_dumps               | 14.2 ms                                                | 11.9 ms: 1.19x faster                                            |
| xml_etree_iterparse      | 115 ms                                                 | 97.1 ms: 1.19x faster                                            |
| xml_etree_generate       | 99.4 ms                                                | 84.5 ms: 1.18x faster                                            |
| bench_thread_pool        | 986 us                                                 | 866 us: 1.14x faster                                             |
| mdp                      | 2.85 sec                                               | 2.51 sec: 1.13x faster                                           |
| async_generators         | 444 ms                                                 | 391 ms: 1.13x faster                                             |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                            |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                             |
| regex_effbot             | 3.63 ms                                                | 3.24 ms: 1.12x faster                                            |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                            |
| json                     | 5.69 ms                                                | 5.23 ms: 1.09x faster                                            |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                            |
| json_loads               | 31.2 us                                                | 29.2 us: 1.07x faster                                            |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                             |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                             |
| telco                    | 7.27 ms                                                | 7.99 ms: 1.10x slower                                            |
| coverage                 | 79.4 ms                                                | 90.7 ms: 1.14x slower                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.11 ms: 1.20x slower                                            |
| gc_traversal             | 3.62 ms                                                | 5.03 ms: 1.39x slower                                            |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                            |
| bench_mp_pool            | 24.0 ms                                                | 81.8 ms: 3.41x slower                                            |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                     |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250123-3.14.0a4+-8ffb2c1/bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.439x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.26x
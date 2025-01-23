# Results vs. 3.10.4

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-x86_64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.235x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.51x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 309 ms: 1.13x faster                                             |
| docutils       | 3.30 sec                                               | 2.83 sec: 1.16x faster                                           |
| html5lib       | 88.9 ms                                                | 69.0 ms: 1.29x faster                                            |
| Geometric mean | (ref)                                                  | 1.19x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 596 ms: 2.97x faster                                             |
| async_tree_none         | 728 ms                                                 | 287 ms: 2.54x faster                                             |
| async_tree_memoization  | 870 ms                                                 | 366 ms: 2.38x faster                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 528 ms: 1.93x faster                                             |
| Geometric mean          | (ref)                                                  | 2.42x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 117 ms                                                 | 79.1 ms: 1.48x faster                                            |
| nbody          | 154 ms                                                 | 140 ms: 1.10x faster                                             |
| pidigits       | 191 ms                                                 | 181 ms: 1.05x faster                                             |
| Geometric mean | (ref)                                                  | 1.20x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 150 ms: 1.25x faster                                             |
| regex_v8       | 27.8 ms                                                | 25.3 ms: 1.10x faster                                            |
| regex_effbot   | 3.63 ms                                                | 3.48 ms: 1.04x faster                                            |
| regex_dna      | 227 ms                                                 | 223 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.10x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.41 sec: 1.30x faster                                           |
| pickle_pure_python   | 484 us                                                 | 380 us: 1.27x faster                                             |
| unpickle_pure_python | 331 us                                                 | 270 us: 1.22x faster                                             |
| xml_etree_iterparse  | 115 ms                                                 | 95.2 ms: 1.21x faster                                            |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                             |
| json_dumps           | 14.2 ms                                                | 12.9 ms: 1.10x faster                                            |
| xml_etree_process    | 79.1 ms                                                | 72.1 ms: 1.10x faster                                            |
| xml_etree_generate   | 99.4 ms                                                | 96.3 ms: 1.03x faster                                            |
| json_loads           | 31.2 us                                                | 31.8 us: 1.02x slower                                            |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 15.0 ms: 1.03x slower                                            |
| python_startup_no_site | 5.93 ms                                                | 9.34 ms: 1.57x slower                                            |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 41.7 ms: 1.15x faster                                            |
| genshi_text     | 31.8 ms                                                | 29.0 ms: 1.10x faster                                            |
| genshi_xml      | 66.0 ms                                                | 61.4 ms: 1.08x faster                                            |
| mako            | 16.3 ms                                                | 16.5 ms: 1.01x slower                                            |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 596 ms: 2.97x faster                                             |
| generators               | 80.1 ms                                                | 30.8 ms: 2.60x faster                                            |
| async_tree_none          | 728 ms                                                 | 287 ms: 2.54x faster                                             |
| typing_runtime_protocols | 544 us                                                 | 215 us: 2.54x faster                                             |
| async_tree_memoization   | 870 ms                                                 | 366 ms: 2.38x faster                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 528 ms: 1.93x faster                                             |
| pylint                   | 551 ms                                                 | 316 ms: 1.74x faster                                             |
| deltablue                | 7.91 ms                                                | 4.68 ms: 1.69x faster                                            |
| go                       | 240 ms                                                 | 142 ms: 1.69x faster                                             |
| logging_silent           | 190 ns                                                 | 121 ns: 1.57x faster                                             |
| chaos                    | 115 ms                                                 | 74.0 ms: 1.56x faster                                            |
| scimark_sor              | 220 ms                                                 | 143 ms: 1.53x faster                                             |
| richards_super           | 94.7 ms                                                | 62.3 ms: 1.52x faster                                            |
| deepcopy                 | 479 us                                                 | 318 us: 1.51x faster                                             |
| float                    | 117 ms                                                 | 79.1 ms: 1.48x faster                                            |
| richards                 | 79.3 ms                                                | 53.8 ms: 1.47x faster                                            |
| deepcopy_memo            | 58.5 us                                                | 39.9 us: 1.46x faster                                            |
| raytrace                 | 507 ms                                                 | 356 ms: 1.43x faster                                             |
| spectral_norm            | 170 ms                                                 | 119 ms: 1.42x faster                                             |
| crypto_pyaes             | 128 ms                                                 | 90.8 ms: 1.41x faster                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.56 ms: 1.39x faster                                            |
| comprehensions           | 28.8 us                                                | 20.9 us: 1.38x faster                                            |
| pyflate                  | 716 ms                                                 | 528 ms: 1.36x faster                                             |
| scimark_monte_carlo      | 118 ms                                                 | 87.3 ms: 1.35x faster                                            |
| hexiom                   | 10.4 ms                                                | 7.78 ms: 1.34x faster                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.95 ms: 1.32x faster                                            |
| coroutines               | 35.1 ms                                                | 26.7 ms: 1.31x faster                                            |
| tomli_loads              | 3.14 sec                                               | 2.41 sec: 1.30x faster                                           |
| html5lib                 | 88.9 ms                                                | 69.0 ms: 1.29x faster                                            |
| pycparser                | 1.58 sec                                               | 1.23 sec: 1.28x faster                                           |
| pickle_pure_python       | 484 us                                                 | 380 us: 1.27x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 3.30 us: 1.26x faster                                            |
| regex_compile            | 188 ms                                                 | 150 ms: 1.25x faster                                             |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                            |
| scimark_lu               | 176 ms                                                 | 143 ms: 1.24x faster                                             |
| unpickle_pure_python     | 331 us                                                 | 270 us: 1.22x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 95.2 ms: 1.21x faster                                            |
| logging_simple           | 8.30 us                                                | 6.90 us: 1.20x faster                                            |
| dulwich_log              | 84.3 ms                                                | 70.1 ms: 1.20x faster                                            |
| sqlglot_normalize        | 143 ms                                                 | 121 ms: 1.18x faster                                             |
| pprint_pformat           | 2.10 sec                                               | 1.78 sec: 1.18x faster                                           |
| pprint_safe_repr         | 1.02 sec                                               | 865 ms: 1.18x faster                                             |
| logging_format           | 9.09 us                                                | 7.74 us: 1.17x faster                                            |
| docutils                 | 3.30 sec                                               | 2.83 sec: 1.16x faster                                           |
| django_template          | 48.2 ms                                                | 41.7 ms: 1.15x faster                                            |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                             |
| sqlglot_optimize         | 69.2 ms                                                | 60.7 ms: 1.14x faster                                            |
| 2to3                     | 348 ms                                                 | 309 ms: 1.13x faster                                             |
| sqlalchemy_imperative    | 23.3 ms                                                | 20.8 ms: 1.12x faster                                            |
| thrift                   | 1.07 ms                                                | 960 us: 1.12x faster                                             |
| sympy_sum                | 196 ms                                                 | 178 ms: 1.10x faster                                             |
| json_dumps               | 14.2 ms                                                | 12.9 ms: 1.10x faster                                            |
| regex_v8                 | 27.8 ms                                                | 25.3 ms: 1.10x faster                                            |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                            |
| genshi_text              | 31.8 ms                                                | 29.0 ms: 1.10x faster                                            |
| xml_etree_process        | 79.1 ms                                                | 72.1 ms: 1.10x faster                                            |
| nbody                    | 154 ms                                                 | 140 ms: 1.10x faster                                             |
| scimark_fft              | 466 ms                                                 | 429 ms: 1.09x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 23.8 ms: 1.08x faster                                            |
| sympy_str                | 346 ms                                                 | 321 ms: 1.08x faster                                             |
| genshi_xml               | 66.0 ms                                                | 61.4 ms: 1.08x faster                                            |
| nqueens                  | 106 ms                                                 | 99.3 ms: 1.07x faster                                            |
| sympy_expand             | 566 ms                                                 | 536 ms: 1.06x faster                                             |
| sqlalchemy_declarative   | 172 ms                                                 | 163 ms: 1.05x faster                                             |
| pidigits                 | 191 ms                                                 | 181 ms: 1.05x faster                                             |
| regex_effbot             | 3.63 ms                                                | 3.48 ms: 1.04x faster                                            |
| mdp                      | 2.85 sec                                               | 2.74 sec: 1.04x faster                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.24 ms: 1.04x faster                                            |
| fannkuch                 | 532 ms                                                 | 514 ms: 1.03x faster                                             |
| xml_etree_generate       | 99.4 ms                                                | 96.3 ms: 1.03x faster                                            |
| regex_dna                | 227 ms                                                 | 223 ms: 1.01x faster                                             |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                             |
| async_generators         | 444 ms                                                 | 438 ms: 1.01x faster                                             |
| mako                     | 16.3 ms                                                | 16.5 ms: 1.01x slower                                            |
| json_loads               | 31.2 us                                                | 31.8 us: 1.02x slower                                            |
| python_startup           | 14.6 ms                                                | 15.0 ms: 1.03x slower                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.70 ms: 1.05x slower                                            |
| meteor_contest           | 120 ms                                                 | 133 ms: 1.11x slower                                             |
| gc_traversal             | 3.62 ms                                                | 4.17 ms: 1.15x slower                                            |
| telco                    | 7.27 ms                                                | 9.10 ms: 1.25x slower                                            |
| coverage                 | 79.4 ms                                                | 108 ms: 1.36x slower                                             |
| python_startup_no_site   | 5.93 ms                                                | 9.34 ms: 1.57x slower                                            |
| bench_thread_pool        | 986 us                                                 | 3.50 ms: 3.55x slower                                            |
| bench_mp_pool            | 24.0 ms                                                | 89.3 ms: 3.72x slower                                            |
| Geometric mean           | (ref)                                                  | 1.20x faster                                                     |

Benchmark hidden because not significant (1): json
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250123-3.14.0a4+-8ffb2c1-NOGIL/bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.235x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.51x
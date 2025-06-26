# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.440x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                  |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                |
| html5lib       | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                 |
| Geometric mean | (ref)                                                  | 1.35x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 601 ms: 2.94x faster                                                  |
| async_tree_none         | 728 ms                                                 | 264 ms: 2.76x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 497 ms: 2.04x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 73.4 ms: 1.60x faster                                                 |
| nbody          | 154 ms                                                 | 99.4 ms: 1.54x faster                                                 |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| regex_v8       | 27.8 ms                                                | 23.3 ms: 1.19x faster                                                 |
| regex_dna      | 227 ms                                                 | 203 ms: 1.12x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.29 ms: 1.10x faster                                                 |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.01 sec: 1.57x faster                                                |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 60.5 ms: 1.31x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.19x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 98.9 ms: 1.17x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.3 ms: 1.16x faster                                                 |
| json_loads           | 31.2 us                                                | 28.2 us: 1.11x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.91 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.4 ms: 1.49x faster                                                 |
| genshi_text     | 31.8 ms                                                | 22.0 ms: 1.45x faster                                                 |
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 50.3 ms: 1.31x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 601 ms: 2.94x faster                                                  |
| async_tree_none          | 728 ms                                                 | 264 ms: 2.76x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                                  |
| generators               | 80.1 ms                                                | 29.8 ms: 2.69x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                                |
| deltablue                | 7.91 ms                                                | 3.57 ms: 2.22x faster                                                 |
| go                       | 240 ms                                                 | 113 ms: 2.12x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 497 ms: 2.04x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                                 |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                  |
| richards_super           | 94.7 ms                                                | 49.7 ms: 1.91x faster                                                 |
| chaos                    | 115 ms                                                 | 61.8 ms: 1.87x faster                                                 |
| raytrace                 | 507 ms                                                 | 272 ms: 1.86x faster                                                  |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                  |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                  |
| richards                 | 79.3 ms                                                | 43.4 ms: 1.83x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.76x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 69.0 ms: 1.71x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 75.7 ms: 1.69x faster                                                 |
| djangocms                | 38.4 us                                                | 22.8 us: 1.69x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.18 ms: 1.68x faster                                                 |
| pyflate                  | 716 ms                                                 | 438 ms: 1.63x faster                                                  |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                                  |
| float                    | 117 ms                                                 | 73.4 ms: 1.60x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 2.01 sec: 1.57x faster                                                |
| nbody                    | 154 ms                                                 | 99.4 ms: 1.54x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                  |
| django_template          | 48.2 ms                                                | 32.4 ms: 1.49x faster                                                 |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.47x faster                                                  |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| genshi_text              | 31.8 ms                                                | 22.0 ms: 1.45x faster                                                 |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                 |
| html5lib                 | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 59.3 ms: 1.42x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.39x faster                                                |
| coroutines               | 35.1 ms                                                | 25.5 ms: 1.38x faster                                                 |
| thrift                   | 1.07 ms                                                | 781 us: 1.37x faster                                                  |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.35x faster                                                 |
| logging_simple           | 8.30 us                                                | 6.24 us: 1.33x faster                                                 |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                  |
| logging_format           | 9.09 us                                                | 6.91 us: 1.31x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 50.3 ms: 1.31x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 60.5 ms: 1.31x faster                                                 |
| nqueens                  | 106 ms                                                 | 81.7 ms: 1.29x faster                                                 |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                |
| fannkuch                 | 532 ms                                                 | 419 ms: 1.27x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.66 sec: 1.27x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.19 ms: 1.25x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 818 ms: 1.24x faster                                                  |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                  |
| scimark_fft              | 466 ms                                                 | 379 ms: 1.23x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 23.3 ms: 1.19x faster                                                 |
| pathlib                  | 20.5 ms                                                | 17.1 ms: 1.19x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.19x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 98.9 ms: 1.17x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 85.3 ms: 1.16x faster                                                 |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                  |
| regex_dna                | 227 ms                                                 | 203 ms: 1.12x faster                                                  |
| json_loads               | 31.2 us                                                | 28.2 us: 1.11x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.29 ms: 1.10x faster                                                 |
| async_generators         | 444 ms                                                 | 410 ms: 1.08x faster                                                  |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                 |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| coverage                 | 79.4 ms                                                | 87.8 ms: 1.11x slower                                                 |
| telco                    | 7.27 ms                                                | 8.06 ms: 1.11x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.91 ms: 1.17x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 5.09 ms: 1.40x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                                 |
| logging_silent           | 190 ns                                                 | 468 ns: 2.47x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                          |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.440x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.31x
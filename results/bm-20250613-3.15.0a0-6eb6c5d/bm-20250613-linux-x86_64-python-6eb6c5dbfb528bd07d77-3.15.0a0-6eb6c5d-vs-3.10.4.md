# Results vs. 3.10.4

- fork: python
- ref: 6eb6c5dbfb528bd07d77
- machine: linux-x86_64
- commit hash: 6eb6c5d
- commit date: 2025-06-13
- overall geometric mean: 1.327x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                  |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.44x faster                                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 597 ms: 2.96x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 310 ms: 2.81x faster                                                  |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.80x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 502 ms: 2.02x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 72.4 ms: 1.62x faster                                                 |
| nbody          | 154 ms                                                 | 97.3 ms: 1.58x faster                                                 |
| pidigits       | 191 ms                                                 | 192 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                  |
| regex_v8       | 27.8 ms                                                | 22.1 ms: 1.26x faster                                                 |
| regex_dna      | 227 ms                                                 | 184 ms: 1.23x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.10 ms: 1.17x faster                                                 |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.04 sec: 1.54x faster                                                |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.50x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.9 ms: 1.30x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.18x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.3 ms: 1.17x faster                                                 |
| json_loads           | 31.2 us                                                | 27.4 us: 1.14x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.91 ms: 1.16x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.0 ms: 1.52x faster                                                 |
| django_template | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                 |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 597 ms: 2.96x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 310 ms: 2.81x faster                                                  |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.80x faster                                                  |
| generators               | 80.1 ms                                                | 30.0 ms: 2.67x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                                |
| deltablue                | 7.91 ms                                                | 3.47 ms: 2.28x faster                                                 |
| go                       | 240 ms                                                 | 110 ms: 2.18x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 502 ms: 2.02x faster                                                  |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                  |
| richards_super           | 94.7 ms                                                | 48.6 ms: 1.95x faster                                                 |
| chaos                    | 115 ms                                                 | 60.3 ms: 1.91x faster                                                 |
| deepcopy                 | 479 us                                                 | 254 us: 1.89x faster                                                  |
| richards                 | 79.3 ms                                                | 42.4 ms: 1.87x faster                                                 |
| raytrace                 | 507 ms                                                 | 272 ms: 1.86x faster                                                  |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.0 us: 1.80x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 67.6 ms: 1.75x faster                                                 |
| hexiom                   | 10.4 ms                                                | 5.97 ms: 1.74x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 74.5 ms: 1.72x faster                                                 |
| pyflate                  | 716 ms                                                 | 427 ms: 1.68x faster                                                  |
| float                    | 117 ms                                                 | 72.4 ms: 1.62x faster                                                 |
| nbody                    | 154 ms                                                 | 97.3 ms: 1.58x faster                                                 |
| spectral_norm            | 170 ms                                                 | 109 ms: 1.56x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.04 sec: 1.54x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.0 ms: 1.52x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.50x faster                                                  |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                 |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                  |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                  |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.44x faster                                                 |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 59.7 ms: 1.41x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                                |
| coroutines               | 35.1 ms                                                | 25.0 ms: 1.41x faster                                                 |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 18.9 ms: 1.36x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                 |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                  |
| logging_simple           | 8.30 us                                                | 6.32 us: 1.31x faster                                                 |
| nqueens                  | 106 ms                                                 | 80.6 ms: 1.31x faster                                                 |
| fannkuch                 | 532 ms                                                 | 408 ms: 1.30x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.98 ms: 1.30x faster                                                 |
| logging_format           | 9.09 us                                                | 7.00 us: 1.30x faster                                                 |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.9 ms: 1.30x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.63 sec: 1.29x faster                                                |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 799 ms: 1.27x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 22.1 ms: 1.26x faster                                                 |
| sympy_expand             | 566 ms                                                 | 451 ms: 1.25x faster                                                  |
| scimark_fft              | 466 ms                                                 | 372 ms: 1.25x faster                                                  |
| regex_dna                | 227 ms                                                 | 184 ms: 1.23x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.18x faster                                                  |
| pathlib                  | 20.5 ms                                                | 17.4 ms: 1.18x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.10 ms: 1.17x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 85.3 ms: 1.17x faster                                                 |
| json_loads               | 31.2 us                                                | 27.4 us: 1.14x faster                                                 |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.13x faster                                                  |
| json                     | 5.69 ms                                                | 5.20 ms: 1.09x faster                                                 |
| async_generators         | 444 ms                                                 | 411 ms: 1.08x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.05x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                  |
| pidigits                 | 191 ms                                                 | 192 ms: 1.01x slower                                                  |
| telco                    | 7.27 ms                                                | 8.06 ms: 1.11x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.91 ms: 1.16x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.78 ms: 1.32x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                                 |
| logging_silent           | 190 ns                                                 | 468 ns: 2.47x slower                                                  |
| coverage                 | 79.4 ms                                                | 433 ms: 5.45x slower                                                  |
| thrift                   | 1.07 ms                                                | 148 ms: 138.20x slower                                                |
| Geometric mean           | (ref)                                                  | 1.31x faster                                                          |
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250613-3.15.0a0-6eb6c5d/bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.327x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.31x
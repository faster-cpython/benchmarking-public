# Results vs. 3.10.4

- fork: python
- ref: 3.14
- machine: linux-x86_64
- commit hash: c1735c5
- commit date: 2025-06-17
- overall geometric mean: 1.446x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                   |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                 |
| html5lib       | 88.9 ms                                                | 61.6 ms: 1.44x faster                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 592 ms: 2.99x faster                                   |
| async_tree_memoization  | 870 ms                                                 | 308 ms: 2.83x faster                                   |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 487 ms: 2.09x faster                                   |
| Geometric mean          | (ref)                                                  | 2.65x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 117 ms                                                 | 70.1 ms: 1.67x faster                                  |
| nbody          | 154 ms                                                 | 100 ms: 1.53x faster                                   |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                   |
| Geometric mean | (ref)                                                  | 1.38x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                   |
| regex_v8       | 27.8 ms                                                | 23.3 ms: 1.19x faster                                  |
| regex_effbot   | 3.63 ms                                                | 3.21 ms: 1.13x faster                                  |
| regex_dna      | 227 ms                                                 | 207 ms: 1.10x faster                                   |
| Geometric mean | (ref)                                                  | 1.22x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.01 sec: 1.56x faster                                 |
| pickle_pure_python   | 484 us                                                 | 316 us: 1.53x faster                                   |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                   |
| xml_etree_process    | 79.1 ms                                                | 60.2 ms: 1.31x faster                                  |
| json_dumps           | 14.2 ms                                                | 10.9 ms: 1.30x faster                                  |
| xml_etree_iterparse  | 115 ms                                                 | 99.0 ms: 1.17x faster                                  |
| xml_etree_parse      | 168 ms                                                 | 144 ms: 1.17x faster                                   |
| xml_etree_generate   | 99.4 ms                                                | 85.4 ms: 1.16x faster                                  |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                  |
| Geometric mean       | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                  |
| python_startup_no_site | 5.93 ms                                                | 6.92 ms: 1.17x slower                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                  |
| genshi_text     | 31.8 ms                                                | 21.7 ms: 1.47x faster                                  |
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                  |
| genshi_xml      | 66.0 ms                                                | 49.1 ms: 1.35x faster                                  |
| Geometric mean  | (ref)                                                  | 1.43x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.25x faster                                   |
| async_tree_io            | 1.77 sec                                               | 592 ms: 2.99x faster                                   |
| async_tree_memoization   | 870 ms                                                 | 308 ms: 2.83x faster                                   |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                   |
| generators               | 80.1 ms                                                | 31.4 ms: 2.55x faster                                  |
| deltablue                | 7.91 ms                                                | 3.35 ms: 2.36x faster                                  |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.31x faster                                 |
| go                       | 240 ms                                                 | 112 ms: 2.14x faster                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 487 ms: 2.09x faster                                   |
| pylint                   | 551 ms                                                 | 278 ms: 1.99x faster                                   |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.99x faster                                  |
| richards_super           | 94.7 ms                                                | 48.8 ms: 1.94x faster                                  |
| chaos                    | 115 ms                                                 | 60.1 ms: 1.92x faster                                  |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                   |
| richards                 | 79.3 ms                                                | 42.6 ms: 1.86x faster                                  |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                   |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                   |
| scimark_monte_carlo      | 118 ms                                                 | 67.7 ms: 1.75x faster                                  |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                  |
| crypto_pyaes             | 128 ms                                                 | 74.4 ms: 1.72x faster                                  |
| hexiom                   | 10.4 ms                                                | 6.12 ms: 1.70x faster                                  |
| pyflate                  | 716 ms                                                 | 426 ms: 1.68x faster                                   |
| float                    | 117 ms                                                 | 70.1 ms: 1.67x faster                                  |
| tomli_loads              | 3.14 sec                                               | 2.01 sec: 1.56x faster                                 |
| spectral_norm            | 170 ms                                                 | 110 ms: 1.54x faster                                   |
| nbody                    | 154 ms                                                 | 100 ms: 1.53x faster                                   |
| pickle_pure_python       | 484 us                                                 | 316 us: 1.53x faster                                   |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                   |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                   |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.78 us: 1.50x faster                                  |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                   |
| genshi_text              | 31.8 ms                                                | 21.7 ms: 1.47x faster                                  |
| html5lib                 | 88.9 ms                                                | 61.6 ms: 1.44x faster                                  |
| dulwich_log              | 84.3 ms                                                | 59.5 ms: 1.42x faster                                  |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                  |
| coroutines               | 35.1 ms                                                | 24.8 ms: 1.42x faster                                  |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.39x faster                                 |
| pprint_safe_repr         | 1.02 sec                                               | 743 ms: 1.37x faster                                   |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                 |
| sympy_integrate          | 25.8 ms                                                | 18.9 ms: 1.36x faster                                  |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                   |
| logging_simple           | 8.30 us                                                | 6.13 us: 1.35x faster                                  |
| genshi_xml               | 66.0 ms                                                | 49.1 ms: 1.35x faster                                  |
| logging_format           | 9.09 us                                                | 6.77 us: 1.34x faster                                  |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.6 ms: 1.33x faster                                  |
| xml_etree_process        | 79.1 ms                                                | 60.2 ms: 1.31x faster                                  |
| nqueens                  | 106 ms                                                 | 81.0 ms: 1.31x faster                                  |
| json_dumps               | 14.2 ms                                                | 10.9 ms: 1.30x faster                                  |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.02 ms: 1.29x faster                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 134 ms: 1.29x faster                                   |
| fannkuch                 | 532 ms                                                 | 416 ms: 1.28x faster                                   |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                 |
| scimark_fft              | 466 ms                                                 | 373 ms: 1.25x faster                                   |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                   |
| regex_v8                 | 27.8 ms                                                | 23.3 ms: 1.19x faster                                  |
| pathlib                  | 20.5 ms                                                | 17.3 ms: 1.18x faster                                  |
| xml_etree_iterparse      | 115 ms                                                 | 99.0 ms: 1.17x faster                                  |
| xml_etree_parse          | 168 ms                                                 | 144 ms: 1.17x faster                                   |
| xml_etree_generate       | 99.4 ms                                                | 85.4 ms: 1.16x faster                                  |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                   |
| regex_effbot             | 3.63 ms                                                | 3.21 ms: 1.13x faster                                  |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                  |
| regex_dna                | 227 ms                                                 | 207 ms: 1.10x faster                                   |
| json                     | 5.69 ms                                                | 5.20 ms: 1.09x faster                                  |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                  |
| async_generators         | 444 ms                                                 | 408 ms: 1.09x faster                                   |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.05x faster                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                   |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                   |
| coverage                 | 79.4 ms                                                | 87.1 ms: 1.10x slower                                  |
| telco                    | 7.27 ms                                                | 8.02 ms: 1.10x slower                                  |
| python_startup_no_site   | 5.93 ms                                                | 6.92 ms: 1.17x slower                                  |
| gc_traversal             | 3.62 ms                                                | 4.74 ms: 1.31x slower                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.58 ms: 1.59x slower                                  |
| logging_silent           | 190 ns                                                 | 471 ns: 2.48x slower                                   |
| Geometric mean           | (ref)                                                  | 1.42x faster                                           |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250617-3.14.0b2+-c1735c5/bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.446x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.31x
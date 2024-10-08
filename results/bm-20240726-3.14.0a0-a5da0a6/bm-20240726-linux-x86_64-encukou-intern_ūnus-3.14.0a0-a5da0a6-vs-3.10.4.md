# Results vs. 3.10.4

- fork: encukou
- ref: intern_ūnus
- machine: linux-x86_64
- commit hash: a5da0a6
- commit date: 2024-07-26
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                          |
| docutils       | 3.30 sec                                               | 2.73 sec: 1.21x faster                                        |
| html5lib       | 88.9 ms                                                | 65.9 ms: 1.35x faster                                         |
| tornado_http   | 136 ms                                                 | 89.9 ms: 1.52x faster                                         |
| Geometric mean | (ref)                                                  | 1.35x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 324 ms: 2.25x faster                                          |
| async_tree_memoization  | 870 ms                                                 | 413 ms: 2.11x faster                                          |
| async_tree_io           | 1.77 sec                                               | 902 ms: 1.96x faster                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.79x faster                                          |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 84.6 ms: 1.81x faster                                         |
| float          | 117 ms                                                 | 77.4 ms: 1.51x faster                                         |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                  | 1.41x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.43x faster                                          |
| regex_v8       | 27.8 ms                                                | 25.3 ms: 1.10x faster                                         |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                          |
| regex_effbot   | 3.63 ms                                                | 3.78 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 299 us: 1.62x faster                                          |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                          |
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.50x faster                                        |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                         |
| xml_etree_process    | 79.1 ms                                                | 58.5 ms: 1.35x faster                                         |
| xml_etree_generate   | 99.4 ms                                                | 84.7 ms: 1.17x faster                                         |
| json_loads           | 31.2 us                                                | 27.7 us: 1.12x faster                                         |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                          |
| xml_etree_parse      | 168 ms                                                 | 157 ms: 1.07x faster                                          |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                         |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                         |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                         |
| genshi_text     | 31.8 ms                                                | 22.3 ms: 1.43x faster                                         |
| django_template | 48.2 ms                                                | 33.8 ms: 1.43x faster                                         |
| genshi_xml      | 66.0 ms                                                | 50.0 ms: 1.32x faster                                         |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.25x faster                                          |
| generators               | 80.1 ms                                                | 28.0 ms: 2.86x faster                                         |
| deltablue                | 7.91 ms                                                | 3.12 ms: 2.53x faster                                         |
| async_tree_none          | 728 ms                                                 | 324 ms: 2.25x faster                                          |
| async_tree_memoization   | 870 ms                                                 | 413 ms: 2.11x faster                                          |
| raytrace                 | 507 ms                                                 | 255 ms: 1.98x faster                                          |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                         |
| async_tree_io            | 1.77 sec                                               | 902 ms: 1.96x faster                                          |
| chaos                    | 115 ms                                                 | 58.9 ms: 1.96x faster                                         |
| logging_silent           | 190 ns                                                 | 97.5 ns: 1.95x faster                                         |
| asyncio_tcp              | 922 ms                                                 | 481 ms: 1.91x faster                                          |
| richards_super           | 94.7 ms                                                | 51.2 ms: 1.85x faster                                         |
| deepcopy                 | 479 us                                                 | 261 us: 1.83x faster                                          |
| nbody                    | 154 ms                                                 | 84.6 ms: 1.81x faster                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.79x faster                                          |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                         |
| richards                 | 79.3 ms                                                | 45.3 ms: 1.75x faster                                         |
| pylint                   | 551 ms                                                 | 317 ms: 1.74x faster                                          |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.73x faster                                          |
| go                       | 240 ms                                                 | 140 ms: 1.72x faster                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                         |
| crypto_pyaes             | 128 ms                                                 | 75.1 ms: 1.70x faster                                         |
| hexiom                   | 10.4 ms                                                | 6.14 ms: 1.69x faster                                         |
| scimark_monte_carlo      | 118 ms                                                 | 71.4 ms: 1.66x faster                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                         |
| pickle_pure_python       | 484 us                                                 | 299 us: 1.62x faster                                          |
| deepcopy_reduce          | 4.17 us                                                | 2.63 us: 1.59x faster                                         |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.57x faster                                          |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                          |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                         |
| pyflate                  | 716 ms                                                 | 469 ms: 1.53x faster                                          |
| tornado_http             | 136 ms                                                 | 89.9 ms: 1.52x faster                                         |
| logging_simple           | 8.30 us                                                | 5.49 us: 1.51x faster                                         |
| float                    | 117 ms                                                 | 77.4 ms: 1.51x faster                                         |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.51x faster                                          |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.50x faster                                        |
| logging_format           | 9.09 us                                                | 6.08 us: 1.49x faster                                         |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.51 ms: 1.44x faster                                         |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                         |
| regex_compile            | 188 ms                                                 | 132 ms: 1.43x faster                                          |
| genshi_text              | 31.8 ms                                                | 22.3 ms: 1.43x faster                                         |
| django_template          | 48.2 ms                                                | 33.8 ms: 1.43x faster                                         |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                         |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.37x faster                                        |
| thrift                   | 1.07 ms                                                | 783 us: 1.37x faster                                          |
| pprint_safe_repr         | 1.02 sec                                               | 745 ms: 1.37x faster                                          |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                         |
| xml_etree_process        | 79.1 ms                                                | 58.5 ms: 1.35x faster                                         |
| html5lib                 | 88.9 ms                                                | 65.9 ms: 1.35x faster                                         |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.34x faster                                          |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                        |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                          |
| genshi_xml               | 66.0 ms                                                | 50.0 ms: 1.32x faster                                         |
| scimark_fft              | 466 ms                                                 | 355 ms: 1.31x faster                                          |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                         |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                          |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                          |
| sqlglot_optimize         | 69.2 ms                                                | 53.2 ms: 1.30x faster                                         |
| nqueens                  | 106 ms                                                 | 82.2 ms: 1.29x faster                                         |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                         |
| sympy_str                | 346 ms                                                 | 271 ms: 1.28x faster                                          |
| bench_thread_pool        | 986 us                                                 | 786 us: 1.25x faster                                          |
| dask                     | 441 ms                                                 | 353 ms: 1.25x faster                                          |
| sympy_expand             | 566 ms                                                 | 459 ms: 1.23x faster                                          |
| docutils                 | 3.30 sec                                               | 2.73 sec: 1.21x faster                                        |
| xml_etree_generate       | 99.4 ms                                                | 84.7 ms: 1.17x faster                                         |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                        |
| json_loads               | 31.2 us                                                | 27.7 us: 1.12x faster                                         |
| json                     | 5.69 ms                                                | 5.09 ms: 1.12x faster                                         |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                          |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                          |
| regex_v8                 | 27.8 ms                                                | 25.3 ms: 1.10x faster                                         |
| xml_etree_parse          | 168 ms                                                 | 157 ms: 1.07x faster                                          |
| gc_traversal             | 3.62 ms                                                | 3.49 ms: 1.04x faster                                         |
| async_generators         | 444 ms                                                 | 431 ms: 1.03x faster                                          |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                          |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                          |
| regex_effbot             | 3.63 ms                                                | 3.78 ms: 1.04x slower                                         |
| create_gc_cycles         | 1.62 ms                                                | 1.72 ms: 1.06x slower                                         |
| telco                    | 7.27 ms                                                | 8.15 ms: 1.12x slower                                         |
| coverage                 | 79.4 ms                                                | 89.3 ms: 1.12x slower                                         |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                         |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                  |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240726-3.14.0a0-a5da0a6/bm-20240726-linux-x86_64-encukou-intern_ūnus-3.14.0a0-a5da0a6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.12x
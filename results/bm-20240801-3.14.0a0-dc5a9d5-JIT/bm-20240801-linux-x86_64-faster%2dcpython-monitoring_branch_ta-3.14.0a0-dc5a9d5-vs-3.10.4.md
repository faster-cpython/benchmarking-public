# Results vs. 3.10.4

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: linux-x86_64
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 273 ms: 1.27x faster                                                            |
| docutils       | 3.30 sec                                               | 2.90 sec: 1.13x faster                                                          |
| html5lib       | 88.9 ms                                                | 64.2 ms: 1.38x faster                                                           |
| tornado_http   | 136 ms                                                 | 92.1 ms: 1.48x faster                                                           |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 410 ms: 2.12x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 903 ms: 1.96x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 563 ms: 1.80x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.4 ms: 1.93x faster                                                           |
| float          | 117 ms                                                 | 70.4 ms: 1.66x faster                                                           |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.49x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.41x faster                                                            |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                           |
| regex_dna      | 227 ms                                                 | 227 ms: 1.00x slower                                                            |
| regex_effbot   | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 295 us: 1.64x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 55.3 ms: 1.43x faster                                                           |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 79.2 ms: 1.25x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 99.2 ms: 1.16x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                            |
| json_loads           | 31.2 us                                                | 27.8 us: 1.12x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.92 ms: 1.65x faster                                                           |
| django_template | 48.2 ms                                                | 35.9 ms: 1.34x faster                                                           |
| genshi_text     | 31.8 ms                                                | 24.2 ms: 1.31x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 53.9 ms: 1.22x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                            |
| generators               | 80.1 ms                                                | 33.3 ms: 2.41x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.52 ms: 2.25x faster                                                           |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 410 ms: 2.12x faster                                                            |
| richards_super           | 94.7 ms                                                | 46.5 ms: 2.04x faster                                                           |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                                           |
| chaos                    | 115 ms                                                 | 57.6 ms: 2.00x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 59.9 ms: 1.97x faster                                                           |
| richards                 | 79.3 ms                                                | 40.4 ms: 1.96x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 903 ms: 1.96x faster                                                            |
| nbody                    | 154 ms                                                 | 79.4 ms: 1.93x faster                                                           |
| raytrace                 | 507 ms                                                 | 266 ms: 1.91x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 67.9 ms: 1.88x faster                                                           |
| asyncio_tcp              | 922 ms                                                 | 499 ms: 1.85x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 563 ms: 1.80x faster                                                            |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.1 us: 1.78x faster                                                           |
| deepcopy                 | 479 us                                                 | 273 us: 1.76x faster                                                            |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.73x faster                                                            |
| go                       | 240 ms                                                 | 142 ms: 1.69x faster                                                            |
| pyflate                  | 716 ms                                                 | 427 ms: 1.68x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                           |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                            |
| float                    | 117 ms                                                 | 70.4 ms: 1.66x faster                                                           |
| mako                     | 16.3 ms                                                | 9.92 ms: 1.65x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 295 us: 1.64x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                          |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.59x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.67 ms: 1.56x faster                                                           |
| pylint                   | 551 ms                                                 | 355 ms: 1.55x faster                                                            |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.47 us: 1.52x faster                                                           |
| logging_format           | 9.09 us                                                | 6.00 us: 1.52x faster                                                           |
| scimark_fft              | 466 ms                                                 | 308 ms: 1.51x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.77 us: 1.51x faster                                                           |
| tornado_http             | 136 ms                                                 | 92.1 ms: 1.48x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.39 ms: 1.47x faster                                                           |
| fannkuch                 | 532 ms                                                 | 364 ms: 1.46x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 55.3 ms: 1.43x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                          |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                                            |
| regex_compile            | 188 ms                                                 | 134 ms: 1.41x faster                                                            |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                          |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 733 ms: 1.39x faster                                                            |
| html5lib                 | 88.9 ms                                                | 64.2 ms: 1.38x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                           |
| thrift                   | 1.07 ms                                                | 796 us: 1.35x faster                                                            |
| django_template          | 48.2 ms                                                | 35.9 ms: 1.34x faster                                                           |
| genshi_text              | 31.8 ms                                                | 24.2 ms: 1.31x faster                                                           |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                           |
| 2to3                     | 348 ms                                                 | 273 ms: 1.27x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 79.2 ms: 1.25x faster                                                           |
| nqueens                  | 106 ms                                                 | 85.2 ms: 1.24x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 55.9 ms: 1.24x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 53.9 ms: 1.22x faster                                                           |
| dask                     | 441 ms                                                 | 365 ms: 1.21x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 821 us: 1.20x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 99.2 ms: 1.16x faster                                                           |
| sympy_str                | 346 ms                                                 | 298 ms: 1.16x faster                                                            |
| sympy_sum                | 196 ms                                                 | 170 ms: 1.16x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 22.6 ms: 1.14x faster                                                           |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.90 sec: 1.13x faster                                                          |
| sympy_expand             | 566 ms                                                 | 503 ms: 1.12x faster                                                            |
| json_loads               | 31.2 us                                                | 27.8 us: 1.12x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                                          |
| json                     | 5.69 ms                                                | 5.22 ms: 1.09x faster                                                           |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                            |
| regex_dna                | 227 ms                                                 | 227 ms: 1.00x slower                                                            |
| regex_effbot             | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                           |
| async_generators         | 444 ms                                                 | 456 ms: 1.03x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 3.81 ms: 1.05x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                                           |
| telco                    | 7.27 ms                                                | 8.07 ms: 1.11x slower                                                           |
| coverage                 | 79.4 ms                                                | 91.7 ms: 1.15x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240801-3.14.0a0-dc5a9d5-JIT/bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.20x
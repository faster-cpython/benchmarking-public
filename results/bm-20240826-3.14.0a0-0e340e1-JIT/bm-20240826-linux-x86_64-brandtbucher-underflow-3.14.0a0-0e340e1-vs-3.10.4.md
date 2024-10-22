# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 0e340e1
- commit date: 2024-08-26
- overall geometric mean: 1.40x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 283 ms: 1.23x faster                                             |
| docutils       | 3.30 sec                                               | 3.34 sec: 1.01x slower                                           |
| html5lib       | 88.9 ms                                                | 70.6 ms: 1.26x faster                                            |
| tornado_http   | 136 ms                                                 | 102 ms: 1.33x faster                                             |
| Geometric mean | (ref)                                                  | 1.19x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                             |
| async_tree_memoization  | 870 ms                                                 | 414 ms: 2.10x faster                                             |
| async_tree_io           | 1.77 sec                                               | 941 ms: 1.88x faster                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 560 ms: 1.81x faster                                             |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.6 ms: 1.93x faster                                            |
| float          | 117 ms                                                 | 71.0 ms: 1.65x faster                                            |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.48x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 150 ms: 1.25x faster                                             |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                            |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                             |
| Geometric mean | (ref)                                                  | 1.11x faster                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 198 us: 1.67x faster                                             |
| pickle_pure_python   | 484 us                                                 | 310 us: 1.56x faster                                             |
| tomli_loads          | 3.14 sec                                               | 2.05 sec: 1.53x faster                                           |
| xml_etree_process    | 79.1 ms                                                | 54.5 ms: 1.45x faster                                            |
| json_dumps           | 14.2 ms                                                | 9.99 ms: 1.42x faster                                            |
| xml_etree_generate   | 99.4 ms                                                | 77.0 ms: 1.29x faster                                            |
| xml_etree_iterparse  | 115 ms                                                 | 98.8 ms: 1.17x faster                                            |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                             |
| json_loads           | 31.2 us                                                | 29.6 us: 1.05x faster                                            |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                            |
| python_startup_no_site | 5.93 ms                                                | 7.16 ms: 1.21x slower                                            |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.61 ms: 1.70x faster                                            |
| genshi_text     | 31.8 ms                                                | 24.3 ms: 1.31x faster                                            |
| django_template | 48.2 ms                                                | 38.3 ms: 1.26x faster                                            |
| genshi_xml      | 66.0 ms                                                | 65.0 ms: 1.02x faster                                            |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                             |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                            |
| generators               | 80.1 ms                                                | 33.7 ms: 2.38x faster                                            |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                             |
| richards_super           | 94.7 ms                                                | 43.1 ms: 2.20x faster                                            |
| deepcopy_memo            | 58.5 us                                                | 26.6 us: 2.19x faster                                            |
| async_tree_memoization   | 870 ms                                                 | 414 ms: 2.10x faster                                             |
| richards                 | 79.3 ms                                                | 38.1 ms: 2.08x faster                                            |
| scimark_monte_carlo      | 118 ms                                                 | 59.1 ms: 2.00x faster                                            |
| chaos                    | 115 ms                                                 | 58.2 ms: 1.98x faster                                            |
| crypto_pyaes             | 128 ms                                                 | 65.9 ms: 1.94x faster                                            |
| nbody                    | 154 ms                                                 | 79.6 ms: 1.93x faster                                            |
| async_tree_io            | 1.77 sec                                               | 941 ms: 1.88x faster                                             |
| logging_silent           | 190 ns                                                 | 101 ns: 1.87x faster                                             |
| raytrace                 | 507 ms                                                 | 276 ms: 1.83x faster                                             |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 560 ms: 1.81x faster                                             |
| asyncio_tcp              | 922 ms                                                 | 514 ms: 1.79x faster                                             |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.78x faster                                             |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.73x faster                                            |
| mako                     | 16.3 ms                                                | 9.61 ms: 1.70x faster                                            |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                             |
| unpickle_pure_python     | 331 us                                                 | 198 us: 1.67x faster                                             |
| float                    | 117 ms                                                 | 71.0 ms: 1.65x faster                                            |
| pyflate                  | 716 ms                                                 | 440 ms: 1.63x faster                                             |
| pickle_pure_python       | 484 us                                                 | 310 us: 1.56x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                            |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                            |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                             |
| tomli_loads              | 3.14 sec                                               | 2.05 sec: 1.53x faster                                           |
| hexiom                   | 10.4 ms                                                | 6.82 ms: 1.52x faster                                            |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.44 ms: 1.46x faster                                            |
| xml_etree_process        | 79.1 ms                                                | 54.5 ms: 1.45x faster                                            |
| fannkuch                 | 532 ms                                                 | 367 ms: 1.45x faster                                             |
| sqlglot_parse            | 2.17 ms                                                | 1.51 ms: 1.43x faster                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.80 ms: 1.43x faster                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                           |
| logging_simple           | 8.30 us                                                | 5.84 us: 1.42x faster                                            |
| json_dumps               | 14.2 ms                                                | 9.99 ms: 1.42x faster                                            |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                           |
| go                       | 240 ms                                                 | 170 ms: 1.41x faster                                             |
| pprint_safe_repr         | 1.02 sec                                               | 723 ms: 1.41x faster                                             |
| logging_format           | 9.09 us                                                | 6.51 us: 1.40x faster                                            |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                            |
| thrift                   | 1.07 ms                                                | 789 us: 1.36x faster                                             |
| tornado_http             | 136 ms                                                 | 102 ms: 1.33x faster                                             |
| pylint                   | 551 ms                                                 | 415 ms: 1.33x faster                                             |
| genshi_text              | 31.8 ms                                                | 24.3 ms: 1.31x faster                                            |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.30x faster                                            |
| xml_etree_generate       | 99.4 ms                                                | 77.0 ms: 1.29x faster                                            |
| pycparser                | 1.58 sec                                               | 1.23 sec: 1.28x faster                                           |
| nqueens                  | 106 ms                                                 | 83.7 ms: 1.26x faster                                            |
| html5lib                 | 88.9 ms                                                | 70.6 ms: 1.26x faster                                            |
| django_template          | 48.2 ms                                                | 38.3 ms: 1.26x faster                                            |
| regex_compile            | 188 ms                                                 | 150 ms: 1.25x faster                                             |
| 2to3                     | 348 ms                                                 | 283 ms: 1.23x faster                                             |
| bench_thread_pool        | 986 us                                                 | 825 us: 1.19x faster                                             |
| sqlglot_normalize        | 143 ms                                                 | 121 ms: 1.18x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 98.8 ms: 1.17x faster                                            |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                             |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                            |
| sqlglot_optimize         | 69.2 ms                                                | 60.4 ms: 1.14x faster                                            |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                             |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                           |
| json                     | 5.69 ms                                                | 5.26 ms: 1.08x faster                                            |
| sympy_str                | 346 ms                                                 | 321 ms: 1.08x faster                                             |
| sympy_expand             | 566 ms                                                 | 536 ms: 1.06x faster                                             |
| json_loads               | 31.2 us                                                | 29.6 us: 1.05x faster                                            |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 25.0 ms: 1.03x faster                                            |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                             |
| sympy_sum                | 196 ms                                                 | 192 ms: 1.02x faster                                             |
| genshi_xml               | 66.0 ms                                                | 65.0 ms: 1.02x faster                                            |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                             |
| docutils                 | 3.30 sec                                               | 3.34 sec: 1.01x slower                                           |
| async_generators         | 444 ms                                                 | 456 ms: 1.03x slower                                             |
| gc_traversal             | 3.62 ms                                                | 3.78 ms: 1.04x slower                                            |
| telco                    | 7.27 ms                                                | 7.66 ms: 1.05x slower                                            |
| coverage                 | 79.4 ms                                                | 86.9 ms: 1.09x slower                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.16 ms: 1.21x slower                                            |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                     |

Benchmark hidden because not significant (2): regex_effbot, bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240826-3.14.0a0-0e340e1-JIT/bm-20240826-linux-x86_64-brandtbucher-underflow-3.14.0a0-0e340e1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.23x
# Results vs. 3.10.4

- fork: brandtbucher
- ref: optimize
- machine: linux-x86_64
- commit hash: 700ea07
- commit date: 2024-07-11
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 270 ms: 1.29x faster                                            |
| docutils       | 3.30 sec                                               | 2.96 sec: 1.11x faster                                          |
| html5lib       | 88.9 ms                                                | 67.9 ms: 1.31x faster                                           |
| tornado_http   | 136 ms                                                 | 91.9 ms: 1.48x faster                                           |
| Geometric mean | (ref)                                                  | 1.29x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 329 ms: 2.21x faster                                            |
| async_tree_memoization  | 870 ms                                                 | 411 ms: 2.12x faster                                            |
| async_tree_io           | 1.77 sec                                               | 909 ms: 1.95x faster                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 567 ms: 1.79x faster                                            |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 92.2 ms: 1.67x faster                                           |
| float          | 117 ms                                                 | 78.7 ms: 1.49x faster                                           |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                            |
| Geometric mean | (ref)                                                  | 1.36x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.40x faster                                            |
| regex_v8       | 27.8 ms                                                | 24.1 ms: 1.15x faster                                           |
| regex_dna      | 227 ms                                                 | 228 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                  | 1.12x faster                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 304 us: 1.59x faster                                            |
| unpickle_pure_python | 331 us                                                 | 220 us: 1.50x faster                                            |
| tomli_loads          | 3.14 sec                                               | 2.24 sec: 1.40x faster                                          |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                           |
| xml_etree_process    | 79.1 ms                                                | 60.6 ms: 1.31x faster                                           |
| xml_etree_generate   | 99.4 ms                                                | 86.9 ms: 1.14x faster                                           |
| json_loads           | 31.2 us                                                | 27.6 us: 1.13x faster                                           |
| xml_etree_iterparse  | 115 ms                                                 | 108 ms: 1.07x faster                                            |
| xml_etree_parse      | 168 ms                                                 | 159 ms: 1.06x faster                                            |
| Geometric mean       | (ref)                                                  | 1.27x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                           |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                           |
| django_template | 48.2 ms                                                | 34.5 ms: 1.40x faster                                           |
| genshi_text     | 31.8 ms                                                | 25.7 ms: 1.24x faster                                           |
| genshi_xml      | 66.0 ms                                                | 57.1 ms: 1.16x faster                                           |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.30x faster                                            |
| deltablue                | 7.91 ms                                                | 3.28 ms: 2.41x faster                                           |
| async_tree_none          | 728 ms                                                 | 329 ms: 2.21x faster                                            |
| async_tree_memoization   | 870 ms                                                 | 411 ms: 2.12x faster                                            |
| async_tree_io            | 1.77 sec                                               | 909 ms: 1.95x faster                                            |
| chaos                    | 115 ms                                                 | 60.2 ms: 1.92x faster                                           |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                            |
| asyncio_tcp              | 922 ms                                                 | 490 ms: 1.88x faster                                            |
| deepcopy_memo            | 58.5 us                                                | 31.1 us: 1.88x faster                                           |
| logging_silent           | 190 ns                                                 | 106 ns: 1.80x faster                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 567 ms: 1.79x faster                                            |
| deepcopy                 | 479 us                                                 | 269 us: 1.78x faster                                            |
| richards_super           | 94.7 ms                                                | 53.5 ms: 1.77x faster                                           |
| scimark_sor              | 220 ms                                                 | 125 ms: 1.76x faster                                            |
| crypto_pyaes             | 128 ms                                                 | 72.9 ms: 1.75x faster                                           |
| generators               | 80.1 ms                                                | 45.8 ms: 1.75x faster                                           |
| scimark_monte_carlo      | 118 ms                                                 | 69.4 ms: 1.70x faster                                           |
| richards                 | 79.3 ms                                                | 47.0 ms: 1.68x faster                                           |
| nbody                    | 154 ms                                                 | 92.2 ms: 1.67x faster                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.66x faster                                           |
| go                       | 240 ms                                                 | 145 ms: 1.66x faster                                            |
| comprehensions           | 28.8 us                                                | 18.0 us: 1.59x faster                                           |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.59x faster                                            |
| pylint                   | 551 ms                                                 | 347 ms: 1.59x faster                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                           |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                            |
| logging_simple           | 8.30 us                                                | 5.46 us: 1.52x faster                                           |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.50x faster                                            |
| logging_format           | 9.09 us                                                | 6.06 us: 1.50x faster                                           |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.50x faster                                            |
| float                    | 117 ms                                                 | 78.7 ms: 1.49x faster                                           |
| tornado_http             | 136 ms                                                 | 91.9 ms: 1.48x faster                                           |
| hexiom                   | 10.4 ms                                                | 7.05 ms: 1.48x faster                                           |
| pyflate                  | 716 ms                                                 | 485 ms: 1.48x faster                                            |
| coroutines               | 35.1 ms                                                | 24.0 ms: 1.46x faster                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                          |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                           |
| tomli_loads              | 3.14 sec                                               | 2.24 sec: 1.40x faster                                          |
| regex_compile            | 188 ms                                                 | 135 ms: 1.40x faster                                            |
| django_template          | 48.2 ms                                                | 34.5 ms: 1.40x faster                                           |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                           |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                          |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                           |
| pprint_safe_repr         | 1.02 sec                                               | 747 ms: 1.36x faster                                            |
| thrift                   | 1.07 ms                                                | 791 us: 1.35x faster                                            |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                          |
| html5lib                 | 88.9 ms                                                | 67.9 ms: 1.31x faster                                           |
| xml_etree_process        | 79.1 ms                                                | 60.6 ms: 1.31x faster                                           |
| dulwich_log              | 84.3 ms                                                | 64.9 ms: 1.30x faster                                           |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                            |
| 2to3                     | 348 ms                                                 | 270 ms: 1.29x faster                                            |
| fannkuch                 | 532 ms                                                 | 414 ms: 1.28x faster                                            |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                           |
| scimark_fft              | 466 ms                                                 | 369 ms: 1.26x faster                                            |
| sympy_sum                | 196 ms                                                 | 157 ms: 1.25x faster                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.20 ms: 1.24x faster                                           |
| sympy_integrate          | 25.8 ms                                                | 20.8 ms: 1.24x faster                                           |
| genshi_text              | 31.8 ms                                                | 25.7 ms: 1.24x faster                                           |
| sympy_str                | 346 ms                                                 | 280 ms: 1.24x faster                                            |
| dask                     | 441 ms                                                 | 361 ms: 1.22x faster                                            |
| sympy_expand             | 566 ms                                                 | 466 ms: 1.21x faster                                            |
| bench_thread_pool        | 986 us                                                 | 821 us: 1.20x faster                                            |
| sqlglot_optimize         | 69.2 ms                                                | 58.0 ms: 1.19x faster                                           |
| nqueens                  | 106 ms                                                 | 90.6 ms: 1.17x faster                                           |
| genshi_xml               | 66.0 ms                                                | 57.1 ms: 1.16x faster                                           |
| regex_v8                 | 27.8 ms                                                | 24.1 ms: 1.15x faster                                           |
| xml_etree_generate       | 99.4 ms                                                | 86.9 ms: 1.14x faster                                           |
| json_loads               | 31.2 us                                                | 27.6 us: 1.13x faster                                           |
| docutils                 | 3.30 sec                                               | 2.96 sec: 1.11x faster                                          |
| json                     | 5.69 ms                                                | 5.21 ms: 1.09x faster                                           |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.08x faster                                            |
| xml_etree_iterparse      | 115 ms                                                 | 108 ms: 1.07x faster                                            |
| xml_etree_parse          | 168 ms                                                 | 159 ms: 1.06x faster                                            |
| mdp                      | 2.85 sec                                               | 2.77 sec: 1.03x faster                                          |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                            |
| regex_dna                | 227 ms                                                 | 228 ms: 1.01x slower                                            |
| gc_traversal             | 3.62 ms                                                | 3.73 ms: 1.03x slower                                           |
| async_generators         | 444 ms                                                 | 461 ms: 1.04x slower                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                           |
| telco                    | 7.27 ms                                                | 8.30 ms: 1.14x slower                                           |
| coverage                 | 79.4 ms                                                | 92.7 ms: 1.17x slower                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                           |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                    |

Benchmark hidden because not significant (3): asyncio_websockets, bench_mp_pool, regex_effbot
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240711-3.14.0a0-700ea07-JIT/bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.14x
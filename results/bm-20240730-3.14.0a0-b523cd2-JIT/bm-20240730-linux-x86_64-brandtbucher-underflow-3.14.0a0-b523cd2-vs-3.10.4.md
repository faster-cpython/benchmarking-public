# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: b523cd2
- commit date: 2024-07-30
- overall geometric mean: 1.41x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 278 ms: 1.25x faster                                             |
| docutils       | 3.30 sec                                               | 3.09 sec: 1.07x faster                                           |
| html5lib       | 88.9 ms                                                | 69.7 ms: 1.27x faster                                            |
| tornado_http   | 136 ms                                                 | 103 ms: 1.32x faster                                             |
| Geometric mean | (ref)                                                  | 1.22x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 331 ms: 2.20x faster                                             |
| async_tree_memoization  | 870 ms                                                 | 431 ms: 2.02x faster                                             |
| async_tree_io           | 1.77 sec                                               | 915 ms: 1.93x faster                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 565 ms: 1.80x faster                                             |
| Geometric mean          | (ref)                                                  | 1.98x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.3 ms: 1.89x faster                                            |
| float          | 117 ms                                                 | 71.5 ms: 1.64x faster                                            |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.47x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 140 ms: 1.34x faster                                             |
| regex_v8       | 27.8 ms                                                | 25.9 ms: 1.07x faster                                            |
| regex_dna      | 227 ms                                                 | 221 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.10x faster                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 197 us: 1.68x faster                                             |
| pickle_pure_python   | 484 us                                                 | 304 us: 1.59x faster                                             |
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                           |
| xml_etree_process    | 79.1 ms                                                | 56.0 ms: 1.41x faster                                            |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                            |
| xml_etree_generate   | 99.4 ms                                                | 78.9 ms: 1.26x faster                                            |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                            |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.13x faster                                             |
| json_loads           | 31.2 us                                                | 28.4 us: 1.10x faster                                            |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.7 ms: 1.37x faster                                            |
| python_startup_no_site | 5.93 ms                                                | 7.22 ms: 1.22x slower                                            |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.78 ms: 1.67x faster                                            |
| genshi_text     | 31.8 ms                                                | 23.4 ms: 1.36x faster                                            |
| django_template | 48.2 ms                                                | 36.2 ms: 1.33x faster                                            |
| genshi_xml      | 66.0 ms                                                | 59.9 ms: 1.10x faster                                            |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.17x faster                                             |
| generators               | 80.1 ms                                                | 33.3 ms: 2.41x faster                                            |
| async_tree_none          | 728 ms                                                 | 331 ms: 2.20x faster                                             |
| richards_super           | 94.7 ms                                                | 44.4 ms: 2.13x faster                                            |
| richards                 | 79.3 ms                                                | 38.1 ms: 2.08x faster                                            |
| deepcopy_memo            | 58.5 us                                                | 28.4 us: 2.06x faster                                            |
| deltablue                | 7.91 ms                                                | 3.86 ms: 2.05x faster                                            |
| scimark_monte_carlo      | 118 ms                                                 | 57.8 ms: 2.04x faster                                            |
| async_tree_memoization   | 870 ms                                                 | 431 ms: 2.02x faster                                             |
| chaos                    | 115 ms                                                 | 57.9 ms: 1.99x faster                                            |
| async_tree_io            | 1.77 sec                                               | 915 ms: 1.93x faster                                             |
| crypto_pyaes             | 128 ms                                                 | 66.9 ms: 1.91x faster                                            |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                             |
| nbody                    | 154 ms                                                 | 81.3 ms: 1.89x faster                                            |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                             |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                             |
| asyncio_tcp              | 922 ms                                                 | 509 ms: 1.81x faster                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 565 ms: 1.80x faster                                             |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.76x faster                                            |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.73x faster                                             |
| spectral_norm            | 170 ms                                                 | 99.8 ms: 1.70x faster                                            |
| unpickle_pure_python     | 331 us                                                 | 197 us: 1.68x faster                                             |
| mako                     | 16.3 ms                                                | 9.78 ms: 1.67x faster                                            |
| go                       | 240 ms                                                 | 144 ms: 1.66x faster                                             |
| pyflate                  | 716 ms                                                 | 436 ms: 1.64x faster                                             |
| float                    | 117 ms                                                 | 71.5 ms: 1.64x faster                                            |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.59x faster                                             |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                           |
| scimark_fft              | 466 ms                                                 | 300 ms: 1.55x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                            |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.54x faster                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.20 ms: 1.54x faster                                            |
| hexiom                   | 10.4 ms                                                | 6.78 ms: 1.53x faster                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.42 ms: 1.52x faster                                            |
| logging_simple           | 8.30 us                                                | 5.67 us: 1.46x faster                                            |
| logging_format           | 9.09 us                                                | 6.26 us: 1.45x faster                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.77 ms: 1.45x faster                                            |
| fannkuch                 | 532 ms                                                 | 367 ms: 1.45x faster                                             |
| scimark_lu               | 176 ms                                                 | 122 ms: 1.44x faster                                             |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                           |
| pprint_safe_repr         | 1.02 sec                                               | 716 ms: 1.42x faster                                             |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                           |
| pylint                   | 551 ms                                                 | 390 ms: 1.41x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 56.0 ms: 1.41x faster                                            |
| python_startup           | 14.6 ms                                                | 10.7 ms: 1.37x faster                                            |
| genshi_text              | 31.8 ms                                                | 23.4 ms: 1.36x faster                                            |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                            |
| thrift                   | 1.07 ms                                                | 792 us: 1.35x faster                                             |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                           |
| regex_compile            | 188 ms                                                 | 140 ms: 1.34x faster                                             |
| django_template          | 48.2 ms                                                | 36.2 ms: 1.33x faster                                            |
| tornado_http             | 136 ms                                                 | 103 ms: 1.32x faster                                             |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                            |
| nqueens                  | 106 ms                                                 | 83.0 ms: 1.27x faster                                            |
| html5lib                 | 88.9 ms                                                | 69.7 ms: 1.27x faster                                            |
| xml_etree_generate       | 99.4 ms                                                | 78.9 ms: 1.26x faster                                            |
| 2to3                     | 348 ms                                                 | 278 ms: 1.25x faster                                             |
| sqlglot_optimize         | 69.2 ms                                                | 56.6 ms: 1.22x faster                                            |
| sqlglot_normalize        | 143 ms                                                 | 117 ms: 1.22x faster                                             |
| bench_thread_pool        | 986 us                                                 | 827 us: 1.19x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                            |
| dask                     | 441 ms                                                 | 379 ms: 1.16x faster                                             |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                             |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.13x faster                                             |
| genshi_xml               | 66.0 ms                                                | 59.9 ms: 1.10x faster                                            |
| json_loads               | 31.2 us                                                | 28.4 us: 1.10x faster                                            |
| json                     | 5.69 ms                                                | 5.23 ms: 1.09x faster                                            |
| regex_v8                 | 27.8 ms                                                | 25.9 ms: 1.07x faster                                            |
| sympy_sum                | 196 ms                                                 | 183 ms: 1.07x faster                                             |
| sympy_str                | 346 ms                                                 | 323 ms: 1.07x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 24.2 ms: 1.07x faster                                            |
| docutils                 | 3.30 sec                                               | 3.09 sec: 1.07x faster                                           |
| sympy_expand             | 566 ms                                                 | 538 ms: 1.05x faster                                             |
| mdp                      | 2.85 sec                                               | 2.77 sec: 1.03x faster                                           |
| gc_traversal             | 3.62 ms                                                | 3.53 ms: 1.03x faster                                            |
| regex_dna                | 227 ms                                                 | 221 ms: 1.02x faster                                             |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                             |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                             |
| async_generators         | 444 ms                                                 | 453 ms: 1.02x slower                                             |
| telco                    | 7.27 ms                                                | 7.73 ms: 1.06x slower                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                            |
| coverage                 | 79.4 ms                                                | 91.0 ms: 1.15x slower                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.22 ms: 1.22x slower                                            |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                     |

Benchmark hidden because not significant (2): bench_mp_pool, regex_effbot
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240730-3.14.0a0-b523cd2-JIT/bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.21x
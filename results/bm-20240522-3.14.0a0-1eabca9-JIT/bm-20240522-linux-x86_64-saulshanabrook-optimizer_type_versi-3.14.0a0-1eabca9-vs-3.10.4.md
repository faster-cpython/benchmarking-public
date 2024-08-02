# Results vs. 3.10.4

- fork: saulshanabrook
- ref: optimizer_type_versi
- machine: linux-x86_64
- commit hash: 1eabca9
- commit date: 2024-05-22
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 278 ms: 1.25x faster                                                          |
| chameleon      | 9.68 ms                                                | 7.00 ms: 1.38x faster                                                         |
| docutils       | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                        |
| html5lib       | 88.9 ms                                                | 67.0 ms: 1.33x faster                                                         |
| tornado_http   | 136 ms                                                 | 96.7 ms: 1.41x faster                                                         |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 379 ms: 1.92x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 456 ms: 1.91x faster                                                          |
| async_tree_io           | 1.77 sec                                               | 943 ms: 1.87x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 610 ms: 1.67x faster                                                          |
| Geometric mean          | (ref)                                                  | 1.84x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.1 ms: 1.89x faster                                                         |
| float          | 117 ms                                                 | 72.5 ms: 1.61x faster                                                         |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.46x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.37x faster                                                          |
| regex_v8       | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                         |
| regex_dna      | 227 ms                                                 | 228 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                  |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 296 us: 1.64x faster                                                          |
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 221 us: 1.49x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 83.1 ms: 1.20x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.15x faster                                                          |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                          |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                         |
| pickle_list          | 5.08 us                                                | 5.36 us: 1.06x slower                                                         |
| unpickle             | 14.4 us                                                | 15.4 us: 1.07x slower                                                         |
| pickle               | 10.7 us                                                | 12.2 us: 1.15x slower                                                         |
| pickle_dict          | 29.6 us                                                | 36.8 us: 1.24x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                  |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.9 ms: 1.34x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 7.62 ms: 1.28x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.99 ms: 1.63x faster                                                         |
| django_template | 48.2 ms                                                | 36.4 ms: 1.32x faster                                                         |
| genshi_text     | 31.8 ms                                                | 24.4 ms: 1.31x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 56.9 ms: 1.16x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 173 us: 3.15x faster                                                          |
| generators               | 80.1 ms                                                | 30.5 ms: 2.63x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.69 ms: 2.14x faster                                                         |
| richards_super           | 94.7 ms                                                | 48.2 ms: 1.97x faster                                                         |
| chaos                    | 115 ms                                                 | 59.6 ms: 1.94x faster                                                         |
| async_tree_none          | 728 ms                                                 | 379 ms: 1.92x faster                                                          |
| scimark_monte_carlo      | 118 ms                                                 | 61.9 ms: 1.91x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 66.9 ms: 1.91x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 456 ms: 1.91x faster                                                          |
| richards                 | 79.3 ms                                                | 41.7 ms: 1.90x faster                                                         |
| nbody                    | 154 ms                                                 | 81.1 ms: 1.89x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 943 ms: 1.87x faster                                                          |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                                          |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                          |
| asyncio_tcp              | 922 ms                                                 | 521 ms: 1.77x faster                                                          |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.74x faster                                                         |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 610 ms: 1.67x faster                                                          |
| pickle_pure_python       | 484 us                                                 | 296 us: 1.64x faster                                                          |
| mako                     | 16.3 ms                                                | 9.99 ms: 1.63x faster                                                         |
| go                       | 240 ms                                                 | 147 ms: 1.63x faster                                                          |
| pyflate                  | 716 ms                                                 | 439 ms: 1.63x faster                                                          |
| float                    | 117 ms                                                 | 72.5 ms: 1.61x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                        |
| scimark_sor              | 220 ms                                                 | 138 ms: 1.59x faster                                                          |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.62 ms: 1.57x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 37.3 us: 1.57x faster                                                         |
| pylint                   | 551 ms                                                 | 353 ms: 1.56x faster                                                          |
| fannkuch                 | 532 ms                                                 | 354 ms: 1.50x faster                                                          |
| scimark_fft              | 466 ms                                                 | 311 ms: 1.50x faster                                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.33 ms: 1.50x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 221 us: 1.49x faster                                                          |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 694 ms: 1.47x faster                                                          |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.76 us: 1.44x faster                                                         |
| logging_format           | 9.09 us                                                | 6.39 us: 1.42x faster                                                         |
| scimark_lu               | 176 ms                                                 | 124 ms: 1.42x faster                                                          |
| tornado_http             | 136 ms                                                 | 96.7 ms: 1.41x faster                                                         |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                         |
| chameleon                | 9.68 ms                                                | 7.00 ms: 1.38x faster                                                         |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                        |
| regex_compile            | 188 ms                                                 | 138 ms: 1.37x faster                                                          |
| xml_etree_process        | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                         |
| python_startup           | 14.6 ms                                                | 10.9 ms: 1.34x faster                                                         |
| html5lib                 | 88.9 ms                                                | 67.0 ms: 1.33x faster                                                         |
| django_template          | 48.2 ms                                                | 36.4 ms: 1.32x faster                                                         |
| genshi_text              | 31.8 ms                                                | 24.4 ms: 1.31x faster                                                         |
| deepcopy                 | 479 us                                                 | 367 us: 1.31x faster                                                          |
| thrift                   | 1.07 ms                                                | 833 us: 1.29x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 3.32 us: 1.26x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                          |
| 2to3                     | 348 ms                                                 | 278 ms: 1.25x faster                                                          |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 69.0 ms: 1.22x faster                                                         |
| nqueens                  | 106 ms                                                 | 86.9 ms: 1.22x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 56.8 ms: 1.22x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 83.1 ms: 1.20x faster                                                         |
| dask                     | 441 ms                                                 | 378 ms: 1.17x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 56.9 ms: 1.16x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.15x faster                                                          |
| sympy_str                | 346 ms                                                 | 301 ms: 1.15x faster                                                          |
| sympy_integrate          | 25.8 ms                                                | 22.5 ms: 1.15x faster                                                         |
| bench_thread_pool        | 986 us                                                 | 862 us: 1.14x faster                                                          |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.14x faster                                                          |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                         |
| sympy_expand             | 566 ms                                                 | 511 ms: 1.11x faster                                                          |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                                          |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                         |
| json                     | 5.69 ms                                                | 5.23 ms: 1.09x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.05x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.79 sec: 1.02x faster                                                        |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                          |
| regex_dna                | 227 ms                                                 | 228 ms: 1.01x slower                                                          |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                                          |
| async_generators         | 444 ms                                                 | 460 ms: 1.04x slower                                                          |
| gc_traversal             | 3.62 ms                                                | 3.80 ms: 1.05x slower                                                         |
| pickle_list              | 5.08 us                                                | 5.36 us: 1.06x slower                                                         |
| unpickle                 | 14.4 us                                                | 15.4 us: 1.07x slower                                                         |
| flaskblogging            | 8.58 ms                                                | 9.18 ms: 1.07x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 1.80 ms: 1.11x slower                                                         |
| telco                    | 7.27 ms                                                | 8.19 ms: 1.13x slower                                                         |
| pickle                   | 10.7 us                                                | 12.2 us: 1.15x slower                                                         |
| coverage                 | 79.4 ms                                                | 92.5 ms: 1.16x slower                                                         |
| pickle_dict              | 29.6 us                                                | 36.8 us: 1.24x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 7.62 ms: 1.28x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                                  |

Benchmark hidden because not significant (3): regex_effbot, unpickle_list, bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240522-3.14.0a0-1eabca9-JIT/bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.21x
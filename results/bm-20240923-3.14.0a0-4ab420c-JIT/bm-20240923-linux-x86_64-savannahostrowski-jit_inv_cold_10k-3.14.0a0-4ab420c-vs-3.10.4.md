# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_inv_cold_10k
- machine: linux-x86_64
- commit hash: 4ab420c
- commit date: 2024-09-23
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 285 ms: 1.22x faster                                                         |
| docutils       | 3.30 sec                                               | 2.89 sec: 1.14x faster                                                       |
| html5lib       | 88.9 ms                                                | 66.2 ms: 1.34x faster                                                        |
| tornado_http   | 136 ms                                                 | 96.0 ms: 1.42x faster                                                        |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 320 ms: 2.28x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 399 ms: 2.18x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 886 ms: 2.00x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 569 ms: 1.79x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.1 ms: 1.87x faster                                                        |
| float          | 117 ms                                                 | 71.4 ms: 1.64x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.47x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.35x faster                                                         |
| regex_v8       | 27.8 ms                                                | 26.2 ms: 1.06x faster                                                        |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.78 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                                         |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                        |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.40x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 80.7 ms: 1.23x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 99.7 ms: 1.16x faster                                                        |
| json_loads           | 31.2 us                                                | 27.4 us: 1.14x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                         |
| pickle_list          | 5.08 us                                                | 5.18 us: 1.02x slower                                                        |
| unpickle_list        | 5.20 us                                                | 5.32 us: 1.02x slower                                                        |
| unpickle             | 14.4 us                                                | 15.0 us: 1.04x slower                                                        |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                                        |
| pickle_dict          | 29.6 us                                                | 34.6 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.94 ms: 1.64x faster                                                        |
| django_template | 48.2 ms                                                | 36.9 ms: 1.31x faster                                                        |
| genshi_text     | 31.8 ms                                                | 25.7 ms: 1.24x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 60.8 ms: 1.09x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.29x faster                                                         |
| async_tree_none          | 728 ms                                                 | 320 ms: 2.28x faster                                                         |
| generators               | 80.1 ms                                                | 35.6 ms: 2.25x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 399 ms: 2.18x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.65 ms: 2.17x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 27.0 us: 2.17x faster                                                        |
| richards_super           | 94.7 ms                                                | 47.0 ms: 2.02x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 886 ms: 2.00x faster                                                         |
| chaos                    | 115 ms                                                 | 59.3 ms: 1.95x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 67.9 ms: 1.88x faster                                                        |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.87x faster                                                         |
| nbody                    | 154 ms                                                 | 82.1 ms: 1.87x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 495 ms: 1.86x faster                                                         |
| richards                 | 79.3 ms                                                | 42.7 ms: 1.86x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 63.7 ms: 1.86x faster                                                        |
| logging_silent           | 190 ns                                                 | 102 ns: 1.85x faster                                                         |
| raytrace                 | 507 ms                                                 | 281 ms: 1.80x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 569 ms: 1.79x faster                                                         |
| deepcopy                 | 479 us                                                 | 269 us: 1.78x faster                                                         |
| go                       | 240 ms                                                 | 136 ms: 1.77x faster                                                         |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                        |
| mako                     | 16.3 ms                                                | 9.94 ms: 1.64x faster                                                        |
| float                    | 117 ms                                                 | 71.4 ms: 1.64x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.35 ms: 1.60x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                                         |
| pyflate                  | 716 ms                                                 | 456 ms: 1.57x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                        |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.52x faster                                                        |
| spectral_norm            | 170 ms                                                 | 112 ms: 1.51x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                         |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.40 ms: 1.47x faster                                                        |
| logging_format           | 9.09 us                                                | 6.18 us: 1.47x faster                                                        |
| scimark_fft              | 466 ms                                                 | 317 ms: 1.47x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.68 us: 1.46x faster                                                        |
| pylint                   | 551 ms                                                 | 380 ms: 1.45x faster                                                         |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                       |
| tornado_http             | 136 ms                                                 | 96.0 ms: 1.42x faster                                                        |
| fannkuch                 | 532 ms                                                 | 376 ms: 1.41x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                        |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.40x faster                                                        |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                        |
| thrift                   | 1.07 ms                                                | 786 us: 1.36x faster                                                         |
| regex_compile            | 188 ms                                                 | 139 ms: 1.35x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                                       |
| html5lib                 | 88.9 ms                                                | 66.2 ms: 1.34x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 760 ms: 1.34x faster                                                         |
| hexiom                   | 10.4 ms                                                | 7.80 ms: 1.33x faster                                                        |
| django_template          | 48.2 ms                                                | 36.9 ms: 1.31x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.23 sec: 1.28x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 68.1 ms: 1.24x faster                                                        |
| genshi_text              | 31.8 ms                                                | 25.7 ms: 1.24x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 80.7 ms: 1.23x faster                                                        |
| 2to3                     | 348 ms                                                 | 285 ms: 1.22x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 117 ms: 1.22x faster                                                         |
| nqueens                  | 106 ms                                                 | 87.7 ms: 1.21x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 841 us: 1.17x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 99.7 ms: 1.16x faster                                                        |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.14x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.89 sec: 1.14x faster                                                       |
| json_loads               | 31.2 us                                                | 27.4 us: 1.14x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                         |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                                         |
| sympy_expand             | 566 ms                                                 | 503 ms: 1.12x faster                                                         |
| sympy_str                | 346 ms                                                 | 308 ms: 1.12x faster                                                         |
| json                     | 5.69 ms                                                | 5.08 ms: 1.12x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.11x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 60.8 ms: 1.09x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 64.3 ms: 1.08x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 26.2 ms: 1.06x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                         |
| pickle_list              | 5.08 us                                                | 5.18 us: 1.02x slower                                                        |
| unpickle_list            | 5.20 us                                                | 5.32 us: 1.02x slower                                                        |
| async_generators         | 444 ms                                                 | 456 ms: 1.03x slower                                                         |
| sympy_integrate          | 25.8 ms                                                | 26.7 ms: 1.03x slower                                                        |
| regex_effbot             | 3.63 ms                                                | 3.78 ms: 1.04x slower                                                        |
| unpickle                 | 14.4 us                                                | 15.0 us: 1.04x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 3.80 ms: 1.05x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 1.72 ms: 1.06x slower                                                        |
| coverage                 | 79.4 ms                                                | 86.9 ms: 1.09x slower                                                        |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                                        |
| telco                    | 7.27 ms                                                | 8.03 ms: 1.10x slower                                                        |
| pickle_dict              | 29.6 us                                                | 34.6 us: 1.17x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                        |
| unpack_sequence          | 60.0 ns                                                | 112 ns: 1.86x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240923-3.14.0a0-4ab420c-JIT/bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.17x
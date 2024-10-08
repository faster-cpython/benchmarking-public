# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_inv_mem_100k
- machine: linux-x86_64
- commit hash: 17ece50
- commit date: 2024-09-23
- overall geometric mean: 1.37x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.24x faster                                                         |
| docutils       | 3.30 sec                                               | 2.93 sec: 1.12x faster                                                       |
| html5lib       | 88.9 ms                                                | 65.8 ms: 1.35x faster                                                        |
| tornado_http   | 136 ms                                                 | 94.9 ms: 1.44x faster                                                        |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 318 ms: 2.29x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 409 ms: 2.13x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 886 ms: 2.00x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 574 ms: 1.77x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.6 ms: 1.91x faster                                                        |
| float          | 117 ms                                                 | 71.1 ms: 1.65x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.48x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 144 ms: 1.31x faster                                                         |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                        |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 308 us: 1.57x faster                                                         |
| unpickle_pure_python | 331 us                                                 | 221 us: 1.50x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 55.6 ms: 1.42x faster                                                        |
| json_dumps           | 14.2 ms                                                | 10.0 ms: 1.42x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 78.2 ms: 1.27x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 98.8 ms: 1.17x faster                                                        |
| json_loads           | 31.2 us                                                | 27.2 us: 1.15x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                         |
| pickle_list          | 5.08 us                                                | 5.15 us: 1.01x slower                                                        |
| unpickle             | 14.4 us                                                | 14.9 us: 1.03x slower                                                        |
| pickle               | 10.7 us                                                | 11.9 us: 1.12x slower                                                        |
| pickle_dict          | 29.6 us                                                | 34.9 us: 1.18x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.75 ms: 1.68x faster                                                        |
| django_template | 48.2 ms                                                | 36.3 ms: 1.33x faster                                                        |
| genshi_text     | 31.8 ms                                                | 25.4 ms: 1.25x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 59.2 ms: 1.12x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.46x faster                                                        |
| async_tree_none          | 728 ms                                                 | 318 ms: 2.29x faster                                                         |
| generators               | 80.1 ms                                                | 35.2 ms: 2.27x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 27.1 us: 2.16x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 409 ms: 2.13x faster                                                         |
| richards_super           | 94.7 ms                                                | 46.0 ms: 2.06x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 886 ms: 2.00x faster                                                         |
| richards                 | 79.3 ms                                                | 40.9 ms: 1.94x faster                                                        |
| chaos                    | 115 ms                                                 | 59.6 ms: 1.94x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 66.7 ms: 1.92x faster                                                        |
| nbody                    | 154 ms                                                 | 80.6 ms: 1.91x faster                                                        |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 63.0 ms: 1.88x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 495 ms: 1.86x faster                                                         |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                         |
| go                       | 240 ms                                                 | 132 ms: 1.82x faster                                                         |
| deepcopy                 | 479 us                                                 | 265 us: 1.81x faster                                                         |
| raytrace                 | 507 ms                                                 | 281 ms: 1.80x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 574 ms: 1.77x faster                                                         |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                        |
| mako                     | 16.3 ms                                                | 9.75 ms: 1.68x faster                                                        |
| float                    | 117 ms                                                 | 71.1 ms: 1.65x faster                                                        |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.35 ms: 1.61x faster                                                        |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.58x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.64 us: 1.58x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 308 us: 1.57x faster                                                         |
| pyflate                  | 716 ms                                                 | 459 ms: 1.56x faster                                                         |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.52x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 221 us: 1.50x faster                                                         |
| hexiom                   | 10.4 ms                                                | 7.02 ms: 1.48x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.38 ms: 1.48x faster                                                        |
| scimark_fft              | 466 ms                                                 | 317 ms: 1.47x faster                                                         |
| logging_format           | 9.09 us                                                | 6.22 us: 1.46x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.69 us: 1.46x faster                                                        |
| pylint                   | 551 ms                                                 | 378 ms: 1.46x faster                                                         |
| tornado_http             | 136 ms                                                 | 94.9 ms: 1.44x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 55.6 ms: 1.42x faster                                                        |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                       |
| json_dumps               | 14.2 ms                                                | 10.0 ms: 1.42x faster                                                        |
| fannkuch                 | 532 ms                                                 | 378 ms: 1.41x faster                                                         |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                        |
| thrift                   | 1.07 ms                                                | 786 us: 1.36x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 751 ms: 1.36x faster                                                         |
| html5lib                 | 88.9 ms                                                | 65.8 ms: 1.35x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                                       |
| django_template          | 48.2 ms                                                | 36.3 ms: 1.33x faster                                                        |
| regex_compile            | 188 ms                                                 | 144 ms: 1.31x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.22 sec: 1.30x faster                                                       |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 78.2 ms: 1.27x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                         |
| genshi_text              | 31.8 ms                                                | 25.4 ms: 1.25x faster                                                        |
| 2to3                     | 348 ms                                                 | 280 ms: 1.24x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 68.5 ms: 1.23x faster                                                        |
| nqueens                  | 106 ms                                                 | 87.1 ms: 1.21x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 839 us: 1.18x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 98.8 ms: 1.17x faster                                                        |
| json_loads               | 31.2 us                                                | 27.2 us: 1.15x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 60.7 ms: 1.14x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                         |
| sympy_str                | 346 ms                                                 | 305 ms: 1.14x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.93 sec: 1.12x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                       |
| sympy_sum                | 196 ms                                                 | 176 ms: 1.12x faster                                                         |
| sympy_expand             | 566 ms                                                 | 507 ms: 1.12x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 59.2 ms: 1.12x faster                                                        |
| json                     | 5.69 ms                                                | 5.10 ms: 1.12x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 23.1 ms: 1.11x faster                                                        |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                         |
| pickle_list              | 5.08 us                                                | 5.15 us: 1.01x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 3.68 ms: 1.02x slower                                                        |
| async_generators         | 444 ms                                                 | 457 ms: 1.03x slower                                                         |
| unpickle                 | 14.4 us                                                | 14.9 us: 1.03x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 1.72 ms: 1.06x slower                                                        |
| telco                    | 7.27 ms                                                | 7.98 ms: 1.10x slower                                                        |
| pickle                   | 10.7 us                                                | 11.9 us: 1.12x slower                                                        |
| coverage                 | 79.4 ms                                                | 89.3 ms: 1.12x slower                                                        |
| pickle_dict              | 29.6 us                                                | 34.9 us: 1.18x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                        |
| unpack_sequence          | 60.0 ns                                                | 107 ns: 1.79x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                                 |

Benchmark hidden because not significant (3): unpickle_list, bench_mp_pool, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240923-3.14.0a0-17ece50-JIT/bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.18x
# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_inv_cold_100
- machine: linux-x86_64
- commit hash: 99262b6
- commit date: 2024-09-19
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 318 ms: 1.09x faster                                                         |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                       |
| html5lib       | 88.9 ms                                                | 63.2 ms: 1.41x faster                                                        |
| tornado_http   | 136 ms                                                 | 110 ms: 1.24x faster                                                         |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 322 ms: 2.26x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 403 ms: 2.16x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 892 ms: 1.98x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 570 ms: 1.78x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 85.5 ms: 1.80x faster                                                        |
| float          | 117 ms                                                 | 71.3 ms: 1.64x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.45x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                         |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                                         |
| regex_v8       | 27.8 ms                                                | 26.4 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 220 us: 1.50x faster                                                         |
| tomli_loads          | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 331 us: 1.46x faster                                                         |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                        |
| json_loads           | 31.2 us                                                | 26.8 us: 1.16x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 85.6 ms: 1.16x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 99.7 ms: 1.16x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                         |
| unpickle             | 14.4 us                                                | 14.5 us: 1.01x slower                                                        |
| unpickle_list        | 5.20 us                                                | 5.26 us: 1.01x slower                                                        |
| pickle_list          | 5.08 us                                                | 5.17 us: 1.02x slower                                                        |
| pickle               | 10.7 us                                                | 11.8 us: 1.10x slower                                                        |
| pickle_dict          | 29.6 us                                                | 35.4 us: 1.20x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                        |
| genshi_text     | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                        |
| django_template | 48.2 ms                                                | 38.4 ms: 1.26x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 57.8 ms: 1.14x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.27x faster                                                         |
| async_tree_none          | 728 ms                                                 | 322 ms: 2.26x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.58 ms: 2.21x faster                                                        |
| generators               | 80.1 ms                                                | 36.8 ms: 2.18x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 403 ms: 2.16x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 27.5 us: 2.13x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 892 ms: 1.98x faster                                                         |
| go                       | 240 ms                                                 | 122 ms: 1.96x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 67.5 ms: 1.89x faster                                                        |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                         |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                                         |
| chaos                    | 115 ms                                                 | 62.5 ms: 1.85x faster                                                        |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                         |
| asyncio_tcp              | 922 ms                                                 | 504 ms: 1.83x faster                                                         |
| nbody                    | 154 ms                                                 | 85.5 ms: 1.80x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 65.9 ms: 1.79x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 570 ms: 1.78x faster                                                         |
| richards_super           | 94.7 ms                                                | 53.2 ms: 1.78x faster                                                        |
| deepcopy                 | 479 us                                                 | 270 us: 1.77x faster                                                         |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.75x faster                                                        |
| richards                 | 79.3 ms                                                | 48.2 ms: 1.64x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                        |
| float                    | 117 ms                                                 | 71.3 ms: 1.64x faster                                                        |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.64 us: 1.58x faster                                                        |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                         |
| spectral_norm            | 170 ms                                                 | 110 ms: 1.55x faster                                                         |
| pyflate                  | 716 ms                                                 | 466 ms: 1.54x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.81 ms: 1.53x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.50x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                       |
| pylint                   | 551 ms                                                 | 376 ms: 1.47x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 331 us: 1.46x faster                                                         |
| logging_format           | 9.09 us                                                | 6.25 us: 1.45x faster                                                        |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.47 ms: 1.45x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.74 us: 1.45x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.82 sec: 1.41x faster                                                       |
| html5lib                 | 88.9 ms                                                | 63.2 ms: 1.41x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.83 ms: 1.40x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 732 ms: 1.39x faster                                                         |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                        |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                        |
| fannkuch                 | 532 ms                                                 | 389 ms: 1.37x faster                                                         |
| thrift                   | 1.07 ms                                                | 788 us: 1.36x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                        |
| genshi_text              | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                        |
| scimark_fft              | 466 ms                                                 | 366 ms: 1.27x faster                                                         |
| django_template          | 48.2 ms                                                | 38.4 ms: 1.26x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                        |
| sympy_sum                | 196 ms                                                 | 157 ms: 1.25x faster                                                         |
| tornado_http             | 136 ms                                                 | 110 ms: 1.24x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 116 ms: 1.23x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                       |
| dulwich_log              | 84.3 ms                                                | 69.2 ms: 1.22x faster                                                        |
| sympy_str                | 346 ms                                                 | 284 ms: 1.22x faster                                                         |
| nqueens                  | 106 ms                                                 | 87.5 ms: 1.21x faster                                                        |
| sympy_expand             | 566 ms                                                 | 470 ms: 1.20x faster                                                         |
| json_loads               | 31.2 us                                                | 26.8 us: 1.16x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 85.6 ms: 1.16x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 99.7 ms: 1.16x faster                                                        |
| json                     | 5.69 ms                                                | 4.94 ms: 1.15x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 60.1 ms: 1.15x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 57.8 ms: 1.14x faster                                                        |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                                        |
| 2to3                     | 348 ms                                                 | 318 ms: 1.09x faster                                                         |
| bench_thread_pool        | 986 us                                                 | 928 us: 1.06x faster                                                         |
| meteor_contest           | 120 ms                                                 | 113 ms: 1.06x faster                                                         |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.70 sec: 1.05x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 26.4 ms: 1.05x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                         |
| unpickle                 | 14.4 us                                                | 14.5 us: 1.01x slower                                                        |
| unpickle_list            | 5.20 us                                                | 5.26 us: 1.01x slower                                                        |
| pickle_list              | 5.08 us                                                | 5.17 us: 1.02x slower                                                        |
| async_generators         | 444 ms                                                 | 454 ms: 1.02x slower                                                         |
| coverage                 | 79.4 ms                                                | 84.9 ms: 1.07x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                                        |
| sympy_integrate          | 25.8 ms                                                | 28.0 ms: 1.09x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 3.96 ms: 1.09x slower                                                        |
| pickle                   | 10.7 us                                                | 11.8 us: 1.10x slower                                                        |
| telco                    | 7.27 ms                                                | 8.08 ms: 1.11x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                        |
| pickle_dict              | 29.6 us                                                | 35.4 us: 1.20x slower                                                        |
| unpack_sequence          | 60.0 ns                                                | 110 ns: 1.83x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                                 |

Benchmark hidden because not significant (2): regex_effbot, bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240919-3.14.0a0-99262b6-JIT/bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.15x
# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_inv_cold_100
- machine: linux-x86_64
- commit hash: 0ee16f5
- commit date: 2024-09-23
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 318 ms: 1.09x faster                                                         |
| docutils       | 3.30 sec                                               | 2.72 sec: 1.21x faster                                                       |
| html5lib       | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                        |
| tornado_http   | 136 ms                                                 | 110 ms: 1.24x faster                                                         |
| Geometric mean | (ref)                                                  | 1.22x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 319 ms: 2.28x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 407 ms: 2.14x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 892 ms: 1.98x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 574 ms: 1.77x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.6 ms: 1.91x faster                                                        |
| float          | 117 ms                                                 | 70.9 ms: 1.65x faster                                                        |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.47x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.43x faster                                                         |
| regex_dna      | 227 ms                                                 | 221 ms: 1.02x faster                                                         |
| regex_v8       | 27.8 ms                                                | 27.3 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 220 us: 1.50x faster                                                         |
| tomli_loads          | 3.14 sec                                               | 2.14 sec: 1.46x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 332 us: 1.46x faster                                                         |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 61.2 ms: 1.29x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 100.0 ms: 1.16x faster                                                       |
| json_loads           | 31.2 us                                                | 27.3 us: 1.14x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 88.8 ms: 1.12x faster                                                        |
| pickle_list          | 5.08 us                                                | 5.11 us: 1.01x slower                                                        |
| unpickle             | 14.4 us                                                | 15.2 us: 1.06x slower                                                        |
| pickle               | 10.7 us                                                | 11.5 us: 1.08x slower                                                        |
| pickle_dict          | 29.6 us                                                | 35.2 us: 1.19x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.5 ms: 1.56x faster                                                        |
| django_template | 48.2 ms                                                | 37.1 ms: 1.30x faster                                                        |
| genshi_text     | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 58.3 ms: 1.13x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.29x faster                                                         |
| async_tree_none          | 728 ms                                                 | 319 ms: 2.28x faster                                                         |
| generators               | 80.1 ms                                                | 35.5 ms: 2.26x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.58 ms: 2.21x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 407 ms: 2.14x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 27.8 us: 2.11x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 892 ms: 1.98x faster                                                         |
| go                       | 240 ms                                                 | 122 ms: 1.97x faster                                                         |
| nbody                    | 154 ms                                                 | 80.6 ms: 1.91x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 67.7 ms: 1.89x faster                                                        |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.87x faster                                                         |
| chaos                    | 115 ms                                                 | 61.6 ms: 1.87x faster                                                        |
| logging_silent           | 190 ns                                                 | 102 ns: 1.87x faster                                                         |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                         |
| asyncio_tcp              | 922 ms                                                 | 505 ms: 1.83x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 65.5 ms: 1.80x faster                                                        |
| richards_super           | 94.7 ms                                                | 52.9 ms: 1.79x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 574 ms: 1.77x faster                                                         |
| deepcopy                 | 479 us                                                 | 272 us: 1.76x faster                                                         |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.72x faster                                                        |
| richards                 | 79.3 ms                                                | 47.9 ms: 1.66x faster                                                        |
| float                    | 117 ms                                                 | 70.9 ms: 1.65x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.64 us: 1.58x faster                                                        |
| mako                     | 16.3 ms                                                | 10.5 ms: 1.56x faster                                                        |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                         |
| spectral_norm            | 170 ms                                                 | 110 ms: 1.55x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.84 ms: 1.52x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.50x faster                                                         |
| pyflate                  | 716 ms                                                 | 486 ms: 1.47x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 2.14 sec: 1.46x faster                                                       |
| pylint                   | 551 ms                                                 | 377 ms: 1.46x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 332 us: 1.46x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.45 ms: 1.45x faster                                                        |
| logging_format           | 9.09 us                                                | 6.27 us: 1.45x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.79 us: 1.43x faster                                                        |
| regex_compile            | 188 ms                                                 | 132 ms: 1.43x faster                                                         |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.82 sec: 1.42x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 732 ms: 1.39x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.85 ms: 1.39x faster                                                        |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                        |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                        |
| fannkuch                 | 532 ms                                                 | 390 ms: 1.36x faster                                                         |
| html5lib                 | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                        |
| thrift                   | 1.07 ms                                                | 798 us: 1.34x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.30x faster                                                       |
| django_template          | 48.2 ms                                                | 37.1 ms: 1.30x faster                                                        |
| genshi_text              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 61.2 ms: 1.29x faster                                                        |
| scimark_fft              | 466 ms                                                 | 365 ms: 1.28x faster                                                         |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                        |
| tornado_http             | 136 ms                                                 | 110 ms: 1.24x faster                                                         |
| sympy_sum                | 196 ms                                                 | 159 ms: 1.24x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 116 ms: 1.23x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 69.1 ms: 1.22x faster                                                        |
| nqueens                  | 106 ms                                                 | 87.1 ms: 1.22x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.72 sec: 1.21x faster                                                       |
| sympy_str                | 346 ms                                                 | 287 ms: 1.21x faster                                                         |
| sympy_expand             | 566 ms                                                 | 474 ms: 1.19x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 100.0 ms: 1.16x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 60.3 ms: 1.15x faster                                                        |
| json_loads               | 31.2 us                                                | 27.3 us: 1.14x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 58.3 ms: 1.13x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 88.8 ms: 1.12x faster                                                        |
| json                     | 5.69 ms                                                | 5.09 ms: 1.12x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                                        |
| 2to3                     | 348 ms                                                 | 318 ms: 1.09x faster                                                         |
| bench_thread_pool        | 986 us                                                 | 932 us: 1.06x faster                                                         |
| meteor_contest           | 120 ms                                                 | 113 ms: 1.06x faster                                                         |
| regex_dna                | 227 ms                                                 | 221 ms: 1.02x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 27.3 ms: 1.02x faster                                                        |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                         |
| pickle_list              | 5.08 us                                                | 5.11 us: 1.01x slower                                                        |
| async_generators         | 444 ms                                                 | 460 ms: 1.04x slower                                                         |
| unpickle                 | 14.4 us                                                | 15.2 us: 1.06x slower                                                        |
| coverage                 | 79.4 ms                                                | 84.6 ms: 1.07x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                                        |
| pickle                   | 10.7 us                                                | 11.5 us: 1.08x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 3.93 ms: 1.08x slower                                                        |
| sympy_integrate          | 25.8 ms                                                | 28.1 ms: 1.09x slower                                                        |
| telco                    | 7.27 ms                                                | 8.09 ms: 1.11x slower                                                        |
| pickle_dict              | 29.6 us                                                | 35.2 us: 1.19x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                        |
| unpack_sequence          | 60.0 ns                                                | 109 ns: 1.81x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                                 |

Benchmark hidden because not significant (4): bench_mp_pool, asyncio_websockets, regex_effbot, unpickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240923-3.14.0a0-0ee16f5-JIT/bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.15x
# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow_known
- machine: linux-x86_64
- commit hash: 8763a2d
- commit date: 2024-09-07
- overall geometric mean: 1.37x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 281 ms: 1.24x faster                                                   |
| docutils       | 3.30 sec                                               | 3.01 sec: 1.10x faster                                                 |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.44x faster                                                  |
| tornado_http   | 136 ms                                                 | 96.8 ms: 1.41x faster                                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 327 ms: 2.23x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 396 ms: 2.20x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 936 ms: 1.89x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 563 ms: 1.80x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.4 ms: 1.91x faster                                                  |
| float          | 117 ms                                                 | 70.1 ms: 1.67x faster                                                  |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.48x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 146 ms: 1.29x faster                                                   |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                  |
| regex_dna      | 227 ms                                                 | 213 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 198 us: 1.67x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 54.4 ms: 1.46x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 76.9 ms: 1.29x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                   |
| json_loads           | 31.2 us                                                | 28.2 us: 1.10x faster                                                  |
| pickle_list          | 5.08 us                                                | 5.30 us: 1.04x slower                                                  |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                                  |
| pickle               | 10.7 us                                                | 12.0 us: 1.13x slower                                                  |
| pickle_dict          | 29.6 us                                                | 34.9 us: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.7 ms: 1.37x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.72 ms: 1.68x faster                                                  |
| django_template | 48.2 ms                                                | 35.7 ms: 1.35x faster                                                  |
| genshi_text     | 31.8 ms                                                | 23.9 ms: 1.33x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 54.1 ms: 1.22x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.30x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.12 ms: 2.53x faster                                                  |
| generators               | 80.1 ms                                                | 33.1 ms: 2.42x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 25.2 us: 2.32x faster                                                  |
| richards_super           | 94.7 ms                                                | 42.3 ms: 2.24x faster                                                  |
| async_tree_none          | 728 ms                                                 | 327 ms: 2.23x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 396 ms: 2.20x faster                                                   |
| richards                 | 79.3 ms                                                | 37.8 ms: 2.10x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 66.5 ms: 1.92x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 482 ms: 1.91x faster                                                   |
| nbody                    | 154 ms                                                 | 80.4 ms: 1.91x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 936 ms: 1.89x faster                                                   |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                   |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                   |
| chaos                    | 115 ms                                                 | 61.6 ms: 1.87x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 563 ms: 1.80x faster                                                   |
| deepcopy                 | 479 us                                                 | 267 us: 1.80x faster                                                   |
| raytrace                 | 507 ms                                                 | 283 ms: 1.79x faster                                                   |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                  |
| go                       | 240 ms                                                 | 139 ms: 1.73x faster                                                   |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                   |
| mako                     | 16.3 ms                                                | 9.72 ms: 1.68x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 198 us: 1.67x faster                                                   |
| float                    | 117 ms                                                 | 70.1 ms: 1.67x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                 |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.60x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.38 ms: 1.57x faster                                                  |
| pyflate                  | 716 ms                                                 | 455 ms: 1.57x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 77.3 ms: 1.53x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.70 ms: 1.51x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                   |
| pylint                   | 551 ms                                                 | 373 ms: 1.48x faster                                                   |
| scimark_fft              | 466 ms                                                 | 316 ms: 1.47x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.67 us: 1.47x faster                                                  |
| logging_format           | 9.09 us                                                | 6.22 us: 1.46x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 54.4 ms: 1.46x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.49 ms: 1.44x faster                                                  |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.44x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                 |
| fannkuch                 | 532 ms                                                 | 373 ms: 1.42x faster                                                   |
| tornado_http             | 136 ms                                                 | 96.8 ms: 1.41x faster                                                  |
| thrift                   | 1.07 ms                                                | 771 us: 1.39x faster                                                   |
| python_startup           | 14.6 ms                                                | 10.7 ms: 1.37x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 751 ms: 1.36x faster                                                   |
| django_template          | 48.2 ms                                                | 35.7 ms: 1.35x faster                                                  |
| hexiom                   | 10.4 ms                                                | 7.72 ms: 1.35x faster                                                  |
| genshi_text              | 31.8 ms                                                | 23.9 ms: 1.33x faster                                                  |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.30x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 76.9 ms: 1.29x faster                                                  |
| regex_compile            | 188 ms                                                 | 146 ms: 1.29x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.24 sec: 1.27x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                   |
| 2to3                     | 348 ms                                                 | 281 ms: 1.24x faster                                                   |
| nqueens                  | 106 ms                                                 | 86.2 ms: 1.23x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 54.1 ms: 1.22x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 70.8 ms: 1.19x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 835 us: 1.18x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 58.7 ms: 1.18x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                  |
| sympy_str                | 346 ms                                                 | 306 ms: 1.13x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 23.0 ms: 1.12x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                                 |
| sympy_expand             | 566 ms                                                 | 508 ms: 1.11x faster                                                   |
| json_loads               | 31.2 us                                                | 28.2 us: 1.10x faster                                                  |
| sympy_sum                | 196 ms                                                 | 179 ms: 1.10x faster                                                   |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                   |
| docutils                 | 3.30 sec                                               | 3.01 sec: 1.10x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                  |
| regex_dna                | 227 ms                                                 | 213 ms: 1.07x faster                                                   |
| json                     | 5.69 ms                                                | 5.38 ms: 1.06x faster                                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| gc_traversal             | 3.62 ms                                                | 3.59 ms: 1.01x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                   |
| async_generators         | 444 ms                                                 | 462 ms: 1.04x slower                                                   |
| pickle_list              | 5.08 us                                                | 5.30 us: 1.04x slower                                                  |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                                  |
| coverage                 | 79.4 ms                                                | 85.4 ms: 1.08x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                  |
| telco                    | 7.27 ms                                                | 7.97 ms: 1.10x slower                                                  |
| pickle                   | 10.7 us                                                | 12.0 us: 1.13x slower                                                  |
| pickle_dict              | 29.6 us                                                | 34.9 us: 1.18x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                  |
| unpack_sequence          | 60.0 ns                                                | 145 ns: 2.42x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                           |

Benchmark hidden because not significant (3): regex_effbot, bench_mp_pool, unpickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240907-3.14.0a0-8763a2d-JIT/bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.24x
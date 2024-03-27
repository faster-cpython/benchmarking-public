# Results vs. 3.10.4

- fork: brandtbucher
- ref: revert_90a1b28
- machine: linux-x86_64
- commit hash: 0f9d2fe
- commit date: 2024-03-27
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 267 ms: 1.31x faster                                                   |
| chameleon      | 9.68 ms                                                | 6.95 ms: 1.39x faster                                                  |
| docutils       | 3.30 sec                                               | 2.76 sec: 1.19x faster                                                 |
| html5lib       | 88.9 ms                                                | 65.7 ms: 1.35x faster                                                  |
| tornado_http   | 136 ms                                                 | 95.0 ms: 1.44x faster                                                  |
| Geometric mean | (ref)                                                  | 1.33x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 368 ms: 1.98x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 442 ms: 1.97x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 918 ms: 1.93x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 609 ms: 1.67x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.88x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 90.2 ms: 1.70x faster                                                  |
| float          | 117 ms                                                 | 76.7 ms: 1.53x faster                                                  |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.38x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.40x faster                                                   |
| regex_v8       | 27.8 ms                                                | 25.6 ms: 1.08x faster                                                  |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.71 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 299 us: 1.62x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 2.17 sec: 1.45x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 59.2 ms: 1.34x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 85.8 ms: 1.16x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                   |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 160 ms: 1.05x faster                                                   |
| pickle_list          | 5.08 us                                                | 4.97 us: 1.02x faster                                                  |
| unpickle             | 14.4 us                                                | 14.9 us: 1.04x slower                                                  |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                                  |
| pickle_dict          | 29.6 us                                                | 34.3 us: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 6.89 ms: 1.16x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.9 ms: 1.50x faster                                                  |
| django_template | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                  |
| genshi_text     | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 51.7 ms: 1.28x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 112 us: 4.86x faster                                                   |
| generators               | 80.1 ms                                                | 29.7 ms: 2.70x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.24 ms: 2.44x faster                                                  |
| async_tree_none          | 728 ms                                                 | 368 ms: 1.98x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 442 ms: 1.97x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 918 ms: 1.93x faster                                                   |
| chaos                    | 115 ms                                                 | 60.2 ms: 1.92x faster                                                  |
| raytrace                 | 507 ms                                                 | 266 ms: 1.91x faster                                                   |
| logging_silent           | 190 ns                                                 | 101 ns: 1.87x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 498 ms: 1.85x faster                                                   |
| richards_super           | 94.7 ms                                                | 52.2 ms: 1.81x faster                                                  |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.79x faster                                                   |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.75x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 67.7 ms: 1.75x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 73.4 ms: 1.74x faster                                                  |
| pylint                   | 551 ms                                                 | 318 ms: 1.74x faster                                                   |
| richards                 | 79.3 ms                                                | 46.3 ms: 1.71x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                  |
| nbody                    | 154 ms                                                 | 90.2 ms: 1.70x faster                                                  |
| go                       | 240 ms                                                 | 141 ms: 1.70x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 609 ms: 1.67x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.29 ms: 1.65x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 299 us: 1.62x faster                                                   |
| spectral_norm            | 170 ms                                                 | 108 ms: 1.57x faster                                                   |
| pyflate                  | 716 ms                                                 | 463 ms: 1.55x faster                                                   |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                                  |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                   |
| float                    | 117 ms                                                 | 76.7 ms: 1.53x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 38.5 us: 1.52x faster                                                  |
| mako                     | 16.3 ms                                                | 10.9 ms: 1.50x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 2.17 sec: 1.45x faster                                                 |
| tornado_http             | 136 ms                                                 | 95.0 ms: 1.44x faster                                                  |
| django_template          | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                  |
| regex_compile            | 188 ms                                                 | 134 ms: 1.40x faster                                                   |
| python_startup           | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.84 sec: 1.40x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.40x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.95 us: 1.40x faster                                                  |
| chameleon                | 9.68 ms                                                | 6.95 ms: 1.39x faster                                                  |
| logging_format           | 9.09 us                                                | 6.54 us: 1.39x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 735 ms: 1.38x faster                                                   |
| deepcopy                 | 479 us                                                 | 352 us: 1.36x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                  |
| html5lib                 | 88.9 ms                                                | 65.7 ms: 1.35x faster                                                  |
| fannkuch                 | 532 ms                                                 | 394 ms: 1.35x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.80 ms: 1.35x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 59.2 ms: 1.34x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                 |
| thrift                   | 1.07 ms                                                | 806 us: 1.33x faster                                                   |
| nqueens                  | 106 ms                                                 | 80.3 ms: 1.32x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 3.17 us: 1.32x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                   |
| 2to3                     | 348 ms                                                 | 267 ms: 1.31x faster                                                   |
| genshi_text              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                  |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.28x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 51.7 ms: 1.28x faster                                                  |
| scimark_fft              | 466 ms                                                 | 366 ms: 1.27x faster                                                   |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 54.7 ms: 1.26x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 67.5 ms: 1.25x faster                                                  |
| aiohttp                  | 1.44 ms                                                | 1.17 ms: 1.23x faster                                                  |
| sympy_expand             | 566 ms                                                 | 462 ms: 1.22x faster                                                   |
| mypy2                    | 894 ms                                                 | 735 ms: 1.22x faster                                                   |
| djangocms                | 38.4 us                                                | 31.7 us: 1.21x faster                                                  |
| dask                     | 441 ms                                                 | 367 ms: 1.20x faster                                                   |
| gunicorn                 | 1.53 ms                                                | 1.28 ms: 1.20x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.76 sec: 1.19x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 831 us: 1.19x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 85.8 ms: 1.16x faster                                                  |
| pathlib                  | 20.5 ms                                                | 18.4 ms: 1.11x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                                 |
| unpack_sequence          | 60.0 ns                                                | 54.5 ns: 1.10x faster                                                  |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                   |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 25.6 ms: 1.08x faster                                                  |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 160 ms: 1.05x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.93 us: 1.03x faster                                                  |
| pickle_list              | 5.08 us                                                | 4.97 us: 1.02x faster                                                  |
| bench_mp_pool            | 24.0 ms                                                | 23.8 ms: 1.01x faster                                                  |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                   |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 569 ms: 1.02x slower                                                   |
| regex_effbot             | 3.63 ms                                                | 3.71 ms: 1.02x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.67 ms: 1.03x slower                                                  |
| unpickle                 | 14.4 us                                                | 14.9 us: 1.04x slower                                                  |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.00 ms: 1.10x slower                                                  |
| pickle_dict              | 29.6 us                                                | 34.3 us: 1.16x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 6.89 ms: 1.16x slower                                                  |
| telco                    | 7.27 ms                                                | 8.45 ms: 1.16x slower                                                  |
| coverage                 | 79.4 ms                                                | 95.5 ms: 1.20x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                           |

Benchmark hidden because not significant (2): unpickle_list, async_generators
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240327-3.13.0a5+-0f9d2fe/bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x


# Memory

- memory change: 1.09x
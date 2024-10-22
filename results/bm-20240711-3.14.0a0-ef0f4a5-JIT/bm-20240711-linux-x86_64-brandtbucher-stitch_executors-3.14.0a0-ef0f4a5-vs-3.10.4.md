# Results vs. 3.10.4

- fork: brandtbucher
- ref: stitch_executors
- machine: linux-x86_64
- commit hash: ef0f4a5
- commit date: 2024-07-11
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 271 ms: 1.29x faster                                                    |
| docutils       | 3.30 sec                                               | 2.85 sec: 1.16x faster                                                  |
| html5lib       | 88.9 ms                                                | 63.0 ms: 1.41x faster                                                   |
| tornado_http   | 136 ms                                                 | 92.5 ms: 1.47x faster                                                   |
| Geometric mean | (ref)                                                  | 1.33x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 323 ms: 2.25x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 406 ms: 2.14x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 836 ms: 2.11x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 561 ms: 1.81x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.07x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.6 ms: 1.93x faster                                                   |
| float          | 117 ms                                                 | 69.8 ms: 1.68x faster                                                   |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.49x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 136 ms: 1.39x faster                                                    |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                   |
| regex_dna      | 227 ms                                                 | 228 ms: 1.00x slower                                                    |
| regex_effbot   | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 295 us: 1.64x faster                                                    |
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 57.6 ms: 1.37x faster                                                   |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 81.0 ms: 1.23x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                    |
| json_loads           | 31.2 us                                                | 27.9 us: 1.12x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.84 ms: 1.66x faster                                                   |
| django_template | 48.2 ms                                                | 35.3 ms: 1.36x faster                                                   |
| genshi_text     | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 58.1 ms: 1.14x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                                    |
| generators               | 80.1 ms                                                | 29.6 ms: 2.71x faster                                                   |
| async_tree_none          | 728 ms                                                 | 323 ms: 2.25x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.55 ms: 2.23x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 406 ms: 2.14x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 836 ms: 2.11x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 28.2 us: 2.07x faster                                                   |
| chaos                    | 115 ms                                                 | 58.2 ms: 1.99x faster                                                   |
| richards_super           | 94.7 ms                                                | 48.7 ms: 1.95x faster                                                   |
| nbody                    | 154 ms                                                 | 79.6 ms: 1.93x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 61.7 ms: 1.92x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 66.8 ms: 1.91x faster                                                   |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                    |
| richards                 | 79.3 ms                                                | 42.6 ms: 1.86x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 504 ms: 1.83x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 561 ms: 1.81x faster                                                    |
| logging_silent           | 190 ns                                                 | 106 ns: 1.78x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                   |
| deepcopy                 | 479 us                                                 | 278 us: 1.72x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.72x faster                                                   |
| float                    | 117 ms                                                 | 69.8 ms: 1.68x faster                                                   |
| mako                     | 16.3 ms                                                | 9.84 ms: 1.66x faster                                                   |
| scimark_sor              | 220 ms                                                 | 132 ms: 1.66x faster                                                    |
| go                       | 240 ms                                                 | 145 ms: 1.66x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 295 us: 1.64x faster                                                    |
| pylint                   | 551 ms                                                 | 336 ms: 1.64x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                  |
| pyflate                  | 716 ms                                                 | 447 ms: 1.60x faster                                                    |
| spectral_norm            | 170 ms                                                 | 106 ms: 1.60x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.52 ms: 1.59x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.48 us: 1.52x faster                                                   |
| scimark_fft              | 466 ms                                                 | 311 ms: 1.50x faster                                                    |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.36 ms: 1.48x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.48x faster                                                   |
| tornado_http             | 136 ms                                                 | 92.5 ms: 1.47x faster                                                   |
| fannkuch                 | 532 ms                                                 | 363 ms: 1.46x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                  |
| scimark_lu               | 176 ms                                                 | 123 ms: 1.43x faster                                                    |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 717 ms: 1.42x faster                                                    |
| html5lib                 | 88.9 ms                                                | 63.0 ms: 1.41x faster                                                   |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                   |
| regex_compile            | 188 ms                                                 | 136 ms: 1.39x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 57.6 ms: 1.37x faster                                                   |
| django_template          | 48.2 ms                                                | 35.3 ms: 1.36x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                   |
| thrift                   | 1.07 ms                                                | 792 us: 1.35x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                    |
| 2to3                     | 348 ms                                                 | 271 ms: 1.29x faster                                                    |
| genshi_text              | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 67.4 ms: 1.25x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 55.4 ms: 1.25x faster                                                   |
| nqueens                  | 106 ms                                                 | 85.7 ms: 1.23x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 81.0 ms: 1.23x faster                                                   |
| dask                     | 441 ms                                                 | 362 ms: 1.22x faster                                                    |
| sympy_sum                | 196 ms                                                 | 165 ms: 1.19x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 832 us: 1.19x faster                                                    |
| sympy_str                | 346 ms                                                 | 293 ms: 1.18x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 21.9 ms: 1.18x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.85 sec: 1.16x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                    |
| sympy_expand             | 566 ms                                                 | 495 ms: 1.14x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 58.1 ms: 1.14x faster                                                   |
| json_loads               | 31.2 us                                                | 27.9 us: 1.12x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                  |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                    |
| json                     | 5.69 ms                                                | 5.16 ms: 1.10x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                   |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                    |
| regex_dna                | 227 ms                                                 | 228 ms: 1.00x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 3.65 ms: 1.01x slower                                                   |
| regex_effbot             | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                   |
| async_generators         | 444 ms                                                 | 464 ms: 1.05x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.08x slower                                                   |
| telco                    | 7.27 ms                                                | 8.06 ms: 1.11x slower                                                   |
| coverage                 | 79.4 ms                                                | 93.2 ms: 1.17x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240711-3.14.0a0-ef0f4a5-JIT/bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.19x
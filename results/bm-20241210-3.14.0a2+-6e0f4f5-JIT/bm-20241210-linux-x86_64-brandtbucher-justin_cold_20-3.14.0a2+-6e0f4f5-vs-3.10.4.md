# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_cold_20
- machine: linux-x86_64
- commit hash: 6e0f4f5
- commit date: 2024-12-10
- overall geometric mean: 1.426x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                   |
| docutils       | 3.30 sec                                               | 2.79 sec: 1.18x faster                                                 |
| html5lib       | 88.9 ms                                                | 64.6 ms: 1.38x faster                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 617 ms: 2.87x faster                                                   |
| async_tree_none         | 728 ms                                                 | 272 ms: 2.68x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 342 ms: 2.54x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 498 ms: 2.04x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.51x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 84.4 ms: 1.82x faster                                                  |
| float          | 117 ms                                                 | 75.3 ms: 1.56x faster                                                  |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.43x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                   |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.46 ms: 1.05x faster                                                  |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 193 us: 1.71x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 324 us: 1.49x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 54.9 ms: 1.44x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 77.7 ms: 1.28x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.23x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 94.7 ms: 1.22x faster                                                  |
| json_loads           | 31.2 us                                                | 26.2 us: 1.19x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.38x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                  |
| django_template | 48.2 ms                                                | 33.6 ms: 1.43x faster                                                  |
| genshi_text     | 31.8 ms                                                | 23.8 ms: 1.34x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 56.9 ms: 1.16x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 617 ms: 2.87x faster                                                   |
| async_tree_none          | 728 ms                                                 | 272 ms: 2.68x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 342 ms: 2.54x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.16 ms: 2.50x faster                                                  |
| generators               | 80.1 ms                                                | 36.7 ms: 2.18x faster                                                  |
| richards_super           | 94.7 ms                                                | 43.4 ms: 2.18x faster                                                  |
| richards                 | 79.3 ms                                                | 37.5 ms: 2.12x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 498 ms: 2.04x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 2.00x faster                                                  |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.93x faster                                                  |
| logging_silent           | 190 ns                                                 | 99.9 ns: 1.90x faster                                                  |
| pylint                   | 551 ms                                                 | 295 ms: 1.87x faster                                                   |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 64.6 ms: 1.83x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 70.2 ms: 1.82x faster                                                  |
| nbody                    | 154 ms                                                 | 84.4 ms: 1.82x faster                                                  |
| go                       | 240 ms                                                 | 134 ms: 1.79x faster                                                   |
| raytrace                 | 507 ms                                                 | 286 ms: 1.77x faster                                                   |
| deepcopy                 | 479 us                                                 | 276 us: 1.74x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 193 us: 1.71x faster                                                   |
| djangocms                | 38.4 us                                                | 22.6 us: 1.70x faster                                                  |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.68x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                 |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                  |
| pyflate                  | 716 ms                                                 | 452 ms: 1.59x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                                  |
| float                    | 117 ms                                                 | 75.3 ms: 1.56x faster                                                  |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                   |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                                  |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.51x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 324 us: 1.49x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.96 ms: 1.49x faster                                                  |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.73 us: 1.45x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 54.9 ms: 1.44x faster                                                  |
| logging_format           | 9.09 us                                                | 6.32 us: 1.44x faster                                                  |
| django_template          | 48.2 ms                                                | 33.6 ms: 1.43x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                 |
| scimark_fft              | 466 ms                                                 | 328 ms: 1.42x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 718 ms: 1.42x faster                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                 |
| thrift                   | 1.07 ms                                                | 775 us: 1.38x faster                                                   |
| fannkuch                 | 532 ms                                                 | 385 ms: 1.38x faster                                                   |
| html5lib                 | 88.9 ms                                                | 64.6 ms: 1.38x faster                                                  |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                   |
| genshi_text              | 31.8 ms                                                | 23.8 ms: 1.34x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.33x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.91 ms: 1.32x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.29x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 77.7 ms: 1.28x faster                                                  |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 20.7 ms: 1.25x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 67.8 ms: 1.24x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 55.6 ms: 1.24x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.23x faster                                                   |
| sympy_str                | 346 ms                                                 | 283 ms: 1.22x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 94.7 ms: 1.22x faster                                                  |
| json_loads               | 31.2 us                                                | 26.2 us: 1.19x faster                                                  |
| json                     | 5.69 ms                                                | 4.80 ms: 1.19x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.79 sec: 1.18x faster                                                 |
| nqueens                  | 106 ms                                                 | 90.0 ms: 1.18x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 56.9 ms: 1.16x faster                                                  |
| sympy_expand             | 566 ms                                                 | 490 ms: 1.15x faster                                                   |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                  |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 881 us: 1.12x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.82 us: 1.07x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.71 sec: 1.05x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.46 ms: 1.05x faster                                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| async_generators         | 444 ms                                                 | 446 ms: 1.00x slower                                                   |
| telco                    | 7.27 ms                                                | 7.52 ms: 1.03x slower                                                  |
| coverage                 | 79.4 ms                                                | 83.7 ms: 1.05x slower                                                  |
| mypy2                    | 894 ms                                                 | 991 ms: 1.11x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.78 ms: 1.32x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                           |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241210-3.14.0a2+-6e0f4f5-JIT/bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.426x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.29x
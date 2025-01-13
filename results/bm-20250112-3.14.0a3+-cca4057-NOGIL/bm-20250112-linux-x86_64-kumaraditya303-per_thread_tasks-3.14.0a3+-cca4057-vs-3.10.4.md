# Results vs. 3.10.4

- fork: kumaraditya303
- ref: per_thread_tasks
- machine: linux-x86_64
- commit hash: cca4057
- commit date: 2025-01-12
- overall geometric mean: 1.136x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.50x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 340 ms: 1.02x faster                                                       |
| docutils       | 3.30 sec                                               | 2.98 sec: 1.11x faster                                                     |
| html5lib       | 88.9 ms                                                | 85.1 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 733 ms: 2.41x faster                                                       |
| async_tree_none         | 728 ms                                                 | 344 ms: 2.12x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 436 ms: 2.00x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 583 ms: 1.74x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 105 ms: 1.12x faster                                                       |
| nbody          | 154 ms                                                 | 140 ms: 1.10x faster                                                       |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 162 ms: 1.16x faster                                                       |
| regex_v8       | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.46 ms: 1.05x faster                                                      |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.36 sec: 1.33x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 96.0 ms: 1.20x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 73.2 ms: 1.08x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 310 us: 1.07x faster                                                       |
| json_dumps           | 14.2 ms                                                | 13.3 ms: 1.06x faster                                                      |
| json_loads           | 31.2 us                                                | 29.6 us: 1.05x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 96.9 ms: 1.03x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 472 us: 1.03x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 15.5 ms: 1.06x slower                                                      |
| python_startup_no_site | 5.93 ms                                                | 9.62 ms: 1.62x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.31x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 30.2 ms: 1.06x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 62.7 ms: 1.05x faster                                                      |
| django_template | 48.2 ms                                                | 45.9 ms: 1.05x faster                                                      |
| mako            | 16.3 ms                                                | 18.2 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 207 us: 2.63x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 733 ms: 2.41x faster                                                       |
| generators               | 80.1 ms                                                | 36.7 ms: 2.18x faster                                                      |
| async_tree_none          | 728 ms                                                 | 344 ms: 2.12x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 436 ms: 2.00x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 583 ms: 1.74x faster                                                       |
| pylint                   | 551 ms                                                 | 339 ms: 1.63x faster                                                       |
| deepcopy                 | 479 us                                                 | 315 us: 1.52x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 40.4 us: 1.45x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 91.3 ms: 1.40x faster                                                      |
| spectral_norm            | 170 ms                                                 | 123 ms: 1.39x faster                                                       |
| coroutines               | 35.1 ms                                                | 25.5 ms: 1.38x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 2.36 sec: 1.33x faster                                                     |
| richards_super           | 94.7 ms                                                | 72.4 ms: 1.31x faster                                                      |
| richards                 | 79.3 ms                                                | 62.5 ms: 1.27x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 3.32 us: 1.26x faster                                                      |
| chaos                    | 115 ms                                                 | 92.4 ms: 1.25x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 96.0 ms: 1.20x faster                                                      |
| scimark_sor              | 220 ms                                                 | 183 ms: 1.20x faster                                                       |
| pathlib                  | 20.5 ms                                                | 17.1 ms: 1.20x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.35 sec: 1.17x faster                                                     |
| regex_compile            | 188 ms                                                 | 162 ms: 1.16x faster                                                       |
| pyflate                  | 716 ms                                                 | 621 ms: 1.15x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 103 ms: 1.15x faster                                                       |
| hexiom                   | 10.4 ms                                                | 9.07 ms: 1.15x faster                                                      |
| deltablue                | 7.91 ms                                                | 6.93 ms: 1.14x faster                                                      |
| comprehensions           | 28.8 us                                                | 25.3 us: 1.14x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                       |
| dulwich_log              | 84.3 ms                                                | 74.8 ms: 1.13x faster                                                      |
| go                       | 240 ms                                                 | 214 ms: 1.12x faster                                                       |
| float                    | 117 ms                                                 | 105 ms: 1.12x faster                                                       |
| scimark_lu               | 176 ms                                                 | 157 ms: 1.12x faster                                                       |
| scimark_fft              | 466 ms                                                 | 418 ms: 1.12x faster                                                       |
| docutils                 | 3.30 sec                                               | 2.98 sec: 1.11x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 130 ms: 1.10x faster                                                       |
| nbody                    | 154 ms                                                 | 140 ms: 1.10x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 73.2 ms: 1.08x faster                                                      |
| raytrace                 | 507 ms                                                 | 470 ms: 1.08x faster                                                       |
| sympy_sum                | 196 ms                                                 | 182 ms: 1.08x faster                                                       |
| nqueens                  | 106 ms                                                 | 98.3 ms: 1.08x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.02 ms: 1.08x faster                                                      |
| json                     | 5.69 ms                                                | 5.30 ms: 1.07x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 310 us: 1.07x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 955 ms: 1.07x faster                                                       |
| json_dumps               | 14.2 ms                                                | 13.3 ms: 1.06x faster                                                      |
| logging_simple           | 8.30 us                                                | 7.81 us: 1.06x faster                                                      |
| logging_silent           | 190 ns                                                 | 179 ns: 1.06x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.98 sec: 1.06x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 65.2 ms: 1.06x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 24.4 ms: 1.06x faster                                                      |
| genshi_text              | 31.8 ms                                                | 30.2 ms: 1.06x faster                                                      |
| json_loads               | 31.2 us                                                | 29.6 us: 1.05x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 62.7 ms: 1.05x faster                                                      |
| thrift                   | 1.07 ms                                                | 1.02 ms: 1.05x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.46 ms: 1.05x faster                                                      |
| django_template          | 48.2 ms                                                | 45.9 ms: 1.05x faster                                                      |
| fannkuch                 | 532 ms                                                 | 507 ms: 1.05x faster                                                       |
| html5lib                 | 88.9 ms                                                | 85.1 ms: 1.04x faster                                                      |
| logging_format           | 9.09 us                                                | 8.71 us: 1.04x faster                                                      |
| sympy_str                | 346 ms                                                 | 333 ms: 1.04x faster                                                       |
| sympy_expand             | 566 ms                                                 | 552 ms: 1.03x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 96.9 ms: 1.03x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 472 us: 1.03x faster                                                       |
| 2to3                     | 348 ms                                                 | 340 ms: 1.02x faster                                                       |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                       |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 2.19 ms: 1.01x slower                                                      |
| mdp                      | 2.85 sec                                               | 2.93 sec: 1.03x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 3.77 ms: 1.04x slower                                                      |
| sqlalchemy_declarative   | 172 ms                                                 | 180 ms: 1.05x slower                                                       |
| python_startup           | 14.6 ms                                                | 15.5 ms: 1.06x slower                                                      |
| meteor_contest           | 120 ms                                                 | 130 ms: 1.08x slower                                                       |
| async_generators         | 444 ms                                                 | 486 ms: 1.09x slower                                                       |
| mako                     | 16.3 ms                                                | 18.2 ms: 1.12x slower                                                      |
| telco                    | 7.27 ms                                                | 9.18 ms: 1.26x slower                                                      |
| coverage                 | 79.4 ms                                                | 103 ms: 1.30x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 2.35 ms: 1.45x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 9.62 ms: 1.62x slower                                                      |
| bench_thread_pool        | 986 us                                                 | 3.55 ms: 3.60x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 95.3 ms: 3.97x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.10x faster                                                               |

Benchmark hidden because not significant (2): sqlglot_transpile, sqlalchemy_imperative
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250112-3.14.0a3+-cca4057-NOGIL/bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.136x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.50x
# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_cold_18
- machine: linux-x86_64
- commit hash: 1cd9228
- commit date: 2024-12-04
- overall geometric mean: 1.432x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                   |
| docutils       | 3.30 sec                                               | 2.72 sec: 1.21x faster                                                 |
| html5lib       | 88.9 ms                                                | 65.2 ms: 1.36x faster                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 626 ms: 2.82x faster                                                   |
| async_tree_none         | 728 ms                                                 | 271 ms: 2.69x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 341 ms: 2.55x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.51x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.3 ms: 1.89x faster                                                  |
| float          | 117 ms                                                 | 75.5 ms: 1.55x faster                                                  |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.44x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                   |
| regex_v8       | 27.8 ms                                                | 24.9 ms: 1.11x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.26 ms: 1.11x faster                                                  |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 197 us: 1.68x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.62x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.52x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 55.2 ms: 1.43x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 78.0 ms: 1.28x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.23x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 95.0 ms: 1.22x faster                                                  |
| json_loads           | 31.2 us                                                | 26.2 us: 1.19x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                  |
| django_template | 48.2 ms                                                | 34.0 ms: 1.42x faster                                                  |
| genshi_text     | 31.8 ms                                                | 24.2 ms: 1.31x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 56.7 ms: 1.16x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 626 ms: 2.82x faster                                                   |
| async_tree_none          | 728 ms                                                 | 271 ms: 2.69x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 341 ms: 2.55x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.18 ms: 2.49x faster                                                  |
| richards_super           | 94.7 ms                                                | 43.1 ms: 2.20x faster                                                  |
| generators               | 80.1 ms                                                | 36.6 ms: 2.19x faster                                                  |
| richards                 | 79.3 ms                                                | 36.6 ms: 2.17x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 1.99x faster                                                  |
| chaos                    | 115 ms                                                 | 59.9 ms: 1.93x faster                                                  |
| nbody                    | 154 ms                                                 | 81.3 ms: 1.89x faster                                                  |
| pylint                   | 551 ms                                                 | 294 ms: 1.88x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 68.4 ms: 1.87x faster                                                  |
| logging_silent           | 190 ns                                                 | 103 ns: 1.85x faster                                                   |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 64.9 ms: 1.82x faster                                                  |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                                   |
| go                       | 240 ms                                                 | 135 ms: 1.78x faster                                                   |
| raytrace                 | 507 ms                                                 | 288 ms: 1.76x faster                                                   |
| djangocms                | 38.4 us                                                | 22.3 us: 1.72x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 197 us: 1.68x faster                                                   |
| comprehensions           | 28.8 us                                                | 17.4 us: 1.66x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.62x faster                                                 |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                  |
| pyflate                  | 716 ms                                                 | 450 ms: 1.59x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                  |
| float                    | 117 ms                                                 | 75.5 ms: 1.55x faster                                                  |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.52x faster                                                   |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                                   |
| hexiom                   | 10.4 ms                                                | 7.04 ms: 1.48x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.47x faster                                                  |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                   |
| logging_format           | 9.09 us                                                | 6.26 us: 1.45x faster                                                  |
| scimark_fft              | 466 ms                                                 | 321 ms: 1.45x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.72 us: 1.45x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 55.2 ms: 1.43x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 711 ms: 1.43x faster                                                   |
| django_template          | 48.2 ms                                                | 34.0 ms: 1.42x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.39x faster                                                  |
| fannkuch                 | 532 ms                                                 | 384 ms: 1.38x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.72 ms: 1.37x faster                                                  |
| html5lib                 | 88.9 ms                                                | 65.2 ms: 1.36x faster                                                  |
| thrift                   | 1.07 ms                                                | 791 us: 1.35x faster                                                   |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                                 |
| genshi_text              | 31.8 ms                                                | 24.2 ms: 1.31x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 78.0 ms: 1.28x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                  |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 67.7 ms: 1.25x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 20.7 ms: 1.24x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 55.6 ms: 1.24x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.23x faster                                                   |
| sympy_str                | 346 ms                                                 | 284 ms: 1.22x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 95.0 ms: 1.22x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.72 sec: 1.21x faster                                                 |
| json                     | 5.69 ms                                                | 4.76 ms: 1.20x faster                                                  |
| json_loads               | 31.2 us                                                | 26.2 us: 1.19x faster                                                  |
| nqueens                  | 106 ms                                                 | 90.6 ms: 1.17x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 56.7 ms: 1.16x faster                                                  |
| sympy_expand             | 566 ms                                                 | 490 ms: 1.15x faster                                                   |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 874 us: 1.13x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 24.9 ms: 1.11x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.26 ms: 1.11x faster                                                  |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.70 sec: 1.05x faster                                                 |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                                   |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| async_generators         | 444 ms                                                 | 456 ms: 1.03x slower                                                   |
| telco                    | 7.27 ms                                                | 7.63 ms: 1.05x slower                                                  |
| coverage                 | 79.4 ms                                                | 84.3 ms: 1.06x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.96 ms: 1.37x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.53x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 81.5 ms: 3.39x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                           |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241204-3.14.0a2+-1cd9228-JIT/bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.432x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.28x
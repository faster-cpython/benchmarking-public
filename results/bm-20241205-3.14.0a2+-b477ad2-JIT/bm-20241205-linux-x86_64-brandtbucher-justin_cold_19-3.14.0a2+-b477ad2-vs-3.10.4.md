# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_cold_19
- machine: linux-x86_64
- commit hash: b477ad2
- commit date: 2024-12-05
- overall geometric mean: 1.433x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.35x faster                                                   |
| docutils       | 3.30 sec                                               | 2.78 sec: 1.19x faster                                                 |
| html5lib       | 88.9 ms                                                | 64.2 ms: 1.38x faster                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 621 ms: 2.85x faster                                                   |
| async_tree_none         | 728 ms                                                 | 269 ms: 2.70x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 342 ms: 2.54x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 494 ms: 2.06x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.52x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.0 ms: 1.78x faster                                                  |
| float          | 117 ms                                                 | 75.8 ms: 1.54x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.41x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.25 ms: 1.12x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.9 ms: 1.11x faster                                                  |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 195 us: 1.70x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 54.7 ms: 1.45x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.28x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 78.5 ms: 1.27x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.22x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 94.5 ms: 1.22x faster                                                  |
| json_loads           | 31.2 us                                                | 26.0 us: 1.20x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.38x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.98 ms: 1.64x faster                                                  |
| django_template | 48.2 ms                                                | 33.9 ms: 1.42x faster                                                  |
| genshi_text     | 31.8 ms                                                | 24.1 ms: 1.32x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 57.1 ms: 1.16x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.19x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 621 ms: 2.85x faster                                                   |
| async_tree_none          | 728 ms                                                 | 269 ms: 2.70x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 342 ms: 2.54x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.20 ms: 2.48x faster                                                  |
| generators               | 80.1 ms                                                | 36.4 ms: 2.20x faster                                                  |
| richards_super           | 94.7 ms                                                | 43.1 ms: 2.20x faster                                                  |
| richards                 | 79.3 ms                                                | 36.6 ms: 2.17x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 494 ms: 2.06x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 29.1 us: 2.01x faster                                                  |
| chaos                    | 115 ms                                                 | 60.1 ms: 1.92x faster                                                  |
| pylint                   | 551 ms                                                 | 294 ms: 1.87x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 68.5 ms: 1.87x faster                                                  |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 64.2 ms: 1.84x faster                                                  |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                   |
| go                       | 240 ms                                                 | 134 ms: 1.80x faster                                                   |
| deepcopy                 | 479 us                                                 | 268 us: 1.79x faster                                                   |
| nbody                    | 154 ms                                                 | 86.0 ms: 1.78x faster                                                  |
| raytrace                 | 507 ms                                                 | 287 ms: 1.76x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 195 us: 1.70x faster                                                   |
| djangocms                | 38.4 us                                                | 22.8 us: 1.68x faster                                                  |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.67x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.65x faster                                                  |
| mako                     | 16.3 ms                                                | 9.98 ms: 1.64x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                 |
| pyflate                  | 716 ms                                                 | 445 ms: 1.61x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                  |
| float                    | 117 ms                                                 | 75.8 ms: 1.54x faster                                                  |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                   |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                                   |
| hexiom                   | 10.4 ms                                                | 7.04 ms: 1.48x faster                                                  |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.73 us: 1.45x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 54.7 ms: 1.45x faster                                                  |
| logging_format           | 9.09 us                                                | 6.34 us: 1.43x faster                                                  |
| scimark_fft              | 466 ms                                                 | 325 ms: 1.43x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                 |
| django_template          | 48.2 ms                                                | 33.9 ms: 1.42x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 717 ms: 1.42x faster                                                   |
| fannkuch                 | 532 ms                                                 | 381 ms: 1.39x faster                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                  |
| html5lib                 | 88.9 ms                                                | 64.2 ms: 1.38x faster                                                  |
| thrift                   | 1.07 ms                                                | 782 us: 1.37x faster                                                   |
| 2to3                     | 348 ms                                                 | 259 ms: 1.35x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                   |
| genshi_text              | 31.8 ms                                                | 24.1 ms: 1.32x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.01 ms: 1.29x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.28x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 78.5 ms: 1.27x faster                                                  |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 67.6 ms: 1.25x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 55.6 ms: 1.25x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 20.7 ms: 1.24x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.22x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 94.5 ms: 1.22x faster                                                  |
| sympy_str                | 346 ms                                                 | 283 ms: 1.22x faster                                                   |
| json                     | 5.69 ms                                                | 4.74 ms: 1.20x faster                                                  |
| json_loads               | 31.2 us                                                | 26.0 us: 1.20x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.78 sec: 1.19x faster                                                 |
| nqueens                  | 106 ms                                                 | 90.3 ms: 1.17x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 57.1 ms: 1.16x faster                                                  |
| sympy_expand             | 566 ms                                                 | 490 ms: 1.16x faster                                                   |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 875 us: 1.13x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.25 ms: 1.12x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.9 ms: 1.11x faster                                                  |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.82 us: 1.07x faster                                                  |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.74 sec: 1.04x faster                                                 |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                   |
| async_generators         | 444 ms                                                 | 452 ms: 1.02x slower                                                   |
| telco                    | 7.27 ms                                                | 7.51 ms: 1.03x slower                                                  |
| coverage                 | 79.4 ms                                                | 84.5 ms: 1.06x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.74 ms: 1.31x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.44 ms: 1.50x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 81.3 ms: 3.38x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                           |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241205-3.14.0a2+-b477ad2-JIT/bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.433x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.28x
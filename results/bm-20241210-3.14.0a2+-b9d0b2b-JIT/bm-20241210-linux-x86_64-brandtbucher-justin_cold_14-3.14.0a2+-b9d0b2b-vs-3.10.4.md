# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_cold_14
- machine: linux-x86_64
- commit hash: b9d0b2b
- commit date: 2024-12-10
- overall geometric mean: 1.422x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.34x faster                                                   |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                 |
| html5lib       | 88.9 ms                                                | 64.9 ms: 1.37x faster                                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 625 ms: 2.83x faster                                                   |
| async_tree_none         | 728 ms                                                 | 271 ms: 2.68x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 342 ms: 2.54x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 497 ms: 2.04x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.51x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.0 ms: 1.90x faster                                                  |
| float          | 117 ms                                                 | 76.1 ms: 1.54x faster                                                  |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.44x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.44x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.26 ms: 1.11x faster                                                  |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                  |
| regex_dna      | 227 ms                                                 | 215 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 196 us: 1.69x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.62x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.51x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 57.1 ms: 1.38x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.28x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 80.2 ms: 1.24x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.23x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 95.4 ms: 1.21x faster                                                  |
| json_loads           | 31.2 us                                                | 26.1 us: 1.20x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                  |
| django_template | 48.2 ms                                                | 34.4 ms: 1.40x faster                                                  |
| genshi_text     | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 58.8 ms: 1.12x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.16x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 625 ms: 2.83x faster                                                   |
| async_tree_none          | 728 ms                                                 | 271 ms: 2.68x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 342 ms: 2.54x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.18 ms: 2.49x faster                                                  |
| generators               | 80.1 ms                                                | 36.5 ms: 2.19x faster                                                  |
| richards_super           | 94.7 ms                                                | 45.0 ms: 2.11x faster                                                  |
| richards                 | 79.3 ms                                                | 38.2 ms: 2.08x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 497 ms: 2.04x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 2.00x faster                                                  |
| pylint                   | 551 ms                                                 | 284 ms: 1.94x faster                                                   |
| chaos                    | 115 ms                                                 | 59.4 ms: 1.94x faster                                                  |
| nbody                    | 154 ms                                                 | 81.0 ms: 1.90x faster                                                  |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 69.0 ms: 1.85x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 64.1 ms: 1.84x faster                                                  |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                   |
| go                       | 240 ms                                                 | 134 ms: 1.79x faster                                                   |
| raytrace                 | 507 ms                                                 | 287 ms: 1.77x faster                                                   |
| deepcopy                 | 479 us                                                 | 274 us: 1.75x faster                                                   |
| djangocms                | 38.4 us                                                | 22.2 us: 1.73x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 196 us: 1.69x faster                                                   |
| comprehensions           | 28.8 us                                                | 17.4 us: 1.65x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.64x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.62x faster                                                 |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                  |
| pyflate                  | 716 ms                                                 | 453 ms: 1.58x faster                                                   |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.58x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                                  |
| float                    | 117 ms                                                 | 76.1 ms: 1.54x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.51x faster                                                   |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.47x faster                                                   |
| hexiom                   | 10.4 ms                                                | 7.10 ms: 1.46x faster                                                  |
| scimark_fft              | 466 ms                                                 | 322 ms: 1.45x faster                                                   |
| regex_compile            | 188 ms                                                 | 130 ms: 1.44x faster                                                   |
| logging_format           | 9.09 us                                                | 6.33 us: 1.44x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.83 us: 1.42x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 721 ms: 1.41x faster                                                   |
| django_template          | 48.2 ms                                                | 34.4 ms: 1.40x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 57.1 ms: 1.38x faster                                                  |
| html5lib                 | 88.9 ms                                                | 64.9 ms: 1.37x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.76 ms: 1.36x faster                                                  |
| thrift                   | 1.07 ms                                                | 797 us: 1.35x faster                                                   |
| 2to3                     | 348 ms                                                 | 259 ms: 1.34x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                                 |
| fannkuch                 | 532 ms                                                 | 402 ms: 1.32x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.28x faster                                                  |
| sympy_sum                | 196 ms                                                 | 154 ms: 1.28x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                  |
| genshi_text              | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 20.5 ms: 1.26x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 55.2 ms: 1.25x faster                                                  |
| sympy_str                | 346 ms                                                 | 277 ms: 1.25x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 80.2 ms: 1.24x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 68.3 ms: 1.23x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.23x faster                                                   |
| sympy_expand             | 566 ms                                                 | 465 ms: 1.22x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 95.4 ms: 1.21x faster                                                  |
| json                     | 5.69 ms                                                | 4.74 ms: 1.20x faster                                                  |
| json_loads               | 31.2 us                                                | 26.1 us: 1.20x faster                                                  |
| nqueens                  | 106 ms                                                 | 91.5 ms: 1.16x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 58.8 ms: 1.12x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 880 us: 1.12x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.26 ms: 1.11x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                  |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                  |
| regex_dna                | 227 ms                                                 | 215 ms: 1.06x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.78 sec: 1.02x faster                                                 |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                   |
| async_generators         | 444 ms                                                 | 454 ms: 1.02x slower                                                   |
| telco                    | 7.27 ms                                                | 7.56 ms: 1.04x slower                                                  |
| coverage                 | 79.4 ms                                                | 83.8 ms: 1.05x slower                                                  |
| mypy2                    | 894 ms                                                 | 959 ms: 1.07x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.87 ms: 1.34x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 82.0 ms: 3.41x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                           |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241210-3.14.0a2+-b9d0b2b-JIT/bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.422x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.29x
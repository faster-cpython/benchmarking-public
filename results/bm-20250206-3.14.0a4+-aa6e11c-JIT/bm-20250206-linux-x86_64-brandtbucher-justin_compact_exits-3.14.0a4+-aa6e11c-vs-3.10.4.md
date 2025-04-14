# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: aa6e11c
- commit date: 2025-02-06
- overall geometric mean: 1.445x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                                         |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.22x faster                                                       |
| html5lib       | 88.9 ms                                                | 63.5 ms: 1.40x faster                                                        |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 620 ms: 2.85x faster                                                         |
| async_tree_none         | 728 ms                                                 | 268 ms: 2.72x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 325 ms: 2.67x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 494 ms: 2.06x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.55x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 66.9 ms: 1.75x faster                                                        |
| nbody          | 154 ms                                                 | 94.6 ms: 1.62x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.43x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                         |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                        |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 194 us: 1.70x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 54.7 ms: 1.45x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 77.5 ms: 1.28x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.23x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 95.2 ms: 1.21x faster                                                        |
| json_loads           | 31.2 us                                                | 29.0 us: 1.08x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.37x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.14x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.01 ms: 1.18x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                        |
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                        |
| genshi_text     | 31.8 ms                                                | 23.0 ms: 1.39x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 55.1 ms: 1.20x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.31x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 620 ms: 2.85x faster                                                         |
| async_tree_none          | 728 ms                                                 | 268 ms: 2.72x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 325 ms: 2.67x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.49 ms: 2.27x faster                                                        |
| generators               | 80.1 ms                                                | 36.4 ms: 2.20x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 494 ms: 2.06x faster                                                         |
| richards_super           | 94.7 ms                                                | 47.2 ms: 2.01x faster                                                        |
| chaos                    | 115 ms                                                 | 59.4 ms: 1.94x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 30.3 us: 1.93x faster                                                        |
| pylint                   | 551 ms                                                 | 286 ms: 1.93x faster                                                         |
| richards                 | 79.3 ms                                                | 41.2 ms: 1.92x faster                                                        |
| scimark_sor              | 220 ms                                                 | 114 ms: 1.92x faster                                                         |
| go                       | 240 ms                                                 | 126 ms: 1.91x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 63.5 ms: 1.86x faster                                                        |
| deepcopy                 | 479 us                                                 | 265 us: 1.81x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 71.3 ms: 1.79x faster                                                        |
| spectral_norm            | 170 ms                                                 | 95.4 ms: 1.78x faster                                                        |
| raytrace                 | 507 ms                                                 | 287 ms: 1.77x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                       |
| float                    | 117 ms                                                 | 66.9 ms: 1.75x faster                                                        |
| logging_silent           | 190 ns                                                 | 109 ns: 1.73x faster                                                         |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.73x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 194 us: 1.70x faster                                                         |
| pyflate                  | 716 ms                                                 | 438 ms: 1.64x faster                                                         |
| mako                     | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                        |
| nbody                    | 154 ms                                                 | 94.6 ms: 1.62x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                                         |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.51x faster                                                         |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                         |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                        |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                         |
| logging_format           | 9.09 us                                                | 6.21 us: 1.46x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.71 us: 1.45x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 54.7 ms: 1.45x faster                                                        |
| hexiom                   | 10.4 ms                                                | 7.22 ms: 1.44x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.54 ms: 1.43x faster                                                        |
| thrift                   | 1.07 ms                                                | 758 us: 1.41x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                       |
| html5lib                 | 88.9 ms                                                | 63.5 ms: 1.40x faster                                                        |
| fannkuch                 | 532 ms                                                 | 382 ms: 1.39x faster                                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                        |
| genshi_text              | 31.8 ms                                                | 23.0 ms: 1.39x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 737 ms: 1.38x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                         |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 53.5 ms: 1.29x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 77.5 ms: 1.28x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                        |
| sympy_sum                | 196 ms                                                 | 154 ms: 1.28x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 66.7 ms: 1.27x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 20.5 ms: 1.26x faster                                                        |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                        |
| sympy_str                | 346 ms                                                 | 280 ms: 1.23x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.23x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.22x faster                                                       |
| nqueens                  | 106 ms                                                 | 87.1 ms: 1.22x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 95.2 ms: 1.21x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 55.1 ms: 1.20x faster                                                        |
| sympy_expand             | 566 ms                                                 | 476 ms: 1.19x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                        |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.14x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.72 us: 1.11x faster                                                        |
| json                     | 5.69 ms                                                | 5.12 ms: 1.11x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 893 us: 1.10x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                        |
| async_generators         | 444 ms                                                 | 408 ms: 1.09x faster                                                         |
| json_loads               | 31.2 us                                                | 29.0 us: 1.08x faster                                                        |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                         |
| meteor_contest           | 120 ms                                                 | 113 ms: 1.06x faster                                                         |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                         |
| telco                    | 7.27 ms                                                | 7.65 ms: 1.05x slower                                                        |
| coverage                 | 79.4 ms                                                | 89.3 ms: 1.12x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.01 ms: 1.18x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.61 ms: 1.27x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 80.3 ms: 3.34x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250206-3.14.0a4+-aa6e11c-JIT/bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.445x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.28x
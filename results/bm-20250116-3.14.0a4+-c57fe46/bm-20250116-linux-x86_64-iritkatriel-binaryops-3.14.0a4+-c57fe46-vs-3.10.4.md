# Results vs. 3.10.4

- fork: iritkatriel
- ref: binaryops
- machine: linux-x86_64
- commit hash: c57fe46
- commit date: 2025-01-16
- overall geometric mean: 1.442x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                             |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                           |
| html5lib       | 88.9 ms                                                | 61.7 ms: 1.44x faster                                            |
| Geometric mean | (ref)                                                  | 1.36x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 606 ms: 2.92x faster                                             |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.80x faster                                             |
| async_tree_memoization  | 870 ms                                                 | 328 ms: 2.65x faster                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                             |
| Geometric mean          | (ref)                                                  | 2.58x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 117 ms                                                 | 72.0 ms: 1.63x faster                                            |
| nbody          | 154 ms                                                 | 95.2 ms: 1.61x faster                                            |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.39x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                             |
| regex_effbot   | 3.63 ms                                                | 3.29 ms: 1.10x faster                                            |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                            |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                             |
| Geometric mean | (ref)                                                  | 1.16x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.59x faster                                           |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                             |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.51x faster                                             |
| xml_etree_process    | 79.1 ms                                                | 60.6 ms: 1.31x faster                                            |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                             |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.20x faster                                            |
| xml_etree_iterparse  | 115 ms                                                 | 97.3 ms: 1.19x faster                                            |
| xml_etree_generate   | 99.4 ms                                                | 85.3 ms: 1.16x faster                                            |
| json_loads           | 31.2 us                                                | 29.4 us: 1.06x faster                                            |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                            |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                            |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                            |
| genshi_text     | 31.8 ms                                                | 21.7 ms: 1.47x faster                                            |
| mako            | 16.3 ms                                                | 11.8 ms: 1.39x faster                                            |
| genshi_xml      | 66.0 ms                                                | 48.2 ms: 1.37x faster                                            |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                             |
| async_tree_io            | 1.77 sec                                               | 606 ms: 2.92x faster                                             |
| generators               | 80.1 ms                                                | 27.5 ms: 2.91x faster                                            |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.80x faster                                             |
| async_tree_memoization   | 870 ms                                                 | 328 ms: 2.65x faster                                             |
| deltablue                | 7.91 ms                                                | 3.25 ms: 2.44x faster                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                             |
| go                       | 240 ms                                                 | 118 ms: 2.03x faster                                             |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                             |
| chaos                    | 115 ms                                                 | 58.1 ms: 1.99x faster                                            |
| deepcopy_memo            | 58.5 us                                                | 31.3 us: 1.87x faster                                            |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                             |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                             |
| richards_super           | 94.7 ms                                                | 51.2 ms: 1.85x faster                                            |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                             |
| richards                 | 79.3 ms                                                | 44.6 ms: 1.78x faster                                            |
| spectral_norm            | 170 ms                                                 | 96.0 ms: 1.77x faster                                            |
| scimark_monte_carlo      | 118 ms                                                 | 67.1 ms: 1.76x faster                                            |
| crypto_pyaes             | 128 ms                                                 | 74.0 ms: 1.73x faster                                            |
| logging_silent           | 190 ns                                                 | 111 ns: 1.71x faster                                             |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                            |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                            |
| hexiom                   | 10.4 ms                                                | 6.24 ms: 1.67x faster                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                            |
| float                    | 117 ms                                                 | 72.0 ms: 1.63x faster                                            |
| nbody                    | 154 ms                                                 | 95.2 ms: 1.61x faster                                            |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.59x faster                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                            |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                             |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                             |
| logging_simple           | 8.30 us                                                | 5.45 us: 1.52x faster                                            |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.51x faster                                             |
| pyflate                  | 716 ms                                                 | 474 ms: 1.51x faster                                             |
| logging_format           | 9.09 us                                                | 6.03 us: 1.51x faster                                            |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                            |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                            |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                             |
| genshi_text              | 31.8 ms                                                | 21.7 ms: 1.47x faster                                            |
| html5lib                 | 88.9 ms                                                | 61.7 ms: 1.44x faster                                            |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.5 ms: 1.41x faster                                            |
| thrift                   | 1.07 ms                                                | 759 us: 1.41x faster                                             |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.41x faster                                           |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                           |
| pprint_safe_repr         | 1.02 sec                                               | 731 ms: 1.39x faster                                             |
| mako                     | 16.3 ms                                                | 11.8 ms: 1.39x faster                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.71 ms: 1.37x faster                                            |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                             |
| genshi_xml               | 66.0 ms                                                | 48.2 ms: 1.37x faster                                            |
| scimark_fft              | 466 ms                                                 | 343 ms: 1.36x faster                                             |
| sqlglot_normalize        | 143 ms                                                 | 105 ms: 1.36x faster                                             |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                             |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                             |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                             |
| dulwich_log              | 84.3 ms                                                | 64.2 ms: 1.31x faster                                            |
| nqueens                  | 106 ms                                                 | 80.6 ms: 1.31x faster                                            |
| sqlglot_optimize         | 69.2 ms                                                | 52.8 ms: 1.31x faster                                            |
| xml_etree_process        | 79.1 ms                                                | 60.6 ms: 1.31x faster                                            |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                            |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                             |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                           |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                            |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                             |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                             |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.20x faster                                            |
| xml_etree_iterparse      | 115 ms                                                 | 97.3 ms: 1.19x faster                                            |
| xml_etree_generate       | 99.4 ms                                                | 85.3 ms: 1.16x faster                                            |
| async_generators         | 444 ms                                                 | 384 ms: 1.15x faster                                             |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                           |
| bench_thread_pool        | 986 us                                                 | 867 us: 1.14x faster                                             |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                            |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                             |
| regex_effbot             | 3.63 ms                                                | 3.29 ms: 1.10x faster                                            |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                            |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                            |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                            |
| json_loads               | 31.2 us                                                | 29.4 us: 1.06x faster                                            |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                             |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                             |
| telco                    | 7.27 ms                                                | 7.76 ms: 1.07x slower                                            |
| coverage                 | 79.4 ms                                                | 90.4 ms: 1.14x slower                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                            |
| gc_traversal             | 3.62 ms                                                | 4.93 ms: 1.36x slower                                            |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.53x slower                                            |
| bench_mp_pool            | 24.0 ms                                                | 81.1 ms: 3.38x slower                                            |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                     |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250116-3.14.0a4+-c57fe46/bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.442x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.26x
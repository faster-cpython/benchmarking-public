# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_nops
- machine: linux-x86_64
- commit hash: b40ad57
- commit date: 2025-06-27
- overall geometric mean: 1.477x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.34x faster                                            |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                          |
| html5lib       | 88.9 ms                                                | 61.2 ms: 1.45x faster                                           |
| Geometric mean | (ref)                                                  | 1.35x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 601 ms: 2.94x faster                                            |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                            |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.77x faster                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 496 ms: 2.05x faster                                            |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 117 ms                                                 | 66.1 ms: 1.77x faster                                           |
| nbody          | 154 ms                                                 | 96.9 ms: 1.58x faster                                           |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                  | 1.42x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                            |
| regex_v8       | 27.8 ms                                                | 23.2 ms: 1.20x faster                                           |
| regex_effbot   | 3.63 ms                                                | 3.25 ms: 1.12x faster                                           |
| regex_dna      | 227 ms                                                 | 211 ms: 1.08x faster                                            |
| Geometric mean | (ref)                                                  | 1.21x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.70x faster                                          |
| unpickle_pure_python | 331 us                                                 | 201 us: 1.64x faster                                            |
| pickle_pure_python   | 484 us                                                 | 328 us: 1.48x faster                                            |
| xml_etree_process    | 79.1 ms                                                | 56.3 ms: 1.41x faster                                           |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                           |
| xml_etree_generate   | 99.4 ms                                                | 80.5 ms: 1.24x faster                                           |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                            |
| xml_etree_iterparse  | 115 ms                                                 | 99.0 ms: 1.17x faster                                           |
| json_loads           | 31.2 us                                                | 28.2 us: 1.11x faster                                           |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                           |
| python_startup_no_site | 5.93 ms                                                | 6.93 ms: 1.17x slower                                           |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.8 ms: 1.51x faster                                           |
| genshi_text     | 31.8 ms                                                | 21.6 ms: 1.47x faster                                           |
| django_template | 48.2 ms                                                | 32.8 ms: 1.47x faster                                           |
| genshi_xml      | 66.0 ms                                                | 51.3 ms: 1.29x faster                                           |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                            |
| async_tree_io            | 1.77 sec                                               | 601 ms: 2.94x faster                                            |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                            |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.77x faster                                            |
| deltablue                | 7.91 ms                                                | 3.12 ms: 2.54x faster                                           |
| generators               | 80.1 ms                                                | 32.0 ms: 2.51x faster                                           |
| richards_super           | 94.7 ms                                                | 38.5 ms: 2.46x faster                                           |
| richards                 | 79.3 ms                                                | 33.3 ms: 2.38x faster                                           |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.30x faster                                          |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 496 ms: 2.05x faster                                            |
| go                       | 240 ms                                                 | 118 ms: 2.04x faster                                            |
| deepcopy_memo            | 58.5 us                                                | 29.2 us: 2.00x faster                                           |
| pylint                   | 551 ms                                                 | 282 ms: 1.95x faster                                            |
| chaos                    | 115 ms                                                 | 60.9 ms: 1.89x faster                                           |
| deepcopy                 | 479 us                                                 | 256 us: 1.87x faster                                            |
| logging_silent           | 190 ns                                                 | 102 ns: 1.87x faster                                            |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                            |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                            |
| spectral_norm            | 170 ms                                                 | 93.6 ms: 1.82x faster                                           |
| scimark_monte_carlo      | 118 ms                                                 | 65.8 ms: 1.80x faster                                           |
| float                    | 117 ms                                                 | 66.1 ms: 1.77x faster                                           |
| pyflate                  | 716 ms                                                 | 416 ms: 1.72x faster                                            |
| djangocms                | 38.4 us                                                | 22.5 us: 1.71x faster                                           |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.70x faster                                          |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.70x faster                                           |
| crypto_pyaes             | 128 ms                                                 | 75.7 ms: 1.69x faster                                           |
| hexiom                   | 10.4 ms                                                | 6.32 ms: 1.64x faster                                           |
| unpickle_pure_python     | 331 us                                                 | 201 us: 1.64x faster                                            |
| nbody                    | 154 ms                                                 | 96.9 ms: 1.58x faster                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                           |
| mako                     | 16.3 ms                                                | 10.8 ms: 1.51x faster                                           |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                            |
| pickle_pure_python       | 484 us                                                 | 328 us: 1.48x faster                                            |
| genshi_text              | 31.8 ms                                                | 21.6 ms: 1.47x faster                                           |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.47x faster                                            |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                           |
| django_template          | 48.2 ms                                                | 32.8 ms: 1.47x faster                                           |
| html5lib                 | 88.9 ms                                                | 61.2 ms: 1.45x faster                                           |
| logging_format           | 9.09 us                                                | 6.28 us: 1.45x faster                                           |
| scimark_fft              | 466 ms                                                 | 324 ms: 1.44x faster                                            |
| dulwich_log              | 84.3 ms                                                | 59.3 ms: 1.42x faster                                           |
| coroutines               | 35.1 ms                                                | 24.7 ms: 1.42x faster                                           |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.42x faster                                          |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                          |
| pprint_safe_repr         | 1.02 sec                                               | 722 ms: 1.41x faster                                            |
| xml_etree_process        | 79.1 ms                                                | 56.3 ms: 1.41x faster                                           |
| thrift                   | 1.07 ms                                                | 780 us: 1.37x faster                                            |
| 2to3                     | 348 ms                                                 | 259 ms: 1.34x faster                                            |
| sympy_integrate          | 25.8 ms                                                | 19.3 ms: 1.33x faster                                           |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.95 ms: 1.31x faster                                           |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                           |
| genshi_xml               | 66.0 ms                                                | 51.3 ms: 1.29x faster                                           |
| fannkuch                 | 532 ms                                                 | 414 ms: 1.28x faster                                            |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                            |
| nqueens                  | 106 ms                                                 | 84.0 ms: 1.26x faster                                           |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                          |
| xml_etree_generate       | 99.4 ms                                                | 80.5 ms: 1.24x faster                                           |
| sympy_expand             | 566 ms                                                 | 467 ms: 1.21x faster                                            |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                           |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                           |
| regex_v8                 | 27.8 ms                                                | 23.2 ms: 1.20x faster                                           |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                            |
| xml_etree_iterparse      | 115 ms                                                 | 99.0 ms: 1.17x faster                                           |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                            |
| regex_effbot             | 3.63 ms                                                | 3.25 ms: 1.12x faster                                           |
| json_loads               | 31.2 us                                                | 28.2 us: 1.11x faster                                           |
| json                     | 5.69 ms                                                | 5.23 ms: 1.09x faster                                           |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                           |
| regex_dna                | 227 ms                                                 | 211 ms: 1.08x faster                                            |
| async_generators         | 444 ms                                                 | 429 ms: 1.03x faster                                            |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                            |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                            |
| telco                    | 7.27 ms                                                | 7.77 ms: 1.07x slower                                           |
| coverage                 | 79.4 ms                                                | 87.8 ms: 1.11x slower                                           |
| python_startup_no_site   | 5.93 ms                                                | 6.93 ms: 1.17x slower                                           |
| gc_traversal             | 3.62 ms                                                | 4.96 ms: 1.37x slower                                           |
| create_gc_cycles         | 1.62 ms                                                | 2.58 ms: 1.59x slower                                           |
| Geometric mean           | (ref)                                                  | 1.48x faster                                                    |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250627-3.15.0a0-b40ad57-JIT/bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.477x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.33x
# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_12_10
- machine: linux-x86_64
- commit hash: 0d5e4e2
- commit date: 2025-06-29
- overall geometric mean: 1.480x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.35x faster                                                |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                              |
| html5lib       | 88.9 ms                                                | 61.3 ms: 1.45x faster                                               |
| Geometric mean | (ref)                                                  | 1.34x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 601 ms: 2.94x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                                |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.77x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 496 ms: 2.05x faster                                                |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.7 ms: 1.78x faster                                               |
| nbody          | 154 ms                                                 | 97.1 ms: 1.58x faster                                               |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.42x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                                |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.37 ms: 1.08x faster                                               |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 193 us: 1.72x faster                                                |
| tomli_loads          | 3.14 sec                                               | 1.83 sec: 1.71x faster                                              |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.50x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 55.8 ms: 1.42x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 80.6 ms: 1.23x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                               |
| json_loads           | 31.2 us                                                | 28.5 us: 1.09x faster                                               |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.19x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 6.96 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.8 ms: 1.52x faster                                               |
| django_template | 48.2 ms                                                | 32.5 ms: 1.48x faster                                               |
| genshi_text     | 31.8 ms                                                | 22.4 ms: 1.42x faster                                               |
| genshi_xml      | 66.0 ms                                                | 51.4 ms: 1.28x faster                                               |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.25x faster                                                |
| async_tree_io            | 1.77 sec                                               | 601 ms: 2.94x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                                |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.77x faster                                                |
| generators               | 80.1 ms                                                | 30.4 ms: 2.63x faster                                               |
| deltablue                | 7.91 ms                                                | 3.05 ms: 2.60x faster                                               |
| richards_super           | 94.7 ms                                                | 37.6 ms: 2.52x faster                                               |
| richards                 | 79.3 ms                                                | 32.4 ms: 2.44x faster                                               |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.30x faster                                              |
| go                       | 240 ms                                                 | 117 ms: 2.06x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 496 ms: 2.05x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.9 us: 1.95x faster                                               |
| pylint                   | 551 ms                                                 | 283 ms: 1.95x faster                                                |
| spectral_norm            | 170 ms                                                 | 90.2 ms: 1.88x faster                                               |
| chaos                    | 115 ms                                                 | 61.7 ms: 1.87x faster                                               |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                |
| float                    | 117 ms                                                 | 65.7 ms: 1.78x faster                                               |
| logging_silent           | 190 ns                                                 | 106 ns: 1.78x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 66.6 ms: 1.78x faster                                               |
| pyflate                  | 716 ms                                                 | 406 ms: 1.76x faster                                                |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 193 us: 1.72x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.83 sec: 1.71x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 75.1 ms: 1.70x faster                                               |
| djangocms                | 38.4 us                                                | 22.8 us: 1.68x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.26 ms: 1.66x faster                                               |
| nbody                    | 154 ms                                                 | 97.1 ms: 1.58x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                               |
| mako                     | 16.3 ms                                                | 10.8 ms: 1.52x faster                                               |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.50x faster                                                |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                |
| django_template          | 48.2 ms                                                | 32.5 ms: 1.48x faster                                               |
| logging_simple           | 8.30 us                                                | 5.60 us: 1.48x faster                                               |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.43 sec: 1.47x faster                                              |
| logging_format           | 9.09 us                                                | 6.26 us: 1.45x faster                                               |
| html5lib                 | 88.9 ms                                                | 61.3 ms: 1.45x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 704 ms: 1.45x faster                                                |
| coroutines               | 35.1 ms                                                | 24.5 ms: 1.43x faster                                               |
| genshi_text              | 31.8 ms                                                | 22.4 ms: 1.42x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 55.8 ms: 1.42x faster                                               |
| dulwich_log              | 84.3 ms                                                | 59.7 ms: 1.41x faster                                               |
| thrift                   | 1.07 ms                                                | 776 us: 1.38x faster                                                |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                              |
| 2to3                     | 348 ms                                                 | 259 ms: 1.35x faster                                                |
| fannkuch                 | 532 ms                                                 | 396 ms: 1.34x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                               |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.94 ms: 1.31x faster                                               |
| genshi_xml               | 66.0 ms                                                | 51.4 ms: 1.28x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                               |
| nqueens                  | 106 ms                                                 | 82.7 ms: 1.28x faster                                               |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                                |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 80.6 ms: 1.23x faster                                               |
| sympy_expand             | 566 ms                                                 | 469 ms: 1.21x faster                                                |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.21x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.19x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                               |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                               |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                |
| json_loads               | 31.2 us                                                | 28.5 us: 1.09x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                               |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.37 ms: 1.08x faster                                               |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                |
| async_generators         | 444 ms                                                 | 438 ms: 1.01x faster                                                |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                |
| telco                    | 7.27 ms                                                | 7.72 ms: 1.06x slower                                               |
| coverage                 | 79.4 ms                                                | 88.0 ms: 1.11x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 6.96 ms: 1.17x slower                                               |
| gc_traversal             | 3.62 ms                                                | 5.17 ms: 1.43x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.61 ms: 1.61x slower                                               |
| Geometric mean           | (ref)                                                  | 1.48x faster                                                        |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250629-3.15.0a0-0d5e4e2-JIT/bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.480x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.33x
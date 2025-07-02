# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_6_6
- machine: linux-x86_64
- commit hash: 6c99b17
- commit date: 2025-07-02
- overall geometric mean: 1.421x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 267 ms: 1.30x faster                                              |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.23x faster                                            |
| html5lib       | 88.9 ms                                                | 61.7 ms: 1.44x faster                                             |
| Geometric mean | (ref)                                                  | 1.32x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 602 ms: 2.94x faster                                              |
| async_tree_none         | 728 ms                                                 | 255 ms: 2.85x faster                                              |
| async_tree_memoization  | 870 ms                                                 | 321 ms: 2.71x faster                                              |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 502 ms: 2.02x faster                                              |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.7 ms: 1.78x faster                                             |
| nbody          | 154 ms                                                 | 92.9 ms: 1.65x faster                                             |
| pidigits       | 191 ms                                                 | 193 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                  | 1.43x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                              |
| regex_v8       | 27.8 ms                                                | 23.1 ms: 1.20x faster                                             |
| regex_effbot   | 3.63 ms                                                | 3.39 ms: 1.07x faster                                             |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                              |
| Geometric mean | (ref)                                                  | 1.18x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 192 us: 1.72x faster                                              |
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.70x faster                                            |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                              |
| xml_etree_process    | 79.1 ms                                                | 54.9 ms: 1.44x faster                                             |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                             |
| xml_etree_generate   | 99.4 ms                                                | 78.8 ms: 1.26x faster                                             |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                              |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                             |
| json_loads           | 31.2 us                                                | 28.9 us: 1.08x faster                                             |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                             |
| python_startup_no_site | 5.93 ms                                                | 6.95 ms: 1.17x slower                                             |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.5 ms: 1.56x faster                                             |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                             |
| django_template | 48.2 ms                                                | 32.6 ms: 1.48x faster                                             |
| genshi_xml      | 66.0 ms                                                | 50.9 ms: 1.30x faster                                             |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                              |
| async_tree_io            | 1.77 sec                                               | 602 ms: 2.94x faster                                              |
| async_tree_none          | 728 ms                                                 | 255 ms: 2.85x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 321 ms: 2.71x faster                                              |
| generators               | 80.1 ms                                                | 30.4 ms: 2.63x faster                                             |
| deltablue                | 7.91 ms                                                | 3.06 ms: 2.58x faster                                             |
| richards_super           | 94.7 ms                                                | 39.3 ms: 2.41x faster                                             |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.30x faster                                            |
| richards                 | 79.3 ms                                                | 34.7 ms: 2.28x faster                                             |
| go                       | 240 ms                                                 | 115 ms: 2.09x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 502 ms: 2.02x faster                                              |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                             |
| chaos                    | 115 ms                                                 | 60.5 ms: 1.91x faster                                             |
| pylint                   | 551 ms                                                 | 289 ms: 1.91x faster                                              |
| spectral_norm            | 170 ms                                                 | 90.1 ms: 1.88x faster                                             |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                              |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                              |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                              |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                              |
| float                    | 117 ms                                                 | 65.7 ms: 1.78x faster                                             |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.77x faster                                             |
| crypto_pyaes             | 128 ms                                                 | 72.2 ms: 1.77x faster                                             |
| pyflate                  | 716 ms                                                 | 406 ms: 1.76x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 67.1 ms: 1.76x faster                                             |
| unpickle_pure_python     | 331 us                                                 | 192 us: 1.72x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.08 ms: 1.71x faster                                             |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.70x faster                                            |
| djangocms                | 38.4 us                                                | 22.8 us: 1.69x faster                                             |
| nbody                    | 154 ms                                                 | 92.9 ms: 1.65x faster                                             |
| mako                     | 16.3 ms                                                | 10.5 ms: 1.56x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                             |
| pprint_pformat           | 2.10 sec                                               | 1.39 sec: 1.51x faster                                            |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                              |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                              |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                             |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                              |
| django_template          | 48.2 ms                                                | 32.6 ms: 1.48x faster                                             |
| logging_simple           | 8.30 us                                                | 5.68 us: 1.46x faster                                             |
| pprint_safe_repr         | 1.02 sec                                               | 698 ms: 1.46x faster                                              |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                              |
| xml_etree_process        | 79.1 ms                                                | 54.9 ms: 1.44x faster                                             |
| html5lib                 | 88.9 ms                                                | 61.7 ms: 1.44x faster                                             |
| logging_format           | 9.09 us                                                | 6.35 us: 1.43x faster                                             |
| dulwich_log              | 84.3 ms                                                | 59.8 ms: 1.41x faster                                             |
| thrift                   | 1.07 ms                                                | 776 us: 1.38x faster                                              |
| coroutines               | 35.1 ms                                                | 25.4 ms: 1.38x faster                                             |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                            |
| fannkuch                 | 532 ms                                                 | 396 ms: 1.34x faster                                              |
| 2to3                     | 348 ms                                                 | 267 ms: 1.30x faster                                              |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                             |
| genshi_xml               | 66.0 ms                                                | 50.9 ms: 1.30x faster                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.02 ms: 1.29x faster                                             |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                             |
| sympy_sum                | 196 ms                                                 | 153 ms: 1.28x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 78.8 ms: 1.26x faster                                             |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                              |
| nqueens                  | 106 ms                                                 | 84.1 ms: 1.26x faster                                             |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.23x faster                                            |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                              |
| sympy_expand             | 566 ms                                                 | 470 ms: 1.20x faster                                              |
| regex_v8                 | 27.8 ms                                                | 23.1 ms: 1.20x faster                                             |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                             |
| pathlib                  | 20.5 ms                                                | 17.2 ms: 1.19x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                             |
| meteor_contest           | 120 ms                                                 | 103 ms: 1.16x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                             |
| json_loads               | 31.2 us                                                | 28.9 us: 1.08x faster                                             |
| regex_effbot             | 3.63 ms                                                | 3.39 ms: 1.07x faster                                             |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                             |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                              |
| async_generators         | 444 ms                                                 | 427 ms: 1.04x faster                                              |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                              |
| pidigits                 | 191 ms                                                 | 193 ms: 1.01x slower                                              |
| coverage                 | 79.4 ms                                                | 87.4 ms: 1.10x slower                                             |
| python_startup_no_site   | 5.93 ms                                                | 6.95 ms: 1.17x slower                                             |
| gc_traversal             | 3.62 ms                                                | 5.03 ms: 1.39x slower                                             |
| create_gc_cycles         | 1.62 ms                                                | 2.64 ms: 1.63x slower                                             |
| telco                    | 7.27 ms                                                | 161 ms: 22.19x slower                                             |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                      |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250702-3.15.0a0-6c99b17-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.421x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.38x
# Results vs. 3.10.4

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-x86_64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.204x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.53x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 332 ms: 1.05x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.96 sec: 1.15x faster                                                       |
| html5lib       | 94.6 ms                                                      | 72.6 ms: 1.30x faster                                                        |
| Geometric mean | (ref)                                                        | 1.17x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 619 ms: 2.58x faster                                                         |
| async_tree_none         | 692 ms                                                       | 297 ms: 2.33x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 365 ms: 2.24x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 532 ms: 1.76x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.21x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 74.5 ms: 1.49x faster                                                        |
| pidigits       | 271 ms                                                       | 248 ms: 1.09x faster                                                         |
| nbody          | 134 ms                                                       | 128 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.19x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 153 ms: 1.24x faster                                                         |
| regex_dna      | 261 ms                                                       | 237 ms: 1.10x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.5 ms: 1.07x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.20 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 236 us: 1.32x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 89.6 ms: 1.23x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 370 us: 1.23x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.38 sec: 1.23x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 70.0 ms: 1.09x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 13.7 ms: 1.07x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 96.8 ms: 1.05x slower                                                        |
| json_loads           | 30.3 us                                                      | 32.9 us: 1.08x slower                                                        |
| unpickle             | 13.5 us                                                      | 15.6 us: 1.16x slower                                                        |
| unpickle_list        | 4.65 us                                                      | 5.39 us: 1.16x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 36.6 us: 1.24x slower                                                        |
| pickle               | 9.89 us                                                      | 12.4 us: 1.25x slower                                                        |
| pickle_list          | 4.12 us                                                      | 5.42 us: 1.32x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                        |
| python_startup         | 11.5 ms                                                      | 18.7 ms: 1.62x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.61x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 45.4 ms: 1.11x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 29.6 ms: 1.06x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 63.6 ms: 1.01x slower                                                        |
| mako            | 14.7 ms                                                      | 17.9 ms: 1.22x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 619 ms: 2.58x faster                                                         |
| typing_runtime_protocols | 537 us                                                       | 213 us: 2.52x faster                                                         |
| async_tree_none          | 692 ms                                                       | 297 ms: 2.33x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 365 ms: 2.24x faster                                                         |
| asyncio_tcp              | 779 ms                                                       | 425 ms: 1.83x faster                                                         |
| generators               | 57.3 ms                                                      | 32.0 ms: 1.79x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 532 ms: 1.76x faster                                                         |
| go                       | 262 ms                                                       | 150 ms: 1.75x faster                                                         |
| logging_silent           | 167 ns                                                       | 99.6 ns: 1.68x faster                                                        |
| deltablue                | 7.50 ms                                                      | 4.49 ms: 1.67x faster                                                        |
| gc_traversal             | 3.42 ms                                                      | 2.05 ms: 1.67x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.88 sec: 1.65x faster                                                       |
| pylint                   | 566 ms                                                       | 347 ms: 1.63x faster                                                         |
| chaos                    | 109 ms                                                       | 70.2 ms: 1.55x faster                                                        |
| scimark_sor              | 180 ms                                                       | 118 ms: 1.53x faster                                                         |
| pyflate                  | 733 ms                                                       | 491 ms: 1.49x faster                                                         |
| float                    | 111 ms                                                       | 74.5 ms: 1.49x faster                                                        |
| coroutines               | 30.3 ms                                                      | 20.9 ms: 1.45x faster                                                        |
| raytrace                 | 489 ms                                                       | 337 ms: 1.45x faster                                                         |
| deepcopy                 | 468 us                                                       | 327 us: 1.43x faster                                                         |
| scimark_lu               | 167 ms                                                       | 119 ms: 1.40x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.62 ms: 1.38x faster                                                        |
| spectral_norm            | 139 ms                                                       | 101 ms: 1.38x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 36.3 us: 1.37x faster                                                        |
| comprehensions           | 26.7 us                                                      | 19.7 us: 1.35x faster                                                        |
| richards_super           | 90.6 ms                                                      | 67.2 ms: 1.35x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.1 ms: 1.32x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 2.03 ms: 1.32x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 236 us: 1.32x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 7.19 ms: 1.31x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 72.6 ms: 1.30x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 84.4 ms: 1.27x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 93.6 ms: 1.27x faster                                                        |
| richards                 | 75.1 ms                                                      | 59.2 ms: 1.27x faster                                                        |
| regex_compile            | 190 ms                                                       | 153 ms: 1.24x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 89.6 ms: 1.23x faster                                                        |
| logging_simple           | 8.88 us                                                      | 7.21 us: 1.23x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 370 us: 1.23x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.38 sec: 1.23x faster                                                       |
| logging_format           | 9.64 us                                                      | 8.07 us: 1.19x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 69.0 ms: 1.18x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 896 ms: 1.17x faster                                                         |
| thrift                   | 1.18 ms                                                      | 1.01 ms: 1.16x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.86 sec: 1.16x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.59 us: 1.16x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.96 sec: 1.15x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.56 us: 1.13x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 128 ms: 1.12x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 20.5 ms: 1.11x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 171 ms: 1.11x faster                                                         |
| django_template          | 50.2 ms                                                      | 45.4 ms: 1.11x faster                                                        |
| sympy_sum                | 193 ms                                                       | 174 ms: 1.10x faster                                                         |
| regex_dna                | 261 ms                                                       | 237 ms: 1.10x faster                                                         |
| pidigits                 | 271 ms                                                       | 248 ms: 1.09x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.76 sec: 1.09x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 70.0 ms: 1.09x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 55.7 ns: 1.07x faster                                                        |
| scimark_fft              | 361 ms                                                       | 337 ms: 1.07x faster                                                         |
| sympy_expand             | 600 ms                                                       | 561 ms: 1.07x faster                                                         |
| sympy_str                | 360 ms                                                       | 337 ms: 1.07x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 65.7 ms: 1.07x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.5 ms: 1.07x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 13.7 ms: 1.07x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 29.6 ms: 1.06x faster                                                        |
| 2to3                     | 350 ms                                                       | 332 ms: 1.05x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 26.9 ms: 1.05x faster                                                        |
| nbody                    | 134 ms                                                       | 128 ms: 1.04x faster                                                         |
| nqueens                  | 115 ms                                                       | 111 ms: 1.04x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 379 ms: 1.03x faster                                                         |
| fannkuch                 | 483 ms                                                       | 476 ms: 1.01x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 63.6 ms: 1.01x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.20 ms: 1.04x slower                                                        |
| json                     | 5.86 ms                                                      | 6.15 ms: 1.05x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 96.8 ms: 1.05x slower                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.47 ms: 1.08x slower                                                        |
| json_loads               | 30.3 us                                                      | 32.9 us: 1.08x slower                                                        |
| async_generators         | 421 ms                                                       | 470 ms: 1.12x slower                                                         |
| meteor_contest           | 138 ms                                                       | 155 ms: 1.12x slower                                                         |
| create_gc_cycles         | 1.76 ms                                                      | 2.02 ms: 1.14x slower                                                        |
| unpickle                 | 13.5 us                                                      | 15.6 us: 1.16x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 5.39 us: 1.16x slower                                                        |
| mako                     | 14.7 ms                                                      | 17.9 ms: 1.22x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 36.6 us: 1.24x slower                                                        |
| pickle                   | 9.89 us                                                      | 12.4 us: 1.25x slower                                                        |
| telco                    | 7.23 ms                                                      | 9.12 ms: 1.26x slower                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.46 ms: 1.28x slower                                                        |
| pickle_list              | 4.12 us                                                      | 5.42 us: 1.32x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                        |
| python_startup           | 11.5 ms                                                      | 18.7 ms: 1.62x slower                                                        |
| coverage                 | 63.3 ms                                                      | 108 ms: 1.71x slower                                                         |
| bench_mp_pool            | 6.37 ms                                                      | 47.5 ms: 7.45x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.16x faster                                                                 |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (11) of results/bm-20250201-3.14.0a4+-cf4c4ec-NOGIL/bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.204x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.53x
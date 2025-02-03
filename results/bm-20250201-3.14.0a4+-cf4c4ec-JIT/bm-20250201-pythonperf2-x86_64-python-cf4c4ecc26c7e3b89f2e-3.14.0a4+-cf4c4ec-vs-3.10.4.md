# Results vs. 3.10.4

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-x86_64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.316x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 289 ms: 1.21x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.95 sec: 1.16x faster                                                       |
| html5lib       | 94.6 ms                                                      | 69.7 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 656 ms: 2.43x faster                                                         |
| async_tree_none         | 692 ms                                                       | 298 ms: 2.32x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 359 ms: 2.28x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 528 ms: 1.77x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.19x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 67.7 ms: 1.64x faster                                                        |
| nbody          | 134 ms                                                       | 89.5 ms: 1.50x faster                                                        |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.36x faster                                                         |
| regex_dna      | 261 ms                                                       | 239 ms: 1.09x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.13 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 203 us: 1.54x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.04 sec: 1.43x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 334 us: 1.36x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 57.1 ms: 1.33x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.0 ms: 1.33x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 94.5 ms: 1.17x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 80.3 ms: 1.15x faster                                                        |
| json_loads           | 30.3 us                                                      | 26.7 us: 1.14x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.79 us: 1.03x slower                                                        |
| unpickle             | 13.5 us                                                      | 14.1 us: 1.04x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 32.2 us: 1.09x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.99 us: 1.21x slower                                                        |
| pickle               | 9.89 us                                                      | 12.0 us: 1.22x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.42 ms: 1.56x faster                                                        |
| django_template | 50.2 ms                                                      | 37.7 ms: 1.33x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 26.5 ms: 1.18x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 61.8 ms: 1.02x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 175 us: 3.07x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 656 ms: 2.43x faster                                                         |
| async_tree_none          | 692 ms                                                       | 298 ms: 2.32x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 359 ms: 2.28x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.43 ms: 2.19x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 367 ms: 2.13x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                       |
| go                       | 262 ms                                                       | 140 ms: 1.87x faster                                                         |
| scimark_sor              | 180 ms                                                       | 101 ms: 1.79x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 528 ms: 1.77x faster                                                         |
| pylint                   | 566 ms                                                       | 328 ms: 1.72x faster                                                         |
| richards_super           | 90.6 ms                                                      | 53.2 ms: 1.70x faster                                                        |
| logging_silent           | 167 ns                                                       | 99.1 ns: 1.69x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 64.3 ms: 1.67x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.9 us: 1.67x faster                                                        |
| scimark_lu               | 167 ms                                                       | 101 ms: 1.65x faster                                                         |
| float                    | 111 ms                                                       | 67.7 ms: 1.64x faster                                                        |
| chaos                    | 109 ms                                                       | 67.6 ms: 1.61x faster                                                        |
| richards                 | 75.1 ms                                                      | 46.8 ms: 1.60x faster                                                        |
| pyflate                  | 733 ms                                                       | 458 ms: 1.60x faster                                                         |
| raytrace                 | 489 ms                                                       | 306 ms: 1.60x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                        |
| spectral_norm            | 139 ms                                                       | 87.8 ms: 1.58x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.42 ms: 1.56x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 203 us: 1.54x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 78.2 ms: 1.52x faster                                                        |
| deepcopy                 | 468 us                                                       | 308 us: 1.52x faster                                                         |
| nbody                    | 134 ms                                                       | 89.5 ms: 1.50x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                                        |
| coroutines               | 30.3 ms                                                      | 20.7 ms: 1.46x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.04 sec: 1.43x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.30 us: 1.41x faster                                                        |
| comprehensions           | 26.7 us                                                      | 19.0 us: 1.40x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.90 us: 1.40x faster                                                        |
| regex_compile            | 190 ms                                                       | 139 ms: 1.36x faster                                                         |
| generators               | 57.3 ms                                                      | 42.0 ms: 1.36x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 334 us: 1.36x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 69.7 ms: 1.36x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 785 ms: 1.34x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                                       |
| django_template          | 50.2 ms                                                      | 37.7 ms: 1.33x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 57.1 ms: 1.33x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.0 ms: 1.33x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.03 us: 1.32x faster                                                        |
| thrift                   | 1.18 ms                                                      | 889 us: 1.32x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 16.3 ms: 1.31x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 145 ms: 1.31x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.7 ms: 1.28x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 7.54 ms: 1.25x faster                                                        |
| fannkuch                 | 483 ms                                                       | 388 ms: 1.24x faster                                                         |
| sympy_sum                | 193 ms                                                       | 157 ms: 1.23x faster                                                         |
| scimark_fft              | 361 ms                                                       | 294 ms: 1.23x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 66.8 ms: 1.21x faster                                                        |
| 2to3                     | 350 ms                                                       | 289 ms: 1.21x faster                                                         |
| sympy_str                | 360 ms                                                       | 303 ms: 1.19x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 26.5 ms: 1.18x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 969 us: 1.18x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 24.0 ms: 1.18x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 94.5 ms: 1.17x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.58 sec: 1.17x faster                                                       |
| sympy_expand             | 600 ms                                                       | 517 ms: 1.16x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.95 sec: 1.16x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 125 ms: 1.15x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 80.3 ms: 1.15x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 61.1 ms: 1.15x faster                                                        |
| json_loads               | 30.3 us                                                      | 26.7 us: 1.14x faster                                                        |
| nqueens                  | 115 ms                                                       | 103 ms: 1.12x faster                                                         |
| regex_dna                | 261 ms                                                       | 239 ms: 1.09x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.75 us: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.06x faster                                                         |
| json                     | 5.86 ms                                                      | 5.56 ms: 1.06x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.88 ms: 1.04x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 61.8 ms: 1.02x faster                                                        |
| async_generators         | 421 ms                                                       | 426 ms: 1.01x slower                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.13 ms: 1.01x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 4.79 us: 1.03x slower                                                        |
| unpickle                 | 13.5 us                                                      | 14.1 us: 1.04x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.71 ms: 1.07x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 32.2 us: 1.09x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.99 us: 1.21x slower                                                        |
| pickle                   | 9.89 us                                                      | 12.0 us: 1.22x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                        |
| coverage                 | 63.3 ms                                                      | 79.2 ms: 1.25x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.65 ms: 1.51x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.29 ms: 1.84x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.33 sec: 208.19x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.22x faster                                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, unpack_sequence
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (11) of results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.316x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.29x
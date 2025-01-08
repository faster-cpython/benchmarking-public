# Results vs. 3.10.4

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.308x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 290 ms: 1.21x faster                                                |
| docutils       | 3.41 sec                                                     | 2.96 sec: 1.15x faster                                              |
| html5lib       | 94.6 ms                                                      | 69.8 ms: 1.36x faster                                               |
| Geometric mean | (ref)                                                        | 1.24x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 637 ms: 2.51x faster                                                |
| async_tree_none         | 692 ms                                                       | 287 ms: 2.41x faster                                                |
| async_tree_memoization  | 819 ms                                                       | 355 ms: 2.31x faster                                                |
| async_tree_cpu_io_mixed | 936 ms                                                       | 520 ms: 1.80x faster                                                |
| Geometric mean          | (ref)                                                        | 2.24x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 111 ms                                                       | 68.1 ms: 1.63x faster                                               |
| nbody          | 134 ms                                                       | 98.2 ms: 1.37x faster                                               |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                |
| Geometric mean | (ref)                                                        | 1.33x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.38x faster                                                |
| regex_dna      | 261 ms                                                       | 231 ms: 1.13x faster                                                |
| regex_v8       | 27.2 ms                                                      | 25.7 ms: 1.05x faster                                               |
| regex_effbot   | 3.09 ms                                                      | 3.17 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                        | 1.12x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 198 us: 1.58x faster                                                |
| tomli_loads          | 2.92 sec                                                     | 2.03 sec: 1.43x faster                                              |
| pickle_pure_python   | 455 us                                                       | 335 us: 1.36x faster                                                |
| xml_etree_process    | 75.9 ms                                                      | 57.7 ms: 1.32x faster                                               |
| json_dumps           | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                               |
| json_loads           | 30.3 us                                                      | 24.0 us: 1.27x faster                                               |
| xml_etree_iterparse  | 110 ms                                                       | 93.9 ms: 1.18x faster                                               |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                |
| xml_etree_generate   | 92.3 ms                                                      | 81.7 ms: 1.13x faster                                               |
| Geometric mean       | (ref)                                                        | 1.30x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                               |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                               |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.61 ms: 1.53x faster                                               |
| django_template | 50.2 ms                                                      | 39.2 ms: 1.28x faster                                               |
| genshi_text     | 31.4 ms                                                      | 27.0 ms: 1.16x faster                                               |
| genshi_xml      | 63.3 ms                                                      | 62.9 ms: 1.01x faster                                               |
| Geometric mean  | (ref)                                                        | 1.23x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 180 us: 2.99x faster                                                |
| async_tree_io            | 1.60 sec                                                     | 637 ms: 2.51x faster                                                |
| async_tree_none          | 692 ms                                                       | 287 ms: 2.41x faster                                                |
| async_tree_memoization   | 819 ms                                                       | 355 ms: 2.31x faster                                                |
| deltablue                | 7.50 ms                                                      | 3.51 ms: 2.14x faster                                               |
| scimark_sor              | 180 ms                                                       | 98.7 ms: 1.83x faster                                               |
| go                       | 262 ms                                                       | 145 ms: 1.81x faster                                                |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 520 ms: 1.80x faster                                                |
| deepcopy_memo            | 49.8 us                                                      | 27.9 us: 1.78x faster                                               |
| scimark_lu               | 167 ms                                                       | 94.7 ms: 1.76x faster                                               |
| richards_super           | 90.6 ms                                                      | 52.5 ms: 1.73x faster                                               |
| scimark_monte_carlo      | 107 ms                                                       | 62.6 ms: 1.72x faster                                               |
| pylint                   | 566 ms                                                       | 331 ms: 1.71x faster                                                |
| logging_silent           | 167 ns                                                       | 101 ns: 1.66x faster                                                |
| sqlglot_parse            | 2.24 ms                                                      | 1.36 ms: 1.65x faster                                               |
| float                    | 111 ms                                                       | 68.1 ms: 1.63x faster                                               |
| richards                 | 75.1 ms                                                      | 46.3 ms: 1.62x faster                                               |
| crypto_pyaes             | 119 ms                                                       | 74.5 ms: 1.60x faster                                               |
| chaos                    | 109 ms                                                       | 68.2 ms: 1.59x faster                                               |
| pyflate                  | 733 ms                                                       | 463 ms: 1.58x faster                                                |
| unpickle_pure_python     | 312 us                                                       | 198 us: 1.58x faster                                                |
| deepcopy                 | 468 us                                                       | 299 us: 1.56x faster                                                |
| spectral_norm            | 139 ms                                                       | 90.1 ms: 1.54x faster                                               |
| mako                     | 14.7 ms                                                      | 9.61 ms: 1.53x faster                                               |
| sqlglot_transpile        | 2.68 ms                                                      | 1.77 ms: 1.52x faster                                               |
| raytrace                 | 489 ms                                                       | 334 ms: 1.46x faster                                                |
| coroutines               | 30.3 ms                                                      | 20.9 ms: 1.45x faster                                               |
| generators               | 57.3 ms                                                      | 39.9 ms: 1.44x faster                                               |
| tomli_loads              | 2.92 sec                                                     | 2.03 sec: 1.43x faster                                              |
| comprehensions           | 26.7 us                                                      | 19.3 us: 1.38x faster                                               |
| regex_compile            | 190 ms                                                       | 138 ms: 1.38x faster                                                |
| nbody                    | 134 ms                                                       | 98.2 ms: 1.37x faster                                               |
| pickle_pure_python       | 455 us                                                       | 335 us: 1.36x faster                                                |
| html5lib                 | 94.6 ms                                                      | 69.8 ms: 1.36x faster                                               |
| deepcopy_reduce          | 4.01 us                                                      | 2.98 us: 1.35x faster                                               |
| logging_simple           | 8.88 us                                                      | 6.63 us: 1.34x faster                                               |
| thrift                   | 1.18 ms                                                      | 879 us: 1.34x faster                                                |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                              |
| xml_etree_process        | 75.9 ms                                                      | 57.7 ms: 1.32x faster                                               |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.32x faster                                              |
| logging_format           | 9.64 us                                                      | 7.36 us: 1.31x faster                                               |
| json_dumps               | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                               |
| pprint_safe_repr         | 1.05 sec                                                     | 807 ms: 1.30x faster                                                |
| sqlalchemy_declarative   | 190 ms                                                       | 146 ms: 1.30x faster                                                |
| pathlib                  | 21.4 ms                                                      | 16.5 ms: 1.29x faster                                               |
| django_template          | 50.2 ms                                                      | 39.2 ms: 1.28x faster                                               |
| hexiom                   | 9.42 ms                                                      | 7.42 ms: 1.27x faster                                               |
| json_loads               | 30.3 us                                                      | 24.0 us: 1.27x faster                                               |
| fannkuch                 | 483 ms                                                       | 382 ms: 1.26x faster                                                |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.1 ms: 1.25x faster                                               |
| dulwich_log              | 81.1 ms                                                      | 66.9 ms: 1.21x faster                                               |
| sympy_sum                | 193 ms                                                       | 159 ms: 1.21x faster                                                |
| 2to3                     | 350 ms                                                       | 290 ms: 1.21x faster                                                |
| scimark_fft              | 361 ms                                                       | 300 ms: 1.21x faster                                                |
| sympy_str                | 360 ms                                                       | 305 ms: 1.18x faster                                                |
| xml_etree_iterparse      | 110 ms                                                       | 93.9 ms: 1.18x faster                                               |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                |
| sympy_integrate          | 28.2 ms                                                      | 24.1 ms: 1.17x faster                                               |
| sqlglot_normalize        | 144 ms                                                       | 123 ms: 1.17x faster                                                |
| mdp                      | 3.01 sec                                                     | 2.58 sec: 1.17x faster                                              |
| genshi_text              | 31.4 ms                                                      | 27.0 ms: 1.16x faster                                               |
| sympy_expand             | 600 ms                                                       | 520 ms: 1.15x faster                                                |
| json                     | 5.86 ms                                                      | 5.09 ms: 1.15x faster                                               |
| docutils                 | 3.41 sec                                                     | 2.96 sec: 1.15x faster                                              |
| bench_thread_pool        | 1.14 ms                                                      | 995 us: 1.15x faster                                                |
| sqlglot_optimize         | 70.1 ms                                                      | 61.4 ms: 1.14x faster                                               |
| regex_dna                | 261 ms                                                       | 231 ms: 1.13x faster                                                |
| xml_etree_generate       | 92.3 ms                                                      | 81.7 ms: 1.13x faster                                               |
| nqueens                  | 115 ms                                                       | 102 ms: 1.12x faster                                                |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                               |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                |
| regex_v8                 | 27.2 ms                                                      | 25.7 ms: 1.05x faster                                               |
| meteor_contest           | 138 ms                                                       | 132 ms: 1.05x faster                                                |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.88 ms: 1.04x faster                                               |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.01x faster                                                |
| genshi_xml               | 63.3 ms                                                      | 62.9 ms: 1.01x faster                                               |
| regex_effbot             | 3.09 ms                                                      | 3.17 ms: 1.03x slower                                               |
| telco                    | 7.23 ms                                                      | 7.79 ms: 1.08x slower                                               |
| async_generators         | 421 ms                                                       | 467 ms: 1.11x slower                                                |
| mypy2                    | 933 ms                                                       | 1.04 sec: 1.11x slower                                              |
| python_startup_no_site   | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                               |
| coverage                 | 63.3 ms                                                      | 79.4 ms: 1.25x slower                                               |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                               |
| create_gc_cycles         | 1.76 ms                                                      | 2.69 ms: 1.52x slower                                               |
| gc_traversal             | 3.42 ms                                                      | 6.32 ms: 1.85x slower                                               |
| bench_mp_pool            | 6.37 ms                                                      | 1.48 sec: 232.92x slower                                            |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                        |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250107-3.14.0a3+-f098037-JIT/bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.308x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.31x
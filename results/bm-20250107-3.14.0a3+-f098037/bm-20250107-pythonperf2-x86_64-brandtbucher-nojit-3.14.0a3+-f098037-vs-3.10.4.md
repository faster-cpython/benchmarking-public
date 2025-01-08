# Results vs. 3.10.4

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.347x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                                |
| docutils       | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                              |
| html5lib       | 94.6 ms                                                      | 67.2 ms: 1.41x faster                                               |
| Geometric mean | (ref)                                                        | 1.27x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 629 ms: 2.54x faster                                                |
| async_tree_none         | 692 ms                                                       | 282 ms: 2.45x faster                                                |
| async_tree_memoization  | 819 ms                                                       | 344 ms: 2.38x faster                                                |
| async_tree_cpu_io_mixed | 936 ms                                                       | 511 ms: 1.83x faster                                                |
| Geometric mean          | (ref)                                                        | 2.28x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 111 ms                                                       | 71.8 ms: 1.55x faster                                               |
| nbody          | 134 ms                                                       | 89.3 ms: 1.50x faster                                               |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                |
| Geometric mean | (ref)                                                        | 1.35x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 136 ms: 1.40x faster                                                |
| regex_dna      | 261 ms                                                       | 244 ms: 1.07x faster                                                |
| regex_v8       | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                               |
| regex_effbot   | 3.09 ms                                                      | 3.26 ms: 1.06x slower                                               |
| Geometric mean | (ref)                                                        | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 207 us: 1.51x faster                                                |
| tomli_loads          | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                              |
| pickle_pure_python   | 455 us                                                       | 328 us: 1.39x faster                                                |
| xml_etree_process    | 75.9 ms                                                      | 58.8 ms: 1.29x faster                                               |
| json_loads           | 30.3 us                                                      | 23.6 us: 1.28x faster                                               |
| json_dumps           | 14.5 ms                                                      | 11.4 ms: 1.27x faster                                               |
| xml_etree_parse      | 160 ms                                                       | 139 ms: 1.15x faster                                                |
| xml_etree_iterparse  | 110 ms                                                       | 97.3 ms: 1.14x faster                                               |
| xml_etree_generate   | 92.3 ms                                                      | 83.3 ms: 1.11x faster                                               |
| Geometric mean       | (ref)                                                        | 1.28x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                               |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                               |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.9 ms: 1.40x faster                                               |
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                               |
| genshi_text     | 31.4 ms                                                      | 24.0 ms: 1.31x faster                                               |
| genshi_xml      | 63.3 ms                                                      | 53.8 ms: 1.18x faster                                               |
| Geometric mean  | (ref)                                                        | 1.31x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 175 us: 3.07x faster                                                |
| async_tree_io            | 1.60 sec                                                     | 629 ms: 2.54x faster                                                |
| async_tree_none          | 692 ms                                                       | 282 ms: 2.45x faster                                                |
| async_tree_memoization   | 819 ms                                                       | 344 ms: 2.38x faster                                                |
| deltablue                | 7.50 ms                                                      | 3.38 ms: 2.22x faster                                               |
| go                       | 262 ms                                                       | 126 ms: 2.07x faster                                                |
| generators               | 57.3 ms                                                      | 28.4 ms: 2.02x faster                                               |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 511 ms: 1.83x faster                                                |
| raytrace                 | 489 ms                                                       | 268 ms: 1.82x faster                                                |
| pylint                   | 566 ms                                                       | 317 ms: 1.79x faster                                                |
| scimark_lu               | 167 ms                                                       | 94.1 ms: 1.77x faster                                               |
| chaos                    | 109 ms                                                       | 61.9 ms: 1.75x faster                                               |
| richards_super           | 90.6 ms                                                      | 51.9 ms: 1.74x faster                                               |
| scimark_monte_carlo      | 107 ms                                                       | 62.0 ms: 1.73x faster                                               |
| logging_silent           | 167 ns                                                       | 98.3 ns: 1.70x faster                                               |
| sqlglot_parse            | 2.24 ms                                                      | 1.33 ms: 1.68x faster                                               |
| deepcopy                 | 468 us                                                       | 281 us: 1.67x faster                                                |
| deepcopy_memo            | 49.8 us                                                      | 30.0 us: 1.66x faster                                               |
| crypto_pyaes             | 119 ms                                                       | 72.1 ms: 1.65x faster                                               |
| richards                 | 75.1 ms                                                      | 46.0 ms: 1.63x faster                                               |
| scimark_sor              | 180 ms                                                       | 111 ms: 1.63x faster                                                |
| pyflate                  | 733 ms                                                       | 453 ms: 1.62x faster                                                |
| sqlglot_transpile        | 2.68 ms                                                      | 1.73 ms: 1.55x faster                                               |
| float                    | 111 ms                                                       | 71.8 ms: 1.55x faster                                               |
| hexiom                   | 9.42 ms                                                      | 6.09 ms: 1.55x faster                                               |
| spectral_norm            | 139 ms                                                       | 90.0 ms: 1.55x faster                                               |
| comprehensions           | 26.7 us                                                      | 17.5 us: 1.53x faster                                               |
| unpickle_pure_python     | 312 us                                                       | 207 us: 1.51x faster                                                |
| nbody                    | 134 ms                                                       | 89.3 ms: 1.50x faster                                               |
| coroutines               | 30.3 ms                                                      | 20.9 ms: 1.45x faster                                               |
| html5lib                 | 94.6 ms                                                      | 67.2 ms: 1.41x faster                                               |
| tomli_loads              | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                              |
| django_template          | 50.2 ms                                                      | 35.9 ms: 1.40x faster                                               |
| regex_compile            | 190 ms                                                       | 136 ms: 1.40x faster                                                |
| logging_simple           | 8.88 us                                                      | 6.39 us: 1.39x faster                                               |
| pickle_pure_python       | 455 us                                                       | 328 us: 1.39x faster                                                |
| pprint_pformat           | 2.15 sec                                                     | 1.57 sec: 1.38x faster                                              |
| thrift                   | 1.18 ms                                                      | 857 us: 1.37x faster                                                |
| pprint_safe_repr         | 1.05 sec                                                     | 770 ms: 1.36x faster                                                |
| deepcopy_reduce          | 4.01 us                                                      | 2.94 us: 1.36x faster                                               |
| logging_format           | 9.64 us                                                      | 7.08 us: 1.36x faster                                               |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                              |
| mako                     | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                               |
| sqlalchemy_declarative   | 190 ms                                                       | 143 ms: 1.33x faster                                                |
| fannkuch                 | 483 ms                                                       | 365 ms: 1.32x faster                                                |
| pathlib                  | 21.4 ms                                                      | 16.3 ms: 1.31x faster                                               |
| genshi_text              | 31.4 ms                                                      | 24.0 ms: 1.31x faster                                               |
| xml_etree_process        | 75.9 ms                                                      | 58.8 ms: 1.29x faster                                               |
| json_loads               | 30.3 us                                                      | 23.6 us: 1.28x faster                                               |
| json_dumps               | 14.5 ms                                                      | 11.4 ms: 1.27x faster                                               |
| nqueens                  | 115 ms                                                       | 90.5 ms: 1.27x faster                                               |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.9 ms: 1.27x faster                                               |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                |
| sqlglot_normalize        | 144 ms                                                       | 114 ms: 1.26x faster                                                |
| bench_thread_pool        | 1.14 ms                                                      | 915 us: 1.25x faster                                                |
| 2to3                     | 350 ms                                                       | 282 ms: 1.24x faster                                                |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                |
| dulwich_log              | 81.1 ms                                                      | 65.9 ms: 1.23x faster                                               |
| sqlglot_optimize         | 70.1 ms                                                      | 57.3 ms: 1.22x faster                                               |
| sympy_integrate          | 28.2 ms                                                      | 23.1 ms: 1.22x faster                                               |
| scimark_fft              | 361 ms                                                       | 298 ms: 1.21x faster                                                |
| mdp                      | 3.01 sec                                                     | 2.48 sec: 1.21x faster                                              |
| sympy_expand             | 600 ms                                                       | 497 ms: 1.21x faster                                                |
| docutils                 | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                              |
| genshi_xml               | 63.3 ms                                                      | 53.8 ms: 1.18x faster                                               |
| json                     | 5.86 ms                                                      | 5.09 ms: 1.15x faster                                               |
| xml_etree_parse          | 160 ms                                                       | 139 ms: 1.15x faster                                                |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.45 ms: 1.14x faster                                               |
| xml_etree_iterparse      | 110 ms                                                       | 97.3 ms: 1.14x faster                                               |
| xml_etree_generate       | 92.3 ms                                                      | 83.3 ms: 1.11x faster                                               |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                                |
| regex_dna                | 261 ms                                                       | 244 ms: 1.07x faster                                                |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                |
| sqlite_synth             | 2.99 us                                                      | 2.86 us: 1.04x faster                                               |
| regex_v8                 | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                               |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                |
| async_generators         | 421 ms                                                       | 431 ms: 1.02x slower                                                |
| regex_effbot             | 3.09 ms                                                      | 3.26 ms: 1.06x slower                                               |
| mypy2                    | 933 ms                                                       | 1.02 sec: 1.09x slower                                              |
| telco                    | 7.23 ms                                                      | 7.92 ms: 1.10x slower                                               |
| coverage                 | 63.3 ms                                                      | 77.4 ms: 1.22x slower                                               |
| python_startup_no_site   | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                               |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                               |
| create_gc_cycles         | 1.76 ms                                                      | 2.75 ms: 1.56x slower                                               |
| gc_traversal             | 3.42 ms                                                      | 6.06 ms: 1.77x slower                                               |
| bench_mp_pool            | 6.37 ms                                                      | 1.58 sec: 247.19x slower                                            |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                        |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250107-3.14.0a3+-f098037/bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.347x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.29x
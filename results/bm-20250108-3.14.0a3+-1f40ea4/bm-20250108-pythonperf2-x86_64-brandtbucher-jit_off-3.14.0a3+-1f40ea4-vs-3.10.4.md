# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_off
- machine: linux-x86_64
- commit hash: 1f40ea4
- commit date: 2025-01-08
- overall geometric mean: 1.355x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                                  |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                |
| html5lib       | 94.6 ms                                                      | 67.5 ms: 1.40x faster                                                 |
| Geometric mean | (ref)                                                        | 1.27x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 633 ms: 2.53x faster                                                  |
| async_tree_none         | 692 ms                                                       | 282 ms: 2.45x faster                                                  |
| async_tree_memoization  | 819 ms                                                       | 347 ms: 2.36x faster                                                  |
| async_tree_cpu_io_mixed | 936 ms                                                       | 513 ms: 1.83x faster                                                  |
| Geometric mean          | (ref)                                                        | 2.27x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 111 ms                                                       | 73.0 ms: 1.52x faster                                                 |
| nbody          | 134 ms                                                       | 89.3 ms: 1.50x faster                                                 |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                        | 1.34x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 135 ms: 1.40x faster                                                  |
| regex_dna      | 261 ms                                                       | 233 ms: 1.12x faster                                                  |
| regex_v8       | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                 |
| regex_effbot   | 3.09 ms                                                      | 3.15 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                        | 1.13x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 207 us: 1.51x faster                                                  |
| tomli_loads          | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                |
| pickle_pure_python   | 455 us                                                       | 328 us: 1.39x faster                                                  |
| xml_etree_process    | 75.9 ms                                                      | 58.0 ms: 1.31x faster                                                 |
| json_loads           | 30.3 us                                                      | 24.0 us: 1.27x faster                                                 |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                 |
| xml_etree_parse      | 160 ms                                                       | 135 ms: 1.19x faster                                                  |
| xml_etree_iterparse  | 110 ms                                                       | 96.4 ms: 1.15x faster                                                 |
| xml_etree_generate   | 92.3 ms                                                      | 82.2 ms: 1.12x faster                                                 |
| Geometric mean       | (ref)                                                        | 1.28x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                 |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                 |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.7 ms: 1.41x faster                                                 |
| mako            | 14.7 ms                                                      | 11.0 ms: 1.33x faster                                                 |
| genshi_text     | 31.4 ms                                                      | 23.9 ms: 1.31x faster                                                 |
| genshi_xml      | 63.3 ms                                                      | 51.8 ms: 1.22x faster                                                 |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 175 us: 3.07x faster                                                  |
| async_tree_io            | 1.60 sec                                                     | 633 ms: 2.53x faster                                                  |
| async_tree_none          | 692 ms                                                       | 282 ms: 2.45x faster                                                  |
| async_tree_memoization   | 819 ms                                                       | 347 ms: 2.36x faster                                                  |
| deltablue                | 7.50 ms                                                      | 3.40 ms: 2.21x faster                                                 |
| go                       | 262 ms                                                       | 128 ms: 2.05x faster                                                  |
| generators               | 57.3 ms                                                      | 28.5 ms: 2.01x faster                                                 |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 513 ms: 1.83x faster                                                  |
| raytrace                 | 489 ms                                                       | 271 ms: 1.81x faster                                                  |
| pylint                   | 566 ms                                                       | 319 ms: 1.78x faster                                                  |
| scimark_lu               | 167 ms                                                       | 94.2 ms: 1.77x faster                                                 |
| chaos                    | 109 ms                                                       | 63.0 ms: 1.72x faster                                                 |
| scimark_monte_carlo      | 107 ms                                                       | 62.4 ms: 1.72x faster                                                 |
| richards_super           | 90.6 ms                                                      | 53.1 ms: 1.71x faster                                                 |
| logging_silent           | 167 ns                                                       | 98.1 ns: 1.71x faster                                                 |
| deepcopy_memo            | 49.8 us                                                      | 29.4 us: 1.69x faster                                                 |
| sqlglot_parse            | 2.24 ms                                                      | 1.33 ms: 1.69x faster                                                 |
| deepcopy                 | 468 us                                                       | 283 us: 1.66x faster                                                  |
| scimark_sor              | 180 ms                                                       | 110 ms: 1.64x faster                                                  |
| crypto_pyaes             | 119 ms                                                       | 73.3 ms: 1.63x faster                                                 |
| richards                 | 75.1 ms                                                      | 46.4 ms: 1.62x faster                                                 |
| pyflate                  | 733 ms                                                       | 456 ms: 1.61x faster                                                  |
| spectral_norm            | 139 ms                                                       | 87.5 ms: 1.59x faster                                                 |
| sqlglot_transpile        | 2.68 ms                                                      | 1.72 ms: 1.56x faster                                                 |
| hexiom                   | 9.42 ms                                                      | 6.09 ms: 1.55x faster                                                 |
| float                    | 111 ms                                                       | 73.0 ms: 1.52x faster                                                 |
| comprehensions           | 26.7 us                                                      | 17.6 us: 1.52x faster                                                 |
| unpickle_pure_python     | 312 us                                                       | 207 us: 1.51x faster                                                  |
| nbody                    | 134 ms                                                       | 89.3 ms: 1.50x faster                                                 |
| coroutines               | 30.3 ms                                                      | 20.8 ms: 1.45x faster                                                 |
| tomli_loads              | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                |
| django_template          | 50.2 ms                                                      | 35.7 ms: 1.41x faster                                                 |
| regex_compile            | 190 ms                                                       | 135 ms: 1.40x faster                                                  |
| html5lib                 | 94.6 ms                                                      | 67.5 ms: 1.40x faster                                                 |
| logging_simple           | 8.88 us                                                      | 6.37 us: 1.39x faster                                                 |
| pickle_pure_python       | 455 us                                                       | 328 us: 1.39x faster                                                  |
| logging_format           | 9.64 us                                                      | 6.96 us: 1.38x faster                                                 |
| pprint_pformat           | 2.15 sec                                                     | 1.57 sec: 1.38x faster                                                |
| pprint_safe_repr         | 1.05 sec                                                     | 770 ms: 1.36x faster                                                  |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                |
| thrift                   | 1.18 ms                                                      | 866 us: 1.36x faster                                                  |
| deepcopy_reduce          | 4.01 us                                                      | 2.96 us: 1.35x faster                                                 |
| fannkuch                 | 483 ms                                                       | 358 ms: 1.35x faster                                                  |
| mako                     | 14.7 ms                                                      | 11.0 ms: 1.33x faster                                                 |
| pathlib                  | 21.4 ms                                                      | 16.1 ms: 1.33x faster                                                 |
| sqlalchemy_declarative   | 190 ms                                                       | 143 ms: 1.32x faster                                                  |
| genshi_text              | 31.4 ms                                                      | 23.9 ms: 1.31x faster                                                 |
| xml_etree_process        | 75.9 ms                                                      | 58.0 ms: 1.31x faster                                                 |
| nqueens                  | 115 ms                                                       | 90.1 ms: 1.28x faster                                                 |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                  |
| json_loads               | 30.3 us                                                      | 24.0 us: 1.27x faster                                                 |
| sqlglot_normalize        | 144 ms                                                       | 114 ms: 1.26x faster                                                  |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                 |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.0 ms: 1.26x faster                                                 |
| 2to3                     | 350 ms                                                       | 282 ms: 1.24x faster                                                  |
| sympy_str                | 360 ms                                                       | 293 ms: 1.23x faster                                                  |
| bench_thread_pool        | 1.14 ms                                                      | 932 us: 1.22x faster                                                  |
| genshi_xml               | 63.3 ms                                                      | 51.8 ms: 1.22x faster                                                 |
| sqlglot_optimize         | 70.1 ms                                                      | 57.6 ms: 1.22x faster                                                 |
| mdp                      | 3.01 sec                                                     | 2.47 sec: 1.22x faster                                                |
| dulwich_log              | 81.1 ms                                                      | 66.7 ms: 1.22x faster                                                 |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.21x faster                                                 |
| sympy_expand             | 600 ms                                                       | 502 ms: 1.20x faster                                                  |
| scimark_fft              | 361 ms                                                       | 304 ms: 1.19x faster                                                  |
| xml_etree_parse          | 160 ms                                                       | 135 ms: 1.19x faster                                                  |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                |
| json                     | 5.86 ms                                                      | 5.11 ms: 1.15x faster                                                 |
| xml_etree_iterparse      | 110 ms                                                       | 96.4 ms: 1.15x faster                                                 |
| xml_etree_generate       | 92.3 ms                                                      | 82.2 ms: 1.12x faster                                                 |
| regex_dna                | 261 ms                                                       | 233 ms: 1.12x faster                                                  |
| meteor_contest           | 138 ms                                                       | 125 ms: 1.11x faster                                                  |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.59 ms: 1.11x faster                                                 |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                  |
| regex_v8                 | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                 |
| sqlite_synth             | 2.99 us                                                      | 2.85 us: 1.05x faster                                                 |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                  |
| regex_effbot             | 3.09 ms                                                      | 3.15 ms: 1.02x slower                                                 |
| async_generators         | 421 ms                                                       | 436 ms: 1.04x slower                                                  |
| telco                    | 7.23 ms                                                      | 7.68 ms: 1.06x slower                                                 |
| coverage                 | 63.3 ms                                                      | 77.7 ms: 1.23x slower                                                 |
| python_startup_no_site   | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                 |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                 |
| create_gc_cycles         | 1.76 ms                                                      | 2.74 ms: 1.55x slower                                                 |
| gc_traversal             | 3.42 ms                                                      | 6.25 ms: 1.83x slower                                                 |
| bench_mp_pool            | 6.37 ms                                                      | 1.52 sec: 238.30x slower                                              |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                          |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250108-3.14.0a3+-1f40ea4/bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.355x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.28x
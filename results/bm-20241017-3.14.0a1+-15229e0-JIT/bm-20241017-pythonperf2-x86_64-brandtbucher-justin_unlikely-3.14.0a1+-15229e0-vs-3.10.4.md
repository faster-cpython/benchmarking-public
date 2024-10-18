# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-x86_64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 317 ms: 1.11x faster                                                          |
| docutils       | 3.41 sec                                                     | 3.21 sec: 1.06x faster                                                        |
| html5lib       | 94.6 ms                                                      | 70.3 ms: 1.35x faster                                                         |
| tornado_http   | 157 ms                                                       | 124 ms: 1.27x faster                                                          |
| Geometric mean | (ref)                                                        | 1.19x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 333 ms: 2.08x faster                                                          |
| async_tree_memoization  | 819 ms                                                       | 408 ms: 2.01x faster                                                          |
| async_tree_io           | 1.60 sec                                                     | 821 ms: 1.95x faster                                                          |
| async_tree_cpu_io_mixed | 936 ms                                                       | 576 ms: 1.63x faster                                                          |
| Geometric mean          | (ref)                                                        | 1.91x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 84.6 ms: 1.59x faster                                                         |
| float          | 111 ms                                                       | 78.7 ms: 1.41x faster                                                         |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                          |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 153 ms: 1.24x faster                                                          |
| regex_dna      | 261 ms                                                       | 231 ms: 1.13x faster                                                          |
| regex_v8       | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.42 ms: 1.11x slower                                                         |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 223 us: 1.40x faster                                                          |
| pickle_pure_python   | 455 us                                                       | 332 us: 1.37x faster                                                          |
| tomli_loads          | 2.92 sec                                                     | 2.13 sec: 1.37x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 56.9 ms: 1.33x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                         |
| json_loads           | 30.3 us                                                      | 24.1 us: 1.26x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 81.4 ms: 1.13x faster                                                         |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                          |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                          |
| unpickle_list        | 4.65 us                                                      | 4.90 us: 1.05x slower                                                         |
| pickle               | 9.89 us                                                      | 10.6 us: 1.07x slower                                                         |
| unpickle             | 13.5 us                                                      | 14.8 us: 1.09x slower                                                         |
| pickle_dict          | 29.5 us                                                      | 32.9 us: 1.11x slower                                                         |
| pickle_list          | 4.12 us                                                      | 4.60 us: 1.12x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                         |
| python_startup         | 11.5 ms                                                      | 15.0 ms: 1.30x slower                                                         |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.57 ms: 1.54x faster                                                         |
| django_template | 50.2 ms                                                      | 42.7 ms: 1.18x faster                                                         |
| genshi_text     | 31.4 ms                                                      | 28.8 ms: 1.09x faster                                                         |
| Geometric mean  | (ref)                                                        | 1.19x faster                                                                  |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 182 us: 2.94x faster                                                          |
| deltablue                | 7.50 ms                                                      | 3.30 ms: 2.27x faster                                                         |
| async_tree_none          | 692 ms                                                       | 333 ms: 2.08x faster                                                          |
| asyncio_tcp              | 779 ms                                                       | 376 ms: 2.07x faster                                                          |
| async_tree_memoization   | 819 ms                                                       | 408 ms: 2.01x faster                                                          |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.59 sec: 1.96x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 821 ms: 1.95x faster                                                          |
| logging_silent           | 167 ns                                                       | 91.4 ns: 1.83x faster                                                         |
| richards_super           | 90.6 ms                                                      | 49.8 ms: 1.82x faster                                                         |
| scimark_lu               | 167 ms                                                       | 94.7 ms: 1.76x faster                                                         |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.74x faster                                                          |
| richards                 | 75.1 ms                                                      | 44.5 ms: 1.69x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 29.7 us: 1.68x faster                                                         |
| go                       | 262 ms                                                       | 156 ms: 1.67x faster                                                          |
| crypto_pyaes             | 119 ms                                                       | 71.4 ms: 1.67x faster                                                         |
| chaos                    | 109 ms                                                       | 65.2 ms: 1.66x faster                                                         |
| raytrace                 | 489 ms                                                       | 299 ms: 1.63x faster                                                          |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 576 ms: 1.63x faster                                                          |
| pyflate                  | 733 ms                                                       | 460 ms: 1.59x faster                                                          |
| nbody                    | 134 ms                                                       | 84.6 ms: 1.59x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 69.7 ms: 1.54x faster                                                         |
| mako                     | 14.7 ms                                                      | 9.57 ms: 1.54x faster                                                         |
| spectral_norm            | 139 ms                                                       | 93.3 ms: 1.49x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.51 ms: 1.48x faster                                                         |
| generators               | 57.3 ms                                                      | 38.9 ms: 1.47x faster                                                         |
| deepcopy                 | 468 us                                                       | 319 us: 1.47x faster                                                          |
| comprehensions           | 26.7 us                                                      | 18.6 us: 1.44x faster                                                         |
| float                    | 111 ms                                                       | 78.7 ms: 1.41x faster                                                         |
| coroutines               | 30.3 ms                                                      | 21.6 ms: 1.40x faster                                                         |
| unpickle_pure_python     | 312 us                                                       | 223 us: 1.40x faster                                                          |
| pickle_pure_python       | 455 us                                                       | 332 us: 1.37x faster                                                          |
| logging_format           | 9.64 us                                                      | 7.04 us: 1.37x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.13 sec: 1.37x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.53 us: 1.36x faster                                                         |
| sqlglot_transpile        | 2.68 ms                                                      | 1.98 ms: 1.36x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.35x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 70.3 ms: 1.35x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.34x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 56.9 ms: 1.33x faster                                                         |
| pylint                   | 566 ms                                                       | 425 ms: 1.33x faster                                                          |
| pprint_safe_repr         | 1.05 sec                                                     | 788 ms: 1.33x faster                                                          |
| fannkuch                 | 483 ms                                                       | 364 ms: 1.33x faster                                                          |
| hexiom                   | 9.42 ms                                                      | 7.18 ms: 1.31x faster                                                         |
| thrift                   | 1.18 ms                                                      | 898 us: 1.31x faster                                                          |
| json_dumps               | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 3.11 us: 1.29x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.30 sec: 1.28x faster                                                        |
| tornado_http             | 157 ms                                                       | 124 ms: 1.27x faster                                                          |
| json_loads               | 30.3 us                                                      | 24.1 us: 1.26x faster                                                         |
| scimark_fft              | 361 ms                                                       | 288 ms: 1.26x faster                                                          |
| dulwich_log              | 81.1 ms                                                      | 65.0 ms: 1.25x faster                                                         |
| regex_compile            | 190 ms                                                       | 153 ms: 1.24x faster                                                          |
| bench_thread_pool        | 1.14 ms                                                      | 955 us: 1.19x faster                                                          |
| django_template          | 50.2 ms                                                      | 42.7 ms: 1.18x faster                                                         |
| json                     | 5.86 ms                                                      | 5.03 ms: 1.17x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.41 ms: 1.15x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.62 sec: 1.15x faster                                                        |
| nqueens                  | 115 ms                                                       | 101 ms: 1.13x faster                                                          |
| xml_etree_generate       | 92.3 ms                                                      | 81.4 ms: 1.13x faster                                                         |
| regex_dna                | 261 ms                                                       | 231 ms: 1.13x faster                                                          |
| sympy_expand             | 600 ms                                                       | 535 ms: 1.12x faster                                                          |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                          |
| sympy_str                | 360 ms                                                       | 322 ms: 1.12x faster                                                          |
| sqlite_synth             | 2.99 us                                                      | 2.69 us: 1.11x faster                                                         |
| async_generators         | 421 ms                                                       | 380 ms: 1.11x faster                                                          |
| 2to3                     | 350 ms                                                       | 317 ms: 1.11x faster                                                          |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                          |
| sympy_sum                | 193 ms                                                       | 176 ms: 1.09x faster                                                          |
| genshi_text              | 31.4 ms                                                      | 28.8 ms: 1.09x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 133 ms: 1.08x faster                                                          |
| pidigits                 | 271 ms                                                       | 252 ms: 1.08x faster                                                          |
| docutils                 | 3.41 sec                                                     | 3.21 sec: 1.06x faster                                                        |
| meteor_contest           | 138 ms                                                       | 135 ms: 1.02x faster                                                          |
| sympy_integrate          | 28.2 ms                                                      | 27.6 ms: 1.02x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 383 ms: 1.02x faster                                                          |
| sqlglot_optimize         | 70.1 ms                                                      | 69.9 ms: 1.00x faster                                                         |
| unpickle_list            | 4.65 us                                                      | 4.90 us: 1.05x slower                                                         |
| telco                    | 7.23 ms                                                      | 7.74 ms: 1.07x slower                                                         |
| pickle                   | 9.89 us                                                      | 10.6 us: 1.07x slower                                                         |
| unpickle                 | 13.5 us                                                      | 14.8 us: 1.09x slower                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.42 ms: 1.11x slower                                                         |
| pickle_dict              | 29.5 us                                                      | 32.9 us: 1.11x slower                                                         |
| pickle_list              | 4.12 us                                                      | 4.60 us: 1.12x slower                                                         |
| python_startup_no_site   | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                         |
| coverage                 | 63.3 ms                                                      | 79.8 ms: 1.26x slower                                                         |
| python_startup           | 11.5 ms                                                      | 15.0 ms: 1.30x slower                                                         |
| unpack_sequence          | 59.9 ns                                                      | 90.0 ns: 1.50x slower                                                         |
| gc_traversal             | 3.42 ms                                                      | 5.35 ms: 1.57x slower                                                         |
| create_gc_cycles         | 1.76 ms                                                      | 2.92 ms: 1.66x slower                                                         |
| bench_mp_pool            | 6.37 ms                                                      | 3.14 sec: 493.00x slower                                                      |
| Geometric mean           | (ref)                                                        | 1.18x faster                                                                  |

Benchmark hidden because not significant (1): genshi_xml
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.35x
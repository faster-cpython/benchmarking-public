# Results vs. 3.10.4

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.31x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                               |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                             |
| html5lib       | 94.6 ms                                                      | 70.9 ms: 1.33x faster                                              |
| tornado_http   | 157 ms                                                       | 116 ms: 1.36x faster                                               |
| Geometric mean | (ref)                                                        | 1.27x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 319 ms: 2.17x faster                                               |
| async_tree_memoization  | 819 ms                                                       | 397 ms: 2.06x faster                                               |
| async_tree_io           | 1.60 sec                                                     | 818 ms: 1.95x faster                                               |
| async_tree_cpu_io_mixed | 936 ms                                                       | 569 ms: 1.64x faster                                               |
| Geometric mean          | (ref)                                                        | 1.95x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 89.1 ms: 1.51x faster                                              |
| float          | 111 ms                                                       | 79.6 ms: 1.40x faster                                              |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                               |
| Geometric mean | (ref)                                                        | 1.31x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.37x faster                                               |
| regex_dna      | 261 ms                                                       | 237 ms: 1.10x faster                                               |
| regex_v8       | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                              |
| regex_effbot   | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                              |
| Geometric mean | (ref)                                                        | 1.10x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 216 us: 1.44x faster                                               |
| pickle_pure_python   | 455 us                                                       | 323 us: 1.41x faster                                               |
| json_dumps           | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                              |
| xml_etree_process    | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                              |
| json_loads           | 30.3 us                                                      | 24.8 us: 1.22x faster                                              |
| tomli_loads          | 2.92 sec                                                     | 2.58 sec: 1.13x faster                                             |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                               |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.09x faster                                               |
| xml_etree_generate   | 92.3 ms                                                      | 84.8 ms: 1.09x faster                                              |
| pickle_list          | 4.12 us                                                      | 4.18 us: 1.01x slower                                              |
| pickle_dict          | 29.5 us                                                      | 30.3 us: 1.03x slower                                              |
| unpickle_list        | 4.65 us                                                      | 4.81 us: 1.03x slower                                              |
| pickle               | 9.89 us                                                      | 10.3 us: 1.04x slower                                              |
| unpickle             | 13.5 us                                                      | 15.5 us: 1.15x slower                                              |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                              |
| python_startup_no_site | 7.33 ms                                                      | 8.98 ms: 1.23x slower                                              |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.6 ms: 1.39x faster                                              |
| genshi_text     | 31.4 ms                                                      | 24.8 ms: 1.27x faster                                              |
| django_template | 50.2 ms                                                      | 39.6 ms: 1.27x faster                                              |
| genshi_xml      | 63.3 ms                                                      | 55.4 ms: 1.14x faster                                              |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 172 us: 3.11x faster                                               |
| deltablue                | 7.50 ms                                                      | 3.42 ms: 2.19x faster                                              |
| async_tree_none          | 692 ms                                                       | 319 ms: 2.17x faster                                               |
| asyncio_tcp              | 779 ms                                                       | 371 ms: 2.10x faster                                               |
| async_tree_memoization   | 819 ms                                                       | 397 ms: 2.06x faster                                               |
| generators               | 57.3 ms                                                      | 28.8 ms: 1.99x faster                                              |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                             |
| async_tree_io            | 1.60 sec                                                     | 818 ms: 1.95x faster                                               |
| go                       | 262 ms                                                       | 135 ms: 1.94x faster                                               |
| raytrace                 | 489 ms                                                       | 275 ms: 1.78x faster                                               |
| chaos                    | 109 ms                                                       | 62.5 ms: 1.74x faster                                              |
| scimark_lu               | 167 ms                                                       | 99.2 ms: 1.68x faster                                              |
| logging_silent           | 167 ns                                                       | 100 ns: 1.67x faster                                               |
| deepcopy_memo            | 49.8 us                                                      | 30.1 us: 1.65x faster                                              |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 569 ms: 1.64x faster                                               |
| crypto_pyaes             | 119 ms                                                       | 73.2 ms: 1.63x faster                                              |
| richards_super           | 90.6 ms                                                      | 55.8 ms: 1.63x faster                                              |
| pylint                   | 566 ms                                                       | 350 ms: 1.62x faster                                               |
| deepcopy                 | 468 us                                                       | 291 us: 1.61x faster                                               |
| scimark_monte_carlo      | 107 ms                                                       | 67.4 ms: 1.59x faster                                              |
| sqlglot_parse            | 2.24 ms                                                      | 1.43 ms: 1.57x faster                                              |
| pyflate                  | 733 ms                                                       | 483 ms: 1.52x faster                                               |
| comprehensions           | 26.7 us                                                      | 17.7 us: 1.51x faster                                              |
| nbody                    | 134 ms                                                       | 89.1 ms: 1.51x faster                                              |
| hexiom                   | 9.42 ms                                                      | 6.26 ms: 1.50x faster                                              |
| richards                 | 75.1 ms                                                      | 50.0 ms: 1.50x faster                                              |
| sqlglot_transpile        | 2.68 ms                                                      | 1.81 ms: 1.48x faster                                              |
| unpickle_pure_python     | 312 us                                                       | 216 us: 1.44x faster                                               |
| spectral_norm            | 139 ms                                                       | 97.6 ms: 1.43x faster                                              |
| pickle_pure_python       | 455 us                                                       | 323 us: 1.41x faster                                               |
| scimark_sor              | 180 ms                                                       | 129 ms: 1.40x faster                                               |
| float                    | 111 ms                                                       | 79.6 ms: 1.40x faster                                              |
| mako                     | 14.7 ms                                                      | 10.6 ms: 1.39x faster                                              |
| coroutines               | 30.3 ms                                                      | 21.9 ms: 1.38x faster                                              |
| bench_mp_pool            | 6.37 ms                                                      | 4.63 ms: 1.38x faster                                              |
| regex_compile            | 190 ms                                                       | 139 ms: 1.37x faster                                               |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                             |
| tornado_http             | 157 ms                                                       | 116 ms: 1.36x faster                                               |
| deepcopy_reduce          | 4.01 us                                                      | 2.97 us: 1.35x faster                                              |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.35x faster                                              |
| logging_simple           | 8.88 us                                                      | 6.58 us: 1.35x faster                                              |
| logging_format           | 9.64 us                                                      | 7.15 us: 1.35x faster                                              |
| thrift                   | 1.18 ms                                                      | 875 us: 1.34x faster                                               |
| html5lib                 | 94.6 ms                                                      | 70.9 ms: 1.33x faster                                              |
| json_dumps               | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                              |
| fannkuch                 | 483 ms                                                       | 365 ms: 1.32x faster                                               |
| pprint_safe_repr         | 1.05 sec                                                     | 815 ms: 1.29x faster                                               |
| pprint_pformat           | 2.15 sec                                                     | 1.68 sec: 1.28x faster                                             |
| xml_etree_process        | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                              |
| bench_thread_pool        | 1.14 ms                                                      | 894 us: 1.28x faster                                               |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                               |
| genshi_text              | 31.4 ms                                                      | 24.8 ms: 1.27x faster                                              |
| django_template          | 50.2 ms                                                      | 39.6 ms: 1.27x faster                                              |
| nqueens                  | 115 ms                                                       | 91.4 ms: 1.26x faster                                              |
| 2to3                     | 350 ms                                                       | 282 ms: 1.24x faster                                               |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                               |
| json_loads               | 30.3 us                                                      | 24.8 us: 1.22x faster                                              |
| sympy_integrate          | 28.2 ms                                                      | 23.1 ms: 1.22x faster                                              |
| dulwich_log              | 81.1 ms                                                      | 66.5 ms: 1.22x faster                                              |
| sympy_expand             | 600 ms                                                       | 497 ms: 1.21x faster                                               |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.20x faster                                               |
| mdp                      | 3.01 sec                                                     | 2.51 sec: 1.20x faster                                             |
| sqlglot_optimize         | 70.1 ms                                                      | 59.1 ms: 1.19x faster                                              |
| scimark_fft              | 361 ms                                                       | 307 ms: 1.18x faster                                               |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                             |
| async_generators         | 421 ms                                                       | 362 ms: 1.16x faster                                               |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.40 ms: 1.15x faster                                              |
| genshi_xml               | 63.3 ms                                                      | 55.4 ms: 1.14x faster                                              |
| tomli_loads              | 2.92 sec                                                     | 2.58 sec: 1.13x faster                                             |
| json                     | 5.86 ms                                                      | 5.23 ms: 1.12x faster                                              |
| regex_dna                | 261 ms                                                       | 237 ms: 1.10x faster                                               |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.10x faster                                               |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                               |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.09x faster                                               |
| xml_etree_generate       | 92.3 ms                                                      | 84.8 ms: 1.09x faster                                              |
| sqlite_synth             | 2.99 us                                                      | 2.75 us: 1.09x faster                                              |
| regex_v8                 | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                              |
| unpack_sequence          | 59.9 ns                                                      | 55.2 ns: 1.09x faster                                              |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                               |
| pickle_list              | 4.12 us                                                      | 4.18 us: 1.01x slower                                              |
| pickle_dict              | 29.5 us                                                      | 30.3 us: 1.03x slower                                              |
| unpickle_list            | 4.65 us                                                      | 4.81 us: 1.03x slower                                              |
| pickle                   | 9.89 us                                                      | 10.3 us: 1.04x slower                                              |
| create_gc_cycles         | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                              |
| regex_effbot             | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                              |
| unpickle                 | 13.5 us                                                      | 15.5 us: 1.15x slower                                              |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                              |
| telco                    | 7.23 ms                                                      | 8.45 ms: 1.17x slower                                              |
| python_startup_no_site   | 7.33 ms                                                      | 8.98 ms: 1.23x slower                                              |
| coverage                 | 63.3 ms                                                      | 86.1 ms: 1.36x slower                                              |
| gc_traversal             | 3.42 ms                                                      | 4.70 ms: 1.38x slower                                              |
| Geometric mean           | (ref)                                                        | 1.31x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.13x
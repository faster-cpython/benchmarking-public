# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: linux-x86_64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 309 ms: 1.13x faster                                                          |
| docutils       | 3.41 sec                                                     | 3.18 sec: 1.07x faster                                                        |
| html5lib       | 94.6 ms                                                      | 70.6 ms: 1.34x faster                                                         |
| tornado_http   | 157 ms                                                       | 122 ms: 1.28x faster                                                          |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 323 ms: 2.14x faster                                                          |
| async_tree_memoization  | 819 ms                                                       | 404 ms: 2.03x faster                                                          |
| async_tree_io           | 1.60 sec                                                     | 802 ms: 1.99x faster                                                          |
| async_tree_cpu_io_mixed | 936 ms                                                       | 575 ms: 1.63x faster                                                          |
| Geometric mean          | (ref)                                                        | 1.94x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 83.5 ms: 1.61x faster                                                         |
| float          | 111 ms                                                       | 75.6 ms: 1.47x faster                                                         |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                          |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 149 ms: 1.27x faster                                                          |
| regex_dna      | 261 ms                                                       | 236 ms: 1.11x faster                                                          |
| regex_v8       | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                         |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 217 us: 1.44x faster                                                          |
| pickle_pure_python   | 455 us                                                       | 330 us: 1.38x faster                                                          |
| tomli_loads          | 2.92 sec                                                     | 2.13 sec: 1.37x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 56.5 ms: 1.34x faster                                                         |
| json_loads           | 30.3 us                                                      | 24.0 us: 1.26x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 79.9 ms: 1.15x faster                                                         |
| xml_etree_parse      | 160 ms                                                       | 142 ms: 1.12x faster                                                          |
| xml_etree_iterparse  | 110 ms                                                       | 99.5 ms: 1.11x faster                                                         |
| pickle               | 9.89 us                                                      | 10.7 us: 1.08x slower                                                         |
| pickle_list          | 4.12 us                                                      | 4.52 us: 1.10x slower                                                         |
| pickle_dict          | 29.5 us                                                      | 32.7 us: 1.11x slower                                                         |
| unpickle             | 13.5 us                                                      | 15.2 us: 1.12x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                                  |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                         |
| python_startup_no_site | 7.33 ms                                                      | 8.98 ms: 1.23x slower                                                         |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.21 ms: 1.60x faster                                                         |
| django_template | 50.2 ms                                                      | 40.8 ms: 1.23x faster                                                         |
| genshi_text     | 31.4 ms                                                      | 29.3 ms: 1.07x faster                                                         |
| genshi_xml      | 63.3 ms                                                      | 64.3 ms: 1.02x slower                                                         |
| Geometric mean  | (ref)                                                        | 1.20x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 183 us: 2.93x faster                                                          |
| deltablue                | 7.50 ms                                                      | 3.21 ms: 2.33x faster                                                         |
| async_tree_none          | 692 ms                                                       | 323 ms: 2.14x faster                                                          |
| asyncio_tcp              | 779 ms                                                       | 379 ms: 2.05x faster                                                          |
| async_tree_memoization   | 819 ms                                                       | 404 ms: 2.03x faster                                                          |
| async_tree_io            | 1.60 sec                                                     | 802 ms: 1.99x faster                                                          |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 28.0 us: 1.78x faster                                                         |
| go                       | 262 ms                                                       | 150 ms: 1.74x faster                                                          |
| scimark_lu               | 167 ms                                                       | 96.8 ms: 1.72x faster                                                         |
| richards_super           | 90.6 ms                                                      | 52.8 ms: 1.72x faster                                                         |
| spectral_norm            | 139 ms                                                       | 81.4 ms: 1.71x faster                                                         |
| scimark_sor              | 180 ms                                                       | 106 ms: 1.69x faster                                                          |
| crypto_pyaes             | 119 ms                                                       | 71.1 ms: 1.68x faster                                                         |
| chaos                    | 109 ms                                                       | 66.0 ms: 1.65x faster                                                         |
| pyflate                  | 733 ms                                                       | 446 ms: 1.65x faster                                                          |
| richards                 | 75.1 ms                                                      | 45.9 ms: 1.64x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 575 ms: 1.63x faster                                                          |
| logging_silent           | 167 ns                                                       | 104 ns: 1.61x faster                                                          |
| nbody                    | 134 ms                                                       | 83.5 ms: 1.61x faster                                                         |
| mako                     | 14.7 ms                                                      | 9.21 ms: 1.60x faster                                                         |
| raytrace                 | 489 ms                                                       | 309 ms: 1.58x faster                                                          |
| deepcopy                 | 468 us                                                       | 298 us: 1.57x faster                                                          |
| scimark_monte_carlo      | 107 ms                                                       | 68.8 ms: 1.56x faster                                                         |
| generators               | 57.3 ms                                                      | 36.8 ms: 1.56x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.48 ms: 1.51x faster                                                         |
| float                    | 111 ms                                                       | 75.6 ms: 1.47x faster                                                         |
| comprehensions           | 26.7 us                                                      | 18.5 us: 1.44x faster                                                         |
| unpickle_pure_python     | 312 us                                                       | 217 us: 1.44x faster                                                          |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.42x faster                                                         |
| sqlglot_transpile        | 2.68 ms                                                      | 1.93 ms: 1.39x faster                                                         |
| pylint                   | 566 ms                                                       | 410 ms: 1.38x faster                                                          |
| pickle_pure_python       | 455 us                                                       | 330 us: 1.38x faster                                                          |
| tomli_loads              | 2.92 sec                                                     | 2.13 sec: 1.37x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.95 us: 1.36x faster                                                         |
| logging_simple           | 8.88 us                                                      | 6.53 us: 1.36x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 15.7 ms: 1.36x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                         |
| logging_format           | 9.64 us                                                      | 7.12 us: 1.35x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 56.5 ms: 1.34x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 70.6 ms: 1.34x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 7.06 ms: 1.33x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 792 ms: 1.33x faster                                                          |
| thrift                   | 1.18 ms                                                      | 889 us: 1.32x faster                                                          |
| fannkuch                 | 483 ms                                                       | 366 ms: 1.32x faster                                                          |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.31x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.28 sec: 1.30x faster                                                        |
| tornado_http             | 157 ms                                                       | 122 ms: 1.28x faster                                                          |
| regex_compile            | 190 ms                                                       | 149 ms: 1.27x faster                                                          |
| json_loads               | 30.3 us                                                      | 24.0 us: 1.26x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.02 ms: 1.26x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 64.4 ms: 1.26x faster                                                         |
| scimark_fft              | 361 ms                                                       | 289 ms: 1.25x faster                                                          |
| bench_thread_pool        | 1.14 ms                                                      | 915 us: 1.25x faster                                                          |
| django_template          | 50.2 ms                                                      | 40.8 ms: 1.23x faster                                                         |
| bench_mp_pool            | 6.37 ms                                                      | 5.31 ms: 1.20x faster                                                         |
| nqueens                  | 115 ms                                                       | 98.6 ms: 1.17x faster                                                         |
| sympy_str                | 360 ms                                                       | 309 ms: 1.16x faster                                                          |
| mdp                      | 3.01 sec                                                     | 2.59 sec: 1.16x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 79.9 ms: 1.15x faster                                                         |
| sympy_expand             | 600 ms                                                       | 525 ms: 1.14x faster                                                          |
| sympy_sum                | 193 ms                                                       | 169 ms: 1.14x faster                                                          |
| 2to3                     | 350 ms                                                       | 309 ms: 1.13x faster                                                          |
| xml_etree_parse          | 160 ms                                                       | 142 ms: 1.12x faster                                                          |
| json                     | 5.86 ms                                                      | 5.24 ms: 1.12x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 99.5 ms: 1.11x faster                                                         |
| regex_dna                | 261 ms                                                       | 236 ms: 1.11x faster                                                          |
| sqlite_synth             | 2.99 us                                                      | 2.72 us: 1.10x faster                                                         |
| async_generators         | 421 ms                                                       | 386 ms: 1.09x faster                                                          |
| sqlglot_normalize        | 144 ms                                                       | 132 ms: 1.09x faster                                                          |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                          |
| genshi_text              | 31.4 ms                                                      | 29.3 ms: 1.07x faster                                                         |
| docutils                 | 3.41 sec                                                     | 3.18 sec: 1.07x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 26.4 ms: 1.07x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 66.3 ms: 1.06x faster                                                         |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.05x faster                                                          |
| regex_v8                 | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 64.3 ms: 1.02x slower                                                         |
| pickle                   | 9.89 us                                                      | 10.7 us: 1.08x slower                                                         |
| create_gc_cycles         | 1.76 ms                                                      | 1.91 ms: 1.08x slower                                                         |
| pickle_list              | 4.12 us                                                      | 4.52 us: 1.10x slower                                                         |
| pickle_dict              | 29.5 us                                                      | 32.7 us: 1.11x slower                                                         |
| unpickle                 | 13.5 us                                                      | 15.2 us: 1.12x slower                                                         |
| telco                    | 7.23 ms                                                      | 8.30 ms: 1.15x slower                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                         |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                         |
| python_startup_no_site   | 7.33 ms                                                      | 8.98 ms: 1.23x slower                                                         |
| coverage                 | 63.3 ms                                                      | 80.8 ms: 1.28x slower                                                         |
| gc_traversal             | 3.42 ms                                                      | 4.41 ms: 1.29x slower                                                         |
| unpack_sequence          | 59.9 ns                                                      | 88.0 ns: 1.47x slower                                                         |
| Geometric mean           | (ref)                                                        | 1.29x faster                                                                  |

Benchmark hidden because not significant (2): unpickle_list, asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.22x
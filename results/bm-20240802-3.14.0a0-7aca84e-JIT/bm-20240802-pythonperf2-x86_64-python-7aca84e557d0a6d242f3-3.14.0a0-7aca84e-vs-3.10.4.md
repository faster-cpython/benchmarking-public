# Results vs. 3.10.4

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-x86_64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 308 ms: 1.13x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.14 sec: 1.09x faster                                                      |
| html5lib       | 94.6 ms                                                      | 71.1 ms: 1.33x faster                                                       |
| tornado_http   | 157 ms                                                       | 120 ms: 1.31x faster                                                        |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 322 ms: 2.15x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 413 ms: 1.98x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 828 ms: 1.93x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 563 ms: 1.66x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.92x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 88.3 ms: 1.52x faster                                                       |
| float          | 111 ms                                                       | 76.2 ms: 1.46x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.37x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 27.1 ms: 1.00x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 211 us: 1.48x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 314 us: 1.45x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.10 sec: 1.39x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 56.5 ms: 1.34x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.4 us: 1.20x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 139 ms: 1.15x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 80.3 ms: 1.15x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 97.2 ms: 1.14x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.29x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.10 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.12 ms: 1.61x faster                                                       |
| django_template | 50.2 ms                                                      | 41.5 ms: 1.21x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 28.2 ms: 1.11x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 62.0 ms: 1.02x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.22x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 183 us: 2.93x faster                                                        |
| async_tree_none          | 692 ms                                                       | 322 ms: 2.15x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 377 ms: 2.07x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.74 ms: 2.01x faster                                                       |
| async_tree_memoization   | 819 ms                                                       | 413 ms: 1.98x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 828 ms: 1.93x faster                                                        |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.74x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.1 us: 1.71x faster                                                       |
| spectral_norm            | 139 ms                                                       | 81.4 ms: 1.71x faster                                                       |
| scimark_lu               | 167 ms                                                       | 97.8 ms: 1.71x faster                                                       |
| raytrace                 | 489 ms                                                       | 289 ms: 1.69x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 71.0 ms: 1.68x faster                                                       |
| richards_super           | 90.6 ms                                                      | 54.1 ms: 1.67x faster                                                       |
| logging_silent           | 167 ns                                                       | 100 ns: 1.67x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 563 ms: 1.66x faster                                                        |
| chaos                    | 109 ms                                                       | 66.0 ms: 1.64x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.12 ms: 1.61x faster                                                       |
| richards                 | 75.1 ms                                                      | 46.6 ms: 1.61x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 67.5 ms: 1.59x faster                                                       |
| generators               | 57.3 ms                                                      | 36.2 ms: 1.58x faster                                                       |
| pyflate                  | 733 ms                                                       | 463 ms: 1.58x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.43 ms: 1.56x faster                                                       |
| go                       | 262 ms                                                       | 168 ms: 1.55x faster                                                        |
| nbody                    | 134 ms                                                       | 88.3 ms: 1.52x faster                                                       |
| deepcopy                 | 468 us                                                       | 311 us: 1.50x faster                                                        |
| comprehensions           | 26.7 us                                                      | 18.0 us: 1.48x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 211 us: 1.48x faster                                                        |
| pylint                   | 566 ms                                                       | 387 ms: 1.46x faster                                                        |
| float                    | 111 ms                                                       | 76.2 ms: 1.46x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.84 ms: 1.45x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 314 us: 1.45x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.29 us: 1.41x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.77 ms: 1.39x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.10 sec: 1.39x faster                                                      |
| regex_compile            | 190 ms                                                       | 138 ms: 1.37x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.05 us: 1.37x faster                                                       |
| fannkuch                 | 483 ms                                                       | 355 ms: 1.36x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.4 ms: 1.35x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 56.5 ms: 1.34x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                      |
| bench_mp_pool            | 6.37 ms                                                      | 4.79 ms: 1.33x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 71.1 ms: 1.33x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.04 us: 1.32x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.3 ms: 1.31x faster                                                       |
| tornado_http             | 157 ms                                                       | 120 ms: 1.31x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.30x faster                                                      |
| thrift                   | 1.18 ms                                                      | 902 us: 1.30x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 812 ms: 1.29x faster                                                        |
| scimark_fft              | 361 ms                                                       | 285 ms: 1.27x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 910 us: 1.25x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.11 ms: 1.23x faster                                                       |
| django_template          | 50.2 ms                                                      | 41.5 ms: 1.21x faster                                                       |
| dask                     | 472 ms                                                       | 395 ms: 1.20x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.4 us: 1.20x faster                                                       |
| sympy_str                | 360 ms                                                       | 310 ms: 1.16x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.59 sec: 1.16x faster                                                      |
| nqueens                  | 115 ms                                                       | 99.3 ms: 1.16x faster                                                       |
| sympy_sum                | 193 ms                                                       | 167 ms: 1.16x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 139 ms: 1.15x faster                                                        |
| sympy_expand             | 600 ms                                                       | 521 ms: 1.15x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 80.3 ms: 1.15x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 97.2 ms: 1.14x faster                                                       |
| 2to3                     | 350 ms                                                       | 308 ms: 1.13x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 62.2 ms: 1.13x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 128 ms: 1.13x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 28.2 ms: 1.11x faster                                                       |
| async_generators         | 421 ms                                                       | 386 ms: 1.09x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 25.9 ms: 1.09x faster                                                       |
| docutils                 | 3.41 sec                                                     | 3.14 sec: 1.09x faster                                                      |
| json                     | 5.86 ms                                                      | 5.42 ms: 1.08x faster                                                       |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 62.0 ms: 1.02x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 27.1 ms: 1.00x faster                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.92 ms: 1.09x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.09 ms: 1.12x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.10 ms: 1.24x slower                                                       |
| coverage                 | 63.3 ms                                                      | 78.8 ms: 1.25x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.34 ms: 1.27x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.33x faster                                                                |

Benchmark hidden because not significant (2): regex_dna, asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.21x
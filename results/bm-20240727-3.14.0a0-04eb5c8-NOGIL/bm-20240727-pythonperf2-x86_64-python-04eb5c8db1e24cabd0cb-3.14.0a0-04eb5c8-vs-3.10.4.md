# Results vs. 3.10.4

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.11x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 435 ms: 1.24x slower                                                        |
| docutils       | 3.41 sec                                                     | 3.54 sec: 1.04x slower                                                      |
| html5lib       | 94.6 ms                                                      | 109 ms: 1.15x slower                                                        |
| tornado_http   | 157 ms                                                       | 163 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.11x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 967 ms: 1.65x faster                                                        |
| async_tree_none         | 692 ms                                                       | 430 ms: 1.61x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 531 ms: 1.54x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 687 ms: 1.36x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.54x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| float          | 111 ms                                                       | 144 ms: 1.30x slower                                                        |
| nbody          | 134 ms                                                       | 200 ms: 1.49x slower                                                        |
| Geometric mean | (ref)                                                        | 1.22x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 239 ms: 1.09x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 27.8 ms: 1.02x slower                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.52 ms: 1.14x slower                                                       |
| regex_compile  | 190 ms                                                       | 233 ms: 1.23x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.14x faster                                                        |
| json_loads           | 30.3 us                                                      | 29.8 us: 1.02x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 14.3 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 109 ms: 1.01x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 3.43 sec: 1.18x slower                                                      |
| xml_etree_process    | 75.9 ms                                                      | 94.3 ms: 1.24x slower                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 116 ms: 1.25x slower                                                        |
| pickle_pure_python   | 455 us                                                       | 596 us: 1.31x slower                                                        |
| unpickle_pure_python | 312 us                                                       | 421 us: 1.35x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.12x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 16.7 ms: 1.45x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 11.4 ms: 1.56x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.50x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 63.3 ms                                                      | 84.3 ms: 1.33x slower                                                       |
| django_template | 50.2 ms                                                      | 69.0 ms: 1.37x slower                                                       |
| genshi_text     | 31.4 ms                                                      | 43.4 ms: 1.38x slower                                                       |
| mako            | 14.7 ms                                                      | 22.1 ms: 1.51x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.40x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 278 us: 1.93x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.77 sec: 1.75x faster                                                      |
| asyncio_tcp              | 779 ms                                                       | 453 ms: 1.72x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 967 ms: 1.65x faster                                                        |
| async_tree_none          | 692 ms                                                       | 430 ms: 1.61x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 531 ms: 1.54x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.40 ms: 1.45x faster                                                       |
| generators               | 57.3 ms                                                      | 41.9 ms: 1.37x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 687 ms: 1.36x faster                                                        |
| pylint                   | 566 ms                                                       | 435 ms: 1.30x faster                                                        |
| gc_traversal             | 3.42 ms                                                      | 2.88 ms: 1.18x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 141 ms: 1.14x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 19.6 ms: 1.09x faster                                                       |
| regex_dna                | 261 ms                                                       | 239 ms: 1.09x faster                                                        |
| coroutines               | 30.3 ms                                                      | 28.1 ms: 1.08x faster                                                       |
| pidigits                 | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| deepcopy                 | 468 us                                                       | 453 us: 1.03x faster                                                        |
| json_loads               | 30.3 us                                                      | 29.8 us: 1.02x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 383 ms: 1.02x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 14.3 ms: 1.02x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 109 ms: 1.01x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 27.8 ms: 1.02x slower                                                       |
| tornado_http             | 157 ms                                                       | 163 ms: 1.04x slower                                                        |
| crypto_pyaes             | 119 ms                                                       | 124 ms: 1.04x slower                                                        |
| docutils                 | 3.41 sec                                                     | 3.54 sec: 1.04x slower                                                      |
| pycparser                | 1.67 sec                                                     | 1.75 sec: 1.05x slower                                                      |
| json                     | 5.86 ms                                                      | 6.21 ms: 1.06x slower                                                       |
| deepcopy_memo            | 49.8 us                                                      | 53.2 us: 1.07x slower                                                       |
| mdp                      | 3.01 sec                                                     | 3.27 sec: 1.09x slower                                                      |
| pyflate                  | 733 ms                                                       | 813 ms: 1.11x slower                                                        |
| logging_silent           | 167 ns                                                       | 187 ns: 1.12x slower                                                        |
| deltablue                | 7.50 ms                                                      | 8.40 ms: 1.12x slower                                                       |
| richards                 | 75.1 ms                                                      | 85.1 ms: 1.13x slower                                                       |
| nqueens                  | 115 ms                                                       | 130 ms: 1.13x slower                                                        |
| comprehensions           | 26.7 us                                                      | 30.3 us: 1.14x slower                                                       |
| richards_super           | 90.6 ms                                                      | 103 ms: 1.14x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.52 ms: 1.14x slower                                                       |
| chaos                    | 109 ms                                                       | 124 ms: 1.14x slower                                                        |
| sympy_integrate          | 28.2 ms                                                      | 32.4 ms: 1.15x slower                                                       |
| html5lib                 | 94.6 ms                                                      | 109 ms: 1.15x slower                                                        |
| scimark_fft              | 361 ms                                                       | 417 ms: 1.16x slower                                                        |
| thrift                   | 1.18 ms                                                      | 1.37 ms: 1.17x slower                                                       |
| tomli_loads              | 2.92 sec                                                     | 3.43 sec: 1.18x slower                                                      |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 6.01 ms: 1.18x slower                                                       |
| async_generators         | 421 ms                                                       | 508 ms: 1.21x slower                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 4.85 us: 1.21x slower                                                       |
| spectral_norm            | 139 ms                                                       | 169 ms: 1.22x slower                                                        |
| regex_compile            | 190 ms                                                       | 233 ms: 1.23x slower                                                        |
| xml_etree_process        | 75.9 ms                                                      | 94.3 ms: 1.24x slower                                                       |
| 2to3                     | 350 ms                                                       | 435 ms: 1.24x slower                                                        |
| raytrace                 | 489 ms                                                       | 612 ms: 1.25x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 116 ms: 1.25x slower                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 136 ms: 1.27x slower                                                        |
| meteor_contest           | 138 ms                                                       | 175 ms: 1.27x slower                                                        |
| sympy_str                | 360 ms                                                       | 456 ms: 1.27x slower                                                        |
| fannkuch                 | 483 ms                                                       | 614 ms: 1.27x slower                                                        |
| hexiom                   | 9.42 ms                                                      | 12.1 ms: 1.28x slower                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 3.44 ms: 1.28x slower                                                       |
| go                       | 262 ms                                                       | 338 ms: 1.29x slower                                                        |
| float                    | 111 ms                                                       | 144 ms: 1.30x slower                                                        |
| pickle_pure_python       | 455 us                                                       | 596 us: 1.31x slower                                                        |
| sqlglot_normalize        | 144 ms                                                       | 188 ms: 1.31x slower                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 2.94 ms: 1.31x slower                                                       |
| logging_format           | 9.64 us                                                      | 12.7 us: 1.31x slower                                                       |
| logging_simple           | 8.88 us                                                      | 11.8 us: 1.33x slower                                                       |
| genshi_xml               | 63.3 ms                                                      | 84.3 ms: 1.33x slower                                                       |
| unpickle_pure_python     | 312 us                                                       | 421 us: 1.35x slower                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 95.2 ms: 1.36x slower                                                       |
| sympy_sum                | 193 ms                                                       | 262 ms: 1.36x slower                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.56 ms: 1.37x slower                                                       |
| django_template          | 50.2 ms                                                      | 69.0 ms: 1.37x slower                                                       |
| genshi_text              | 31.4 ms                                                      | 43.4 ms: 1.38x slower                                                       |
| sympy_expand             | 600 ms                                                       | 830 ms: 1.38x slower                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 1.47 sec: 1.40x slower                                                      |
| pprint_pformat           | 2.15 sec                                                     | 3.04 sec: 1.41x slower                                                      |
| telco                    | 7.23 ms                                                      | 10.3 ms: 1.42x slower                                                       |
| scimark_lu               | 167 ms                                                       | 242 ms: 1.45x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.7 ms: 1.45x slower                                                       |
| scimark_sor              | 180 ms                                                       | 266 ms: 1.48x slower                                                        |
| nbody                    | 134 ms                                                       | 200 ms: 1.49x slower                                                        |
| mako                     | 14.7 ms                                                      | 22.1 ms: 1.51x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 11.4 ms: 1.56x slower                                                       |
| coverage                 | 63.3 ms                                                      | 107 ms: 1.69x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.11x slower                                                                |

Benchmark hidden because not significant (1): create_gc_cycles
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.31x
# Results vs. 3.10.4

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-x86_64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 433 ms: 1.24x slower                                                        |
| docutils       | 3.41 sec                                                     | 3.49 sec: 1.02x slower                                                      |
| html5lib       | 94.6 ms                                                      | 106 ms: 1.12x slower                                                        |
| tornado_http   | 157 ms                                                       | 163 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 968 ms: 1.65x faster                                                        |
| async_tree_none         | 692 ms                                                       | 429 ms: 1.61x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 540 ms: 1.52x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 693 ms: 1.35x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.53x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| float          | 111 ms                                                       | 148 ms: 1.33x slower                                                        |
| nbody          | 134 ms                                                       | 204 ms: 1.52x slower                                                        |
| Geometric mean | (ref)                                                        | 1.24x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 234 ms: 1.12x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 28.4 ms: 1.05x slower                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.33 ms: 1.08x slower                                                       |
| regex_compile  | 190 ms                                                       | 231 ms: 1.22x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 14.4 ms: 1.01x faster                                                       |
| json_loads           | 30.3 us                                                      | 30.5 us: 1.00x slower                                                       |
| tomli_loads          | 2.92 sec                                                     | 3.38 sec: 1.16x slower                                                      |
| xml_etree_generate   | 92.3 ms                                                      | 114 ms: 1.24x slower                                                        |
| xml_etree_process    | 75.9 ms                                                      | 94.4 ms: 1.24x slower                                                       |
| pickle_pure_python   | 455 us                                                       | 589 us: 1.30x slower                                                        |
| unpickle_pure_python | 312 us                                                       | 418 us: 1.34x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.11x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 16.9 ms: 1.47x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 11.5 ms: 1.57x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.52x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 63.3 ms                                                      | 83.1 ms: 1.31x slower                                                       |
| genshi_text     | 31.4 ms                                                      | 42.4 ms: 1.35x slower                                                       |
| django_template | 50.2 ms                                                      | 68.2 ms: 1.36x slower                                                       |
| mako            | 14.7 ms                                                      | 22.3 ms: 1.52x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.38x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 271 us: 1.98x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.79 sec: 1.74x faster                                                      |
| asyncio_tcp              | 779 ms                                                       | 452 ms: 1.72x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 968 ms: 1.65x faster                                                        |
| async_tree_none          | 692 ms                                                       | 429 ms: 1.61x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 540 ms: 1.52x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.44 ms: 1.44x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 693 ms: 1.35x faster                                                        |
| pylint                   | 566 ms                                                       | 427 ms: 1.32x faster                                                        |
| generators               | 57.3 ms                                                      | 45.5 ms: 1.26x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                        |
| regex_dna                | 261 ms                                                       | 234 ms: 1.12x faster                                                        |
| gc_traversal             | 3.42 ms                                                      | 3.10 ms: 1.10x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 19.8 ms: 1.08x faster                                                       |
| pidigits                 | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| coroutines               | 30.3 ms                                                      | 28.8 ms: 1.05x faster                                                       |
| deepcopy                 | 468 us                                                       | 444 us: 1.05x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 381 ms: 1.03x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 14.4 ms: 1.01x faster                                                       |
| json_loads               | 30.3 us                                                      | 30.5 us: 1.00x slower                                                       |
| docutils                 | 3.41 sec                                                     | 3.49 sec: 1.02x slower                                                      |
| deepcopy_memo            | 49.8 us                                                      | 51.0 us: 1.02x slower                                                       |
| tornado_http             | 157 ms                                                       | 163 ms: 1.04x slower                                                        |
| crypto_pyaes             | 119 ms                                                       | 124 ms: 1.04x slower                                                        |
| regex_v8                 | 27.2 ms                                                      | 28.4 ms: 1.05x slower                                                       |
| json                     | 5.86 ms                                                      | 6.18 ms: 1.05x slower                                                       |
| pyflate                  | 733 ms                                                       | 774 ms: 1.06x slower                                                        |
| pycparser                | 1.67 sec                                                     | 1.77 sec: 1.06x slower                                                      |
| regex_effbot             | 3.09 ms                                                      | 3.33 ms: 1.08x slower                                                       |
| logging_silent           | 167 ns                                                       | 183 ns: 1.09x slower                                                        |
| mdp                      | 3.01 sec                                                     | 3.29 sec: 1.09x slower                                                      |
| richards_super           | 90.6 ms                                                      | 100 ms: 1.11x slower                                                        |
| dulwich_log              | 81.1 ms                                                      | 90.2 ms: 1.11x slower                                                       |
| richards                 | 75.1 ms                                                      | 83.5 ms: 1.11x slower                                                       |
| deltablue                | 7.50 ms                                                      | 8.39 ms: 1.12x slower                                                       |
| html5lib                 | 94.6 ms                                                      | 106 ms: 1.12x slower                                                        |
| comprehensions           | 26.7 us                                                      | 30.3 us: 1.14x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.79 ms: 1.14x slower                                                       |
| nqueens                  | 115 ms                                                       | 131 ms: 1.14x slower                                                        |
| sympy_integrate          | 28.2 ms                                                      | 32.2 ms: 1.14x slower                                                       |
| scimark_fft              | 361 ms                                                       | 415 ms: 1.15x slower                                                        |
| tomli_loads              | 2.92 sec                                                     | 3.38 sec: 1.16x slower                                                      |
| chaos                    | 109 ms                                                       | 127 ms: 1.17x slower                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 4.73 us: 1.18x slower                                                       |
| async_generators         | 421 ms                                                       | 497 ms: 1.18x slower                                                        |
| thrift                   | 1.18 ms                                                      | 1.42 ms: 1.21x slower                                                       |
| fannkuch                 | 483 ms                                                       | 582 ms: 1.21x slower                                                        |
| regex_compile            | 190 ms                                                       | 231 ms: 1.22x slower                                                        |
| 2to3                     | 350 ms                                                       | 433 ms: 1.24x slower                                                        |
| spectral_norm            | 139 ms                                                       | 172 ms: 1.24x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 114 ms: 1.24x slower                                                        |
| xml_etree_process        | 75.9 ms                                                      | 94.4 ms: 1.24x slower                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 134 ms: 1.25x slower                                                        |
| meteor_contest           | 138 ms                                                       | 174 ms: 1.26x slower                                                        |
| sympy_str                | 360 ms                                                       | 455 ms: 1.26x slower                                                        |
| raytrace                 | 489 ms                                                       | 623 ms: 1.27x slower                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 3.42 ms: 1.27x slower                                                       |
| hexiom                   | 9.42 ms                                                      | 12.1 ms: 1.28x slower                                                       |
| logging_format           | 9.64 us                                                      | 12.5 us: 1.29x slower                                                       |
| pickle_pure_python       | 455 us                                                       | 589 us: 1.30x slower                                                        |
| logging_simple           | 8.88 us                                                      | 11.5 us: 1.30x slower                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 2.91 ms: 1.30x slower                                                       |
| sqlglot_normalize        | 144 ms                                                       | 187 ms: 1.30x slower                                                        |
| go                       | 262 ms                                                       | 342 ms: 1.31x slower                                                        |
| genshi_xml               | 63.3 ms                                                      | 83.1 ms: 1.31x slower                                                       |
| float                    | 111 ms                                                       | 148 ms: 1.33x slower                                                        |
| unpickle_pure_python     | 312 us                                                       | 418 us: 1.34x slower                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 94.6 ms: 1.35x slower                                                       |
| genshi_text              | 31.4 ms                                                      | 42.4 ms: 1.35x slower                                                       |
| django_template          | 50.2 ms                                                      | 68.2 ms: 1.36x slower                                                       |
| sympy_sum                | 193 ms                                                       | 263 ms: 1.36x slower                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.56 ms: 1.37x slower                                                       |
| sympy_expand             | 600 ms                                                       | 827 ms: 1.38x slower                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 1.45 sec: 1.38x slower                                                      |
| pprint_pformat           | 2.15 sec                                                     | 2.99 sec: 1.39x slower                                                      |
| scimark_sor              | 180 ms                                                       | 251 ms: 1.39x slower                                                        |
| scimark_lu               | 167 ms                                                       | 236 ms: 1.41x slower                                                        |
| telco                    | 7.23 ms                                                      | 10.4 ms: 1.43x slower                                                       |
| python_startup           | 11.5 ms                                                      | 16.9 ms: 1.47x slower                                                       |
| mako                     | 14.7 ms                                                      | 22.3 ms: 1.52x slower                                                       |
| nbody                    | 134 ms                                                       | 204 ms: 1.52x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 11.5 ms: 1.57x slower                                                       |
| coverage                 | 63.3 ms                                                      | 105 ms: 1.65x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.10x slower                                                                |

Benchmark hidden because not significant (2): create_gc_cycles, xml_etree_iterparse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240713-3.14.0a0-a2bec77-NOGIL/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.30x
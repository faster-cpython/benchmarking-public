# Results vs. 3.10.4

- fork: python
- ref: e38d0afe3548b856ccf0
- machine: linux-x86_64
- commit hash: e38d0af
- commit date: 2024-08-24
- overall geometric mean: 1.332x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.96 sec: 1.15x faster                                                      |
| html5lib       | 94.6 ms                                                      | 75.1 ms: 1.26x faster                                                       |
| tornado_http   | 157 ms                                                       | 116 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 323 ms: 2.14x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 401 ms: 2.04x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 807 ms: 1.98x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 575 ms: 1.63x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.94x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 90.7 ms: 1.48x faster                                                       |
| float          | 111 ms                                                       | 78.9 ms: 1.41x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.36x faster                                                        |
| regex_dna      | 261 ms                                                       | 234 ms: 1.12x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 314 us: 1.45x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 220 us: 1.42x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.9 ms: 1.34x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 59.7 ms: 1.27x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.54 sec: 1.15x faster                                                      |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 84.1 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.10x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.23x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 24.7 ms: 1.27x faster                                                       |
| django_template | 50.2 ms                                                      | 41.3 ms: 1.22x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 55.1 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 171 us: 3.15x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.38 ms: 2.22x faster                                                       |
| async_tree_none          | 692 ms                                                       | 323 ms: 2.14x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 372 ms: 2.10x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 401 ms: 2.04x faster                                                        |
| generators               | 57.3 ms                                                      | 28.6 ms: 2.01x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 807 ms: 1.98x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                      |
| chaos                    | 109 ms                                                       | 61.4 ms: 1.77x faster                                                       |
| raytrace                 | 489 ms                                                       | 277 ms: 1.76x faster                                                        |
| scimark_lu               | 167 ms                                                       | 95.0 ms: 1.76x faster                                                       |
| logging_silent           | 167 ns                                                       | 98.0 ns: 1.71x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 29.2 us: 1.70x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 65.2 ms: 1.65x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 72.5 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 575 ms: 1.63x faster                                                        |
| pylint                   | 566 ms                                                       | 350 ms: 1.62x faster                                                        |
| deepcopy                 | 468 us                                                       | 290 us: 1.61x faster                                                        |
| richards_super           | 90.6 ms                                                      | 56.8 ms: 1.60x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.57x faster                                                       |
| scimark_sor              | 180 ms                                                       | 116 ms: 1.55x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.5 us: 1.53x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.24 ms: 1.51x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.80 ms: 1.49x faster                                                       |
| richards                 | 75.1 ms                                                      | 50.5 ms: 1.49x faster                                                       |
| nbody                    | 134 ms                                                       | 90.7 ms: 1.48x faster                                                       |
| pyflate                  | 733 ms                                                       | 498 ms: 1.47x faster                                                        |
| go                       | 262 ms                                                       | 180 ms: 1.45x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 314 us: 1.45x faster                                                        |
| spectral_norm            | 139 ms                                                       | 96.2 ms: 1.45x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.41 ms: 1.44x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 220 us: 1.42x faster                                                        |
| float                    | 111 ms                                                       | 78.9 ms: 1.41x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.31 us: 1.41x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.97 us: 1.38x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.6 ms: 1.37x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.93 us: 1.37x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                      |
| regex_compile            | 190 ms                                                       | 139 ms: 1.36x faster                                                        |
| tornado_http             | 157 ms                                                       | 116 ms: 1.35x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.9 ms: 1.34x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 852 us: 1.34x faster                                                        |
| thrift                   | 1.18 ms                                                      | 878 us: 1.34x faster                                                        |
| fannkuch                 | 483 ms                                                       | 361 ms: 1.34x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 808 ms: 1.30x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 24.7 ms: 1.27x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 59.7 ms: 1.27x faster                                                       |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 75.1 ms: 1.26x faster                                                       |
| nqueens                  | 115 ms                                                       | 91.8 ms: 1.25x faster                                                       |
| 2to3                     | 350 ms                                                       | 282 ms: 1.24x faster                                                        |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.9 ms: 1.23x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.22x faster                                                        |
| django_template          | 50.2 ms                                                      | 41.3 ms: 1.22x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                                       |
| scimark_fft              | 361 ms                                                       | 300 ms: 1.20x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.50 sec: 1.20x faster                                                      |
| sqlglot_optimize         | 70.1 ms                                                      | 58.4 ms: 1.20x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.23 ms: 1.20x faster                                                       |
| sympy_expand             | 600 ms                                                       | 501 ms: 1.20x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.96 sec: 1.15x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 55.1 ms: 1.15x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.54 sec: 1.15x faster                                                      |
| async_generators         | 421 ms                                                       | 369 ms: 1.14x faster                                                        |
| regex_dna                | 261 ms                                                       | 234 ms: 1.12x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                                        |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 84.1 ms: 1.10x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.10x faster                                                        |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| json                     | 5.86 ms                                                      | 5.44 ms: 1.08x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.00 ms: 1.13x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.39 ms: 1.16x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.48 ms: 1.31x slower                                                       |
| coverage                 | 63.3 ms                                                      | 84.2 ms: 1.33x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240824-3.14.0a0-e38d0af/bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.332x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.14x
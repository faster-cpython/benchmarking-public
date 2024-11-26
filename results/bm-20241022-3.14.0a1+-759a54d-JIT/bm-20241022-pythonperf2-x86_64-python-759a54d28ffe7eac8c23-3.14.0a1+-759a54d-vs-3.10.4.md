# Results vs. 3.10.4

- fork: python
- ref: 759a54d28ffe7eac8c23
- machine: linux-x86_64
- commit hash: 759a54d
- commit date: 2024-10-22
- overall geometric mean: 1.277x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 314 ms: 1.11x faster                                                         |
| docutils       | 3.41 sec                                                     | 3.22 sec: 1.06x faster                                                       |
| html5lib       | 94.6 ms                                                      | 71.0 ms: 1.33x faster                                                        |
| tornado_http   | 157 ms                                                       | 124 ms: 1.27x faster                                                         |
| Geometric mean | (ref)                                                        | 1.19x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 342 ms: 2.02x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 412 ms: 1.99x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 842 ms: 1.90x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 576 ms: 1.62x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.88x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.6 ms: 1.57x faster                                                        |
| float          | 111 ms                                                       | 79.4 ms: 1.40x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 147 ms: 1.29x faster                                                         |
| regex_dna      | 261 ms                                                       | 242 ms: 1.08x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.5 ms: 1.06x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.65 ms: 1.18x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 220 us: 1.42x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.10 sec: 1.39x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 333 us: 1.37x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 60.3 ms: 1.26x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.10x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 84.5 ms: 1.09x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 147 ms: 1.09x faster                                                         |
| Geometric mean       | (ref)                                                        | 1.24x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 14.9 ms: 1.30x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.42 ms: 1.56x faster                                                        |
| django_template | 50.2 ms                                                      | 43.4 ms: 1.16x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 30.2 ms: 1.04x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.17x faster                                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 181 us: 2.96x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.29 ms: 2.28x faster                                                        |
| async_tree_none          | 692 ms                                                       | 342 ms: 2.02x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 412 ms: 1.99x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 842 ms: 1.90x faster                                                         |
| richards_super           | 90.6 ms                                                      | 51.0 ms: 1.78x faster                                                        |
| scimark_lu               | 167 ms                                                       | 97.3 ms: 1.72x faster                                                        |
| go                       | 262 ms                                                       | 154 ms: 1.70x faster                                                         |
| logging_silent           | 167 ns                                                       | 98.2 ns: 1.70x faster                                                        |
| scimark_sor              | 180 ms                                                       | 106 ms: 1.70x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 30.0 us: 1.66x faster                                                        |
| richards                 | 75.1 ms                                                      | 46.1 ms: 1.63x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 73.2 ms: 1.63x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 576 ms: 1.62x faster                                                         |
| pyflate                  | 733 ms                                                       | 452 ms: 1.62x faster                                                         |
| nbody                    | 134 ms                                                       | 85.6 ms: 1.57x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 68.6 ms: 1.57x faster                                                        |
| chaos                    | 109 ms                                                       | 69.5 ms: 1.56x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.42 ms: 1.56x faster                                                        |
| deepcopy                 | 468 us                                                       | 309 us: 1.51x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.51 ms: 1.48x faster                                                        |
| raytrace                 | 489 ms                                                       | 336 ms: 1.46x faster                                                         |
| spectral_norm            | 139 ms                                                       | 95.7 ms: 1.45x faster                                                        |
| generators               | 57.3 ms                                                      | 39.7 ms: 1.44x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                        |
| comprehensions           | 26.7 us                                                      | 18.8 us: 1.42x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 220 us: 1.42x faster                                                         |
| float                    | 111 ms                                                       | 79.4 ms: 1.40x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.10 sec: 1.39x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 333 us: 1.37x faster                                                         |
| logging_simple           | 8.88 us                                                      | 6.54 us: 1.36x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.98 ms: 1.36x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.12 us: 1.35x faster                                                        |
| pylint                   | 566 ms                                                       | 424 ms: 1.34x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 71.0 ms: 1.33x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.1 ms: 1.33x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 794 ms: 1.32x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 3.03 us: 1.32x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 7.21 ms: 1.31x faster                                                        |
| regex_compile            | 190 ms                                                       | 147 ms: 1.29x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.67 sec: 1.29x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 63.1 ms: 1.29x faster                                                        |
| fannkuch                 | 483 ms                                                       | 380 ms: 1.27x faster                                                         |
| tornado_http             | 157 ms                                                       | 124 ms: 1.27x faster                                                         |
| thrift                   | 1.18 ms                                                      | 928 us: 1.27x faster                                                         |
| scimark_fft              | 361 ms                                                       | 287 ms: 1.26x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 60.3 ms: 1.26x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 950 us: 1.20x faster                                                         |
| django_template          | 50.2 ms                                                      | 43.4 ms: 1.16x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.40 ms: 1.15x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.66 sec: 1.13x faster                                                       |
| sympy_expand             | 600 ms                                                       | 534 ms: 1.12x faster                                                         |
| sympy_str                | 360 ms                                                       | 323 ms: 1.11x faster                                                         |
| json                     | 5.86 ms                                                      | 5.26 ms: 1.11x faster                                                        |
| nqueens                  | 115 ms                                                       | 103 ms: 1.11x faster                                                         |
| 2to3                     | 350 ms                                                       | 314 ms: 1.11x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.10x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 84.5 ms: 1.09x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 147 ms: 1.09x faster                                                         |
| sympy_sum                | 193 ms                                                       | 177 ms: 1.09x faster                                                         |
| regex_dna                | 261 ms                                                       | 242 ms: 1.08x faster                                                         |
| async_generators         | 421 ms                                                       | 390 ms: 1.08x faster                                                         |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 133 ms: 1.08x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 25.5 ms: 1.06x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.22 sec: 1.06x faster                                                       |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.05x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 30.2 ms: 1.04x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 382 ms: 1.02x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 27.6 ms: 1.02x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 69.6 ms: 1.01x faster                                                        |
| telco                    | 7.23 ms                                                      | 7.75 ms: 1.07x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.65 ms: 1.18x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                                        |
| python_startup           | 11.5 ms                                                      | 14.9 ms: 1.30x slower                                                        |
| coverage                 | 63.3 ms                                                      | 86.3 ms: 1.36x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 5.53 ms: 1.62x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.89 ms: 1.64x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 2.18 sec: 342.34x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.19x faster                                                                 |

Benchmark hidden because not significant (1): genshi_xml
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241022-3.14.0a1+-759a54d-JIT/bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.277x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.34x
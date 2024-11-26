# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.291x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 316 ms: 1.11x faster                                                 |
| docutils       | 3.41 sec                                                     | 3.22 sec: 1.06x faster                                               |
| html5lib       | 94.6 ms                                                      | 71.5 ms: 1.32x faster                                                |
| tornado_http   | 157 ms                                                       | 122 ms: 1.28x faster                                                 |
| Geometric mean | (ref)                                                        | 1.19x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 322 ms: 2.15x faster                                                 |
| async_tree_memoization  | 819 ms                                                       | 411 ms: 1.99x faster                                                 |
| async_tree_io           | 1.60 sec                                                     | 837 ms: 1.91x faster                                                 |
| async_tree_cpu_io_mixed | 936 ms                                                       | 564 ms: 1.66x faster                                                 |
| Geometric mean          | (ref)                                                        | 1.92x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 80.3 ms: 1.67x faster                                                |
| float          | 111 ms                                                       | 78.1 ms: 1.42x faster                                                |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                        | 1.37x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 147 ms: 1.29x faster                                                 |
| regex_dna      | 261 ms                                                       | 247 ms: 1.06x faster                                                 |
| regex_v8       | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                |
| regex_effbot   | 3.09 ms                                                      | 3.47 ms: 1.12x slower                                                |
| Geometric mean | (ref)                                                        | 1.07x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 220 us: 1.42x faster                                                 |
| json_dumps           | 14.5 ms                                                      | 10.5 ms: 1.39x faster                                                |
| pickle_pure_python   | 455 us                                                       | 335 us: 1.36x faster                                                 |
| xml_etree_process    | 75.9 ms                                                      | 56.6 ms: 1.34x faster                                                |
| tomli_loads          | 2.92 sec                                                     | 2.18 sec: 1.34x faster                                               |
| json_loads           | 30.3 us                                                      | 23.9 us: 1.27x faster                                                |
| xml_etree_generate   | 92.3 ms                                                      | 79.4 ms: 1.16x faster                                                |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.08x faster                                                 |
| unpickle_list        | 4.65 us                                                      | 4.75 us: 1.02x slower                                                |
| pickle_dict          | 29.5 us                                                      | 30.2 us: 1.02x slower                                                |
| pickle_list          | 4.12 us                                                      | 4.25 us: 1.03x slower                                                |
| pickle               | 9.89 us                                                      | 10.3 us: 1.05x slower                                                |
| unpickle             | 13.5 us                                                      | 15.7 us: 1.16x slower                                                |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.99 ms: 1.23x slower                                                |
| python_startup         | 11.5 ms                                                      | 14.9 ms: 1.30x slower                                                |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.15 ms: 1.61x faster                                                |
| django_template | 50.2 ms                                                      | 42.5 ms: 1.18x faster                                                |
| genshi_text     | 31.4 ms                                                      | 28.9 ms: 1.09x faster                                                |
| genshi_xml      | 63.3 ms                                                      | 64.8 ms: 1.02x slower                                                |
| Geometric mean  | (ref)                                                        | 1.19x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 181 us: 2.96x faster                                                 |
| deltablue                | 7.50 ms                                                      | 3.24 ms: 2.31x faster                                                |
| async_tree_none          | 692 ms                                                       | 322 ms: 2.15x faster                                                 |
| asyncio_tcp              | 779 ms                                                       | 377 ms: 2.07x faster                                                 |
| async_tree_memoization   | 819 ms                                                       | 411 ms: 1.99x faster                                                 |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                               |
| async_tree_io            | 1.60 sec                                                     | 837 ms: 1.91x faster                                                 |
| logging_silent           | 167 ns                                                       | 90.2 ns: 1.86x faster                                                |
| deepcopy_memo            | 49.8 us                                                      | 28.1 us: 1.77x faster                                                |
| go                       | 262 ms                                                       | 152 ms: 1.73x faster                                                 |
| scimark_lu               | 167 ms                                                       | 97.0 ms: 1.72x faster                                                |
| scimark_sor              | 180 ms                                                       | 106 ms: 1.71x faster                                                 |
| richards_super           | 90.6 ms                                                      | 53.3 ms: 1.70x faster                                                |
| crypto_pyaes             | 119 ms                                                       | 71.1 ms: 1.68x faster                                                |
| nbody                    | 134 ms                                                       | 80.3 ms: 1.67x faster                                                |
| richards                 | 75.1 ms                                                      | 45.0 ms: 1.67x faster                                                |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 564 ms: 1.66x faster                                                 |
| pyflate                  | 733 ms                                                       | 450 ms: 1.63x faster                                                 |
| mako                     | 14.7 ms                                                      | 9.15 ms: 1.61x faster                                                |
| chaos                    | 109 ms                                                       | 68.4 ms: 1.59x faster                                                |
| scimark_monte_carlo      | 107 ms                                                       | 68.3 ms: 1.57x faster                                                |
| deepcopy                 | 468 us                                                       | 302 us: 1.55x faster                                                 |
| spectral_norm            | 139 ms                                                       | 90.2 ms: 1.54x faster                                                |
| raytrace                 | 489 ms                                                       | 324 ms: 1.51x faster                                                 |
| sqlglot_parse            | 2.24 ms                                                      | 1.50 ms: 1.49x faster                                                |
| generators               | 57.3 ms                                                      | 39.8 ms: 1.44x faster                                                |
| float                    | 111 ms                                                       | 78.1 ms: 1.42x faster                                                |
| unpickle_pure_python     | 312 us                                                       | 220 us: 1.42x faster                                                 |
| coroutines               | 30.3 ms                                                      | 21.5 ms: 1.41x faster                                                |
| json_dumps               | 14.5 ms                                                      | 10.5 ms: 1.39x faster                                                |
| comprehensions           | 26.7 us                                                      | 19.4 us: 1.37x faster                                                |
| pathlib                  | 21.4 ms                                                      | 15.7 ms: 1.36x faster                                                |
| sqlglot_transpile        | 2.68 ms                                                      | 1.97 ms: 1.36x faster                                                |
| pickle_pure_python       | 455 us                                                       | 335 us: 1.36x faster                                                 |
| pylint                   | 566 ms                                                       | 418 ms: 1.35x faster                                                 |
| deepcopy_reduce          | 4.01 us                                                      | 2.98 us: 1.35x faster                                                |
| xml_etree_process        | 75.9 ms                                                      | 56.6 ms: 1.34x faster                                                |
| tomli_loads              | 2.92 sec                                                     | 2.18 sec: 1.34x faster                                               |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.33x faster                                               |
| thrift                   | 1.18 ms                                                      | 883 us: 1.33x faster                                                 |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                               |
| logging_format           | 9.64 us                                                      | 7.28 us: 1.32x faster                                                |
| html5lib                 | 94.6 ms                                                      | 71.5 ms: 1.32x faster                                                |
| pprint_safe_repr         | 1.05 sec                                                     | 794 ms: 1.32x faster                                                 |
| logging_simple           | 8.88 us                                                      | 6.71 us: 1.32x faster                                                |
| hexiom                   | 9.42 ms                                                      | 7.13 ms: 1.32x faster                                                |
| fannkuch                 | 483 ms                                                       | 367 ms: 1.32x faster                                                 |
| scimark_fft              | 361 ms                                                       | 278 ms: 1.30x faster                                                 |
| regex_compile            | 190 ms                                                       | 147 ms: 1.29x faster                                                 |
| tornado_http             | 157 ms                                                       | 122 ms: 1.28x faster                                                 |
| json_loads               | 30.3 us                                                      | 23.9 us: 1.27x faster                                                |
| dulwich_log              | 81.1 ms                                                      | 65.9 ms: 1.23x faster                                                |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.13 ms: 1.23x faster                                                |
| django_template          | 50.2 ms                                                      | 42.5 ms: 1.18x faster                                                |
| bench_thread_pool        | 1.14 ms                                                      | 968 us: 1.18x faster                                                 |
| xml_etree_generate       | 92.3 ms                                                      | 79.4 ms: 1.16x faster                                                |
| mdp                      | 3.01 sec                                                     | 2.62 sec: 1.15x faster                                               |
| sympy_expand             | 600 ms                                                       | 526 ms: 1.14x faster                                                 |
| json                     | 5.86 ms                                                      | 5.17 ms: 1.13x faster                                                |
| sympy_str                | 360 ms                                                       | 320 ms: 1.13x faster                                                 |
| nqueens                  | 115 ms                                                       | 102 ms: 1.12x faster                                                 |
| 2to3                     | 350 ms                                                       | 316 ms: 1.11x faster                                                 |
| sympy_sum                | 193 ms                                                       | 174 ms: 1.11x faster                                                 |
| sqlite_synth             | 2.99 us                                                      | 2.71 us: 1.10x faster                                                |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.10x faster                                                 |
| async_generators         | 421 ms                                                       | 386 ms: 1.09x faster                                                 |
| genshi_text              | 31.4 ms                                                      | 28.9 ms: 1.09x faster                                                |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.08x faster                                                 |
| pidigits                 | 271 ms                                                       | 252 ms: 1.08x faster                                                 |
| sqlglot_normalize        | 144 ms                                                       | 135 ms: 1.07x faster                                                 |
| docutils                 | 3.41 sec                                                     | 3.22 sec: 1.06x faster                                               |
| regex_dna                | 261 ms                                                       | 247 ms: 1.06x faster                                                 |
| regex_v8                 | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                |
| meteor_contest           | 138 ms                                                       | 134 ms: 1.03x faster                                                 |
| sympy_integrate          | 28.2 ms                                                      | 27.3 ms: 1.03x faster                                                |
| asyncio_websockets       | 390 ms                                                       | 383 ms: 1.02x faster                                                 |
| sqlglot_optimize         | 70.1 ms                                                      | 69.3 ms: 1.01x faster                                                |
| genshi_xml               | 63.3 ms                                                      | 64.8 ms: 1.02x slower                                                |
| unpickle_list            | 4.65 us                                                      | 4.75 us: 1.02x slower                                                |
| pickle_dict              | 29.5 us                                                      | 30.2 us: 1.02x slower                                                |
| pickle_list              | 4.12 us                                                      | 4.25 us: 1.03x slower                                                |
| pickle                   | 9.89 us                                                      | 10.3 us: 1.05x slower                                                |
| telco                    | 7.23 ms                                                      | 7.76 ms: 1.07x slower                                                |
| regex_effbot             | 3.09 ms                                                      | 3.47 ms: 1.12x slower                                                |
| unpickle                 | 13.5 us                                                      | 15.7 us: 1.16x slower                                                |
| python_startup_no_site   | 7.33 ms                                                      | 8.99 ms: 1.23x slower                                                |
| coverage                 | 63.3 ms                                                      | 78.4 ms: 1.24x slower                                                |
| python_startup           | 11.5 ms                                                      | 14.9 ms: 1.30x slower                                                |
| unpack_sequence          | 59.9 ns                                                      | 88.6 ns: 1.48x slower                                                |
| gc_traversal             | 3.42 ms                                                      | 5.17 ms: 1.51x slower                                                |
| create_gc_cycles         | 1.76 ms                                                      | 2.80 ms: 1.59x slower                                                |
| bench_mp_pool            | 6.37 ms                                                      | 2.97 sec: 466.32x slower                                             |
| Geometric mean           | (ref)                                                        | 1.19x faster                                                         |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.291x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.36x
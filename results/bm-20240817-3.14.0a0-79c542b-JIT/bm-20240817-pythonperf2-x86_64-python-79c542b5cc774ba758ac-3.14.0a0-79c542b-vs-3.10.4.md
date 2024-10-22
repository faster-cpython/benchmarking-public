# Results vs. 3.10.4

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-x86_64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 314 ms: 1.11x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.28 sec: 1.04x faster                                                      |
| html5lib       | 94.6 ms                                                      | 72.4 ms: 1.31x faster                                                       |
| tornado_http   | 157 ms                                                       | 122 ms: 1.28x faster                                                        |
| Geometric mean | (ref)                                                        | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 321 ms: 2.16x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 412 ms: 1.99x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 819 ms: 1.95x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 560 ms: 1.67x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.93x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 83.3 ms: 1.61x faster                                                       |
| float          | 111 ms                                                       | 75.0 ms: 1.48x faster                                                       |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 145 ms: 1.31x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.9 ms: 1.01x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.67 ms: 1.19x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 213 us: 1.46x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 319 us: 1.43x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.4 ms: 1.39x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.12 sec: 1.38x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 55.3 ms: 1.37x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.3 us: 1.20x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 77.7 ms: 1.19x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.14x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 98.0 ms: 1.13x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.29x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.16 ms: 1.61x faster                                                       |
| django_template | 50.2 ms                                                      | 42.1 ms: 1.19x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 30.3 ms: 1.04x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 64.5 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.18x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 188 us: 2.86x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.11 ms: 2.41x faster                                                       |
| async_tree_none          | 692 ms                                                       | 321 ms: 2.16x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 378 ms: 2.06x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 412 ms: 1.99x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 819 ms: 1.95x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 27.2 us: 1.83x faster                                                       |
| richards_super           | 90.6 ms                                                      | 50.7 ms: 1.79x faster                                                       |
| scimark_sor              | 180 ms                                                       | 101 ms: 1.78x faster                                                        |
| scimark_lu               | 167 ms                                                       | 95.2 ms: 1.75x faster                                                       |
| raytrace                 | 489 ms                                                       | 283 ms: 1.73x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 69.2 ms: 1.72x faster                                                       |
| richards                 | 75.1 ms                                                      | 43.8 ms: 1.71x faster                                                       |
| spectral_norm            | 139 ms                                                       | 82.1 ms: 1.69x faster                                                       |
| logging_silent           | 167 ns                                                       | 99.5 ns: 1.68x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 560 ms: 1.67x faster                                                        |
| chaos                    | 109 ms                                                       | 65.9 ms: 1.65x faster                                                       |
| nbody                    | 134 ms                                                       | 83.3 ms: 1.61x faster                                                       |
| go                       | 262 ms                                                       | 163 ms: 1.61x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.16 ms: 1.61x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 68.4 ms: 1.57x faster                                                       |
| deepcopy                 | 468 us                                                       | 301 us: 1.55x faster                                                        |
| pyflate                  | 733 ms                                                       | 475 ms: 1.54x faster                                                        |
| generators               | 57.3 ms                                                      | 37.8 ms: 1.52x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.48 ms: 1.51x faster                                                       |
| float                    | 111 ms                                                       | 75.0 ms: 1.48x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 213 us: 1.46x faster                                                        |
| comprehensions           | 26.7 us                                                      | 18.3 us: 1.46x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 319 us: 1.43x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.5 ms: 1.41x faster                                                       |
| pylint                   | 566 ms                                                       | 405 ms: 1.40x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.4 ms: 1.39x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.91 us: 1.38x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.12 sec: 1.38x faster                                                      |
| xml_etree_process        | 75.9 ms                                                      | 55.3 ms: 1.37x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.96 ms: 1.37x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.49 us: 1.37x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.95 ms: 1.36x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.16 us: 1.35x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.35x faster                                                       |
| fannkuch                 | 483 ms                                                       | 360 ms: 1.34x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                      |
| bench_mp_pool            | 6.37 ms                                                      | 4.84 ms: 1.32x faster                                                       |
| thrift                   | 1.18 ms                                                      | 898 us: 1.31x faster                                                        |
| regex_compile            | 190 ms                                                       | 145 ms: 1.31x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 72.4 ms: 1.31x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 804 ms: 1.31x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.68 sec: 1.29x faster                                                      |
| tornado_http             | 157 ms                                                       | 122 ms: 1.28x faster                                                        |
| scimark_fft              | 361 ms                                                       | 285 ms: 1.27x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.00 ms: 1.27x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 920 us: 1.24x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.3 us: 1.20x faster                                                       |
| django_template          | 50.2 ms                                                      | 42.1 ms: 1.19x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 77.7 ms: 1.19x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.58 sec: 1.17x faster                                                      |
| nqueens                  | 115 ms                                                       | 99.0 ms: 1.16x faster                                                       |
| sympy_str                | 360 ms                                                       | 315 ms: 1.14x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 141 ms: 1.14x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 98.0 ms: 1.13x faster                                                       |
| sympy_expand             | 600 ms                                                       | 535 ms: 1.12x faster                                                        |
| sympy_sum                | 193 ms                                                       | 172 ms: 1.12x faster                                                        |
| 2to3                     | 350 ms                                                       | 314 ms: 1.11x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 129 ms: 1.11x faster                                                        |
| json                     | 5.86 ms                                                      | 5.31 ms: 1.10x faster                                                       |
| async_generators         | 421 ms                                                       | 382 ms: 1.10x faster                                                        |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 65.9 ms: 1.06x faster                                                       |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.06x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 26.7 ms: 1.05x faster                                                       |
| docutils                 | 3.41 sec                                                     | 3.28 sec: 1.04x faster                                                      |
| genshi_text              | 31.4 ms                                                      | 30.3 ms: 1.04x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 26.9 ms: 1.01x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 396 ms: 1.02x slower                                                        |
| genshi_xml               | 63.3 ms                                                      | 64.5 ms: 1.02x slower                                                       |
| telco                    | 7.23 ms                                                      | 7.85 ms: 1.09x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.93 ms: 1.09x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.67 ms: 1.19x slower                                                       |
| coverage                 | 63.3 ms                                                      | 78.0 ms: 1.23x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.37 ms: 1.28x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.33x faster                                                                |

Benchmark hidden because not significant (1): regex_dna
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.23x
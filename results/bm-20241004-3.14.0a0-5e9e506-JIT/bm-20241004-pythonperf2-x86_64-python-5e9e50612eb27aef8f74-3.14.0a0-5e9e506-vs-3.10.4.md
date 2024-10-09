# Results vs. 3.10.4

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: linux-x86_64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 317 ms: 1.10x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.22 sec: 1.06x faster                                                      |
| html5lib       | 94.6 ms                                                      | 70.5 ms: 1.34x faster                                                       |
| tornado_http   | 157 ms                                                       | 122 ms: 1.29x faster                                                        |
| Geometric mean | (ref)                                                        | 1.19x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 324 ms: 2.13x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 402 ms: 2.04x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 820 ms: 1.95x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 575 ms: 1.63x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.93x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 84.3 ms: 1.59x faster                                                       |
| float          | 111 ms                                                       | 75.7 ms: 1.47x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.36x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 153 ms: 1.24x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                       |
| regex_dna      | 261 ms                                                       | 249 ms: 1.05x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.52 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 220 us: 1.42x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 324 us: 1.40x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.5 ms: 1.38x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.17 sec: 1.34x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 56.7 ms: 1.34x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.4 us: 1.24x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 79.1 ms: 1.17x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.10x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 148 ms: 1.08x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.60 us: 1.01x faster                                                       |
| pickle_list          | 4.12 us                                                      | 4.24 us: 1.03x slower                                                       |
| pickle               | 9.89 us                                                      | 10.2 us: 1.04x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 30.9 us: 1.05x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.5 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.5 ms: 1.17x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 8.97 ms: 1.22x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.16 ms: 1.61x faster                                                       |
| django_template | 50.2 ms                                                      | 42.9 ms: 1.17x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 29.7 ms: 1.06x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 64.9 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.18x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 181 us: 2.96x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.21 ms: 2.34x faster                                                       |
| async_tree_none          | 692 ms                                                       | 324 ms: 2.13x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 368 ms: 2.12x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 402 ms: 2.04x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 820 ms: 1.95x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 27.4 us: 1.81x faster                                                       |
| richards_super           | 90.6 ms                                                      | 51.5 ms: 1.76x faster                                                       |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.74x faster                                                        |
| logging_silent           | 167 ns                                                       | 97.5 ns: 1.72x faster                                                       |
| go                       | 262 ms                                                       | 154 ms: 1.70x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 70.2 ms: 1.70x faster                                                       |
| richards                 | 75.1 ms                                                      | 44.3 ms: 1.69x faster                                                       |
| scimark_lu               | 167 ms                                                       | 98.7 ms: 1.69x faster                                                       |
| spectral_norm            | 139 ms                                                       | 82.6 ms: 1.68x faster                                                       |
| chaos                    | 109 ms                                                       | 66.4 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 575 ms: 1.63x faster                                                        |
| pyflate                  | 733 ms                                                       | 452 ms: 1.62x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.16 ms: 1.61x faster                                                       |
| nbody                    | 134 ms                                                       | 84.3 ms: 1.59x faster                                                       |
| deepcopy                 | 468 us                                                       | 294 us: 1.59x faster                                                        |
| raytrace                 | 489 ms                                                       | 312 ms: 1.57x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 68.8 ms: 1.56x faster                                                       |
| generators               | 57.3 ms                                                      | 38.8 ms: 1.48x faster                                                       |
| float                    | 111 ms                                                       | 75.7 ms: 1.47x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.53 ms: 1.47x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 220 us: 1.42x faster                                                        |
| comprehensions           | 26.7 us                                                      | 18.8 us: 1.42x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.4 ms: 1.41x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 324 us: 1.40x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.5 ms: 1.38x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 768 ms: 1.37x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.97 ms: 1.36x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.53 us: 1.36x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.7 ms: 1.36x faster                                                       |
| fannkuch                 | 483 ms                                                       | 356 ms: 1.36x faster                                                        |
| pylint                   | 566 ms                                                       | 418 ms: 1.35x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.97 us: 1.35x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.17 us: 1.34x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 70.5 ms: 1.34x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.17 sec: 1.34x faster                                                      |
| xml_etree_process        | 75.9 ms                                                      | 56.7 ms: 1.34x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.34x faster                                                      |
| hexiom                   | 9.42 ms                                                      | 7.09 ms: 1.33x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.28 sec: 1.31x faster                                                      |
| thrift                   | 1.18 ms                                                      | 905 us: 1.30x faster                                                        |
| scimark_fft              | 361 ms                                                       | 278 ms: 1.30x faster                                                        |
| tornado_http             | 157 ms                                                       | 122 ms: 1.29x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 64.3 ms: 1.26x faster                                                       |
| regex_compile            | 190 ms                                                       | 153 ms: 1.24x faster                                                        |
| json_loads               | 30.3 us                                                      | 24.4 us: 1.24x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.13 ms: 1.23x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 954 us: 1.20x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.56 sec: 1.17x faster                                                      |
| django_template          | 50.2 ms                                                      | 42.9 ms: 1.17x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 79.1 ms: 1.17x faster                                                       |
| nqueens                  | 115 ms                                                       | 99.7 ms: 1.15x faster                                                       |
| sympy_expand             | 600 ms                                                       | 529 ms: 1.13x faster                                                        |
| sympy_str                | 360 ms                                                       | 319 ms: 1.13x faster                                                        |
| json                     | 5.86 ms                                                      | 5.22 ms: 1.12x faster                                                       |
| sympy_sum                | 193 ms                                                       | 173 ms: 1.12x faster                                                        |
| 2to3                     | 350 ms                                                       | 317 ms: 1.10x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 131 ms: 1.10x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.72 us: 1.10x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.10x faster                                                        |
| async_generators         | 421 ms                                                       | 385 ms: 1.09x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 148 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.22 sec: 1.06x faster                                                      |
| genshi_text              | 31.4 ms                                                      | 29.7 ms: 1.06x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                       |
| regex_dna                | 261 ms                                                       | 249 ms: 1.05x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 27.2 ms: 1.03x faster                                                       |
| meteor_contest           | 138 ms                                                       | 134 ms: 1.03x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 69.4 ms: 1.01x faster                                                       |
| unpickle_list            | 4.65 us                                                      | 4.60 us: 1.01x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 64.9 ms: 1.03x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.24 us: 1.03x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.2 us: 1.04x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 30.9 us: 1.05x slower                                                       |
| telco                    | 7.23 ms                                                      | 7.65 ms: 1.06x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.87 ms: 1.06x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.52 ms: 1.14x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.5 us: 1.15x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.5 ms: 1.17x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.97 ms: 1.22x slower                                                       |
| coverage                 | 63.3 ms                                                      | 84.0 ms: 1.33x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.62 ms: 1.35x slower                                                       |
| unpack_sequence          | 59.9 ns                                                      | 88.0 ns: 1.47x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 1.57 sec: 246.83x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.21x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.19x
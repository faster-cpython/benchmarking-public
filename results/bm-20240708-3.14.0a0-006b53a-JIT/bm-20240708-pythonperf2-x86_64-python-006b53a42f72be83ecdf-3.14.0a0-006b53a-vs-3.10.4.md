# Results vs. 3.10.4

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: linux-x86_64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 306 ms: 1.15x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.11 sec: 1.10x faster                                                      |
| html5lib       | 94.6 ms                                                      | 71.4 ms: 1.32x faster                                                       |
| tornado_http   | 157 ms                                                       | 121 ms: 1.29x faster                                                        |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 336 ms: 2.06x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 405 ms: 2.03x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 810 ms: 1.97x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 577 ms: 1.62x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.91x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 83.1 ms: 1.61x faster                                                       |
| float          | 111 ms                                                       | 75.7 ms: 1.47x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.38x faster                                                        |
| regex_dna      | 261 ms                                                       | 256 ms: 1.02x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.8 ms: 1.01x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 217 us: 1.44x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 318 us: 1.43x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 58.5 ms: 1.30x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 82.1 ms: 1.12x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 99.0 ms: 1.12x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.08 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.21 ms: 1.60x faster                                                       |
| django_template | 50.2 ms                                                      | 42.1 ms: 1.19x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 28.5 ms: 1.10x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 63.8 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 184 us: 2.91x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 375 ms: 2.08x faster                                                        |
| async_tree_none          | 692 ms                                                       | 336 ms: 2.06x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.70 ms: 2.03x faster                                                       |
| async_tree_memoization   | 819 ms                                                       | 405 ms: 2.03x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 810 ms: 1.97x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| deepcopy_memo            | 49.8 us                                                      | 28.0 us: 1.78x faster                                                       |
| raytrace                 | 489 ms                                                       | 286 ms: 1.71x faster                                                        |
| richards_super           | 90.6 ms                                                      | 53.6 ms: 1.69x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 70.7 ms: 1.69x faster                                                       |
| spectral_norm            | 139 ms                                                       | 82.9 ms: 1.68x faster                                                       |
| richards                 | 75.1 ms                                                      | 44.9 ms: 1.67x faster                                                       |
| logging_silent           | 167 ns                                                       | 101 ns: 1.66x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 64.8 ms: 1.66x faster                                                       |
| chaos                    | 109 ms                                                       | 65.6 ms: 1.66x faster                                                       |
| pyflate                  | 733 ms                                                       | 443 ms: 1.65x faster                                                        |
| generators               | 57.3 ms                                                      | 34.7 ms: 1.65x faster                                                       |
| go                       | 262 ms                                                       | 161 ms: 1.63x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 577 ms: 1.62x faster                                                        |
| nbody                    | 134 ms                                                       | 83.1 ms: 1.61x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.21 ms: 1.60x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.58x faster                                                       |
| pylint                   | 566 ms                                                       | 371 ms: 1.52x faster                                                        |
| deepcopy                 | 468 us                                                       | 310 us: 1.51x faster                                                        |
| scimark_lu               | 167 ms                                                       | 112 ms: 1.49x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.82 ms: 1.47x faster                                                       |
| float                    | 111 ms                                                       | 75.7 ms: 1.47x faster                                                       |
| comprehensions           | 26.7 us                                                      | 18.2 us: 1.46x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.1 ms: 1.44x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 217 us: 1.44x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 318 us: 1.43x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.64 ms: 1.42x faster                                                       |
| scimark_sor              | 180 ms                                                       | 128 ms: 1.40x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.39 us: 1.39x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                                      |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.38x faster                                                      |
| regex_compile            | 190 ms                                                       | 138 ms: 1.38x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.09 us: 1.36x faster                                                       |
| fannkuch                 | 483 ms                                                       | 358 ms: 1.35x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 71.4 ms: 1.32x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.05 us: 1.31x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.3 ms: 1.31x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.31x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 805 ms: 1.30x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 58.5 ms: 1.30x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.91 ms: 1.30x faster                                                       |
| tornado_http             | 157 ms                                                       | 121 ms: 1.29x faster                                                        |
| thrift                   | 1.18 ms                                                      | 918 us: 1.28x faster                                                        |
| scimark_fft              | 361 ms                                                       | 291 ms: 1.24x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 921 us: 1.24x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.17 ms: 1.22x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 67.2 ms: 1.21x faster                                                       |
| django_template          | 50.2 ms                                                      | 42.1 ms: 1.19x faster                                                       |
| nqueens                  | 115 ms                                                       | 96.5 ms: 1.19x faster                                                       |
| dask                     | 472 ms                                                       | 400 ms: 1.18x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.55 sec: 1.18x faster                                                      |
| sympy_str                | 360 ms                                                       | 312 ms: 1.15x faster                                                        |
| sympy_sum                | 193 ms                                                       | 168 ms: 1.15x faster                                                        |
| 2to3                     | 350 ms                                                       | 306 ms: 1.15x faster                                                        |
| sympy_expand             | 600 ms                                                       | 526 ms: 1.14x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 82.1 ms: 1.12x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 128 ms: 1.12x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 99.0 ms: 1.12x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 63.0 ms: 1.11x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 28.5 ms: 1.10x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 25.6 ms: 1.10x faster                                                       |
| docutils                 | 3.41 sec                                                     | 3.11 sec: 1.10x faster                                                      |
| async_generators         | 421 ms                                                       | 385 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| json                     | 5.86 ms                                                      | 5.46 ms: 1.07x faster                                                       |
| meteor_contest           | 138 ms                                                       | 129 ms: 1.07x faster                                                        |
| regex_dna                | 261 ms                                                       | 256 ms: 1.02x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.8 ms: 1.01x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 63.8 ms: 1.01x slower                                                       |
| asyncio_websockets       | 390 ms                                                       | 394 ms: 1.01x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.92 ms: 1.09x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.07 ms: 1.12x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.08 ms: 1.24x slower                                                       |
| coverage                 | 63.3 ms                                                      | 78.8 ms: 1.25x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.31 ms: 1.26x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.33x faster                                                                |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240708-3.14.0a0-006b53a-JIT/bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.20x
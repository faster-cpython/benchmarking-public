# Results vs. 3.10.4

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: linux-x86_64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 305 ms: 1.15x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.08 sec: 1.11x faster                                                      |
| html5lib       | 94.6 ms                                                      | 72.1 ms: 1.31x faster                                                       |
| tornado_http   | 157 ms                                                       | 121 ms: 1.29x faster                                                        |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 342 ms: 2.02x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 410 ms: 2.00x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 818 ms: 1.95x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 581 ms: 1.61x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.89x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 81.8 ms: 1.64x faster                                                       |
| float          | 111 ms                                                       | 75.2 ms: 1.48x faster                                                       |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.38x faster                                                        |
| regex_dna      | 261 ms                                                       | 237 ms: 1.10x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 311 us: 1.46x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 216 us: 1.44x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.08 sec: 1.40x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 58.7 ms: 1.29x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.4 us: 1.19x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 82.3 ms: 1.12x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 99.4 ms: 1.11x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.22 ms: 1.60x faster                                                       |
| django_template | 50.2 ms                                                      | 42.1 ms: 1.19x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 29.1 ms: 1.08x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 65.5 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 183 us: 2.93x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 379 ms: 2.06x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.69 ms: 2.03x faster                                                       |
| async_tree_none          | 692 ms                                                       | 342 ms: 2.02x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 410 ms: 2.00x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 818 ms: 1.95x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 28.6 us: 1.74x faster                                                       |
| richards_super           | 90.6 ms                                                      | 52.7 ms: 1.72x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 69.8 ms: 1.71x faster                                                       |
| logging_silent           | 167 ns                                                       | 100 ns: 1.67x faster                                                        |
| chaos                    | 109 ms                                                       | 65.1 ms: 1.67x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 64.5 ms: 1.67x faster                                                       |
| generators               | 57.3 ms                                                      | 34.5 ms: 1.66x faster                                                       |
| spectral_norm            | 139 ms                                                       | 84.0 ms: 1.66x faster                                                       |
| raytrace                 | 489 ms                                                       | 296 ms: 1.65x faster                                                        |
| richards                 | 75.1 ms                                                      | 45.8 ms: 1.64x faster                                                       |
| nbody                    | 134 ms                                                       | 81.8 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 581 ms: 1.61x faster                                                        |
| pyflate                  | 733 ms                                                       | 455 ms: 1.61x faster                                                        |
| go                       | 262 ms                                                       | 163 ms: 1.61x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.22 ms: 1.60x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.40 ms: 1.59x faster                                                       |
| pylint                   | 566 ms                                                       | 369 ms: 1.53x faster                                                        |
| deepcopy                 | 468 us                                                       | 307 us: 1.52x faster                                                        |
| float                    | 111 ms                                                       | 75.2 ms: 1.48x faster                                                       |
| comprehensions           | 26.7 us                                                      | 18.1 us: 1.48x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.82 ms: 1.48x faster                                                       |
| scimark_sor              | 180 ms                                                       | 123 ms: 1.47x faster                                                        |
| scimark_lu               | 167 ms                                                       | 114 ms: 1.46x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 311 us: 1.46x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 216 us: 1.44x faster                                                        |
| fannkuch                 | 483 ms                                                       | 337 ms: 1.43x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.68 ms: 1.41x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.08 sec: 1.40x faster                                                      |
| coroutines               | 30.3 ms                                                      | 21.9 ms: 1.39x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.45 us: 1.38x faster                                                       |
| regex_compile            | 190 ms                                                       | 138 ms: 1.38x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.99 us: 1.34x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.19 us: 1.34x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.81 ms: 1.32x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                                      |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 795 ms: 1.32x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 72.1 ms: 1.31x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.3 ms: 1.31x faster                                                       |
| thrift                   | 1.18 ms                                                      | 905 us: 1.30x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 58.7 ms: 1.29x faster                                                       |
| tornado_http             | 157 ms                                                       | 121 ms: 1.29x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 3.97 ms: 1.28x faster                                                       |
| scimark_fft              | 361 ms                                                       | 289 ms: 1.25x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 920 us: 1.24x faster                                                        |
| nqueens                  | 115 ms                                                       | 93.5 ms: 1.23x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 66.2 ms: 1.22x faster                                                       |
| django_template          | 50.2 ms                                                      | 42.1 ms: 1.19x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.4 us: 1.19x faster                                                       |
| dask                     | 472 ms                                                       | 396 ms: 1.19x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.55 sec: 1.18x faster                                                      |
| sympy_sum                | 193 ms                                                       | 164 ms: 1.17x faster                                                        |
| sympy_str                | 360 ms                                                       | 310 ms: 1.16x faster                                                        |
| 2to3                     | 350 ms                                                       | 305 ms: 1.15x faster                                                        |
| sympy_expand             | 600 ms                                                       | 523 ms: 1.15x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 82.3 ms: 1.12x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 129 ms: 1.12x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 62.9 ms: 1.11x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 99.4 ms: 1.11x faster                                                       |
| docutils                 | 3.41 sec                                                     | 3.08 sec: 1.11x faster                                                      |
| sympy_integrate          | 28.2 ms                                                      | 25.5 ms: 1.10x faster                                                       |
| regex_dna                | 261 ms                                                       | 237 ms: 1.10x faster                                                        |
| async_generators         | 421 ms                                                       | 386 ms: 1.09x faster                                                        |
| json                     | 5.86 ms                                                      | 5.39 ms: 1.09x faster                                                       |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 29.1 ms: 1.08x faster                                                       |
| meteor_contest           | 138 ms                                                       | 129 ms: 1.07x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 394 ms: 1.01x slower                                                        |
| genshi_xml               | 63.3 ms                                                      | 65.5 ms: 1.03x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.96 ms: 1.11x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.09 ms: 1.12x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                       |
| coverage                 | 63.3 ms                                                      | 83.8 ms: 1.33x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.67 ms: 1.37x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.33x faster                                                                |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240708-3.14.0a0-006b53a-JIT/bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.19x
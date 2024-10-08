# Results vs. 3.10.4

- fork: python
- ref: e256a7590a0149feadfe
- machine: linux-x86_64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.32x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| html5lib       | 94.6 ms                                                      | 71.4 ms: 1.32x faster                                                       |
| tornado_http   | 157 ms                                                       | 116 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 322 ms: 2.15x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 399 ms: 2.05x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 809 ms: 1.97x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 572 ms: 1.64x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.94x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 88.6 ms: 1.51x faster                                                       |
| float          | 111 ms                                                       | 79.6 ms: 1.40x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.37x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.5 ms: 1.06x faster                                                       |
| regex_dna      | 261 ms                                                       | 248 ms: 1.05x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.58 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 213 us: 1.47x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 321 us: 1.42x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 59.9 ms: 1.27x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 142 ms: 1.13x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.64 sec: 1.10x faster                                                      |
| xml_etree_generate   | 92.3 ms                                                      | 84.8 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.08x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.57 us: 1.02x faster                                                       |
| pickle_dict          | 29.5 us                                                      | 30.0 us: 1.02x slower                                                       |
| pickle               | 9.89 us                                                      | 10.2 us: 1.03x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.30 us: 1.04x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.1 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 8.95 ms: 1.22x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 24.6 ms: 1.28x faster                                                       |
| django_template | 50.2 ms                                                      | 40.8 ms: 1.23x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 54.4 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 172 us: 3.11x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.40 ms: 2.20x faster                                                       |
| async_tree_none          | 692 ms                                                       | 322 ms: 2.15x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 369 ms: 2.11x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 399 ms: 2.05x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 809 ms: 1.97x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.57 sec: 1.97x faster                                                      |
| generators               | 57.3 ms                                                      | 29.7 ms: 1.93x faster                                                       |
| go                       | 262 ms                                                       | 138 ms: 1.89x faster                                                        |
| chaos                    | 109 ms                                                       | 62.0 ms: 1.75x faster                                                       |
| scimark_lu               | 167 ms                                                       | 96.0 ms: 1.74x faster                                                       |
| raytrace                 | 489 ms                                                       | 283 ms: 1.73x faster                                                        |
| logging_silent           | 167 ns                                                       | 97.9 ns: 1.71x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 30.0 us: 1.66x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 71.9 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 572 ms: 1.64x faster                                                        |
| deepcopy                 | 468 us                                                       | 286 us: 1.64x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 66.0 ms: 1.63x faster                                                       |
| pylint                   | 566 ms                                                       | 349 ms: 1.62x faster                                                        |
| richards_super           | 90.6 ms                                                      | 56.0 ms: 1.62x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.43 ms: 1.56x faster                                                       |
| scimark_sor              | 180 ms                                                       | 115 ms: 1.56x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.2 us: 1.55x faster                                                       |
| nbody                    | 134 ms                                                       | 88.6 ms: 1.51x faster                                                       |
| richards                 | 75.1 ms                                                      | 49.7 ms: 1.51x faster                                                       |
| pyflate                  | 733 ms                                                       | 487 ms: 1.51x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.33 ms: 1.49x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.81 ms: 1.48x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 213 us: 1.47x faster                                                        |
| spectral_norm            | 139 ms                                                       | 96.4 ms: 1.44x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 321 us: 1.42x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.6 ms: 1.40x faster                                                       |
| float                    | 111 ms                                                       | 79.6 ms: 1.40x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.89 us: 1.39x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.62 ms: 1.38x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.50 us: 1.37x faster                                                       |
| regex_compile            | 190 ms                                                       | 139 ms: 1.37x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.7 ms: 1.36x faster                                                       |
| thrift                   | 1.18 ms                                                      | 863 us: 1.36x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                      |
| tornado_http             | 157 ms                                                       | 116 ms: 1.35x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.21 us: 1.34x faster                                                       |
| fannkuch                 | 483 ms                                                       | 361 ms: 1.34x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 71.4 ms: 1.32x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 865 us: 1.32x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.32x faster                                                      |
| nqueens                  | 115 ms                                                       | 87.6 ms: 1.31x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 803 ms: 1.31x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 24.6 ms: 1.28x faster                                                       |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 59.9 ms: 1.27x faster                                                       |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                        |
| 2to3                     | 350 ms                                                       | 284 ms: 1.23x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.8 ms: 1.23x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.23x faster                                                        |
| django_template          | 50.2 ms                                                      | 40.8 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.16 ms: 1.22x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 66.9 ms: 1.21x faster                                                       |
| scimark_fft              | 361 ms                                                       | 298 ms: 1.21x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.49 sec: 1.21x faster                                                      |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| sympy_expand             | 600 ms                                                       | 498 ms: 1.20x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 58.3 ms: 1.20x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| async_generators         | 421 ms                                                       | 358 ms: 1.17x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 54.4 ms: 1.16x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 142 ms: 1.13x faster                                                        |
| json                     | 5.86 ms                                                      | 5.26 ms: 1.11x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.64 sec: 1.10x faster                                                      |
| sqlite_synth             | 2.99 us                                                      | 2.73 us: 1.09x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 84.8 ms: 1.09x faster                                                       |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.5 ms: 1.06x faster                                                       |
| regex_dna                | 261 ms                                                       | 248 ms: 1.05x faster                                                        |
| unpickle_list            | 4.65 us                                                      | 4.57 us: 1.02x faster                                                       |
| pickle_dict              | 29.5 us                                                      | 30.0 us: 1.02x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.2 us: 1.03x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.30 us: 1.04x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.1 us: 1.12x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.01 ms: 1.14x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.29 ms: 1.15x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.58 ms: 1.16x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.95 ms: 1.22x slower                                                       |
| coverage                 | 63.3 ms                                                      | 82.6 ms: 1.30x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.78 ms: 1.40x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.32x faster                                                                |

Benchmark hidden because not significant (2): asyncio_websockets, unpack_sequence
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.12x
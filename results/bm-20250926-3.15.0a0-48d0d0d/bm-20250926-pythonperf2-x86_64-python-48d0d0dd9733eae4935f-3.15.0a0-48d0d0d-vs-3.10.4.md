# Results vs. 3.10.4

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: linux-x86_64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.348x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 278 ms: 1.26x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                      |
| html5lib       | 94.6 ms                                                      | 64.9 ms: 1.46x faster                                                       |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 614 ms: 2.60x faster                                                        |
| async_tree_none         | 692 ms                                                       | 271 ms: 2.55x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 328 ms: 2.50x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 501 ms: 1.87x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 67.3 ms: 1.65x faster                                                       |
| nbody          | 134 ms                                                       | 91.2 ms: 1.47x faster                                                       |
| pidigits       | 271 ms                                                       | 254 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 131 ms: 1.45x faster                                                        |
| regex_dna      | 261 ms                                                       | 222 ms: 1.17x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.5 ms: 1.16x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.42 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                        | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 206 us: 1.51x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.98 sec: 1.47x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 9.92 ms: 1.47x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 325 us: 1.40x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 57.6 ms: 1.32x faster                                                       |
| json_loads           | 30.3 us                                                      | 26.1 us: 1.16x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 82.5 ms: 1.12x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 99.3 ms: 1.11x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.09x faster                                                        |
| unpickle             | 13.5 us                                                      | 14.6 us: 1.08x slower                                                       |
| unpickle_list        | 4.65 us                                                      | 5.07 us: 1.09x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 33.5 us: 1.14x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.84 us: 1.18x slower                                                       |
| pickle               | 9.89 us                                                      | 12.5 us: 1.26x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.83 ms: 1.21x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 34.6 ms: 1.45x faster                                                       |
| mako            | 14.7 ms                                                      | 10.8 ms: 1.37x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.2 ms: 1.35x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 52.4 ms: 1.21x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.34x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 167 us: 3.20x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 614 ms: 2.60x faster                                                        |
| async_tree_none          | 692 ms                                                       | 271 ms: 2.55x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 328 ms: 2.50x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.17 ms: 2.36x faster                                                       |
| mdp                      | 3.01 sec                                                     | 1.27 sec: 2.36x faster                                                      |
| go                       | 262 ms                                                       | 117 ms: 2.24x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 368 ms: 2.12x faster                                                        |
| generators               | 57.3 ms                                                      | 28.1 ms: 2.04x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 25.3 us: 1.96x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 501 ms: 1.87x faster                                                        |
| chaos                    | 109 ms                                                       | 58.8 ms: 1.85x faster                                                       |
| logging_silent           | 167 ns                                                       | 91.8 ns: 1.82x faster                                                       |
| pyflate                  | 733 ms                                                       | 405 ms: 1.81x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 59.3 ms: 1.81x faster                                                       |
| raytrace                 | 489 ms                                                       | 271 ms: 1.80x faster                                                        |
| richards_super           | 90.6 ms                                                      | 50.4 ms: 1.80x faster                                                       |
| pylint                   | 566 ms                                                       | 317 ms: 1.78x faster                                                        |
| scimark_lu               | 167 ms                                                       | 93.7 ms: 1.78x faster                                                       |
| scimark_sor              | 180 ms                                                       | 101 ms: 1.78x faster                                                        |
| deepcopy                 | 468 us                                                       | 264 us: 1.77x faster                                                        |
| richards                 | 75.1 ms                                                      | 44.6 ms: 1.68x faster                                                       |
| float                    | 111 ms                                                       | 67.3 ms: 1.65x faster                                                       |
| comprehensions           | 26.7 us                                                      | 16.3 us: 1.63x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 5.77 ms: 1.63x faster                                                       |
| spectral_norm            | 139 ms                                                       | 85.9 ms: 1.62x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 76.5 ms: 1.56x faster                                                       |
| logging_simple           | 8.88 us                                                      | 5.86 us: 1.52x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 206 us: 1.51x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.43 us: 1.50x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.98 sec: 1.47x faster                                                      |
| nbody                    | 134 ms                                                       | 91.2 ms: 1.47x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 9.92 ms: 1.47x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 64.9 ms: 1.46x faster                                                       |
| regex_compile            | 190 ms                                                       | 131 ms: 1.45x faster                                                        |
| django_template          | 50.2 ms                                                      | 34.6 ms: 1.45x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.51 sec: 1.42x faster                                                      |
| pathlib                  | 21.4 ms                                                      | 15.0 ms: 1.42x faster                                                       |
| thrift                   | 1.18 ms                                                      | 830 us: 1.42x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 743 ms: 1.41x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 42.7 ns: 1.40x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 325 us: 1.40x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.9 ms: 1.38x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.91 us: 1.38x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 59.0 ms: 1.37x faster                                                       |
| fannkuch                 | 483 ms                                                       | 351 ms: 1.37x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.8 ms: 1.37x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                      |
| genshi_text              | 31.4 ms                                                      | 23.2 ms: 1.35x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 57.6 ms: 1.32x faster                                                       |
| scimark_fft              | 361 ms                                                       | 279 ms: 1.29x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 21.8 ms: 1.29x faster                                                       |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.29x faster                                                        |
| nqueens                  | 115 ms                                                       | 90.1 ms: 1.28x faster                                                       |
| sympy_str                | 360 ms                                                       | 283 ms: 1.27x faster                                                        |
| 2to3                     | 350 ms                                                       | 278 ms: 1.26x faster                                                        |
| sympy_expand             | 600 ms                                                       | 481 ms: 1.25x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 938 us: 1.22x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 52.4 ms: 1.21x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                      |
| regex_dna                | 261 ms                                                       | 222 ms: 1.17x faster                                                        |
| meteor_contest           | 138 ms                                                       | 118 ms: 1.17x faster                                                        |
| json_loads               | 30.3 us                                                      | 26.1 us: 1.16x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 23.5 ms: 1.16x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 82.5 ms: 1.12x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 99.3 ms: 1.11x faster                                                       |
| json                     | 5.86 ms                                                      | 5.33 ms: 1.10x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.62 ms: 1.10x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 146 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 254 ms: 1.06x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                        |
| unpickle                 | 13.5 us                                                      | 14.6 us: 1.08x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 5.07 us: 1.09x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.42 ms: 1.11x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 33.5 us: 1.14x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.84 us: 1.18x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.83 ms: 1.21x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.5 us: 1.26x slower                                                       |
| coverage                 | 63.3 ms                                                      | 80.2 ms: 1.27x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.83 ms: 1.61x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.25 ms: 1.83x slower                                                       |
| telco                    | 7.23 ms                                                      | 155 ms: 21.46x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 2.46 sec: 385.80x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.24x faster                                                                |

Benchmark hidden because not significant (1): async_generators
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.348x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.39x
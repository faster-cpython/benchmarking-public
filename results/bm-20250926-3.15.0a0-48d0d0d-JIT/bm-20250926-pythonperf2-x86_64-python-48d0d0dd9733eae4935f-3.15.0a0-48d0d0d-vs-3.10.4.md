# Results vs. 3.10.4

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: linux-x86_64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.342x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.88 sec: 1.18x faster                                                      |
| html5lib       | 94.6 ms                                                      | 65.9 ms: 1.44x faster                                                       |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 619 ms: 2.58x faster                                                        |
| async_tree_none         | 692 ms                                                       | 275 ms: 2.52x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 329 ms: 2.49x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 501 ms: 1.87x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.34x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 68.4 ms: 1.63x faster                                                       |
| nbody          | 134 ms                                                       | 97.7 ms: 1.37x faster                                                       |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 131 ms: 1.45x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.4 ms: 1.16x faster                                                       |
| regex_dna      | 261 ms                                                       | 231 ms: 1.13x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.67 ms: 1.19x slower                                                       |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 193 us: 1.62x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.89 sec: 1.54x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.0 ms: 1.45x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 325 us: 1.40x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 55.3 ms: 1.37x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 80.0 ms: 1.15x faster                                                       |
| json_loads           | 30.3 us                                                      | 26.4 us: 1.15x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 97.6 ms: 1.13x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 142 ms: 1.13x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.97 us: 1.07x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.0 us: 1.11x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 33.9 us: 1.15x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.98 us: 1.21x slower                                                       |
| pickle               | 9.89 us                                                      | 12.3 us: 1.25x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.88 ms: 1.21x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.5 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.28x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.90 ms: 1.49x faster                                                       |
| django_template | 50.2 ms                                                      | 35.0 ms: 1.43x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.2 ms: 1.36x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 53.6 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.36x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 169 us: 3.17x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 619 ms: 2.58x faster                                                        |
| async_tree_none          | 692 ms                                                       | 275 ms: 2.52x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 329 ms: 2.49x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.29 sec: 2.34x faster                                                      |
| deltablue                | 7.50 ms                                                      | 3.21 ms: 2.33x faster                                                       |
| go                       | 262 ms                                                       | 119 ms: 2.20x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 23.3 us: 2.14x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 371 ms: 2.10x faster                                                        |
| richards_super           | 90.6 ms                                                      | 44.5 ms: 2.03x faster                                                       |
| richards                 | 75.1 ms                                                      | 38.2 ms: 1.97x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.59 sec: 1.95x faster                                                      |
| generators               | 57.3 ms                                                      | 30.0 ms: 1.91x faster                                                       |
| pyflate                  | 733 ms                                                       | 392 ms: 1.87x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 501 ms: 1.87x faster                                                        |
| chaos                    | 109 ms                                                       | 59.1 ms: 1.84x faster                                                       |
| logging_silent           | 167 ns                                                       | 91.9 ns: 1.82x faster                                                       |
| scimark_lu               | 167 ms                                                       | 93.9 ms: 1.78x faster                                                       |
| pylint                   | 566 ms                                                       | 319 ms: 1.77x faster                                                        |
| scimark_sor              | 180 ms                                                       | 102 ms: 1.77x faster                                                        |
| deepcopy                 | 468 us                                                       | 268 us: 1.75x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 61.5 ms: 1.75x faster                                                       |
| raytrace                 | 489 ms                                                       | 284 ms: 1.72x faster                                                        |
| float                    | 111 ms                                                       | 68.4 ms: 1.63x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 193 us: 1.62x faster                                                        |
| spectral_norm            | 139 ms                                                       | 86.3 ms: 1.61x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 5.92 ms: 1.59x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 75.8 ms: 1.57x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.89 sec: 1.54x faster                                                      |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.53x faster                                                       |
| logging_simple           | 8.88 us                                                      | 5.90 us: 1.51x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.90 ms: 1.49x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.51 us: 1.48x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.0 ms: 1.45x faster                                                       |
| regex_compile            | 190 ms                                                       | 131 ms: 1.45x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.49 sec: 1.45x faster                                                      |
| html5lib                 | 94.6 ms                                                      | 65.9 ms: 1.44x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 731 ms: 1.43x faster                                                        |
| django_template          | 50.2 ms                                                      | 35.0 ms: 1.43x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.19 sec: 1.41x faster                                                      |
| pickle_pure_python       | 455 us                                                       | 325 us: 1.40x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.3 ms: 1.39x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 58.6 ms: 1.38x faster                                                       |
| thrift                   | 1.18 ms                                                      | 855 us: 1.37x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 55.3 ms: 1.37x faster                                                       |
| nbody                    | 134 ms                                                       | 97.7 ms: 1.37x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.93 us: 1.37x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 23.2 ms: 1.36x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.8 ms: 1.33x faster                                                       |
| scimark_fft              | 361 ms                                                       | 275 ms: 1.31x faster                                                        |
| fannkuch                 | 483 ms                                                       | 368 ms: 1.31x faster                                                        |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.27x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.3 ms: 1.26x faster                                                       |
| nqueens                  | 115 ms                                                       | 91.6 ms: 1.25x faster                                                       |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                        |
| 2to3                     | 350 ms                                                       | 284 ms: 1.23x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 939 us: 1.22x faster                                                        |
| sympy_expand             | 600 ms                                                       | 498 ms: 1.20x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.88 sec: 1.18x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 53.6 ms: 1.18x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 23.4 ms: 1.16x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 80.0 ms: 1.15x faster                                                       |
| json_loads               | 30.3 us                                                      | 26.4 us: 1.15x faster                                                       |
| meteor_contest           | 138 ms                                                       | 121 ms: 1.15x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 97.6 ms: 1.13x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 142 ms: 1.13x faster                                                        |
| regex_dna                | 261 ms                                                       | 231 ms: 1.13x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 53.2 ns: 1.13x faster                                                       |
| json                     | 5.86 ms                                                      | 5.45 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.74 ms: 1.07x faster                                                       |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.83 us: 1.06x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                        |
| async_generators         | 421 ms                                                       | 438 ms: 1.04x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 4.97 us: 1.07x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.0 us: 1.11x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 33.9 us: 1.15x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.67 ms: 1.19x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.98 us: 1.21x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.88 ms: 1.21x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.3 us: 1.25x slower                                                       |
| coverage                 | 63.3 ms                                                      | 81.4 ms: 1.29x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.5 ms: 1.34x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.90 ms: 1.64x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.73 ms: 1.97x slower                                                       |
| telco                    | 7.23 ms                                                      | 155 ms: 21.42x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 2.51 sec: 394.05x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.342x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.41x
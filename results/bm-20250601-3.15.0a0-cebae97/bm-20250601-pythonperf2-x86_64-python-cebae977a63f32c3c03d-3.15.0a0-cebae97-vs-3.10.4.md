# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.138x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 311 ms: 1.13x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.12 sec: 1.09x faster                                                      |
| html5lib       | 94.6 ms                                                      | 71.6 ms: 1.32x faster                                                       |
| Geometric mean | (ref)                                                        | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 689 ms: 2.32x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 358 ms: 2.29x faster                                                        |
| async_tree_none         | 692 ms                                                       | 307 ms: 2.25x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 655 ms: 1.43x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.03x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 80.6 ms: 1.38x faster                                                       |
| nbody          | 134 ms                                                       | 101 ms: 1.33x faster                                                        |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 154 ms: 1.24x faster                                                        |
| regex_dna      | 261 ms                                                       | 243 ms: 1.08x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 27.5 ms: 1.01x slower                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.36 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 239 us: 1.30x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.38 sec: 1.22x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 378 us: 1.20x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 72.6 ms: 1.05x faster                                                       |
| json_loads           | 30.3 us                                                      | 29.1 us: 1.04x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 14.4 ms: 1.01x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 168 ms: 1.05x slower                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 117 ms: 1.06x slower                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 107 ms: 1.15x slower                                                        |
| unpickle_list        | 4.65 us                                                      | 5.47 us: 1.18x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 36.4 us: 1.23x slower                                                       |
| unpickle             | 13.5 us                                                      | 17.6 us: 1.30x slower                                                       |
| pickle_list          | 4.12 us                                                      | 5.92 us: 1.44x slower                                                       |
| pickle               | 9.89 us                                                      | 14.7 us: 1.48x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.40 ms: 1.28x slower                                                       |
| python_startup         | 11.5 ms                                                      | 16.4 ms: 1.43x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.35x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 42.2 ms: 1.19x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 27.7 ms: 1.13x faster                                                       |
| mako            | 14.7 ms                                                      | 13.7 ms: 1.07x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 60.5 ms: 1.05x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.11x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 210 us: 2.56x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 689 ms: 2.32x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 358 ms: 2.29x faster                                                        |
| async_tree_none          | 692 ms                                                       | 307 ms: 2.25x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.46 ms: 2.17x faster                                                       |
| go                       | 262 ms                                                       | 127 ms: 2.07x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 378 ms: 2.06x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.55 sec: 1.94x faster                                                      |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.62 sec: 1.91x faster                                                      |
| generators               | 57.3 ms                                                      | 31.7 ms: 1.81x faster                                                       |
| pylint                   | 566 ms                                                       | 351 ms: 1.61x faster                                                        |
| pyflate                  | 733 ms                                                       | 469 ms: 1.56x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 32.2 us: 1.55x faster                                                       |
| chaos                    | 109 ms                                                       | 71.5 ms: 1.52x faster                                                       |
| richards_super           | 90.6 ms                                                      | 60.8 ms: 1.49x faster                                                       |
| raytrace                 | 489 ms                                                       | 331 ms: 1.48x faster                                                        |
| deepcopy                 | 468 us                                                       | 317 us: 1.48x faster                                                        |
| scimark_sor              | 180 ms                                                       | 124 ms: 1.45x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.50 ms: 1.45x faster                                                       |
| comprehensions           | 26.7 us                                                      | 18.6 us: 1.44x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 655 ms: 1.43x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 76.1 ms: 1.41x faster                                                       |
| richards                 | 75.1 ms                                                      | 53.9 ms: 1.39x faster                                                       |
| float                    | 111 ms                                                       | 80.6 ms: 1.38x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 87.9 ms: 1.36x faster                                                       |
| scimark_lu               | 167 ms                                                       | 123 ms: 1.35x faster                                                        |
| nbody                    | 134 ms                                                       | 101 ms: 1.33x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 71.6 ms: 1.32x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 239 us: 1.30x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 63.1 ms: 1.29x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.33 sec: 1.25x faster                                                      |
| coroutines               | 30.3 ms                                                      | 24.4 ms: 1.24x faster                                                       |
| regex_compile            | 190 ms                                                       | 154 ms: 1.24x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.38 sec: 1.22x faster                                                      |
| spectral_norm            | 139 ms                                                       | 114 ms: 1.22x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 378 us: 1.20x faster                                                        |
| django_template          | 50.2 ms                                                      | 42.2 ms: 1.19x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 23.8 ms: 1.19x faster                                                       |
| logging_simple           | 8.88 us                                                      | 7.55 us: 1.17x faster                                                       |
| thrift                   | 1.18 ms                                                      | 1.01 ms: 1.16x faster                                                       |
| logging_format           | 9.64 us                                                      | 8.33 us: 1.16x faster                                                       |
| sympy_sum                | 193 ms                                                       | 169 ms: 1.14x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.52 us: 1.14x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 27.7 ms: 1.13x faster                                                       |
| 2to3                     | 350 ms                                                       | 311 ms: 1.13x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.04 ms: 1.10x faster                                                       |
| docutils                 | 3.41 sec                                                     | 3.12 sec: 1.09x faster                                                      |
| pathlib                  | 21.4 ms                                                      | 19.5 ms: 1.09x faster                                                       |
| sympy_str                | 360 ms                                                       | 330 ms: 1.09x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 55.5 ns: 1.08x faster                                                       |
| regex_dna                | 261 ms                                                       | 243 ms: 1.08x faster                                                        |
| mako                     | 14.7 ms                                                      | 13.7 ms: 1.07x faster                                                       |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| nqueens                  | 115 ms                                                       | 108 ms: 1.07x faster                                                        |
| sympy_expand             | 600 ms                                                       | 571 ms: 1.05x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 72.6 ms: 1.05x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 60.5 ms: 1.05x faster                                                       |
| json_loads               | 30.3 us                                                      | 29.1 us: 1.04x faster                                                       |
| fannkuch                 | 483 ms                                                       | 463 ms: 1.04x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 2.11 sec: 1.02x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 1.03 sec: 1.01x faster                                                      |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 14.4 ms: 1.01x faster                                                       |
| meteor_contest           | 138 ms                                                       | 139 ms: 1.00x slower                                                        |
| json                     | 5.86 ms                                                      | 5.93 ms: 1.01x slower                                                       |
| regex_v8                 | 27.2 ms                                                      | 27.5 ms: 1.01x slower                                                       |
| xml_etree_parse          | 160 ms                                                       | 168 ms: 1.05x slower                                                        |
| async_generators         | 421 ms                                                       | 444 ms: 1.06x slower                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 117 ms: 1.06x slower                                                        |
| scimark_fft              | 361 ms                                                       | 383 ms: 1.06x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.36 ms: 1.09x slower                                                       |
| sqlite_synth             | 2.99 us                                                      | 3.40 us: 1.14x slower                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 107 ms: 1.15x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 5.47 us: 1.18x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 36.4 us: 1.23x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 6.46 ms: 1.27x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.40 ms: 1.28x slower                                                       |
| unpickle                 | 13.5 us                                                      | 17.6 us: 1.30x slower                                                       |
| telco                    | 7.23 ms                                                      | 9.64 ms: 1.33x slower                                                       |
| python_startup           | 11.5 ms                                                      | 16.4 ms: 1.43x slower                                                       |
| pickle_list              | 4.12 us                                                      | 5.92 us: 1.44x slower                                                       |
| pickle                   | 9.89 us                                                      | 14.7 us: 1.48x slower                                                       |
| coverage                 | 63.3 ms                                                      | 98.2 ms: 1.55x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 5.65 ms: 1.65x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.99 ms: 1.69x slower                                                       |
| logging_silent           | 167 ns                                                       | 676 ns: 4.04x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.00 sec: 156.93x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.09x faster                                                                |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.138x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.36x
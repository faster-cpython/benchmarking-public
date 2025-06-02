# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.218x faster
- HPT reliability: 98.22%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 286 ms: 1.16x slower                                                       |
| docutils       | 1.92 sec                                                    | 2.06 sec: 1.07x slower                                                     |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 536 ms: 2.07x faster                                                       |
| async_tree_none         | 435 ms                                                      | 230 ms: 1.89x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 282 ms: 1.87x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 426 ms: 1.50x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.82x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 55.8 ms: 1.28x faster                                                      |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| float          | 61.7 ms                                                     | 78.8 ms: 1.28x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| regex_compile  | 106 ms                                                      | 112 ms: 1.06x slower                                                       |
| regex_v8       | 15.4 ms                                                     | 16.4 ms: 1.06x slower                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.78 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 156 us: 1.18x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.55 sec: 1.08x faster                                                     |
| json_dumps           | 9.16 ms                                                     | 8.78 ms: 1.04x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 103 ms: 1.06x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 3.07 us: 1.13x slower                                                      |
| xml_etree_process    | 44.5 ms                                                     | 50.8 ms: 1.14x slower                                                      |
| pickle_pure_python   | 270 us                                                      | 319 us: 1.18x slower                                                       |
| unpickle             | 9.09 us                                                     | 11.2 us: 1.23x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 70.0 ms: 1.26x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 22.0 us: 1.28x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 85.0 ms: 1.31x slower                                                      |
| pickle               | 6.85 us                                                     | 9.47 us: 1.38x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.95 us: 1.44x slower                                                      |
| json_loads           | 14.0 us                                                     | 20.4 us: 1.46x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.17x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.2 ms: 1.30x slower                                                      |
| python_startup         | 20.6 ms                                                     | 27.2 ms: 1.32x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.09 ms: 1.27x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 49.3 ms: 1.20x slower                                                      |
| genshi_text     | 19.8 ms                                                     | 24.2 ms: 1.22x slower                                                      |
| django_template | 28.9 ms                                                     | 37.3 ms: 1.29x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pprint_pformat           | 1.22 sec                                                    | 1.56 us: 781045.40x faster                                                 |
| pprint_safe_repr         | 592 ms                                                      | 904 ns: 654943.37x faster                                                  |
| typing_runtime_protocols | 336 us                                                      | 144 us: 2.33x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 33.9 ms: 2.23x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 536 ms: 2.07x faster                                                       |
| async_tree_none          | 435 ms                                                      | 230 ms: 1.89x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 282 ms: 1.87x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 426 ms: 1.50x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.20 sec: 1.49x faster                                                     |
| pylint                   | 350 ms                                                      | 247 ms: 1.42x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.49 sec: 1.41x faster                                                     |
| asyncio_tcp              | 732 ms                                                      | 560 ms: 1.31x faster                                                       |
| nbody                    | 71.3 ms                                                     | 55.8 ms: 1.28x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.09 ms: 1.27x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 156 us: 1.18x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.72 us: 1.11x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.55 sec: 1.08x faster                                                     |
| pyflate                  | 409 ms                                                      | 383 ms: 1.07x faster                                                       |
| comprehensions           | 16.5 us                                                     | 15.5 us: 1.07x faster                                                      |
| go                       | 139 ms                                                      | 133 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.61 ms: 1.04x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 8.78 ms: 1.04x faster                                                      |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| scimark_fft              | 187 ms                                                      | 184 ms: 1.02x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 62.2 ms: 1.01x faster                                                      |
| deltablue                | 4.19 ms                                                     | 4.29 ms: 1.03x slower                                                      |
| dulwich_log              | 50.5 ms                                                     | 52.0 ms: 1.03x slower                                                      |
| chaos                    | 61.7 ms                                                     | 65.0 ms: 1.05x slower                                                      |
| sympy_sum                | 107 ms                                                      | 113 ms: 1.06x slower                                                       |
| regex_compile            | 106 ms                                                      | 112 ms: 1.06x slower                                                       |
| deepcopy                 | 255 us                                                      | 270 us: 1.06x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 16.4 ms: 1.06x slower                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 103 ms: 1.06x slower                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.78 ms: 1.07x slower                                                      |
| docutils                 | 1.92 sec                                                    | 2.06 sec: 1.07x slower                                                     |
| meteor_contest           | 75.9 ms                                                     | 82.1 ms: 1.08x slower                                                      |
| sympy_integrate          | 15.3 ms                                                     | 16.7 ms: 1.09x slower                                                      |
| raytrace                 | 273 ms                                                      | 299 ms: 1.09x slower                                                       |
| richards_super           | 52.2 ms                                                     | 58.1 ms: 1.11x slower                                                      |
| fannkuch                 | 256 ms                                                      | 286 ms: 1.12x slower                                                       |
| generators               | 32.4 ms                                                     | 36.5 ms: 1.13x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.07 us: 1.13x slower                                                      |
| xml_etree_process        | 44.5 ms                                                     | 50.8 ms: 1.14x slower                                                      |
| 2to3                     | 246 ms                                                      | 286 ms: 1.16x slower                                                       |
| pickle_pure_python       | 270 us                                                      | 319 us: 1.18x slower                                                       |
| deepcopy_memo            | 28.8 us                                                     | 34.2 us: 1.19x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 49.3 ms: 1.20x slower                                                      |
| richards                 | 42.4 ms                                                     | 51.2 ms: 1.21x slower                                                      |
| sympy_str                | 194 ms                                                      | 236 ms: 1.22x slower                                                       |
| genshi_text              | 19.8 ms                                                     | 24.2 ms: 1.22x slower                                                      |
| unpickle                 | 9.09 us                                                     | 11.2 us: 1.23x slower                                                      |
| scimark_sor              | 106 ms                                                      | 131 ms: 1.23x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 70.0 ms: 1.26x slower                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.80 us: 1.27x slower                                                      |
| float                    | 61.7 ms                                                     | 78.8 ms: 1.28x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 22.0 us: 1.28x slower                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 73.8 ms: 1.29x slower                                                      |
| django_template          | 28.9 ms                                                     | 37.3 ms: 1.29x slower                                                      |
| json                     | 3.14 ms                                                     | 4.06 ms: 1.29x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 20.2 ms: 1.30x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.14 ms: 1.30x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 85.0 ms: 1.31x slower                                                      |
| python_startup           | 20.6 ms                                                     | 27.2 ms: 1.32x slower                                                      |
| sympy_expand             | 314 ms                                                      | 416 ms: 1.32x slower                                                       |
| hexiom                   | 5.74 ms                                                     | 7.72 ms: 1.34x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 90.5 ms: 1.36x slower                                                      |
| pickle                   | 6.85 us                                                     | 9.47 us: 1.38x slower                                                      |
| scimark_lu               | 85.8 ms                                                     | 120 ms: 1.40x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.95 us: 1.44x slower                                                      |
| json_loads               | 14.0 us                                                     | 20.4 us: 1.46x slower                                                      |
| logging_format           | 6.76 us                                                     | 9.85 us: 1.46x slower                                                      |
| spectral_norm            | 77.3 ms                                                     | 116 ms: 1.50x slower                                                       |
| logging_simple           | 6.22 us                                                     | 9.39 us: 1.51x slower                                                      |
| coroutines               | 16.0 ms                                                     | 25.1 ms: 1.57x slower                                                      |
| async_generators         | 222 ms                                                      | 353 ms: 1.59x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 104 ms: 1.67x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.43 ms: 1.78x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 72.9 ns: 1.84x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.75 ms: 1.95x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 497 ns: 5.25x slower                                                       |
| coverage                 | 39.0 ms                                                     | 479 ms: 12.29x slower                                                      |
| thrift                   | 617 us                                                      | 98.9 ms: 160.26x slower                                                    |
| Geometric mean           | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (3): pycparser, html5lib, bench_thread_pool
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.218x faster

# HPT report

- Reliability score: 98.22% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
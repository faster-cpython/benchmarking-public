# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.314x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.41x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 338 ms: 1.37x slower                                                       |
| docutils       | 1.92 sec                                                    | 4.14 sec: 2.16x slower                                                     |
| html5lib       | 51.0 ms                                                     | 63.5 ms: 1.24x slower                                                      |
| Geometric mean | (ref)                                                       | 1.55x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 575 ms: 1.93x faster                                                       |
| async_tree_none         | 435 ms                                                      | 273 ms: 1.59x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 333 ms: 1.58x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 480 ms: 1.33x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.59x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 149 ms                                                      | 141 ms: 1.06x faster                                                       |
| float          | 61.7 ms                                                     | 97.2 ms: 1.58x slower                                                      |
| nbody          | 71.3 ms                                                     | 179 ms: 2.52x slower                                                       |
| Geometric mean | (ref)                                                       | 1.55x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 113 ms: 1.20x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 16.9 ms: 1.09x slower                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.82 ms: 1.10x slower                                                      |
| regex_compile  | 106 ms                                                      | 160 ms: 1.51x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 9.47 ms: 1.03x slower                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 111 ms: 1.14x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 21.3 us: 1.24x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.47 us: 1.28x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.73 us: 1.36x slower                                                      |
| pickle               | 6.85 us                                                     | 9.53 us: 1.39x slower                                                      |
| unpickle             | 9.09 us                                                     | 12.7 us: 1.40x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 93.9 ms: 1.45x slower                                                      |
| json_loads           | 14.0 us                                                     | 22.3 us: 1.59x slower                                                      |
| pickle_pure_python   | 270 us                                                      | 454 us: 1.68x slower                                                       |
| xml_etree_process    | 44.5 ms                                                     | 79.8 ms: 1.79x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 110 ms: 1.99x slower                                                       |
| unpickle_pure_python | 183 us                                                      | 364 us: 1.99x slower                                                       |
| tomli_loads          | 1.67 sec                                                    | 5.09 sec: 3.04x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.54x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.2 ms: 1.30x slower                                                      |
| python_startup         | 20.6 ms                                                     | 27.9 ms: 1.35x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.33x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 45.9 ms: 1.59x slower                                                      |
| genshi_xml      | 41.0 ms                                                     | 66.2 ms: 1.61x slower                                                      |
| genshi_text     | 19.8 ms                                                     | 33.4 ms: 1.69x slower                                                      |
| mako            | 9.03 ms                                                     | 16.9 ms: 1.87x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.69x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                  | 75.7 ms                                                     | 35.3 ms: 2.15x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 575 ms: 1.93x faster                                                       |
| typing_runtime_protocols | 336 us                                                      | 202 us: 1.67x faster                                                       |
| async_tree_none          | 435 ms                                                      | 273 ms: 1.59x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 333 ms: 1.58x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 539 ms: 1.36x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 480 ms: 1.33x faster                                                       |
| pylint                   | 350 ms                                                      | 282 ms: 1.24x faster                                                       |
| regex_dna                | 136 ms                                                      | 113 ms: 1.20x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.69 us: 1.13x faster                                                      |
| pidigits                 | 149 ms                                                      | 141 ms: 1.06x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 9.47 ms: 1.03x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 16.9 ms: 1.09x slower                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.82 ms: 1.10x slower                                                      |
| dulwich_log              | 50.5 ms                                                     | 56.8 ms: 1.13x slower                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 111 ms: 1.14x slower                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.56 sec: 1.21x slower                                                     |
| generators               | 32.4 ms                                                     | 39.3 ms: 1.21x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 21.3 us: 1.24x slower                                                      |
| html5lib                 | 51.0 ms                                                     | 63.5 ms: 1.24x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.47 us: 1.28x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.80 ms: 1.28x slower                                                      |
| mdp                      | 1.78 sec                                                    | 2.30 sec: 1.29x slower                                                     |
| bench_thread_pool        | 958 us                                                      | 1.24 ms: 1.30x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 20.2 ms: 1.30x slower                                                      |
| deepcopy                 | 255 us                                                      | 334 us: 1.31x slower                                                       |
| json                     | 3.14 ms                                                     | 4.14 ms: 1.32x slower                                                      |
| sympy_sum                | 107 ms                                                      | 145 ms: 1.35x slower                                                       |
| python_startup           | 20.6 ms                                                     | 27.9 ms: 1.35x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.73 us: 1.36x slower                                                      |
| go                       | 139 ms                                                      | 189 ms: 1.36x slower                                                       |
| sympy_integrate          | 15.3 ms                                                     | 20.9 ms: 1.37x slower                                                      |
| 2to3                     | 246 ms                                                      | 338 ms: 1.37x slower                                                       |
| thrift                   | 617 us                                                      | 849 us: 1.38x slower                                                       |
| pickle                   | 6.85 us                                                     | 9.53 us: 1.39x slower                                                      |
| unpickle                 | 9.09 us                                                     | 12.7 us: 1.40x slower                                                      |
| deltablue                | 4.19 ms                                                     | 5.88 ms: 1.40x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.13 ms: 1.41x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 88.6 ms: 1.43x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 93.9 ms: 1.45x slower                                                      |
| raytrace                 | 273 ms                                                      | 403 ms: 1.47x slower                                                       |
| sympy_str                | 194 ms                                                      | 292 ms: 1.50x slower                                                       |
| regex_compile            | 106 ms                                                      | 160 ms: 1.51x slower                                                       |
| richards_super           | 52.2 ms                                                     | 79.2 ms: 1.52x slower                                                      |
| deepcopy_memo            | 28.8 us                                                     | 43.7 us: 1.52x slower                                                      |
| pyflate                  | 409 ms                                                      | 626 ms: 1.53x slower                                                       |
| chaos                    | 61.7 ms                                                     | 95.4 ms: 1.55x slower                                                      |
| sympy_expand             | 314 ms                                                      | 491 ms: 1.56x slower                                                       |
| comprehensions           | 16.5 us                                                     | 25.9 us: 1.57x slower                                                      |
| float                    | 61.7 ms                                                     | 97.2 ms: 1.58x slower                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 3.48 us: 1.58x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 120 ms: 1.58x slower                                                       |
| django_template          | 28.9 ms                                                     | 45.9 ms: 1.59x slower                                                      |
| json_loads               | 14.0 us                                                     | 22.3 us: 1.59x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 66.2 ms: 1.61x slower                                                      |
| richards                 | 42.4 ms                                                     | 69.7 ms: 1.64x slower                                                      |
| pickle_pure_python       | 270 us                                                      | 454 us: 1.68x slower                                                       |
| genshi_text              | 19.8 ms                                                     | 33.4 ms: 1.69x slower                                                      |
| logging_format           | 6.76 us                                                     | 11.8 us: 1.74x slower                                                      |
| scimark_sor              | 106 ms                                                      | 190 ms: 1.79x slower                                                       |
| xml_etree_process        | 44.5 ms                                                     | 79.8 ms: 1.79x slower                                                      |
| logging_simple           | 6.22 us                                                     | 11.2 us: 1.80x slower                                                      |
| hexiom                   | 5.74 ms                                                     | 10.6 ms: 1.85x slower                                                      |
| async_generators         | 222 ms                                                      | 412 ms: 1.86x slower                                                       |
| pycparser                | 930 ms                                                      | 1.73 sec: 1.86x slower                                                     |
| scimark_monte_carlo      | 57.3 ms                                                     | 107 ms: 1.87x slower                                                       |
| mako                     | 9.03 ms                                                     | 16.9 ms: 1.87x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 127 ms: 1.91x slower                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 120 ms: 1.91x slower                                                       |
| scimark_lu               | 85.8 ms                                                     | 167 ms: 1.94x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 110 ms: 1.99x slower                                                       |
| unpickle_pure_python     | 183 us                                                      | 364 us: 1.99x slower                                                       |
| coroutines               | 16.0 ms                                                     | 32.4 ms: 2.03x slower                                                      |
| telco                    | 3.94 ms                                                     | 8.09 ms: 2.05x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 82.8 ns: 2.09x slower                                                      |
| docutils                 | 1.92 sec                                                    | 4.14 sec: 2.16x slower                                                     |
| coverage                 | 39.0 ms                                                     | 84.5 ms: 2.17x slower                                                      |
| spectral_norm            | 77.3 ms                                                     | 170 ms: 2.20x slower                                                       |
| scimark_fft              | 187 ms                                                      | 415 ms: 2.21x slower                                                       |
| fannkuch                 | 256 ms                                                      | 596 ms: 2.33x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 6.43 ms: 2.36x slower                                                      |
| nbody                    | 71.3 ms                                                     | 179 ms: 2.52x slower                                                       |
| pprint_safe_repr         | 592 ms                                                      | 1.50 sec: 2.53x slower                                                     |
| tomli_loads              | 1.67 sec                                                    | 5.09 sec: 3.04x slower                                                     |
| pprint_pformat           | 1.22 sec                                                    | 4.25 sec: 3.48x slower                                                     |
| logging_silent           | 94.6 ns                                                     | 577 ns: 6.09x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.47x slower                                                               |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.314x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.48x
- 95% likely to have a slowdown of 1.46x
- 99% likely to have a slowdown of 1.41x

# Memory
- memory change: unknown
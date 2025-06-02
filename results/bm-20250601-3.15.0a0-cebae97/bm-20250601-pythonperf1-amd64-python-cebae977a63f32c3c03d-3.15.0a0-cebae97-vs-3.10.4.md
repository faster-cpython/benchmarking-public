# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.212x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 292 ms: 1.19x slower                                                       |
| docutils       | 1.92 sec                                                    | 2.06 sec: 1.07x slower                                                     |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 548 ms: 2.02x faster                                                       |
| async_tree_none         | 435 ms                                                      | 242 ms: 1.80x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 296 ms: 1.78x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 443 ms: 1.44x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.75x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                       |
| float          | 61.7 ms                                                     | 77.0 ms: 1.25x slower                                                      |
| nbody          | 71.3 ms                                                     | 105 ms: 1.47x slower                                                       |
| Geometric mean | (ref)                                                       | 1.21x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 16.6 ms: 1.08x slower                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.80 ms: 1.09x slower                                                      |
| regex_compile  | 106 ms                                                      | 124 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 8.73 ms: 1.05x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 108 ms: 1.11x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 3.14 us: 1.16x slower                                                      |
| unpickle             | 9.09 us                                                     | 11.4 us: 1.26x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.10 sec: 1.26x slower                                                     |
| pickle_dict          | 17.2 us                                                     | 22.5 us: 1.31x slower                                                      |
| pickle_pure_python   | 270 us                                                      | 359 us: 1.33x slower                                                       |
| pickle               | 6.85 us                                                     | 9.46 us: 1.38x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 90.2 ms: 1.39x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.96 us: 1.44x slower                                                      |
| xml_etree_process    | 44.5 ms                                                     | 64.8 ms: 1.46x slower                                                      |
| json_loads           | 14.0 us                                                     | 20.5 us: 1.46x slower                                                      |
| unpickle_pure_python | 183 us                                                      | 275 us: 1.50x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 89.7 ms: 1.62x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.32x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.2 ms: 1.30x slower                                                      |
| python_startup         | 20.6 ms                                                     | 27.4 ms: 1.33x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 41.0 ms                                                     | 49.1 ms: 1.20x slower                                                      |
| genshi_text     | 19.8 ms                                                     | 23.8 ms: 1.20x slower                                                      |
| django_template | 28.9 ms                                                     | 37.2 ms: 1.29x slower                                                      |
| mako            | 9.03 ms                                                     | 12.5 ms: 1.39x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.27x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                  | 75.7 ms                                                     | 34.2 ms: 2.21x faster                                                      |
| typing_runtime_protocols | 336 us                                                      | 155 us: 2.17x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 548 ms: 2.02x faster                                                       |
| async_tree_none          | 435 ms                                                      | 242 ms: 1.80x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 296 ms: 1.78x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 422 ms: 1.73x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.36 sec: 1.55x faster                                                     |
| mdp                      | 1.78 sec                                                    | 1.18 sec: 1.51x faster                                                     |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 443 ms: 1.44x faster                                                       |
| pylint                   | 350 ms                                                      | 245 ms: 1.43x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 8.73 ms: 1.05x faster                                                      |
| go                       | 139 ms                                                      | 133 ms: 1.04x faster                                                       |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.87 us: 1.02x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 51.1 ms: 1.01x slower                                                      |
| deltablue                | 4.19 ms                                                     | 4.31 ms: 1.03x slower                                                      |
| deepcopy                 | 255 us                                                      | 265 us: 1.04x slower                                                       |
| bench_thread_pool        | 958 us                                                      | 1.00 ms: 1.05x slower                                                      |
| pycparser                | 930 ms                                                      | 985 ms: 1.06x slower                                                       |
| generators               | 32.4 ms                                                     | 34.3 ms: 1.06x slower                                                      |
| chaos                    | 61.7 ms                                                     | 65.8 ms: 1.07x slower                                                      |
| docutils                 | 1.92 sec                                                    | 2.06 sec: 1.07x slower                                                     |
| sympy_sum                | 107 ms                                                      | 115 ms: 1.08x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 16.6 ms: 1.08x slower                                                      |
| sympy_integrate          | 15.3 ms                                                     | 16.6 ms: 1.08x slower                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.80 ms: 1.09x slower                                                      |
| richards_super           | 52.2 ms                                                     | 57.4 ms: 1.10x slower                                                      |
| raytrace                 | 273 ms                                                      | 302 ms: 1.10x slower                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 108 ms: 1.11x slower                                                       |
| pyflate                  | 409 ms                                                      | 455 ms: 1.11x slower                                                       |
| deepcopy_memo            | 28.8 us                                                     | 33.3 us: 1.16x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.14 us: 1.16x slower                                                      |
| regex_compile            | 106 ms                                                      | 124 ms: 1.17x slower                                                       |
| comprehensions           | 16.5 us                                                     | 19.6 us: 1.19x slower                                                      |
| 2to3                     | 246 ms                                                      | 292 ms: 1.19x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 49.1 ms: 1.20x slower                                                      |
| richards                 | 42.4 ms                                                     | 50.8 ms: 1.20x slower                                                      |
| sympy_str                | 194 ms                                                      | 234 ms: 1.20x slower                                                       |
| genshi_text              | 19.8 ms                                                     | 23.8 ms: 1.20x slower                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.74 us: 1.24x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 94.4 ms: 1.24x slower                                                      |
| float                    | 61.7 ms                                                     | 77.0 ms: 1.25x slower                                                      |
| scimark_sor              | 106 ms                                                      | 133 ms: 1.25x slower                                                       |
| unpickle                 | 9.09 us                                                     | 11.4 us: 1.26x slower                                                      |
| tomli_loads              | 1.67 sec                                                    | 2.10 sec: 1.26x slower                                                     |
| json                     | 3.14 ms                                                     | 3.94 ms: 1.26x slower                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 72.5 ms: 1.27x slower                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 79.3 ms: 1.27x slower                                                      |
| sympy_expand             | 314 ms                                                      | 400 ms: 1.27x slower                                                       |
| django_template          | 28.9 ms                                                     | 37.2 ms: 1.29x slower                                                      |
| hexiom                   | 5.74 ms                                                     | 7.39 ms: 1.29x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 20.2 ms: 1.30x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 22.5 us: 1.31x slower                                                      |
| python_startup           | 20.6 ms                                                     | 27.4 ms: 1.33x slower                                                      |
| pickle_pure_python       | 270 us                                                      | 359 us: 1.33x slower                                                       |
| scimark_lu               | 85.8 ms                                                     | 117 ms: 1.37x slower                                                       |
| pickle                   | 6.85 us                                                     | 9.46 us: 1.38x slower                                                      |
| mako                     | 9.03 ms                                                     | 12.5 ms: 1.39x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 90.2 ms: 1.39x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 94.2 ms: 1.41x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.74 sec: 1.43x slower                                                     |
| pprint_safe_repr         | 592 ms                                                      | 848 ms: 1.43x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.96 us: 1.44x slower                                                      |
| xml_etree_process        | 44.5 ms                                                     | 64.8 ms: 1.46x slower                                                      |
| json_loads               | 14.0 us                                                     | 20.5 us: 1.46x slower                                                      |
| logging_format           | 6.76 us                                                     | 9.89 us: 1.46x slower                                                      |
| scimark_fft              | 187 ms                                                      | 274 ms: 1.46x slower                                                       |
| nbody                    | 71.3 ms                                                     | 105 ms: 1.47x slower                                                       |
| unpickle_pure_python     | 183 us                                                      | 275 us: 1.50x slower                                                       |
| logging_simple           | 6.22 us                                                     | 9.36 us: 1.51x slower                                                      |
| spectral_norm            | 77.3 ms                                                     | 117 ms: 1.51x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 4.14 ms: 1.52x slower                                                      |
| async_generators         | 222 ms                                                      | 343 ms: 1.55x slower                                                       |
| telco                    | 3.94 ms                                                     | 6.25 ms: 1.59x slower                                                      |
| coroutines               | 16.0 ms                                                     | 25.6 ms: 1.60x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 89.7 ms: 1.62x slower                                                      |
| fannkuch                 | 256 ms                                                      | 420 ms: 1.64x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 103 ms: 1.67x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.45 ms: 1.81x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.82 ms: 2.00x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 81.9 ns: 2.07x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 494 ns: 5.22x slower                                                       |
| coverage                 | 39.0 ms                                                     | 475 ms: 12.18x slower                                                      |
| thrift                   | 617 us                                                      | 98.8 ms: 160.02x slower                                                    |
| Geometric mean           | (ref)                                                       | 1.28x slower                                                               |

Benchmark hidden because not significant (1): html5lib
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.212x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: unknown
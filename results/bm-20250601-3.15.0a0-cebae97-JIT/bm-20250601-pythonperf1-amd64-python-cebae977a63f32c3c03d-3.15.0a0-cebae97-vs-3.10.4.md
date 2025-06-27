# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.895x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 216 ms: 1.14x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 393 ms: 2.82x faster                                                       |
| async_tree_none         | 435 ms                                                      | 170 ms: 2.56x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 206 ms: 2.56x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 332 ms: 1.92x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.44x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                                      |
| nbody          | 71.3 ms                                                     | 59.7 ms: 1.20x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 70.6 ms: 1.50x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 110 us: 1.67x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 6.21 ms: 1.47x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.15 sec: 1.46x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 207 us: 1.31x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.0 ms: 1.10x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 52.0 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.7 ms: 1.02x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.6 ms: 1.27x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.43 ms: 1.66x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                      |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.32x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pprint_pformat           | 1.22 sec                                                    | 995 ns: 1225778.83x faster                                                 |
| pprint_safe_repr         | 592 ms                                                      | 579 ns: 1021360.76x faster                                                 |
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.21x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 393 ms: 2.82x faster                                                       |
| async_tree_none          | 435 ms                                                      | 170 ms: 2.56x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 206 ms: 2.56x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 31.8 ms: 2.38x faster                                                      |
| mdp                      | 1.78 sec                                                    | 802 ms: 2.22x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 332 ms: 1.92x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.19 ms: 1.91x faster                                                      |
| go                       | 139 ms                                                      | 76.4 ms: 1.82x faster                                                      |
| pylint                   | 350 ms                                                      | 201 ms: 1.75x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.5 ms: 1.71x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 110 us: 1.67x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.43 ms: 1.66x faster                                                      |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 17.7 us: 1.63x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.0 ms: 1.57x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.6 ms: 1.56x faster                                                      |
| pyflate                  | 409 ms                                                      | 263 ms: 1.55x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.8 us: 1.53x faster                                                      |
| deepcopy                 | 255 us                                                      | 168 us: 1.52x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 56.8 ms: 1.51x faster                                                      |
| regex_compile            | 106 ms                                                      | 70.6 ms: 1.50x faster                                                      |
| raytrace                 | 273 ms                                                      | 183 ms: 1.49x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.21 ms: 1.47x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.15 sec: 1.46x faster                                                     |
| float                    | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.06 ms: 1.42x faster                                                      |
| scimark_sor              | 106 ms                                                      | 75.0 ms: 1.41x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.7 ms: 1.41x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.6 ms: 1.34x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 207 us: 1.31x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                      |
| pycparser                | 930 ms                                                      | 722 ms: 1.29x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 60.8 ms: 1.27x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 40.4 ms: 1.25x faster                                                      |
| thrift                   | 617 us                                                      | 499 us: 1.24x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.23x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.23x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.5 ms: 1.22x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                      |
| nbody                    | 71.3 ms                                                     | 59.7 ms: 1.20x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                      |
| scimark_fft              | 187 ms                                                      | 161 ms: 1.16x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.37 ms: 1.15x faster                                                      |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                     |
| sympy_str                | 194 ms                                                      | 170 ms: 1.14x faster                                                       |
| 2to3                     | 246 ms                                                      | 216 ms: 1.14x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 58.9 ms: 1.13x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 88.0 ms: 1.10x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 52.0 ms: 1.07x faster                                                      |
| sympy_expand             | 314 ms                                                      | 296 ms: 1.06x faster                                                       |
| json                     | 3.14 ms                                                     | 2.97 ms: 1.06x faster                                                      |
| fannkuch                 | 256 ms                                                      | 250 ms: 1.02x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 74.3 ms: 1.02x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.7 ms: 1.02x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.66 us: 1.02x faster                                                      |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.35 ms: 1.10x slower                                                      |
| async_generators         | 222 ms                                                      | 246 ms: 1.11x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.4 ms: 1.24x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.6 ms: 1.27x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.17 ms: 1.54x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.34 ms: 1.67x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 316 ns: 3.34x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.84x faster                                                               |

Benchmark hidden because not significant (3): logging_simple, pidigits, regex_effbot
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.895x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown
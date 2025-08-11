# Results vs. 3.10.4

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: windows-amd64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.315x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.15x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 391 ms: 2.84x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 206 ms: 2.56x faster                                                       |
| async_tree_none         | 435 ms                                                      | 175 ms: 2.49x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 334 ms: 1.91x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.42x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.9 ms: 1.37x faster                                                      |
| nbody          | 71.3 ms                                                     | 57.5 ms: 1.24x faster                                                      |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.1 ms: 1.36x faster                                                      |
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.1 ms: 1.10x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 106 us: 1.73x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 5.44 ms: 1.69x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.11 sec: 1.51x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 205 us: 1.31x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 35.6 ms: 1.25x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 50.1 ms: 1.11x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.6 ms: 1.11x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.48 us: 1.07x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.6 ms: 1.04x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| pickle               | 6.85 us                                                     | 7.64 us: 1.12x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.5 us: 1.14x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.31 us: 1.20x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.8 ms: 1.28x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.6 ms: 1.29x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.26 ms: 1.72x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.4 ms: 1.28x faster                                                      |
| django_template | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.9 ms: 1.18x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.32x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.26x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 391 ms: 2.84x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 206 ms: 2.56x faster                                                       |
| async_tree_none          | 435 ms                                                      | 175 ms: 2.49x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.0 ms: 2.36x faster                                                      |
| mdp                      | 1.78 sec                                                    | 804 ms: 2.21x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 334 ms: 1.91x faster                                                       |
| go                       | 139 ms                                                      | 75.5 ms: 1.84x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.28 ms: 1.84x faster                                                      |
| pylint                   | 350 ms                                                      | 200 ms: 1.75x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 54.2 ns: 1.74x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 106 us: 1.73x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.26 ms: 1.72x faster                                                      |
| richards_super           | 52.2 ms                                                     | 31.0 ms: 1.69x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.44 ms: 1.69x faster                                                      |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.3 us: 1.57x faster                                                      |
| pyflate                  | 409 ms                                                      | 261 ms: 1.57x faster                                                       |
| richards                 | 42.4 ms                                                     | 27.1 ms: 1.56x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                      |
| raytrace                 | 273 ms                                                      | 179 ms: 1.53x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.11 sec: 1.51x faster                                                     |
| chaos                    | 61.7 ms                                                     | 41.1 ms: 1.50x faster                                                      |
| deepcopy                 | 255 us                                                      | 171 us: 1.50x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.44 sec: 1.46x faster                                                     |
| scimark_lu               | 85.8 ms                                                     | 59.3 ms: 1.45x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.2 ms: 1.42x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 522 ms: 1.40x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.13 ms: 1.39x faster                                                      |
| scimark_sor              | 106 ms                                                      | 76.8 ms: 1.38x faster                                                      |
| float                    | 61.7 ms                                                     | 44.9 ms: 1.37x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 889 ms: 1.37x faster                                                       |
| regex_compile            | 106 ms                                                      | 78.1 ms: 1.36x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.0 ms: 1.36x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 436 ms: 1.36x faster                                                       |
| pycparser                | 930 ms                                                      | 696 ms: 1.34x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 205 us: 1.31x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.4 ms: 1.28x faster                                                      |
| thrift                   | 617 us                                                      | 488 us: 1.27x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.3 ms: 1.25x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 35.6 ms: 1.25x faster                                                      |
| nbody                    | 71.3 ms                                                     | 57.5 ms: 1.24x faster                                                      |
| sympy_sum                | 107 ms                                                      | 86.7 ms: 1.23x faster                                                      |
| scimark_fft              | 187 ms                                                      | 153 ms: 1.23x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.22x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.82 us: 1.21x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 64.1 ms: 1.21x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.8 ms: 1.20x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.28 ms: 1.19x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                                      |
| fannkuch                 | 256 ms                                                      | 217 ms: 1.18x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 34.9 ms: 1.18x faster                                                      |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.15x faster                                                     |
| unpack_sequence          | 39.6 ns                                                     | 34.4 ns: 1.15x faster                                                      |
| sympy_str                | 194 ms                                                      | 170 ms: 1.15x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 862 us: 1.11x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 50.1 ms: 1.11x faster                                                      |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 60.2 ms: 1.11x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 87.6 ms: 1.11x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.1 ms: 1.10x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.7 ms: 1.09x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.48 us: 1.07x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 70.9 ms: 1.07x faster                                                      |
| sympy_expand             | 314 ms                                                      | 296 ms: 1.06x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.41 us: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.6 ms: 1.04x faster                                                      |
| json                     | 3.14 ms                                                     | 3.04 ms: 1.03x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.05 us: 1.03x faster                                                      |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.29 ms: 1.09x slower                                                      |
| async_generators         | 222 ms                                                      | 245 ms: 1.11x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.64 us: 1.12x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.5 us: 1.14x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.31 us: 1.20x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.5 ms: 1.27x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.8 ms: 1.28x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.6 ms: 1.29x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.18 ms: 1.55x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 96.3 ms: 1.55x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.65x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.28x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.315x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown
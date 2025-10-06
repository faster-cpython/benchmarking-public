# Results vs. 3.10.4

- fork: python
- ref: 880c9526f91960b9cba5
- machine: windows-amd64
- commit hash: 880c952
- commit date: 2025-10-04
- overall geometric mean: 1.330x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 215 ms: 1.15x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 379 ms: 2.93x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 203 ms: 2.59x faster                                                       |
| async_tree_none         | 435 ms                                                      | 174 ms: 2.50x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 336 ms: 1.90x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.45x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                      |
| nbody          | 71.3 ms                                                     | 54.9 ms: 1.30x faster                                                      |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.0 ms: 1.36x faster                                                      |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 107 us: 1.72x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 5.47 ms: 1.68x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.11 sec: 1.51x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 200 us: 1.35x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 35.6 ms: 1.25x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 49.9 ms: 1.11x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 90.5 ms: 1.07x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.89 us: 1.02x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.9 ms: 1.02x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.86 us: 1.05x slower                                                      |
| pickle               | 6.85 us                                                     | 7.85 us: 1.15x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.27 us: 1.19x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.5 us: 1.19x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.43 ms: 1.66x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                      |
| django_template | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 35.2 ms: 1.17x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.26x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 379 ms: 2.93x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 203 ms: 2.59x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 29.6 ms: 2.56x faster                                                      |
| async_tree_none          | 435 ms                                                      | 174 ms: 2.50x faster                                                       |
| mdp                      | 1.78 sec                                                    | 811 ms: 2.20x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 336 ms: 1.90x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.85x faster                                                      |
| go                       | 139 ms                                                      | 75.8 ms: 1.83x faster                                                      |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.7 us: 1.72x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 107 us: 1.72x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.5 ms: 1.71x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 55.5 ns: 1.71x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.47 ms: 1.68x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.43 ms: 1.66x faster                                                      |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                      |
| pyflate                  | 409 ms                                                      | 250 ms: 1.64x faster                                                       |
| richards                 | 42.4 ms                                                     | 27.1 ms: 1.57x faster                                                      |
| raytrace                 | 273 ms                                                      | 176 ms: 1.56x faster                                                       |
| chaos                    | 61.7 ms                                                     | 39.7 ms: 1.56x faster                                                      |
| deepcopy                 | 255 us                                                      | 165 us: 1.55x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.8 us: 1.53x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.11 sec: 1.51x faster                                                     |
| asyncio_tcp              | 732 ms                                                      | 492 ms: 1.49x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 58.3 ms: 1.47x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.44 sec: 1.47x faster                                                     |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.4 ms: 1.46x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 839 ms: 1.45x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 412 ms: 1.44x faster                                                       |
| float                    | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                      |
| scimark_sor              | 106 ms                                                      | 76.1 ms: 1.40x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 45.0 ms: 1.39x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.14 ms: 1.39x faster                                                      |
| scimark_fft              | 187 ms                                                      | 137 ms: 1.37x faster                                                       |
| regex_compile            | 106 ms                                                      | 78.0 ms: 1.36x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 200 us: 1.35x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                      |
| nbody                    | 71.3 ms                                                     | 54.9 ms: 1.30x faster                                                      |
| pycparser                | 930 ms                                                      | 716 ms: 1.30x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 40.1 ms: 1.26x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.76 us: 1.25x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 35.6 ms: 1.25x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.54 us: 1.24x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.0 ms: 1.23x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.24 ms: 1.22x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.6 ms: 1.21x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 64.0 ms: 1.21x faster                                                      |
| thrift                   | 617 us                                                      | 514 us: 1.20x faster                                                       |
| fannkuch                 | 256 ms                                                      | 213 ms: 1.20x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 35.2 ms: 1.17x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                     |
| sympy_str                | 194 ms                                                      | 169 ms: 1.15x faster                                                       |
| 2to3                     | 246 ms                                                      | 215 ms: 1.15x faster                                                       |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 850 us: 1.13x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 35.4 ns: 1.12x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 49.9 ms: 1.11x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 60.0 ms: 1.11x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.6 ms: 1.09x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                      |
| sympy_expand             | 314 ms                                                      | 291 ms: 1.08x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 90.5 ms: 1.07x faster                                                      |
| json                     | 3.14 ms                                                     | 2.93 ms: 1.07x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.85 us: 1.06x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.37 us: 1.06x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 71.9 ms: 1.06x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.89 us: 1.02x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.9 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                       |
| telco                    | 3.94 ms                                                     | 4.04 ms: 1.03x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.86 us: 1.05x slower                                                      |
| async_generators         | 222 ms                                                      | 246 ms: 1.11x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.85 us: 1.15x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.27 us: 1.19x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 20.5 us: 1.19x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                      |
| coverage                 | 39.0 ms                                                     | 51.2 ms: 1.31x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 90.1 ms: 1.45x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.12 ms: 1.50x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.29 ms: 1.61x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.29x faster                                                               |

Benchmark hidden because not significant (1): json_loads
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.330x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown
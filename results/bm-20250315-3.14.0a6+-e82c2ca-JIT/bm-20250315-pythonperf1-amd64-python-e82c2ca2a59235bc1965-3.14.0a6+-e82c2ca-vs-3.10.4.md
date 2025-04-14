# Results vs. 3.10.4

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: windows-amd64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.232x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 228 ms: 1.08x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.75 sec: 1.09x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.4 ms: 1.26x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 425 ms: 2.61x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 227 ms: 2.32x faster                                                        |
| async_tree_none         | 435 ms                                                      | 189 ms: 2.30x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 348 ms: 1.84x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.25x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.9 ms: 1.32x faster                                                       |
| nbody          | 71.3 ms                                                     | 63.4 ms: 1.12x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 86.2 ms: 1.23x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.41 ms: 1.18x faster                                                       |
| regex_dna      | 136 ms                                                      | 116 ms: 1.18x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 13.5 ms: 1.14x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 125 us: 1.47x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.24 sec: 1.35x faster                                                      |
| json_dumps           | 9.16 ms                                                     | 7.13 ms: 1.28x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 217 us: 1.24x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 38.3 ms: 1.16x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 88.6 ms: 1.09x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.55 us: 1.06x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 52.6 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.0 ms: 1.03x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.91 us: 1.07x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.3 us: 1.09x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 19.8 us: 1.15x slower                                                       |
| pickle               | 6.85 us                                                     | 8.31 us: 1.21x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.37 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.6 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.76 ms: 1.57x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.3 ms: 1.14x faster                                                       |
| django_template | 28.9 ms                                                     | 26.7 ms: 1.08x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 40.1 ms: 1.02x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 115 us: 2.93x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 425 ms: 2.61x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 227 ms: 2.32x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.7 ms: 2.31x faster                                                       |
| async_tree_none          | 435 ms                                                      | 189 ms: 2.30x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 348 ms: 1.84x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.38 ms: 1.76x faster                                                       |
| pylint                   | 350 ms                                                      | 207 ms: 1.70x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 59.6 ns: 1.59x faster                                                       |
| generators               | 32.4 ms                                                     | 20.5 ms: 1.58x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.2 ms: 1.57x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.76 ms: 1.57x faster                                                       |
| go                       | 139 ms                                                      | 90.6 ms: 1.53x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 125 us: 1.47x faster                                                        |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.45 sec: 1.46x faster                                                      |
| pyflate                  | 409 ms                                                      | 281 ms: 1.45x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 19.8 us: 1.45x faster                                                       |
| richards                 | 42.4 ms                                                     | 29.4 ms: 1.45x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 59.9 ms: 1.43x faster                                                       |
| chaos                    | 61.7 ms                                                     | 43.2 ms: 1.43x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 516 ms: 1.42x faster                                                        |
| raytrace                 | 273 ms                                                      | 194 ms: 1.41x faster                                                        |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.39x faster                                                       |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.24 sec: 1.35x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 58.3 ms: 1.33x faster                                                       |
| scimark_sor              | 106 ms                                                      | 80.6 ms: 1.32x faster                                                       |
| float                    | 61.7 ms                                                     | 46.9 ms: 1.32x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.42 ms: 1.30x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 7.13 ms: 1.28x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.6 ms: 1.28x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 49.4 ms: 1.27x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.4 ms: 1.26x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.53 us: 1.25x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 217 us: 1.24x faster                                                        |
| regex_compile            | 106 ms                                                      | 86.2 ms: 1.23x faster                                                       |
| pycparser                | 930 ms                                                      | 759 ms: 1.23x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.28 ms: 1.19x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.18x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.41 ms: 1.18x faster                                                       |
| regex_dna                | 136 ms                                                      | 116 ms: 1.18x faster                                                        |
| scimark_fft              | 187 ms                                                      | 159 ms: 1.18x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 43.0 ms: 1.17x faster                                                       |
| sympy_sum                | 107 ms                                                      | 91.5 ms: 1.17x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.05 sec: 1.16x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 38.3 ms: 1.16x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.5 ms: 1.14x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.3 ms: 1.14x faster                                                       |
| thrift                   | 617 us                                                      | 541 us: 1.14x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 523 ms: 1.13x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.6 ms: 1.13x faster                                                       |
| nbody                    | 71.3 ms                                                     | 63.4 ms: 1.12x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 862 us: 1.11x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.75 sec: 1.09x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 88.6 ms: 1.09x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.64 sec: 1.08x faster                                                      |
| django_template          | 28.9 ms                                                     | 26.7 ms: 1.08x faster                                                       |
| 2to3                     | 246 ms                                                      | 228 ms: 1.08x faster                                                        |
| sympy_str                | 194 ms                                                      | 182 ms: 1.07x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 2.07 us: 1.07x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.55 us: 1.06x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 52.6 ms: 1.06x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 64.0 ms: 1.04x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.0 ms: 1.03x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 38.7 ns: 1.02x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 40.1 ms: 1.02x faster                                                       |
| fannkuch                 | 256 ms                                                      | 252 ms: 1.01x faster                                                        |
| json                     | 3.14 ms                                                     | 3.10 ms: 1.01x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 75.1 ms: 1.01x faster                                                       |
| sympy_expand             | 314 ms                                                      | 319 ms: 1.01x slower                                                        |
| logging_format           | 6.76 us                                                     | 7.06 us: 1.04x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.55 us: 1.05x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.91 us: 1.07x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.3 us: 1.09x slower                                                       |
| async_generators         | 222 ms                                                      | 250 ms: 1.13x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.45 ms: 1.13x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 19.8 us: 1.15x slower                                                       |
| pickle                   | 6.85 us                                                     | 8.31 us: 1.21x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.37 us: 1.23x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                       |
| coverage                 | 39.0 ms                                                     | 49.4 ms: 1.27x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.6 ms: 1.33x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.7 ms: 1.43x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.05 ms: 1.45x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.24 ms: 1.55x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.232x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown
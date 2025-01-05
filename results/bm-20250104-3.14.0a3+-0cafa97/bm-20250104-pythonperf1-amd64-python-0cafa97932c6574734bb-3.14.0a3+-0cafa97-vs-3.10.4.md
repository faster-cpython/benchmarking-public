# Results vs. 3.10.4

- fork: python
- ref: 0cafa97932c6574734bb
- machine: windows-amd64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.205x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.4 ms: 1.30x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 397 ms: 2.79x faster                                                        |
| async_tree_none         | 435 ms                                                      | 179 ms: 2.42x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 222 ms: 2.37x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 345 ms: 1.85x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 52.1 ms: 1.19x faster                                                       |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| nbody          | 71.3 ms                                                     | 75.3 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 86.5 ms: 1.23x faster                                                       |
| regex_dna      | 136 ms                                                      | 116 ms: 1.17x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.46 ms: 1.14x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 21.8 ms: 1.41x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.57 ms: 1.39x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 145 us: 1.27x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 220 us: 1.23x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 39.6 ms: 1.12x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 88.8 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.5 ms: 1.04x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 56.4 ms: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.3 ms: 1.12x slower                                                       |
| python_startup         | 20.6 ms                                                     | 23.6 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.69 ms: 1.35x faster                                                       |
| django_template | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.5 ms: 1.13x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 36.2 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.97x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 397 ms: 2.79x faster                                                        |
| async_tree_none          | 435 ms                                                      | 179 ms: 2.42x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 222 ms: 2.37x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.25 ms: 1.86x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 345 ms: 1.85x faster                                                        |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                        |
| go                       | 139 ms                                                      | 87.1 ms: 1.60x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 61.6 ns: 1.54x faster                                                       |
| generators               | 32.4 ms                                                     | 21.2 ms: 1.53x faster                                                       |
| richards_super           | 52.2 ms                                                     | 34.5 ms: 1.51x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 19.8 us: 1.45x faster                                                       |
| raytrace                 | 273 ms                                                      | 190 ms: 1.44x faster                                                        |
| chaos                    | 61.7 ms                                                     | 43.0 ms: 1.44x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 60.5 ms: 1.42x faster                                                       |
| richards                 | 42.4 ms                                                     | 30.4 ms: 1.40x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.40x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.57 ms: 1.39x faster                                                       |
| deepcopy                 | 255 us                                                      | 185 us: 1.38x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 895 us: 1.36x faster                                                        |
| mako                     | 9.03 ms                                                     | 6.69 ms: 1.35x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.11 ms: 1.33x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.34 ms: 1.32x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 48.1 ms: 1.30x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.4 ms: 1.30x faster                                                       |
| pycparser                | 930 ms                                                      | 727 ms: 1.28x faster                                                        |
| pyflate                  | 409 ms                                                      | 321 ms: 1.28x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 145 us: 1.27x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 45.8 ms: 1.25x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 62.2 ms: 1.24x faster                                                       |
| scimark_sor              | 106 ms                                                      | 86.1 ms: 1.23x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 220 us: 1.23x faster                                                        |
| regex_compile            | 106 ms                                                      | 86.5 ms: 1.23x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.46 sec: 1.22x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 42.1 ms: 1.20x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.4 ms: 1.19x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.9 ms: 1.19x faster                                                       |
| float                    | 61.7 ms                                                     | 52.1 ms: 1.19x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.88 us: 1.18x faster                                                       |
| regex_dna                | 136 ms                                                      | 116 ms: 1.17x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                      |
| thrift                   | 617 us                                                      | 533 us: 1.16x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 836 us: 1.15x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.07 sec: 1.14x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.46 ms: 1.14x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.5 ms: 1.13x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.2 ms: 1.13x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.6 ms: 1.12x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 531 ms: 1.12x faster                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 35.9 ms: 1.11x faster                                                       |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| sympy_str                | 194 ms                                                      | 178 ms: 1.10x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 88.8 ms: 1.09x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 195 ms: 1.05x faster                                                        |
| json                     | 3.14 ms                                                     | 2.98 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.59 ms: 1.05x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 63.7 ms: 1.05x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.5 ms: 1.04x faster                                                       |
| sympy_expand             | 314 ms                                                      | 306 ms: 1.03x faster                                                        |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 76.9 ms: 1.01x slower                                                       |
| logging_format           | 6.76 us                                                     | 6.86 us: 1.02x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 56.4 ms: 1.02x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.36 us: 1.02x slower                                                       |
| scimark_fft              | 187 ms                                                      | 193 ms: 1.03x slower                                                        |
| fannkuch                 | 256 ms                                                      | 270 ms: 1.05x slower                                                        |
| nbody                    | 71.3 ms                                                     | 75.3 ms: 1.06x slower                                                       |
| async_generators         | 222 ms                                                      | 237 ms: 1.07x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 17.3 ms: 1.12x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.6 ms: 1.14x slower                                                       |
| mypy2                    | 555 ms                                                      | 637 ms: 1.15x slower                                                        |
| coverage                 | 39.0 ms                                                     | 45.8 ms: 1.17x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.76 ms: 1.21x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 82.3 ms: 1.33x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.98 ms: 1.40x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 21.8 ms: 1.41x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.20 ms: 1.50x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (2): pathlib, json_loads
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.205x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown
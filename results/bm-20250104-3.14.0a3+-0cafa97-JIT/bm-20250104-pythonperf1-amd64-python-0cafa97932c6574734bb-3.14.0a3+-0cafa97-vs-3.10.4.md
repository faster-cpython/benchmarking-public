# Results vs. 3.10.4

- fork: python
- ref: 0cafa97932c6574734bb
- machine: windows-amd64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.253x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                      |
| html5lib       | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 392 ms: 2.82x faster                                                        |
| async_tree_none         | 435 ms                                                      | 176 ms: 2.47x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 217 ms: 2.43x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 346 ms: 1.84x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 40.3 ms: 1.53x faster                                                       |
| nbody          | 71.3 ms                                                     | 52.4 ms: 1.36x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.28x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.7 ms: 1.33x faster                                                       |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.53 ms: 1.09x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 22.0 ms: 1.42x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 108 us: 1.69x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 6.23 ms: 1.47x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.18 sec: 1.42x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 205 us: 1.31x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 35.7 ms: 1.25x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 86.1 ms: 1.13x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 49.6 ms: 1.12x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.3 ms: 1.10x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.9 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.25x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.6 ms: 1.13x slower                                                       |
| python_startup         | 20.6 ms                                                     | 23.5 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.06 ms: 1.79x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 18.7 ms: 1.06x faster                                                       |
| django_template | 28.9 ms                                                     | 27.5 ms: 1.05x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 48.0 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.00x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 392 ms: 2.82x faster                                                        |
| async_tree_none          | 435 ms                                                      | 176 ms: 2.47x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 217 ms: 2.43x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 346 ms: 1.84x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.27 ms: 1.84x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.06 ms: 1.79x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.2 us: 1.77x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 108 us: 1.69x faster                                                        |
| scimark_sor              | 106 ms                                                      | 62.8 ms: 1.69x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 56.5 ns: 1.68x faster                                                       |
| pylint                   | 350 ms                                                      | 210 ms: 1.67x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 53.5 ms: 1.60x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 36.7 ms: 1.56x faster                                                       |
| go                       | 139 ms                                                      | 89.9 ms: 1.55x faster                                                       |
| float                    | 61.7 ms                                                     | 40.3 ms: 1.53x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 50.6 ms: 1.53x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 41.3 ms: 1.52x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.1 ms: 1.50x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.23 ms: 1.47x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 838 us: 1.45x faster                                                        |
| pyflate                  | 409 ms                                                      | 283 ms: 1.44x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.18 sec: 1.42x faster                                                      |
| generators               | 32.4 ms                                                     | 23.2 ms: 1.39x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.39x faster                                                       |
| richards_super           | 52.2 ms                                                     | 37.7 ms: 1.38x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.08 ms: 1.36x faster                                                       |
| nbody                    | 71.3 ms                                                     | 52.4 ms: 1.36x faster                                                       |
| raytrace                 | 273 ms                                                      | 202 ms: 1.35x faster                                                        |
| deepcopy                 | 255 us                                                      | 190 us: 1.34x faster                                                        |
| regex_compile            | 106 ms                                                      | 79.7 ms: 1.33x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 205 us: 1.31x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.09 ms: 1.30x faster                                                       |
| pycparser                | 930 ms                                                      | 720 ms: 1.29x faster                                                        |
| scimark_fft              | 187 ms                                                      | 145 ms: 1.29x faster                                                        |
| richards                 | 42.4 ms                                                     | 33.4 ms: 1.27x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 39.8 ms: 1.27x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 972 ms: 1.25x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 35.7 ms: 1.25x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.23x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 483 ms: 1.23x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.4 ms: 1.20x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.87 us: 1.18x faster                                                       |
| sympy_sum                | 107 ms                                                      | 91.2 ms: 1.17x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.53 sec: 1.17x faster                                                      |
| thrift                   | 617 us                                                      | 530 us: 1.17x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 828 us: 1.16x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 5.00 ms: 1.15x faster                                                       |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 86.1 ms: 1.13x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 49.6 ms: 1.12x faster                                                       |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                        |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.3 ms: 1.10x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.53 ms: 1.09x faster                                                       |
| json                     | 3.14 ms                                                     | 2.90 ms: 1.08x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 37.5 ms: 1.06x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 18.7 ms: 1.06x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 63.4 ms: 1.05x faster                                                       |
| django_template          | 28.9 ms                                                     | 27.5 ms: 1.05x faster                                                       |
| sympy_expand             | 314 ms                                                      | 305 ms: 1.03x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 74.4 ms: 1.02x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.65 us: 1.02x faster                                                       |
| fannkuch                 | 256 ms                                                      | 252 ms: 1.02x faster                                                        |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 76.3 ms: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.9 us: 1.06x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.24 ms: 1.08x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.6 ms: 1.13x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.5 ms: 1.14x slower                                                       |
| mypy2                    | 555 ms                                                      | 646 ms: 1.16x slower                                                        |
| async_generators         | 222 ms                                                      | 258 ms: 1.16x slower                                                        |
| genshi_xml               | 41.0 ms                                                     | 48.0 ms: 1.17x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.1 ms: 1.21x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 82.7 ms: 1.33x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.97 ms: 1.40x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 22.0 ms: 1.42x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.52x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                                |

Benchmark hidden because not significant (2): sqlglot_normalize, logging_simple
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.253x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown
# Results vs. 3.10.4

- fork: brandtbucher
- ref: nojit
- machine: windows-amd64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.209x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                               |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                             |
| html5lib       | 51.0 ms                                                     | 37.1 ms: 1.37x faster                                              |
| Geometric mean | (ref)                                                       | 1.21x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 409 ms: 2.71x faster                                               |
| async_tree_none         | 435 ms                                                      | 185 ms: 2.35x faster                                               |
| async_tree_memoization  | 526 ms                                                      | 226 ms: 2.33x faster                                               |
| async_tree_cpu_io_mixed | 638 ms                                                      | 349 ms: 1.83x faster                                               |
| Geometric mean          | (ref)                                                       | 2.28x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 51.2 ms: 1.21x faster                                              |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                               |
| nbody          | 71.3 ms                                                     | 73.5 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                       | 1.06x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 82.9 ms: 1.28x faster                                              |
| regex_effbot   | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                              |
| regex_dna      | 136 ms                                                      | 124 ms: 1.10x faster                                               |
| regex_v8       | 15.4 ms                                                     | 15.6 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                       | 1.12x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.80 ms: 1.35x faster                                              |
| unpickle_pure_python | 183 us                                                      | 144 us: 1.28x faster                                               |
| pickle_pure_python   | 270 us                                                      | 220 us: 1.22x faster                                               |
| tomli_loads          | 1.67 sec                                                    | 1.41 sec: 1.18x faster                                             |
| xml_etree_process    | 44.5 ms                                                     | 40.6 ms: 1.10x faster                                              |
| xml_etree_parse      | 96.8 ms                                                     | 88.6 ms: 1.09x faster                                              |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                              |
| xml_etree_generate   | 55.5 ms                                                     | 57.0 ms: 1.03x slower                                              |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                              |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.3 ms: 1.11x slower                                              |
| python_startup         | 20.6 ms                                                     | 23.4 ms: 1.13x slower                                              |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.71 ms: 1.35x faster                                              |
| genshi_xml      | 41.0 ms                                                     | 34.9 ms: 1.17x faster                                              |
| genshi_text     | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                              |
| django_template | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                              |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.98x faster                                               |
| async_tree_io            | 1.11 sec                                                    | 409 ms: 2.71x faster                                               |
| async_tree_none          | 435 ms                                                      | 185 ms: 2.35x faster                                               |
| async_tree_memoization   | 526 ms                                                      | 226 ms: 2.33x faster                                               |
| deltablue                | 4.19 ms                                                     | 2.23 ms: 1.88x faster                                              |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 349 ms: 1.83x faster                                               |
| pylint                   | 350 ms                                                      | 201 ms: 1.75x faster                                               |
| go                       | 139 ms                                                      | 85.3 ms: 1.63x faster                                              |
| logging_silent           | 94.6 ns                                                     | 61.7 ns: 1.53x faster                                              |
| scimark_lu               | 85.8 ms                                                     | 57.0 ms: 1.51x faster                                              |
| richards_super           | 52.2 ms                                                     | 35.3 ms: 1.48x faster                                              |
| generators               | 32.4 ms                                                     | 21.9 ms: 1.48x faster                                              |
| raytrace                 | 273 ms                                                      | 188 ms: 1.45x faster                                               |
| chaos                    | 61.7 ms                                                     | 42.8 ms: 1.44x faster                                              |
| deepcopy_memo            | 28.8 us                                                     | 20.4 us: 1.41x faster                                              |
| sqlglot_parse            | 1.22 ms                                                     | 877 us: 1.39x faster                                               |
| html5lib                 | 51.0 ms                                                     | 37.1 ms: 1.37x faster                                              |
| deepcopy                 | 255 us                                                      | 187 us: 1.37x faster                                               |
| richards                 | 42.4 ms                                                     | 31.1 ms: 1.37x faster                                              |
| json_dumps               | 9.16 ms                                                     | 6.80 ms: 1.35x faster                                              |
| mako                     | 9.03 ms                                                     | 6.71 ms: 1.35x faster                                              |
| comprehensions           | 16.5 us                                                     | 12.3 us: 1.34x faster                                              |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.34x faster                                              |
| hexiom                   | 5.74 ms                                                     | 4.33 ms: 1.33x faster                                              |
| spectral_norm            | 77.3 ms                                                     | 59.1 ms: 1.31x faster                                              |
| crypto_pyaes             | 62.5 ms                                                     | 48.2 ms: 1.30x faster                                              |
| dulwich_log              | 50.5 ms                                                     | 39.0 ms: 1.29x faster                                              |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.5 ms: 1.29x faster                                              |
| pyflate                  | 409 ms                                                      | 319 ms: 1.28x faster                                               |
| regex_compile            | 106 ms                                                      | 82.9 ms: 1.28x faster                                              |
| unpickle_pure_python     | 183 us                                                      | 144 us: 1.28x faster                                               |
| pycparser                | 930 ms                                                      | 747 ms: 1.25x faster                                               |
| pickle_pure_python       | 270 us                                                      | 220 us: 1.22x faster                                               |
| sympy_sum                | 107 ms                                                      | 88.4 ms: 1.21x faster                                              |
| float                    | 61.7 ms                                                     | 51.2 ms: 1.21x faster                                              |
| coroutines               | 16.0 ms                                                     | 13.3 ms: 1.20x faster                                              |
| thrift                   | 617 us                                                      | 514 us: 1.20x faster                                               |
| scimark_sor              | 106 ms                                                      | 88.9 ms: 1.19x faster                                              |
| mdp                      | 1.78 sec                                                    | 1.50 sec: 1.19x faster                                             |
| tomli_loads              | 1.67 sec                                                    | 1.41 sec: 1.18x faster                                             |
| genshi_xml               | 41.0 ms                                                     | 34.9 ms: 1.17x faster                                              |
| genshi_text              | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                              |
| deepcopy_reduce          | 2.20 us                                                     | 1.89 us: 1.16x faster                                              |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                             |
| bench_thread_pool        | 958 us                                                      | 829 us: 1.16x faster                                               |
| sqlite_synth             | 1.91 us                                                     | 1.66 us: 1.15x faster                                              |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                              |
| regex_effbot             | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                              |
| sympy_str                | 194 ms                                                      | 171 ms: 1.14x faster                                               |
| django_template          | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                              |
| pprint_pformat           | 1.22 sec                                                    | 1.09 sec: 1.12x faster                                             |
| sqlglot_optimize         | 39.8 ms                                                     | 35.6 ms: 1.12x faster                                              |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                               |
| regex_dna                | 136 ms                                                      | 124 ms: 1.10x faster                                               |
| xml_etree_process        | 44.5 ms                                                     | 40.6 ms: 1.10x faster                                              |
| xml_etree_parse          | 96.8 ms                                                     | 88.6 ms: 1.09x faster                                              |
| sympy_expand             | 314 ms                                                      | 288 ms: 1.09x faster                                               |
| pprint_safe_repr         | 592 ms                                                      | 542 ms: 1.09x faster                                               |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.54 ms: 1.07x faster                                              |
| json                     | 3.14 ms                                                     | 2.97 ms: 1.06x faster                                              |
| sqlglot_normalize        | 205 ms                                                      | 196 ms: 1.05x faster                                               |
| nqueens                  | 66.6 ms                                                     | 63.8 ms: 1.04x faster                                              |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                              |
| scimark_fft              | 187 ms                                                      | 185 ms: 1.01x faster                                               |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                               |
| regex_v8                 | 15.4 ms                                                     | 15.6 ms: 1.01x slower                                              |
| logging_format           | 6.76 us                                                     | 6.83 us: 1.01x slower                                              |
| meteor_contest           | 75.9 ms                                                     | 77.5 ms: 1.02x slower                                              |
| logging_simple           | 6.22 us                                                     | 6.37 us: 1.02x slower                                              |
| xml_etree_generate       | 55.5 ms                                                     | 57.0 ms: 1.03x slower                                              |
| nbody                    | 71.3 ms                                                     | 73.5 ms: 1.03x slower                                              |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                              |
| fannkuch                 | 256 ms                                                      | 271 ms: 1.06x slower                                               |
| async_generators         | 222 ms                                                      | 236 ms: 1.06x slower                                               |
| python_startup_no_site   | 15.5 ms                                                     | 17.3 ms: 1.11x slower                                              |
| python_startup           | 20.6 ms                                                     | 23.4 ms: 1.13x slower                                              |
| mypy2                    | 555 ms                                                      | 639 ms: 1.15x slower                                               |
| coverage                 | 39.0 ms                                                     | 46.8 ms: 1.20x slower                                              |
| telco                    | 3.94 ms                                                     | 4.78 ms: 1.21x slower                                              |
| bench_mp_pool            | 62.0 ms                                                     | 82.1 ms: 1.32x slower                                              |
| gc_traversal             | 1.41 ms                                                     | 1.96 ms: 1.39x slower                                              |
| create_gc_cycles         | 800 us                                                      | 1.20 ms: 1.50x slower                                              |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                       |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250107-3.14.0a3+-f098037/bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.209x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown
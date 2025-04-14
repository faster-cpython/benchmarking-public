# Results vs. 3.10.4

- fork: python
- ref: v3.13.1
- machine: windows-amd64
- commit hash: 0671451
- commit date: 2024-12-03
- overall geometric mean: 1.209x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 216 ms: 1.14x faster                                        |
| chameleon      | 5.79 ms                                                     | 4.87 ms: 1.19x faster                                       |
| docutils       | 1.92 sec                                                    | 1.55 sec: 1.24x faster                                      |
| html5lib       | 51.0 ms                                                     | 38.5 ms: 1.33x faster                                       |
| tornado_http   | 108 ms                                                      | 82.1 ms: 1.32x faster                                       |
| Geometric mean | (ref)                                                       | 1.24x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 516 ms: 2.15x faster                                        |
| async_tree_none         | 435 ms                                                      | 221 ms: 1.97x faster                                        |
| async_tree_memoization  | 526 ms                                                      | 269 ms: 1.96x faster                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 386 ms: 1.65x faster                                        |
| Geometric mean          | (ref)                                                       | 1.92x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 61.7 ms                                                     | 49.1 ms: 1.26x faster                                       |
| nbody          | 71.3 ms                                                     | 67.0 ms: 1.06x faster                                       |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                       | 1.11x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.7 ms: 1.30x faster                                       |
| regex_dna      | 136 ms                                                      | 115 ms: 1.18x faster                                        |
| regex_effbot   | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                       |
| regex_v8       | 15.4 ms                                                     | 25.8 ms: 1.67x slower                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.20 ms: 1.48x faster                                       |
| pickle_pure_python   | 270 us                                                      | 190 us: 1.42x faster                                        |
| unpickle_pure_python | 183 us                                                      | 133 us: 1.38x faster                                        |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                      |
| xml_etree_process    | 44.5 ms                                                     | 36.9 ms: 1.20x faster                                       |
| xml_etree_parse      | 96.8 ms                                                     | 92.4 ms: 1.05x faster                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.5 ms: 1.04x faster                                       |
| xml_etree_generate   | 55.5 ms                                                     | 53.9 ms: 1.03x faster                                       |
| json_loads           | 14.0 us                                                     | 15.8 us: 1.13x slower                                       |
| Geometric mean       | (ref)                                                       | 1.17x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.1 ms: 1.10x slower                                       |
| python_startup         | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 20.5 ms: 1.41x faster                                       |
| mako            | 9.03 ms                                                     | 6.65 ms: 1.36x faster                                       |
| genshi_text     | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                       |
| genshi_xml      | 41.0 ms                                                     | 33.6 ms: 1.22x faster                                       |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.24x faster                                        |
| deltablue                | 4.19 ms                                                     | 1.93 ms: 2.17x faster                                       |
| async_tree_io            | 1.11 sec                                                    | 516 ms: 2.15x faster                                        |
| async_tree_none          | 435 ms                                                      | 221 ms: 1.97x faster                                        |
| async_tree_memoization   | 526 ms                                                      | 269 ms: 1.96x faster                                        |
| logging_silent           | 94.6 ns                                                     | 53.7 ns: 1.76x faster                                       |
| raytrace                 | 273 ms                                                      | 158 ms: 1.73x faster                                        |
| richards_super           | 52.2 ms                                                     | 30.7 ms: 1.70x faster                                       |
| pylint                   | 350 ms                                                      | 207 ms: 1.70x faster                                        |
| generators               | 32.4 ms                                                     | 19.5 ms: 1.66x faster                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 386 ms: 1.65x faster                                        |
| chaos                    | 61.7 ms                                                     | 37.9 ms: 1.63x faster                                       |
| go                       | 139 ms                                                      | 86.6 ms: 1.60x faster                                       |
| sqlglot_parse            | 1.22 ms                                                     | 769 us: 1.58x faster                                        |
| richards                 | 42.4 ms                                                     | 27.1 ms: 1.57x faster                                       |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.55x faster                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 966 us: 1.53x faster                                        |
| json_dumps               | 9.16 ms                                                     | 6.20 ms: 1.48x faster                                       |
| scimark_lu               | 85.8 ms                                                     | 58.3 ms: 1.47x faster                                       |
| hexiom                   | 5.74 ms                                                     | 3.91 ms: 1.47x faster                                       |
| pyflate                  | 409 ms                                                      | 286 ms: 1.43x faster                                        |
| pickle_pure_python       | 270 us                                                      | 190 us: 1.42x faster                                        |
| django_template          | 28.9 ms                                                     | 20.5 ms: 1.41x faster                                       |
| crypto_pyaes             | 62.5 ms                                                     | 45.2 ms: 1.38x faster                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.4 ms: 1.38x faster                                       |
| unpickle_pure_python     | 183 us                                                      | 133 us: 1.38x faster                                        |
| pycparser                | 930 ms                                                      | 685 ms: 1.36x faster                                        |
| mako                     | 9.03 ms                                                     | 6.65 ms: 1.36x faster                                       |
| scimark_sor              | 106 ms                                                      | 78.3 ms: 1.36x faster                                       |
| html5lib                 | 51.0 ms                                                     | 38.5 ms: 1.33x faster                                       |
| tornado_http             | 108 ms                                                      | 82.1 ms: 1.32x faster                                       |
| sqlalchemy_declarative   | 103 ms                                                      | 78.8 ms: 1.31x faster                                       |
| regex_compile            | 106 ms                                                      | 81.7 ms: 1.30x faster                                       |
| genshi_text              | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                       |
| mdp                      | 1.78 sec                                                    | 1.41 sec: 1.26x faster                                      |
| float                    | 61.7 ms                                                     | 49.1 ms: 1.26x faster                                       |
| dulwich_log              | 50.5 ms                                                     | 40.4 ms: 1.25x faster                                       |
| sympy_sum                | 107 ms                                                      | 86.0 ms: 1.24x faster                                       |
| docutils                 | 1.92 sec                                                    | 1.55 sec: 1.24x faster                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.24x faster                                       |
| genshi_xml               | 41.0 ms                                                     | 33.6 ms: 1.22x faster                                       |
| deepcopy_memo            | 28.8 us                                                     | 23.6 us: 1.22x faster                                       |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                      |
| sqlalchemy_imperative    | 11.4 ms                                                     | 9.39 ms: 1.21x faster                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.01 sec: 1.21x faster                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.9 ms: 1.20x faster                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 33.1 ms: 1.20x faster                                       |
| pprint_safe_repr         | 592 ms                                                      | 494 ms: 1.20x faster                                        |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.19x faster                                       |
| chameleon                | 5.79 ms                                                     | 4.87 ms: 1.19x faster                                       |
| regex_dna                | 136 ms                                                      | 115 ms: 1.18x faster                                        |
| spectral_norm            | 77.3 ms                                                     | 65.5 ms: 1.18x faster                                       |
| sqlglot_normalize        | 205 ms                                                      | 175 ms: 1.17x faster                                        |
| nqueens                  | 66.6 ms                                                     | 57.3 ms: 1.16x faster                                       |
| sympy_str                | 194 ms                                                      | 168 ms: 1.16x faster                                        |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                       |
| regex_effbot             | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                       |
| 2to3                     | 246 ms                                                      | 216 ms: 1.14x faster                                        |
| bench_thread_pool        | 958 us                                                      | 844 us: 1.13x faster                                        |
| deepcopy                 | 255 us                                                      | 230 us: 1.11x faster                                        |
| sympy_expand             | 314 ms                                                      | 287 ms: 1.10x faster                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.49 ms: 1.09x faster                                       |
| logging_format           | 6.76 us                                                     | 6.21 us: 1.09x faster                                       |
| scimark_fft              | 187 ms                                                      | 174 ms: 1.07x faster                                        |
| meteor_contest           | 75.9 ms                                                     | 70.8 ms: 1.07x faster                                       |
| logging_simple           | 6.22 us                                                     | 5.84 us: 1.06x faster                                       |
| nbody                    | 71.3 ms                                                     | 67.0 ms: 1.06x faster                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.09 us: 1.05x faster                                       |
| xml_etree_parse          | 96.8 ms                                                     | 92.4 ms: 1.05x faster                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.5 ms: 1.04x faster                                       |
| xml_etree_generate       | 55.5 ms                                                     | 53.9 ms: 1.03x faster                                       |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                        |
| fannkuch                 | 256 ms                                                      | 254 ms: 1.01x faster                                        |
| json                     | 3.14 ms                                                     | 3.18 ms: 1.01x slower                                       |
| async_generators         | 222 ms                                                      | 228 ms: 1.03x slower                                        |
| python_startup_no_site   | 15.5 ms                                                     | 17.1 ms: 1.10x slower                                       |
| json_loads               | 14.0 us                                                     | 15.8 us: 1.13x slower                                       |
| coverage                 | 39.0 ms                                                     | 45.1 ms: 1.16x slower                                       |
| python_startup           | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                       |
| telco                    | 3.94 ms                                                     | 4.94 ms: 1.25x slower                                       |
| bench_mp_pool            | 62.0 ms                                                     | 84.3 ms: 1.36x slower                                       |
| gc_traversal             | 1.41 ms                                                     | 1.92 ms: 1.36x slower                                       |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.53x slower                                       |
| regex_v8                 | 15.4 ms                                                     | 25.8 ms: 1.67x slower                                       |
| thrift                   | 617 us                                                      | 8.47 ms: 13.73x slower                                      |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20241203-3.13.1-0671451/bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.209x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown
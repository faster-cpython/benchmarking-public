# Results vs. 3.10.4

- fork: python
- ref: v3.13.0
- machine: windows-amd64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.205x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                        |
| chameleon      | 5.79 ms                                                     | 4.82 ms: 1.20x faster                                       |
| docutils       | 1.92 sec                                                    | 1.57 sec: 1.22x faster                                      |
| html5lib       | 51.0 ms                                                     | 38.9 ms: 1.31x faster                                       |
| tornado_http   | 108 ms                                                      | 93.0 ms: 1.16x faster                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 521 ms: 2.13x faster                                        |
| async_tree_none         | 435 ms                                                      | 226 ms: 1.93x faster                                        |
| async_tree_memoization  | 526 ms                                                      | 276 ms: 1.91x faster                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 383 ms: 1.67x faster                                        |
| Geometric mean          | (ref)                                                       | 1.90x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 61.7 ms                                                     | 49.9 ms: 1.24x faster                                       |
| nbody          | 71.3 ms                                                     | 68.4 ms: 1.04x faster                                       |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                       | 1.09x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.5 ms: 1.32x faster                                       |
| regex_dna      | 136 ms                                                      | 115 ms: 1.18x faster                                        |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                       |
| regex_v8       | 15.4 ms                                                     | 21.4 ms: 1.39x slower                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.92 ms: 1.55x faster                                       |
| pickle_pure_python   | 270 us                                                      | 190 us: 1.42x faster                                        |
| unpickle_pure_python | 183 us                                                      | 133 us: 1.37x faster                                        |
| xml_etree_process    | 44.5 ms                                                     | 37.0 ms: 1.20x faster                                       |
| tomli_loads          | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.8 ms: 1.05x faster                                       |
| xml_etree_parse      | 96.8 ms                                                     | 93.6 ms: 1.03x faster                                       |
| xml_etree_generate   | 55.5 ms                                                     | 54.0 ms: 1.03x faster                                       |
| json_loads           | 14.0 us                                                     | 15.1 us: 1.08x slower                                       |
| Geometric mean       | (ref)                                                       | 1.18x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                       |
| python_startup         | 20.6 ms                                                     | 25.4 ms: 1.23x slower                                       |
| Geometric mean         | (ref)                                                       | 1.20x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.35 ms: 1.42x faster                                       |
| django_template | 28.9 ms                                                     | 22.4 ms: 1.29x faster                                       |
| genshi_text     | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                       |
| genshi_xml      | 41.0 ms                                                     | 35.5 ms: 1.16x faster                                       |
| Geometric mean  | (ref)                                                       | 1.28x faster                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.19x faster                                        |
| deltablue                | 4.19 ms                                                     | 1.92 ms: 2.18x faster                                       |
| async_tree_io            | 1.11 sec                                                    | 521 ms: 2.13x faster                                        |
| async_tree_none          | 435 ms                                                      | 226 ms: 1.93x faster                                        |
| async_tree_memoization   | 526 ms                                                      | 276 ms: 1.91x faster                                        |
| logging_silent           | 94.6 ns                                                     | 54.6 ns: 1.73x faster                                       |
| raytrace                 | 273 ms                                                      | 160 ms: 1.71x faster                                        |
| richards_super           | 52.2 ms                                                     | 30.9 ms: 1.69x faster                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 383 ms: 1.67x faster                                        |
| pylint                   | 350 ms                                                      | 211 ms: 1.66x faster                                        |
| generators               | 32.4 ms                                                     | 19.5 ms: 1.66x faster                                       |
| scimark_lu               | 85.8 ms                                                     | 53.0 ms: 1.62x faster                                       |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.61x faster                                       |
| chaos                    | 61.7 ms                                                     | 38.5 ms: 1.60x faster                                       |
| go                       | 139 ms                                                      | 87.0 ms: 1.60x faster                                       |
| sqlglot_parse            | 1.22 ms                                                     | 771 us: 1.58x faster                                        |
| richards                 | 42.4 ms                                                     | 27.3 ms: 1.55x faster                                       |
| json_dumps               | 9.16 ms                                                     | 5.92 ms: 1.55x faster                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 956 us: 1.54x faster                                        |
| hexiom                   | 5.74 ms                                                     | 3.89 ms: 1.48x faster                                       |
| pyflate                  | 409 ms                                                      | 283 ms: 1.44x faster                                        |
| pickle_pure_python       | 270 us                                                      | 190 us: 1.42x faster                                        |
| mako                     | 9.03 ms                                                     | 6.35 ms: 1.42x faster                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.8 ms: 1.40x faster                                       |
| scimark_sor              | 106 ms                                                      | 76.2 ms: 1.39x faster                                       |
| crypto_pyaes             | 62.5 ms                                                     | 45.4 ms: 1.38x faster                                       |
| unpickle_pure_python     | 183 us                                                      | 133 us: 1.37x faster                                        |
| pycparser                | 930 ms                                                      | 683 ms: 1.36x faster                                        |
| regex_compile            | 106 ms                                                      | 80.5 ms: 1.32x faster                                       |
| html5lib                 | 51.0 ms                                                     | 38.9 ms: 1.31x faster                                       |
| sqlalchemy_declarative   | 103 ms                                                      | 79.2 ms: 1.31x faster                                       |
| django_template          | 28.9 ms                                                     | 22.4 ms: 1.29x faster                                       |
| mdp                      | 1.78 sec                                                    | 1.39 sec: 1.28x faster                                      |
| genshi_text              | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                       |
| coroutines               | 16.0 ms                                                     | 12.8 ms: 1.25x faster                                       |
| dulwich_log              | 50.5 ms                                                     | 40.8 ms: 1.24x faster                                       |
| float                    | 61.7 ms                                                     | 49.9 ms: 1.24x faster                                       |
| deepcopy_memo            | 28.8 us                                                     | 23.3 us: 1.24x faster                                       |
| sympy_sum                | 107 ms                                                      | 86.9 ms: 1.23x faster                                       |
| spectral_norm            | 77.3 ms                                                     | 62.8 ms: 1.23x faster                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                       |
| docutils                 | 1.92 sec                                                    | 1.57 sec: 1.22x faster                                      |
| pprint_pformat           | 1.22 sec                                                    | 999 ms: 1.22x faster                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 32.9 ms: 1.21x faster                                       |
| xml_etree_process        | 44.5 ms                                                     | 37.0 ms: 1.20x faster                                       |
| chameleon                | 5.79 ms                                                     | 4.82 ms: 1.20x faster                                       |
| pprint_safe_repr         | 592 ms                                                      | 494 ms: 1.20x faster                                        |
| tomli_loads              | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                      |
| regex_dna                | 136 ms                                                      | 115 ms: 1.18x faster                                        |
| sqlalchemy_imperative    | 11.4 ms                                                     | 9.69 ms: 1.18x faster                                       |
| sqlglot_normalize        | 205 ms                                                      | 175 ms: 1.18x faster                                        |
| nqueens                  | 66.6 ms                                                     | 56.7 ms: 1.18x faster                                       |
| tornado_http             | 108 ms                                                      | 93.0 ms: 1.16x faster                                       |
| genshi_xml               | 41.0 ms                                                     | 35.5 ms: 1.16x faster                                       |
| sympy_str                | 194 ms                                                      | 169 ms: 1.15x faster                                        |
| bench_thread_pool        | 958 us                                                      | 847 us: 1.13x faster                                        |
| deepcopy                 | 255 us                                                      | 226 us: 1.13x faster                                        |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.46 ms: 1.11x faster                                       |
| scimark_fft              | 187 ms                                                      | 172 ms: 1.09x faster                                        |
| logging_format           | 6.76 us                                                     | 6.26 us: 1.08x faster                                       |
| sympy_expand             | 314 ms                                                      | 291 ms: 1.08x faster                                        |
| deepcopy_reduce          | 2.20 us                                                     | 2.06 us: 1.07x faster                                       |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.8 ms: 1.05x faster                                       |
| logging_simple           | 6.22 us                                                     | 5.96 us: 1.04x faster                                       |
| nbody                    | 71.3 ms                                                     | 68.4 ms: 1.04x faster                                       |
| xml_etree_parse          | 96.8 ms                                                     | 93.6 ms: 1.03x faster                                       |
| meteor_contest           | 75.9 ms                                                     | 73.5 ms: 1.03x faster                                       |
| xml_etree_generate       | 55.5 ms                                                     | 54.0 ms: 1.03x faster                                       |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                        |
| fannkuch                 | 256 ms                                                      | 253 ms: 1.01x faster                                        |
| async_generators         | 222 ms                                                      | 223 ms: 1.01x slower                                        |
| pathlib                  | 75.7 ms                                                     | 80.9 ms: 1.07x slower                                       |
| json_loads               | 14.0 us                                                     | 15.1 us: 1.08x slower                                       |
| coverage                 | 39.0 ms                                                     | 45.6 ms: 1.17x slower                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                       |
| telco                    | 3.94 ms                                                     | 4.79 ms: 1.22x slower                                       |
| mypy2                    | 555 ms                                                      | 679 ms: 1.22x slower                                        |
| python_startup           | 20.6 ms                                                     | 25.4 ms: 1.23x slower                                       |
| regex_v8                 | 15.4 ms                                                     | 21.4 ms: 1.39x slower                                       |
| bench_mp_pool            | 62.0 ms                                                     | 86.4 ms: 1.39x slower                                       |
| gc_traversal             | 1.41 ms                                                     | 1.97 ms: 1.40x slower                                       |
| create_gc_cycles         | 800 us                                                      | 1.26 ms: 1.57x slower                                       |
| thrift                   | 617 us                                                      | 8.80 ms: 14.25x slower                                      |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                |

Benchmark hidden because not significant (1): json
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.205x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown
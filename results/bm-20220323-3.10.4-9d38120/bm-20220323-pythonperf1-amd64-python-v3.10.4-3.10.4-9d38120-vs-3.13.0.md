# Results vs. 3.13.0

- fork: python
- ref: v3.10.4
- machine: windows-amd64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.165x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 246 ms: 1.11x slower                                        |
| chameleon      | 4.82 ms                                                     | 5.79 ms: 1.20x slower                                       |
| docutils       | 1.57 sec                                                    | 1.92 sec: 1.22x slower                                      |
| html5lib       | 38.9 ms                                                     | 51.0 ms: 1.31x slower                                       |
| tornado_http   | 93.0 ms                                                     | 108 ms: 1.16x slower                                        |
| Geometric mean | (ref)                                                       | 1.20x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_generators        | 223 ms                                                      | 222 ms: 1.01x faster                                        |
| coroutines              | 12.8 ms                                                     | 16.0 ms: 1.25x slower                                       |
| async_tree_cpu_io_mixed | 383 ms                                                      | 638 ms: 1.67x slower                                        |
| async_tree_memoization  | 276 ms                                                      | 526 ms: 1.91x slower                                        |
| async_tree_none         | 226 ms                                                      | 435 ms: 1.93x slower                                        |
| async_tree_io           | 521 ms                                                      | 1.11 sec: 2.13x slower                                      |
| Geometric mean          | (ref)                                                       | 1.59x slower                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                        |
| nbody          | 68.4 ms                                                     | 71.3 ms: 1.04x slower                                       |
| float          | 49.9 ms                                                     | 61.7 ms: 1.24x slower                                       |
| Geometric mean | (ref)                                                       | 1.09x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.4 ms: 1.39x faster                                       |
| regex_effbot   | 1.58 ms                                                     | 1.66 ms: 1.05x slower                                       |
| regex_dna      | 115 ms                                                      | 136 ms: 1.18x slower                                        |
| regex_compile  | 80.5 ms                                                     | 106 ms: 1.32x slower                                        |
| Geometric mean | (ref)                                                       | 1.04x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.0 us: 1.08x faster                                       |
| xml_etree_generate   | 54.0 ms                                                     | 55.5 ms: 1.03x slower                                       |
| xml_etree_parse      | 93.6 ms                                                     | 96.8 ms: 1.03x slower                                       |
| xml_etree_iterparse  | 61.8 ms                                                     | 65.0 ms: 1.05x slower                                       |
| tomli_loads          | 1.39 sec                                                    | 1.67 sec: 1.20x slower                                      |
| xml_etree_process    | 37.0 ms                                                     | 44.5 ms: 1.20x slower                                       |
| unpickle_pure_python | 133 us                                                      | 183 us: 1.37x slower                                        |
| pickle_pure_python   | 190 us                                                      | 270 us: 1.42x slower                                        |
| json_dumps           | 5.92 ms                                                     | 9.16 ms: 1.55x slower                                       |
| Geometric mean       | (ref)                                                       | 1.18x slower                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 20.6 ms: 1.23x faster                                       |
| python_startup_no_site | 18.1 ms                                                     | 15.5 ms: 1.17x faster                                       |
| Geometric mean         | (ref)                                                       | 1.20x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 41.0 ms: 1.16x slower                                       |
| genshi_text     | 15.6 ms                                                     | 19.8 ms: 1.27x slower                                       |
| django_template | 22.4 ms                                                     | 28.9 ms: 1.29x slower                                       |
| mako            | 6.35 ms                                                     | 9.03 ms: 1.42x slower                                       |
| Geometric mean  | (ref)                                                       | 1.28x slower                                                |

All benchmarks:
===============

| Benchmark                | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| thrift                   | 8.80 ms                                                     | 617 us: 14.25x faster                                       |
| create_gc_cycles         | 1.26 ms                                                     | 800 us: 1.57x faster                                        |
| gc_traversal             | 1.97 ms                                                     | 1.41 ms: 1.40x faster                                       |
| bench_mp_pool            | 86.4 ms                                                     | 62.0 ms: 1.39x faster                                       |
| regex_v8                 | 21.4 ms                                                     | 15.4 ms: 1.39x faster                                       |
| python_startup           | 25.4 ms                                                     | 20.6 ms: 1.23x faster                                       |
| mypy2                    | 679 ms                                                      | 555 ms: 1.22x faster                                        |
| telco                    | 4.79 ms                                                     | 3.94 ms: 1.22x faster                                       |
| python_startup_no_site   | 18.1 ms                                                     | 15.5 ms: 1.17x faster                                       |
| coverage                 | 45.6 ms                                                     | 39.0 ms: 1.17x faster                                       |
| json_loads               | 15.1 us                                                     | 14.0 us: 1.08x faster                                       |
| pathlib                  | 80.9 ms                                                     | 75.7 ms: 1.07x faster                                       |
| async_generators         | 223 ms                                                      | 222 ms: 1.01x faster                                        |
| fannkuch                 | 253 ms                                                      | 256 ms: 1.01x slower                                        |
| pidigits                 | 148 ms                                                      | 149 ms: 1.01x slower                                        |
| xml_etree_generate       | 54.0 ms                                                     | 55.5 ms: 1.03x slower                                       |
| meteor_contest           | 73.5 ms                                                     | 75.9 ms: 1.03x slower                                       |
| xml_etree_parse          | 93.6 ms                                                     | 96.8 ms: 1.03x slower                                       |
| nbody                    | 68.4 ms                                                     | 71.3 ms: 1.04x slower                                       |
| logging_simple           | 5.96 us                                                     | 6.22 us: 1.04x slower                                       |
| xml_etree_iterparse      | 61.8 ms                                                     | 65.0 ms: 1.05x slower                                       |
| regex_effbot             | 1.58 ms                                                     | 1.66 ms: 1.05x slower                                       |
| deepcopy_reduce          | 2.06 us                                                     | 2.20 us: 1.07x slower                                       |
| sympy_expand             | 291 ms                                                      | 314 ms: 1.08x slower                                        |
| logging_format           | 6.26 us                                                     | 6.76 us: 1.08x slower                                       |
| scimark_fft              | 172 ms                                                      | 187 ms: 1.09x slower                                        |
| scimark_sparse_mat_mult  | 2.46 ms                                                     | 2.72 ms: 1.11x slower                                       |
| 2to3                     | 221 ms                                                      | 246 ms: 1.11x slower                                        |
| deepcopy                 | 226 us                                                      | 255 us: 1.13x slower                                        |
| bench_thread_pool        | 847 us                                                      | 958 us: 1.13x slower                                        |
| sympy_str                | 169 ms                                                      | 194 ms: 1.15x slower                                        |
| genshi_xml               | 35.5 ms                                                     | 41.0 ms: 1.16x slower                                       |
| tornado_http             | 93.0 ms                                                     | 108 ms: 1.16x slower                                        |
| nqueens                  | 56.7 ms                                                     | 66.6 ms: 1.18x slower                                       |
| sqlglot_normalize        | 175 ms                                                      | 205 ms: 1.18x slower                                        |
| sqlalchemy_imperative    | 9.69 ms                                                     | 11.4 ms: 1.18x slower                                       |
| regex_dna                | 115 ms                                                      | 136 ms: 1.18x slower                                        |
| tomli_loads              | 1.39 sec                                                    | 1.67 sec: 1.20x slower                                      |
| pprint_safe_repr         | 494 ms                                                      | 592 ms: 1.20x slower                                        |
| chameleon                | 4.82 ms                                                     | 5.79 ms: 1.20x slower                                       |
| xml_etree_process        | 37.0 ms                                                     | 44.5 ms: 1.20x slower                                       |
| sqlglot_optimize         | 32.9 ms                                                     | 39.8 ms: 1.21x slower                                       |
| pprint_pformat           | 999 ms                                                      | 1.22 sec: 1.22x slower                                      |
| docutils                 | 1.57 sec                                                    | 1.92 sec: 1.22x slower                                      |
| sympy_integrate          | 12.5 ms                                                     | 15.3 ms: 1.22x slower                                       |
| spectral_norm            | 62.8 ms                                                     | 77.3 ms: 1.23x slower                                       |
| sympy_sum                | 86.9 ms                                                     | 107 ms: 1.23x slower                                        |
| deepcopy_memo            | 23.3 us                                                     | 28.8 us: 1.24x slower                                       |
| float                    | 49.9 ms                                                     | 61.7 ms: 1.24x slower                                       |
| dulwich_log              | 40.8 ms                                                     | 50.5 ms: 1.24x slower                                       |
| coroutines               | 12.8 ms                                                     | 16.0 ms: 1.25x slower                                       |
| genshi_text              | 15.6 ms                                                     | 19.8 ms: 1.27x slower                                       |
| mdp                      | 1.39 sec                                                    | 1.78 sec: 1.28x slower                                      |
| django_template          | 22.4 ms                                                     | 28.9 ms: 1.29x slower                                       |
| sqlalchemy_declarative   | 79.2 ms                                                     | 103 ms: 1.31x slower                                        |
| html5lib                 | 38.9 ms                                                     | 51.0 ms: 1.31x slower                                       |
| regex_compile            | 80.5 ms                                                     | 106 ms: 1.32x slower                                        |
| pycparser                | 683 ms                                                      | 930 ms: 1.36x slower                                        |
| unpickle_pure_python     | 133 us                                                      | 183 us: 1.37x slower                                        |
| crypto_pyaes             | 45.4 ms                                                     | 62.5 ms: 1.38x slower                                       |
| scimark_sor              | 76.2 ms                                                     | 106 ms: 1.39x slower                                        |
| scimark_monte_carlo      | 40.8 ms                                                     | 57.3 ms: 1.40x slower                                       |
| mako                     | 6.35 ms                                                     | 9.03 ms: 1.42x slower                                       |
| pickle_pure_python       | 190 us                                                      | 270 us: 1.42x slower                                        |
| pyflate                  | 283 ms                                                      | 409 ms: 1.44x slower                                        |
| hexiom                   | 3.89 ms                                                     | 5.74 ms: 1.48x slower                                       |
| sqlglot_transpile        | 956 us                                                      | 1.48 ms: 1.54x slower                                       |
| json_dumps               | 5.92 ms                                                     | 9.16 ms: 1.55x slower                                       |
| richards                 | 27.3 ms                                                     | 42.4 ms: 1.55x slower                                       |
| sqlglot_parse            | 771 us                                                      | 1.22 ms: 1.58x slower                                       |
| go                       | 87.0 ms                                                     | 139 ms: 1.60x slower                                        |
| chaos                    | 38.5 ms                                                     | 61.7 ms: 1.60x slower                                       |
| comprehensions           | 10.3 us                                                     | 16.5 us: 1.61x slower                                       |
| scimark_lu               | 53.0 ms                                                     | 85.8 ms: 1.62x slower                                       |
| generators               | 19.5 ms                                                     | 32.4 ms: 1.66x slower                                       |
| pylint                   | 211 ms                                                      | 350 ms: 1.66x slower                                        |
| async_tree_cpu_io_mixed  | 383 ms                                                      | 638 ms: 1.67x slower                                        |
| richards_super           | 30.9 ms                                                     | 52.2 ms: 1.69x slower                                       |
| raytrace                 | 160 ms                                                      | 273 ms: 1.71x slower                                        |
| logging_silent           | 54.6 ns                                                     | 94.6 ns: 1.73x slower                                       |
| async_tree_memoization   | 276 ms                                                      | 526 ms: 1.91x slower                                        |
| async_tree_none          | 226 ms                                                      | 435 ms: 1.93x slower                                        |
| async_tree_io            | 521 ms                                                      | 1.11 sec: 2.13x slower                                      |
| deltablue                | 1.92 ms                                                     | 4.19 ms: 2.18x slower                                       |
| typing_runtime_protocols | 105 us                                                      | 336 us: 3.19x slower                                        |
| Geometric mean           | (ref)                                                       | 1.19x slower                                                |

Benchmark hidden because not significant (1): json
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.165x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.20x
- 95% likely to have a slowdown of 1.20x
- 99% likely to have a slowdown of 1.18x

# Memory
- memory change: unknown
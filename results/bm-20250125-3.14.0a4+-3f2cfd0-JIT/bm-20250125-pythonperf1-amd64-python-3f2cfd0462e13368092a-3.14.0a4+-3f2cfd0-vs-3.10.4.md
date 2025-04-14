# Results vs. 3.10.4

- fork: python
- ref: 3f2cfd0462e13368092a
- machine: windows-amd64
- commit hash: 3f2cfd0
- commit date: 2025-01-25
- overall geometric mean: 1.231x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 231 ms: 1.06x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.76 sec: 1.09x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.4 ms: 1.26x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 426 ms: 2.60x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 226 ms: 2.33x faster                                                        |
| async_tree_none         | 435 ms                                                      | 190 ms: 2.29x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 345 ms: 1.85x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.25x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 40.4 ms: 1.53x faster                                                       |
| nbody          | 71.3 ms                                                     | 55.9 ms: 1.27x faster                                                       |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.26x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 84.6 ms: 1.25x faster                                                       |
| regex_dna      | 136 ms                                                      | 114 ms: 1.20x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 15.1 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 112 us: 1.64x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.21 sec: 1.38x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 213 us: 1.26x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.8 ms: 1.21x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 50.2 ms: 1.11x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.0 ms: 1.08x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.86 us: 1.03x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.80 us: 1.03x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 18.3 us: 1.06x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.08 us: 1.12x slower                                                       |
| json_loads           | 14.0 us                                                     | 16.0 us: 1.14x slower                                                       |
| pickle               | 6.85 us                                                     | 7.93 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                       |
| python_startup         | 20.6 ms                                                     | 24.1 ms: 1.17x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.09 ms: 1.77x faster                                                       |
| django_template | 28.9 ms                                                     | 27.4 ms: 1.05x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 47.3 ms: 1.15x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.00x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 426 ms: 2.60x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 226 ms: 2.33x faster                                                        |
| async_tree_none          | 435 ms                                                      | 190 ms: 2.29x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 345 ms: 1.85x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.09 ms: 1.77x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.42 ms: 1.73x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 17.1 us: 1.69x faster                                                       |
| scimark_sor              | 106 ms                                                      | 63.2 ms: 1.68x faster                                                       |
| pylint                   | 350 ms                                                      | 212 ms: 1.65x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 112 us: 1.64x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 59.4 ns: 1.59x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 49.2 ms: 1.57x faster                                                       |
| float                    | 61.7 ms                                                     | 40.4 ms: 1.53x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 41.1 ms: 1.52x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 56.9 ms: 1.51x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.3 ms: 1.49x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.43 sec: 1.48x faster                                                      |
| pyflate                  | 409 ms                                                      | 277 ms: 1.48x faster                                                        |
| chaos                    | 61.7 ms                                                     | 42.0 ms: 1.47x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                       |
| go                       | 139 ms                                                      | 95.4 ms: 1.46x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 869 us: 1.40x faster                                                        |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.39x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.21 sec: 1.38x faster                                                      |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.04 ms: 1.34x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.11 ms: 1.33x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 557 ms: 1.31x faster                                                        |
| generators               | 32.4 ms                                                     | 25.0 ms: 1.29x faster                                                       |
| richards_super           | 52.2 ms                                                     | 40.6 ms: 1.29x faster                                                       |
| scimark_fft              | 187 ms                                                      | 146 ms: 1.28x faster                                                        |
| nbody                    | 71.3 ms                                                     | 55.9 ms: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 736 ms: 1.26x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 40.4 ms: 1.26x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 213 us: 1.26x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 970 ms: 1.26x faster                                                        |
| regex_compile            | 106 ms                                                      | 84.6 ms: 1.25x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 487 ms: 1.22x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.8 ms: 1.21x faster                                                       |
| regex_dna                | 136 ms                                                      | 114 ms: 1.20x faster                                                        |
| raytrace                 | 273 ms                                                      | 228 ms: 1.20x faster                                                        |
| richards                 | 42.4 ms                                                     | 35.9 ms: 1.18x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.1 ms: 1.17x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.89 us: 1.16x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.53 sec: 1.16x faster                                                      |
| sympy_sum                | 107 ms                                                      | 93.1 ms: 1.15x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 842 us: 1.14x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 5.05 ms: 1.14x faster                                                       |
| thrift                   | 617 us                                                      | 544 us: 1.14x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.6 ms: 1.13x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 50.2 ms: 1.11x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.10x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.76 sec: 1.09x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.0 ms: 1.08x faster                                                       |
| sympy_str                | 194 ms                                                      | 182 ms: 1.07x faster                                                        |
| 2to3                     | 246 ms                                                      | 231 ms: 1.06x faster                                                        |
| fannkuch                 | 256 ms                                                      | 241 ms: 1.06x faster                                                        |
| django_template          | 28.9 ms                                                     | 27.4 ms: 1.05x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 63.7 ms: 1.05x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 38.5 ms: 1.04x faster                                                       |
| json                     | 3.14 ms                                                     | 3.04 ms: 1.03x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.86 us: 1.03x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 15.1 ms: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                        |
| sympy_expand             | 314 ms                                                      | 311 ms: 1.01x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 208 ms: 1.01x slower                                                        |
| meteor_contest           | 75.9 ms                                                     | 76.8 ms: 1.01x slower                                                       |
| logging_format           | 6.76 us                                                     | 6.92 us: 1.02x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.80 us: 1.03x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 78.5 ms: 1.04x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.48 us: 1.04x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.3 us: 1.06x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 43.0 ns: 1.09x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.34 ms: 1.10x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.08 us: 1.12x slower                                                       |
| async_generators         | 222 ms                                                      | 248 ms: 1.12x slower                                                        |
| json_loads               | 14.0 us                                                     | 16.0 us: 1.14x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 47.3 ms: 1.15x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.93 us: 1.16x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.1 ms: 1.17x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.7 ms: 1.22x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.98 ms: 1.40x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.4 ms: 1.42x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.52x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                                |

Benchmark hidden because not significant (1): genshi_text
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250125-3.14.0a4+-3f2cfd0-JIT/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.231x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown
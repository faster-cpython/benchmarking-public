# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: windows-amd64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.181x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 248 ms: 1.01x slower                                                              |
| docutils       | 1.92 sec                                                    | 1.90 sec: 1.01x faster                                                            |
| html5lib       | 51.0 ms                                                     | 39.1 ms: 1.31x faster                                                             |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 532 ms: 2.08x faster                                                              |
| async_tree_none         | 435 ms                                                      | 212 ms: 2.05x faster                                                              |
| async_tree_memoization  | 526 ms                                                      | 262 ms: 2.01x faster                                                              |
| async_tree_cpu_io_mixed | 638 ms                                                      | 394 ms: 1.62x faster                                                              |
| Geometric mean          | (ref)                                                       | 1.93x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 48.4 ms: 1.28x faster                                                             |
| nbody          | 71.3 ms                                                     | 56.5 ms: 1.26x faster                                                             |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 93.3 ms: 1.14x faster                                                             |
| regex_dna      | 136 ms                                                      | 121 ms: 1.12x faster                                                              |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                             |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.11 ms: 1.50x faster                                                             |
| tomli_loads          | 1.67 sec                                                    | 1.30 sec: 1.29x faster                                                            |
| pickle_pure_python   | 270 us                                                      | 214 us: 1.26x faster                                                              |
| unpickle_pure_python | 183 us                                                      | 149 us: 1.23x faster                                                              |
| xml_etree_process    | 44.5 ms                                                     | 37.1 ms: 1.20x faster                                                             |
| xml_etree_generate   | 55.5 ms                                                     | 51.8 ms: 1.07x faster                                                             |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.0 ms: 1.03x faster                                                             |
| xml_etree_parse      | 96.8 ms                                                     | 93.9 ms: 1.03x faster                                                             |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                             |
| Geometric mean       | (ref)                                                       | 1.17x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 23.5 ms: 1.14x slower                                                             |
| python_startup_no_site | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                             |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.44 ms: 1.66x faster                                                             |
| django_template | 28.9 ms                                                     | 26.9 ms: 1.07x faster                                                             |
| genshi_xml      | 41.0 ms                                                     | 46.4 ms: 1.13x slower                                                             |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                                      |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 115 us: 2.93x faster                                                              |
| async_tree_io            | 1.11 sec                                                    | 532 ms: 2.08x faster                                                              |
| async_tree_none          | 435 ms                                                      | 212 ms: 2.05x faster                                                              |
| async_tree_memoization   | 526 ms                                                      | 262 ms: 2.01x faster                                                              |
| deltablue                | 4.19 ms                                                     | 2.43 ms: 1.72x faster                                                             |
| mako                     | 9.03 ms                                                     | 5.44 ms: 1.66x faster                                                             |
| deepcopy_memo            | 28.8 us                                                     | 17.6 us: 1.64x faster                                                             |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 394 ms: 1.62x faster                                                              |
| logging_silent           | 94.6 ns                                                     | 59.2 ns: 1.60x faster                                                             |
| scimark_sor              | 106 ms                                                      | 68.9 ms: 1.54x faster                                                             |
| json_dumps               | 9.16 ms                                                     | 6.11 ms: 1.50x faster                                                             |
| scimark_lu               | 85.8 ms                                                     | 57.4 ms: 1.49x faster                                                             |
| crypto_pyaes             | 62.5 ms                                                     | 42.3 ms: 1.48x faster                                                             |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.2 ms: 1.46x faster                                                             |
| go                       | 139 ms                                                      | 95.9 ms: 1.45x faster                                                             |
| chaos                    | 61.7 ms                                                     | 42.6 ms: 1.45x faster                                                             |
| spectral_norm            | 77.3 ms                                                     | 55.7 ms: 1.39x faster                                                             |
| richards_super           | 52.2 ms                                                     | 39.0 ms: 1.34x faster                                                             |
| sqlglot_parse            | 1.22 ms                                                     | 915 us: 1.33x faster                                                              |
| html5lib                 | 51.0 ms                                                     | 39.1 ms: 1.31x faster                                                             |
| comprehensions           | 16.5 us                                                     | 12.7 us: 1.29x faster                                                             |
| deepcopy                 | 255 us                                                      | 197 us: 1.29x faster                                                              |
| tomli_loads              | 1.67 sec                                                    | 1.30 sec: 1.29x faster                                                            |
| pyflate                  | 409 ms                                                      | 317 ms: 1.29x faster                                                              |
| generators               | 32.4 ms                                                     | 25.3 ms: 1.28x faster                                                             |
| float                    | 61.7 ms                                                     | 48.4 ms: 1.28x faster                                                             |
| dulwich_log              | 50.5 ms                                                     | 39.7 ms: 1.27x faster                                                             |
| pycparser                | 930 ms                                                      | 734 ms: 1.27x faster                                                              |
| pylint                   | 350 ms                                                      | 277 ms: 1.26x faster                                                              |
| nbody                    | 71.3 ms                                                     | 56.5 ms: 1.26x faster                                                             |
| pickle_pure_python       | 270 us                                                      | 214 us: 1.26x faster                                                              |
| pprint_pformat           | 1.22 sec                                                    | 979 ms: 1.25x faster                                                              |
| pprint_safe_repr         | 592 ms                                                      | 478 ms: 1.24x faster                                                              |
| sqlglot_transpile        | 1.48 ms                                                     | 1.20 ms: 1.23x faster                                                             |
| unpickle_pure_python     | 183 us                                                      | 149 us: 1.23x faster                                                              |
| raytrace                 | 273 ms                                                      | 225 ms: 1.22x faster                                                              |
| richards                 | 42.4 ms                                                     | 35.0 ms: 1.21x faster                                                             |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                             |
| xml_etree_process        | 44.5 ms                                                     | 37.1 ms: 1.20x faster                                                             |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.31 ms: 1.18x faster                                                             |
| bench_thread_pool        | 958 us                                                      | 821 us: 1.17x faster                                                              |
| thrift                   | 617 us                                                      | 530 us: 1.16x faster                                                              |
| mdp                      | 1.78 sec                                                    | 1.53 sec: 1.16x faster                                                            |
| regex_compile            | 106 ms                                                      | 93.3 ms: 1.14x faster                                                             |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.14x faster                                                             |
| scimark_fft              | 187 ms                                                      | 166 ms: 1.13x faster                                                              |
| regex_dna                | 136 ms                                                      | 121 ms: 1.12x faster                                                              |
| deepcopy_reduce          | 2.20 us                                                     | 1.98 us: 1.11x faster                                                             |
| django_template          | 28.9 ms                                                     | 26.9 ms: 1.07x faster                                                             |
| json                     | 3.14 ms                                                     | 2.93 ms: 1.07x faster                                                             |
| xml_etree_generate       | 55.5 ms                                                     | 51.8 ms: 1.07x faster                                                             |
| fannkuch                 | 256 ms                                                      | 243 ms: 1.05x faster                                                              |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                             |
| hexiom                   | 5.74 ms                                                     | 5.53 ms: 1.04x faster                                                             |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.0 ms: 1.03x faster                                                             |
| xml_etree_parse          | 96.8 ms                                                     | 93.9 ms: 1.03x faster                                                             |
| sympy_sum                | 107 ms                                                      | 104 ms: 1.03x faster                                                              |
| logging_format           | 6.76 us                                                     | 6.68 us: 1.01x faster                                                             |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                              |
| docutils                 | 1.92 sec                                                    | 1.90 sec: 1.01x faster                                                            |
| pathlib                  | 75.7 ms                                                     | 75.2 ms: 1.01x faster                                                             |
| logging_simple           | 6.22 us                                                     | 6.25 us: 1.00x slower                                                             |
| nqueens                  | 66.6 ms                                                     | 67.0 ms: 1.01x slower                                                             |
| 2to3                     | 246 ms                                                      | 248 ms: 1.01x slower                                                              |
| sympy_str                | 194 ms                                                      | 196 ms: 1.01x slower                                                              |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                             |
| sqlglot_normalize        | 205 ms                                                      | 214 ms: 1.04x slower                                                              |
| sympy_integrate          | 15.3 ms                                                     | 16.0 ms: 1.05x slower                                                             |
| sympy_expand             | 314 ms                                                      | 331 ms: 1.05x slower                                                              |
| sqlglot_optimize         | 39.8 ms                                                     | 43.6 ms: 1.10x slower                                                             |
| genshi_xml               | 41.0 ms                                                     | 46.4 ms: 1.13x slower                                                             |
| python_startup           | 20.6 ms                                                     | 23.5 ms: 1.14x slower                                                             |
| python_startup_no_site   | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                             |
| telco                    | 3.94 ms                                                     | 4.62 ms: 1.17x slower                                                             |
| async_generators         | 222 ms                                                      | 263 ms: 1.19x slower                                                              |
| coverage                 | 39.0 ms                                                     | 46.5 ms: 1.19x slower                                                             |
| gc_traversal             | 1.41 ms                                                     | 1.92 ms: 1.36x slower                                                             |
| bench_mp_pool            | 62.0 ms                                                     | 87.6 ms: 1.41x slower                                                             |
| create_gc_cycles         | 800 us                                                      | 1.36 ms: 1.70x slower                                                             |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                                      |

Benchmark hidden because not significant (3): genshi_text, regex_v8, meteor_contest
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241114-3.14.0a1+-b1f0a4e-JIT/bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.181x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown
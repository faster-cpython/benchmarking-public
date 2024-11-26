# Results vs. 3.10.4

- fork: eendebakpt
- ref: int_freelist
- machine: windows-amd64
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.161x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 225 ms: 1.09x faster                                                    |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                  |
| html5lib       | 51.0 ms                                                     | 40.3 ms: 1.27x faster                                                   |
| Geometric mean | (ref)                                                       | 1.16x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 221 ms: 1.97x faster                                                    |
| async_tree_io           | 1.11 sec                                                    | 563 ms: 1.97x faster                                                    |
| async_tree_memoization  | 526 ms                                                      | 278 ms: 1.89x faster                                                    |
| async_tree_cpu_io_mixed | 638 ms                                                      | 386 ms: 1.65x faster                                                    |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.2 ms: 1.10x faster                                                   |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                    |
| nbody          | 71.3 ms                                                     | 78.8 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                       | 1.00x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 115 ms: 1.18x faster                                                    |
| regex_compile  | 106 ms                                                      | 91.6 ms: 1.16x faster                                                   |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                   |
| regex_v8       | 15.4 ms                                                     | 14.9 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                       | 1.11x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.78 ms: 1.35x faster                                                   |
| pickle_pure_python   | 270 us                                                      | 231 us: 1.17x faster                                                    |
| unpickle_pure_python | 183 us                                                      | 157 us: 1.16x faster                                                    |
| xml_etree_process    | 44.5 ms                                                     | 41.0 ms: 1.08x faster                                                   |
| tomli_loads          | 1.67 sec                                                    | 1.55 sec: 1.08x faster                                                  |
| xml_etree_parse      | 96.8 ms                                                     | 94.0 ms: 1.03x faster                                                   |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.0 ms: 1.02x slower                                                   |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                   |
| xml_etree_generate   | 55.5 ms                                                     | 58.3 ms: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.2 ms: 1.11x slower                                                   |
| python_startup         | 20.6 ms                                                     | 23.2 ms: 1.13x slower                                                   |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.04 ms: 1.28x faster                                                   |
| genshi_text     | 19.8 ms                                                     | 17.0 ms: 1.16x faster                                                   |
| django_template | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                   |
| genshi_xml      | 41.0 ms                                                     | 36.7 ms: 1.12x faster                                                   |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 116 us: 2.89x faster                                                    |
| async_tree_none          | 435 ms                                                      | 221 ms: 1.97x faster                                                    |
| async_tree_io            | 1.11 sec                                                    | 563 ms: 1.97x faster                                                    |
| async_tree_memoization   | 526 ms                                                      | 278 ms: 1.89x faster                                                    |
| deltablue                | 4.19 ms                                                     | 2.35 ms: 1.78x faster                                                   |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 386 ms: 1.65x faster                                                    |
| pylint                   | 350 ms                                                      | 225 ms: 1.56x faster                                                    |
| go                       | 139 ms                                                      | 90.5 ms: 1.54x faster                                                   |
| generators               | 32.4 ms                                                     | 22.4 ms: 1.44x faster                                                   |
| logging_silent           | 94.6 ns                                                     | 65.7 ns: 1.44x faster                                                   |
| richards_super           | 52.2 ms                                                     | 36.5 ms: 1.43x faster                                                   |
| chaos                    | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                                   |
| raytrace                 | 273 ms                                                      | 198 ms: 1.38x faster                                                    |
| json_dumps               | 9.16 ms                                                     | 6.78 ms: 1.35x faster                                                   |
| comprehensions           | 16.5 us                                                     | 12.4 us: 1.33x faster                                                   |
| sqlglot_parse            | 1.22 ms                                                     | 918 us: 1.32x faster                                                    |
| deepcopy                 | 255 us                                                      | 195 us: 1.31x faster                                                    |
| deepcopy_memo            | 28.8 us                                                     | 22.0 us: 1.31x faster                                                   |
| richards                 | 42.4 ms                                                     | 32.7 ms: 1.30x faster                                                   |
| sqlglot_transpile        | 1.48 ms                                                     | 1.14 ms: 1.30x faster                                                   |
| scimark_lu               | 85.8 ms                                                     | 66.3 ms: 1.29x faster                                                   |
| pyflate                  | 409 ms                                                      | 319 ms: 1.28x faster                                                    |
| mako                     | 9.03 ms                                                     | 7.04 ms: 1.28x faster                                                   |
| crypto_pyaes             | 62.5 ms                                                     | 49.1 ms: 1.27x faster                                                   |
| html5lib                 | 51.0 ms                                                     | 40.3 ms: 1.27x faster                                                   |
| pycparser                | 930 ms                                                      | 738 ms: 1.26x faster                                                    |
| hexiom                   | 5.74 ms                                                     | 4.61 ms: 1.25x faster                                                   |
| mdp                      | 1.78 sec                                                    | 1.46 sec: 1.22x faster                                                  |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.20x faster                                                   |
| sympy_sum                | 107 ms                                                      | 90.2 ms: 1.19x faster                                                   |
| thrift                   | 617 us                                                      | 523 us: 1.18x faster                                                    |
| regex_dna                | 136 ms                                                      | 115 ms: 1.18x faster                                                    |
| dulwich_log              | 50.5 ms                                                     | 43.1 ms: 1.17x faster                                                   |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.0 ms: 1.17x faster                                                   |
| pickle_pure_python       | 270 us                                                      | 231 us: 1.17x faster                                                    |
| bench_thread_pool        | 958 us                                                      | 820 us: 1.17x faster                                                    |
| spectral_norm            | 77.3 ms                                                     | 66.2 ms: 1.17x faster                                                   |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.17x faster                                                   |
| unpickle_pure_python     | 183 us                                                      | 157 us: 1.16x faster                                                    |
| genshi_text              | 19.8 ms                                                     | 17.0 ms: 1.16x faster                                                   |
| scimark_sor              | 106 ms                                                      | 91.6 ms: 1.16x faster                                                   |
| regex_compile            | 106 ms                                                      | 91.6 ms: 1.16x faster                                                   |
| django_template          | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                   |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                   |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                  |
| genshi_xml               | 41.0 ms                                                     | 36.7 ms: 1.12x faster                                                   |
| float                    | 61.7 ms                                                     | 56.2 ms: 1.10x faster                                                   |
| 2to3                     | 246 ms                                                      | 225 ms: 1.09x faster                                                    |
| sympy_str                | 194 ms                                                      | 179 ms: 1.08x faster                                                    |
| deepcopy_reduce          | 2.20 us                                                     | 2.03 us: 1.08x faster                                                   |
| xml_etree_process        | 44.5 ms                                                     | 41.0 ms: 1.08x faster                                                   |
| tomli_loads              | 1.67 sec                                                    | 1.55 sec: 1.08x faster                                                  |
| sqlglot_optimize         | 39.8 ms                                                     | 37.4 ms: 1.07x faster                                                   |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                   |
| pprint_pformat           | 1.22 sec                                                    | 1.15 sec: 1.06x faster                                                  |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.60 ms: 1.05x faster                                                   |
| pprint_safe_repr         | 592 ms                                                      | 572 ms: 1.04x faster                                                    |
| regex_v8                 | 15.4 ms                                                     | 14.9 ms: 1.03x faster                                                   |
| xml_etree_parse          | 96.8 ms                                                     | 94.0 ms: 1.03x faster                                                   |
| sqlglot_normalize        | 205 ms                                                      | 199 ms: 1.03x faster                                                    |
| nqueens                  | 66.6 ms                                                     | 65.1 ms: 1.02x faster                                                   |
| json                     | 3.14 ms                                                     | 3.09 ms: 1.02x faster                                                   |
| sympy_expand             | 314 ms                                                      | 311 ms: 1.01x faster                                                    |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                    |
| pathlib                  | 75.7 ms                                                     | 76.1 ms: 1.01x slower                                                   |
| logging_format           | 6.76 us                                                     | 6.85 us: 1.01x slower                                                   |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.0 ms: 1.02x slower                                                   |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                   |
| logging_simple           | 6.22 us                                                     | 6.42 us: 1.03x slower                                                   |
| meteor_contest           | 75.9 ms                                                     | 78.9 ms: 1.04x slower                                                   |
| scimark_fft              | 187 ms                                                      | 197 ms: 1.05x slower                                                    |
| xml_etree_generate       | 55.5 ms                                                     | 58.3 ms: 1.05x slower                                                   |
| fannkuch                 | 256 ms                                                      | 279 ms: 1.09x slower                                                    |
| async_generators         | 222 ms                                                      | 245 ms: 1.11x slower                                                    |
| nbody                    | 71.3 ms                                                     | 78.8 ms: 1.11x slower                                                   |
| python_startup_no_site   | 15.5 ms                                                     | 17.2 ms: 1.11x slower                                                   |
| python_startup           | 20.6 ms                                                     | 23.2 ms: 1.13x slower                                                   |
| coverage                 | 39.0 ms                                                     | 47.4 ms: 1.21x slower                                                   |
| telco                    | 3.94 ms                                                     | 4.85 ms: 1.23x slower                                                   |
| bench_mp_pool            | 62.0 ms                                                     | 81.8 ms: 1.32x slower                                                   |
| gc_traversal             | 1.41 ms                                                     | 1.92 ms: 1.36x slower                                                   |
| create_gc_cycles         | 800 us                                                      | 1.37 ms: 1.72x slower                                                   |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                            |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241121-3.14.0a1+-d1e4aa2/bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.161x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown
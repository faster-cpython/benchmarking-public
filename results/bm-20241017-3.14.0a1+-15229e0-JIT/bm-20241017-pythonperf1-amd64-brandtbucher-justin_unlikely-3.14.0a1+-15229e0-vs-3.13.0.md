# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_unlikely
- machine: windows-amd64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.012x slower
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 251 ms: 1.14x slower                                                         |
| docutils       | 1.57 sec                                                    | 1.93 sec: 1.23x slower                                                       |
| html5lib       | 38.9 ms                                                     | 39.9 ms: 1.03x slower                                                        |
| sphinx         | 633 ms                                                      | 772 ms: 1.22x slower                                                         |
| tornado_http   | 93.0 ms                                                     | 101 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                       | 1.14x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 264 ms: 1.09x faster                                                         |
| async_tree_none            | 226 ms                                                      | 220 ms: 1.03x faster                                                         |
| async_tree_io              | 521 ms                                                      | 557 ms: 1.07x slower                                                         |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 406 ms: 1.08x slower                                                         |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.10x slower                                                        |
| async_generators           | 223 ms                                                      | 269 ms: 1.20x slower                                                         |
| async_tree_io_tg           | 518 ms                                                      | 637 ms: 1.23x slower                                                         |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                                 |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 51.8 ms: 1.32x faster                                                        |
| float          | 49.9 ms                                                     | 46.7 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.7 ms: 1.45x faster                                                        |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                         |
| regex_effbot   | 1.58 ms                                                     | 1.60 ms: 1.02x slower                                                        |
| regex_compile  | 80.5 ms                                                     | 92.5 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 54.0 ms                                                     | 51.0 ms: 1.06x faster                                                        |
| tomli_loads          | 1.39 sec                                                    | 1.32 sec: 1.06x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                        |
| xml_etree_process    | 37.0 ms                                                     | 36.4 ms: 1.02x faster                                                        |
| xml_etree_parse      | 93.6 ms                                                     | 95.3 ms: 1.02x slower                                                        |
| xml_etree_iterparse  | 61.8 ms                                                     | 63.5 ms: 1.03x slower                                                        |
| json_dumps           | 5.92 ms                                                     | 6.24 ms: 1.05x slower                                                        |
| pickle_pure_python   | 190 us                                                      | 202 us: 1.07x slower                                                         |
| unpickle_pure_python | 133 us                                                      | 147 us: 1.10x slower                                                         |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 24.3 ms: 1.05x faster                                                        |
| python_startup_no_site | 18.1 ms                                                     | 18.4 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.02 ms: 1.27x faster                                                        |
| django_template | 22.4 ms                                                     | 27.0 ms: 1.21x slower                                                        |
| genshi_text     | 15.6 ms                                                     | 19.5 ms: 1.25x slower                                                        |
| genshi_xml      | 35.5 ms                                                     | 46.9 ms: 1.32x slower                                                        |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 526 us: 16.71x faster                                                        |
| regex_v8                   | 21.4 ms                                                     | 14.7 ms: 1.45x faster                                                        |
| deepcopy_memo              | 23.3 us                                                     | 17.1 us: 1.37x faster                                                        |
| nbody                      | 68.4 ms                                                     | 51.8 ms: 1.32x faster                                                        |
| mako                       | 6.35 ms                                                     | 5.02 ms: 1.27x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 62.8 ms: 1.21x faster                                                        |
| spectral_norm              | 62.8 ms                                                     | 53.2 ms: 1.18x faster                                                        |
| deepcopy                   | 226 us                                                      | 192 us: 1.18x faster                                                         |
| crypto_pyaes               | 45.4 ms                                                     | 39.9 ms: 1.14x faster                                                        |
| pprint_safe_repr           | 494 ms                                                      | 449 ms: 1.10x faster                                                         |
| scimark_fft                | 172 ms                                                      | 157 ms: 1.10x faster                                                         |
| async_tree_memoization_tg  | 288 ms                                                      | 264 ms: 1.09x faster                                                         |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.26 ms: 1.09x faster                                                        |
| telco                      | 4.79 ms                                                     | 4.42 ms: 1.08x faster                                                        |
| deepcopy_reduce            | 2.06 us                                                     | 1.90 us: 1.08x faster                                                        |
| pprint_pformat             | 999 ms                                                      | 924 ms: 1.08x faster                                                         |
| fannkuch                   | 253 ms                                                      | 234 ms: 1.08x faster                                                         |
| scimark_monte_carlo        | 40.8 ms                                                     | 37.8 ms: 1.08x faster                                                        |
| float                      | 49.9 ms                                                     | 46.7 ms: 1.07x faster                                                        |
| json                       | 3.19 ms                                                     | 3.00 ms: 1.06x faster                                                        |
| xml_etree_generate         | 54.0 ms                                                     | 51.0 ms: 1.06x faster                                                        |
| tomli_loads                | 1.39 sec                                                    | 1.32 sec: 1.06x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                        |
| python_startup             | 25.4 ms                                                     | 24.3 ms: 1.05x faster                                                        |
| async_tree_none            | 226 ms                                                      | 220 ms: 1.03x faster                                                         |
| xml_etree_process          | 37.0 ms                                                     | 36.4 ms: 1.02x faster                                                        |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                         |
| python_startup_no_site     | 18.1 ms                                                     | 18.4 ms: 1.02x slower                                                        |
| dulwich_log                | 40.8 ms                                                     | 41.5 ms: 1.02x slower                                                        |
| xml_etree_parse            | 93.6 ms                                                     | 95.3 ms: 1.02x slower                                                        |
| regex_effbot               | 1.58 ms                                                     | 1.60 ms: 1.02x slower                                                        |
| pyflate                    | 283 ms                                                      | 289 ms: 1.02x slower                                                         |
| meteor_contest             | 73.5 ms                                                     | 75.2 ms: 1.02x slower                                                        |
| html5lib                   | 38.9 ms                                                     | 39.9 ms: 1.03x slower                                                        |
| xml_etree_iterparse        | 61.8 ms                                                     | 63.5 ms: 1.03x slower                                                        |
| coverage                   | 45.6 ms                                                     | 47.1 ms: 1.03x slower                                                        |
| bench_mp_pool              | 86.4 ms                                                     | 89.3 ms: 1.03x slower                                                        |
| logging_simple             | 5.96 us                                                     | 6.18 us: 1.04x slower                                                        |
| scimark_lu                 | 53.0 ms                                                     | 55.0 ms: 1.04x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 57.4 ns: 1.05x slower                                                        |
| json_dumps                 | 5.92 ms                                                     | 6.24 ms: 1.05x slower                                                        |
| logging_format             | 6.26 us                                                     | 6.66 us: 1.06x slower                                                        |
| pickle_pure_python         | 190 us                                                      | 202 us: 1.07x slower                                                         |
| async_tree_io              | 521 ms                                                      | 557 ms: 1.07x slower                                                         |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 406 ms: 1.08x slower                                                         |
| chaos                      | 38.5 ms                                                     | 41.5 ms: 1.08x slower                                                        |
| tornado_http               | 93.0 ms                                                     | 101 ms: 1.08x slower                                                         |
| pycparser                  | 683 ms                                                      | 745 ms: 1.09x slower                                                         |
| go                         | 87.0 ms                                                     | 95.4 ms: 1.10x slower                                                        |
| typing_runtime_protocols   | 105 us                                                      | 116 us: 1.10x slower                                                         |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.10x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 147 us: 1.10x slower                                                         |
| mdp                        | 1.39 sec                                                    | 1.55 sec: 1.12x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 63.5 ms: 1.12x slower                                                        |
| create_gc_cycles           | 1.26 ms                                                     | 1.42 ms: 1.12x slower                                                        |
| comprehensions             | 10.3 us                                                     | 11.6 us: 1.13x slower                                                        |
| sympy_expand               | 291 ms                                                      | 331 ms: 1.13x slower                                                         |
| 2to3                       | 221 ms                                                      | 251 ms: 1.14x slower                                                         |
| regex_compile              | 80.5 ms                                                     | 92.5 ms: 1.15x slower                                                        |
| sympy_str                  | 169 ms                                                      | 196 ms: 1.16x slower                                                         |
| generators                 | 19.5 ms                                                     | 22.9 ms: 1.18x slower                                                        |
| sympy_sum                  | 86.9 ms                                                     | 102 ms: 1.18x slower                                                         |
| sqlglot_parse              | 771 us                                                      | 915 us: 1.19x slower                                                         |
| sqlglot_normalize          | 175 ms                                                      | 209 ms: 1.20x slower                                                         |
| async_generators           | 223 ms                                                      | 269 ms: 1.20x slower                                                         |
| django_template            | 22.4 ms                                                     | 27.0 ms: 1.21x slower                                                        |
| sphinx                     | 633 ms                                                      | 772 ms: 1.22x slower                                                         |
| docutils                   | 1.57 sec                                                    | 1.93 sec: 1.23x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 637 ms: 1.23x slower                                                         |
| deltablue                  | 1.92 ms                                                     | 2.37 ms: 1.23x slower                                                        |
| genshi_text                | 15.6 ms                                                     | 19.5 ms: 1.25x slower                                                        |
| richards                   | 27.3 ms                                                     | 34.5 ms: 1.26x slower                                                        |
| richards_super             | 30.9 ms                                                     | 39.1 ms: 1.27x slower                                                        |
| sqlglot_transpile          | 956 us                                                      | 1.21 ms: 1.27x slower                                                        |
| sympy_integrate            | 12.5 ms                                                     | 15.9 ms: 1.27x slower                                                        |
| sqlglot_optimize           | 32.9 ms                                                     | 43.2 ms: 1.31x slower                                                        |
| genshi_xml                 | 35.5 ms                                                     | 46.9 ms: 1.32x slower                                                        |
| raytrace                   | 160 ms                                                      | 214 ms: 1.34x slower                                                         |
| pylint                     | 211 ms                                                      | 283 ms: 1.34x slower                                                         |
| hexiom                     | 3.89 ms                                                     | 5.25 ms: 1.35x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                 |

Benchmark hidden because not significant (7): bench_thread_pool, gc_traversal, pidigits, pathlib, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.012x slower
# HPT report

- Reliability score: 99.75% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
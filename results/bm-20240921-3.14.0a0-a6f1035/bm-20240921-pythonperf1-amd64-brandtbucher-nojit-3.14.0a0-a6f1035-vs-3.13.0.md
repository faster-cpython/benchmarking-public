# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: windows-amd64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.024x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 226 ms: 1.02x slower                                              |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                            |
| html5lib       | 38.9 ms                                                     | 40.9 ms: 1.05x slower                                             |
| tornado_http   | 93.0 ms                                                     | 84.2 ms: 1.11x faster                                             |
| Geometric mean | (ref)                                                       | 1.01x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.15x faster                                              |
| async_tree_none            | 226 ms                                                      | 209 ms: 1.08x faster                                              |
| async_tree_memoization     | 276 ms                                                      | 260 ms: 1.06x faster                                              |
| async_tree_none_tg         | 209 ms                                                      | 199 ms: 1.05x faster                                              |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 398 ms: 1.06x slower                                              |
| coroutines                 | 12.8 ms                                                     | 13.8 ms: 1.08x slower                                             |
| async_tree_io_tg           | 518 ms                                                      | 562 ms: 1.08x slower                                              |
| async_tree_io              | 521 ms                                                      | 570 ms: 1.09x slower                                              |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                              |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                      |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                              |
| float          | 49.9 ms                                                     | 55.3 ms: 1.11x slower                                             |
| nbody          | 68.4 ms                                                     | 83.8 ms: 1.22x slower                                             |
| Geometric mean | (ref)                                                       | 1.11x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.3 ms: 1.40x faster                                             |
| regex_effbot   | 1.58 ms                                                     | 1.59 ms: 1.01x slower                                             |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                              |
| regex_compile  | 80.5 ms                                                     | 93.1 ms: 1.16x slower                                             |
| Geometric mean | (ref)                                                       | 1.03x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.2 us: 1.07x faster                                             |
| xml_etree_parse      | 93.6 ms                                                     | 94.3 ms: 1.01x slower                                             |
| xml_etree_iterparse  | 61.8 ms                                                     | 65.2 ms: 1.05x slower                                             |
| json_dumps           | 5.92 ms                                                     | 6.26 ms: 1.06x slower                                             |
| xml_etree_generate   | 54.0 ms                                                     | 58.6 ms: 1.09x slower                                             |
| xml_etree_process    | 37.0 ms                                                     | 40.9 ms: 1.11x slower                                             |
| pickle_pure_python   | 190 us                                                      | 215 us: 1.13x slower                                              |
| unpickle_pure_python | 133 us                                                      | 153 us: 1.15x slower                                              |
| tomli_loads          | 1.39 sec                                                    | 1.61 sec: 1.15x slower                                            |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 21.9 ms: 1.16x faster                                             |
| Geometric mean | (ref)                                                       | 1.08x faster                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 6.85 ms: 1.08x slower                                             |
| genshi_text     | 15.6 ms                                                     | 16.9 ms: 1.09x slower                                             |
| django_template | 22.4 ms                                                     | 25.9 ms: 1.16x slower                                             |
| Geometric mean  | (ref)                                                       | 1.08x slower                                                      |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 512 us: 17.17x faster                                             |
| create_gc_cycles           | 1.26 ms                                                     | 882 us: 1.43x faster                                              |
| regex_v8                   | 21.4 ms                                                     | 15.3 ms: 1.40x faster                                             |
| bench_mp_pool              | 86.4 ms                                                     | 66.6 ms: 1.30x faster                                             |
| gc_traversal               | 1.97 ms                                                     | 1.53 ms: 1.29x faster                                             |
| deepcopy                   | 226 us                                                      | 191 us: 1.19x faster                                              |
| python_startup             | 25.4 ms                                                     | 21.9 ms: 1.16x faster                                             |
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.15x faster                                              |
| deepcopy_memo              | 23.3 us                                                     | 20.6 us: 1.13x faster                                             |
| tornado_http               | 93.0 ms                                                     | 84.2 ms: 1.11x faster                                             |
| async_tree_none            | 226 ms                                                      | 209 ms: 1.08x faster                                              |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.07x faster                                             |
| pathlib                    | 80.9 ms                                                     | 75.7 ms: 1.07x faster                                             |
| deepcopy_reduce            | 2.06 us                                                     | 1.94 us: 1.06x faster                                             |
| async_tree_memoization     | 276 ms                                                      | 260 ms: 1.06x faster                                              |
| bench_thread_pool          | 847 us                                                      | 805 us: 1.05x faster                                              |
| async_tree_none_tg         | 209 ms                                                      | 199 ms: 1.05x faster                                              |
| regex_effbot               | 1.58 ms                                                     | 1.59 ms: 1.01x slower                                             |
| xml_etree_parse            | 93.6 ms                                                     | 94.3 ms: 1.01x slower                                             |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                              |
| go                         | 87.0 ms                                                     | 88.9 ms: 1.02x slower                                             |
| 2to3                       | 221 ms                                                      | 226 ms: 1.02x slower                                              |
| sympy_sum                  | 86.9 ms                                                     | 90.6 ms: 1.04x slower                                             |
| sympy_expand               | 291 ms                                                      | 305 ms: 1.05x slower                                              |
| html5lib                   | 38.9 ms                                                     | 40.9 ms: 1.05x slower                                             |
| typing_runtime_protocols   | 105 us                                                      | 111 us: 1.05x slower                                              |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                              |
| crypto_pyaes               | 45.4 ms                                                     | 47.9 ms: 1.05x slower                                             |
| sympy_str                  | 169 ms                                                      | 178 ms: 1.05x slower                                              |
| xml_etree_iterparse        | 61.8 ms                                                     | 65.2 ms: 1.05x slower                                             |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 398 ms: 1.06x slower                                              |
| json_dumps                 | 5.92 ms                                                     | 6.26 ms: 1.06x slower                                             |
| sympy_integrate            | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                             |
| dulwich_log                | 40.8 ms                                                     | 43.4 ms: 1.06x slower                                             |
| coverage                   | 45.6 ms                                                     | 48.5 ms: 1.06x slower                                             |
| meteor_contest             | 73.5 ms                                                     | 78.9 ms: 1.07x slower                                             |
| mako                       | 6.35 ms                                                     | 6.85 ms: 1.08x slower                                             |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                            |
| coroutines                 | 12.8 ms                                                     | 13.8 ms: 1.08x slower                                             |
| async_tree_io_tg           | 518 ms                                                      | 562 ms: 1.08x slower                                              |
| telco                      | 4.79 ms                                                     | 5.20 ms: 1.08x slower                                             |
| xml_etree_generate         | 54.0 ms                                                     | 58.6 ms: 1.09x slower                                             |
| mdp                        | 1.39 sec                                                    | 1.51 sec: 1.09x slower                                            |
| genshi_text                | 15.6 ms                                                     | 16.9 ms: 1.09x slower                                             |
| generators                 | 19.5 ms                                                     | 21.3 ms: 1.09x slower                                             |
| async_tree_io              | 521 ms                                                      | 570 ms: 1.09x slower                                              |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                              |
| xml_etree_process          | 37.0 ms                                                     | 40.9 ms: 1.11x slower                                             |
| float                      | 49.9 ms                                                     | 55.3 ms: 1.11x slower                                             |
| spectral_norm              | 62.8 ms                                                     | 69.9 ms: 1.11x slower                                             |
| pprint_safe_repr           | 494 ms                                                      | 551 ms: 1.12x slower                                              |
| sqlglot_optimize           | 32.9 ms                                                     | 36.8 ms: 1.12x slower                                             |
| logging_simple             | 5.96 us                                                     | 6.68 us: 1.12x slower                                             |
| pycparser                  | 683 ms                                                      | 770 ms: 1.13x slower                                              |
| sqlglot_normalize          | 175 ms                                                      | 197 ms: 1.13x slower                                              |
| logging_format             | 6.26 us                                                     | 7.08 us: 1.13x slower                                             |
| pprint_pformat             | 999 ms                                                      | 1.13 sec: 1.13x slower                                            |
| pickle_pure_python         | 190 us                                                      | 215 us: 1.13x slower                                              |
| pyflate                    | 283 ms                                                      | 324 ms: 1.14x slower                                              |
| unpickle_pure_python       | 133 us                                                      | 153 us: 1.15x slower                                              |
| tomli_loads                | 1.39 sec                                                    | 1.61 sec: 1.15x slower                                            |
| regex_compile              | 80.5 ms                                                     | 93.1 ms: 1.16x slower                                             |
| django_template            | 22.4 ms                                                     | 25.9 ms: 1.16x slower                                             |
| logging_silent             | 54.6 ns                                                     | 63.5 ns: 1.16x slower                                             |
| nqueens                    | 56.7 ms                                                     | 65.9 ms: 1.16x slower                                             |
| chaos                      | 38.5 ms                                                     | 44.9 ms: 1.16x slower                                             |
| comprehensions             | 10.3 us                                                     | 12.0 us: 1.17x slower                                             |
| sqlglot_parse              | 771 us                                                      | 902 us: 1.17x slower                                              |
| sqlglot_transpile          | 956 us                                                      | 1.12 ms: 1.17x slower                                             |
| hexiom                     | 3.89 ms                                                     | 4.62 ms: 1.19x slower                                             |
| scimark_sor                | 76.2 ms                                                     | 90.7 ms: 1.19x slower                                             |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.93 ms: 1.19x slower                                             |
| richards_super             | 30.9 ms                                                     | 36.9 ms: 1.19x slower                                             |
| richards                   | 27.3 ms                                                     | 33.0 ms: 1.21x slower                                             |
| deltablue                  | 1.92 ms                                                     | 2.32 ms: 1.21x slower                                             |
| fannkuch                   | 253 ms                                                      | 308 ms: 1.22x slower                                              |
| nbody                      | 68.4 ms                                                     | 83.8 ms: 1.22x slower                                             |
| raytrace                   | 160 ms                                                      | 197 ms: 1.23x slower                                              |
| scimark_fft                | 172 ms                                                      | 212 ms: 1.23x slower                                              |
| scimark_lu                 | 53.0 ms                                                     | 65.7 ms: 1.24x slower                                             |
| scimark_monte_carlo        | 40.8 ms                                                     | 51.4 ms: 1.26x slower                                             |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                      |

Benchmark hidden because not significant (5): json, python_startup_no_site, async_tree_cpu_io_mixed, genshi_xml, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.024x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown
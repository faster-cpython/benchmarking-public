# Results vs. 3.13.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: windows-amd64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.036x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 227 ms: 1.03x slower                                                        |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                      |
| html5lib       | 38.9 ms                                                     | 40.3 ms: 1.03x slower                                                       |
| sphinx         | 633 ms                                                      | 668 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 261 ms: 1.11x faster                                                        |
| asyncio_websockets         | 318 ms                                                      | 305 ms: 1.04x faster                                                        |
| async_tree_none            | 226 ms                                                      | 220 ms: 1.03x faster                                                        |
| async_tree_none_tg         | 209 ms                                                      | 212 ms: 1.02x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 13.6 ms: 1.06x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 402 ms: 1.07x slower                                                        |
| async_tree_io              | 521 ms                                                      | 564 ms: 1.08x slower                                                        |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 635 ms: 1.23x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 49.9 ms                                                     | 56.0 ms: 1.12x slower                                                       |
| nbody          | 68.4 ms                                                     | 79.6 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.5 ms: 1.38x faster                                                       |
| regex_effbot   | 1.58 ms                                                     | 1.62 ms: 1.03x slower                                                       |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| regex_compile  | 80.5 ms                                                     | 91.5 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.5 us: 1.05x faster                                                       |
| xml_etree_iterparse  | 61.8 ms                                                     | 65.3 ms: 1.06x slower                                                       |
| xml_etree_generate   | 54.0 ms                                                     | 57.4 ms: 1.06x slower                                                       |
| xml_etree_process    | 37.0 ms                                                     | 40.5 ms: 1.10x slower                                                       |
| json_dumps           | 5.92 ms                                                     | 6.67 ms: 1.13x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 153 us: 1.15x slower                                                        |
| tomli_loads          | 1.39 sec                                                    | 1.60 sec: 1.15x slower                                                      |
| pickle_pure_python   | 190 us                                                      | 229 us: 1.21x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 24.3 ms: 1.04x faster                                                       |
| python_startup_no_site | 18.1 ms                                                     | 17.6 ms: 1.03x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 15.6 ms                                                     | 16.9 ms: 1.08x slower                                                       |
| mako            | 6.35 ms                                                     | 6.93 ms: 1.09x slower                                                       |
| django_template | 22.4 ms                                                     | 25.5 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 530 us: 16.59x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 15.5 ms: 1.38x faster                                                       |
| deepcopy                   | 226 us                                                      | 196 us: 1.15x faster                                                        |
| async_tree_memoization_tg  | 288 ms                                                      | 261 ms: 1.11x faster                                                        |
| deepcopy_memo              | 23.3 us                                                     | 21.2 us: 1.10x faster                                                       |
| json                       | 3.19 ms                                                     | 2.92 ms: 1.09x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.05x faster                                                       |
| python_startup             | 25.4 ms                                                     | 24.3 ms: 1.04x faster                                                       |
| bench_mp_pool              | 86.4 ms                                                     | 83.0 ms: 1.04x faster                                                       |
| bench_thread_pool          | 847 us                                                      | 813 us: 1.04x faster                                                        |
| asyncio_websockets         | 318 ms                                                      | 305 ms: 1.04x faster                                                        |
| python_startup_no_site     | 18.1 ms                                                     | 17.6 ms: 1.03x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 2.00 us: 1.03x faster                                                       |
| async_tree_none            | 226 ms                                                      | 220 ms: 1.03x faster                                                        |
| pathlib                    | 80.9 ms                                                     | 79.1 ms: 1.02x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.93 ms: 1.02x faster                                                       |
| connected_components       | 332 ms                                                      | 329 ms: 1.01x faster                                                        |
| telco                      | 4.79 ms                                                     | 4.81 ms: 1.00x slower                                                       |
| async_tree_none_tg         | 209 ms                                                      | 212 ms: 1.02x slower                                                        |
| regex_effbot               | 1.58 ms                                                     | 1.62 ms: 1.03x slower                                                       |
| 2to3                       | 221 ms                                                      | 227 ms: 1.03x slower                                                        |
| html5lib                   | 38.9 ms                                                     | 40.3 ms: 1.03x slower                                                       |
| coverage                   | 45.6 ms                                                     | 47.2 ms: 1.04x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 90.3 ms: 1.04x slower                                                       |
| go                         | 87.0 ms                                                     | 90.5 ms: 1.04x slower                                                       |
| mdp                        | 1.39 sec                                                    | 1.45 sec: 1.05x slower                                                      |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| sympy_expand               | 291 ms                                                      | 307 ms: 1.05x slower                                                        |
| sphinx                     | 633 ms                                                      | 668 ms: 1.06x slower                                                        |
| crypto_pyaes               | 45.4 ms                                                     | 48.0 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 65.3 ms: 1.06x slower                                                       |
| sympy_str                  | 169 ms                                                      | 179 ms: 1.06x slower                                                        |
| meteor_contest             | 73.5 ms                                                     | 78.0 ms: 1.06x slower                                                       |
| xml_etree_generate         | 54.0 ms                                                     | 57.4 ms: 1.06x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 13.6 ms: 1.06x slower                                                       |
| dulwich_log                | 40.8 ms                                                     | 43.4 ms: 1.06x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 402 ms: 1.07x slower                                                        |
| typing_runtime_protocols   | 105 us                                                      | 113 us: 1.07x slower                                                        |
| bpe_tokeniser              | 2.91 sec                                                    | 3.11 sec: 1.07x slower                                                      |
| logging_simple             | 5.96 us                                                     | 6.39 us: 1.07x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 13.4 ms: 1.08x slower                                                       |
| spectral_norm              | 62.8 ms                                                     | 67.8 ms: 1.08x slower                                                       |
| pycparser                  | 683 ms                                                      | 738 ms: 1.08x slower                                                        |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                      |
| async_tree_io              | 521 ms                                                      | 564 ms: 1.08x slower                                                        |
| genshi_text                | 15.6 ms                                                     | 16.9 ms: 1.08x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.83 us: 1.09x slower                                                       |
| mako                       | 6.35 ms                                                     | 6.93 ms: 1.09x slower                                                       |
| xml_etree_process          | 37.0 ms                                                     | 40.5 ms: 1.10x slower                                                       |
| create_gc_cycles           | 1.26 ms                                                     | 1.38 ms: 1.10x slower                                                       |
| fannkuch                   | 253 ms                                                      | 280 ms: 1.10x slower                                                        |
| pprint_safe_repr           | 494 ms                                                      | 545 ms: 1.10x slower                                                        |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                        |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.73 ms: 1.11x slower                                                       |
| generators                 | 19.5 ms                                                     | 21.7 ms: 1.11x slower                                                       |
| float                      | 49.9 ms                                                     | 56.0 ms: 1.12x slower                                                       |
| pprint_pformat             | 999 ms                                                      | 1.12 sec: 1.12x slower                                                      |
| json_dumps                 | 5.92 ms                                                     | 6.67 ms: 1.13x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 37.2 ms: 1.13x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 198 ms: 1.13x slower                                                        |
| scimark_fft                | 172 ms                                                      | 196 ms: 1.14x slower                                                        |
| regex_compile              | 80.5 ms                                                     | 91.5 ms: 1.14x slower                                                       |
| pyflate                    | 283 ms                                                      | 322 ms: 1.14x slower                                                        |
| django_template            | 22.4 ms                                                     | 25.5 ms: 1.14x slower                                                       |
| scimark_lu                 | 53.0 ms                                                     | 60.6 ms: 1.14x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 65.0 ms: 1.15x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 153 us: 1.15x slower                                                        |
| tomli_loads                | 1.39 sec                                                    | 1.60 sec: 1.15x slower                                                      |
| hexiom                     | 3.89 ms                                                     | 4.49 ms: 1.15x slower                                                       |
| chaos                      | 38.5 ms                                                     | 44.8 ms: 1.16x slower                                                       |
| nbody                      | 68.4 ms                                                     | 79.6 ms: 1.16x slower                                                       |
| comprehensions             | 10.3 us                                                     | 12.0 us: 1.17x slower                                                       |
| scimark_monte_carlo        | 40.8 ms                                                     | 48.0 ms: 1.18x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 64.6 ns: 1.18x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.14 ms: 1.19x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 91.0 ms: 1.19x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 922 us: 1.20x slower                                                        |
| richards                   | 27.3 ms                                                     | 32.9 ms: 1.20x slower                                                       |
| richards_super             | 30.9 ms                                                     | 37.2 ms: 1.21x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 229 us: 1.21x slower                                                        |
| deltablue                  | 1.92 ms                                                     | 2.34 ms: 1.22x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 635 ms: 1.23x slower                                                        |
| raytrace                   | 160 ms                                                      | 200 ms: 1.25x slower                                                        |
| k_core                     | 1.74 sec                                                    | 2.53 sec: 1.45x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (7): genshi_xml, xml_etree_parse, pidigits, shortest_path, async_tree_cpu_io_mixed, async_tree_memoization, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: sqlite_synth

- Geometric mean (including insignificant results): 1.036x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown
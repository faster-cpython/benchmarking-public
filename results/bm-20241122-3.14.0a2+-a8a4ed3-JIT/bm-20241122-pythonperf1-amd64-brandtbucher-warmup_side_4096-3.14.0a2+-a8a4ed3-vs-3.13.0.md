# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_side_4096
- machine: windows-amd64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.018x faster
- HPT reliability: 95.94%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| docutils       | 1.57 sec                                                    | 1.75 sec: 1.11x slower                                                        |
| html5lib       | 38.9 ms                                                     | 39.6 ms: 1.02x slower                                                         |
| sphinx         | 633 ms                                                      | 687 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                  |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                                          |
| async_tree_none            | 226 ms                                                      | 214 ms: 1.06x faster                                                          |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 399 ms: 1.04x slower                                                          |
| coroutines                 | 12.8 ms                                                     | 13.6 ms: 1.07x slower                                                         |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 410 ms: 1.09x slower                                                          |
| async_tree_io              | 521 ms                                                      | 575 ms: 1.10x slower                                                          |
| async_tree_io_tg           | 518 ms                                                      | 579 ms: 1.12x slower                                                          |
| async_generators           | 223 ms                                                      | 270 ms: 1.21x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                  |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_memoization, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 56.4 ms: 1.21x faster                                                         |
| float          | 49.9 ms                                                     | 48.3 ms: 1.03x faster                                                         |
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.8 ms: 1.45x faster                                                         |
| regex_effbot   | 1.58 ms                                                     | 1.42 ms: 1.11x faster                                                         |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                          |
| regex_compile  | 80.5 ms                                                     | 82.2 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 111 us: 1.21x faster                                                          |
| json_loads           | 15.1 us                                                     | 14.0 us: 1.08x faster                                                         |
| tomli_loads          | 1.39 sec                                                    | 1.29 sec: 1.08x faster                                                        |
| xml_etree_generate   | 54.0 ms                                                     | 50.8 ms: 1.06x faster                                                         |
| xml_etree_process    | 37.0 ms                                                     | 35.7 ms: 1.04x faster                                                         |
| xml_etree_iterparse  | 61.8 ms                                                     | 62.3 ms: 1.01x slower                                                         |
| json_dumps           | 5.92 ms                                                     | 6.27 ms: 1.06x slower                                                         |
| pickle_pure_python   | 190 us                                                      | 208 us: 1.10x slower                                                          |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                  |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 23.7 ms: 1.07x faster                                                         |
| python_startup_no_site | 18.1 ms                                                     | 17.6 ms: 1.03x faster                                                         |
| Geometric mean         | (ref)                                                       | 1.05x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.17 ms: 1.23x faster                                                         |
| django_template | 22.4 ms                                                     | 27.6 ms: 1.23x slower                                                         |
| genshi_text     | 15.6 ms                                                     | 19.6 ms: 1.26x slower                                                         |
| genshi_xml      | 35.5 ms                                                     | 48.0 ms: 1.35x slower                                                         |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 543 us: 16.19x faster                                                         |
| regex_v8                   | 21.4 ms                                                     | 14.8 ms: 1.45x faster                                                         |
| deepcopy_memo              | 23.3 us                                                     | 16.8 us: 1.39x faster                                                         |
| mako                       | 6.35 ms                                                     | 5.17 ms: 1.23x faster                                                         |
| scimark_sor                | 76.2 ms                                                     | 62.1 ms: 1.23x faster                                                         |
| nbody                      | 68.4 ms                                                     | 56.4 ms: 1.21x faster                                                         |
| unpickle_pure_python       | 133 us                                                      | 111 us: 1.21x faster                                                          |
| spectral_norm              | 62.8 ms                                                     | 52.6 ms: 1.19x faster                                                         |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.08 ms: 1.18x faster                                                         |
| deepcopy                   | 226 us                                                      | 193 us: 1.17x faster                                                          |
| crypto_pyaes               | 45.4 ms                                                     | 39.9 ms: 1.14x faster                                                         |
| scimark_fft                | 172 ms                                                      | 153 ms: 1.12x faster                                                          |
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                                          |
| telco                      | 4.79 ms                                                     | 4.28 ms: 1.12x faster                                                         |
| regex_effbot               | 1.58 ms                                                     | 1.42 ms: 1.11x faster                                                         |
| deepcopy_reduce            | 2.06 us                                                     | 1.87 us: 1.10x faster                                                         |
| scimark_monte_carlo        | 40.8 ms                                                     | 37.1 ms: 1.10x faster                                                         |
| json                       | 3.19 ms                                                     | 2.91 ms: 1.09x faster                                                         |
| json_loads                 | 15.1 us                                                     | 14.0 us: 1.08x faster                                                         |
| bpe_tokeniser              | 2.91 sec                                                    | 2.69 sec: 1.08x faster                                                        |
| tomli_loads                | 1.39 sec                                                    | 1.29 sec: 1.08x faster                                                        |
| python_startup             | 25.4 ms                                                     | 23.7 ms: 1.07x faster                                                         |
| xml_etree_generate         | 54.0 ms                                                     | 50.8 ms: 1.06x faster                                                         |
| pathlib                    | 80.9 ms                                                     | 76.1 ms: 1.06x faster                                                         |
| pylint                     | 211 ms                                                      | 198 ms: 1.06x faster                                                          |
| connected_components       | 332 ms                                                      | 313 ms: 1.06x faster                                                          |
| fannkuch                   | 253 ms                                                      | 240 ms: 1.06x faster                                                          |
| gc_traversal               | 1.97 ms                                                     | 1.86 ms: 1.06x faster                                                         |
| async_tree_none            | 226 ms                                                      | 214 ms: 1.06x faster                                                          |
| shortest_path              | 362 ms                                                      | 344 ms: 1.05x faster                                                          |
| bench_mp_pool              | 86.4 ms                                                     | 82.1 ms: 1.05x faster                                                         |
| bench_thread_pool          | 847 us                                                      | 806 us: 1.05x faster                                                          |
| xml_etree_process          | 37.0 ms                                                     | 35.7 ms: 1.04x faster                                                         |
| float                      | 49.9 ms                                                     | 48.3 ms: 1.03x faster                                                         |
| python_startup_no_site     | 18.1 ms                                                     | 17.6 ms: 1.03x faster                                                         |
| dulwich_log                | 40.8 ms                                                     | 40.0 ms: 1.02x faster                                                         |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                          |
| pprint_pformat             | 999 ms                                                      | 988 ms: 1.01x faster                                                          |
| pidigits                   | 148 ms                                                      | 147 ms: 1.01x faster                                                          |
| pprint_safe_repr           | 494 ms                                                      | 497 ms: 1.01x slower                                                          |
| xml_etree_iterparse        | 61.8 ms                                                     | 62.3 ms: 1.01x slower                                                         |
| html5lib                   | 38.9 ms                                                     | 39.6 ms: 1.02x slower                                                         |
| coverage                   | 45.6 ms                                                     | 46.5 ms: 1.02x slower                                                         |
| regex_compile              | 80.5 ms                                                     | 82.2 ms: 1.02x slower                                                         |
| pyflate                    | 283 ms                                                      | 290 ms: 1.02x slower                                                          |
| go                         | 87.0 ms                                                     | 89.7 ms: 1.03x slower                                                         |
| logging_silent             | 54.6 ns                                                     | 56.7 ns: 1.04x slower                                                         |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 399 ms: 1.04x slower                                                          |
| pycparser                  | 683 ms                                                      | 717 ms: 1.05x slower                                                          |
| sympy_sum                  | 86.9 ms                                                     | 91.5 ms: 1.05x slower                                                         |
| sympy_expand               | 291 ms                                                      | 307 ms: 1.05x slower                                                          |
| sympy_str                  | 169 ms                                                      | 178 ms: 1.05x slower                                                          |
| json_dumps                 | 5.92 ms                                                     | 6.27 ms: 1.06x slower                                                         |
| create_gc_cycles           | 1.26 ms                                                     | 1.33 ms: 1.06x slower                                                         |
| logging_simple             | 5.96 us                                                     | 6.32 us: 1.06x slower                                                         |
| chaos                      | 38.5 ms                                                     | 41.1 ms: 1.07x slower                                                         |
| coroutines                 | 12.8 ms                                                     | 13.6 ms: 1.07x slower                                                         |
| typing_runtime_protocols   | 105 us                                                      | 114 us: 1.08x slower                                                          |
| mdp                        | 1.39 sec                                                    | 1.50 sec: 1.08x slower                                                        |
| sphinx                     | 633 ms                                                      | 687 ms: 1.09x slower                                                          |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 410 ms: 1.09x slower                                                          |
| logging_format             | 6.26 us                                                     | 6.82 us: 1.09x slower                                                         |
| sympy_integrate            | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                         |
| pickle_pure_python         | 190 us                                                      | 208 us: 1.10x slower                                                          |
| async_tree_io              | 521 ms                                                      | 575 ms: 1.10x slower                                                          |
| docutils                   | 1.57 sec                                                    | 1.75 sec: 1.11x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 579 ms: 1.12x slower                                                          |
| sqlglot_parse              | 771 us                                                      | 863 us: 1.12x slower                                                          |
| nqueens                    | 56.7 ms                                                     | 64.2 ms: 1.13x slower                                                         |
| k_core                     | 1.74 sec                                                    | 1.98 sec: 1.14x slower                                                        |
| comprehensions             | 10.3 us                                                     | 11.8 us: 1.15x slower                                                         |
| sqlglot_transpile          | 956 us                                                      | 1.11 ms: 1.16x slower                                                         |
| sqlglot_optimize           | 32.9 ms                                                     | 38.9 ms: 1.18x slower                                                         |
| sqlglot_normalize          | 175 ms                                                      | 208 ms: 1.19x slower                                                          |
| generators                 | 19.5 ms                                                     | 23.4 ms: 1.20x slower                                                         |
| async_generators           | 223 ms                                                      | 270 ms: 1.21x slower                                                          |
| deltablue                  | 1.92 ms                                                     | 2.34 ms: 1.22x slower                                                         |
| django_template            | 22.4 ms                                                     | 27.6 ms: 1.23x slower                                                         |
| genshi_text                | 15.6 ms                                                     | 19.6 ms: 1.26x slower                                                         |
| hexiom                     | 3.89 ms                                                     | 4.98 ms: 1.28x slower                                                         |
| richards                   | 27.3 ms                                                     | 35.1 ms: 1.29x slower                                                         |
| richards_super             | 30.9 ms                                                     | 39.7 ms: 1.29x slower                                                         |
| raytrace                   | 160 ms                                                      | 212 ms: 1.33x slower                                                          |
| genshi_xml                 | 35.5 ms                                                     | 48.0 ms: 1.35x slower                                                         |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                  |

Benchmark hidden because not significant (7): async_tree_none_tg, xml_etree_parse, async_tree_memoization, scimark_lu, meteor_contest, 2to3, asyncio_websockets
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (3) of results/bm-20241122-3.14.0a2+-a8a4ed3-JIT/bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.018x faster
# HPT report

- Reliability score: 95.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
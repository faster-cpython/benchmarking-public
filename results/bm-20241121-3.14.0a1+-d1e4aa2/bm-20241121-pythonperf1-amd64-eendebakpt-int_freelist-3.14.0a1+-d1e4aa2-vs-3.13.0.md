# Results vs. 3.13.0

- fork: eendebakpt
- ref: int_freelist
- machine: windows-amd64
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.038x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 225 ms: 1.02x slower                                                    |
| docutils       | 1.57 sec                                                    | 1.71 sec: 1.09x slower                                                  |
| html5lib       | 38.9 ms                                                     | 40.3 ms: 1.04x slower                                                   |
| sphinx         | 633 ms                                                      | 675 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                       | 1.05x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 259 ms: 1.11x faster                                                    |
| asyncio_websockets         | 318 ms                                                      | 308 ms: 1.03x faster                                                    |
| async_tree_none            | 226 ms                                                      | 221 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 402 ms: 1.07x slower                                                    |
| coroutines                 | 12.8 ms                                                     | 13.7 ms: 1.07x slower                                                   |
| async_tree_io              | 521 ms                                                      | 563 ms: 1.08x slower                                                    |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                    |
| async_tree_io_tg           | 518 ms                                                      | 629 ms: 1.21x slower                                                    |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                            |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 49.9 ms                                                     | 56.2 ms: 1.12x slower                                                   |
| nbody          | 68.4 ms                                                     | 78.8 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                       | 1.09x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.9 ms: 1.43x faster                                                   |
| regex_effbot   | 1.58 ms                                                     | 1.56 ms: 1.01x faster                                                   |
| regex_compile  | 80.5 ms                                                     | 91.6 ms: 1.14x slower                                                   |
| Geometric mean | (ref)                                                       | 1.06x faster                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                   |
| xml_etree_iterparse  | 61.8 ms                                                     | 66.0 ms: 1.07x slower                                                   |
| xml_etree_generate   | 54.0 ms                                                     | 58.3 ms: 1.08x slower                                                   |
| xml_etree_process    | 37.0 ms                                                     | 41.0 ms: 1.11x slower                                                   |
| tomli_loads          | 1.39 sec                                                    | 1.55 sec: 1.11x slower                                                  |
| json_dumps           | 5.92 ms                                                     | 6.78 ms: 1.15x slower                                                   |
| unpickle_pure_python | 133 us                                                      | 157 us: 1.18x slower                                                    |
| pickle_pure_python   | 190 us                                                      | 231 us: 1.22x slower                                                    |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 23.2 ms: 1.10x faster                                                   |
| python_startup_no_site | 18.1 ms                                                     | 17.2 ms: 1.05x faster                                                   |
| Geometric mean         | (ref)                                                       | 1.07x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 36.7 ms: 1.04x slower                                                   |
| genshi_text     | 15.6 ms                                                     | 17.0 ms: 1.09x slower                                                   |
| mako            | 6.35 ms                                                     | 7.04 ms: 1.11x slower                                                   |
| django_template | 22.4 ms                                                     | 25.6 ms: 1.14x slower                                                   |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 523 us: 16.81x faster                                                   |
| regex_v8                   | 21.4 ms                                                     | 14.9 ms: 1.43x faster                                                   |
| deepcopy                   | 226 us                                                      | 195 us: 1.16x faster                                                    |
| async_tree_memoization_tg  | 288 ms                                                      | 259 ms: 1.11x faster                                                    |
| python_startup             | 25.4 ms                                                     | 23.2 ms: 1.10x faster                                                   |
| pathlib                    | 80.9 ms                                                     | 76.1 ms: 1.06x faster                                                   |
| deepcopy_memo              | 23.3 us                                                     | 22.0 us: 1.06x faster                                                   |
| bench_mp_pool              | 86.4 ms                                                     | 81.8 ms: 1.06x faster                                                   |
| python_startup_no_site     | 18.1 ms                                                     | 17.2 ms: 1.05x faster                                                   |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                   |
| asyncio_websockets         | 318 ms                                                      | 308 ms: 1.03x faster                                                    |
| gc_traversal               | 1.97 ms                                                     | 1.92 ms: 1.03x faster                                                   |
| async_tree_none            | 226 ms                                                      | 221 ms: 1.02x faster                                                    |
| deepcopy_reduce            | 2.06 us                                                     | 2.03 us: 1.01x faster                                                   |
| regex_effbot               | 1.58 ms                                                     | 1.56 ms: 1.01x faster                                                   |
| connected_components       | 332 ms                                                      | 330 ms: 1.01x faster                                                    |
| telco                      | 4.79 ms                                                     | 4.85 ms: 1.01x slower                                                   |
| 2to3                       | 221 ms                                                      | 225 ms: 1.02x slower                                                    |
| html5lib                   | 38.9 ms                                                     | 40.3 ms: 1.04x slower                                                   |
| genshi_xml                 | 35.5 ms                                                     | 36.7 ms: 1.04x slower                                                   |
| sympy_sum                  | 86.9 ms                                                     | 90.2 ms: 1.04x slower                                                   |
| coverage                   | 45.6 ms                                                     | 47.4 ms: 1.04x slower                                                   |
| go                         | 87.0 ms                                                     | 90.5 ms: 1.04x slower                                                   |
| mdp                        | 1.39 sec                                                    | 1.46 sec: 1.05x slower                                                  |
| spectral_norm              | 62.8 ms                                                     | 66.2 ms: 1.05x slower                                                   |
| dulwich_log                | 40.8 ms                                                     | 43.1 ms: 1.06x slower                                                   |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.60 ms: 1.06x slower                                                   |
| sympy_str                  | 169 ms                                                      | 179 ms: 1.06x slower                                                    |
| sphinx                     | 633 ms                                                      | 675 ms: 1.07x slower                                                    |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 402 ms: 1.07x slower                                                    |
| sympy_expand               | 291 ms                                                      | 311 ms: 1.07x slower                                                    |
| xml_etree_iterparse        | 61.8 ms                                                     | 66.0 ms: 1.07x slower                                                   |
| meteor_contest             | 73.5 ms                                                     | 78.9 ms: 1.07x slower                                                   |
| coroutines                 | 12.8 ms                                                     | 13.7 ms: 1.07x slower                                                   |
| bpe_tokeniser              | 2.91 sec                                                    | 3.13 sec: 1.07x slower                                                  |
| logging_simple             | 5.96 us                                                     | 6.42 us: 1.08x slower                                                   |
| xml_etree_generate         | 54.0 ms                                                     | 58.3 ms: 1.08x slower                                                   |
| async_tree_io              | 521 ms                                                      | 563 ms: 1.08x slower                                                    |
| crypto_pyaes               | 45.4 ms                                                     | 49.1 ms: 1.08x slower                                                   |
| pycparser                  | 683 ms                                                      | 738 ms: 1.08x slower                                                    |
| sympy_integrate            | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                   |
| docutils                   | 1.57 sec                                                    | 1.71 sec: 1.09x slower                                                  |
| create_gc_cycles           | 1.26 ms                                                     | 1.37 ms: 1.09x slower                                                   |
| genshi_text                | 15.6 ms                                                     | 17.0 ms: 1.09x slower                                                   |
| logging_format             | 6.26 us                                                     | 6.85 us: 1.09x slower                                                   |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                    |
| fannkuch                   | 253 ms                                                      | 279 ms: 1.10x slower                                                    |
| typing_runtime_protocols   | 105 us                                                      | 116 us: 1.10x slower                                                    |
| mako                       | 6.35 ms                                                     | 7.04 ms: 1.11x slower                                                   |
| xml_etree_process          | 37.0 ms                                                     | 41.0 ms: 1.11x slower                                                   |
| tomli_loads                | 1.39 sec                                                    | 1.55 sec: 1.11x slower                                                  |
| float                      | 49.9 ms                                                     | 56.2 ms: 1.12x slower                                                   |
| pyflate                    | 283 ms                                                      | 319 ms: 1.13x slower                                                    |
| sqlglot_optimize           | 32.9 ms                                                     | 37.4 ms: 1.14x slower                                                   |
| regex_compile              | 80.5 ms                                                     | 91.6 ms: 1.14x slower                                                   |
| chaos                      | 38.5 ms                                                     | 44.0 ms: 1.14x slower                                                   |
| sqlglot_normalize          | 175 ms                                                      | 199 ms: 1.14x slower                                                    |
| django_template            | 22.4 ms                                                     | 25.6 ms: 1.14x slower                                                   |
| scimark_fft                | 172 ms                                                      | 197 ms: 1.14x slower                                                    |
| json_dumps                 | 5.92 ms                                                     | 6.78 ms: 1.15x slower                                                   |
| nqueens                    | 56.7 ms                                                     | 65.1 ms: 1.15x slower                                                   |
| generators                 | 19.5 ms                                                     | 22.4 ms: 1.15x slower                                                   |
| nbody                      | 68.4 ms                                                     | 78.8 ms: 1.15x slower                                                   |
| pprint_pformat             | 999 ms                                                      | 1.15 sec: 1.16x slower                                                  |
| pprint_safe_repr           | 494 ms                                                      | 572 ms: 1.16x slower                                                    |
| unpickle_pure_python       | 133 us                                                      | 157 us: 1.18x slower                                                    |
| richards_super             | 30.9 ms                                                     | 36.5 ms: 1.18x slower                                                   |
| hexiom                     | 3.89 ms                                                     | 4.61 ms: 1.18x slower                                                   |
| sqlglot_transpile          | 956 us                                                      | 1.14 ms: 1.19x slower                                                   |
| sqlglot_parse              | 771 us                                                      | 918 us: 1.19x slower                                                    |
| richards                   | 27.3 ms                                                     | 32.7 ms: 1.20x slower                                                   |
| scimark_monte_carlo        | 40.8 ms                                                     | 49.0 ms: 1.20x slower                                                   |
| logging_silent             | 54.6 ns                                                     | 65.7 ns: 1.20x slower                                                   |
| scimark_sor                | 76.2 ms                                                     | 91.6 ms: 1.20x slower                                                   |
| comprehensions             | 10.3 us                                                     | 12.4 us: 1.21x slower                                                   |
| async_tree_io_tg           | 518 ms                                                      | 629 ms: 1.21x slower                                                    |
| pickle_pure_python         | 190 us                                                      | 231 us: 1.22x slower                                                    |
| deltablue                  | 1.92 ms                                                     | 2.35 ms: 1.23x slower                                                   |
| raytrace                   | 160 ms                                                      | 198 ms: 1.24x slower                                                    |
| scimark_lu                 | 53.0 ms                                                     | 66.3 ms: 1.25x slower                                                   |
| k_core                     | 1.74 sec                                                    | 2.50 sec: 1.44x slower                                                  |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                            |

Benchmark hidden because not significant (10): bench_thread_pool, json, pidigits, regex_dna, xml_etree_parse, shortest_path, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (3) of results/bm-20241121-3.14.0a1+-d1e4aa2/bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.038x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown
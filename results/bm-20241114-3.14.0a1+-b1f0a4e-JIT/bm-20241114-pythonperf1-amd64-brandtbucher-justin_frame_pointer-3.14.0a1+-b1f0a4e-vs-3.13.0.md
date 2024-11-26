# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: windows-amd64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.021x slower
- HPT reliability: 99.21%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 248 ms: 1.12x slower                                                              |
| docutils       | 1.57 sec                                                    | 1.90 sec: 1.21x slower                                                            |
| sphinx         | 633 ms                                                      | 772 ms: 1.22x slower                                                              |
| Geometric mean | (ref)                                                       | 1.13x slower                                                                      |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 251 ms: 1.15x faster                                                              |
| async_tree_none            | 226 ms                                                      | 212 ms: 1.07x faster                                                              |
| async_tree_memoization     | 276 ms                                                      | 262 ms: 1.05x faster                                                              |
| asyncio_websockets         | 318 ms                                                      | 305 ms: 1.04x faster                                                              |
| async_tree_io              | 521 ms                                                      | 532 ms: 1.02x slower                                                              |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 394 ms: 1.03x slower                                                              |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 395 ms: 1.05x slower                                                              |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.10x slower                                                             |
| async_tree_io_tg           | 518 ms                                                      | 587 ms: 1.13x slower                                                              |
| async_generators           | 223 ms                                                      | 263 ms: 1.18x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 56.5 ms: 1.21x faster                                                             |
| float          | 49.9 ms                                                     | 48.4 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.4 ms: 1.39x faster                                                             |
| regex_effbot   | 1.58 ms                                                     | 1.59 ms: 1.01x slower                                                             |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                              |
| regex_compile  | 80.5 ms                                                     | 93.3 ms: 1.16x slower                                                             |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.30 sec: 1.08x faster                                                            |
| json_loads           | 15.1 us                                                     | 14.3 us: 1.06x faster                                                             |
| xml_etree_generate   | 54.0 ms                                                     | 51.8 ms: 1.04x faster                                                             |
| xml_etree_iterparse  | 61.8 ms                                                     | 63.0 ms: 1.02x slower                                                             |
| json_dumps           | 5.92 ms                                                     | 6.11 ms: 1.03x slower                                                             |
| unpickle_pure_python | 133 us                                                      | 149 us: 1.12x slower                                                              |
| pickle_pure_python   | 190 us                                                      | 214 us: 1.13x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 23.5 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.44 ms: 1.17x faster                                                             |
| django_template | 22.4 ms                                                     | 26.9 ms: 1.20x slower                                                             |
| genshi_text     | 15.6 ms                                                     | 19.4 ms: 1.25x slower                                                             |
| genshi_xml      | 35.5 ms                                                     | 46.4 ms: 1.31x slower                                                             |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 530 us: 16.59x faster                                                             |
| regex_v8                   | 21.4 ms                                                     | 15.4 ms: 1.39x faster                                                             |
| deepcopy_memo              | 23.3 us                                                     | 17.6 us: 1.33x faster                                                             |
| nbody                      | 68.4 ms                                                     | 56.5 ms: 1.21x faster                                                             |
| mako                       | 6.35 ms                                                     | 5.44 ms: 1.17x faster                                                             |
| async_tree_memoization_tg  | 288 ms                                                      | 251 ms: 1.15x faster                                                              |
| deepcopy                   | 226 us                                                      | 197 us: 1.15x faster                                                              |
| spectral_norm              | 62.8 ms                                                     | 55.7 ms: 1.13x faster                                                             |
| scimark_sor                | 76.2 ms                                                     | 68.9 ms: 1.11x faster                                                             |
| json                       | 3.19 ms                                                     | 2.93 ms: 1.09x faster                                                             |
| python_startup             | 25.4 ms                                                     | 23.5 ms: 1.08x faster                                                             |
| tomli_loads                | 1.39 sec                                                    | 1.30 sec: 1.08x faster                                                            |
| pathlib                    | 80.9 ms                                                     | 75.2 ms: 1.08x faster                                                             |
| crypto_pyaes               | 45.4 ms                                                     | 42.3 ms: 1.07x faster                                                             |
| async_tree_none            | 226 ms                                                      | 212 ms: 1.07x faster                                                              |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.31 ms: 1.06x faster                                                             |
| bpe_tokeniser              | 2.91 sec                                                    | 2.75 sec: 1.06x faster                                                            |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.06x faster                                                             |
| async_tree_memoization     | 276 ms                                                      | 262 ms: 1.05x faster                                                              |
| connected_components       | 332 ms                                                      | 316 ms: 1.05x faster                                                              |
| asyncio_websockets         | 318 ms                                                      | 305 ms: 1.04x faster                                                              |
| shortest_path              | 362 ms                                                      | 347 ms: 1.04x faster                                                              |
| xml_etree_generate         | 54.0 ms                                                     | 51.8 ms: 1.04x faster                                                             |
| fannkuch                   | 253 ms                                                      | 243 ms: 1.04x faster                                                              |
| scimark_monte_carlo        | 40.8 ms                                                     | 39.2 ms: 1.04x faster                                                             |
| deepcopy_reduce            | 2.06 us                                                     | 1.98 us: 1.04x faster                                                             |
| scimark_fft                | 172 ms                                                      | 166 ms: 1.04x faster                                                              |
| telco                      | 4.79 ms                                                     | 4.62 ms: 1.04x faster                                                             |
| float                      | 49.9 ms                                                     | 48.4 ms: 1.03x faster                                                             |
| pprint_safe_repr           | 494 ms                                                      | 478 ms: 1.03x faster                                                              |
| dulwich_log                | 40.8 ms                                                     | 39.7 ms: 1.03x faster                                                             |
| gc_traversal               | 1.97 ms                                                     | 1.92 ms: 1.03x faster                                                             |
| pprint_pformat             | 999 ms                                                      | 979 ms: 1.02x faster                                                              |
| regex_effbot               | 1.58 ms                                                     | 1.59 ms: 1.01x slower                                                             |
| bench_mp_pool              | 86.4 ms                                                     | 87.6 ms: 1.01x slower                                                             |
| xml_etree_iterparse        | 61.8 ms                                                     | 63.0 ms: 1.02x slower                                                             |
| async_tree_io              | 521 ms                                                      | 532 ms: 1.02x slower                                                              |
| coverage                   | 45.6 ms                                                     | 46.5 ms: 1.02x slower                                                             |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 394 ms: 1.03x slower                                                              |
| meteor_contest             | 73.5 ms                                                     | 75.8 ms: 1.03x slower                                                             |
| json_dumps                 | 5.92 ms                                                     | 6.11 ms: 1.03x slower                                                             |
| logging_simple             | 5.96 us                                                     | 6.25 us: 1.05x slower                                                             |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 395 ms: 1.05x slower                                                              |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                              |
| logging_format             | 6.26 us                                                     | 6.68 us: 1.07x slower                                                             |
| pycparser                  | 683 ms                                                      | 734 ms: 1.08x slower                                                              |
| create_gc_cycles           | 1.26 ms                                                     | 1.36 ms: 1.08x slower                                                             |
| logging_silent             | 54.6 ns                                                     | 59.2 ns: 1.08x slower                                                             |
| scimark_lu                 | 53.0 ms                                                     | 57.4 ms: 1.08x slower                                                             |
| typing_runtime_protocols   | 105 us                                                      | 115 us: 1.09x slower                                                              |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.10x slower                                                             |
| go                         | 87.0 ms                                                     | 95.9 ms: 1.10x slower                                                             |
| mdp                        | 1.39 sec                                                    | 1.53 sec: 1.10x slower                                                            |
| chaos                      | 38.5 ms                                                     | 42.6 ms: 1.11x slower                                                             |
| unpickle_pure_python       | 133 us                                                      | 149 us: 1.12x slower                                                              |
| 2to3                       | 221 ms                                                      | 248 ms: 1.12x slower                                                              |
| pyflate                    | 283 ms                                                      | 317 ms: 1.12x slower                                                              |
| pickle_pure_python         | 190 us                                                      | 214 us: 1.13x slower                                                              |
| async_tree_io_tg           | 518 ms                                                      | 587 ms: 1.13x slower                                                              |
| sympy_expand               | 291 ms                                                      | 331 ms: 1.14x slower                                                              |
| regex_compile              | 80.5 ms                                                     | 93.3 ms: 1.16x slower                                                             |
| sympy_str                  | 169 ms                                                      | 196 ms: 1.16x slower                                                              |
| async_generators           | 223 ms                                                      | 263 ms: 1.18x slower                                                              |
| nqueens                    | 56.7 ms                                                     | 67.0 ms: 1.18x slower                                                             |
| sqlglot_parse              | 771 us                                                      | 915 us: 1.19x slower                                                              |
| sympy_sum                  | 86.9 ms                                                     | 104 ms: 1.20x slower                                                              |
| django_template            | 22.4 ms                                                     | 26.9 ms: 1.20x slower                                                             |
| docutils                   | 1.57 sec                                                    | 1.90 sec: 1.21x slower                                                            |
| sphinx                     | 633 ms                                                      | 772 ms: 1.22x slower                                                              |
| sqlglot_normalize          | 175 ms                                                      | 214 ms: 1.23x slower                                                              |
| comprehensions             | 10.3 us                                                     | 12.7 us: 1.24x slower                                                             |
| genshi_text                | 15.6 ms                                                     | 19.4 ms: 1.25x slower                                                             |
| sqlglot_transpile          | 956 us                                                      | 1.20 ms: 1.25x slower                                                             |
| richards_super             | 30.9 ms                                                     | 39.0 ms: 1.26x slower                                                             |
| deltablue                  | 1.92 ms                                                     | 2.43 ms: 1.27x slower                                                             |
| richards                   | 27.3 ms                                                     | 35.0 ms: 1.28x slower                                                             |
| sympy_integrate            | 12.5 ms                                                     | 16.0 ms: 1.28x slower                                                             |
| generators                 | 19.5 ms                                                     | 25.3 ms: 1.30x slower                                                             |
| genshi_xml                 | 35.5 ms                                                     | 46.4 ms: 1.31x slower                                                             |
| pylint                     | 211 ms                                                      | 277 ms: 1.32x slower                                                              |
| sqlglot_optimize           | 32.9 ms                                                     | 43.6 ms: 1.33x slower                                                             |
| k_core                     | 1.74 sec                                                    | 2.44 sec: 1.40x slower                                                            |
| raytrace                   | 160 ms                                                      | 225 ms: 1.40x slower                                                              |
| hexiom                     | 3.89 ms                                                     | 5.53 ms: 1.42x slower                                                             |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                      |

Benchmark hidden because not significant (7): bench_thread_pool, python_startup_no_site, pidigits, async_tree_none_tg, xml_etree_process, xml_etree_parse, html5lib
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (3) of results/bm-20241114-3.14.0a1+-b1f0a4e-JIT/bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.021x slower
# HPT report

- Reliability score: 99.21% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
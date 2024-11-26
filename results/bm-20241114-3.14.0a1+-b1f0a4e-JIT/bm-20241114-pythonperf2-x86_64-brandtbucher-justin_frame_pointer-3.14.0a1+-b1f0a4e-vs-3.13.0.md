# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-x86_64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.051x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 330 ms: 1.13x slower                                                               |
| docutils       | 2.81 sec                                                     | 3.24 sec: 1.15x slower                                                             |
| html5lib       | 72.9 ms                                                      | 72.2 ms: 1.01x faster                                                              |
| sphinx         | 1.11 sec                                                     | 1.30 sec: 1.17x slower                                                             |
| Geometric mean | (ref)                                                        | 1.11x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 379 ms: 1.21x faster                                                               |
| async_tree_none            | 370 ms                                                       | 345 ms: 1.07x faster                                                               |
| async_tree_memoization     | 447 ms                                                       | 424 ms: 1.06x faster                                                               |
| async_tree_none_tg         | 342 ms                                                       | 328 ms: 1.04x faster                                                               |
| asyncio_websockets         | 395 ms                                                       | 385 ms: 1.03x faster                                                               |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 565 ms: 1.02x faster                                                               |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 588 ms: 1.01x faster                                                               |
| async_tree_io              | 832 ms                                                       | 861 ms: 1.03x slower                                                               |
| async_tree_io_tg           | 823 ms                                                       | 878 ms: 1.07x slower                                                               |
| async_generators           | 364 ms                                                       | 479 ms: 1.32x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                                       |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 81.1 ms: 1.01x faster                                                              |
| pidigits       | 252 ms                                                       | 252 ms: 1.00x faster                                                               |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.70 ms: 1.05x slower                                                              |
| regex_compile  | 143 ms                                                       | 153 ms: 1.07x slower                                                               |
| regex_v8       | 24.9 ms                                                      | 26.8 ms: 1.08x slower                                                              |
| regex_dna      | 238 ms                                                       | 257 ms: 1.08x slower                                                               |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.22 sec: 1.09x faster                                                             |
| json_loads           | 24.7 us                                                      | 24.5 us: 1.01x faster                                                              |
| xml_etree_process    | 60.7 ms                                                      | 61.3 ms: 1.01x slower                                                              |
| xml_etree_generate   | 85.2 ms                                                      | 86.3 ms: 1.01x slower                                                              |
| xml_etree_parse      | 144 ms                                                       | 147 ms: 1.02x slower                                                               |
| xml_etree_iterparse  | 99.8 ms                                                      | 102 ms: 1.02x slower                                                               |
| unpickle_pure_python | 216 us                                                       | 228 us: 1.05x slower                                                               |
| json_dumps           | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                                              |
| pickle_pure_python   | 322 us                                                       | 351 us: 1.09x slower                                                               |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.93 ms                                                      | 9.08 ms: 1.02x slower                                                              |
| python_startup         | 15.6 ms                                                      | 16.1 ms: 1.03x slower                                                              |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 10.2 ms: 1.01x faster                                                              |
| genshi_text     | 27.2 ms                                                      | 30.7 ms: 1.13x slower                                                              |
| django_template | 38.9 ms                                                      | 44.0 ms: 1.13x slower                                                              |
| genshi_xml      | 58.0 ms                                                      | 67.6 ms: 1.16x slower                                                              |
| Geometric mean  | (ref)                                                        | 1.10x slower                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 379 ms: 1.21x faster                                                               |
| deepcopy                   | 388 us                                                       | 325 us: 1.20x faster                                                               |
| deepcopy_memo              | 38.9 us                                                      | 33.8 us: 1.15x faster                                                              |
| telco                      | 8.77 ms                                                      | 7.89 ms: 1.11x faster                                                              |
| deepcopy_reduce            | 3.49 us                                                      | 3.17 us: 1.10x faster                                                              |
| tomli_loads                | 2.43 sec                                                     | 2.22 sec: 1.09x faster                                                             |
| json                       | 5.62 ms                                                      | 5.21 ms: 1.08x faster                                                              |
| shortest_path              | 477 ms                                                       | 444 ms: 1.08x faster                                                               |
| async_tree_none            | 370 ms                                                       | 345 ms: 1.07x faster                                                               |
| coverage                   | 84.5 ms                                                      | 78.8 ms: 1.07x faster                                                              |
| pathlib                    | 17.4 ms                                                      | 16.3 ms: 1.07x faster                                                              |
| scimark_sor                | 125 ms                                                       | 117 ms: 1.07x faster                                                               |
| connected_components       | 443 ms                                                       | 416 ms: 1.06x faster                                                               |
| async_tree_memoization     | 447 ms                                                       | 424 ms: 1.06x faster                                                               |
| async_tree_none_tg         | 342 ms                                                       | 328 ms: 1.04x faster                                                               |
| richards                   | 52.5 ms                                                      | 50.8 ms: 1.03x faster                                                              |
| richards_super             | 60.2 ms                                                      | 58.6 ms: 1.03x faster                                                              |
| asyncio_websockets         | 395 ms                                                       | 385 ms: 1.03x faster                                                               |
| bpe_tokeniser              | 5.09 sec                                                     | 5.01 sec: 1.02x faster                                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 565 ms: 1.02x faster                                                               |
| mako                       | 10.3 ms                                                      | 10.2 ms: 1.01x faster                                                              |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 588 ms: 1.01x faster                                                               |
| go                         | 167 ms                                                       | 165 ms: 1.01x faster                                                               |
| json_loads                 | 24.7 us                                                      | 24.5 us: 1.01x faster                                                              |
| html5lib                   | 72.9 ms                                                      | 72.2 ms: 1.01x faster                                                              |
| thrift                     | 918 us                                                       | 909 us: 1.01x faster                                                               |
| float                      | 81.6 ms                                                      | 81.1 ms: 1.01x faster                                                              |
| pidigits                   | 252 ms                                                       | 252 ms: 1.00x faster                                                               |
| pycparser                  | 1.28 sec                                                     | 1.29 sec: 1.01x slower                                                             |
| xml_etree_process          | 60.7 ms                                                      | 61.3 ms: 1.01x slower                                                              |
| xml_etree_generate         | 85.2 ms                                                      | 86.3 ms: 1.01x slower                                                              |
| pprint_pformat             | 1.70 sec                                                     | 1.73 sec: 1.02x slower                                                             |
| python_startup_no_site     | 8.93 ms                                                      | 9.08 ms: 1.02x slower                                                              |
| xml_etree_parse            | 144 ms                                                       | 147 ms: 1.02x slower                                                               |
| xml_etree_iterparse        | 99.8 ms                                                      | 102 ms: 1.02x slower                                                               |
| logging_silent             | 97.5 ns                                                      | 100 ns: 1.03x slower                                                               |
| python_startup             | 15.6 ms                                                      | 16.1 ms: 1.03x slower                                                              |
| dulwich_log                | 65.5 ms                                                      | 67.6 ms: 1.03x slower                                                              |
| spectral_norm              | 97.4 ms                                                      | 101 ms: 1.03x slower                                                               |
| async_tree_io              | 832 ms                                                       | 861 ms: 1.03x slower                                                               |
| sqlalchemy_imperative      | 18.1 ms                                                      | 18.8 ms: 1.04x slower                                                              |
| pyflate                    | 493 ms                                                       | 511 ms: 1.04x slower                                                               |
| meteor_contest             | 130 ms                                                       | 135 ms: 1.04x slower                                                               |
| scimark_lu                 | 97.4 ms                                                      | 102 ms: 1.04x slower                                                               |
| mdp                        | 2.53 sec                                                     | 2.65 sec: 1.05x slower                                                             |
| deltablue                  | 3.38 ms                                                      | 3.55 ms: 1.05x slower                                                              |
| fannkuch                   | 384 ms                                                       | 403 ms: 1.05x slower                                                               |
| logging_format             | 6.95 us                                                      | 7.31 us: 1.05x slower                                                              |
| unpickle_pure_python       | 216 us                                                       | 228 us: 1.05x slower                                                               |
| regex_effbot               | 3.51 ms                                                      | 3.70 ms: 1.05x slower                                                              |
| typing_runtime_protocols   | 176 us                                                       | 186 us: 1.06x slower                                                               |
| crypto_pyaes               | 73.5 ms                                                      | 78.1 ms: 1.06x slower                                                              |
| json_dumps                 | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                                              |
| async_tree_io_tg           | 823 ms                                                       | 878 ms: 1.07x slower                                                               |
| regex_compile              | 143 ms                                                       | 153 ms: 1.07x slower                                                               |
| bench_thread_pool          | 929 us                                                       | 998 us: 1.07x slower                                                               |
| regex_v8                   | 24.9 ms                                                      | 26.8 ms: 1.08x slower                                                              |
| regex_dna                  | 238 ms                                                       | 257 ms: 1.08x slower                                                               |
| logging_simple             | 6.28 us                                                      | 6.78 us: 1.08x slower                                                              |
| sympy_expand               | 506 ms                                                       | 548 ms: 1.08x slower                                                               |
| pickle_pure_python         | 322 us                                                       | 351 us: 1.09x slower                                                               |
| create_gc_cycles           | 2.65 ms                                                      | 2.90 ms: 1.09x slower                                                              |
| scimark_fft                | 298 ms                                                       | 326 ms: 1.10x slower                                                               |
| sqlglot_parse              | 1.37 ms                                                      | 1.53 ms: 1.12x slower                                                              |
| sympy_str                  | 297 ms                                                       | 332 ms: 1.12x slower                                                               |
| 2to3                       | 293 ms                                                       | 330 ms: 1.13x slower                                                               |
| genshi_text                | 27.2 ms                                                      | 30.7 ms: 1.13x slower                                                              |
| scimark_monte_carlo        | 65.2 ms                                                      | 73.8 ms: 1.13x slower                                                              |
| django_template            | 38.9 ms                                                      | 44.0 ms: 1.13x slower                                                              |
| pylint                     | 345 ms                                                       | 392 ms: 1.14x slower                                                               |
| sqlalchemy_declarative     | 148 ms                                                       | 170 ms: 1.15x slower                                                               |
| sqlglot_transpile          | 1.76 ms                                                      | 2.03 ms: 1.15x slower                                                              |
| docutils                   | 2.81 sec                                                     | 3.24 sec: 1.15x slower                                                             |
| genshi_xml                 | 58.0 ms                                                      | 67.6 ms: 1.16x slower                                                              |
| chaos                      | 60.6 ms                                                      | 70.9 ms: 1.17x slower                                                              |
| sphinx                     | 1.11 sec                                                     | 1.30 sec: 1.17x slower                                                             |
| sympy_sum                  | 154 ms                                                       | 181 ms: 1.18x slower                                                               |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.00 ms: 1.19x slower                                                              |
| nqueens                    | 92.3 ms                                                      | 110 ms: 1.19x slower                                                               |
| raytrace                   | 267 ms                                                       | 318 ms: 1.19x slower                                                               |
| sympy_integrate            | 23.4 ms                                                      | 28.1 ms: 1.20x slower                                                              |
| sqlglot_normalize          | 119 ms                                                       | 144 ms: 1.21x slower                                                               |
| hexiom                     | 6.47 ms                                                      | 7.96 ms: 1.23x slower                                                              |
| comprehensions             | 17.3 us                                                      | 21.7 us: 1.26x slower                                                              |
| sqlglot_optimize           | 58.7 ms                                                      | 74.3 ms: 1.27x slower                                                              |
| generators                 | 33.9 ms                                                      | 43.4 ms: 1.28x slower                                                              |
| async_generators           | 364 ms                                                       | 479 ms: 1.32x slower                                                               |
| k_core                     | 2.18 sec                                                     | 3.03 sec: 1.39x slower                                                             |
| gc_traversal               | 4.48 ms                                                      | 6.29 ms: 1.40x slower                                                              |
| bench_mp_pool              | 4.82 ms                                                      | 1.37 sec: 285.05x slower                                                           |
| Geometric mean             | (ref)                                                        | 1.12x slower                                                                       |

Benchmark hidden because not significant (3): nbody, coroutines, pprint_safe_repr
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (3) of results/bm-20241114-3.14.0a1+-b1f0a4e-JIT/bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.051x slower
# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.07x
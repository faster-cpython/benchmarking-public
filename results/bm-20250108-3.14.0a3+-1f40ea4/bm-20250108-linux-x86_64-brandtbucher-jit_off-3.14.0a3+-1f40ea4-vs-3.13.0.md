# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_off
- machine: linux-x86_64
- commit hash: 1f40ea4
- commit date: 2025-01-08
- overall geometric mean: 1.038x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                            |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                          |
| html5lib       | 63.4 ms                                                | 61.8 ms: 1.02x faster                                           |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.01x faster                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 306 ms: 1.51x faster                                            |
| async_tree_io_tg           | 861 ms                                                 | 587 ms: 1.47x faster                                            |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.39x faster                                            |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                            |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.35x faster                                            |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 483 ms: 1.19x faster                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 461 ms: 1.18x faster                                            |
| async_generators           | 433 ms                                                 | 429 ms: 1.01x faster                                            |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                           |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 78.7 ms                                                | 73.2 ms: 1.07x faster                                           |
| pidigits       | 186 ms                                                 | 190 ms: 1.02x slower                                            |
| nbody          | 87.7 ms                                                | 97.8 ms: 1.12x slower                                           |
| Geometric mean | (ref)                                                  | 1.02x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.42 ms: 1.10x faster                                           |
| regex_v8       | 26.9 ms                                                | 25.8 ms: 1.04x faster                                           |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                            |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                            |
| tomli_loads          | 2.12 sec                                               | 1.99 sec: 1.06x faster                                          |
| xml_etree_iterparse  | 101 ms                                                 | 98.3 ms: 1.03x faster                                           |
| xml_etree_generate   | 86.8 ms                                                | 84.7 ms: 1.03x faster                                           |
| xml_etree_process    | 60.5 ms                                                | 59.1 ms: 1.02x faster                                           |
| json_loads           | 27.2 us                                                | 27.1 us: 1.00x faster                                           |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                            |
| pickle_pure_python   | 302 us                                                 | 323 us: 1.07x slower                                            |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.12x slower                                           |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                           |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                           |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 50.1 ms: 1.01x faster                                           |
| django_template | 31.7 ms                                                | 32.0 ms: 1.01x slower                                           |
| mako            | 10.7 ms                                                | 11.4 ms: 1.07x slower                                           |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 306 ms: 1.51x faster                                            |
| async_tree_io_tg           | 861 ms                                                 | 587 ms: 1.47x faster                                            |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.39x faster                                            |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                            |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.35x faster                                            |
| deepcopy                   | 354 us                                                 | 263 us: 1.35x faster                                            |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                            |
| deepcopy_memo              | 38.4 us                                                | 31.0 us: 1.24x faster                                           |
| deepcopy_reduce            | 3.24 us                                                | 2.68 us: 1.21x faster                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 483 ms: 1.19x faster                                            |
| go                         | 141 ms                                                 | 119 ms: 1.18x faster                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 461 ms: 1.18x faster                                            |
| pylint                     | 312 ms                                                 | 277 ms: 1.13x faster                                            |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                            |
| regex_effbot               | 3.77 ms                                                | 3.42 ms: 1.10x faster                                           |
| pathlib                    | 17.4 ms                                                | 16.1 ms: 1.08x faster                                           |
| float                      | 78.7 ms                                                | 73.2 ms: 1.07x faster                                           |
| telco                      | 8.40 ms                                                | 7.83 ms: 1.07x faster                                           |
| tomli_loads                | 2.12 sec                                               | 1.99 sec: 1.06x faster                                          |
| richards                   | 47.5 ms                                                | 45.0 ms: 1.06x faster                                           |
| json                       | 5.32 ms                                                | 5.04 ms: 1.06x faster                                           |
| scimark_fft                | 367 ms                                                 | 347 ms: 1.06x faster                                            |
| spectral_norm              | 113 ms                                                 | 107 ms: 1.05x faster                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.79 ms: 1.05x faster                                           |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                            |
| regex_v8                   | 26.9 ms                                                | 25.8 ms: 1.04x faster                                           |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                          |
| richards_super             | 53.7 ms                                                | 51.8 ms: 1.04x faster                                           |
| thrift                     | 800 us                                                 | 771 us: 1.04x faster                                            |
| generators                 | 28.8 ms                                                | 27.8 ms: 1.04x faster                                           |
| sqlglot_normalize          | 108 ms                                                 | 104 ms: 1.04x faster                                            |
| crypto_pyaes               | 74.7 ms                                                | 72.4 ms: 1.03x faster                                           |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                           |
| xml_etree_iterparse        | 101 ms                                                 | 98.3 ms: 1.03x faster                                           |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                           |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                            |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.57 sec: 1.03x faster                                          |
| xml_etree_generate         | 86.8 ms                                                | 84.7 ms: 1.03x faster                                           |
| html5lib                   | 63.4 ms                                                | 61.8 ms: 1.02x faster                                           |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                          |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                            |
| xml_etree_process          | 60.5 ms                                                | 59.1 ms: 1.02x faster                                           |
| pprint_safe_repr           | 727 ms                                                 | 713 ms: 1.02x faster                                            |
| logging_format             | 6.23 us                                                | 6.12 us: 1.02x faster                                           |
| connected_components       | 447 ms                                                 | 439 ms: 1.02x faster                                            |
| logging_simple             | 5.65 us                                                | 5.57 us: 1.02x faster                                           |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.02x faster                                            |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                            |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.01x faster                                          |
| sqlglot_optimize           | 53.4 ms                                                | 52.7 ms: 1.01x faster                                           |
| nqueens                    | 80.9 ms                                                | 79.9 ms: 1.01x faster                                           |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.01x faster                                          |
| async_generators           | 433 ms                                                 | 429 ms: 1.01x faster                                            |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                            |
| genshi_xml                 | 50.5 ms                                                | 50.1 ms: 1.01x faster                                           |
| dulwich_log                | 64.6 ms                                                | 64.2 ms: 1.01x faster                                           |
| json_loads                 | 27.2 us                                                | 27.1 us: 1.00x faster                                           |
| sqlglot_parse              | 1.26 ms                                                | 1.27 ms: 1.00x slower                                           |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                           |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                           |
| coverage                   | 82.8 ms                                                | 83.6 ms: 1.01x slower                                           |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                           |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                           |
| django_template            | 31.7 ms                                                | 32.0 ms: 1.01x slower                                           |
| docutils                   | 2.58 sec                                               | 2.62 sec: 1.01x slower                                          |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                           |
| pyflate                    | 470 ms                                                 | 476 ms: 1.01x slower                                            |
| scimark_sor                | 122 ms                                                 | 124 ms: 1.01x slower                                            |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                            |
| pidigits                   | 186 ms                                                 | 190 ms: 1.02x slower                                            |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                            |
| hexiom                     | 6.08 ms                                                | 6.24 ms: 1.03x slower                                           |
| gc_traversal               | 4.90 ms                                                | 5.03 ms: 1.03x slower                                           |
| deltablue                  | 3.19 ms                                                | 3.29 ms: 1.03x slower                                           |
| mdp                        | 2.54 sec                                               | 2.63 sec: 1.03x slower                                          |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.04x slower                                            |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                           |
| fannkuch                   | 394 ms                                                 | 412 ms: 1.05x slower                                            |
| chaos                      | 58.0 ms                                                | 60.7 ms: 1.05x slower                                           |
| raytrace                   | 262 ms                                                 | 275 ms: 1.05x slower                                            |
| bench_thread_pool          | 818 us                                                 | 864 us: 1.06x slower                                            |
| pickle_pure_python         | 302 us                                                 | 323 us: 1.07x slower                                            |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.07x slower                                           |
| logging_silent             | 101 ns                                                 | 110 ns: 1.09x slower                                            |
| many_optionals             | 857 us                                                 | 950 us: 1.11x slower                                            |
| nbody                      | 87.7 ms                                                | 97.8 ms: 1.12x slower                                           |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.12x slower                                           |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                           |
| bench_mp_pool              | 24.0 ms                                                | 81.8 ms: 3.41x slower                                           |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                    |

Benchmark hidden because not significant (6): shortest_path, sympy_integrate, sympy_expand, genshi_text, asyncio_websockets, scimark_monte_carlo
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.038x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x
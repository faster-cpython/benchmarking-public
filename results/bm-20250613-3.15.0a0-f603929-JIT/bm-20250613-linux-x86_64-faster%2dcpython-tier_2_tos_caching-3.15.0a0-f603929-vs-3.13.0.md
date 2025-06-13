# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: f603929
- commit date: 2025-06-13
- overall geometric mean: 1.034x slower
- HPT reliability: 98.49%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                                          |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                        |
| html5lib       | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                         |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                          |
| async_tree_io              | 838 ms                                                 | 603 ms: 1.39x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 623 ms: 1.38x faster                                                          |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                          |
| coroutines                 | 22.2 ms                                                | 25.9 ms: 1.16x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                  |

Benchmark hidden because not significant (2): asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.9 ms: 1.19x faster                                                         |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                  |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.22 ms: 1.17x faster                                                         |
| regex_v8       | 26.9 ms                                                | 23.4 ms: 1.15x faster                                                         |
| regex_dna      | 220 ms                                                 | 196 ms: 1.12x faster                                                          |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.91 sec: 1.11x faster                                                        |
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.08x faster                                                          |
| xml_etree_process    | 60.5 ms                                                | 56.4 ms: 1.07x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 81.9 ms: 1.06x faster                                                         |
| unpickle_pure_python | 213 us                                                 | 203 us: 1.05x faster                                                          |
| xml_etree_iterparse  | 101 ms                                                 | 99.4 ms: 1.02x faster                                                         |
| json_loads           | 27.2 us                                                | 28.3 us: 1.04x slower                                                         |
| pickle_pure_python   | 302 us                                                 | 325 us: 1.07x slower                                                          |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.08x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                         |
| python_startup_no_site | 7.00 ms                                                | 6.93 ms: 1.01x faster                                                         |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                         |
| genshi_xml      | 50.5 ms                                                | 49.7 ms: 1.02x faster                                                         |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                         |
| django_template | 31.7 ms                                                | 32.7 ms: 1.03x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.06x faster                                                        |
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                          |
| async_tree_io              | 838 ms                                                 | 603 ms: 1.39x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 623 ms: 1.38x faster                                                          |
| deepcopy                   | 354 us                                                 | 258 us: 1.37x faster                                                          |
| richards                   | 47.5 ms                                                | 35.0 ms: 1.36x faster                                                         |
| richards_super             | 53.7 ms                                                | 40.0 ms: 1.35x faster                                                         |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                          |
| deepcopy_memo              | 38.4 us                                                | 29.9 us: 1.29x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                          |
| float                      | 78.7 ms                                                | 65.9 ms: 1.19x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.77 us: 1.17x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 3.22 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                                          |
| regex_v8                   | 26.9 ms                                                | 23.4 ms: 1.15x faster                                                         |
| go                         | 141 ms                                                 | 125 ms: 1.13x faster                                                          |
| regex_dna                  | 220 ms                                                 | 196 ms: 1.12x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                          |
| tomli_loads                | 2.12 sec                                               | 1.91 sec: 1.11x faster                                                        |
| pyflate                    | 470 ms                                                 | 425 ms: 1.10x faster                                                          |
| pylint                     | 312 ms                                                 | 282 ms: 1.10x faster                                                          |
| scimark_fft                | 367 ms                                                 | 336 ms: 1.09x faster                                                          |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.08x faster                                                          |
| xml_etree_process          | 60.5 ms                                                | 56.4 ms: 1.07x faster                                                         |
| telco                      | 8.40 ms                                                | 7.91 ms: 1.06x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 81.9 ms: 1.06x faster                                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.43 sec: 1.06x faster                                                        |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                         |
| dulwich_log                | 64.6 ms                                                | 61.4 ms: 1.05x faster                                                         |
| unpickle_pure_python       | 213 us                                                 | 203 us: 1.05x faster                                                          |
| spectral_norm              | 113 ms                                                 | 109 ms: 1.04x faster                                                          |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                                         |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                                         |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                        |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                                        |
| sympy_integrate            | 19.8 ms                                                | 19.3 ms: 1.03x faster                                                         |
| json                       | 5.32 ms                                                | 5.18 ms: 1.03x faster                                                         |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                          |
| html5lib                   | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                         |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                                          |
| xml_etree_iterparse        | 101 ms                                                 | 99.4 ms: 1.02x faster                                                         |
| genshi_xml                 | 50.5 ms                                                | 49.7 ms: 1.02x faster                                                         |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                        |
| deltablue                  | 3.19 ms                                                | 3.14 ms: 1.02x faster                                                         |
| python_startup_no_site     | 7.00 ms                                                | 6.93 ms: 1.01x faster                                                         |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                          |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                          |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                          |
| scimark_monte_carlo        | 66.8 ms                                                | 67.2 ms: 1.01x slower                                                         |
| shortest_path              | 487 ms                                                 | 497 ms: 1.02x slower                                                          |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                        |
| crypto_pyaes               | 74.7 ms                                                | 76.5 ms: 1.02x slower                                                         |
| sympy_expand               | 456 ms                                                 | 468 ms: 1.03x slower                                                          |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                         |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                          |
| django_template            | 31.7 ms                                                | 32.7 ms: 1.03x slower                                                         |
| gc_traversal               | 4.90 ms                                                | 5.07 ms: 1.04x slower                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.23 ms: 1.04x slower                                                         |
| nqueens                    | 80.9 ms                                                | 84.2 ms: 1.04x slower                                                         |
| json_loads                 | 27.2 us                                                | 28.3 us: 1.04x slower                                                         |
| connected_components       | 447 ms                                                 | 467 ms: 1.04x slower                                                          |
| generators                 | 28.8 ms                                                | 30.2 ms: 1.05x slower                                                         |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.05x slower                                                          |
| raytrace                   | 262 ms                                                 | 276 ms: 1.06x slower                                                          |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                         |
| comprehensions             | 16.5 us                                                | 17.5 us: 1.06x slower                                                         |
| fannkuch                   | 394 ms                                                 | 418 ms: 1.06x slower                                                          |
| hexiom                     | 6.08 ms                                                | 6.52 ms: 1.07x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.07x slower                                                          |
| chaos                      | 58.0 ms                                                | 62.6 ms: 1.08x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.08x slower                                                         |
| logging_simple             | 5.65 us                                                | 6.18 us: 1.09x slower                                                         |
| logging_format             | 6.23 us                                                | 6.88 us: 1.10x slower                                                         |
| many_optionals             | 857 us                                                 | 981 us: 1.14x slower                                                          |
| coroutines                 | 22.2 ms                                                | 25.9 ms: 1.16x slower                                                         |
| pprint_safe_repr           | 727 ms                                                 | 850 ms: 1.17x slower                                                          |
| pprint_pformat             | 1.48 sec                                               | 1.78 sec: 1.21x slower                                                        |
| subparsers                 | 15.5 ms                                                | 23.9 ms: 1.55x slower                                                         |
| logging_silent             | 101 ns                                                 | 480 ns: 4.75x slower                                                          |
| coverage                   | 82.8 ms                                                | 424 ms: 5.12x slower                                                          |
| thrift                     | 800 us                                                 | 148 ms: 185.23x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                                  |

Benchmark hidden because not significant (5): meteor_contest, sympy_str, asyncio_websockets, async_generators, nbody
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250613-3.15.0a0-f603929-JIT/bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.034x slower

# HPT report

- Reliability score: 98.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x
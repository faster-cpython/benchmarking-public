# Results vs. 3.13.0

- fork: faster-cpython
- ref: escaping_decref_1
- machine: linux-x86_64
- commit hash: 74f69b8
- commit date: 2025-01-10
- overall geometric mean: 1.049x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                          |
| html5lib       | 63.4 ms                                                | 61.8 ms: 1.02x faster                                                         |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                  |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 305 ms: 1.52x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 582 ms: 1.48x faster                                                          |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                                          |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 323 ms: 1.35x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 246 ms: 1.30x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 480 ms: 1.19x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 457 ms: 1.19x faster                                                          |
| async_generators           | 433 ms                                                 | 421 ms: 1.03x faster                                                          |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.05x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.6 ms: 1.11x faster                                                         |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                          |
| nbody          | 87.7 ms                                                | 95.7 ms: 1.09x slower                                                         |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.43 ms: 1.10x faster                                                         |
| regex_v8       | 26.9 ms                                                | 25.3 ms: 1.06x faster                                                         |
| regex_compile  | 132 ms                                                 | 126 ms: 1.04x faster                                                          |
| regex_dna      | 220 ms                                                 | 211 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                          |
| tomli_loads          | 2.12 sec                                               | 1.99 sec: 1.06x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 96.4 ms: 1.05x faster                                                         |
| json_loads           | 27.2 us                                                | 26.4 us: 1.03x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 84.7 ms: 1.03x faster                                                         |
| xml_etree_process    | 60.5 ms                                                | 59.2 ms: 1.02x faster                                                         |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                          |
| pickle_pure_python   | 302 us                                                 | 318 us: 1.05x slower                                                          |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                         |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 49.0 ms: 1.03x faster                                                         |
| genshi_text     | 22.6 ms                                                | 22.1 ms: 1.02x faster                                                         |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                         |
| mako            | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-faster%2dcpython-escaping_decref_1-3.14.0a3+-74f69b8 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 305 ms: 1.52x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 582 ms: 1.48x faster                                                          |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                                          |
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                                          |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 323 ms: 1.35x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 246 ms: 1.30x faster                                                          |
| deepcopy_memo              | 38.4 us                                                | 30.8 us: 1.25x faster                                                         |
| go                         | 141 ms                                                 | 116 ms: 1.21x faster                                                          |
| deepcopy_reduce            | 3.24 us                                                | 2.68 us: 1.21x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 480 ms: 1.19x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 457 ms: 1.19x faster                                                          |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                          |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                          |
| float                      | 78.7 ms                                                | 70.6 ms: 1.11x faster                                                         |
| pathlib                    | 17.4 ms                                                | 15.7 ms: 1.11x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 3.43 ms: 1.10x faster                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.59 ms: 1.10x faster                                                         |
| json                       | 5.32 ms                                                | 4.89 ms: 1.09x faster                                                         |
| telco                      | 8.40 ms                                                | 7.72 ms: 1.09x faster                                                         |
| richards                   | 47.5 ms                                                | 44.1 ms: 1.08x faster                                                         |
| scimark_fft                | 367 ms                                                 | 341 ms: 1.08x faster                                                          |
| richards_super             | 53.7 ms                                                | 50.0 ms: 1.08x faster                                                         |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                        |
| spectral_norm              | 113 ms                                                 | 106 ms: 1.07x faster                                                          |
| tomli_loads                | 2.12 sec                                               | 1.99 sec: 1.06x faster                                                        |
| regex_v8                   | 26.9 ms                                                | 25.3 ms: 1.06x faster                                                         |
| crypto_pyaes               | 74.7 ms                                                | 70.8 ms: 1.06x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 96.4 ms: 1.05x faster                                                         |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                          |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.05x faster                                                        |
| regex_compile              | 132 ms                                                 | 126 ms: 1.04x faster                                                          |
| regex_dna                  | 220 ms                                                 | 211 ms: 1.04x faster                                                          |
| generators                 | 28.8 ms                                                | 27.7 ms: 1.04x faster                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                          |
| bpe_tokeniser              | 4.69 sec                                               | 4.53 sec: 1.03x faster                                                        |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                                         |
| sqlglot_normalize          | 108 ms                                                 | 104 ms: 1.03x faster                                                          |
| thrift                     | 800 us                                                 | 774 us: 1.03x faster                                                          |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                          |
| gc_traversal               | 4.90 ms                                                | 4.75 ms: 1.03x faster                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                                         |
| genshi_xml                 | 50.5 ms                                                | 49.0 ms: 1.03x faster                                                         |
| pyflate                    | 470 ms                                                 | 456 ms: 1.03x faster                                                          |
| async_generators           | 433 ms                                                 | 421 ms: 1.03x faster                                                          |
| json_loads                 | 27.2 us                                                | 26.4 us: 1.03x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 84.7 ms: 1.03x faster                                                         |
| html5lib                   | 63.4 ms                                                | 61.8 ms: 1.02x faster                                                         |
| connected_components       | 447 ms                                                 | 437 ms: 1.02x faster                                                          |
| genshi_text                | 22.6 ms                                                | 22.1 ms: 1.02x faster                                                         |
| xml_etree_process          | 60.5 ms                                                | 59.2 ms: 1.02x faster                                                         |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                          |
| shortest_path              | 487 ms                                                 | 477 ms: 1.02x faster                                                          |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                        |
| sympy_str                  | 273 ms                                                 | 268 ms: 1.02x faster                                                          |
| scimark_lu                 | 114 ms                                                 | 113 ms: 1.02x faster                                                          |
| nqueens                    | 80.9 ms                                                | 79.7 ms: 1.01x faster                                                         |
| pprint_safe_repr           | 727 ms                                                 | 717 ms: 1.01x faster                                                          |
| dulwich_log                | 64.6 ms                                                | 63.8 ms: 1.01x faster                                                         |
| sqlglot_optimize           | 53.4 ms                                                | 52.8 ms: 1.01x faster                                                         |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                          |
| logging_simple             | 5.65 us                                                | 5.61 us: 1.01x faster                                                         |
| sqlglot_parse              | 1.26 ms                                                | 1.26 ms: 1.01x faster                                                         |
| pprint_pformat             | 1.48 sec                                               | 1.47 sec: 1.01x faster                                                        |
| sympy_integrate            | 19.8 ms                                                | 19.7 ms: 1.01x faster                                                         |
| sympy_expand               | 456 ms                                                 | 455 ms: 1.00x faster                                                          |
| sqlglot_transpile          | 1.57 ms                                                | 1.57 ms: 1.00x faster                                                         |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                          |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                                         |
| logging_format             | 6.23 us                                                | 6.27 us: 1.01x slower                                                         |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.01x slower                                                         |
| deltablue                  | 3.19 ms                                                | 3.22 ms: 1.01x slower                                                         |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                         |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                         |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                          |
| fannkuch                   | 394 ms                                                 | 400 ms: 1.02x slower                                                          |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                         |
| hexiom                     | 6.08 ms                                                | 6.19 ms: 1.02x slower                                                         |
| coverage                   | 82.8 ms                                                | 85.0 ms: 1.03x slower                                                         |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                                          |
| chaos                      | 58.0 ms                                                | 60.6 ms: 1.04x slower                                                         |
| mdp                        | 2.54 sec                                               | 2.66 sec: 1.05x slower                                                        |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.05x slower                                                         |
| logging_silent             | 101 ns                                                 | 106 ns: 1.05x slower                                                          |
| pickle_pure_python         | 302 us                                                 | 318 us: 1.05x slower                                                          |
| bench_thread_pool          | 818 us                                                 | 860 us: 1.05x slower                                                          |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                         |
| nbody                      | 87.7 ms                                                | 95.7 ms: 1.09x slower                                                         |
| many_optionals             | 857 us                                                 | 946 us: 1.10x slower                                                          |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                         |
| subparsers                 | 15.5 ms                                                | 20.5 ms: 1.33x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                  |

Benchmark hidden because not significant (4): typing_runtime_protocols, docutils, asyncio_websockets, scimark_monte_carlo
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x
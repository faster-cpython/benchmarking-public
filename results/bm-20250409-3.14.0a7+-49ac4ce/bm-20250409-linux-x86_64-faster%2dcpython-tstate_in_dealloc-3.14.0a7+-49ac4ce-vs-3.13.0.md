# Results vs. 3.13.0

- fork: faster-cpython
- ref: tstate_in_dealloc
- machine: linux-x86_64
- commit hash: 49ac4ce
- commit date: 2025-04-09
- overall geometric mean: 1.053x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 252 ms: 1.06x faster                                                          |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                        |
| html5lib       | 63.4 ms                                                | 62.2 ms: 1.02x faster                                                         |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                                          |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                          |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.33x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                                          |
| async_generators           | 433 ms                                                 | 407 ms: 1.06x faster                                                          |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.08x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.3 ms: 1.12x faster                                                         |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                          |
| nbody          | 87.7 ms                                                | 97.1 ms: 1.11x slower                                                         |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.10 ms: 1.21x faster                                                         |
| regex_v8       | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                         |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                          |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                                          |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                          |
| tomli_loads          | 2.12 sec                                               | 2.00 sec: 1.06x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 58.1 ms: 1.04x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 83.5 ms: 1.04x faster                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 97.7 ms: 1.04x faster                                                         |
| unpickle_pure_python | 213 us                                                 | 214 us: 1.00x slower                                                          |
| pickle_pure_python   | 302 us                                                 | 313 us: 1.03x slower                                                          |
| json_loads           | 27.2 us                                                | 30.5 us: 1.12x slower                                                         |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                         |
| python_startup_no_site | 7.00 ms                                                | 8.24 ms: 1.18x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.9 ms: 1.08x faster                                                         |
| genshi_xml      | 50.5 ms                                                | 49.5 ms: 1.02x faster                                                         |
| django_template | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                         |
| mako            | 10.7 ms                                                | 11.3 ms: 1.05x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.06x faster                                                        |
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                          |
| deepcopy                   | 354 us                                                 | 251 us: 1.41x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                                          |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                          |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.33x faster                                                          |
| deepcopy_memo              | 38.4 us                                                | 28.9 us: 1.33x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                          |
| go                         | 141 ms                                                 | 110 ms: 1.28x faster                                                          |
| regex_effbot               | 3.77 ms                                                | 3.10 ms: 1.21x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.21x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                                          |
| regex_v8                   | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                         |
| richards                   | 47.5 ms                                                | 42.4 ms: 1.12x faster                                                         |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                          |
| float                      | 78.7 ms                                                | 70.3 ms: 1.12x faster                                                         |
| pyflate                    | 470 ms                                                 | 425 ms: 1.11x faster                                                          |
| richards_super             | 53.7 ms                                                | 48.7 ms: 1.10x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                          |
| genshi_text                | 22.6 ms                                                | 20.9 ms: 1.08x faster                                                         |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.08x faster                                                        |
| dulwich_log                | 64.6 ms                                                | 60.1 ms: 1.07x faster                                                         |
| async_generators           | 433 ms                                                 | 407 ms: 1.06x faster                                                          |
| tomli_loads                | 2.12 sec                                               | 2.00 sec: 1.06x faster                                                        |
| logging_silent             | 101 ns                                                 | 95.5 ns: 1.06x faster                                                         |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                          |
| spectral_norm              | 113 ms                                                 | 107 ms: 1.06x faster                                                          |
| 2to3                       | 266 ms                                                 | 252 ms: 1.06x faster                                                          |
| regex_dna                  | 220 ms                                                 | 209 ms: 1.05x faster                                                          |
| telco                      | 8.40 ms                                                | 7.98 ms: 1.05x faster                                                         |
| xml_etree_process          | 60.5 ms                                                | 58.1 ms: 1.04x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 83.5 ms: 1.04x faster                                                         |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                                          |
| sympy_integrate            | 19.8 ms                                                | 19.1 ms: 1.04x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 97.7 ms: 1.04x faster                                                         |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.57 sec: 1.03x faster                                                        |
| gc_traversal               | 4.90 ms                                                | 4.79 ms: 1.02x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.84 us: 1.02x faster                                                         |
| html5lib                   | 63.4 ms                                                | 62.2 ms: 1.02x faster                                                         |
| genshi_xml                 | 50.5 ms                                                | 49.5 ms: 1.02x faster                                                         |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                        |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                          |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.02x faster                                                          |
| pprint_safe_repr           | 727 ms                                                 | 717 ms: 1.01x faster                                                          |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.01x faster                                                        |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                          |
| django_template            | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                         |
| chaos                      | 58.0 ms                                                | 57.7 ms: 1.01x faster                                                         |
| hexiom                     | 6.08 ms                                                | 6.05 ms: 1.01x faster                                                         |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                          |
| unpickle_pure_python       | 213 us                                                 | 214 us: 1.00x slower                                                          |
| sympy_expand               | 456 ms                                                 | 459 ms: 1.01x slower                                                          |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                         |
| nqueens                    | 80.9 ms                                                | 81.6 ms: 1.01x slower                                                         |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                        |
| crypto_pyaes               | 74.7 ms                                                | 75.4 ms: 1.01x slower                                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 67.5 ms: 1.01x slower                                                         |
| raytrace                   | 262 ms                                                 | 265 ms: 1.01x slower                                                          |
| typing_runtime_protocols   | 160 us                                                 | 162 us: 1.01x slower                                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.10 ms: 1.01x slower                                                         |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.02x slower                                                         |
| deltablue                  | 3.19 ms                                                | 3.28 ms: 1.03x slower                                                         |
| coverage                   | 82.8 ms                                                | 85.6 ms: 1.03x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 313 us: 1.03x slower                                                          |
| fannkuch                   | 394 ms                                                 | 408 ms: 1.04x slower                                                          |
| generators                 | 28.8 ms                                                | 29.9 ms: 1.04x slower                                                         |
| json                       | 5.32 ms                                                | 5.54 ms: 1.04x slower                                                         |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                         |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.05x slower                                                         |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.08x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 882 us: 1.08x slower                                                          |
| many_optionals             | 857 us                                                 | 932 us: 1.09x slower                                                          |
| nbody                      | 87.7 ms                                                | 97.1 ms: 1.11x slower                                                         |
| json_loads                 | 27.2 us                                                | 30.5 us: 1.12x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                         |
| python_startup_no_site     | 7.00 ms                                                | 8.24 ms: 1.18x slower                                                         |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 82.3 ms: 3.43x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                  |

Benchmark hidden because not significant (9): logging_simple, sqlalchemy_imperative, connected_components, logging_format, scimark_fft, sqlalchemy_declarative, asyncio_websockets, scimark_lu, shortest_path
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250409-3.14.0a7+-49ac4ce/bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x
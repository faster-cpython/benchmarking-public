# Results vs. 3.13.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-x86_64
- commit hash: c84beef
- commit date: 2025-06-23
- overall geometric mean: 1.040x faster
- HPT reliability: 99.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                                            |
| html5lib       | 63.4 ms                                                | 62.5 ms: 1.01x faster                                                           |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                            |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.40x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 638 ms: 1.35x faster                                                            |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.32x faster                                                            |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 508 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 501 ms: 1.08x faster                                                            |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                            |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                            |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.5 ms: 1.08x faster                                                           |
| pidigits       | 186 ms                                                 | 193 ms: 1.03x slower                                                            |
| nbody          | 87.7 ms                                                | 95.5 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.5 ms: 1.14x faster                                                           |
| regex_effbot   | 3.77 ms                                                | 3.33 ms: 1.13x faster                                                           |
| regex_dna      | 220 ms                                                 | 210 ms: 1.05x faster                                                            |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 144 ms: 1.07x faster                                                            |
| tomli_loads          | 2.12 sec                                               | 2.00 sec: 1.06x faster                                                          |
| xml_etree_iterparse  | 101 ms                                                 | 99.6 ms: 1.02x faster                                                           |
| xml_etree_generate   | 86.8 ms                                                | 85.6 ms: 1.01x faster                                                           |
| xml_etree_process    | 60.5 ms                                                | 60.0 ms: 1.01x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 222 us: 1.04x slower                                                            |
| json_loads           | 27.2 us                                                | 28.3 us: 1.04x slower                                                           |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                                            |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                           |
| python_startup_no_site | 7.00 ms                                                | 6.95 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                           |
| genshi_xml      | 50.5 ms                                                | 49.7 ms: 1.02x faster                                                           |
| django_template | 31.7 ms                                                | 32.4 ms: 1.02x slower                                                           |
| mako            | 10.7 ms                                                | 11.5 ms: 1.08x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                            |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.40x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                            |
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 638 ms: 1.35x faster                                                            |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.32x faster                                                            |
| go                         | 141 ms                                                 | 111 ms: 1.27x faster                                                            |
| deepcopy_memo              | 38.4 us                                                | 30.3 us: 1.27x faster                                                           |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                                           |
| regex_v8                   | 26.9 ms                                                | 23.5 ms: 1.14x faster                                                           |
| regex_effbot               | 3.77 ms                                                | 3.33 ms: 1.13x faster                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 508 ms: 1.13x faster                                                            |
| spectral_norm              | 113 ms                                                 | 101 ms: 1.12x faster                                                            |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                                            |
| pyflate                    | 470 ms                                                 | 425 ms: 1.10x faster                                                            |
| richards                   | 47.5 ms                                                | 43.2 ms: 1.10x faster                                                           |
| richards_super             | 53.7 ms                                                | 48.8 ms: 1.10x faster                                                           |
| dulwich_log                | 64.6 ms                                                | 59.0 ms: 1.10x faster                                                           |
| float                      | 78.7 ms                                                | 72.5 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 501 ms: 1.08x faster                                                            |
| xml_etree_parse            | 154 ms                                                 | 144 ms: 1.07x faster                                                            |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                           |
| telco                      | 8.40 ms                                                | 7.90 ms: 1.06x faster                                                           |
| scimark_sor                | 122 ms                                                 | 115 ms: 1.06x faster                                                            |
| tomli_loads                | 2.12 sec                                               | 2.00 sec: 1.06x faster                                                          |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                            |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.06x faster                                                          |
| regex_dna                  | 220 ms                                                 | 210 ms: 1.05x faster                                                            |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                                            |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                                           |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                           |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.54 sec: 1.03x faster                                                          |
| thrift                     | 800 us                                                 | 777 us: 1.03x faster                                                            |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                            |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                          |
| comprehensions             | 16.5 us                                                | 16.1 us: 1.03x faster                                                           |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                          |
| sympy_str                  | 273 ms                                                 | 268 ms: 1.02x faster                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 99.6 ms: 1.02x faster                                                           |
| scimark_monte_carlo        | 66.8 ms                                                | 65.7 ms: 1.02x faster                                                           |
| genshi_xml                 | 50.5 ms                                                | 49.7 ms: 1.02x faster                                                           |
| xml_etree_generate         | 86.8 ms                                                | 85.6 ms: 1.01x faster                                                           |
| scimark_fft                | 367 ms                                                 | 361 ms: 1.01x faster                                                            |
| html5lib                   | 63.4 ms                                                | 62.5 ms: 1.01x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                            |
| json                       | 5.32 ms                                                | 5.27 ms: 1.01x faster                                                           |
| sqlite_synth               | 2.90 us                                                | 2.88 us: 1.01x faster                                                           |
| xml_etree_process          | 60.5 ms                                                | 60.0 ms: 1.01x faster                                                           |
| sympy_expand               | 456 ms                                                 | 453 ms: 1.01x faster                                                            |
| python_startup_no_site     | 7.00 ms                                                | 6.95 ms: 1.01x faster                                                           |
| nqueens                    | 80.9 ms                                                | 81.2 ms: 1.00x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                            |
| hexiom                     | 6.08 ms                                                | 6.11 ms: 1.01x slower                                                           |
| crypto_pyaes               | 74.7 ms                                                | 75.7 ms: 1.01x slower                                                           |
| django_template            | 31.7 ms                                                | 32.4 ms: 1.02x slower                                                           |
| gc_traversal               | 4.90 ms                                                | 5.02 ms: 1.03x slower                                                           |
| raytrace                   | 262 ms                                                 | 268 ms: 1.03x slower                                                            |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                            |
| generators                 | 28.8 ms                                                | 29.7 ms: 1.03x slower                                                           |
| pidigits                   | 186 ms                                                 | 193 ms: 1.03x slower                                                            |
| chaos                      | 58.0 ms                                                | 60.2 ms: 1.04x slower                                                           |
| fannkuch                   | 394 ms                                                 | 408 ms: 1.04x slower                                                            |
| unpickle_pure_python       | 213 us                                                 | 222 us: 1.04x slower                                                            |
| shortest_path              | 487 ms                                                 | 507 ms: 1.04x slower                                                            |
| json_loads                 | 27.2 us                                                | 28.3 us: 1.04x slower                                                           |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.05x slower                                                            |
| coverage                   | 82.8 ms                                                | 87.3 ms: 1.05x slower                                                           |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                           |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                                            |
| connected_components       | 447 ms                                                 | 477 ms: 1.07x slower                                                            |
| mako                       | 10.7 ms                                                | 11.5 ms: 1.08x slower                                                           |
| deltablue                  | 3.19 ms                                                | 3.45 ms: 1.08x slower                                                           |
| nbody                      | 87.7 ms                                                | 95.5 ms: 1.09x slower                                                           |
| logging_simple             | 5.65 us                                                | 6.19 us: 1.10x slower                                                           |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                           |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                           |
| logging_format             | 6.23 us                                                | 6.90 us: 1.11x slower                                                           |
| pprint_safe_repr           | 727 ms                                                 | 807 ms: 1.11x slower                                                            |
| pprint_pformat             | 1.48 sec                                               | 1.65 sec: 1.11x slower                                                          |
| many_optionals             | 857 us                                                 | 966 us: 1.13x slower                                                            |
| subparsers                 | 15.5 ms                                                | 23.9 ms: 1.55x slower                                                           |
| logging_silent             | 101 ns                                                 | 471 ns: 4.66x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (4): djangocms, scimark_sparse_mat_mult, pathlib, docutils
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250623-3.15.0a0-c84beef/bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 99.85% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x
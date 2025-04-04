# Results vs. 3.13.0

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: linux-x86_64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.058x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 249 ms: 1.07x faster                                                   |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.01x slower                                                 |
| html5lib       | 63.4 ms                                                | 60.8 ms: 1.04x faster                                                  |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                   |
| async_tree_io              | 838 ms                                                 | 613 ms: 1.37x faster                                                   |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 480 ms: 1.19x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                                   |
| async_generators           | 433 ms                                                 | 391 ms: 1.11x faster                                                   |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.2 ms: 1.12x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| nbody          | 87.7 ms                                                | 91.3 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.35 ms: 1.12x faster                                                  |
| regex_v8       | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                  |
| regex_compile  | 132 ms                                                 | 124 ms: 1.06x faster                                                   |
| regex_dna      | 220 ms                                                 | 214 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 83.8 ms: 1.04x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 58.9 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 98.9 ms: 1.02x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 313 us: 1.03x slower                                                   |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 8.17 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 48.7 ms: 1.04x faster                                                  |
| django_template | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                  |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.08x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                                   |
| deepcopy                   | 354 us                                                 | 253 us: 1.40x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                   |
| async_tree_io              | 838 ms                                                 | 613 ms: 1.37x faster                                                   |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                   |
| go                         | 141 ms                                                 | 111 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 480 ms: 1.19x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.76 us: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                                   |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.35 ms: 1.12x faster                                                  |
| spectral_norm              | 113 ms                                                 | 101 ms: 1.12x faster                                                   |
| float                      | 78.7 ms                                                | 70.2 ms: 1.12x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                  |
| async_generators           | 433 ms                                                 | 391 ms: 1.11x faster                                                   |
| richards                   | 47.5 ms                                                | 43.0 ms: 1.10x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                 |
| richards_super             | 53.7 ms                                                | 49.3 ms: 1.09x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 59.5 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.64 ms: 1.08x faster                                                  |
| scimark_fft                | 367 ms                                                 | 340 ms: 1.08x faster                                                   |
| telco                      | 8.40 ms                                                | 7.80 ms: 1.08x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                 |
| logging_silent             | 101 ns                                                 | 94.4 ns: 1.07x faster                                                  |
| 2to3                       | 266 ms                                                 | 249 ms: 1.07x faster                                                   |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                  |
| scimark_sor                | 122 ms                                                 | 115 ms: 1.07x faster                                                   |
| regex_compile              | 132 ms                                                 | 124 ms: 1.06x faster                                                   |
| pyflate                    | 470 ms                                                 | 445 ms: 1.06x faster                                                   |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                                  |
| html5lib                   | 63.4 ms                                                | 60.8 ms: 1.04x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.51 sec: 1.04x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 48.7 ms: 1.04x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 83.8 ms: 1.04x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 58.9 ms: 1.03x faster                                                  |
| chaos                      | 58.0 ms                                                | 56.5 ms: 1.03x faster                                                  |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.03x faster                                                   |
| logging_simple             | 5.65 us                                                | 5.51 us: 1.03x faster                                                  |
| regex_dna                  | 220 ms                                                 | 214 ms: 1.03x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 98.9 ms: 1.02x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 73.0 ms: 1.02x faster                                                  |
| sympy_str                  | 273 ms                                                 | 268 ms: 1.02x faster                                                   |
| logging_format             | 6.23 us                                                | 6.12 us: 1.02x faster                                                  |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| raytrace                   | 262 ms                                                 | 258 ms: 1.01x faster                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 66.2 ms: 1.01x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.01x faster                                                   |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.00x faster                                                   |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| sympy_expand               | 456 ms                                                 | 457 ms: 1.00x slower                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.01x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.01x slower                                                 |
| django_template            | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                  |
| nqueens                    | 80.9 ms                                                | 81.7 ms: 1.01x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.14 ms: 1.01x slower                                                  |
| connected_components       | 447 ms                                                 | 453 ms: 1.01x slower                                                   |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                   |
| shortest_path              | 487 ms                                                 | 495 ms: 1.02x slower                                                   |
| coverage                   | 82.8 ms                                                | 84.4 ms: 1.02x slower                                                  |
| comprehensions             | 16.5 us                                                | 16.9 us: 1.02x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 5.02 ms: 1.03x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.03x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.03x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 313 us: 1.03x slower                                                   |
| deltablue                  | 3.19 ms                                                | 3.31 ms: 1.04x slower                                                  |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                  |
| generators                 | 28.8 ms                                                | 29.9 ms: 1.04x slower                                                  |
| nbody                      | 87.7 ms                                                | 91.3 ms: 1.04x slower                                                  |
| fannkuch                   | 394 ms                                                 | 413 ms: 1.05x slower                                                   |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 877 us: 1.07x slower                                                   |
| many_optionals             | 857 us                                                 | 933 us: 1.09x slower                                                   |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.11x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 8.17 ms: 1.17x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.41x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (5): pprint_safe_repr, pprint_pformat, sqlalchemy_imperative, json, asyncio_websockets
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250403-3.14.0a6+-275056a/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.058x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x
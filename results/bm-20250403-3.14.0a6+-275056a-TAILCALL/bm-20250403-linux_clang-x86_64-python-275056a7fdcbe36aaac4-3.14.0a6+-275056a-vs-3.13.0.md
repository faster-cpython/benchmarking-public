# Results vs. 3.13.0

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: linux-x86_64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.090x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 244 ms: 1.09x faster                                                   |
| docutils       | 2.58 sec                                               | 2.56 sec: 1.01x faster                                                 |
| html5lib       | 63.4 ms                                                | 57.7 ms: 1.10x faster                                                  |
| sphinx         | 1.03 sec                                               | 985 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 304 ms: 1.44x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 608 ms: 1.41x faster                                                   |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                                   |
| async_tree_none            | 350 ms                                                 | 253 ms: 1.39x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 243 ms: 1.31x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 483 ms: 1.19x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 480 ms: 1.13x faster                                                   |
| async_generators           | 433 ms                                                 | 383 ms: 1.13x faster                                                   |
| coroutines                 | 22.2 ms                                                | 21.5 ms: 1.03x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.26x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.6 ms: 1.16x faster                                                  |
| nbody          | 87.7 ms                                                | 83.5 ms: 1.05x faster                                                  |
| pidigits       | 186 ms                                                 | 201 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.08 ms: 1.22x faster                                                  |
| regex_v8       | 26.9 ms                                                | 22.7 ms: 1.19x faster                                                  |
| regex_dna      | 220 ms                                                 | 188 ms: 1.17x faster                                                   |
| regex_compile  | 132 ms                                                 | 124 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 59.2 ms: 1.02x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 210 us: 1.01x faster                                                   |
| xml_etree_generate   | 86.8 ms                                                | 86.1 ms: 1.01x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 103 ms: 1.01x slower                                                   |
| xml_etree_parse      | 154 ms                                                 | 162 ms: 1.05x slower                                                   |
| json_loads           | 27.2 us                                                | 29.0 us: 1.07x slower                                                  |
| json_dumps           | 10.1 ms                                                | 12.5 ms: 1.23x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 8.07 ms: 1.15x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.4 ms: 1.11x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 47.3 ms: 1.07x faster                                                  |
| django_template | 31.7 ms                                                | 31.8 ms: 1.01x slower                                                  |
| mako            | 10.7 ms                                                | 11.7 ms: 1.10x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.20 sec: 2.13x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                                   |
| deepcopy                   | 354 us                                                 | 243 us: 1.46x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 304 ms: 1.44x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 608 ms: 1.41x faster                                                   |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                                   |
| async_tree_none            | 350 ms                                                 | 253 ms: 1.39x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 28.2 us: 1.36x faster                                                  |
| go                         | 141 ms                                                 | 106 ms: 1.32x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 243 ms: 1.31x faster                                                   |
| spectral_norm              | 113 ms                                                 | 87.5 ms: 1.29x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.53 us: 1.28x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 3.96 ms: 1.27x faster                                                  |
| scimark_fft                | 367 ms                                                 | 296 ms: 1.24x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.08 ms: 1.22x faster                                                  |
| richards                   | 47.5 ms                                                | 39.8 ms: 1.19x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 22.7 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 483 ms: 1.19x faster                                                   |
| regex_dna                  | 220 ms                                                 | 188 ms: 1.17x faster                                                   |
| richards_super             | 53.7 ms                                                | 46.0 ms: 1.17x faster                                                  |
| pathlib                    | 17.4 ms                                                | 14.9 ms: 1.17x faster                                                  |
| float                      | 78.7 ms                                                | 67.6 ms: 1.16x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                 |
| pyflate                    | 470 ms                                                 | 410 ms: 1.15x faster                                                   |
| scimark_sor                | 122 ms                                                 | 107 ms: 1.15x faster                                                   |
| pylint                     | 312 ms                                                 | 272 ms: 1.15x faster                                                   |
| logging_silent             | 101 ns                                                 | 88.8 ns: 1.14x faster                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 58.8 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 480 ms: 1.13x faster                                                   |
| async_generators           | 433 ms                                                 | 383 ms: 1.13x faster                                                   |
| telco                      | 8.40 ms                                                | 7.50 ms: 1.12x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 57.8 ms: 1.12x faster                                                  |
| genshi_text                | 22.6 ms                                                | 20.4 ms: 1.11x faster                                                  |
| html5lib                   | 63.4 ms                                                | 57.7 ms: 1.10x faster                                                  |
| deltablue                  | 3.19 ms                                                | 2.92 ms: 1.09x faster                                                  |
| 2to3                       | 266 ms                                                 | 244 ms: 1.09x faster                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.32 sec: 1.09x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.68 us: 1.08x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 18.4 ms: 1.08x faster                                                  |
| chaos                      | 58.0 ms                                                | 53.9 ms: 1.08x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 47.3 ms: 1.07x faster                                                  |
| regex_compile              | 132 ms                                                 | 124 ms: 1.07x faster                                                   |
| crypto_pyaes               | 74.7 ms                                                | 71.0 ms: 1.05x faster                                                  |
| raytrace                   | 262 ms                                                 | 249 ms: 1.05x faster                                                   |
| hexiom                     | 6.08 ms                                                | 5.79 ms: 1.05x faster                                                  |
| nbody                      | 87.7 ms                                                | 83.5 ms: 1.05x faster                                                  |
| sphinx                     | 1.03 sec                                               | 985 ms: 1.05x faster                                                   |
| sympy_str                  | 273 ms                                                 | 261 ms: 1.05x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.04x faster                                                   |
| typing_runtime_protocols   | 160 us                                                 | 154 us: 1.04x faster                                                   |
| sympy_sum                  | 150 ms                                                 | 145 ms: 1.04x faster                                                   |
| logging_format             | 6.23 us                                                | 5.99 us: 1.04x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.46 us: 1.04x faster                                                  |
| comprehensions             | 16.5 us                                                | 16.0 us: 1.03x faster                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                                  |
| coroutines                 | 22.2 ms                                                | 21.5 ms: 1.03x faster                                                  |
| nqueens                    | 80.9 ms                                                | 78.7 ms: 1.03x faster                                                  |
| scimark_lu                 | 114 ms                                                 | 111 ms: 1.03x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.02x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 59.2 ms: 1.02x faster                                                  |
| coverage                   | 82.8 ms                                                | 81.1 ms: 1.02x faster                                                  |
| generators                 | 28.8 ms                                                | 28.3 ms: 1.02x faster                                                  |
| sympy_expand               | 456 ms                                                 | 448 ms: 1.02x faster                                                   |
| unpickle_pure_python       | 213 us                                                 | 210 us: 1.01x faster                                                   |
| docutils                   | 2.58 sec                                               | 2.56 sec: 1.01x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 86.1 ms: 1.01x faster                                                  |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                   |
| django_template            | 31.7 ms                                                | 31.8 ms: 1.01x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 4.94 ms: 1.01x slower                                                  |
| fannkuch                   | 394 ms                                                 | 398 ms: 1.01x slower                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 103 ms: 1.01x slower                                                   |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.50 ms: 1.02x slower                                                  |
| shortest_path              | 487 ms                                                 | 499 ms: 1.02x slower                                                   |
| pprint_safe_repr           | 727 ms                                                 | 745 ms: 1.03x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.52 sec: 1.03x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 842 us: 1.03x slower                                                   |
| connected_components       | 447 ms                                                 | 462 ms: 1.03x slower                                                   |
| xml_etree_parse            | 154 ms                                                 | 162 ms: 1.05x slower                                                   |
| many_optionals             | 857 us                                                 | 906 us: 1.06x slower                                                   |
| json_loads                 | 27.2 us                                                | 29.0 us: 1.07x slower                                                  |
| pidigits                   | 186 ms                                                 | 201 ms: 1.08x slower                                                   |
| mako                       | 10.7 ms                                                | 11.7 ms: 1.10x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 8.07 ms: 1.15x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 12.5 ms: 1.23x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.4 ms: 1.32x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 80.4 ms: 3.35x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (3): json, asyncio_websockets, pickle_pure_python
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250403-3.14.0a6+-275056a-CLANG/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.090x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.04x
# Results vs. 3.13.0

- fork: iritkatriel
- ref: stats
- machine: linux-x86_64
- commit hash: fb33c24
- commit date: 2025-02-21
- overall geometric mean: 1.050x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                         |
| html5lib       | 63.4 ms                                                | 60.6 ms: 1.05x faster                                        |
| sphinx         | 1.03 sec                                               | 999 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.38x faster                                         |
| async_tree_io              | 838 ms                                                 | 608 ms: 1.38x faster                                         |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 326 ms: 1.34x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 484 ms: 1.18x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 471 ms: 1.15x faster                                         |
| async_generators           | 433 ms                                                 | 384 ms: 1.13x faster                                         |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.03x slower                                        |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.6 ms: 1.13x faster                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| nbody          | 87.7 ms                                                | 90.3 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.37 ms: 1.12x faster                                        |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                         |
| regex_v8       | 26.9 ms                                                | 25.6 ms: 1.05x faster                                        |
| regex_dna      | 220 ms                                                 | 213 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.90 sec: 1.11x faster                                       |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                         |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                        |
| xml_etree_generate   | 86.8 ms                                                | 84.5 ms: 1.03x faster                                        |
| xml_etree_process    | 60.5 ms                                                | 59.1 ms: 1.02x faster                                        |
| unpickle_pure_python | 213 us                                                 | 221 us: 1.04x slower                                         |
| pickle_pure_python   | 302 us                                                 | 316 us: 1.05x slower                                         |
| json_loads           | 27.2 us                                                | 29.7 us: 1.10x slower                                        |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.12x slower                                        |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.05 ms: 1.01x slower                                        |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                        |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 21.2 ms: 1.07x faster                                        |
| genshi_xml     | 50.5 ms                                                | 48.3 ms: 1.05x faster                                        |
| mako           | 10.7 ms                                                | 10.8 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                         |
| deepcopy                   | 354 us                                                 | 254 us: 1.39x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.38x faster                                         |
| async_tree_io              | 838 ms                                                 | 608 ms: 1.38x faster                                         |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 326 ms: 1.34x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                         |
| deepcopy_memo              | 38.4 us                                                | 29.8 us: 1.29x faster                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.22x faster                                        |
| go                         | 141 ms                                                 | 116 ms: 1.21x faster                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 484 ms: 1.18x faster                                         |
| spectral_norm              | 113 ms                                                 | 96.9 ms: 1.17x faster                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 471 ms: 1.15x faster                                         |
| pylint                     | 312 ms                                                 | 272 ms: 1.14x faster                                         |
| float                      | 78.7 ms                                                | 69.6 ms: 1.13x faster                                        |
| async_generators           | 433 ms                                                 | 384 ms: 1.13x faster                                         |
| regex_effbot               | 3.77 ms                                                | 3.37 ms: 1.12x faster                                        |
| tomli_loads                | 2.12 sec                                               | 1.90 sec: 1.11x faster                                       |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                         |
| richards                   | 47.5 ms                                                | 44.1 ms: 1.08x faster                                        |
| scimark_fft                | 367 ms                                                 | 341 ms: 1.08x faster                                         |
| telco                      | 8.40 ms                                                | 7.82 ms: 1.07x faster                                        |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.07x faster                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.40 sec: 1.06x faster                                       |
| richards_super             | 53.7 ms                                                | 50.5 ms: 1.06x faster                                        |
| thrift                     | 800 us                                                 | 754 us: 1.06x faster                                         |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                         |
| sqlite_synth               | 2.90 us                                                | 2.76 us: 1.05x faster                                        |
| regex_v8                   | 26.9 ms                                                | 25.6 ms: 1.05x faster                                        |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.80 ms: 1.05x faster                                        |
| html5lib                   | 63.4 ms                                                | 60.6 ms: 1.05x faster                                        |
| genshi_xml                 | 50.5 ms                                                | 48.3 ms: 1.05x faster                                        |
| pyflate                    | 470 ms                                                 | 450 ms: 1.04x faster                                         |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                       |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                        |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                         |
| crypto_pyaes               | 74.7 ms                                                | 72.0 ms: 1.04x faster                                        |
| sqlglot_normalize          | 108 ms                                                 | 104 ms: 1.04x faster                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.3 ms: 1.04x faster                                        |
| sympy_str                  | 273 ms                                                 | 264 ms: 1.03x faster                                         |
| regex_dna                  | 220 ms                                                 | 213 ms: 1.03x faster                                         |
| sphinx                     | 1.03 sec                                               | 999 ms: 1.03x faster                                         |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                        |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                       |
| logging_simple             | 5.65 us                                                | 5.49 us: 1.03x faster                                        |
| generators                 | 28.8 ms                                                | 28.0 ms: 1.03x faster                                        |
| shortest_path              | 487 ms                                                 | 474 ms: 1.03x faster                                         |
| xml_etree_generate         | 86.8 ms                                                | 84.5 ms: 1.03x faster                                        |
| mdp                        | 2.54 sec                                               | 2.48 sec: 1.03x faster                                       |
| xml_etree_process          | 60.5 ms                                                | 59.1 ms: 1.02x faster                                        |
| sqlglot_optimize           | 53.4 ms                                                | 52.2 ms: 1.02x faster                                        |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                         |
| pprint_safe_repr           | 727 ms                                                 | 712 ms: 1.02x faster                                         |
| connected_components       | 447 ms                                                 | 438 ms: 1.02x faster                                         |
| typing_runtime_protocols   | 160 us                                                 | 157 us: 1.02x faster                                         |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                         |
| pprint_pformat             | 1.48 sec                                               | 1.45 sec: 1.02x faster                                       |
| logging_format             | 6.23 us                                                | 6.13 us: 1.02x faster                                        |
| sympy_expand               | 456 ms                                                 | 450 ms: 1.01x faster                                         |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                        |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                         |
| sqlglot_parse              | 1.26 ms                                                | 1.26 ms: 1.00x faster                                        |
| deltablue                  | 3.19 ms                                                | 3.18 ms: 1.00x faster                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.57 ms: 1.00x faster                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| hexiom                     | 6.08 ms                                                | 6.09 ms: 1.00x slower                                        |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.00x slower                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.01x slower                                        |
| python_startup_no_site     | 7.00 ms                                                | 7.05 ms: 1.01x slower                                        |
| mako                       | 10.7 ms                                                | 10.8 ms: 1.01x slower                                        |
| logging_silent             | 101 ns                                                 | 102 ns: 1.01x slower                                         |
| gc_traversal               | 4.90 ms                                                | 4.96 ms: 1.01x slower                                        |
| chaos                      | 58.0 ms                                                | 58.9 ms: 1.02x slower                                        |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 68.1 ms: 1.02x slower                                        |
| fannkuch                   | 394 ms                                                 | 402 ms: 1.02x slower                                         |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.03x slower                                         |
| nbody                      | 87.7 ms                                                | 90.3 ms: 1.03x slower                                        |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.03x slower                                        |
| unpickle_pure_python       | 213 us                                                 | 221 us: 1.04x slower                                         |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                         |
| pickle_pure_python         | 302 us                                                 | 316 us: 1.05x slower                                         |
| bench_thread_pool          | 818 us                                                 | 863 us: 1.06x slower                                         |
| coverage                   | 82.8 ms                                                | 89.5 ms: 1.08x slower                                        |
| many_optionals             | 857 us                                                 | 937 us: 1.09x slower                                         |
| json_loads                 | 27.2 us                                                | 29.7 us: 1.10x slower                                        |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.12x slower                                        |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.41x slower                                        |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                 |

Benchmark hidden because not significant (6): django_template, dulwich_log, docutils, asyncio_websockets, nqueens, json
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.050x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x
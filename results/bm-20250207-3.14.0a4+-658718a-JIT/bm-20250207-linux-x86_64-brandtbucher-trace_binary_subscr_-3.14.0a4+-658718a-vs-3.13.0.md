# Results vs. 3.13.0

- fork: brandtbucher
- ref: trace_binary_subscr_
- machine: linux-x86_64
- commit hash: 658718a
- commit date: 2025-02-07
- overall geometric mean: 1.043x faster
- HPT reliability: 99.81%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                                         |
| docutils       | 2.58 sec                                               | 2.71 sec: 1.05x slower                                                       |
| html5lib       | 63.4 ms                                                | 61.6 ms: 1.03x faster                                                        |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 625 ms: 1.38x faster                                                         |
| async_tree_io              | 838 ms                                                 | 624 ms: 1.34x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 327 ms: 1.33x faster                                                         |
| async_tree_none            | 350 ms                                                 | 270 ms: 1.30x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 258 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 501 ms: 1.14x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 491 ms: 1.11x faster                                                         |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                                         |
| coroutines                 | 22.2 ms                                                | 22.8 ms: 1.03x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.0 ms: 1.11x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| nbody          | 87.7 ms                                                | 96.7 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 2.99 ms: 1.26x faster                                                        |
| regex_v8       | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                        |
| regex_dna      | 220 ms                                                 | 199 ms: 1.11x faster                                                         |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                       |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 79.5 ms: 1.09x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 55.8 ms: 1.08x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 200 us: 1.07x faster                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 95.5 ms: 1.06x faster                                                        |
| pickle_pure_python   | 302 us                                                 | 318 us: 1.05x slower                                                         |
| json_loads           | 27.2 us                                                | 28.9 us: 1.06x slower                                                        |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                        |
| python_startup_no_site | 7.00 ms                                                | 7.07 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.2 ms: 1.05x faster                                                        |
| genshi_text     | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                        |
| genshi_xml      | 50.5 ms                                                | 50.2 ms: 1.01x faster                                                        |
| django_template | 31.7 ms                                                | 32.1 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 625 ms: 1.38x faster                                                         |
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                                         |
| async_tree_io              | 838 ms                                                 | 624 ms: 1.34x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 327 ms: 1.33x faster                                                         |
| async_tree_none            | 350 ms                                                 | 270 ms: 1.30x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 2.99 ms: 1.26x faster                                                        |
| deepcopy_memo              | 38.4 us                                                | 30.8 us: 1.25x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 258 ms: 1.24x faster                                                         |
| spectral_norm              | 113 ms                                                 | 93.4 ms: 1.21x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.21x faster                                                        |
| go                         | 141 ms                                                 | 120 ms: 1.17x faster                                                         |
| scimark_fft                | 367 ms                                                 | 313 ms: 1.17x faster                                                         |
| tomli_loads                | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 501 ms: 1.14x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                        |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                         |
| float                      | 78.7 ms                                                | 71.0 ms: 1.11x faster                                                        |
| regex_dna                  | 220 ms                                                 | 199 ms: 1.11x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 491 ms: 1.11x faster                                                         |
| telco                      | 8.40 ms                                                | 7.68 ms: 1.09x faster                                                        |
| xml_etree_generate         | 86.8 ms                                                | 79.5 ms: 1.09x faster                                                        |
| pathlib                    | 17.4 ms                                                | 15.9 ms: 1.09x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.63 ms: 1.09x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 55.8 ms: 1.08x faster                                                        |
| richards                   | 47.5 ms                                                | 44.2 ms: 1.08x faster                                                        |
| pyflate                    | 470 ms                                                 | 439 ms: 1.07x faster                                                         |
| crypto_pyaes               | 74.7 ms                                                | 69.8 ms: 1.07x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.39 sec: 1.07x faster                                                       |
| richards_super             | 53.7 ms                                                | 50.4 ms: 1.07x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 200 us: 1.07x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.73 us: 1.06x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 95.5 ms: 1.06x faster                                                        |
| mako                       | 10.7 ms                                                | 10.2 ms: 1.05x faster                                                        |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                                         |
| thrift                     | 800 us                                                 | 767 us: 1.04x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                       |
| genshi_text                | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                        |
| logging_simple             | 5.65 us                                                | 5.47 us: 1.03x faster                                                        |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| json                       | 5.32 ms                                                | 5.17 ms: 1.03x faster                                                        |
| html5lib                   | 63.4 ms                                                | 61.6 ms: 1.03x faster                                                        |
| gc_traversal               | 4.90 ms                                                | 4.77 ms: 1.03x faster                                                        |
| generators                 | 28.8 ms                                                | 28.1 ms: 1.02x faster                                                        |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                       |
| logging_format             | 6.23 us                                                | 6.10 us: 1.02x faster                                                        |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                                         |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                         |
| connected_components       | 447 ms                                                 | 440 ms: 1.02x faster                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                                         |
| shortest_path              | 487 ms                                                 | 483 ms: 1.01x faster                                                         |
| genshi_xml                 | 50.5 ms                                                | 50.2 ms: 1.01x faster                                                        |
| fannkuch                   | 394 ms                                                 | 392 ms: 1.00x faster                                                         |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| sqlglot_parse              | 1.26 ms                                                | 1.27 ms: 1.00x slower                                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.00x slower                                                         |
| mdp                        | 2.54 sec                                               | 2.56 sec: 1.01x slower                                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                        |
| sympy_str                  | 273 ms                                                 | 275 ms: 1.01x slower                                                         |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                        |
| python_startup_no_site     | 7.00 ms                                                | 7.07 ms: 1.01x slower                                                        |
| chaos                      | 58.0 ms                                                | 58.7 ms: 1.01x slower                                                        |
| sqlglot_optimize           | 53.4 ms                                                | 54.1 ms: 1.01x slower                                                        |
| django_template            | 31.7 ms                                                | 32.1 ms: 1.02x slower                                                        |
| sympy_integrate            | 19.8 ms                                                | 20.2 ms: 1.02x slower                                                        |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                                         |
| dulwich_log                | 64.6 ms                                                | 66.0 ms: 1.02x slower                                                        |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.02x slower                                                         |
| coroutines                 | 22.2 ms                                                | 22.8 ms: 1.03x slower                                                        |
| pprint_safe_repr           | 727 ms                                                 | 750 ms: 1.03x slower                                                         |
| deltablue                  | 3.19 ms                                                | 3.31 ms: 1.04x slower                                                        |
| sympy_expand               | 456 ms                                                 | 473 ms: 1.04x slower                                                         |
| pprint_pformat             | 1.48 sec                                               | 1.54 sec: 1.04x slower                                                       |
| docutils                   | 2.58 sec                                               | 2.71 sec: 1.05x slower                                                       |
| pickle_pure_python         | 302 us                                                 | 318 us: 1.05x slower                                                         |
| raytrace                   | 262 ms                                                 | 276 ms: 1.05x slower                                                         |
| json_loads                 | 27.2 us                                                | 28.9 us: 1.06x slower                                                        |
| comprehensions             | 16.5 us                                                | 17.6 us: 1.07x slower                                                        |
| bench_thread_pool          | 818 us                                                 | 884 us: 1.08x slower                                                         |
| coverage                   | 82.8 ms                                                | 90.0 ms: 1.09x slower                                                        |
| hexiom                     | 6.08 ms                                                | 6.66 ms: 1.10x slower                                                        |
| logging_silent             | 101 ns                                                 | 111 ns: 1.10x slower                                                         |
| nbody                      | 87.7 ms                                                | 96.7 ms: 1.10x slower                                                        |
| many_optionals             | 857 us                                                 | 951 us: 1.11x slower                                                         |
| nqueens                    | 80.9 ms                                                | 91.1 ms: 1.13x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                        |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.33x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 80.7 ms: 3.36x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (6): scimark_monte_carlo, sqlglot_normalize, meteor_contest, sqlalchemy_imperative, asyncio_websockets, pycparser
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 99.81% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
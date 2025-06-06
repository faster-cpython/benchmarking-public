# Results vs. 3.13.0

- fork: iritkatriel
- ref: subscr_stats
- machine: linux-x86_64
- commit hash: ebd800a
- commit date: 2025-04-03
- overall geometric mean: 1.050x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                                |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.00x slower                                              |
| html5lib       | 63.4 ms                                                | 61.9 ms: 1.02x faster                                               |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 486 ms: 1.18x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 475 ms: 1.14x faster                                                |
| async_generators           | 433 ms                                                 | 392 ms: 1.11x faster                                                |
| coroutines                 | 22.2 ms                                                | 24.3 ms: 1.09x slower                                               |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.4 ms: 1.12x faster                                               |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                |
| nbody          | 87.7 ms                                                | 96.6 ms: 1.10x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.8 ms: 1.18x faster                                               |
| regex_dna      | 220 ms                                                 | 207 ms: 1.06x faster                                                |
| regex_compile  | 132 ms                                                 | 126 ms: 1.04x faster                                                |
| regex_effbot   | 3.77 ms                                                | 3.76 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.10x faster                                                |
| tomli_loads          | 2.12 sec                                               | 1.97 sec: 1.07x faster                                              |
| xml_etree_process    | 60.5 ms                                                | 58.9 ms: 1.03x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 98.6 ms: 1.03x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 84.8 ms: 1.02x faster                                               |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                                |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.07x slower                                                |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.15x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                               |
| python_startup_no_site | 7.00 ms                                                | 8.17 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.3 ms: 1.06x faster                                               |
| genshi_xml      | 50.5 ms                                                | 49.5 ms: 1.02x faster                                               |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                               |
| mako            | 10.7 ms                                                | 11.4 ms: 1.07x slower                                               |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.08x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                                |
| deepcopy                   | 354 us                                                 | 255 us: 1.39x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 29.8 us: 1.29x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                |
| go                         | 141 ms                                                 | 114 ms: 1.24x faster                                                |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                               |
| regex_v8                   | 26.9 ms                                                | 22.8 ms: 1.18x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 486 ms: 1.18x faster                                                |
| spectral_norm              | 113 ms                                                 | 97.7 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 475 ms: 1.14x faster                                                |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                |
| float                      | 78.7 ms                                                | 70.4 ms: 1.12x faster                                               |
| dulwich_log                | 64.6 ms                                                | 58.1 ms: 1.11x faster                                               |
| async_generators           | 433 ms                                                 | 392 ms: 1.11x faster                                                |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.10x faster                                                |
| richards                   | 47.5 ms                                                | 44.2 ms: 1.08x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.97 sec: 1.07x faster                                              |
| telco                      | 8.40 ms                                                | 7.86 ms: 1.07x faster                                               |
| richards_super             | 53.7 ms                                                | 50.3 ms: 1.07x faster                                               |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                               |
| regex_dna                  | 220 ms                                                 | 207 ms: 1.06x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                              |
| scimark_fft                | 367 ms                                                 | 346 ms: 1.06x faster                                                |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.77 ms: 1.05x faster                                               |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.76 us: 1.05x faster                                               |
| regex_compile              | 132 ms                                                 | 126 ms: 1.04x faster                                                |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                                |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 19.1 ms: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                              |
| xml_etree_process          | 60.5 ms                                                | 58.9 ms: 1.03x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 98.6 ms: 1.03x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 84.8 ms: 1.02x faster                                               |
| html5lib                   | 63.4 ms                                                | 61.9 ms: 1.02x faster                                               |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.59 sec: 1.02x faster                                              |
| genshi_xml                 | 50.5 ms                                                | 49.5 ms: 1.02x faster                                               |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                              |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                                |
| gc_traversal               | 4.90 ms                                                | 4.82 ms: 1.02x faster                                               |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                               |
| crypto_pyaes               | 74.7 ms                                                | 73.8 ms: 1.01x faster                                               |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                |
| json                       | 5.32 ms                                                | 5.27 ms: 1.01x faster                                               |
| deltablue                  | 3.19 ms                                                | 3.16 ms: 1.01x faster                                               |
| generators                 | 28.8 ms                                                | 28.6 ms: 1.01x faster                                               |
| logging_simple             | 5.65 us                                                | 5.62 us: 1.01x faster                                               |
| pyflate                    | 470 ms                                                 | 468 ms: 1.00x faster                                                |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                |
| regex_effbot               | 3.77 ms                                                | 3.76 ms: 1.00x faster                                               |
| sympy_expand               | 456 ms                                                 | 458 ms: 1.00x slower                                                |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.00x slower                                              |
| scimark_monte_carlo        | 66.8 ms                                                | 67.2 ms: 1.01x slower                                               |
| raytrace                   | 262 ms                                                 | 265 ms: 1.01x slower                                                |
| connected_components       | 447 ms                                                 | 454 ms: 1.02x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                               |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                                |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                               |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                               |
| pprint_pformat             | 1.48 sec                                               | 1.51 sec: 1.02x slower                                              |
| coverage                   | 82.8 ms                                                | 84.5 ms: 1.02x slower                                               |
| pprint_safe_repr           | 727 ms                                                 | 742 ms: 1.02x slower                                                |
| shortest_path              | 487 ms                                                 | 497 ms: 1.02x slower                                                |
| nqueens                    | 80.9 ms                                                | 82.8 ms: 1.02x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.03x slower                                                |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                                |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.33 ms: 1.04x slower                                               |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.07x slower                                               |
| bench_thread_pool          | 818 us                                                 | 871 us: 1.07x slower                                                |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.07x slower                                                |
| fannkuch                   | 394 ms                                                 | 426 ms: 1.08x slower                                                |
| coroutines                 | 22.2 ms                                                | 24.3 ms: 1.09x slower                                               |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                               |
| nbody                      | 87.7 ms                                                | 96.6 ms: 1.10x slower                                               |
| many_optionals             | 857 us                                                 | 948 us: 1.11x slower                                                |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.15x slower                                               |
| python_startup_no_site     | 7.00 ms                                                | 8.17 ms: 1.17x slower                                               |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.46x slower                                               |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (4): logging_silent, chaos, logging_format, asyncio_websockets
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250403-3.14.0a6+-ebd800a/bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.050x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x
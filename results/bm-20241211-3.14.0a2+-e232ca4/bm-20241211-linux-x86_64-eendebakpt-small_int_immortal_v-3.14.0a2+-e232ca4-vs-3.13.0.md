# Results vs. 3.13.0

- fork: eendebakpt
- ref: small_int_immortal_v
- machine: linux-x86_64
- commit hash: e232ca4
- commit date: 2024-12-11
- overall geometric mean: 1.028x faster
- HPT reliability: 99.71%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                                       |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 631 ms: 1.36x faster                                                       |
| async_tree_io              | 838 ms                                                 | 626 ms: 1.34x faster                                                       |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 339 ms: 1.29x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 507 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 489 ms: 1.11x faster                                                       |
| async_generators           | 433 ms                                                 | 421 ms: 1.03x faster                                                       |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.04x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 76.3 ms: 1.03x faster                                                      |
| nbody          | 87.7 ms                                                | 94.0 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.52 ms: 1.07x faster                                                      |
| regex_v8       | 26.9 ms                                                | 25.9 ms: 1.03x faster                                                      |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                       |
| regex_dna      | 220 ms                                                 | 227 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 101 ms                                                 | 97.3 ms: 1.04x faster                                                      |
| json_loads           | 27.2 us                                                | 26.8 us: 1.01x faster                                                      |
| tomli_loads          | 2.12 sec                                               | 2.09 sec: 1.01x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 221 us: 1.04x slower                                                       |
| pickle_pure_python   | 302 us                                                 | 327 us: 1.08x slower                                                       |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.01 ms: 1.00x slower                                                      |
| python_startup         | 12.7 ms                                                | 12.7 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 22.1 ms: 1.02x faster                                                      |
| genshi_xml      | 50.5 ms                                                | 50.2 ms: 1.01x faster                                                      |
| django_template | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                      |
| mako            | 10.7 ms                                                | 11.7 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                       |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 631 ms: 1.36x faster                                                       |
| async_tree_io              | 838 ms                                                 | 626 ms: 1.34x faster                                                       |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 339 ms: 1.29x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                       |
| deepcopy_memo              | 38.4 us                                                | 30.9 us: 1.24x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                                      |
| go                         | 141 ms                                                 | 119 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 507 ms: 1.13x faster                                                       |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                       |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 489 ms: 1.11x faster                                                       |
| telco                      | 8.40 ms                                                | 7.78 ms: 1.08x faster                                                      |
| regex_effbot               | 3.77 ms                                                | 3.52 ms: 1.07x faster                                                      |
| crypto_pyaes               | 74.7 ms                                                | 70.4 ms: 1.06x faster                                                      |
| generators                 | 28.8 ms                                                | 27.3 ms: 1.05x faster                                                      |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.05x faster                                                       |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                     |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 101 ms                                                 | 97.3 ms: 1.04x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.51 sec: 1.04x faster                                                     |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.3 ms: 1.04x faster                                                      |
| json                       | 5.32 ms                                                | 5.13 ms: 1.04x faster                                                      |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                                     |
| regex_v8                   | 26.9 ms                                                | 25.9 ms: 1.03x faster                                                      |
| sqlglot_normalize          | 108 ms                                                 | 104 ms: 1.03x faster                                                       |
| thrift                     | 800 us                                                 | 776 us: 1.03x faster                                                       |
| float                      | 78.7 ms                                                | 76.3 ms: 1.03x faster                                                      |
| async_generators           | 433 ms                                                 | 421 ms: 1.03x faster                                                       |
| richards                   | 47.5 ms                                                | 46.2 ms: 1.03x faster                                                      |
| gc_traversal               | 4.90 ms                                                | 4.76 ms: 1.03x faster                                                      |
| richards_super             | 53.7 ms                                                | 52.3 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.90 ms: 1.03x faster                                                      |
| genshi_text                | 22.6 ms                                                | 22.1 ms: 1.02x faster                                                      |
| djangocms                  | 22.3 us                                                | 21.8 us: 1.02x faster                                                      |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                       |
| connected_components       | 447 ms                                                 | 438 ms: 1.02x faster                                                       |
| shortest_path              | 487 ms                                                 | 478 ms: 1.02x faster                                                       |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                       |
| sqlglot_optimize           | 53.4 ms                                                | 52.6 ms: 1.01x faster                                                      |
| json_loads                 | 27.2 us                                                | 26.8 us: 1.01x faster                                                      |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.01x faster                                                       |
| logging_simple             | 5.65 us                                                | 5.58 us: 1.01x faster                                                      |
| spectral_norm              | 113 ms                                                 | 112 ms: 1.01x faster                                                       |
| sqlite_synth               | 2.90 us                                                | 2.87 us: 1.01x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 2.09 sec: 1.01x faster                                                     |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                       |
| genshi_xml                 | 50.5 ms                                                | 50.2 ms: 1.01x faster                                                      |
| python_startup_no_site     | 7.00 ms                                                | 7.01 ms: 1.00x slower                                                      |
| sympy_integrate            | 19.8 ms                                                | 19.9 ms: 1.00x slower                                                      |
| coverage                   | 82.8 ms                                                | 83.1 ms: 1.00x slower                                                      |
| python_startup             | 12.7 ms                                                | 12.7 ms: 1.01x slower                                                      |
| pprint_safe_repr           | 727 ms                                                 | 731 ms: 1.01x slower                                                       |
| django_template            | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                      |
| dulwich_log                | 64.6 ms                                                | 65.2 ms: 1.01x slower                                                      |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.01x slower                                                     |
| docutils                   | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                     |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                      |
| sqlglot_parse              | 1.26 ms                                                | 1.29 ms: 1.02x slower                                                      |
| deltablue                  | 3.19 ms                                                | 3.27 ms: 1.02x slower                                                      |
| scimark_fft                | 367 ms                                                 | 376 ms: 1.03x slower                                                       |
| comprehensions             | 16.5 us                                                | 16.9 us: 1.03x slower                                                      |
| fannkuch                   | 394 ms                                                 | 405 ms: 1.03x slower                                                       |
| regex_dna                  | 220 ms                                                 | 227 ms: 1.03x slower                                                       |
| hexiom                     | 6.08 ms                                                | 6.27 ms: 1.03x slower                                                      |
| scimark_sor                | 122 ms                                                 | 126 ms: 1.03x slower                                                       |
| scimark_monte_carlo        | 66.8 ms                                                | 68.9 ms: 1.03x slower                                                      |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                       |
| unpickle_pure_python       | 213 us                                                 | 221 us: 1.04x slower                                                       |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                                       |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.04x slower                                                      |
| bench_thread_pool          | 818 us                                                 | 857 us: 1.05x slower                                                       |
| chaos                      | 58.0 ms                                                | 61.1 ms: 1.05x slower                                                      |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.06x slower                                                       |
| pyflate                    | 470 ms                                                 | 496 ms: 1.06x slower                                                       |
| nbody                      | 87.7 ms                                                | 94.0 ms: 1.07x slower                                                      |
| logging_silent             | 101 ns                                                 | 109 ns: 1.07x slower                                                       |
| pickle_pure_python         | 302 us                                                 | 327 us: 1.08x slower                                                       |
| mako                       | 10.7 ms                                                | 11.7 ms: 1.09x slower                                                      |
| many_optionals             | 857 us                                                 | 944 us: 1.10x slower                                                       |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                      |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 81.0 ms: 3.38x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (11): nqueens, create_gc_cycles, sphinx, xml_etree_generate, pidigits, html5lib, asyncio_websockets, xml_etree_process, sympy_expand, logging_format, mdp
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241211-3.14.0a2+-e232ca4/bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4.json: mypy2

- Geometric mean (including insignificant results): 1.028x faster

# HPT report

- Reliability score: 99.71% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x
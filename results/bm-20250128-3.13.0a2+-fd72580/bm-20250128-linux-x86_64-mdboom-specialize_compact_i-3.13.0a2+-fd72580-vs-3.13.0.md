# Results vs. 3.13.0

- fork: mdboom
- ref: specialize_compact_i
- machine: linux-x86_64
- commit hash: fd72580
- commit date: 2025-01-28
- overall geometric mean: 1.052x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 265 ms: 1.00x faster                                                   |
| chameleon      | 6.81 ms                                                | 7.02 ms: 1.03x slower                                                  |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                 |
| html5lib       | 63.4 ms                                                | 64.7 ms: 1.02x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.07 sec: 1.03x slower                                                 |
| tornado_http   | 91.2 ms                                                | 96.0 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                   |
| async_generators           | 433 ms                                                 | 456 ms: 1.05x slower                                                   |
| async_tree_memoization     | 437 ms                                                 | 565 ms: 1.29x slower                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 741 ms: 1.29x slower                                                   |
| async_tree_none            | 350 ms                                                 | 463 ms: 1.32x slower                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 632 ms: 1.37x slower                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 747 ms: 1.37x slower                                                   |
| async_tree_none_tg         | 319 ms                                                 | 455 ms: 1.43x slower                                                   |
| async_tree_io              | 838 ms                                                 | 1.20 sec: 1.43x slower                                                 |
| async_tree_io_tg           | 861 ms                                                 | 1.24 sec: 1.44x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.26x slower                                                           |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 83.0 ms: 1.06x slower                                                  |
| nbody          | 87.7 ms                                                | 93.3 ms: 1.06x slower                                                  |
| pidigits       | 186 ms                                                 | 222 ms: 1.19x slower                                                   |
| Geometric mean | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 26.1 ms: 1.03x faster                                                  |
| regex_effbot   | 3.77 ms                                                | 3.70 ms: 1.02x faster                                                  |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                   |
| regex_compile  | 132 ms                                                 | 134 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_process    | 60.5 ms                                                | 58.9 ms: 1.03x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 86.0 ms: 1.01x faster                                                  |
| pickle_pure_python   | 302 us                                                 | 309 us: 1.02x slower                                                   |
| xml_etree_parse      | 154 ms                                                 | 158 ms: 1.03x slower                                                   |
| json_dumps           | 10.1 ms                                                | 10.5 ms: 1.04x slower                                                  |
| unpickle_pure_python | 213 us                                                 | 222 us: 1.04x slower                                                   |
| json_loads           | 27.2 us                                                | 28.4 us: 1.04x slower                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 107 ms: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.6 ms: 1.01x faster                                                  |
| python_startup_no_site | 7.00 ms                                                | 9.00 ms: 1.29x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 50.8 ms: 1.01x slower                                                  |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                  |
| genshi_text     | 22.6 ms                                                | 23.1 ms: 1.02x slower                                                  |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols   | 160 us                                                 | 115 us: 1.39x faster                                                   |
| gc_traversal               | 4.90 ms                                                | 4.72 ms: 1.04x faster                                                  |
| spectral_norm              | 113 ms                                                 | 110 ms: 1.03x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 26.1 ms: 1.03x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 58.9 ms: 1.03x faster                                                  |
| pyflate                    | 470 ms                                                 | 458 ms: 1.03x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 3.16 us: 1.03x faster                                                  |
| nqueens                    | 80.9 ms                                                | 79.0 ms: 1.02x faster                                                  |
| json                       | 5.32 ms                                                | 5.20 ms: 1.02x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.83 us: 1.02x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.70 ms: 1.02x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.5 ms: 1.02x faster                                                  |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                   |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.01x faster                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.42 ms: 1.01x faster                                                  |
| go                         | 141 ms                                                 | 139 ms: 1.01x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 86.0 ms: 1.01x faster                                                  |
| deepcopy                   | 354 us                                                 | 351 us: 1.01x faster                                                   |
| shortest_path              | 487 ms                                                 | 483 ms: 1.01x faster                                                   |
| thrift                     | 800 us                                                 | 794 us: 1.01x faster                                                   |
| python_startup             | 12.7 ms                                                | 12.6 ms: 1.01x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 74.3 ms: 1.01x faster                                                  |
| 2to3                       | 266 ms                                                 | 265 ms: 1.00x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 50.8 ms: 1.01x slower                                                  |
| sqlglot_parse              | 1.26 ms                                                | 1.27 ms: 1.01x slower                                                  |
| telco                      | 8.40 ms                                                | 8.46 ms: 1.01x slower                                                  |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.01x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 67.5 ms: 1.01x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.15 ms: 1.01x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 735 ms: 1.01x slower                                                   |
| regex_compile              | 132 ms                                                 | 134 ms: 1.01x slower                                                   |
| scimark_sor                | 122 ms                                                 | 124 ms: 1.01x slower                                                   |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                                   |
| generators                 | 28.8 ms                                                | 29.3 ms: 1.02x slower                                                  |
| meteor_contest             | 108 ms                                                 | 110 ms: 1.02x slower                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.02x slower                                                 |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                  |
| pycparser                  | 1.20 sec                                               | 1.22 sec: 1.02x slower                                                 |
| scimark_fft                | 367 ms                                                 | 374 ms: 1.02x slower                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.13 ms: 1.02x slower                                                  |
| html5lib                   | 63.4 ms                                                | 64.7 ms: 1.02x slower                                                  |
| genshi_text                | 22.6 ms                                                | 23.1 ms: 1.02x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 309 us: 1.02x slower                                                   |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                  |
| xml_etree_parse            | 154 ms                                                 | 158 ms: 1.03x slower                                                   |
| chaos                      | 58.0 ms                                                | 59.5 ms: 1.03x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 840 us: 1.03x slower                                                   |
| many_optionals             | 857 us                                                 | 881 us: 1.03x slower                                                   |
| richards_super             | 53.7 ms                                                | 55.3 ms: 1.03x slower                                                  |
| chameleon                  | 6.81 ms                                                | 7.02 ms: 1.03x slower                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 137 ms: 1.03x slower                                                   |
| logging_format             | 6.23 us                                                | 6.43 us: 1.03x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.07 sec: 1.03x slower                                                 |
| richards                   | 47.5 ms                                                | 49.1 ms: 1.03x slower                                                  |
| dulwich_log                | 64.6 ms                                                | 66.8 ms: 1.03x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 10.5 ms: 1.04x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 222 us: 1.04x slower                                                   |
| deltablue                  | 3.19 ms                                                | 3.33 ms: 1.04x slower                                                  |
| logging_silent             | 101 ns                                                 | 105 ns: 1.04x slower                                                   |
| json_loads                 | 27.2 us                                                | 28.4 us: 1.04x slower                                                  |
| logging_simple             | 5.65 us                                                | 5.91 us: 1.05x slower                                                  |
| gunicorn                   | 1.18 ms                                                | 1.24 ms: 1.05x slower                                                  |
| tornado_http               | 91.2 ms                                                | 96.0 ms: 1.05x slower                                                  |
| async_generators           | 433 ms                                                 | 456 ms: 1.05x slower                                                   |
| raytrace                   | 262 ms                                                 | 276 ms: 1.05x slower                                                   |
| float                      | 78.7 ms                                                | 83.0 ms: 1.06x slower                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 107 ms: 1.06x slower                                                   |
| mdp                        | 2.54 sec                                               | 2.69 sec: 1.06x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.97 sec: 1.06x slower                                                 |
| pathlib                    | 17.4 ms                                                | 18.4 ms: 1.06x slower                                                  |
| nbody                      | 87.7 ms                                                | 93.3 ms: 1.06x slower                                                  |
| k_core                     | 2.37 sec                                               | 2.68 sec: 1.13x slower                                                 |
| coverage                   | 82.8 ms                                                | 94.2 ms: 1.14x slower                                                  |
| pidigits                   | 186 ms                                                 | 222 ms: 1.19x slower                                                   |
| python_startup_no_site     | 7.00 ms                                                | 9.00 ms: 1.29x slower                                                  |
| async_tree_memoization     | 437 ms                                                 | 565 ms: 1.29x slower                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 741 ms: 1.29x slower                                                   |
| async_tree_none            | 350 ms                                                 | 463 ms: 1.32x slower                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 632 ms: 1.37x slower                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 747 ms: 1.37x slower                                                   |
| async_tree_none_tg         | 319 ms                                                 | 455 ms: 1.43x slower                                                   |
| async_tree_io              | 838 ms                                                 | 1.20 sec: 1.43x slower                                                 |
| async_tree_io_tg           | 861 ms                                                 | 1.24 sec: 1.44x slower                                                 |
| subparsers                 | 15.5 ms                                                | 51.7 ms: 3.35x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                           |

Benchmark hidden because not significant (10): pylint, sympy_str, sqlglot_optimize, tomli_loads, bench_mp_pool, connected_components, fannkuch, sympy_expand, coroutines, deepcopy_memo
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: djangocms, gevent_hub

- Geometric mean (including insignificant results): 1.052x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x
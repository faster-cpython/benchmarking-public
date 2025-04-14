# Results vs. 3.13.0

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: 696d3fd
- commit date: 2025-03-30
- overall geometric mean: 1.000x slower
- HPT reliability: 96.59%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 272 ms: 1.02x slower                                          |
| docutils       | 2.58 sec                                               | 2.77 sec: 1.07x slower                                        |
| html5lib       | 63.4 ms                                                | 64.5 ms: 1.02x slower                                         |
| sphinx         | 1.03 sec                                               | 1.05 sec: 1.02x slower                                        |
| Geometric mean | (ref)                                                  | 1.03x slower                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 322 ms: 1.44x faster                                          |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                          |
| async_tree_io              | 838 ms                                                 | 625 ms: 1.34x faster                                          |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                          |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                          |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                          |
| async_generators           | 433 ms                                                 | 418 ms: 1.04x faster                                          |
| coroutines                 | 22.2 ms                                                | 21.9 ms: 1.02x faster                                         |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                          |
| float          | 78.7 ms                                                | 81.0 ms: 1.03x slower                                         |
| nbody          | 87.7 ms                                                | 107 ms: 1.22x slower                                          |
| Geometric mean | (ref)                                                  | 1.08x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.2 ms: 1.16x faster                                         |
| regex_effbot   | 3.77 ms                                                | 3.26 ms: 1.15x faster                                         |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                          |
| regex_compile  | 132 ms                                                 | 137 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.85 sec: 1.14x faster                                        |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.10x faster                                          |
| xml_etree_generate   | 86.8 ms                                                | 84.5 ms: 1.03x faster                                         |
| xml_etree_process    | 60.5 ms                                                | 59.1 ms: 1.02x faster                                         |
| xml_etree_iterparse  | 101 ms                                                 | 99.1 ms: 1.02x faster                                         |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                         |
| unpickle_pure_python | 213 us                                                 | 236 us: 1.11x slower                                          |
| pickle_pure_python   | 302 us                                                 | 342 us: 1.13x slower                                          |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                         |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                         |
| python_startup_no_site | 7.00 ms                                                | 8.22 ms: 1.17x slower                                         |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 22.1 ms: 1.02x faster                                         |
| genshi_xml      | 50.5 ms                                                | 52.1 ms: 1.03x slower                                         |
| django_template | 31.7 ms                                                | 33.5 ms: 1.06x slower                                         |
| mako            | 10.7 ms                                                | 11.6 ms: 1.09x slower                                         |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.33 sec: 1.92x faster                                        |
| async_tree_memoization_tg  | 463 ms                                                 | 322 ms: 1.44x faster                                          |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                          |
| async_tree_io              | 838 ms                                                 | 625 ms: 1.34x faster                                          |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                          |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                          |
| deepcopy                   | 354 us                                                 | 274 us: 1.29x faster                                          |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                          |
| deepcopy_memo              | 38.4 us                                                | 30.8 us: 1.25x faster                                         |
| richards                   | 47.5 ms                                                | 40.4 ms: 1.18x faster                                         |
| richards_super             | 53.7 ms                                                | 45.8 ms: 1.17x faster                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                          |
| regex_v8                   | 26.9 ms                                                | 23.2 ms: 1.16x faster                                         |
| regex_effbot               | 3.77 ms                                                | 3.26 ms: 1.15x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                          |
| tomli_loads                | 2.12 sec                                               | 1.85 sec: 1.14x faster                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.89 us: 1.12x faster                                         |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.10x faster                                          |
| pylint                     | 312 ms                                                 | 290 ms: 1.07x faster                                          |
| regex_dna                  | 220 ms                                                 | 209 ms: 1.05x faster                                          |
| dulwich_log                | 64.6 ms                                                | 62.2 ms: 1.04x faster                                         |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.04x faster                                         |
| async_generators           | 433 ms                                                 | 418 ms: 1.04x faster                                          |
| xml_etree_generate         | 86.8 ms                                                | 84.5 ms: 1.03x faster                                         |
| sqlite_synth               | 2.90 us                                                | 2.83 us: 1.03x faster                                         |
| telco                      | 8.40 ms                                                | 8.19 ms: 1.03x faster                                         |
| xml_etree_process          | 60.5 ms                                                | 59.1 ms: 1.02x faster                                         |
| xml_etree_iterparse        | 101 ms                                                 | 99.1 ms: 1.02x faster                                         |
| genshi_text                | 22.6 ms                                                | 22.1 ms: 1.02x faster                                         |
| coroutines                 | 22.2 ms                                                | 21.9 ms: 1.02x faster                                         |
| gc_traversal               | 4.90 ms                                                | 4.82 ms: 1.01x faster                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.66 sec: 1.01x faster                                        |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                          |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.01x slower                                         |
| html5lib                   | 63.4 ms                                                | 64.5 ms: 1.02x slower                                         |
| pyflate                    | 470 ms                                                 | 478 ms: 1.02x slower                                          |
| sphinx                     | 1.03 sec                                               | 1.05 sec: 1.02x slower                                        |
| 2to3                       | 266 ms                                                 | 272 ms: 1.02x slower                                          |
| sqlalchemy_declarative     | 133 ms                                                 | 136 ms: 1.02x slower                                          |
| logging_format             | 6.23 us                                                | 6.40 us: 1.03x slower                                         |
| float                      | 78.7 ms                                                | 81.0 ms: 1.03x slower                                         |
| generators                 | 28.8 ms                                                | 29.7 ms: 1.03x slower                                         |
| genshi_xml                 | 50.5 ms                                                | 52.1 ms: 1.03x slower                                         |
| logging_simple             | 5.65 us                                                | 5.85 us: 1.04x slower                                         |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.04x slower                                          |
| coverage                   | 82.8 ms                                                | 86.1 ms: 1.04x slower                                         |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                         |
| pycparser                  | 1.20 sec                                               | 1.25 sec: 1.04x slower                                        |
| regex_compile              | 132 ms                                                 | 137 ms: 1.04x slower                                          |
| sympy_integrate            | 19.8 ms                                                | 20.7 ms: 1.05x slower                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.7 ms: 1.05x slower                                         |
| meteor_contest             | 108 ms                                                 | 114 ms: 1.05x slower                                          |
| sympy_str                  | 273 ms                                                 | 286 ms: 1.05x slower                                          |
| shortest_path              | 487 ms                                                 | 513 ms: 1.05x slower                                          |
| connected_components       | 447 ms                                                 | 472 ms: 1.06x slower                                          |
| chaos                      | 58.0 ms                                                | 61.3 ms: 1.06x slower                                         |
| django_template            | 31.7 ms                                                | 33.5 ms: 1.06x slower                                         |
| scimark_fft                | 367 ms                                                 | 390 ms: 1.06x slower                                          |
| go                         | 141 ms                                                 | 150 ms: 1.06x slower                                          |
| docutils                   | 2.58 sec                                               | 2.77 sec: 1.07x slower                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 72.6 ms: 1.09x slower                                         |
| mako                       | 10.7 ms                                                | 11.6 ms: 1.09x slower                                         |
| sympy_expand               | 456 ms                                                 | 498 ms: 1.09x slower                                          |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                         |
| bench_thread_pool          | 818 us                                                 | 899 us: 1.10x slower                                          |
| scimark_sor                | 122 ms                                                 | 134 ms: 1.10x slower                                          |
| scimark_lu                 | 114 ms                                                 | 126 ms: 1.10x slower                                          |
| unpickle_pure_python       | 213 us                                                 | 236 us: 1.11x slower                                          |
| nqueens                    | 80.9 ms                                                | 89.7 ms: 1.11x slower                                         |
| raytrace                   | 262 ms                                                 | 291 ms: 1.11x slower                                          |
| spectral_norm              | 113 ms                                                 | 127 ms: 1.12x slower                                          |
| deltablue                  | 3.19 ms                                                | 3.58 ms: 1.12x slower                                         |
| pprint_safe_repr           | 727 ms                                                 | 817 ms: 1.12x slower                                          |
| typing_runtime_protocols   | 160 us                                                 | 181 us: 1.13x slower                                          |
| pickle_pure_python         | 302 us                                                 | 342 us: 1.13x slower                                          |
| fannkuch                   | 394 ms                                                 | 448 ms: 1.14x slower                                          |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                         |
| pprint_pformat             | 1.48 sec                                               | 1.71 sec: 1.16x slower                                        |
| many_optionals             | 857 us                                                 | 1.01 ms: 1.17x slower                                         |
| python_startup_no_site     | 7.00 ms                                                | 8.22 ms: 1.17x slower                                         |
| crypto_pyaes               | 74.7 ms                                                | 88.5 ms: 1.18x slower                                         |
| hexiom                     | 6.08 ms                                                | 7.41 ms: 1.22x slower                                         |
| nbody                      | 87.7 ms                                                | 107 ms: 1.22x slower                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.18 ms: 1.23x slower                                         |
| comprehensions             | 16.5 us                                                | 20.5 us: 1.24x slower                                         |
| subparsers                 | 15.5 ms                                                | 21.9 ms: 1.42x slower                                         |
| bench_mp_pool              | 24.0 ms                                                | 84.3 ms: 3.52x slower                                         |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                  |

Benchmark hidden because not significant (4): k_core, json, logging_silent, asyncio_websockets
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250330-3.14.0a6+-696d3fd-JIT/bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 96.59% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.91x
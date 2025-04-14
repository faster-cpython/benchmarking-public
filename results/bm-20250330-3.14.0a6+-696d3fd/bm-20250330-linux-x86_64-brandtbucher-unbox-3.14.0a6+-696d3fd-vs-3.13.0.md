# Results vs. 3.13.0

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: 696d3fd
- commit date: 2025-03-30
- overall geometric mean: 1.018x faster
- HPT reliability: 62.45%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.80x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 262 ms: 1.02x faster                                          |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.03x slower                                        |
| html5lib       | 63.4 ms                                                | 64.2 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                          |
| async_tree_io_tg           | 861 ms                                                 | 605 ms: 1.42x faster                                          |
| async_tree_io              | 838 ms                                                 | 603 ms: 1.39x faster                                          |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                          |
| async_tree_none            | 350 ms                                                 | 255 ms: 1.37x faster                                          |
| async_tree_none_tg         | 319 ms                                                 | 242 ms: 1.32x faster                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                          |
| async_generators           | 433 ms                                                 | 400 ms: 1.08x faster                                          |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                  |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 189 ms: 1.02x slower                                          |
| float          | 78.7 ms                                                | 85.4 ms: 1.09x slower                                         |
| nbody          | 87.7 ms                                                | 111 ms: 1.27x slower                                          |
| Geometric mean | (ref)                                                  | 1.12x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.3 ms: 1.15x faster                                         |
| regex_effbot   | 3.77 ms                                                | 3.32 ms: 1.13x faster                                         |
| regex_compile  | 132 ms                                                 | 134 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                  |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.89 sec: 1.12x faster                                        |
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.08x faster                                          |
| xml_etree_iterparse  | 101 ms                                                 | 100 ms: 1.01x faster                                          |
| xml_etree_generate   | 86.8 ms                                                | 87.2 ms: 1.00x slower                                         |
| unpickle_pure_python | 213 us                                                 | 228 us: 1.07x slower                                          |
| pickle_pure_python   | 302 us                                                 | 330 us: 1.09x slower                                          |
| json_loads           | 27.2 us                                                | 29.7 us: 1.09x slower                                         |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                         |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                  |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                         |
| python_startup_no_site | 7.00 ms                                                | 8.18 ms: 1.17x slower                                         |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.8 ms: 1.04x faster                                         |
| django_template | 31.7 ms                                                | 32.7 ms: 1.03x slower                                         |
| mako            | 10.7 ms                                                | 11.9 ms: 1.11x slower                                         |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                  |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.29 sec: 1.97x faster                                        |
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                          |
| async_tree_io_tg           | 861 ms                                                 | 605 ms: 1.42x faster                                          |
| async_tree_io              | 838 ms                                                 | 603 ms: 1.39x faster                                          |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                          |
| async_tree_none            | 350 ms                                                 | 255 ms: 1.37x faster                                          |
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                          |
| async_tree_none_tg         | 319 ms                                                 | 242 ms: 1.32x faster                                          |
| deepcopy_memo              | 38.4 us                                                | 30.4 us: 1.26x faster                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                          |
| regex_v8                   | 26.9 ms                                                | 23.3 ms: 1.15x faster                                         |
| go                         | 141 ms                                                 | 122 ms: 1.15x faster                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                          |
| regex_effbot               | 3.77 ms                                                | 3.32 ms: 1.13x faster                                         |
| tomli_loads                | 2.12 sec                                               | 1.89 sec: 1.12x faster                                        |
| pylint                     | 312 ms                                                 | 282 ms: 1.11x faster                                          |
| async_generators           | 433 ms                                                 | 400 ms: 1.08x faster                                          |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.08x faster                                          |
| dulwich_log                | 64.6 ms                                                | 60.1 ms: 1.08x faster                                         |
| telco                      | 8.40 ms                                                | 7.92 ms: 1.06x faster                                         |
| richards                   | 47.5 ms                                                | 45.3 ms: 1.05x faster                                         |
| richards_super             | 53.7 ms                                                | 51.8 ms: 1.04x faster                                         |
| genshi_text                | 22.6 ms                                                | 21.8 ms: 1.04x faster                                         |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                         |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.54 sec: 1.03x faster                                        |
| pyflate                    | 470 ms                                                 | 455 ms: 1.03x faster                                          |
| sqlite_synth               | 2.90 us                                                | 2.82 us: 1.03x faster                                         |
| 2to3                       | 266 ms                                                 | 262 ms: 1.02x faster                                          |
| xml_etree_iterparse        | 101 ms                                                 | 100 ms: 1.01x faster                                          |
| gc_traversal               | 4.90 ms                                                | 4.86 ms: 1.01x faster                                         |
| sympy_integrate            | 19.8 ms                                                | 19.9 ms: 1.00x slower                                         |
| xml_etree_generate         | 86.8 ms                                                | 87.2 ms: 1.00x slower                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.0 ms: 1.01x slower                                         |
| hexiom                     | 6.08 ms                                                | 6.13 ms: 1.01x slower                                         |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                          |
| pycparser                  | 1.20 sec                                               | 1.21 sec: 1.01x slower                                        |
| html5lib                   | 63.4 ms                                                | 64.2 ms: 1.01x slower                                         |
| pidigits                   | 186 ms                                                 | 189 ms: 1.02x slower                                          |
| regex_compile              | 132 ms                                                 | 134 ms: 1.02x slower                                          |
| sympy_expand               | 456 ms                                                 | 466 ms: 1.02x slower                                          |
| create_gc_cycles           | 2.45 ms                                                | 2.51 ms: 1.02x slower                                         |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.03x slower                                        |
| pprint_safe_repr           | 727 ms                                                 | 747 ms: 1.03x slower                                          |
| shortest_path              | 487 ms                                                 | 501 ms: 1.03x slower                                          |
| typing_runtime_protocols   | 160 us                                                 | 165 us: 1.03x slower                                          |
| pprint_pformat             | 1.48 sec                                               | 1.53 sec: 1.03x slower                                        |
| generators                 | 28.8 ms                                                | 29.7 ms: 1.03x slower                                         |
| django_template            | 31.7 ms                                                | 32.7 ms: 1.03x slower                                         |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                         |
| coverage                   | 82.8 ms                                                | 86.1 ms: 1.04x slower                                         |
| chaos                      | 58.0 ms                                                | 60.6 ms: 1.04x slower                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 69.9 ms: 1.05x slower                                         |
| connected_components       | 447 ms                                                 | 469 ms: 1.05x slower                                          |
| nqueens                    | 80.9 ms                                                | 85.5 ms: 1.06x slower                                         |
| comprehensions             | 16.5 us                                                | 17.6 us: 1.07x slower                                         |
| unpickle_pure_python       | 213 us                                                 | 228 us: 1.07x slower                                          |
| bench_thread_pool          | 818 us                                                 | 884 us: 1.08x slower                                          |
| raytrace                   | 262 ms                                                 | 283 ms: 1.08x slower                                          |
| float                      | 78.7 ms                                                | 85.4 ms: 1.09x slower                                         |
| pickle_pure_python         | 302 us                                                 | 330 us: 1.09x slower                                          |
| scimark_sor                | 122 ms                                                 | 134 ms: 1.09x slower                                          |
| json_loads                 | 27.2 us                                                | 29.7 us: 1.09x slower                                         |
| fannkuch                   | 394 ms                                                 | 431 ms: 1.10x slower                                          |
| crypto_pyaes               | 74.7 ms                                                | 82.9 ms: 1.11x slower                                         |
| scimark_lu                 | 114 ms                                                 | 127 ms: 1.11x slower                                          |
| mako                       | 10.7 ms                                                | 11.9 ms: 1.11x slower                                         |
| spectral_norm              | 113 ms                                                 | 127 ms: 1.12x slower                                          |
| many_optionals             | 857 us                                                 | 966 us: 1.13x slower                                          |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                         |
| deltablue                  | 3.19 ms                                                | 3.65 ms: 1.14x slower                                         |
| python_startup_no_site     | 7.00 ms                                                | 8.18 ms: 1.17x slower                                         |
| scimark_fft                | 367 ms                                                 | 450 ms: 1.23x slower                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.30 ms: 1.25x slower                                         |
| nbody                      | 87.7 ms                                                | 111 ms: 1.27x slower                                          |
| subparsers                 | 15.5 ms                                                | 21.4 ms: 1.39x slower                                         |
| bench_mp_pool              | 24.0 ms                                                | 83.7 ms: 3.49x slower                                         |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (13): json, genshi_xml, coroutines, meteor_contest, logging_silent, sqlalchemy_declarative, regex_dna, sphinx, logging_format, logging_simple, asyncio_websockets, xml_etree_process, sympy_str
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250330-3.14.0a6+-696d3fd/bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.018x faster

# HPT report

- Reliability score: 62.45% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.80x
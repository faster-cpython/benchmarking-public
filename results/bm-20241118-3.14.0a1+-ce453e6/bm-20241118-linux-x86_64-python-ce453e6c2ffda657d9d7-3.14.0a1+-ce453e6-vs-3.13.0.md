# Results vs. 3.13.0

- fork: python
- ref: ce453e6c2ffda657d9d7
- machine: linux-x86_64
- commit hash: ce453e6
- commit date: 2024-11-18
- overall geometric mean: 1.004x slower
- HPT reliability: 75.86%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                                   |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                 |
| html5lib       | 63.4 ms                                                | 64.6 ms: 1.02x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 381 ms: 1.21x faster                                                   |
| async_tree_none            | 350 ms                                                 | 325 ms: 1.08x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 414 ms: 1.06x faster                                                   |
| async_generators           | 433 ms                                                 | 431 ms: 1.01x faster                                                   |
| async_tree_io              | 838 ms                                                 | 859 ms: 1.03x slower                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 561 ms: 1.03x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                                  |
| async_tree_io_tg           | 861 ms                                                 | 974 ms: 1.13x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                   |
| float          | 78.7 ms                                                | 79.8 ms: 1.01x slower                                                  |
| nbody          | 87.7 ms                                                | 96.0 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                  |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                   |
| regex_effbot   | 3.77 ms                                                | 3.68 ms: 1.02x faster                                                  |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_generate   | 86.8 ms                                                | 85.2 ms: 1.02x faster                                                  |
| json_loads           | 27.2 us                                                | 26.8 us: 1.02x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 59.6 ms: 1.01x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                   |
| xml_etree_parse      | 154 ms                                                 | 158 ms: 1.02x slower                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 106 ms: 1.05x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 327 us: 1.08x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                           |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.04 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                  |
| mako            | 10.7 ms                                                | 11.6 ms: 1.09x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                           |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 354 us                                                 | 265 us: 1.34x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 31.0 us: 1.24x faster                                                  |
| async_tree_memoization_tg  | 463 ms                                                 | 381 ms: 1.21x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.20x faster                                                  |
| go                         | 141 ms                                                 | 121 ms: 1.16x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.0 ms: 1.09x faster                                                  |
| json                       | 5.32 ms                                                | 4.91 ms: 1.08x faster                                                  |
| async_tree_none            | 350 ms                                                 | 325 ms: 1.08x faster                                                   |
| telco                      | 8.40 ms                                                | 7.88 ms: 1.07x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 414 ms: 1.06x faster                                                   |
| generators                 | 28.8 ms                                                | 27.4 ms: 1.05x faster                                                  |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                   |
| richards                   | 47.5 ms                                                | 45.7 ms: 1.04x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 72.2 ms: 1.03x faster                                                  |
| thrift                     | 800 us                                                 | 775 us: 1.03x faster                                                   |
| richards_super             | 53.7 ms                                                | 52.2 ms: 1.03x faster                                                  |
| shortest_path              | 487 ms                                                 | 474 ms: 1.03x faster                                                   |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.68 ms: 1.02x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                   |
| pyflate                    | 470 ms                                                 | 460 ms: 1.02x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 85.2 ms: 1.02x faster                                                  |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| connected_components       | 447 ms                                                 | 440 ms: 1.02x faster                                                   |
| json_loads                 | 27.2 us                                                | 26.8 us: 1.02x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 59.6 ms: 1.01x faster                                                  |
| regex_dna                  | 220 ms                                                 | 217 ms: 1.01x faster                                                   |
| sympy_str                  | 273 ms                                                 | 270 ms: 1.01x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.87 us: 1.01x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.84 ms: 1.01x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.59 us: 1.01x faster                                                  |
| logging_format             | 6.23 us                                                | 6.18 us: 1.01x faster                                                  |
| async_generators           | 433 ms                                                 | 431 ms: 1.01x faster                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.47 sec: 1.01x faster                                                 |
| sympy_integrate            | 19.8 ms                                                | 19.9 ms: 1.00x slower                                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                   |
| python_startup_no_site     | 7.00 ms                                                | 7.04 ms: 1.01x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 162 us: 1.01x slower                                                   |
| float                      | 78.7 ms                                                | 79.8 ms: 1.01x slower                                                  |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                  |
| coverage                   | 82.8 ms                                                | 84.4 ms: 1.02x slower                                                  |
| html5lib                   | 63.4 ms                                                | 64.6 ms: 1.02x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                   |
| xml_etree_parse            | 154 ms                                                 | 158 ms: 1.02x slower                                                   |
| async_tree_io              | 838 ms                                                 | 859 ms: 1.03x slower                                                   |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.03x slower                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.82 sec: 1.03x slower                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 561 ms: 1.03x slower                                                   |
| scimark_fft                | 367 ms                                                 | 379 ms: 1.03x slower                                                   |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.29 ms: 1.03x slower                                                  |
| mdp                        | 2.54 sec                                               | 2.64 sec: 1.04x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 851 us: 1.04x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                 |
| fannkuch                   | 394 ms                                                 | 410 ms: 1.04x slower                                                   |
| deltablue                  | 3.19 ms                                                | 3.33 ms: 1.04x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 69.8 ms: 1.05x slower                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 106 ms: 1.05x slower                                                   |
| scimark_sor                | 122 ms                                                 | 128 ms: 1.05x slower                                                   |
| spectral_norm              | 113 ms                                                 | 119 ms: 1.05x slower                                                   |
| raytrace                   | 262 ms                                                 | 276 ms: 1.06x slower                                                   |
| chaos                      | 58.0 ms                                                | 61.3 ms: 1.06x slower                                                  |
| logging_silent             | 101 ns                                                 | 107 ns: 1.06x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 327 us: 1.08x slower                                                   |
| mako                       | 10.7 ms                                                | 11.6 ms: 1.09x slower                                                  |
| nbody                      | 87.7 ms                                                | 96.0 ms: 1.09x slower                                                  |
| many_optionals             | 857 us                                                 | 948 us: 1.11x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.75 ms: 1.12x slower                                                  |
| async_tree_io_tg           | 861 ms                                                 | 974 ms: 1.13x slower                                                   |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                                  |
| k_core                     | 2.37 sec                                               | 3.58 sec: 1.51x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 79.9 ms: 3.33x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (14): djangocms, genshi_xml, sqlalchemy_imperative, async_tree_cpu_io_mixed, nqueens, asyncio_websockets, tomli_loads, dulwich_log, sympy_expand, pprint_safe_repr, scimark_sparse_mat_mult, genshi_text, async_tree_none_tg, pylint
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20241118-3.14.0a1+-ce453e6/bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 75.86% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x
# Results vs. 3.13.0

- fork: python
- ref: ea8ec95cfadbf58a11ef
- machine: linux-x86_64
- commit hash: ea8ec95
- commit date: 2025-04-21
- overall geometric mean: 1.049x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 252 ms: 1.06x faster                                                   |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                 |
| html5lib       | 63.4 ms                                                | 60.2 ms: 1.05x faster                                                  |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.40x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 614 ms: 1.37x faster                                                   |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 483 ms: 1.19x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.12x faster                                                   |
| async_generators           | 433 ms                                                 | 401 ms: 1.08x faster                                                   |
| coroutines                 | 22.2 ms                                                | 24.3 ms: 1.09x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.6 ms: 1.11x faster                                                  |
| pidigits       | 186 ms                                                 | 194 ms: 1.04x slower                                                   |
| nbody          | 87.7 ms                                                | 96.1 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.3 ms: 1.20x faster                                                  |
| regex_effbot   | 3.77 ms                                                | 3.13 ms: 1.20x faster                                                  |
| regex_dna      | 220 ms                                                 | 205 ms: 1.07x faster                                                   |
| regex_compile  | 132 ms                                                 | 126 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 98.7 ms: 1.03x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 85.7 ms: 1.01x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 314 us: 1.04x slower                                                   |
| json_loads           | 27.2 us                                                | 30.1 us: 1.11x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 8.20 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 20.8 ms: 1.09x faster                                                  |
| genshi_xml     | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                  |
| mako           | 10.7 ms                                                | 11.8 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.09x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                   |
| deepcopy                   | 354 us                                                 | 251 us: 1.41x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.40x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 614 ms: 1.37x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 28.5 us: 1.35x faster                                                  |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                   |
| go                         | 141 ms                                                 | 112 ms: 1.25x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.20x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 22.3 ms: 1.20x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.13 ms: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 483 ms: 1.19x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.12x faster                                                   |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                   |
| float                      | 78.7 ms                                                | 70.6 ms: 1.11x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                   |
| genshi_text                | 22.6 ms                                                | 20.8 ms: 1.09x faster                                                  |
| richards                   | 47.5 ms                                                | 43.7 ms: 1.09x faster                                                  |
| async_generators           | 433 ms                                                 | 401 ms: 1.08x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 59.8 ms: 1.08x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                 |
| spectral_norm              | 113 ms                                                 | 105 ms: 1.08x faster                                                   |
| richards_super             | 53.7 ms                                                | 50.0 ms: 1.07x faster                                                  |
| regex_dna                  | 220 ms                                                 | 205 ms: 1.07x faster                                                   |
| telco                      | 8.40 ms                                                | 7.91 ms: 1.06x faster                                                  |
| 2to3                       | 266 ms                                                 | 252 ms: 1.06x faster                                                   |
| html5lib                   | 63.4 ms                                                | 60.2 ms: 1.05x faster                                                  |
| pyflate                    | 470 ms                                                 | 446 ms: 1.05x faster                                                   |
| regex_compile              | 132 ms                                                 | 126 ms: 1.04x faster                                                   |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.50 sec: 1.04x faster                                                 |
| logging_silent             | 101 ns                                                 | 97.2 ns: 1.04x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                                 |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 98.7 ms: 1.03x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.52 us: 1.02x faster                                                  |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                   |
| gc_traversal               | 4.90 ms                                                | 4.78 ms: 1.02x faster                                                  |
| chaos                      | 58.0 ms                                                | 56.7 ms: 1.02x faster                                                  |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| scimark_fft                | 367 ms                                                 | 360 ms: 1.02x faster                                                   |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                   |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                   |
| pprint_safe_repr           | 727 ms                                                 | 714 ms: 1.02x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 73.5 ms: 1.02x faster                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.01x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 85.7 ms: 1.01x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                                   |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 66.2 ms: 1.01x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                  |
| logging_format             | 6.23 us                                                | 6.18 us: 1.01x faster                                                  |
| raytrace                   | 262 ms                                                 | 263 ms: 1.01x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                 |
| generators                 | 28.8 ms                                                | 29.1 ms: 1.01x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.1 ms: 1.01x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                   |
| comprehensions             | 16.5 us                                                | 16.9 us: 1.02x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.23 ms: 1.03x slower                                                  |
| json                       | 5.32 ms                                                | 5.49 ms: 1.03x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 314 us: 1.04x slower                                                   |
| pidigits                   | 186 ms                                                 | 194 ms: 1.04x slower                                                   |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.06x slower                                                   |
| deltablue                  | 3.19 ms                                                | 3.41 ms: 1.07x slower                                                  |
| fannkuch                   | 394 ms                                                 | 420 ms: 1.07x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 882 us: 1.08x slower                                                   |
| coroutines                 | 22.2 ms                                                | 24.3 ms: 1.09x slower                                                  |
| many_optionals             | 857 us                                                 | 938 us: 1.09x slower                                                   |
| nbody                      | 87.7 ms                                                | 96.1 ms: 1.10x slower                                                  |
| mako                       | 10.7 ms                                                | 11.8 ms: 1.10x slower                                                  |
| json_loads                 | 27.2 us                                                | 30.1 us: 1.11x slower                                                  |
| coverage                   | 82.8 ms                                                | 93.4 ms: 1.13x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.15x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 8.20 ms: 1.17x slower                                                  |
| subparsers                 | 15.5 ms                                                | 21.3 ms: 1.38x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.41x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (7): sympy_expand, django_template, shortest_path, nqueens, scimark_sparse_mat_mult, asyncio_websockets, connected_components
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250421-3.14.0a7+-ea8ec95/bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x
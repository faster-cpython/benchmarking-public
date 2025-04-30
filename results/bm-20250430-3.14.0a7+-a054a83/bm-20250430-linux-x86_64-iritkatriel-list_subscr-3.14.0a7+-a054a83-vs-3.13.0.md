# Results vs. 3.13.0

- fork: iritkatriel
- ref: list_subscr
- machine: linux-x86_64
- commit hash: a054a83
- commit date: 2025-04-30
- overall geometric mean: 1.049x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                               |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                             |
| html5lib       | 63.4 ms                                                | 62.4 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.49x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                               |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                               |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 491 ms: 1.11x faster                                               |
| async_generators           | 433 ms                                                 | 395 ms: 1.10x faster                                               |
| coroutines                 | 22.2 ms                                                | 25.7 ms: 1.16x slower                                              |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.6 ms: 1.16x faster                                              |
| pidigits       | 186 ms                                                 | 195 ms: 1.05x slower                                               |
| nbody          | 87.7 ms                                                | 96.6 ms: 1.10x slower                                              |
| Geometric mean | (ref)                                                  | 1.00x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.26 ms: 1.16x faster                                              |
| regex_v8       | 26.9 ms                                                | 23.9 ms: 1.12x faster                                              |
| regex_dna      | 220 ms                                                 | 208 ms: 1.06x faster                                               |
| regex_compile  | 132 ms                                                 | 125 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.10x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.08x faster                                               |
| tomli_loads          | 2.12 sec                                               | 1.98 sec: 1.07x faster                                             |
| xml_etree_iterparse  | 101 ms                                                 | 99.1 ms: 1.02x faster                                              |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                               |
| pickle_pure_python   | 302 us                                                 | 314 us: 1.04x slower                                               |
| json_loads           | 27.2 us                                                | 29.7 us: 1.09x slower                                              |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.16x slower                                              |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                       |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.91 ms: 1.01x faster                                              |
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                              |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.3 ms: 1.06x faster                                              |
| genshi_xml      | 50.5 ms                                                | 49.4 ms: 1.02x faster                                              |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                              |
| mako            | 10.7 ms                                                | 11.6 ms: 1.09x slower                                              |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.08x faster                                             |
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.49x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                               |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                               |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 28.6 us: 1.34x faster                                              |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                               |
| go                         | 141 ms                                                 | 113 ms: 1.24x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.19x faster                                              |
| float                      | 78.7 ms                                                | 67.6 ms: 1.16x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.26 ms: 1.16x faster                                              |
| regex_v8                   | 26.9 ms                                                | 23.9 ms: 1.12x faster                                              |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                               |
| spectral_norm              | 113 ms                                                 | 102 ms: 1.11x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 491 ms: 1.11x faster                                               |
| dulwich_log                | 64.6 ms                                                | 58.7 ms: 1.10x faster                                              |
| async_generators           | 433 ms                                                 | 395 ms: 1.10x faster                                               |
| richards                   | 47.5 ms                                                | 43.5 ms: 1.09x faster                                              |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.08x faster                                               |
| richards_super             | 53.7 ms                                                | 49.8 ms: 1.08x faster                                              |
| telco                      | 8.40 ms                                                | 7.78 ms: 1.08x faster                                              |
| tomli_loads                | 2.12 sec                                               | 1.98 sec: 1.07x faster                                             |
| pyflate                    | 470 ms                                                 | 442 ms: 1.06x faster                                               |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                              |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                             |
| regex_dna                  | 220 ms                                                 | 208 ms: 1.06x faster                                               |
| regex_compile              | 132 ms                                                 | 125 ms: 1.05x faster                                               |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                              |
| k_core                     | 2.37 sec                                               | 2.25 sec: 1.05x faster                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.47 sec: 1.05x faster                                             |
| scimark_fft                | 367 ms                                                 | 352 ms: 1.04x faster                                               |
| logging_silent             | 101 ns                                                 | 97.1 ns: 1.04x faster                                              |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                               |
| sympy_integrate            | 19.8 ms                                                | 19.1 ms: 1.04x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                              |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.03x faster                                               |
| pprint_safe_repr           | 727 ms                                                 | 709 ms: 1.02x faster                                               |
| crypto_pyaes               | 74.7 ms                                                | 73.0 ms: 1.02x faster                                              |
| xml_etree_iterparse        | 101 ms                                                 | 99.1 ms: 1.02x faster                                              |
| genshi_xml                 | 50.5 ms                                                | 49.4 ms: 1.02x faster                                              |
| gc_traversal               | 4.90 ms                                                | 4.80 ms: 1.02x faster                                              |
| chaos                      | 58.0 ms                                                | 56.9 ms: 1.02x faster                                              |
| sympy_str                  | 273 ms                                                 | 268 ms: 1.02x faster                                               |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                               |
| pprint_pformat             | 1.48 sec                                               | 1.45 sec: 1.02x faster                                             |
| html5lib                   | 63.4 ms                                                | 62.4 ms: 1.02x faster                                              |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                               |
| python_startup_no_site     | 7.00 ms                                                | 6.91 ms: 1.01x faster                                              |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                               |
| logging_simple             | 5.65 us                                                | 5.60 us: 1.01x faster                                              |
| raytrace                   | 262 ms                                                 | 261 ms: 1.00x faster                                               |
| shortest_path              | 487 ms                                                 | 491 ms: 1.01x slower                                               |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.1 ms: 1.01x slower                                              |
| docutils                   | 2.58 sec                                               | 2.62 sec: 1.01x slower                                             |
| nqueens                    | 80.9 ms                                                | 82.0 ms: 1.01x slower                                              |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                              |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                              |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                               |
| comprehensions             | 16.5 us                                                | 16.9 us: 1.03x slower                                              |
| generators                 | 28.8 ms                                                | 29.7 ms: 1.03x slower                                              |
| deltablue                  | 3.19 ms                                                | 3.30 ms: 1.03x slower                                              |
| fannkuch                   | 394 ms                                                 | 407 ms: 1.03x slower                                               |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                              |
| pickle_pure_python         | 302 us                                                 | 314 us: 1.04x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.33 ms: 1.04x slower                                              |
| pidigits                   | 186 ms                                                 | 195 ms: 1.05x slower                                               |
| json                       | 5.32 ms                                                | 5.60 ms: 1.05x slower                                              |
| scimark_lu                 | 114 ms                                                 | 121 ms: 1.06x slower                                               |
| mako                       | 10.7 ms                                                | 11.6 ms: 1.09x slower                                              |
| bench_thread_pool          | 818 us                                                 | 888 us: 1.09x slower                                               |
| many_optionals             | 857 us                                                 | 934 us: 1.09x slower                                               |
| json_loads                 | 27.2 us                                                | 29.7 us: 1.09x slower                                              |
| nbody                      | 87.7 ms                                                | 96.6 ms: 1.10x slower                                              |
| coverage                   | 82.8 ms                                                | 93.7 ms: 1.13x slower                                              |
| coroutines                 | 22.2 ms                                                | 25.7 ms: 1.16x slower                                              |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.16x slower                                              |
| subparsers                 | 15.5 ms                                                | 21.1 ms: 1.37x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 82.5 ms: 3.44x slower                                              |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (9): sphinx, sympy_expand, connected_components, scimark_sparse_mat_mult, xml_etree_generate, xml_etree_process, asyncio_websockets, scimark_monte_carlo, logging_format
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250430-3.14.0a7+-a054a83/bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x
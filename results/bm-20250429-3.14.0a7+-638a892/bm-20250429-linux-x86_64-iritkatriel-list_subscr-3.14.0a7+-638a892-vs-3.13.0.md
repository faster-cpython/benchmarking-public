# Results vs. 3.13.0

- fork: iritkatriel
- ref: list_subscr
- machine: linux-x86_64
- commit hash: 638a892
- commit date: 2025-04-29
- overall geometric mean: 1.050x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                               |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                             |
| html5lib       | 63.4 ms                                                | 62.2 ms: 1.02x faster                                              |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                               |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                               |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.17x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                               |
| async_generators           | 433 ms                                                 | 401 ms: 1.08x faster                                               |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.12x slower                                              |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.2 ms: 1.14x faster                                              |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                               |
| nbody          | 87.7 ms                                                | 96.3 ms: 1.10x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.1 ms: 1.21x faster                                              |
| regex_effbot   | 3.77 ms                                                | 3.14 ms: 1.20x faster                                              |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                               |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.13x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 143 ms: 1.08x faster                                               |
| tomli_loads          | 2.12 sec                                               | 1.98 sec: 1.07x faster                                             |
| xml_etree_iterparse  | 101 ms                                                 | 100 ms: 1.01x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 87.6 ms: 1.01x slower                                              |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                               |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.05x slower                                               |
| json_loads           | 27.2 us                                                | 30.0 us: 1.11x slower                                              |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.16x slower                                              |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                       |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.87 ms: 1.02x faster                                              |
| python_startup         | 12.7 ms                                                | 13.0 ms: 1.03x slower                                              |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 21.1 ms: 1.07x faster                                              |
| genshi_xml     | 50.5 ms                                                | 49.2 ms: 1.03x faster                                              |
| mako           | 10.7 ms                                                | 11.7 ms: 1.09x slower                                              |
| Geometric mean | (ref)                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.08x faster                                             |
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                               |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                               |
| deepcopy                   | 354 us                                                 | 258 us: 1.37x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 28.3 us: 1.36x faster                                              |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                               |
| go                         | 141 ms                                                 | 112 ms: 1.26x faster                                               |
| regex_v8                   | 26.9 ms                                                | 22.1 ms: 1.21x faster                                              |
| regex_effbot               | 3.77 ms                                                | 3.14 ms: 1.20x faster                                              |
| deepcopy_reduce            | 3.24 us                                                | 2.72 us: 1.19x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.17x faster                                               |
| float                      | 78.7 ms                                                | 69.2 ms: 1.14x faster                                              |
| pylint                     | 312 ms                                                 | 277 ms: 1.13x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                               |
| richards                   | 47.5 ms                                                | 43.4 ms: 1.10x faster                                              |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.08x faster                                               |
| pyflate                    | 470 ms                                                 | 433 ms: 1.08x faster                                               |
| dulwich_log                | 64.6 ms                                                | 59.7 ms: 1.08x faster                                              |
| richards_super             | 53.7 ms                                                | 49.7 ms: 1.08x faster                                              |
| async_generators           | 433 ms                                                 | 401 ms: 1.08x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 143 ms: 1.08x faster                                               |
| telco                      | 8.40 ms                                                | 7.80 ms: 1.08x faster                                              |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                              |
| tomli_loads                | 2.12 sec                                               | 1.98 sec: 1.07x faster                                             |
| regex_dna                  | 220 ms                                                 | 209 ms: 1.05x faster                                               |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                               |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                               |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.50 sec: 1.04x faster                                             |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                             |
| scimark_fft                | 367 ms                                                 | 356 ms: 1.03x faster                                               |
| logging_silent             | 101 ns                                                 | 98.2 ns: 1.03x faster                                              |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.03x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                             |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.03x faster                                               |
| genshi_xml                 | 50.5 ms                                                | 49.2 ms: 1.03x faster                                              |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                               |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                              |
| chaos                      | 58.0 ms                                                | 56.9 ms: 1.02x faster                                              |
| logging_format             | 6.23 us                                                | 6.11 us: 1.02x faster                                              |
| python_startup_no_site     | 7.00 ms                                                | 6.87 ms: 1.02x faster                                              |
| logging_simple             | 5.65 us                                                | 5.55 us: 1.02x faster                                              |
| html5lib                   | 63.4 ms                                                | 62.2 ms: 1.02x faster                                              |
| crypto_pyaes               | 74.7 ms                                                | 73.6 ms: 1.02x faster                                              |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.01x faster                                               |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.01x faster                                             |
| gc_traversal               | 4.90 ms                                                | 4.85 ms: 1.01x faster                                              |
| xml_etree_iterparse        | 101 ms                                                 | 100 ms: 1.01x faster                                               |
| sympy_expand               | 456 ms                                                 | 453 ms: 1.01x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.88 us: 1.01x faster                                              |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.01x faster                                               |
| nqueens                    | 80.9 ms                                                | 80.4 ms: 1.01x faster                                              |
| pprint_safe_repr           | 727 ms                                                 | 723 ms: 1.00x faster                                               |
| pprint_pformat             | 1.48 sec                                               | 1.47 sec: 1.00x faster                                             |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                               |
| xml_etree_generate         | 86.8 ms                                                | 87.6 ms: 1.01x slower                                              |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                             |
| connected_components       | 447 ms                                                 | 452 ms: 1.01x slower                                               |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                              |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                              |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.3 ms: 1.02x slower                                              |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.16 ms: 1.03x slower                                              |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                               |
| generators                 | 28.8 ms                                                | 29.6 ms: 1.03x slower                                              |
| python_startup             | 12.7 ms                                                | 13.0 ms: 1.03x slower                                              |
| json                       | 5.32 ms                                                | 5.50 ms: 1.03x slower                                              |
| fannkuch                   | 394 ms                                                 | 408 ms: 1.04x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.30 ms: 1.04x slower                                              |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                               |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.05x slower                                               |
| deltablue                  | 3.19 ms                                                | 3.38 ms: 1.06x slower                                              |
| bench_thread_pool          | 818 us                                                 | 885 us: 1.08x slower                                               |
| mako                       | 10.7 ms                                                | 11.7 ms: 1.09x slower                                              |
| many_optionals             | 857 us                                                 | 937 us: 1.09x slower                                               |
| nbody                      | 87.7 ms                                                | 96.3 ms: 1.10x slower                                              |
| json_loads                 | 27.2 us                                                | 30.0 us: 1.11x slower                                              |
| coverage                   | 82.8 ms                                                | 92.8 ms: 1.12x slower                                              |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.12x slower                                              |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.16x slower                                              |
| subparsers                 | 15.5 ms                                                | 21.1 ms: 1.37x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 82.0 ms: 3.42x slower                                              |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                       |

Benchmark hidden because not significant (6): raytrace, xml_etree_process, asyncio_websockets, scimark_monte_carlo, shortest_path, django_template
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250429-3.14.0a7+-638a892/bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.050x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
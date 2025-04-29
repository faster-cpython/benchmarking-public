# Results vs. 3.13.0

- fork: iritkatriel
- ref: array_subscr
- machine: linux-x86_64
- commit hash: 0cb6e84
- commit date: 2025-04-28
- overall geometric mean: 1.050x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                              |
| html5lib       | 63.4 ms                                                | 61.6 ms: 1.03x faster                                               |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 307 ms: 1.51x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 602 ms: 1.43x faster                                                |
| async_tree_io              | 838 ms                                                 | 590 ms: 1.42x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 482 ms: 1.19x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                |
| async_generators           | 433 ms                                                 | 396 ms: 1.09x faster                                                |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                               |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.4 ms: 1.13x faster                                               |
| pidigits       | 186 ms                                                 | 190 ms: 1.02x slower                                                |
| nbody          | 87.7 ms                                                | 97.8 ms: 1.12x slower                                               |
| Geometric mean | (ref)                                                  | 1.00x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.2 ms: 1.21x faster                                               |
| regex_effbot   | 3.77 ms                                                | 3.14 ms: 1.20x faster                                               |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                |
| regex_dna      | 220 ms                                                 | 208 ms: 1.06x faster                                                |
| Geometric mean | (ref)                                                  | 1.13x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                                |
| tomli_loads          | 2.12 sec                                               | 1.97 sec: 1.07x faster                                              |
| xml_etree_generate   | 86.8 ms                                                | 84.3 ms: 1.03x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 59.0 ms: 1.02x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 99.0 ms: 1.02x faster                                               |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                |
| pickle_pure_python   | 302 us                                                 | 314 us: 1.04x slower                                                |
| json_loads           | 27.2 us                                                | 30.4 us: 1.12x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.16x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.3 ms: 1.05x slower                                               |
| python_startup_no_site | 7.00 ms                                                | 8.24 ms: 1.18x slower                                               |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.06x faster                                               |
| genshi_xml      | 50.5 ms                                                | 49.9 ms: 1.01x faster                                               |
| django_template | 31.7 ms                                                | 31.5 ms: 1.00x faster                                               |
| mako            | 10.7 ms                                                | 11.6 ms: 1.09x slower                                               |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.21 sec: 2.10x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 307 ms: 1.51x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 602 ms: 1.43x faster                                                |
| async_tree_io              | 838 ms                                                 | 590 ms: 1.42x faster                                                |
| deepcopy                   | 354 us                                                 | 252 us: 1.41x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 28.7 us: 1.34x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                |
| go                         | 141 ms                                                 | 111 ms: 1.27x faster                                                |
| deepcopy_reduce            | 3.24 us                                                | 2.65 us: 1.22x faster                                               |
| regex_v8                   | 26.9 ms                                                | 22.2 ms: 1.21x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.14 ms: 1.20x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 482 ms: 1.19x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                |
| float                      | 78.7 ms                                                | 69.4 ms: 1.13x faster                                               |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                |
| richards                   | 47.5 ms                                                | 43.2 ms: 1.10x faster                                               |
| async_generators           | 433 ms                                                 | 396 ms: 1.09x faster                                                |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                                |
| dulwich_log                | 64.6 ms                                                | 59.3 ms: 1.09x faster                                               |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.08x faster                                                |
| richards_super             | 53.7 ms                                                | 49.7 ms: 1.08x faster                                               |
| telco                      | 8.40 ms                                                | 7.79 ms: 1.08x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.97 sec: 1.07x faster                                              |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                               |
| regex_dna                  | 220 ms                                                 | 208 ms: 1.06x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.45 sec: 1.05x faster                                              |
| logging_silent             | 101 ns                                                 | 96.3 ns: 1.05x faster                                               |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                              |
| chaos                      | 58.0 ms                                                | 56.0 ms: 1.04x faster                                               |
| pyflate                    | 470 ms                                                 | 454 ms: 1.03x faster                                                |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                               |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                              |
| sympy_str                  | 273 ms                                                 | 265 ms: 1.03x faster                                                |
| xml_etree_generate         | 86.8 ms                                                | 84.3 ms: 1.03x faster                                               |
| html5lib                   | 63.4 ms                                                | 61.6 ms: 1.03x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 59.0 ms: 1.02x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 99.0 ms: 1.02x faster                                               |
| crypto_pyaes               | 74.7 ms                                                | 73.1 ms: 1.02x faster                                               |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                              |
| pprint_safe_repr           | 727 ms                                                 | 713 ms: 1.02x faster                                                |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                |
| logging_format             | 6.23 us                                                | 6.13 us: 1.02x faster                                               |
| logging_simple             | 5.65 us                                                | 5.56 us: 1.02x faster                                               |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                                |
| sympy_expand               | 456 ms                                                 | 451 ms: 1.01x faster                                                |
| genshi_xml                 | 50.5 ms                                                | 49.9 ms: 1.01x faster                                               |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.01x faster                                              |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                |
| nqueens                    | 80.9 ms                                                | 80.2 ms: 1.01x faster                                               |
| raytrace                   | 262 ms                                                 | 260 ms: 1.00x faster                                                |
| django_template            | 31.7 ms                                                | 31.5 ms: 1.00x faster                                               |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.0 ms: 1.01x slower                                               |
| shortest_path              | 487 ms                                                 | 491 ms: 1.01x slower                                                |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                                |
| docutils                   | 2.58 sec                                               | 2.62 sec: 1.01x slower                                              |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                               |
| connected_components       | 447 ms                                                 | 454 ms: 1.02x slower                                                |
| gc_traversal               | 4.90 ms                                                | 4.98 ms: 1.02x slower                                               |
| pidigits                   | 186 ms                                                 | 190 ms: 1.02x slower                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 68.0 ms: 1.02x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.20 ms: 1.02x slower                                               |
| generators                 | 28.8 ms                                                | 29.5 ms: 1.02x slower                                               |
| pickle_pure_python         | 302 us                                                 | 314 us: 1.04x slower                                                |
| deltablue                  | 3.19 ms                                                | 3.32 ms: 1.04x slower                                               |
| scimark_fft                | 367 ms                                                 | 382 ms: 1.04x slower                                                |
| python_startup             | 12.7 ms                                                | 13.3 ms: 1.05x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                |
| fannkuch                   | 394 ms                                                 | 418 ms: 1.06x slower                                                |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                               |
| bench_thread_pool          | 818 us                                                 | 884 us: 1.08x slower                                                |
| scimark_lu                 | 114 ms                                                 | 124 ms: 1.08x slower                                                |
| mako                       | 10.7 ms                                                | 11.6 ms: 1.09x slower                                               |
| many_optionals             | 857 us                                                 | 933 us: 1.09x slower                                                |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.50 ms: 1.09x slower                                               |
| coverage                   | 82.8 ms                                                | 92.3 ms: 1.11x slower                                               |
| nbody                      | 87.7 ms                                                | 97.8 ms: 1.12x slower                                               |
| json_loads                 | 27.2 us                                                | 30.4 us: 1.12x slower                                               |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.16x slower                                               |
| python_startup_no_site     | 7.00 ms                                                | 8.24 ms: 1.18x slower                                               |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.1 ms: 3.42x slower                                               |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (5): pathlib, scimark_sor, asyncio_websockets, comprehensions, json
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250428-3.14.0a7+-0cb6e84/bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.050x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x
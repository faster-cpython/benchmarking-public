# Results vs. 3.13.0

- fork: iritkatriel
- ref: array_subscr
- machine: linux-x86_64
- commit hash: 933e225
- commit date: 2025-04-29
- overall geometric mean: 1.049x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 253 ms: 1.05x faster                                                |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                              |
| html5lib       | 63.4 ms                                                | 62.1 ms: 1.02x faster                                               |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 305 ms: 1.52x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 603 ms: 1.43x faster                                                |
| async_tree_io              | 838 ms                                                 | 595 ms: 1.41x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                                |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.18x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.14x faster                                                |
| async_generators           | 433 ms                                                 | 397 ms: 1.09x faster                                                |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                               |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 68.3 ms: 1.15x faster                                               |
| pidigits       | 186 ms                                                 | 194 ms: 1.04x slower                                                |
| nbody          | 87.7 ms                                                | 95.1 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.18 ms: 1.18x faster                                               |
| regex_v8       | 26.9 ms                                                | 23.3 ms: 1.15x faster                                               |
| regex_dna      | 220 ms                                                 | 204 ms: 1.08x faster                                                |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                |
| Geometric mean | (ref)                                                  | 1.12x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                |
| tomli_loads          | 2.12 sec                                               | 1.96 sec: 1.08x faster                                              |
| xml_etree_generate   | 86.8 ms                                                | 84.2 ms: 1.03x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 98.4 ms: 1.03x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 59.0 ms: 1.03x faster                                               |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                |
| pickle_pure_python   | 302 us                                                 | 317 us: 1.05x slower                                                |
| json_loads           | 27.2 us                                                | 30.0 us: 1.10x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.15x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.05x slower                                               |
| python_startup_no_site | 7.00 ms                                                | 8.20 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 20.8 ms: 1.09x faster                                               |
| genshi_xml     | 50.5 ms                                                | 49.2 ms: 1.03x faster                                               |
| mako           | 10.7 ms                                                | 11.6 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.09x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 305 ms: 1.52x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 603 ms: 1.43x faster                                                |
| async_tree_io              | 838 ms                                                 | 595 ms: 1.41x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                                |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                                |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 28.6 us: 1.34x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                |
| go                         | 141 ms                                                 | 114 ms: 1.24x faster                                                |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.20x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.18 ms: 1.18x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.18x faster                                                |
| regex_v8                   | 26.9 ms                                                | 23.3 ms: 1.15x faster                                               |
| float                      | 78.7 ms                                                | 68.3 ms: 1.15x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.14x faster                                                |
| pylint                     | 312 ms                                                 | 277 ms: 1.13x faster                                                |
| dulwich_log                | 64.6 ms                                                | 58.6 ms: 1.10x faster                                               |
| spectral_norm              | 113 ms                                                 | 103 ms: 1.10x faster                                                |
| richards                   | 47.5 ms                                                | 43.2 ms: 1.10x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                |
| async_generators           | 433 ms                                                 | 397 ms: 1.09x faster                                                |
| genshi_text                | 22.6 ms                                                | 20.8 ms: 1.09x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.96 sec: 1.08x faster                                              |
| regex_dna                  | 220 ms                                                 | 204 ms: 1.08x faster                                                |
| richards_super             | 53.7 ms                                                | 49.9 ms: 1.08x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.42 sec: 1.06x faster                                              |
| gc_traversal               | 4.90 ms                                                | 4.64 ms: 1.06x faster                                               |
| telco                      | 8.40 ms                                                | 7.95 ms: 1.06x faster                                               |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                |
| 2to3                       | 266 ms                                                 | 253 ms: 1.05x faster                                                |
| pyflate                    | 470 ms                                                 | 449 ms: 1.04x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                               |
| logging_silent             | 101 ns                                                 | 97.9 ns: 1.03x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 84.2 ms: 1.03x faster                                               |
| crypto_pyaes               | 74.7 ms                                                | 72.4 ms: 1.03x faster                                               |
| sympy_str                  | 273 ms                                                 | 265 ms: 1.03x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 98.4 ms: 1.03x faster                                               |
| chaos                      | 58.0 ms                                                | 56.4 ms: 1.03x faster                                               |
| genshi_xml                 | 50.5 ms                                                | 49.2 ms: 1.03x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 59.0 ms: 1.03x faster                                               |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                |
| html5lib                   | 63.4 ms                                                | 62.1 ms: 1.02x faster                                               |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                              |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.01x faster                                               |
| logging_simple             | 5.65 us                                                | 5.57 us: 1.01x faster                                               |
| sympy_expand               | 456 ms                                                 | 450 ms: 1.01x faster                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                                |
| pprint_safe_repr           | 727 ms                                                 | 721 ms: 1.01x faster                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                               |
| raytrace                   | 262 ms                                                 | 263 ms: 1.00x slower                                                |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.0 ms: 1.01x slower                                               |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                              |
| hexiom                     | 6.08 ms                                                | 6.14 ms: 1.01x slower                                               |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                |
| json                       | 5.32 ms                                                | 5.40 ms: 1.01x slower                                               |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                               |
| connected_components       | 447 ms                                                 | 455 ms: 1.02x slower                                                |
| generators                 | 28.8 ms                                                | 29.3 ms: 1.02x slower                                               |
| shortest_path              | 487 ms                                                 | 503 ms: 1.03x slower                                                |
| pidigits                   | 186 ms                                                 | 194 ms: 1.04x slower                                                |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.05x slower                                               |
| fannkuch                   | 394 ms                                                 | 412 ms: 1.05x slower                                                |
| pickle_pure_python         | 302 us                                                 | 317 us: 1.05x slower                                                |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                |
| scimark_fft                | 367 ms                                                 | 386 ms: 1.05x slower                                                |
| deltablue                  | 3.19 ms                                                | 3.40 ms: 1.07x slower                                               |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                               |
| scimark_lu                 | 114 ms                                                 | 123 ms: 1.07x slower                                                |
| bench_thread_pool          | 818 us                                                 | 886 us: 1.08x slower                                                |
| mako                       | 10.7 ms                                                | 11.6 ms: 1.08x slower                                               |
| nbody                      | 87.7 ms                                                | 95.1 ms: 1.09x slower                                               |
| scimark_monte_carlo        | 66.8 ms                                                | 72.6 ms: 1.09x slower                                               |
| many_optionals             | 857 us                                                 | 932 us: 1.09x slower                                                |
| json_loads                 | 27.2 us                                                | 30.0 us: 1.10x slower                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.63 ms: 1.12x slower                                               |
| coverage                   | 82.8 ms                                                | 93.1 ms: 1.12x slower                                               |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.15x slower                                               |
| python_startup_no_site     | 7.00 ms                                                | 8.20 ms: 1.17x slower                                               |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.36x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.2 ms: 3.43x slower                                               |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (6): nqueens, pprint_pformat, scimark_sor, asyncio_websockets, logging_format, django_template
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250429-3.14.0a7+-933e225/bm-20250429-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-933e225.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x
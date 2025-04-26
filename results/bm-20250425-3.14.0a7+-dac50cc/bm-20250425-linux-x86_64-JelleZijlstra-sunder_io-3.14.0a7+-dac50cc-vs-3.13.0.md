# Results vs. 3.13.0

- fork: JelleZijlstra
- ref: sunder_io
- machine: linux-x86_64
- commit hash: dac50cc
- commit date: 2025-04-25
- overall geometric mean: 1.051x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                               |
| html5lib       | 63.4 ms                                                | 59.6 ms: 1.06x faster                                              |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                               |
| async_tree_io              | 838 ms                                                 | 593 ms: 1.41x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                               |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 489 ms: 1.11x faster                                               |
| async_generators           | 433 ms                                                 | 403 ms: 1.08x faster                                               |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                              |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 68.4 ms: 1.15x faster                                              |
| pidigits       | 186 ms                                                 | 195 ms: 1.05x slower                                               |
| nbody          | 87.7 ms                                                | 99.4 ms: 1.13x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.1 ms: 1.21x faster                                              |
| regex_effbot   | 3.77 ms                                                | 3.19 ms: 1.18x faster                                              |
| regex_compile  | 132 ms                                                 | 125 ms: 1.05x faster                                               |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.12x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.96 sec: 1.08x faster                                             |
| xml_etree_parse      | 154 ms                                                 | 143 ms: 1.08x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 98.8 ms: 1.03x faster                                              |
| xml_etree_generate   | 86.8 ms                                                | 84.9 ms: 1.02x faster                                              |
| xml_etree_process    | 60.5 ms                                                | 59.5 ms: 1.02x faster                                              |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                               |
| pickle_pure_python   | 302 us                                                 | 312 us: 1.03x slower                                               |
| json_loads           | 27.2 us                                                | 30.4 us: 1.12x slower                                              |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.16x slower                                              |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.90 ms: 1.01x faster                                              |
| python_startup         | 12.7 ms                                                | 13.3 ms: 1.05x slower                                              |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.2 ms: 1.07x faster                                              |
| genshi_xml      | 50.5 ms                                                | 49.5 ms: 1.02x faster                                              |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                              |
| mako            | 10.7 ms                                                | 11.7 ms: 1.10x slower                                              |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.08x faster                                             |
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                               |
| async_tree_io              | 838 ms                                                 | 593 ms: 1.41x faster                                               |
| deepcopy                   | 354 us                                                 | 253 us: 1.40x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 28.4 us: 1.35x faster                                              |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                               |
| go                         | 141 ms                                                 | 113 ms: 1.24x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.22x faster                                              |
| regex_v8                   | 26.9 ms                                                | 22.1 ms: 1.21x faster                                              |
| regex_effbot               | 3.77 ms                                                | 3.19 ms: 1.18x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.16x faster                                               |
| float                      | 78.7 ms                                                | 68.4 ms: 1.15x faster                                              |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 489 ms: 1.11x faster                                               |
| richards                   | 47.5 ms                                                | 43.0 ms: 1.11x faster                                              |
| dulwich_log                | 64.6 ms                                                | 59.2 ms: 1.09x faster                                              |
| spectral_norm              | 113 ms                                                 | 105 ms: 1.08x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.96 sec: 1.08x faster                                             |
| xml_etree_parse            | 154 ms                                                 | 143 ms: 1.08x faster                                               |
| richards_super             | 53.7 ms                                                | 49.9 ms: 1.08x faster                                              |
| async_generators           | 433 ms                                                 | 403 ms: 1.08x faster                                               |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.07x faster                                              |
| telco                      | 8.40 ms                                                | 7.89 ms: 1.06x faster                                              |
| html5lib                   | 63.4 ms                                                | 59.6 ms: 1.06x faster                                              |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.76 ms: 1.06x faster                                              |
| regex_compile              | 132 ms                                                 | 125 ms: 1.05x faster                                               |
| logging_silent             | 101 ns                                                 | 96.0 ns: 1.05x faster                                              |
| regex_dna                  | 220 ms                                                 | 209 ms: 1.05x faster                                               |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                               |
| sympy_integrate            | 19.8 ms                                                | 18.9 ms: 1.05x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.49 sec: 1.04x faster                                             |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                             |
| pyflate                    | 470 ms                                                 | 454 ms: 1.03x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                             |
| sympy_str                  | 273 ms                                                 | 265 ms: 1.03x faster                                               |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                               |
| scimark_fft                | 367 ms                                                 | 356 ms: 1.03x faster                                               |
| crypto_pyaes               | 74.7 ms                                                | 72.7 ms: 1.03x faster                                              |
| xml_etree_iterparse        | 101 ms                                                 | 98.8 ms: 1.03x faster                                              |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                              |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                             |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 84.9 ms: 1.02x faster                                              |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.84 us: 1.02x faster                                              |
| logging_simple             | 5.65 us                                                | 5.54 us: 1.02x faster                                              |
| genshi_xml                 | 50.5 ms                                                | 49.5 ms: 1.02x faster                                              |
| chaos                      | 58.0 ms                                                | 56.9 ms: 1.02x faster                                              |
| xml_etree_process          | 60.5 ms                                                | 59.5 ms: 1.02x faster                                              |
| logging_format             | 6.23 us                                                | 6.13 us: 1.02x faster                                              |
| python_startup_no_site     | 7.00 ms                                                | 6.90 ms: 1.01x faster                                              |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                               |
| sympy_expand               | 456 ms                                                 | 451 ms: 1.01x faster                                               |
| gc_traversal               | 4.90 ms                                                | 4.84 ms: 1.01x faster                                              |
| nqueens                    | 80.9 ms                                                | 80.5 ms: 1.00x faster                                              |
| raytrace                   | 262 ms                                                 | 263 ms: 1.01x slower                                               |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.0 ms: 1.01x slower                                              |
| hexiom                     | 6.08 ms                                                | 6.15 ms: 1.01x slower                                              |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                              |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                              |
| connected_components       | 447 ms                                                 | 456 ms: 1.02x slower                                               |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                               |
| generators                 | 28.8 ms                                                | 29.5 ms: 1.03x slower                                              |
| comprehensions             | 16.5 us                                                | 16.9 us: 1.03x slower                                              |
| pickle_pure_python         | 302 us                                                 | 312 us: 1.03x slower                                               |
| shortest_path              | 487 ms                                                 | 504 ms: 1.04x slower                                               |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                               |
| pidigits                   | 186 ms                                                 | 195 ms: 1.05x slower                                               |
| python_startup             | 12.7 ms                                                | 13.3 ms: 1.05x slower                                              |
| fannkuch                   | 394 ms                                                 | 415 ms: 1.05x slower                                               |
| json                       | 5.32 ms                                                | 5.62 ms: 1.05x slower                                              |
| deltablue                  | 3.19 ms                                                | 3.41 ms: 1.07x slower                                              |
| bench_thread_pool          | 818 us                                                 | 885 us: 1.08x slower                                               |
| many_optionals             | 857 us                                                 | 934 us: 1.09x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 175 us: 1.09x slower                                               |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                              |
| mako                       | 10.7 ms                                                | 11.7 ms: 1.10x slower                                              |
| json_loads                 | 27.2 us                                                | 30.4 us: 1.12x slower                                              |
| coverage                   | 82.8 ms                                                | 92.8 ms: 1.12x slower                                              |
| nbody                      | 87.7 ms                                                | 99.4 ms: 1.13x slower                                              |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.16x slower                                              |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 82.4 ms: 3.44x slower                                              |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                       |

Benchmark hidden because not significant (5): scimark_monte_carlo, asyncio_websockets, pprint_pformat, pprint_safe_repr, docutils
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250425-3.14.0a7+-dac50cc/bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x
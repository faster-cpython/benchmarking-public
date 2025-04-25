# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_cached_consts_un
- machine: linux-x86_64
- commit hash: 7e6d8a4
- commit date: 2025-04-24
- overall geometric mean: 1.053x faster
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                         |
| docutils       | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                         |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                         |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 486 ms: 1.12x faster                                                         |
| async_generators           | 433 ms                                                 | 422 ms: 1.03x faster                                                         |
| coroutines                 | 22.2 ms                                                | 24.7 ms: 1.11x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.5 ms: 1.13x faster                                                        |
| pidigits       | 186 ms                                                 | 190 ms: 1.02x slower                                                         |
| nbody          | 87.7 ms                                                | 89.3 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.18 ms: 1.19x faster                                                        |
| regex_v8       | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                        |
| regex_dna      | 220 ms                                                 | 204 ms: 1.08x faster                                                         |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                       |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 79.7 ms: 1.09x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 55.8 ms: 1.08x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 98.4 ms: 1.03x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 208 us: 1.03x faster                                                         |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.06x slower                                                         |
| json_loads           | 27.2 us                                                | 30.2 us: 1.11x slower                                                        |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.3 ms: 1.05x slower                                                        |
| python_startup_no_site | 7.00 ms                                                | 8.27 ms: 1.18x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                        |
| genshi_xml      | 50.5 ms                                                | 49.5 ms: 1.02x faster                                                        |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                        |
| mako            | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.21 sec: 2.10x faster                                                       |
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                                         |
| deepcopy                   | 354 us                                                 | 253 us: 1.40x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                         |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                         |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                         |
| richards                   | 47.5 ms                                                | 36.2 ms: 1.31x faster                                                        |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                                        |
| richards_super             | 53.7 ms                                                | 41.1 ms: 1.31x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.21x faster                                                        |
| regex_effbot               | 3.77 ms                                                | 3.18 ms: 1.19x faster                                                        |
| scimark_fft                | 367 ms                                                 | 312 ms: 1.18x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                         |
| tomli_loads                | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                       |
| float                      | 78.7 ms                                                | 69.5 ms: 1.13x faster                                                        |
| spectral_norm              | 113 ms                                                 | 100 ms: 1.13x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                        |
| go                         | 141 ms                                                 | 125 ms: 1.13x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 486 ms: 1.12x faster                                                         |
| pylint                     | 312 ms                                                 | 285 ms: 1.09x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                         |
| telco                      | 8.40 ms                                                | 7.70 ms: 1.09x faster                                                        |
| xml_etree_generate         | 86.8 ms                                                | 79.7 ms: 1.09x faster                                                        |
| pyflate                    | 470 ms                                                 | 433 ms: 1.09x faster                                                         |
| xml_etree_process          | 60.5 ms                                                | 55.8 ms: 1.08x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.65 ms: 1.08x faster                                                        |
| regex_dna                  | 220 ms                                                 | 204 ms: 1.08x faster                                                         |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.39 sec: 1.07x faster                                                       |
| deltablue                  | 3.19 ms                                                | 3.00 ms: 1.06x faster                                                        |
| dulwich_log                | 64.6 ms                                                | 61.2 ms: 1.06x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.05x faster                                                       |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                                        |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                                       |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                                        |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 98.4 ms: 1.03x faster                                                        |
| async_generators           | 433 ms                                                 | 422 ms: 1.03x faster                                                         |
| unpickle_pure_python       | 213 us                                                 | 208 us: 1.03x faster                                                         |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                                        |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                         |
| genshi_xml                 | 50.5 ms                                                | 49.5 ms: 1.02x faster                                                        |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                         |
| logging_simple             | 5.65 us                                                | 5.56 us: 1.02x faster                                                        |
| crypto_pyaes               | 74.7 ms                                                | 73.9 ms: 1.01x faster                                                        |
| sympy_str                  | 273 ms                                                 | 270 ms: 1.01x faster                                                         |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                         |
| pprint_safe_repr           | 727 ms                                                 | 733 ms: 1.01x slower                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 134 ms: 1.01x slower                                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 67.5 ms: 1.01x slower                                                        |
| chaos                      | 58.0 ms                                                | 58.8 ms: 1.01x slower                                                        |
| shortest_path              | 487 ms                                                 | 493 ms: 1.01x slower                                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                                        |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                        |
| nqueens                    | 80.9 ms                                                | 82.3 ms: 1.02x slower                                                        |
| pidigits                   | 186 ms                                                 | 190 ms: 1.02x slower                                                         |
| nbody                      | 87.7 ms                                                | 89.3 ms: 1.02x slower                                                        |
| sympy_expand               | 456 ms                                                 | 465 ms: 1.02x slower                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                        |
| raytrace                   | 262 ms                                                 | 268 ms: 1.03x slower                                                         |
| gc_traversal               | 4.90 ms                                                | 5.03 ms: 1.03x slower                                                        |
| json                       | 5.32 ms                                                | 5.49 ms: 1.03x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                       |
| connected_components       | 447 ms                                                 | 464 ms: 1.04x slower                                                         |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                        |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                         |
| fannkuch                   | 394 ms                                                 | 413 ms: 1.05x slower                                                         |
| python_startup             | 12.7 ms                                                | 13.3 ms: 1.05x slower                                                        |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.06x slower                                                         |
| generators                 | 28.8 ms                                                | 30.4 ms: 1.06x slower                                                        |
| typing_runtime_protocols   | 160 us                                                 | 171 us: 1.07x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 894 us: 1.09x slower                                                         |
| hexiom                     | 6.08 ms                                                | 6.64 ms: 1.09x slower                                                        |
| coroutines                 | 22.2 ms                                                | 24.7 ms: 1.11x slower                                                        |
| many_optionals             | 857 us                                                 | 953 us: 1.11x slower                                                         |
| json_loads                 | 27.2 us                                                | 30.2 us: 1.11x slower                                                        |
| comprehensions             | 16.5 us                                                | 18.6 us: 1.13x slower                                                        |
| coverage                   | 82.8 ms                                                | 93.7 ms: 1.13x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                        |
| python_startup_no_site     | 7.00 ms                                                | 8.27 ms: 1.18x slower                                                        |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.8 ms: 3.41x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (6): sphinx, html5lib, pprint_pformat, asyncio_websockets, logging_format, logging_silent
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250424-3.14.0a7+-7e6d8a4-JIT/bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 99.84% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x
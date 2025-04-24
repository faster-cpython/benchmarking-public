# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_cached_consts
- machine: linux-x86_64
- commit hash: d7c354b
- commit date: 2025-04-24
- overall geometric mean: 1.053x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                      |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                    |
| html5lib       | 63.4 ms                                                | 60.2 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 618 ms: 1.39x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                      |
| async_tree_io              | 838 ms                                                 | 614 ms: 1.36x faster                                                      |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 493 ms: 1.10x faster                                                      |
| async_generators           | 433 ms                                                 | 417 ms: 1.04x faster                                                      |
| coroutines                 | 22.2 ms                                                | 25.4 ms: 1.14x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.3 ms: 1.12x faster                                                     |
| pidigits       | 186 ms                                                 | 191 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.16 ms: 1.19x faster                                                     |
| regex_v8       | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                     |
| regex_dna      | 220 ms                                                 | 202 ms: 1.09x faster                                                      |
| regex_compile  | 132 ms                                                 | 126 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.85 sec: 1.14x faster                                                    |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                      |
| xml_etree_generate   | 86.8 ms                                                | 80.5 ms: 1.08x faster                                                     |
| xml_etree_process    | 60.5 ms                                                | 56.3 ms: 1.07x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 98.6 ms: 1.03x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 209 us: 1.02x faster                                                      |
| pickle_pure_python   | 302 us                                                 | 323 us: 1.07x slower                                                      |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                     |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                     |
| python_startup_no_site | 7.00 ms                                                | 8.21 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                     |
| genshi_xml      | 50.5 ms                                                | 50.1 ms: 1.01x faster                                                     |
| django_template | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                     |
| mako            | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.21 sec: 2.10x faster                                                    |
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                      |
| deepcopy                   | 354 us                                                 | 252 us: 1.40x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 618 ms: 1.39x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                      |
| async_tree_io              | 838 ms                                                 | 614 ms: 1.36x faster                                                      |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                      |
| richards                   | 47.5 ms                                                | 35.6 ms: 1.34x faster                                                     |
| richards_super             | 53.7 ms                                                | 40.8 ms: 1.32x faster                                                     |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.20x faster                                                     |
| regex_effbot               | 3.77 ms                                                | 3.16 ms: 1.19x faster                                                     |
| scimark_fft                | 367 ms                                                 | 315 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 1.85 sec: 1.14x faster                                                    |
| regex_v8                   | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                     |
| float                      | 78.7 ms                                                | 70.3 ms: 1.12x faster                                                     |
| go                         | 141 ms                                                 | 126 ms: 1.12x faster                                                      |
| pyflate                    | 470 ms                                                 | 422 ms: 1.11x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 493 ms: 1.10x faster                                                      |
| telco                      | 8.40 ms                                                | 7.65 ms: 1.10x faster                                                     |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                                      |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                      |
| regex_dna                  | 220 ms                                                 | 202 ms: 1.09x faster                                                      |
| spectral_norm              | 113 ms                                                 | 105 ms: 1.08x faster                                                      |
| xml_etree_generate         | 86.8 ms                                                | 80.5 ms: 1.08x faster                                                     |
| xml_etree_process          | 60.5 ms                                                | 56.3 ms: 1.07x faster                                                     |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                     |
| deltablue                  | 3.19 ms                                                | 2.99 ms: 1.07x faster                                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.43 sec: 1.06x faster                                                    |
| dulwich_log                | 64.6 ms                                                | 61.0 ms: 1.06x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.75 ms: 1.06x faster                                                     |
| html5lib                   | 63.4 ms                                                | 60.2 ms: 1.05x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                                    |
| regex_compile              | 132 ms                                                 | 126 ms: 1.04x faster                                                      |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                                     |
| async_generators           | 433 ms                                                 | 417 ms: 1.04x faster                                                      |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                    |
| xml_etree_iterparse        | 101 ms                                                 | 98.6 ms: 1.03x faster                                                     |
| sympy_integrate            | 19.8 ms                                                | 19.3 ms: 1.03x faster                                                     |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                      |
| unpickle_pure_python       | 213 us                                                 | 209 us: 1.02x faster                                                      |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.02x faster                                                     |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                      |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                      |
| gc_traversal               | 4.90 ms                                                | 4.82 ms: 1.01x faster                                                     |
| sympy_str                  | 273 ms                                                 | 270 ms: 1.01x faster                                                      |
| genshi_xml                 | 50.5 ms                                                | 50.1 ms: 1.01x faster                                                     |
| logging_simple             | 5.65 us                                                | 5.68 us: 1.01x slower                                                     |
| scimark_monte_carlo        | 66.8 ms                                                | 67.2 ms: 1.01x slower                                                     |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                     |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.1 ms: 1.01x slower                                                     |
| nqueens                    | 80.9 ms                                                | 81.8 ms: 1.01x slower                                                     |
| connected_components       | 447 ms                                                 | 452 ms: 1.01x slower                                                      |
| shortest_path              | 487 ms                                                 | 495 ms: 1.02x slower                                                      |
| chaos                      | 58.0 ms                                                | 59.1 ms: 1.02x slower                                                     |
| pidigits                   | 186 ms                                                 | 191 ms: 1.02x slower                                                      |
| sympy_expand               | 456 ms                                                 | 468 ms: 1.03x slower                                                      |
| django_template            | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                     |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                    |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                                      |
| generators                 | 28.8 ms                                                | 29.7 ms: 1.03x slower                                                     |
| json                       | 5.32 ms                                                | 5.54 ms: 1.04x slower                                                     |
| fannkuch                   | 394 ms                                                 | 411 ms: 1.04x slower                                                      |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                     |
| mako                       | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                     |
| scimark_lu                 | 114 ms                                                 | 120 ms: 1.05x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 323 us: 1.07x slower                                                      |
| typing_runtime_protocols   | 160 us                                                 | 173 us: 1.08x slower                                                      |
| hexiom                     | 6.08 ms                                                | 6.64 ms: 1.09x slower                                                     |
| bench_thread_pool          | 818 us                                                 | 895 us: 1.09x slower                                                      |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                     |
| many_optionals             | 857 us                                                 | 955 us: 1.11x slower                                                      |
| comprehensions             | 16.5 us                                                | 18.5 us: 1.12x slower                                                     |
| coverage                   | 82.8 ms                                                | 93.4 ms: 1.13x slower                                                     |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.13x slower                                                     |
| coroutines                 | 22.2 ms                                                | 25.4 ms: 1.14x slower                                                     |
| python_startup_no_site     | 7.00 ms                                                | 8.21 ms: 1.17x slower                                                     |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 81.4 ms: 3.40x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (10): sphinx, nbody, logging_silent, crypto_pyaes, pprint_safe_repr, sqlalchemy_declarative, meteor_contest, asyncio_websockets, pprint_pformat, logging_format
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250424-3.14.0a7+-d7c354b-JIT/bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x
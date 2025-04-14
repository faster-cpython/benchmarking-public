# Results vs. 3.13.0

- fork: brandtbucher
- ref: unbox_unsigned
- machine: linux-x86_64
- commit hash: f31fd63
- commit date: 2025-04-01
- overall geometric mean: 1.022x faster
- HPT reliability: 60.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 264 ms: 1.01x faster                                                   |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.02x slower                                                 |
| html5lib       | 63.4 ms                                                | 63.8 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 326 ms: 1.42x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 634 ms: 1.36x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.35x faster                                                   |
| async_tree_io              | 838 ms                                                 | 631 ms: 1.33x faster                                                   |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 257 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                   |
| async_generators           | 433 ms                                                 | 400 ms: 1.08x faster                                                   |
| coroutines                 | 22.2 ms                                                | 21.6 ms: 1.03x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 75.0 ms: 1.05x faster                                                  |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                   |
| nbody          | 87.7 ms                                                | 98.1 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.30 ms: 1.14x faster                                                  |
| regex_v8       | 26.9 ms                                                | 23.5 ms: 1.14x faster                                                  |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                                   |
| regex_compile  | 132 ms                                                 | 133 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.88 sec: 1.13x faster                                                 |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 99.8 ms: 1.01x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 86.1 ms: 1.01x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 60.0 ms: 1.01x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 230 us: 1.08x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 333 us: 1.10x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.14x slower                                                  |
| json_loads           | 27.2 us                                                | 32.3 us: 1.19x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 8.23 ms: 1.18x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.9 ms: 1.03x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 49.7 ms: 1.02x faster                                                  |
| django_template | 31.7 ms                                                | 32.7 ms: 1.03x slower                                                  |
| mako            | 10.7 ms                                                | 12.3 ms: 1.15x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.25 sec: 2.03x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 326 ms: 1.42x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 634 ms: 1.36x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.35x faster                                                   |
| deepcopy                   | 354 us                                                 | 262 us: 1.35x faster                                                   |
| async_tree_io              | 838 ms                                                 | 631 ms: 1.33x faster                                                   |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 257 ms: 1.24x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 31.2 us: 1.23x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.77 us: 1.17x faster                                                  |
| spectral_norm              | 113 ms                                                 | 97.4 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.30 ms: 1.14x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 23.5 ms: 1.14x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.88 sec: 1.13x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                   |
| go                         | 141 ms                                                 | 126 ms: 1.12x faster                                                   |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                   |
| async_generators           | 433 ms                                                 | 400 ms: 1.08x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 60.4 ms: 1.07x faster                                                  |
| float                      | 78.7 ms                                                | 75.0 ms: 1.05x faster                                                  |
| telco                      | 8.40 ms                                                | 8.01 ms: 1.05x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.6 ms: 1.05x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.51 sec: 1.04x faster                                                 |
| genshi_text                | 22.6 ms                                                | 21.9 ms: 1.03x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                                  |
| coroutines                 | 22.2 ms                                                | 21.6 ms: 1.03x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 49.7 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 99.8 ms: 1.01x faster                                                  |
| regex_dna                  | 220 ms                                                 | 217 ms: 1.01x faster                                                   |
| richards                   | 47.5 ms                                                | 47.1 ms: 1.01x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 86.1 ms: 1.01x faster                                                  |
| richards_super             | 53.7 ms                                                | 53.3 ms: 1.01x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 60.0 ms: 1.01x faster                                                  |
| 2to3                       | 266 ms                                                 | 264 ms: 1.01x faster                                                   |
| generators                 | 28.8 ms                                                | 28.6 ms: 1.00x faster                                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                   |
| gc_traversal               | 4.90 ms                                                | 4.91 ms: 1.00x slower                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 133 ms: 1.00x slower                                                   |
| sympy_integrate            | 19.8 ms                                                | 19.9 ms: 1.00x slower                                                  |
| html5lib                   | 63.4 ms                                                | 63.8 ms: 1.01x slower                                                  |
| regex_compile              | 132 ms                                                 | 133 ms: 1.01x slower                                                   |
| sympy_str                  | 273 ms                                                 | 275 ms: 1.01x slower                                                   |
| pyflate                    | 470 ms                                                 | 474 ms: 1.01x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 153 ms: 1.01x slower                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                                  |
| connected_components       | 447 ms                                                 | 456 ms: 1.02x slower                                                   |
| shortest_path              | 487 ms                                                 | 498 ms: 1.02x slower                                                   |
| sympy_expand               | 456 ms                                                 | 467 ms: 1.02x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.02x slower                                                 |
| logging_simple             | 5.65 us                                                | 5.80 us: 1.03x slower                                                  |
| coverage                   | 82.8 ms                                                | 85.2 ms: 1.03x slower                                                  |
| nqueens                    | 80.9 ms                                                | 83.2 ms: 1.03x slower                                                  |
| logging_format             | 6.23 us                                                | 6.42 us: 1.03x slower                                                  |
| json                       | 5.32 ms                                                | 5.50 ms: 1.03x slower                                                  |
| django_template            | 31.7 ms                                                | 32.7 ms: 1.03x slower                                                  |
| chaos                      | 58.0 ms                                                | 60.0 ms: 1.03x slower                                                  |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                  |
| scimark_fft                | 367 ms                                                 | 383 ms: 1.04x slower                                                   |
| logging_silent             | 101 ns                                                 | 106 ns: 1.05x slower                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 70.0 ms: 1.05x slower                                                  |
| scimark_sor                | 122 ms                                                 | 128 ms: 1.05x slower                                                   |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.41 ms: 1.05x slower                                                  |
| raytrace                   | 262 ms                                                 | 278 ms: 1.06x slower                                                   |
| comprehensions             | 16.5 us                                                | 17.5 us: 1.06x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 777 ms: 1.07x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.59 sec: 1.07x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 230 us: 1.08x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 889 us: 1.09x slower                                                   |
| scimark_lu                 | 114 ms                                                 | 125 ms: 1.09x slower                                                   |
| crypto_pyaes               | 74.7 ms                                                | 81.7 ms: 1.09x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 333 us: 1.10x slower                                                   |
| fannkuch                   | 394 ms                                                 | 435 ms: 1.11x slower                                                   |
| nbody                      | 87.7 ms                                                | 98.1 ms: 1.12x slower                                                  |
| many_optionals             | 857 us                                                 | 972 us: 1.13x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.14x slower                                                  |
| mako                       | 10.7 ms                                                | 12.3 ms: 1.15x slower                                                  |
| deltablue                  | 3.19 ms                                                | 3.74 ms: 1.17x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 8.23 ms: 1.18x slower                                                  |
| json_loads                 | 27.2 us                                                | 32.3 us: 1.19x slower                                                  |
| subparsers                 | 15.5 ms                                                | 21.5 ms: 1.39x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 84.1 ms: 3.51x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (5): pycparser, scimark_sparse_mat_mult, meteor_contest, asyncio_websockets, sphinx
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250401-3.14.0a6+-f31fd63/bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.022x faster

# HPT report

- Reliability score: 60.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
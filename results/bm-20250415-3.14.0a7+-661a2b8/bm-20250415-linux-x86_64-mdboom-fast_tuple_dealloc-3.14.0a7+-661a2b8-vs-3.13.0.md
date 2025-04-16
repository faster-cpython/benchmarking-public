# Results vs. 3.13.0

- fork: mdboom
- ref: fast_tuple_dealloc
- machine: linux-x86_64
- commit hash: 661a2b8
- commit date: 2025-04-15
- overall geometric mean: 1.044x faster
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 262 ms: 1.02x faster                                                 |
| docutils       | 2.58 sec                                               | 3.21 sec: 1.24x slower                                               |
| html5lib       | 63.4 ms                                                | 60.5 ms: 1.05x faster                                                |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 310 ms: 1.41x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                 |
| async_tree_io              | 838 ms                                                 | 611 ms: 1.37x faster                                                 |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                                 |
| async_generators           | 433 ms                                                 | 401 ms: 1.08x faster                                                 |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                                |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                         |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.1 ms: 1.14x faster                                                |
| pidigits       | 186 ms                                                 | 198 ms: 1.06x slower                                                 |
| nbody          | 87.7 ms                                                | 94.6 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.15 ms: 1.19x faster                                                |
| regex_v8       | 26.9 ms                                                | 22.7 ms: 1.18x faster                                                |
| regex_dna      | 220 ms                                                 | 203 ms: 1.09x faster                                                 |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                 |
| tomli_loads          | 2.12 sec                                               | 1.98 sec: 1.07x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 58.6 ms: 1.03x faster                                                |
| xml_etree_generate   | 86.8 ms                                                | 84.4 ms: 1.03x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 98.7 ms: 1.03x faster                                                |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.06x slower                                                 |
| json_loads           | 27.2 us                                                | 29.5 us: 1.09x slower                                                |
| json_dumps           | 10.1 ms                                                | 12.1 ms: 1.20x slower                                                |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.3 ms: 1.05x slower                                                |
| python_startup_no_site | 7.00 ms                                                | 8.24 ms: 1.18x slower                                                |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.0 ms: 1.07x faster                                                |
| genshi_xml      | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                |
| django_template | 31.7 ms                                                | 31.3 ms: 1.01x faster                                                |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.25 sec: 2.03x faster                                               |
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 310 ms: 1.41x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                 |
| deepcopy                   | 354 us                                                 | 254 us: 1.40x faster                                                 |
| async_tree_io              | 838 ms                                                 | 611 ms: 1.37x faster                                                 |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                                 |
| deepcopy_memo              | 38.4 us                                                | 29.7 us: 1.29x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                 |
| go                         | 141 ms                                                 | 114 ms: 1.24x faster                                                 |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.20x faster                                                |
| regex_effbot               | 3.77 ms                                                | 3.15 ms: 1.19x faster                                                |
| regex_v8                   | 26.9 ms                                                | 22.7 ms: 1.18x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                 |
| float                      | 78.7 ms                                                | 69.1 ms: 1.14x faster                                                |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                                 |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                 |
| richards                   | 47.5 ms                                                | 43.6 ms: 1.09x faster                                                |
| richards_super             | 53.7 ms                                                | 49.4 ms: 1.09x faster                                                |
| regex_dna                  | 220 ms                                                 | 203 ms: 1.09x faster                                                 |
| async_generators           | 433 ms                                                 | 401 ms: 1.08x faster                                                 |
| dulwich_log                | 64.6 ms                                                | 59.7 ms: 1.08x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.0 ms: 1.07x faster                                                |
| tomli_loads                | 2.12 sec                                               | 1.98 sec: 1.07x faster                                               |
| telco                      | 8.40 ms                                                | 7.86 ms: 1.07x faster                                                |
| spectral_norm              | 113 ms                                                 | 106 ms: 1.06x faster                                                 |
| pyflate                    | 470 ms                                                 | 447 ms: 1.05x faster                                                 |
| html5lib                   | 63.4 ms                                                | 60.5 ms: 1.05x faster                                                |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.86 ms: 1.04x faster                                                |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                                |
| xml_etree_process          | 60.5 ms                                                | 58.6 ms: 1.03x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 19.3 ms: 1.03x faster                                                |
| xml_etree_generate         | 86.8 ms                                                | 84.4 ms: 1.03x faster                                                |
| logging_silent             | 101 ns                                                 | 98.2 ns: 1.03x faster                                                |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                 |
| scimark_fft                | 367 ms                                                 | 358 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 98.7 ms: 1.03x faster                                                |
| chaos                      | 58.0 ms                                                | 56.6 ms: 1.02x faster                                                |
| sqlite_synth               | 2.90 us                                                | 2.84 us: 1.02x faster                                                |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                               |
| 2to3                       | 266 ms                                                 | 262 ms: 1.02x faster                                                 |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.02x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                |
| crypto_pyaes               | 74.7 ms                                                | 73.9 ms: 1.01x faster                                                |
| pprint_safe_repr           | 727 ms                                                 | 719 ms: 1.01x faster                                                 |
| django_template            | 31.7 ms                                                | 31.3 ms: 1.01x faster                                                |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.01x faster                                               |
| logging_simple             | 5.65 us                                                | 5.60 us: 1.01x faster                                                |
| raytrace                   | 262 ms                                                 | 264 ms: 1.01x slower                                                 |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.1 ms: 1.01x slower                                                |
| shortest_path              | 487 ms                                                 | 492 ms: 1.01x slower                                                 |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                                |
| sympy_expand               | 456 ms                                                 | 463 ms: 1.01x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 68.2 ms: 1.02x slower                                                |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                 |
| generators                 | 28.8 ms                                                | 29.5 ms: 1.02x slower                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 137 ms: 1.03x slower                                                 |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.32 ms: 1.04x slower                                                |
| gc_traversal               | 4.90 ms                                                | 5.11 ms: 1.04x slower                                                |
| python_startup             | 12.7 ms                                                | 13.3 ms: 1.05x slower                                                |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.05x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.06x slower                                                 |
| deltablue                  | 3.19 ms                                                | 3.37 ms: 1.06x slower                                                |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                |
| pidigits                   | 186 ms                                                 | 198 ms: 1.06x slower                                                 |
| coverage                   | 82.8 ms                                                | 88.4 ms: 1.07x slower                                                |
| many_optionals             | 857 us                                                 | 921 us: 1.07x slower                                                 |
| nbody                      | 87.7 ms                                                | 94.6 ms: 1.08x slower                                                |
| fannkuch                   | 394 ms                                                 | 425 ms: 1.08x slower                                                 |
| json_loads                 | 27.2 us                                                | 29.5 us: 1.09x slower                                                |
| bench_thread_pool          | 818 us                                                 | 892 us: 1.09x slower                                                 |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                                |
| python_startup_no_site     | 7.00 ms                                                | 8.24 ms: 1.18x slower                                                |
| json_dumps                 | 10.1 ms                                                | 12.1 ms: 1.20x slower                                                |
| docutils                   | 2.58 sec                                               | 3.21 sec: 1.24x slower                                               |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 82.1 ms: 3.42x slower                                                |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (8): sympy_str, asyncio_websockets, bpe_tokeniser, sympy_sum, logging_format, nqueens, connected_components, json
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250415-3.14.0a7+-661a2b8/bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 99.90% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x
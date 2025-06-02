# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.170x faster
- HPT reliability: 99.89%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 297 ms: 1.12x slower                                                  |
| docutils       | 2.58 sec                                               | 2.91 sec: 1.13x slower                                                |
| html5lib       | 63.4 ms                                                | 65.4 ms: 1.03x slower                                                 |
| sphinx         | 1.03 sec                                               | 1.13 sec: 1.10x slower                                                |
| Geometric mean | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 345 ms: 1.34x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 678 ms: 1.27x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 345 ms: 1.27x faster                                                  |
| async_tree_io              | 838 ms                                                 | 665 ms: 1.26x faster                                                  |
| async_tree_none            | 350 ms                                                 | 289 ms: 1.21x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 274 ms: 1.16x faster                                                  |
| async_generators           | 433 ms                                                 | 439 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 592 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 579 ms: 1.07x slower                                                  |
| coroutines                 | 22.2 ms                                                | 27.4 ms: 1.23x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.2 ms: 1.14x faster                                                 |
| pidigits       | 186 ms                                                 | 206 ms: 1.11x slower                                                  |
| nbody          | 87.7 ms                                                | 98.5 ms: 1.12x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.20 ms: 1.18x faster                                                 |
| regex_dna      | 220 ms                                                 | 201 ms: 1.09x faster                                                  |
| regex_v8       | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 2.09 sec: 1.01x faster                                                |
| xml_etree_parse      | 154 ms                                                 | 162 ms: 1.05x slower                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 110 ms: 1.09x slower                                                  |
| unpickle_pure_python | 213 us                                                 | 234 us: 1.10x slower                                                  |
| xml_etree_process    | 60.5 ms                                                | 69.2 ms: 1.14x slower                                                 |
| xml_etree_generate   | 86.8 ms                                                | 102 ms: 1.17x slower                                                  |
| pickle_pure_python   | 302 us                                                 | 372 us: 1.23x slower                                                  |
| json_loads           | 27.2 us                                                | 33.6 us: 1.24x slower                                                 |
| json_dumps           | 10.1 ms                                                | 13.4 ms: 1.32x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.14x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                 |
| python_startup_no_site | 7.00 ms                                                | 7.40 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 25.3 ms: 1.12x slower                                                 |
| genshi_xml      | 50.5 ms                                                | 58.2 ms: 1.15x slower                                                 |
| mako            | 10.7 ms                                                | 13.3 ms: 1.25x slower                                                 |
| django_template | 31.7 ms                                                | 39.9 ms: 1.26x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.19x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pprint_pformat             | 1.48 sec                                               | 1.86 us: 795505.99x faster                                            |
| pprint_safe_repr           | 727 ms                                                 | 1.12 us: 646503.77x faster                                            |
| mdp                        | 2.54 sec                                               | 1.48 sec: 1.72x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 345 ms: 1.34x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 678 ms: 1.27x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 345 ms: 1.27x faster                                                  |
| async_tree_io              | 838 ms                                                 | 665 ms: 1.26x faster                                                  |
| async_tree_none            | 350 ms                                                 | 289 ms: 1.21x faster                                                  |
| richards                   | 47.5 ms                                                | 39.6 ms: 1.20x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.20 ms: 1.18x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 274 ms: 1.16x faster                                                  |
| richards_super             | 53.7 ms                                                | 46.3 ms: 1.16x faster                                                 |
| float                      | 78.7 ms                                                | 69.2 ms: 1.14x faster                                                 |
| deepcopy                   | 354 us                                                 | 315 us: 1.12x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 34.8 us: 1.10x faster                                                 |
| regex_dna                  | 220 ms                                                 | 201 ms: 1.09x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                 |
| go                         | 141 ms                                                 | 130 ms: 1.08x faster                                                  |
| pyflate                    | 470 ms                                                 | 450 ms: 1.04x faster                                                  |
| scimark_fft                | 367 ms                                                 | 353 ms: 1.04x faster                                                  |
| spectral_norm              | 113 ms                                                 | 110 ms: 1.03x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 2.09 sec: 1.01x faster                                                |
| async_generators           | 433 ms                                                 | 439 ms: 1.01x slower                                                  |
| dulwich_log                | 64.6 ms                                                | 66.1 ms: 1.02x slower                                                 |
| html5lib                   | 63.4 ms                                                | 65.4 ms: 1.03x slower                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 592 ms: 1.03x slower                                                  |
| shortest_path              | 487 ms                                                 | 504 ms: 1.04x slower                                                  |
| connected_components       | 447 ms                                                 | 463 ms: 1.04x slower                                                  |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                 |
| deepcopy_reduce            | 3.24 us                                                | 3.38 us: 1.04x slower                                                 |
| gc_traversal               | 4.90 ms                                                | 5.11 ms: 1.04x slower                                                 |
| xml_etree_parse            | 154 ms                                                 | 162 ms: 1.05x slower                                                  |
| pycparser                  | 1.20 sec                                               | 1.26 sec: 1.05x slower                                                |
| pathlib                    | 17.4 ms                                                | 18.4 ms: 1.06x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 7.40 ms: 1.06x slower                                                 |
| deltablue                  | 3.19 ms                                                | 3.37 ms: 1.06x slower                                                 |
| sqlite_synth               | 2.90 us                                                | 3.08 us: 1.06x slower                                                 |
| meteor_contest             | 108 ms                                                 | 115 ms: 1.06x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.61 ms: 1.07x slower                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 579 ms: 1.07x slower                                                  |
| telco                      | 8.40 ms                                                | 9.04 ms: 1.08x slower                                                 |
| sympy_integrate            | 19.8 ms                                                | 21.4 ms: 1.08x slower                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 110 ms: 1.09x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 73.1 ms: 1.09x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 5.14 sec: 1.10x slower                                                |
| unpickle_pure_python       | 213 us                                                 | 234 us: 1.10x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.13 sec: 1.10x slower                                                |
| pidigits                   | 186 ms                                                 | 206 ms: 1.11x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 167 ms: 1.11x slower                                                  |
| 2to3                       | 266 ms                                                 | 297 ms: 1.12x slower                                                  |
| scimark_sor                | 122 ms                                                 | 137 ms: 1.12x slower                                                  |
| genshi_text                | 22.6 ms                                                | 25.3 ms: 1.12x slower                                                 |
| nbody                      | 87.7 ms                                                | 98.5 ms: 1.12x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.91 sec: 1.13x slower                                                |
| json                       | 5.32 ms                                                | 6.01 ms: 1.13x slower                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.74 ms: 1.14x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.94 ms: 1.14x slower                                                 |
| xml_etree_process          | 60.5 ms                                                | 69.2 ms: 1.14x slower                                                 |
| crypto_pyaes               | 74.7 ms                                                | 85.8 ms: 1.15x slower                                                 |
| sympy_str                  | 273 ms                                                 | 314 ms: 1.15x slower                                                  |
| generators                 | 28.8 ms                                                | 33.1 ms: 1.15x slower                                                 |
| genshi_xml                 | 50.5 ms                                                | 58.2 ms: 1.15x slower                                                 |
| xml_etree_generate         | 86.8 ms                                                | 102 ms: 1.17x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 135 ms: 1.18x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 965 us: 1.18x slower                                                  |
| sympy_expand               | 456 ms                                                 | 548 ms: 1.20x slower                                                  |
| chaos                      | 58.0 ms                                                | 70.1 ms: 1.21x slower                                                 |
| fannkuch                   | 394 ms                                                 | 479 ms: 1.22x slower                                                  |
| comprehensions             | 16.5 us                                                | 20.1 us: 1.22x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 372 us: 1.23x slower                                                  |
| raytrace                   | 262 ms                                                 | 322 ms: 1.23x slower                                                  |
| coroutines                 | 22.2 ms                                                | 27.4 ms: 1.23x slower                                                 |
| json_loads                 | 27.2 us                                                | 33.6 us: 1.24x slower                                                 |
| mako                       | 10.7 ms                                                | 13.3 ms: 1.25x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 201 us: 1.25x slower                                                  |
| django_template            | 31.7 ms                                                | 39.9 ms: 1.26x slower                                                 |
| nqueens                    | 80.9 ms                                                | 103 ms: 1.27x slower                                                  |
| many_optionals             | 857 us                                                 | 1.10 ms: 1.29x slower                                                 |
| logging_simple             | 5.65 us                                                | 7.41 us: 1.31x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 13.4 ms: 1.32x slower                                                 |
| logging_format             | 6.23 us                                                | 8.43 us: 1.35x slower                                                 |
| subparsers                 | 15.5 ms                                                | 28.2 ms: 1.82x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 105 ms: 4.36x slower                                                  |
| logging_silent             | 101 ns                                                 | 623 ns: 6.16x slower                                                  |
| coverage                   | 82.8 ms                                                | 529 ms: 6.39x slower                                                  |
| thrift                     | 800 us                                                 | 149 ms: 186.18x slower                                                |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, pylint, k_core
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.170x faster

# HPT report

- Reliability score: 99.89% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.06x
# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.207x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x slower
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 340 ms: 1.28x slower                                                  |
| docutils       | 2.58 sec                                               | 3.15 sec: 1.22x slower                                                |
| html5lib       | 63.4 ms                                                | 74.6 ms: 1.18x slower                                                 |
| sphinx         | 1.03 sec                                               | 1.26 sec: 1.22x slower                                                |
| Geometric mean | (ref)                                                  | 1.22x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 601 ms: 1.43x faster                                                  |
| async_tree_memoization_tg  | 463 ms                                                 | 339 ms: 1.37x faster                                                  |
| async_tree_io              | 838 ms                                                 | 637 ms: 1.32x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 261 ms: 1.22x faster                                                  |
| async_tree_none            | 350 ms                                                 | 300 ms: 1.17x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 377 ms: 1.16x faster                                                  |
| async_generators           | 433 ms                                                 | 453 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 580 ms: 1.07x slower                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 621 ms: 1.08x slower                                                  |
| coroutines                 | 22.2 ms                                                | 29.5 ms: 1.33x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 80.4 ms: 1.02x slower                                                 |
| pidigits       | 186 ms                                                 | 199 ms: 1.07x slower                                                  |
| nbody          | 87.7 ms                                                | 151 ms: 1.72x slower                                                  |
| Geometric mean | (ref)                                                  | 1.23x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.29 ms: 1.15x faster                                                 |
| regex_v8       | 26.9 ms                                                | 24.5 ms: 1.10x faster                                                 |
| regex_dna      | 220 ms                                                 | 204 ms: 1.08x faster                                                  |
| regex_compile  | 132 ms                                                 | 172 ms: 1.30x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 106 ms: 1.05x slower                                                  |
| xml_etree_parse      | 154 ms                                                 | 165 ms: 1.07x slower                                                  |
| tomli_loads          | 2.12 sec                                               | 2.60 sec: 1.23x slower                                                |
| json_loads           | 27.2 us                                                | 37.4 us: 1.38x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 418 us: 1.38x slower                                                  |
| unpickle_pure_python | 213 us                                                 | 304 us: 1.43x slower                                                  |
| xml_etree_generate   | 86.8 ms                                                | 124 ms: 1.43x slower                                                  |
| xml_etree_process    | 60.5 ms                                                | 86.8 ms: 1.44x slower                                                 |
| json_dumps           | 10.1 ms                                                | 15.2 ms: 1.51x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.31x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 17.1 ms: 1.35x slower                                                 |
| python_startup_no_site | 7.00 ms                                                | 10.00 ms: 1.43x slower                                                |
| Geometric mean         | (ref)                                                  | 1.39x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 73.1 ms: 1.45x slower                                                 |
| genshi_text     | 22.6 ms                                                | 34.1 ms: 1.51x slower                                                 |
| django_template | 31.7 ms                                                | 52.6 ms: 1.66x slower                                                 |
| mako            | 10.7 ms                                                | 19.0 ms: 1.78x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.59x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal               | 4.90 ms                                                | 2.74 ms: 1.79x faster                                                 |
| mdp                        | 2.54 sec                                               | 1.73 sec: 1.47x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 601 ms: 1.43x faster                                                  |
| async_tree_memoization_tg  | 463 ms                                                 | 339 ms: 1.37x faster                                                  |
| async_tree_io              | 838 ms                                                 | 637 ms: 1.32x faster                                                  |
| create_gc_cycles           | 2.45 ms                                                | 1.88 ms: 1.30x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 261 ms: 1.22x faster                                                  |
| async_tree_none            | 350 ms                                                 | 300 ms: 1.17x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 377 ms: 1.16x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.29 ms: 1.15x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 24.5 ms: 1.10x faster                                                 |
| regex_dna                  | 220 ms                                                 | 204 ms: 1.08x faster                                                  |
| go                         | 141 ms                                                 | 140 ms: 1.01x faster                                                  |
| float                      | 78.7 ms                                                | 80.4 ms: 1.02x slower                                                 |
| async_generators           | 433 ms                                                 | 453 ms: 1.05x slower                                                  |
| deepcopy                   | 354 us                                                 | 371 us: 1.05x slower                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 106 ms: 1.05x slower                                                  |
| deepcopy_memo              | 38.4 us                                                | 40.9 us: 1.07x slower                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 580 ms: 1.07x slower                                                  |
| pidigits                   | 186 ms                                                 | 199 ms: 1.07x slower                                                  |
| xml_etree_parse            | 154 ms                                                 | 165 ms: 1.07x slower                                                  |
| k_core                     | 2.37 sec                                               | 2.56 sec: 1.08x slower                                                |
| pycparser                  | 1.20 sec                                               | 1.30 sec: 1.08x slower                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 621 ms: 1.08x slower                                                  |
| sqlite_synth               | 2.90 us                                                | 3.21 us: 1.11x slower                                                 |
| dulwich_log                | 64.6 ms                                                | 72.7 ms: 1.13x slower                                                 |
| pathlib                    | 17.4 ms                                                | 19.7 ms: 1.14x slower                                                 |
| pylint                     | 312 ms                                                 | 358 ms: 1.15x slower                                                  |
| pyflate                    | 470 ms                                                 | 552 ms: 1.18x slower                                                  |
| html5lib                   | 63.4 ms                                                | 74.6 ms: 1.18x slower                                                 |
| spectral_norm              | 113 ms                                                 | 134 ms: 1.18x slower                                                  |
| shortest_path              | 487 ms                                                 | 585 ms: 1.20x slower                                                  |
| connected_components       | 447 ms                                                 | 541 ms: 1.21x slower                                                  |
| generators                 | 28.8 ms                                                | 35.0 ms: 1.22x slower                                                 |
| docutils                   | 2.58 sec                                               | 3.15 sec: 1.22x slower                                                |
| sphinx                     | 1.03 sec                                               | 1.26 sec: 1.22x slower                                                |
| tomli_loads                | 2.12 sec                                               | 2.60 sec: 1.23x slower                                                |
| deepcopy_reduce            | 3.24 us                                                | 4.02 us: 1.24x slower                                                 |
| json                       | 5.32 ms                                                | 6.62 ms: 1.24x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 5.84 sec: 1.25x slower                                                |
| meteor_contest             | 108 ms                                                 | 135 ms: 1.25x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 25.0 ms: 1.26x slower                                                 |
| scimark_sor                | 122 ms                                                 | 155 ms: 1.27x slower                                                  |
| 2to3                       | 266 ms                                                 | 340 ms: 1.28x slower                                                  |
| scimark_fft                | 367 ms                                                 | 477 ms: 1.30x slower                                                  |
| regex_compile              | 132 ms                                                 | 172 ms: 1.30x slower                                                  |
| hexiom                     | 6.08 ms                                                | 7.95 ms: 1.31x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 198 ms: 1.31x slower                                                  |
| coroutines                 | 22.2 ms                                                | 29.5 ms: 1.33x slower                                                 |
| sympy_str                  | 273 ms                                                 | 366 ms: 1.34x slower                                                  |
| python_startup             | 12.7 ms                                                | 17.1 ms: 1.35x slower                                                 |
| sympy_expand               | 456 ms                                                 | 624 ms: 1.37x slower                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.89 ms: 1.37x slower                                                 |
| comprehensions             | 16.5 us                                                | 22.6 us: 1.37x slower                                                 |
| json_loads                 | 27.2 us                                                | 37.4 us: 1.38x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 418 us: 1.38x slower                                                  |
| telco                      | 8.40 ms                                                | 11.8 ms: 1.40x slower                                                 |
| richards                   | 47.5 ms                                                | 67.0 ms: 1.41x slower                                                 |
| chaos                      | 58.0 ms                                                | 82.0 ms: 1.41x slower                                                 |
| deltablue                  | 3.19 ms                                                | 4.54 ms: 1.42x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 304 us: 1.43x slower                                                  |
| xml_etree_generate         | 86.8 ms                                                | 124 ms: 1.43x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 10.00 ms: 1.43x slower                                                |
| xml_etree_process          | 60.5 ms                                                | 86.8 ms: 1.44x slower                                                 |
| genshi_xml                 | 50.5 ms                                                | 73.1 ms: 1.45x slower                                                 |
| scimark_lu                 | 114 ms                                                 | 167 ms: 1.46x slower                                                  |
| thrift                     | 800 us                                                 | 1.16 ms: 1.46x slower                                                 |
| nqueens                    | 80.9 ms                                                | 118 ms: 1.46x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 235 us: 1.47x slower                                                  |
| many_optionals             | 857 us                                                 | 1.26 ms: 1.47x slower                                                 |
| fannkuch                   | 394 ms                                                 | 581 ms: 1.48x slower                                                  |
| richards_super             | 53.7 ms                                                | 79.7 ms: 1.48x slower                                                 |
| raytrace                   | 262 ms                                                 | 388 ms: 1.49x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 112 ms: 1.50x slower                                                  |
| genshi_text                | 22.6 ms                                                | 34.1 ms: 1.51x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 15.2 ms: 1.51x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 101 ms: 1.52x slower                                                  |
| coverage                   | 82.8 ms                                                | 133 ms: 1.60x slower                                                  |
| logging_simple             | 5.65 us                                                | 9.07 us: 1.60x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 1.17 sec: 1.61x slower                                                |
| pprint_pformat             | 1.48 sec                                               | 2.41 sec: 1.63x slower                                                |
| logging_format             | 6.23 us                                                | 10.2 us: 1.64x slower                                                 |
| django_template            | 31.7 ms                                                | 52.6 ms: 1.66x slower                                                 |
| nbody                      | 87.7 ms                                                | 151 ms: 1.72x slower                                                  |
| mako                       | 10.7 ms                                                | 19.0 ms: 1.78x slower                                                 |
| subparsers                 | 15.5 ms                                                | 34.6 ms: 2.24x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 3.51 ms: 4.29x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 112 ms: 4.67x slower                                                  |
| logging_silent             | 101 ns                                                 | 720 ns: 7.13x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.29x slower                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.207x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.20x
- 95% likely to have a slowdown of 1.18x
- 99% likely to have a slowdown of 1.15x

# Memory
- memory change: 1.27x
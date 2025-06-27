# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.046x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                  |
| docutils       | 2.58 sec                                               | 2.57 sec: 1.01x faster                                                |
| html5lib       | 63.4 ms                                                | 61.4 ms: 1.03x faster                                                 |
| sphinx         | 1.03 sec                                               | 996 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                  |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                  |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 486 ms: 1.12x faster                                                  |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                                  |
| coroutines                 | 22.2 ms                                                | 25.1 ms: 1.13x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.5 ms: 1.10x faster                                                 |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                  |
| nbody          | 87.7 ms                                                | 103 ms: 1.17x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.07 ms: 1.23x faster                                                 |
| regex_v8       | 26.9 ms                                                | 22.1 ms: 1.22x faster                                                 |
| regex_dna      | 220 ms                                                 | 182 ms: 1.21x faster                                                  |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                  |
| tomli_loads          | 2.12 sec                                               | 2.04 sec: 1.04x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 98.5 ms: 1.03x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 85.1 ms: 1.02x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 60.0 ms: 1.01x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                  |
| json_loads           | 27.2 us                                                | 28.0 us: 1.03x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 318 us: 1.05x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.1 ms: 1.04x faster                                                 |
| python_startup_no_site | 7.00 ms                                                | 6.90 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                 |
| genshi_xml      | 50.5 ms                                                | 48.9 ms: 1.03x faster                                                 |
| django_template | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                 |
| mako            | 10.7 ms                                                | 11.5 ms: 1.08x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                  |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                  |
| deepcopy                   | 354 us                                                 | 254 us: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                  |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                                 |
| go                         | 141 ms                                                 | 111 ms: 1.27x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.63 us: 1.23x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.07 ms: 1.23x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 22.1 ms: 1.22x faster                                                 |
| regex_dna                  | 220 ms                                                 | 182 ms: 1.21x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                  |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 486 ms: 1.12x faster                                                  |
| richards                   | 47.5 ms                                                | 43.0 ms: 1.11x faster                                                 |
| float                      | 78.7 ms                                                | 71.5 ms: 1.10x faster                                                 |
| richards_super             | 53.7 ms                                                | 48.9 ms: 1.10x faster                                                 |
| dulwich_log                | 64.6 ms                                                | 58.9 ms: 1.10x faster                                                 |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                |
| telco                      | 8.40 ms                                                | 7.89 ms: 1.06x faster                                                 |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                 |
| pyflate                    | 470 ms                                                 | 443 ms: 1.06x faster                                                  |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                                  |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                  |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.05x faster                                                 |
| python_startup             | 12.7 ms                                                | 12.1 ms: 1.04x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.50 sec: 1.04x faster                                                |
| spectral_norm              | 113 ms                                                 | 109 ms: 1.04x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 2.04 sec: 1.04x faster                                                |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                                  |
| sphinx                     | 1.03 sec                                               | 996 ms: 1.04x faster                                                  |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                |
| html5lib                   | 63.4 ms                                                | 61.4 ms: 1.03x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 48.9 ms: 1.03x faster                                                 |
| djangocms                  | 22.3 us                                                | 21.7 us: 1.03x faster                                                 |
| json                       | 5.32 ms                                                | 5.18 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 98.5 ms: 1.03x faster                                                 |
| thrift                     | 800 us                                                 | 779 us: 1.03x faster                                                  |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.02x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 85.1 ms: 1.02x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.86 us: 1.02x faster                                                 |
| python_startup_no_site     | 7.00 ms                                                | 6.90 ms: 1.01x faster                                                 |
| comprehensions             | 16.5 us                                                | 16.4 us: 1.01x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 60.0 ms: 1.01x faster                                                 |
| docutils                   | 2.58 sec                                               | 2.57 sec: 1.01x faster                                                |
| sympy_expand               | 456 ms                                                 | 453 ms: 1.01x faster                                                  |
| pathlib                    | 17.4 ms                                                | 17.3 ms: 1.01x faster                                                 |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                  |
| nqueens                    | 80.9 ms                                                | 81.7 ms: 1.01x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 75.7 ms: 1.01x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 68.1 ms: 1.02x slower                                                 |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                  |
| django_template            | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                 |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                                  |
| scimark_fft                | 367 ms                                                 | 379 ms: 1.03x slower                                                  |
| json_loads                 | 27.2 us                                                | 28.0 us: 1.03x slower                                                 |
| gc_traversal               | 4.90 ms                                                | 5.06 ms: 1.03x slower                                                 |
| generators                 | 28.8 ms                                                | 29.9 ms: 1.04x slower                                                 |
| chaos                      | 58.0 ms                                                | 60.4 ms: 1.04x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.56 ms: 1.05x slower                                                 |
| shortest_path              | 487 ms                                                 | 509 ms: 1.05x slower                                                  |
| fannkuch                   | 394 ms                                                 | 413 ms: 1.05x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 318 us: 1.05x slower                                                  |
| connected_components       | 447 ms                                                 | 472 ms: 1.06x slower                                                  |
| coverage                   | 82.8 ms                                                | 89.2 ms: 1.08x slower                                                 |
| mako                       | 10.7 ms                                                | 11.5 ms: 1.08x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 785 ms: 1.08x slower                                                  |
| logging_simple             | 5.65 us                                                | 6.11 us: 1.08x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 1.60 sec: 1.08x slower                                                |
| deltablue                  | 3.19 ms                                                | 3.47 ms: 1.09x slower                                                 |
| logging_format             | 6.23 us                                                | 6.78 us: 1.09x slower                                                 |
| many_optionals             | 857 us                                                 | 958 us: 1.12x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                 |
| coroutines                 | 22.2 ms                                                | 25.1 ms: 1.13x slower                                                 |
| nbody                      | 87.7 ms                                                | 103 ms: 1.17x slower                                                  |
| subparsers                 | 15.5 ms                                                | 23.2 ms: 1.50x slower                                                 |
| logging_silent             | 101 ns                                                 | 475 ns: 4.70x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (3): scimark_sparse_mat_mult, hexiom, asyncio_websockets
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x
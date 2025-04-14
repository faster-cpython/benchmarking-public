# Results vs. 3.13.0

- fork: python
- ref: 1a9d4a1fb3d4beda7c7e
- machine: linux-x86_64
- commit hash: 1a9d4a1
- commit date: 2025-04-01
- overall geometric mean: 1.060x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.04x faster                                                   |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                 |
| html5lib       | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                                   |
| async_tree_io              | 838 ms                                                 | 613 ms: 1.37x faster                                                   |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 491 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                   |
| async_generators           | 433 ms                                                 | 414 ms: 1.05x faster                                                   |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 61.5 ms: 1.28x faster                                                  |
| nbody          | 87.7 ms                                                | 86.4 ms: 1.01x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                  |
| regex_effbot   | 3.77 ms                                                | 3.35 ms: 1.12x faster                                                  |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.83 sec: 1.16x faster                                                 |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                   |
| xml_etree_generate   | 86.8 ms                                                | 79.4 ms: 1.09x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 56.6 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 209 us: 1.02x faster                                                   |
| pickle_pure_python   | 302 us                                                 | 317 us: 1.05x slower                                                   |
| json_loads           | 27.2 us                                                | 29.6 us: 1.09x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 8.19 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                  |
| mako            | 10.7 ms                                                | 10.9 ms: 1.02x slower                                                  |
| django_template | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.09x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                   |
| deepcopy                   | 354 us                                                 | 252 us: 1.41x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                                   |
| async_tree_io              | 838 ms                                                 | 613 ms: 1.37x faster                                                   |
| richards                   | 47.5 ms                                                | 34.9 ms: 1.36x faster                                                  |
| richards_super             | 53.7 ms                                                | 39.7 ms: 1.35x faster                                                  |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 28.6 us: 1.34x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                   |
| float                      | 78.7 ms                                                | 61.5 ms: 1.28x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.64 us: 1.23x faster                                                  |
| scimark_fft                | 367 ms                                                 | 307 ms: 1.20x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 491 ms: 1.17x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.83 sec: 1.16x faster                                                 |
| go                         | 141 ms                                                 | 123 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                   |
| spectral_norm              | 113 ms                                                 | 100 ms: 1.13x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.35 ms: 1.12x faster                                                  |
| pylint                     | 312 ms                                                 | 281 ms: 1.11x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                   |
| pyflate                    | 470 ms                                                 | 429 ms: 1.09x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 79.4 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.64 ms: 1.08x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 60.2 ms: 1.07x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 56.6 ms: 1.07x faster                                                  |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.75 us: 1.05x faster                                                  |
| logging_silent             | 101 ns                                                 | 95.9 ns: 1.05x faster                                                  |
| deltablue                  | 3.19 ms                                                | 3.03 ms: 1.05x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.6 ms: 1.05x faster                                                  |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                   |
| async_generators           | 433 ms                                                 | 414 ms: 1.05x faster                                                   |
| telco                      | 8.40 ms                                                | 8.02 ms: 1.05x faster                                                  |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                                   |
| 2to3                       | 266 ms                                                 | 257 ms: 1.04x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.55 sec: 1.03x faster                                                 |
| html5lib                   | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 209 us: 1.02x faster                                                   |
| chaos                      | 58.0 ms                                                | 56.8 ms: 1.02x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.82 ms: 1.02x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.57 us: 1.01x faster                                                  |
| nbody                      | 87.7 ms                                                | 86.4 ms: 1.01x faster                                                  |
| logging_format             | 6.23 us                                                | 6.15 us: 1.01x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                                  |
| raytrace                   | 262 ms                                                 | 259 ms: 1.01x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                  |
| json                       | 5.32 ms                                                | 5.27 ms: 1.01x faster                                                  |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.01x faster                                                   |
| crypto_pyaes               | 74.7 ms                                                | 74.4 ms: 1.00x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| connected_components       | 447 ms                                                 | 451 ms: 1.01x slower                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.1 ms: 1.01x slower                                                  |
| shortest_path              | 487 ms                                                 | 493 ms: 1.01x slower                                                   |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                                   |
| mako                       | 10.7 ms                                                | 10.9 ms: 1.02x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.50 ms: 1.02x slower                                                  |
| generators                 | 28.8 ms                                                | 29.5 ms: 1.03x slower                                                  |
| coverage                   | 82.8 ms                                                | 85.1 ms: 1.03x slower                                                  |
| sympy_expand               | 456 ms                                                 | 469 ms: 1.03x slower                                                   |
| django_template            | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 750 ms: 1.03x slower                                                   |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.55 sec: 1.05x slower                                                 |
| nqueens                    | 80.9 ms                                                | 84.7 ms: 1.05x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 317 us: 1.05x slower                                                   |
| fannkuch                   | 394 ms                                                 | 415 ms: 1.05x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 173 us: 1.08x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 890 us: 1.09x slower                                                   |
| json_loads                 | 27.2 us                                                | 29.6 us: 1.09x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.70 ms: 1.10x slower                                                  |
| comprehensions             | 16.5 us                                                | 18.2 us: 1.11x slower                                                  |
| many_optionals             | 857 us                                                 | 948 us: 1.11x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 8.19 ms: 1.17x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 82.7 ms: 3.45x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (7): scimark_monte_carlo, sympy_str, sympy_sum, sphinx, asyncio_websockets, sqlalchemy_declarative, regex_dna
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250401-3.14.0a6+-1a9d4a1-JIT/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x
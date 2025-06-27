# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.458x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                  |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                |
| html5lib       | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                 |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 311 ms: 1.40x faster                                                  |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.40x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                  |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                                  |
| async_generators           | 433 ms                                                 | 428 ms: 1.01x faster                                                  |
| coroutines                 | 22.2 ms                                                | 25.6 ms: 1.15x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 63.7 ms: 1.24x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| nbody          | 87.7 ms                                                | 93.1 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.1 ms: 1.16x faster                                                 |
| regex_effbot   | 3.77 ms                                                | 3.29 ms: 1.15x faster                                                 |
| regex_dna      | 220 ms                                                 | 197 ms: 1.12x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.89 sec: 1.12x faster                                                |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 80.5 ms: 1.08x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 56.3 ms: 1.07x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 199 us: 1.07x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 97.1 ms: 1.04x faster                                                 |
| json_loads           | 27.2 us                                                | 28.3 us: 1.04x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 323 us: 1.07x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| python_startup_no_site | 7.00 ms                                                | 6.94 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                 |
| genshi_xml      | 50.5 ms                                                | 50.0 ms: 1.01x faster                                                 |
| mako            | 10.7 ms                                                | 10.7 ms: 1.00x slower                                                 |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pprint_pformat             | 1.48 sec                                               | 1.45 us: 1018667.53x faster                                           |
| pprint_safe_repr           | 727 ms                                                 | 837 ns: 868348.90x faster                                             |
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.05x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                  |
| richards                   | 47.5 ms                                                | 33.5 ms: 1.42x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 311 ms: 1.40x faster                                                  |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.40x faster                                                  |
| deepcopy                   | 354 us                                                 | 255 us: 1.39x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                  |
| richards_super             | 53.7 ms                                                | 39.2 ms: 1.37x faster                                                 |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.6 us: 1.30x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                  |
| float                      | 78.7 ms                                                | 63.7 ms: 1.24x faster                                                 |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.20x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 23.1 ms: 1.16x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.29 ms: 1.15x faster                                                 |
| go                         | 141 ms                                                 | 123 ms: 1.14x faster                                                  |
| pyflate                    | 470 ms                                                 | 412 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                                  |
| spectral_norm              | 113 ms                                                 | 101 ms: 1.13x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.89 sec: 1.12x faster                                                |
| regex_dna                  | 220 ms                                                 | 197 ms: 1.12x faster                                                  |
| scimark_fft                | 367 ms                                                 | 330 ms: 1.11x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                  |
| pylint                     | 312 ms                                                 | 282 ms: 1.10x faster                                                  |
| telco                      | 8.40 ms                                                | 7.72 ms: 1.09x faster                                                 |
| dulwich_log                | 64.6 ms                                                | 59.7 ms: 1.08x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 80.5 ms: 1.08x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 56.3 ms: 1.07x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 199 us: 1.07x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.39 sec: 1.07x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 97.1 ms: 1.04x faster                                                 |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| deltablue                  | 3.19 ms                                                | 3.09 ms: 1.03x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                                 |
| thrift                     | 800 us                                                 | 777 us: 1.03x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.90 ms: 1.03x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                                |
| html5lib                   | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                 |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                  |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                                 |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                                 |
| json                       | 5.32 ms                                                | 5.22 ms: 1.02x faster                                                 |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                |
| async_generators           | 433 ms                                                 | 428 ms: 1.01x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                  |
| sympy_str                  | 273 ms                                                 | 270 ms: 1.01x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 50.0 ms: 1.01x faster                                                 |
| python_startup_no_site     | 7.00 ms                                                | 6.94 ms: 1.01x faster                                                 |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| mako                       | 10.7 ms                                                | 10.7 ms: 1.00x slower                                                 |
| connected_components       | 447 ms                                                 | 450 ms: 1.01x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 75.6 ms: 1.01x slower                                                 |
| sympy_expand               | 456 ms                                                 | 463 ms: 1.01x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                 |
| nqueens                    | 80.9 ms                                                | 82.7 ms: 1.02x slower                                                 |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                  |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                 |
| gc_traversal               | 4.90 ms                                                | 5.08 ms: 1.04x slower                                                 |
| fannkuch                   | 394 ms                                                 | 409 ms: 1.04x slower                                                  |
| json_loads                 | 27.2 us                                                | 28.3 us: 1.04x slower                                                 |
| coverage                   | 82.8 ms                                                | 87.0 ms: 1.05x slower                                                 |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.06x slower                                                  |
| raytrace                   | 262 ms                                                 | 277 ms: 1.06x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.45 ms: 1.06x slower                                                 |
| generators                 | 28.8 ms                                                | 30.6 ms: 1.06x slower                                                 |
| nbody                      | 87.7 ms                                                | 93.1 ms: 1.06x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 323 us: 1.07x slower                                                  |
| chaos                      | 58.0 ms                                                | 62.1 ms: 1.07x slower                                                 |
| logging_simple             | 5.65 us                                                | 6.11 us: 1.08x slower                                                 |
| logging_format             | 6.23 us                                                | 6.78 us: 1.09x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                 |
| many_optionals             | 857 us                                                 | 981 us: 1.14x slower                                                  |
| coroutines                 | 22.2 ms                                                | 25.6 ms: 1.15x slower                                                 |
| subparsers                 | 15.5 ms                                                | 23.4 ms: 1.52x slower                                                 |
| logging_silent             | 101 ns                                                 | 472 ns: 4.67x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.42x faster                                                          |

Benchmark hidden because not significant (4): djangocms, asyncio_websockets, shortest_path, scimark_monte_carlo
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.458x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x
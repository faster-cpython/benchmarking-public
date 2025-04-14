# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_binary_op_swa
- machine: linux-x86_64
- commit hash: 6daa4a6
- commit date: 2025-01-15
- overall geometric mean: 1.031x faster
- HPT reliability: 95.41%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                         |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                       |
| html5lib       | 63.4 ms                                                | 63.9 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.50x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 595 ms: 1.45x faster                                                         |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                         |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 332 ms: 1.32x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.27x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 500 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                                         |
| async_generators           | 433 ms                                                 | 407 ms: 1.07x faster                                                         |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.04x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.1 ms: 1.14x faster                                                        |
| nbody          | 87.7 ms                                                | 85.2 ms: 1.03x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.12 ms: 1.21x faster                                                        |
| regex_v8       | 26.9 ms                                                | 24.2 ms: 1.11x faster                                                        |
| regex_dna      | 220 ms                                                 | 203 ms: 1.08x faster                                                         |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.83 sec: 1.15x faster                                                       |
| xml_etree_parse      | 154 ms                                                 | 136 ms: 1.14x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 77.9 ms: 1.11x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 54.8 ms: 1.10x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 196 us: 1.08x faster                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 94.9 ms: 1.07x faster                                                        |
| pickle_pure_python   | 302 us                                                 | 316 us: 1.05x slower                                                         |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                        |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.11 ms: 1.02x slower                                                        |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 9.94 ms: 1.07x faster                                                        |
| genshi_text     | 22.6 ms                                                | 23.6 ms: 1.04x slower                                                        |
| django_template | 31.7 ms                                                | 34.1 ms: 1.08x slower                                                        |
| genshi_xml      | 50.5 ms                                                | 59.2 ms: 1.17x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.50x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 595 ms: 1.45x faster                                                         |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                         |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 332 ms: 1.32x faster                                                         |
| deepcopy                   | 354 us                                                 | 272 us: 1.30x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.27x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 30.3 us: 1.27x faster                                                        |
| regex_effbot               | 3.77 ms                                                | 3.12 ms: 1.21x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.78 us: 1.17x faster                                                        |
| tomli_loads                | 2.12 sec                                               | 1.83 sec: 1.15x faster                                                       |
| scimark_fft                | 367 ms                                                 | 319 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 500 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                                         |
| float                      | 78.7 ms                                                | 69.1 ms: 1.14x faster                                                        |
| xml_etree_parse            | 154 ms                                                 | 136 ms: 1.14x faster                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.47 ms: 1.12x faster                                                        |
| xml_etree_generate         | 86.8 ms                                                | 77.9 ms: 1.11x faster                                                        |
| regex_v8                   | 26.9 ms                                                | 24.2 ms: 1.11x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 54.8 ms: 1.10x faster                                                        |
| telco                      | 8.40 ms                                                | 7.70 ms: 1.09x faster                                                        |
| richards                   | 47.5 ms                                                | 43.7 ms: 1.09x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 196 us: 1.08x faster                                                         |
| pylint                     | 312 ms                                                 | 288 ms: 1.08x faster                                                         |
| regex_dna                  | 220 ms                                                 | 203 ms: 1.08x faster                                                         |
| pyflate                    | 470 ms                                                 | 435 ms: 1.08x faster                                                         |
| richards_super             | 53.7 ms                                                | 49.9 ms: 1.08x faster                                                        |
| mako                       | 10.7 ms                                                | 9.94 ms: 1.07x faster                                                        |
| spectral_norm              | 113 ms                                                 | 106 ms: 1.07x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 94.9 ms: 1.07x faster                                                        |
| async_generators           | 433 ms                                                 | 407 ms: 1.07x faster                                                         |
| pathlib                    | 17.4 ms                                                | 16.3 ms: 1.06x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                       |
| scimark_sor                | 122 ms                                                 | 115 ms: 1.06x faster                                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 63.0 ms: 1.06x faster                                                        |
| sqlite_synth               | 2.90 us                                                | 2.74 us: 1.06x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.45 sec: 1.05x faster                                                       |
| crypto_pyaes               | 74.7 ms                                                | 71.6 ms: 1.04x faster                                                        |
| go                         | 141 ms                                                 | 136 ms: 1.03x faster                                                         |
| thrift                     | 800 us                                                 | 775 us: 1.03x faster                                                         |
| connected_components       | 447 ms                                                 | 433 ms: 1.03x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                       |
| nbody                      | 87.7 ms                                                | 85.2 ms: 1.03x faster                                                        |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                         |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                                         |
| shortest_path              | 487 ms                                                 | 481 ms: 1.01x faster                                                         |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| fannkuch                   | 394 ms                                                 | 396 ms: 1.01x slower                                                         |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                        |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                         |
| html5lib                   | 63.4 ms                                                | 63.9 ms: 1.01x slower                                                        |
| sqlglot_normalize          | 108 ms                                                 | 109 ms: 1.01x slower                                                         |
| python_startup_no_site     | 7.00 ms                                                | 7.11 ms: 1.02x slower                                                        |
| deltablue                  | 3.19 ms                                                | 3.24 ms: 1.02x slower                                                        |
| logging_format             | 6.23 us                                                | 6.33 us: 1.02x slower                                                        |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                        |
| logging_simple             | 5.65 us                                                | 5.76 us: 1.02x slower                                                        |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                        |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.03x slower                                                         |
| sqlglot_optimize           | 53.4 ms                                                | 54.9 ms: 1.03x slower                                                        |
| gc_traversal               | 4.90 ms                                                | 5.04 ms: 1.03x slower                                                        |
| pprint_safe_repr           | 727 ms                                                 | 752 ms: 1.03x slower                                                         |
| sympy_str                  | 273 ms                                                 | 283 ms: 1.04x slower                                                         |
| pprint_pformat             | 1.48 sec                                               | 1.53 sec: 1.04x slower                                                       |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                       |
| genshi_text                | 22.6 ms                                                | 23.6 ms: 1.04x slower                                                        |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.04x slower                                                        |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.05x slower                                                         |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.05x slower                                                        |
| pickle_pure_python         | 302 us                                                 | 316 us: 1.05x slower                                                         |
| sympy_expand               | 456 ms                                                 | 478 ms: 1.05x slower                                                         |
| sympy_integrate            | 19.8 ms                                                | 20.8 ms: 1.05x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 158 ms: 1.05x slower                                                         |
| dulwich_log                | 64.6 ms                                                | 68.3 ms: 1.06x slower                                                        |
| logging_silent             | 101 ns                                                 | 107 ns: 1.06x slower                                                         |
| django_template            | 31.7 ms                                                | 34.1 ms: 1.08x slower                                                        |
| coverage                   | 82.8 ms                                                | 90.0 ms: 1.09x slower                                                        |
| chaos                      | 58.0 ms                                                | 63.1 ms: 1.09x slower                                                        |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                        |
| bench_thread_pool          | 818 us                                                 | 897 us: 1.10x slower                                                         |
| raytrace                   | 262 ms                                                 | 291 ms: 1.11x slower                                                         |
| nqueens                    | 80.9 ms                                                | 91.6 ms: 1.13x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                        |
| many_optionals             | 857 us                                                 | 988 us: 1.15x slower                                                         |
| genshi_xml                 | 50.5 ms                                                | 59.2 ms: 1.17x slower                                                        |
| hexiom                     | 6.08 ms                                                | 7.17 ms: 1.18x slower                                                        |
| generators                 | 28.8 ms                                                | 37.8 ms: 1.31x slower                                                        |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (5): json, asyncio_websockets, mdp, sqlglot_parse, sphinx
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 95.41% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
# Results vs. 3.13.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.150x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 297 ms: 1.12x slower                                                  |
| docutils       | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                |
| html5lib       | 63.4 ms                                                | 66.1 ms: 1.04x slower                                                 |
| sphinx         | 1.03 sec                                               | 1.14 sec: 1.11x slower                                                |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 350 ms: 1.32x faster                                                  |
| async_tree_io              | 838 ms                                                 | 655 ms: 1.28x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 343 ms: 1.27x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 690 ms: 1.25x faster                                                  |
| async_tree_none            | 350 ms                                                 | 285 ms: 1.23x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 276 ms: 1.15x faster                                                  |
| async_generators           | 433 ms                                                 | 437 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 600 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 595 ms: 1.10x slower                                                  |
| coroutines                 | 22.2 ms                                                | 27.0 ms: 1.22x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.9 ms: 1.16x faster                                                 |
| pidigits       | 186 ms                                                 | 203 ms: 1.09x slower                                                  |
| nbody          | 87.7 ms                                                | 97.0 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.18 ms: 1.18x faster                                                 |
| regex_dna      | 220 ms                                                 | 199 ms: 1.10x faster                                                  |
| regex_v8       | 26.9 ms                                                | 25.6 ms: 1.05x faster                                                 |
| regex_compile  | 132 ms                                                 | 144 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 2.10 sec: 1.01x faster                                                |
| xml_etree_parse      | 154 ms                                                 | 161 ms: 1.05x slower                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 112 ms: 1.10x slower                                                  |
| unpickle_pure_python | 213 us                                                 | 240 us: 1.13x slower                                                  |
| xml_etree_process    | 60.5 ms                                                | 68.8 ms: 1.14x slower                                                 |
| xml_etree_generate   | 86.8 ms                                                | 102 ms: 1.17x slower                                                  |
| json_loads           | 27.2 us                                                | 33.5 us: 1.23x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 377 us: 1.25x slower                                                  |
| json_dumps           | 10.1 ms                                                | 13.3 ms: 1.32x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.15x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                 |
| python_startup_no_site | 7.00 ms                                                | 7.39 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 25.4 ms: 1.12x slower                                                 |
| genshi_xml      | 50.5 ms                                                | 58.4 ms: 1.16x slower                                                 |
| mako            | 10.7 ms                                                | 13.2 ms: 1.24x slower                                                 |
| django_template | 31.7 ms                                                | 40.6 ms: 1.28x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.20x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.48 sec: 1.72x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 350 ms: 1.32x faster                                                  |
| async_tree_io              | 838 ms                                                 | 655 ms: 1.28x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 343 ms: 1.27x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 690 ms: 1.25x faster                                                  |
| async_tree_none            | 350 ms                                                 | 285 ms: 1.23x faster                                                  |
| richards                   | 47.5 ms                                                | 39.7 ms: 1.20x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.18 ms: 1.18x faster                                                 |
| richards_super             | 53.7 ms                                                | 46.3 ms: 1.16x faster                                                 |
| float                      | 78.7 ms                                                | 67.9 ms: 1.16x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 276 ms: 1.15x faster                                                  |
| deepcopy                   | 354 us                                                 | 312 us: 1.14x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 34.4 us: 1.12x faster                                                 |
| regex_dna                  | 220 ms                                                 | 199 ms: 1.10x faster                                                  |
| go                         | 141 ms                                                 | 129 ms: 1.09x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 25.6 ms: 1.05x faster                                                 |
| scimark_fft                | 367 ms                                                 | 351 ms: 1.04x faster                                                  |
| pyflate                    | 470 ms                                                 | 455 ms: 1.03x faster                                                  |
| spectral_norm              | 113 ms                                                 | 110 ms: 1.03x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 2.10 sec: 1.01x faster                                                |
| async_generators           | 433 ms                                                 | 437 ms: 1.01x slower                                                  |
| dulwich_log                | 64.6 ms                                                | 66.9 ms: 1.04x slower                                                 |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                 |
| pathlib                    | 17.4 ms                                                | 18.1 ms: 1.04x slower                                                 |
| deepcopy_reduce            | 3.24 us                                                | 3.38 us: 1.04x slower                                                 |
| html5lib                   | 63.4 ms                                                | 66.1 ms: 1.04x slower                                                 |
| gc_traversal               | 4.90 ms                                                | 5.11 ms: 1.04x slower                                                 |
| xml_etree_parse            | 154 ms                                                 | 161 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 600 ms: 1.05x slower                                                  |
| shortest_path              | 487 ms                                                 | 511 ms: 1.05x slower                                                  |
| connected_components       | 447 ms                                                 | 470 ms: 1.05x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 7.39 ms: 1.06x slower                                                 |
| pycparser                  | 1.20 sec                                               | 1.27 sec: 1.06x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.62 ms: 1.07x slower                                                 |
| deltablue                  | 3.19 ms                                                | 3.45 ms: 1.08x slower                                                 |
| meteor_contest             | 108 ms                                                 | 117 ms: 1.08x slower                                                  |
| telco                      | 8.40 ms                                                | 9.07 ms: 1.08x slower                                                 |
| sympy_integrate            | 19.8 ms                                                | 21.5 ms: 1.08x slower                                                 |
| sqlite_synth               | 2.90 us                                                | 3.14 us: 1.08x slower                                                 |
| pidigits                   | 186 ms                                                 | 203 ms: 1.09x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 72.7 ms: 1.09x slower                                                 |
| regex_compile              | 132 ms                                                 | 144 ms: 1.09x slower                                                  |
| scimark_sor                | 122 ms                                                 | 134 ms: 1.10x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 595 ms: 1.10x slower                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 5.16 sec: 1.10x slower                                                |
| xml_etree_iterparse        | 101 ms                                                 | 112 ms: 1.10x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.14 sec: 1.11x slower                                                |
| nbody                      | 87.7 ms                                                | 97.0 ms: 1.11x slower                                                 |
| 2to3                       | 266 ms                                                 | 297 ms: 1.12x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 168 ms: 1.12x slower                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.64 ms: 1.12x slower                                                 |
| genshi_text                | 22.6 ms                                                | 25.4 ms: 1.12x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 240 us: 1.13x slower                                                  |
| json                       | 5.32 ms                                                | 6.02 ms: 1.13x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                |
| xml_etree_process          | 60.5 ms                                                | 68.8 ms: 1.14x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.94 ms: 1.14x slower                                                 |
| sympy_str                  | 273 ms                                                 | 314 ms: 1.15x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 86.3 ms: 1.16x slower                                                 |
| genshi_xml                 | 50.5 ms                                                | 58.4 ms: 1.16x slower                                                 |
| generators                 | 28.8 ms                                                | 33.5 ms: 1.16x slower                                                 |
| xml_etree_generate         | 86.8 ms                                                | 102 ms: 1.17x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 134 ms: 1.17x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 965 us: 1.18x slower                                                  |
| sympy_expand               | 456 ms                                                 | 548 ms: 1.20x slower                                                  |
| chaos                      | 58.0 ms                                                | 70.2 ms: 1.21x slower                                                 |
| coroutines                 | 22.2 ms                                                | 27.0 ms: 1.22x slower                                                 |
| fannkuch                   | 394 ms                                                 | 482 ms: 1.22x slower                                                  |
| json_loads                 | 27.2 us                                                | 33.5 us: 1.23x slower                                                 |
| raytrace                   | 262 ms                                                 | 323 ms: 1.23x slower                                                  |
| nqueens                    | 80.9 ms                                                | 100 ms: 1.24x slower                                                  |
| mako                       | 10.7 ms                                                | 13.2 ms: 1.24x slower                                                 |
| comprehensions             | 16.5 us                                                | 20.4 us: 1.24x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 200 us: 1.25x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 377 us: 1.25x slower                                                  |
| django_template            | 31.7 ms                                                | 40.6 ms: 1.28x slower                                                 |
| many_optionals             | 857 us                                                 | 1.10 ms: 1.29x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 13.3 ms: 1.32x slower                                                 |
| logging_simple             | 5.65 us                                                | 7.45 us: 1.32x slower                                                 |
| logging_format             | 6.23 us                                                | 8.38 us: 1.35x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 2.15 sec: 1.46x slower                                                |
| pprint_safe_repr           | 727 ms                                                 | 1.06 sec: 1.46x slower                                                |
| subparsers                 | 15.5 ms                                                | 28.4 ms: 1.84x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 104 ms: 4.33x slower                                                  |
| coverage                   | 82.8 ms                                                | 518 ms: 6.26x slower                                                  |
| logging_silent             | 101 ns                                                 | 633 ns: 6.27x slower                                                  |
| thrift                     | 800 us                                                 | 149 ms: 185.72x slower                                                |
| Geometric mean             | (ref)                                                  | 1.20x slower                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, pylint, k_core
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.150x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.07x
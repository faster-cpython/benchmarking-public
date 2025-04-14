# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_peephole
- machine: linux-x86_64
- commit hash: edb68e1
- commit date: 2025-04-08
- overall geometric mean: 1.064x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                 |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                               |
| html5lib       | 63.4 ms                                                | 60.9 ms: 1.04x faster                                                |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                 |
| async_tree_io              | 838 ms                                                 | 613 ms: 1.37x faster                                                 |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                 |
| async_generators           | 433 ms                                                 | 418 ms: 1.04x faster                                                 |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                 |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                                |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 68.8 ms: 1.14x faster                                                |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                 |
| nbody          | 87.7 ms                                                | 88.4 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.04x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 21.9 ms: 1.22x faster                                                |
| regex_effbot   | 3.77 ms                                                | 3.22 ms: 1.17x faster                                                |
| regex_dna      | 220 ms                                                 | 207 ms: 1.06x faster                                                 |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.83 sec: 1.16x faster                                               |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 81.0 ms: 1.07x faster                                                |
| xml_etree_process    | 60.5 ms                                                | 56.6 ms: 1.07x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 97.1 ms: 1.04x faster                                                |
| unpickle_pure_python | 213 us                                                 | 208 us: 1.02x faster                                                 |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.05x slower                                                 |
| json_loads           | 27.2 us                                                | 29.4 us: 1.08x slower                                                |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.13x slower                                                |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                |
| python_startup_no_site | 7.00 ms                                                | 8.18 ms: 1.17x slower                                                |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.7 ms: 1.09x faster                                                |
| genshi_xml      | 50.5 ms                                                | 49.0 ms: 1.03x faster                                                |
| mako            | 10.7 ms                                                | 10.8 ms: 1.01x slower                                                |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.09x faster                                               |
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                 |
| deepcopy                   | 354 us                                                 | 251 us: 1.41x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                 |
| async_tree_io              | 838 ms                                                 | 613 ms: 1.37x faster                                                 |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                 |
| deepcopy_memo              | 38.4 us                                                | 28.7 us: 1.34x faster                                                |
| richards                   | 47.5 ms                                                | 35.8 ms: 1.33x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                 |
| richards_super             | 53.7 ms                                                | 42.0 ms: 1.28x faster                                                |
| deepcopy_reduce            | 3.24 us                                                | 2.60 us: 1.24x faster                                                |
| regex_v8                   | 26.9 ms                                                | 21.9 ms: 1.22x faster                                                |
| scimark_fft                | 367 ms                                                 | 303 ms: 1.21x faster                                                 |
| go                         | 141 ms                                                 | 120 ms: 1.18x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.22 ms: 1.17x faster                                                |
| tomli_loads                | 2.12 sec                                               | 1.83 sec: 1.16x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                 |
| spectral_norm              | 113 ms                                                 | 98.8 ms: 1.15x faster                                                |
| float                      | 78.7 ms                                                | 68.8 ms: 1.14x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                 |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.51 ms: 1.12x faster                                                |
| pyflate                    | 470 ms                                                 | 422 ms: 1.11x faster                                                 |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                 |
| genshi_text                | 22.6 ms                                                | 20.7 ms: 1.09x faster                                                |
| telco                      | 8.40 ms                                                | 7.68 ms: 1.09x faster                                                |
| xml_etree_generate         | 86.8 ms                                                | 81.0 ms: 1.07x faster                                                |
| xml_etree_process          | 60.5 ms                                                | 56.6 ms: 1.07x faster                                                |
| dulwich_log                | 64.6 ms                                                | 60.7 ms: 1.07x faster                                                |
| scimark_sor                | 122 ms                                                 | 115 ms: 1.06x faster                                                 |
| regex_dna                  | 220 ms                                                 | 207 ms: 1.06x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.73 us: 1.06x faster                                                |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                 |
| deltablue                  | 3.19 ms                                                | 3.04 ms: 1.05x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.48 sec: 1.05x faster                                               |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 97.1 ms: 1.04x faster                                                |
| html5lib                   | 63.4 ms                                                | 60.9 ms: 1.04x faster                                                |
| async_generators           | 433 ms                                                 | 418 ms: 1.04x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 49.0 ms: 1.03x faster                                                |
| chaos                      | 58.0 ms                                                | 56.4 ms: 1.03x faster                                                |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                               |
| logging_silent             | 101 ns                                                 | 98.2 ns: 1.03x faster                                                |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                               |
| unpickle_pure_python       | 213 us                                                 | 208 us: 1.02x faster                                                 |
| sympy_str                  | 273 ms                                                 | 268 ms: 1.02x faster                                                 |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.02x faster                                               |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                 |
| crypto_pyaes               | 74.7 ms                                                | 74.1 ms: 1.01x faster                                                |
| raytrace                   | 262 ms                                                 | 260 ms: 1.01x faster                                                 |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                 |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                 |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.01x slower                                                |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                 |
| nbody                      | 87.7 ms                                                | 88.4 ms: 1.01x slower                                                |
| generators                 | 28.8 ms                                                | 29.0 ms: 1.01x slower                                                |
| mako                       | 10.7 ms                                                | 10.8 ms: 1.01x slower                                                |
| connected_components       | 447 ms                                                 | 452 ms: 1.01x slower                                                 |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.1 ms: 1.01x slower                                                |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                                 |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                |
| sympy_expand               | 456 ms                                                 | 466 ms: 1.02x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 1.52 sec: 1.03x slower                                               |
| coverage                   | 82.8 ms                                                | 85.1 ms: 1.03x slower                                                |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                               |
| gc_traversal               | 4.90 ms                                                | 5.05 ms: 1.03x slower                                                |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                 |
| fannkuch                   | 394 ms                                                 | 411 ms: 1.04x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.05x slower                                                 |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                                |
| json_loads                 | 27.2 us                                                | 29.4 us: 1.08x slower                                                |
| hexiom                     | 6.08 ms                                                | 6.60 ms: 1.09x slower                                                |
| bench_thread_pool          | 818 us                                                 | 892 us: 1.09x slower                                                 |
| many_optionals             | 857 us                                                 | 941 us: 1.10x slower                                                 |
| comprehensions             | 16.5 us                                                | 18.5 us: 1.12x slower                                                |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.13x slower                                                |
| python_startup_no_site     | 7.00 ms                                                | 8.18 ms: 1.17x slower                                                |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 82.0 ms: 3.42x slower                                                |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                         |

Benchmark hidden because not significant (8): scimark_monte_carlo, json, logging_simple, sqlalchemy_declarative, logging_format, shortest_path, pprint_safe_repr, nqueens
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250408-3.14.0a7+-edb68e1-JIT/bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.05x
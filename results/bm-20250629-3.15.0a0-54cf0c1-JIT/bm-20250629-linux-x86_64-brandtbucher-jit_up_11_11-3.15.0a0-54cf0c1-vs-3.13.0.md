# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_11_11
- machine: linux-x86_64
- commit hash: 54cf0c1
- commit date: 2025-06-29
- overall geometric mean: 1.060x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.02x slower                                              |
| html5lib       | 63.4 ms                                                | 62.2 ms: 1.02x faster                                               |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                                |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 637 ms: 1.35x faster                                                |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                                |
| coroutines                 | 22.2 ms                                                | 25.8 ms: 1.16x slower                                               |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                        |

Benchmark hidden because not significant (2): async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.9 ms: 1.19x faster                                               |
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                                |
| nbody          | 87.7 ms                                                | 95.2 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.0 ms: 1.17x faster                                               |
| regex_effbot   | 3.77 ms                                                | 3.44 ms: 1.10x faster                                               |
| regex_dna      | 220 ms                                                 | 207 ms: 1.06x faster                                                |
| regex_compile  | 132 ms                                                 | 126 ms: 1.04x faster                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.83 sec: 1.16x faster                                              |
| unpickle_pure_python | 213 us                                                 | 192 us: 1.11x faster                                                |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                |
| xml_etree_process    | 60.5 ms                                                | 56.4 ms: 1.07x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 81.1 ms: 1.07x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 98.9 ms: 1.02x faster                                               |
| json_loads           | 27.2 us                                                | 28.0 us: 1.03x slower                                               |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.10x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                               |
| python_startup_no_site | 7.00 ms                                                | 6.94 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.9 ms: 1.03x faster                                               |
| genshi_xml      | 50.5 ms                                                | 50.2 ms: 1.01x faster                                               |
| django_template | 31.7 ms                                                | 32.7 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.08x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                                |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                |
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 637 ms: 1.35x faster                                                |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 29.7 us: 1.29x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                |
| spectral_norm              | 113 ms                                                 | 91.2 ms: 1.24x faster                                               |
| go                         | 141 ms                                                 | 114 ms: 1.23x faster                                                |
| richards                   | 47.5 ms                                                | 39.2 ms: 1.21x faster                                               |
| float                      | 78.7 ms                                                | 65.9 ms: 1.19x faster                                               |
| richards_super             | 53.7 ms                                                | 45.1 ms: 1.19x faster                                               |
| scimark_fft                | 367 ms                                                 | 309 ms: 1.19x faster                                                |
| regex_v8                   | 26.9 ms                                                | 23.0 ms: 1.17x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.78 us: 1.16x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.83 sec: 1.16x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                |
| pyflate                    | 470 ms                                                 | 416 ms: 1.13x faster                                                |
| unpickle_pure_python       | 213 us                                                 | 192 us: 1.11x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                                |
| pylint                     | 312 ms                                                 | 283 ms: 1.10x faster                                                |
| regex_effbot               | 3.77 ms                                                | 3.44 ms: 1.10x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.34 sec: 1.08x faster                                              |
| dulwich_log                | 64.6 ms                                                | 59.9 ms: 1.08x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                              |
| xml_etree_process          | 60.5 ms                                                | 56.4 ms: 1.07x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 81.1 ms: 1.07x faster                                               |
| telco                      | 8.40 ms                                                | 7.87 ms: 1.07x faster                                               |
| regex_dna                  | 220 ms                                                 | 207 ms: 1.06x faster                                                |
| crypto_pyaes               | 74.7 ms                                                | 70.7 ms: 1.06x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.80 ms: 1.05x faster                                               |
| deltablue                  | 3.19 ms                                                | 3.05 ms: 1.05x faster                                               |
| regex_compile              | 132 ms                                                 | 126 ms: 1.04x faster                                                |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                                |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                               |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                              |
| genshi_text                | 22.6 ms                                                | 21.9 ms: 1.03x faster                                               |
| scimark_monte_carlo        | 66.8 ms                                                | 64.8 ms: 1.03x faster                                               |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                |
| pprint_safe_repr           | 727 ms                                                 | 709 ms: 1.03x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 98.9 ms: 1.02x faster                                               |
| thrift                     | 800 us                                                 | 783 us: 1.02x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                               |
| json                       | 5.32 ms                                                | 5.22 ms: 1.02x faster                                               |
| logging_silent             | 101 ns                                                 | 99.2 ns: 1.02x faster                                               |
| html5lib                   | 63.4 ms                                                | 62.2 ms: 1.02x faster                                               |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.02x faster                                               |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.01x faster                                              |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.01x faster                                              |
| comprehensions             | 16.5 us                                                | 16.3 us: 1.01x faster                                               |
| python_startup_no_site     | 7.00 ms                                                | 6.94 ms: 1.01x faster                                               |
| genshi_xml                 | 50.5 ms                                                | 50.2 ms: 1.01x faster                                               |
| gc_traversal               | 4.90 ms                                                | 4.91 ms: 1.00x slower                                               |
| fannkuch                   | 394 ms                                                 | 395 ms: 1.00x slower                                                |
| hexiom                     | 6.08 ms                                                | 6.11 ms: 1.01x slower                                               |
| logging_format             | 6.23 us                                                | 6.30 us: 1.01x slower                                               |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                                |
| nqueens                    | 80.9 ms                                                | 82.5 ms: 1.02x slower                                               |
| shortest_path              | 487 ms                                                 | 498 ms: 1.02x slower                                                |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.02x slower                                              |
| sympy_expand               | 456 ms                                                 | 468 ms: 1.03x slower                                                |
| connected_components       | 447 ms                                                 | 459 ms: 1.03x slower                                                |
| json_loads                 | 27.2 us                                                | 28.0 us: 1.03x slower                                               |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                                |
| django_template            | 31.7 ms                                                | 32.7 ms: 1.03x slower                                               |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                |
| chaos                      | 58.0 ms                                                | 61.1 ms: 1.05x slower                                               |
| generators                 | 28.8 ms                                                | 30.3 ms: 1.05x slower                                               |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                |
| coverage                   | 82.8 ms                                                | 87.7 ms: 1.06x slower                                               |
| create_gc_cycles           | 2.45 ms                                                | 2.60 ms: 1.06x slower                                               |
| nbody                      | 87.7 ms                                                | 95.2 ms: 1.09x slower                                               |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.10x slower                                               |
| many_optionals             | 857 us                                                 | 986 us: 1.15x slower                                                |
| coroutines                 | 22.2 ms                                                | 25.8 ms: 1.16x slower                                               |
| subparsers                 | 15.5 ms                                                | 23.8 ms: 1.54x slower                                               |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (8): meteor_contest, sympy_str, logging_simple, sympy_sum, async_generators, asyncio_websockets, djangocms, mako
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250629-3.15.0a0-54cf0c1-JIT/bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x
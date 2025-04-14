# Results vs. 3.13.0

- fork: brandtbucher
- ref: keep_stack_pointer
- machine: linux-x86_64
- commit hash: b3d84fd
- commit date: 2025-03-26
- overall geometric mean: 1.077x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 248 ms: 1.07x faster                                                       |
| docutils       | 2.58 sec                                               | 2.55 sec: 1.01x faster                                                     |
| html5lib       | 63.4 ms                                                | 57.7 ms: 1.10x faster                                                      |
| sphinx         | 1.03 sec                                               | 978 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 302 ms: 1.53x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 305 ms: 1.43x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 607 ms: 1.42x faster                                                       |
| async_tree_none            | 350 ms                                                 | 249 ms: 1.41x faster                                                       |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 242 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 497 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                       |
| async_generators           | 433 ms                                                 | 383 ms: 1.13x faster                                                       |
| coroutines                 | 22.2 ms                                                | 22.0 ms: 1.01x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 68.1 ms: 1.16x faster                                                      |
| nbody          | 87.7 ms                                                | 81.2 ms: 1.08x faster                                                      |
| pidigits       | 186 ms                                                 | 202 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.07 ms: 1.23x faster                                                      |
| regex_dna      | 220 ms                                                 | 183 ms: 1.20x faster                                                       |
| regex_v8       | 26.9 ms                                                | 23.0 ms: 1.17x faster                                                      |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                  | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.87 sec: 1.13x faster                                                     |
| xml_etree_process    | 60.5 ms                                                | 58.9 ms: 1.03x faster                                                      |
| pickle_pure_python   | 302 us                                                 | 304 us: 1.00x slower                                                       |
| unpickle_pure_python | 213 us                                                 | 214 us: 1.00x slower                                                       |
| xml_etree_generate   | 86.8 ms                                                | 87.9 ms: 1.01x slower                                                      |
| xml_etree_parse      | 154 ms                                                 | 158 ms: 1.02x slower                                                       |
| json_loads           | 27.2 us                                                | 29.0 us: 1.07x slower                                                      |
| json_dumps           | 10.1 ms                                                | 12.4 ms: 1.23x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                      |
| python_startup_no_site | 7.00 ms                                                | 8.12 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.4 ms: 1.11x faster                                                      |
| genshi_xml      | 50.5 ms                                                | 46.9 ms: 1.08x faster                                                      |
| django_template | 31.7 ms                                                | 30.7 ms: 1.03x faster                                                      |
| mako            | 10.7 ms                                                | 11.6 ms: 1.08x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 302 ms: 1.53x faster                                                       |
| deepcopy                   | 354 us                                                 | 245 us: 1.45x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 305 ms: 1.43x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 607 ms: 1.42x faster                                                       |
| async_tree_none            | 350 ms                                                 | 249 ms: 1.41x faster                                                       |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                       |
| spectral_norm              | 113 ms                                                 | 83.9 ms: 1.35x faster                                                      |
| deepcopy_memo              | 38.4 us                                                | 28.9 us: 1.33x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 242 ms: 1.32x faster                                                       |
| go                         | 141 ms                                                 | 109 ms: 1.29x faster                                                       |
| deepcopy_reduce            | 3.24 us                                                | 2.59 us: 1.25x faster                                                      |
| regex_effbot               | 3.77 ms                                                | 3.07 ms: 1.23x faster                                                      |
| scimark_fft                | 367 ms                                                 | 301 ms: 1.22x faster                                                       |
| regex_dna                  | 220 ms                                                 | 183 ms: 1.20x faster                                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.30 ms: 1.17x faster                                                      |
| pathlib                    | 17.4 ms                                                | 14.9 ms: 1.17x faster                                                      |
| regex_v8                   | 26.9 ms                                                | 23.0 ms: 1.17x faster                                                      |
| float                      | 78.7 ms                                                | 68.1 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 497 ms: 1.15x faster                                                       |
| pylint                     | 312 ms                                                 | 272 ms: 1.15x faster                                                       |
| richards                   | 47.5 ms                                                | 41.5 ms: 1.15x faster                                                      |
| pyflate                    | 470 ms                                                 | 411 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                       |
| logging_silent             | 101 ns                                                 | 89.0 ns: 1.13x faster                                                      |
| async_generators           | 433 ms                                                 | 383 ms: 1.13x faster                                                       |
| scimark_sor                | 122 ms                                                 | 108 ms: 1.13x faster                                                       |
| tomli_loads                | 2.12 sec                                               | 1.87 sec: 1.13x faster                                                     |
| telco                      | 8.40 ms                                                | 7.45 ms: 1.13x faster                                                      |
| dulwich_log                | 64.6 ms                                                | 57.4 ms: 1.13x faster                                                      |
| richards_super             | 53.7 ms                                                | 48.1 ms: 1.12x faster                                                      |
| genshi_text                | 22.6 ms                                                | 20.4 ms: 1.11x faster                                                      |
| scimark_monte_carlo        | 66.8 ms                                                | 60.6 ms: 1.10x faster                                                      |
| html5lib                   | 63.4 ms                                                | 57.7 ms: 1.10x faster                                                      |
| deltablue                  | 3.19 ms                                                | 2.93 ms: 1.09x faster                                                      |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                                     |
| sqlite_synth               | 2.90 us                                                | 2.69 us: 1.08x faster                                                      |
| nbody                      | 87.7 ms                                                | 81.2 ms: 1.08x faster                                                      |
| genshi_xml                 | 50.5 ms                                                | 46.9 ms: 1.08x faster                                                      |
| chaos                      | 58.0 ms                                                | 54.1 ms: 1.07x faster                                                      |
| 2to3                       | 266 ms                                                 | 248 ms: 1.07x faster                                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.38 sec: 1.07x faster                                                     |
| scimark_lu                 | 114 ms                                                 | 107 ms: 1.07x faster                                                       |
| thrift                     | 800 us                                                 | 754 us: 1.06x faster                                                       |
| sympy_integrate            | 19.8 ms                                                | 18.7 ms: 1.06x faster                                                      |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                       |
| hexiom                     | 6.08 ms                                                | 5.74 ms: 1.06x faster                                                      |
| sphinx                     | 1.03 sec                                               | 978 ms: 1.06x faster                                                       |
| comprehensions             | 16.5 us                                                | 15.6 us: 1.05x faster                                                      |
| crypto_pyaes               | 74.7 ms                                                | 71.0 ms: 1.05x faster                                                      |
| nqueens                    | 80.9 ms                                                | 77.4 ms: 1.04x faster                                                      |
| raytrace                   | 262 ms                                                 | 250 ms: 1.04x faster                                                       |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.04x faster                                                       |
| sympy_str                  | 273 ms                                                 | 262 ms: 1.04x faster                                                       |
| logging_simple             | 5.65 us                                                | 5.42 us: 1.04x faster                                                      |
| logging_format             | 6.23 us                                                | 5.98 us: 1.04x faster                                                      |
| sympy_sum                  | 150 ms                                                 | 145 ms: 1.04x faster                                                       |
| generators                 | 28.8 ms                                                | 27.7 ms: 1.04x faster                                                      |
| typing_runtime_protocols   | 160 us                                                 | 154 us: 1.04x faster                                                       |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.3 ms: 1.04x faster                                                      |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                     |
| django_template            | 31.7 ms                                                | 30.7 ms: 1.03x faster                                                      |
| xml_etree_process          | 60.5 ms                                                | 58.9 ms: 1.03x faster                                                      |
| sympy_expand               | 456 ms                                                 | 445 ms: 1.03x faster                                                       |
| coverage                   | 82.8 ms                                                | 81.0 ms: 1.02x faster                                                      |
| docutils                   | 2.58 sec                                               | 2.55 sec: 1.01x faster                                                     |
| coroutines                 | 22.2 ms                                                | 22.0 ms: 1.01x faster                                                      |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.01x faster                                                       |
| pickle_pure_python         | 302 us                                                 | 304 us: 1.00x slower                                                       |
| unpickle_pure_python       | 213 us                                                 | 214 us: 1.00x slower                                                       |
| xml_etree_generate         | 86.8 ms                                                | 87.9 ms: 1.01x slower                                                      |
| gc_traversal               | 4.90 ms                                                | 4.96 ms: 1.01x slower                                                      |
| pprint_safe_repr           | 727 ms                                                 | 738 ms: 1.02x slower                                                       |
| pprint_pformat             | 1.48 sec                                               | 1.51 sec: 1.02x slower                                                     |
| bench_thread_pool          | 818 us                                                 | 834 us: 1.02x slower                                                       |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                      |
| xml_etree_parse            | 154 ms                                                 | 158 ms: 1.02x slower                                                       |
| fannkuch                   | 394 ms                                                 | 407 ms: 1.03x slower                                                       |
| shortest_path              | 487 ms                                                 | 504 ms: 1.03x slower                                                       |
| create_gc_cycles           | 2.45 ms                                                | 2.55 ms: 1.04x slower                                                      |
| connected_components       | 447 ms                                                 | 470 ms: 1.05x slower                                                       |
| json_loads                 | 27.2 us                                                | 29.0 us: 1.07x slower                                                      |
| mdp                        | 2.54 sec                                               | 2.72 sec: 1.07x slower                                                     |
| pidigits                   | 186 ms                                                 | 202 ms: 1.08x slower                                                       |
| mako                       | 10.7 ms                                                | 11.6 ms: 1.08x slower                                                      |
| many_optionals             | 857 us                                                 | 933 us: 1.09x slower                                                       |
| python_startup_no_site     | 7.00 ms                                                | 8.12 ms: 1.16x slower                                                      |
| json_dumps                 | 10.1 ms                                                | 12.4 ms: 1.23x slower                                                      |
| subparsers                 | 15.5 ms                                                | 20.5 ms: 1.32x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                               |

Benchmark hidden because not significant (3): json, asyncio_websockets, xml_etree_iterparse
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250326-3.14.0a6+-b3d84fd-CLANG/bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.077x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.04x
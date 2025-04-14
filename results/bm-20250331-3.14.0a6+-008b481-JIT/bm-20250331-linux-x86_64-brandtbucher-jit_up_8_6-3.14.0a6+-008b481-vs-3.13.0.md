# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_8_6
- machine: linux-x86_64
- commit hash: 008b481
- commit date: 2025-03-31
- overall geometric mean: 1.034x faster
- HPT reliability: 90.07%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 270 ms: 1.02x slower                                               |
| docutils       | 2.58 sec                                               | 2.72 sec: 1.05x slower                                             |
| html5lib       | 63.4 ms                                                | 62.8 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                               |
| async_tree_io              | 838 ms                                                 | 618 ms: 1.36x faster                                               |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                               |
| async_generators           | 433 ms                                                 | 420 ms: 1.03x faster                                               |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                              |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.3 ms: 1.19x faster                                              |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                               |
| nbody          | 87.7 ms                                                | 88.6 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                  | 1.06x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.8 ms: 1.18x faster                                              |
| regex_effbot   | 3.77 ms                                                | 3.23 ms: 1.16x faster                                              |
| regex_dna      | 220 ms                                                 | 213 ms: 1.03x faster                                               |
| regex_compile  | 132 ms                                                 | 130 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.10x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.87 sec: 1.13x faster                                             |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 80.9 ms: 1.07x faster                                              |
| xml_etree_process    | 60.5 ms                                                | 56.8 ms: 1.06x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 98.4 ms: 1.03x faster                                              |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                               |
| pickle_pure_python   | 302 us                                                 | 325 us: 1.08x slower                                               |
| json_loads           | 27.2 us                                                | 29.7 us: 1.09x slower                                              |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.14x slower                                              |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                              |
| python_startup_no_site | 7.00 ms                                                | 8.18 ms: 1.17x slower                                              |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.3 ms: 1.06x faster                                              |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                              |
| mako            | 10.7 ms                                                | 11.1 ms: 1.04x slower                                              |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                               |
| async_tree_io              | 838 ms                                                 | 618 ms: 1.36x faster                                               |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                               |
| deepcopy                   | 354 us                                                 | 265 us: 1.34x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 29.2 us: 1.32x faster                                              |
| richards                   | 47.5 ms                                                | 37.4 ms: 1.27x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                               |
| richards_super             | 53.7 ms                                                | 43.0 ms: 1.25x faster                                              |
| float                      | 78.7 ms                                                | 66.3 ms: 1.19x faster                                              |
| spectral_norm              | 113 ms                                                 | 95.5 ms: 1.19x faster                                              |
| regex_v8                   | 26.9 ms                                                | 22.8 ms: 1.18x faster                                              |
| regex_effbot               | 3.77 ms                                                | 3.23 ms: 1.16x faster                                              |
| scimark_fft                | 367 ms                                                 | 315 ms: 1.16x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.79 us: 1.16x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.87 sec: 1.13x faster                                             |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                               |
| go                         | 141 ms                                                 | 129 ms: 1.09x faster                                               |
| pylint                     | 312 ms                                                 | 288 ms: 1.08x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.66 ms: 1.08x faster                                              |
| xml_etree_generate         | 86.8 ms                                                | 80.9 ms: 1.07x faster                                              |
| dulwich_log                | 64.6 ms                                                | 60.4 ms: 1.07x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.72 us: 1.07x faster                                              |
| telco                      | 8.40 ms                                                | 7.89 ms: 1.06x faster                                              |
| xml_etree_process          | 60.5 ms                                                | 56.8 ms: 1.06x faster                                              |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                              |
| deltablue                  | 3.19 ms                                                | 3.05 ms: 1.05x faster                                              |
| logging_silent             | 101 ns                                                 | 96.8 ns: 1.04x faster                                              |
| thrift                     | 800 us                                                 | 769 us: 1.04x faster                                               |
| regex_dna                  | 220 ms                                                 | 213 ms: 1.03x faster                                               |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                              |
| async_generators           | 433 ms                                                 | 420 ms: 1.03x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 98.4 ms: 1.03x faster                                              |
| logging_simple             | 5.65 us                                                | 5.51 us: 1.03x faster                                              |
| pyflate                    | 470 ms                                                 | 460 ms: 1.02x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                             |
| k_core                     | 2.37 sec                                               | 2.33 sec: 1.02x faster                                             |
| logging_format             | 6.23 us                                                | 6.14 us: 1.01x faster                                              |
| regex_compile              | 132 ms                                                 | 130 ms: 1.01x faster                                               |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                               |
| mdp                        | 2.54 sec                                               | 2.52 sec: 1.01x faster                                             |
| html5lib                   | 63.4 ms                                                | 62.8 ms: 1.01x faster                                              |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                               |
| nbody                      | 87.7 ms                                                | 88.6 ms: 1.01x slower                                              |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                               |
| 2to3                       | 266 ms                                                 | 270 ms: 1.02x slower                                               |
| crypto_pyaes               | 74.7 ms                                                | 76.2 ms: 1.02x slower                                              |
| create_gc_cycles           | 2.45 ms                                                | 2.50 ms: 1.02x slower                                              |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                              |
| gc_traversal               | 4.90 ms                                                | 5.00 ms: 1.02x slower                                              |
| generators                 | 28.8 ms                                                | 29.4 ms: 1.02x slower                                              |
| sympy_str                  | 273 ms                                                 | 280 ms: 1.02x slower                                               |
| raytrace                   | 262 ms                                                 | 268 ms: 1.03x slower                                               |
| scimark_monte_carlo        | 66.8 ms                                                | 68.5 ms: 1.03x slower                                              |
| shortest_path              | 487 ms                                                 | 499 ms: 1.03x slower                                               |
| chaos                      | 58.0 ms                                                | 59.7 ms: 1.03x slower                                              |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.4 ms: 1.03x slower                                              |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                              |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                              |
| sympy_integrate            | 19.8 ms                                                | 20.5 ms: 1.04x slower                                              |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.04x slower                                               |
| coverage                   | 82.8 ms                                                | 86.1 ms: 1.04x slower                                              |
| scimark_lu                 | 114 ms                                                 | 120 ms: 1.05x slower                                               |
| nqueens                    | 80.9 ms                                                | 84.9 ms: 1.05x slower                                              |
| docutils                   | 2.58 sec                                               | 2.72 sec: 1.05x slower                                             |
| sympy_expand               | 456 ms                                                 | 480 ms: 1.05x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.05x slower                                               |
| pprint_safe_repr           | 727 ms                                                 | 766 ms: 1.05x slower                                               |
| sqlalchemy_declarative     | 133 ms                                                 | 141 ms: 1.06x slower                                               |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                              |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.08x slower                                               |
| fannkuch                   | 394 ms                                                 | 428 ms: 1.09x slower                                               |
| pprint_pformat             | 1.48 sec                                               | 1.61 sec: 1.09x slower                                             |
| json_loads                 | 27.2 us                                                | 29.7 us: 1.09x slower                                              |
| bench_thread_pool          | 818 us                                                 | 897 us: 1.10x slower                                               |
| connected_components       | 447 ms                                                 | 492 ms: 1.10x slower                                               |
| comprehensions             | 16.5 us                                                | 18.6 us: 1.13x slower                                              |
| hexiom                     | 6.08 ms                                                | 6.94 ms: 1.14x slower                                              |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.14x slower                                              |
| python_startup_no_site     | 7.00 ms                                                | 8.18 ms: 1.17x slower                                              |
| many_optionals             | 857 us                                                 | 1.00 ms: 1.17x slower                                              |
| subparsers                 | 15.5 ms                                                | 21.1 ms: 1.37x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 83.8 ms: 3.50x slower                                              |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                       |

Benchmark hidden because not significant (6): json, bpe_tokeniser, sphinx, meteor_contest, genshi_xml, asyncio_websockets
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250331-3.14.0a6+-008b481-JIT/bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 90.07% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x
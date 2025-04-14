# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_10_7
- machine: linux-x86_64
- commit hash: c421917
- commit date: 2025-03-29
- overall geometric mean: 1.036x faster
- HPT reliability: 87.37%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 267 ms: 1.01x slower                                                |
| docutils       | 2.58 sec                                               | 2.71 sec: 1.05x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 486 ms: 1.18x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 472 ms: 1.15x faster                                                |
| async_generators           | 433 ms                                                 | 414 ms: 1.05x faster                                                |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                               |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.5 ms: 1.20x faster                                               |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                                |
| nbody          | 87.7 ms                                                | 90.2 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.6 ms: 1.14x faster                                               |
| regex_effbot   | 3.77 ms                                                | 3.45 ms: 1.09x faster                                               |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads         | 2.12 sec                                               | 1.89 sec: 1.12x faster                                              |
| xml_etree_parse     | 154 ms                                                 | 141 ms: 1.10x faster                                                |
| xml_etree_generate  | 86.8 ms                                                | 80.3 ms: 1.08x faster                                               |
| xml_etree_process   | 60.5 ms                                                | 56.3 ms: 1.07x faster                                               |
| xml_etree_iterparse | 101 ms                                                 | 98.1 ms: 1.03x faster                                               |
| pickle_pure_python  | 302 us                                                 | 325 us: 1.07x slower                                                |
| json_loads          | 27.2 us                                                | 30.2 us: 1.11x slower                                               |
| json_dumps          | 10.1 ms                                                | 11.7 ms: 1.16x slower                                               |
| Geometric mean      | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                               |
| python_startup_no_site | 7.00 ms                                                | 8.19 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.06x faster                                               |
| genshi_xml      | 50.5 ms                                                | 49.7 ms: 1.02x faster                                               |
| django_template | 31.7 ms                                                | 32.1 ms: 1.01x slower                                               |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                |
| richards_super             | 53.7 ms                                                | 40.1 ms: 1.34x faster                                               |
| deepcopy                   | 354 us                                                 | 266 us: 1.33x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 28.9 us: 1.33x faster                                               |
| richards                   | 47.5 ms                                                | 35.8 ms: 1.33x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                |
| float                      | 78.7 ms                                                | 65.5 ms: 1.20x faster                                               |
| spectral_norm              | 113 ms                                                 | 94.9 ms: 1.19x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 486 ms: 1.18x faster                                                |
| scimark_fft                | 367 ms                                                 | 313 ms: 1.17x faster                                                |
| deepcopy_reduce            | 3.24 us                                                | 2.80 us: 1.16x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 472 ms: 1.15x faster                                                |
| regex_v8                   | 26.9 ms                                                | 23.6 ms: 1.14x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.89 sec: 1.12x faster                                              |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.10x faster                                                |
| pylint                     | 312 ms                                                 | 285 ms: 1.09x faster                                                |
| regex_effbot               | 3.77 ms                                                | 3.45 ms: 1.09x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 80.3 ms: 1.08x faster                                               |
| pyflate                    | 470 ms                                                 | 436 ms: 1.08x faster                                                |
| telco                      | 8.40 ms                                                | 7.82 ms: 1.07x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 56.3 ms: 1.07x faster                                               |
| dulwich_log                | 64.6 ms                                                | 60.4 ms: 1.07x faster                                               |
| go                         | 141 ms                                                 | 132 ms: 1.07x faster                                                |
| sqlite_synth               | 2.90 us                                                | 2.73 us: 1.06x faster                                               |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                               |
| deltablue                  | 3.19 ms                                                | 3.04 ms: 1.05x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.78 ms: 1.05x faster                                               |
| async_generators           | 433 ms                                                 | 414 ms: 1.05x faster                                                |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.03x faster                                                |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 98.1 ms: 1.03x faster                                               |
| thrift                     | 800 us                                                 | 778 us: 1.03x faster                                                |
| logging_silent             | 101 ns                                                 | 98.5 ns: 1.03x faster                                               |
| k_core                     | 2.37 sec                                               | 2.32 sec: 1.02x faster                                              |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.61 sec: 1.02x faster                                              |
| genshi_xml                 | 50.5 ms                                                | 49.7 ms: 1.02x faster                                               |
| logging_simple             | 5.65 us                                                | 5.57 us: 1.02x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.01x faster                                              |
| logging_format             | 6.23 us                                                | 6.17 us: 1.01x faster                                               |
| pidigits                   | 186 ms                                                 | 185 ms: 1.01x faster                                                |
| 2to3                       | 266 ms                                                 | 267 ms: 1.01x slower                                                |
| mdp                        | 2.54 sec                                               | 2.57 sec: 1.01x slower                                              |
| shortest_path              | 487 ms                                                 | 492 ms: 1.01x slower                                                |
| django_template            | 31.7 ms                                                | 32.1 ms: 1.01x slower                                               |
| gc_traversal               | 4.90 ms                                                | 4.98 ms: 1.02x slower                                               |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                               |
| sympy_str                  | 273 ms                                                 | 279 ms: 1.02x slower                                                |
| generators                 | 28.8 ms                                                | 29.4 ms: 1.02x slower                                               |
| crypto_pyaes               | 74.7 ms                                                | 76.4 ms: 1.02x slower                                               |
| raytrace                   | 262 ms                                                 | 269 ms: 1.03x slower                                                |
| sympy_integrate            | 19.8 ms                                                | 20.4 ms: 1.03x slower                                               |
| nbody                      | 87.7 ms                                                | 90.2 ms: 1.03x slower                                               |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                               |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 137 ms: 1.03x slower                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 69.0 ms: 1.03x slower                                               |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                               |
| coverage                   | 82.8 ms                                                | 85.8 ms: 1.04x slower                                               |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.6 ms: 1.04x slower                                               |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.04x slower                                                |
| chaos                      | 58.0 ms                                                | 60.5 ms: 1.04x slower                                               |
| docutils                   | 2.58 sec                                               | 2.71 sec: 1.05x slower                                              |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                |
| sympy_expand               | 456 ms                                                 | 481 ms: 1.05x slower                                                |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                               |
| nqueens                    | 80.9 ms                                                | 86.1 ms: 1.06x slower                                               |
| pprint_pformat             | 1.48 sec                                               | 1.58 sec: 1.07x slower                                              |
| fannkuch                   | 394 ms                                                 | 422 ms: 1.07x slower                                                |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.07x slower                                                |
| pprint_safe_repr           | 727 ms                                                 | 783 ms: 1.08x slower                                                |
| connected_components       | 447 ms                                                 | 483 ms: 1.08x slower                                                |
| bench_thread_pool          | 818 us                                                 | 892 us: 1.09x slower                                                |
| json_loads                 | 27.2 us                                                | 30.2 us: 1.11x slower                                               |
| comprehensions             | 16.5 us                                                | 19.0 us: 1.16x slower                                               |
| hexiom                     | 6.08 ms                                                | 7.04 ms: 1.16x slower                                               |
| many_optionals             | 857 us                                                 | 993 us: 1.16x slower                                                |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.16x slower                                               |
| python_startup_no_site     | 7.00 ms                                                | 8.19 ms: 1.17x slower                                               |
| subparsers                 | 15.5 ms                                                | 21.2 ms: 1.37x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.46x slower                                               |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (7): meteor_contest, asyncio_websockets, html5lib, json, unpickle_pure_python, sphinx, regex_dna
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250329-3.14.0a6+-c421917-JIT/bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 87.37% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x
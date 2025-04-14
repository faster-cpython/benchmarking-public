# Results vs. 3.13.0

- fork: iritkatriel
- ref: tuple
- machine: linux-x86_64
- commit hash: d737f33
- commit date: 2025-03-23
- overall geometric mean: 1.040x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.04x faster                                         |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                       |
| html5lib       | 63.4 ms                                                | 61.4 ms: 1.03x faster                                        |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                         |
| async_tree_io              | 838 ms                                                 | 611 ms: 1.37x faster                                         |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                         |
| async_generators           | 433 ms                                                 | 399 ms: 1.08x faster                                         |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                        |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.5 ms: 1.12x faster                                        |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                         |
| nbody          | 87.7 ms                                                | 97.4 ms: 1.11x slower                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 24.2 ms: 1.11x faster                                        |
| regex_effbot   | 3.77 ms                                                | 3.49 ms: 1.08x faster                                        |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                         |
| regex_dna      | 220 ms                                                 | 227 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.10x faster                                         |
| tomli_loads          | 2.12 sec                                               | 1.97 sec: 1.07x faster                                       |
| xml_etree_process    | 60.5 ms                                                | 58.3 ms: 1.04x faster                                        |
| xml_etree_generate   | 86.8 ms                                                | 84.2 ms: 1.03x faster                                        |
| xml_etree_iterparse  | 101 ms                                                 | 98.7 ms: 1.03x faster                                        |
| unpickle_pure_python | 213 us                                                 | 220 us: 1.03x slower                                         |
| pickle_pure_python   | 302 us                                                 | 315 us: 1.04x slower                                         |
| json_loads           | 27.2 us                                                | 30.0 us: 1.10x slower                                        |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.16x slower                                        |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.05x slower                                        |
| python_startup_no_site | 7.00 ms                                                | 8.24 ms: 1.18x slower                                        |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                        |
| genshi_xml      | 50.5 ms                                                | 49.2 ms: 1.03x faster                                        |
| django_template | 31.7 ms                                                | 31.3 ms: 1.01x faster                                        |
| mako            | 10.7 ms                                                | 11.4 ms: 1.07x slower                                        |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                         |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                         |
| async_tree_io              | 838 ms                                                 | 611 ms: 1.37x faster                                         |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                         |
| deepcopy_memo              | 38.4 us                                                | 29.4 us: 1.31x faster                                        |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                         |
| go                         | 141 ms                                                 | 114 ms: 1.23x faster                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                        |
| spectral_norm              | 113 ms                                                 | 97.4 ms: 1.16x faster                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                         |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                         |
| float                      | 78.7 ms                                                | 70.5 ms: 1.12x faster                                        |
| regex_v8                   | 26.9 ms                                                | 24.2 ms: 1.11x faster                                        |
| richards                   | 47.5 ms                                                | 43.2 ms: 1.10x faster                                        |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.10x faster                                         |
| dulwich_log                | 64.6 ms                                                | 59.2 ms: 1.09x faster                                        |
| richards_super             | 53.7 ms                                                | 49.4 ms: 1.09x faster                                        |
| async_generators           | 433 ms                                                 | 399 ms: 1.08x faster                                         |
| regex_effbot               | 3.77 ms                                                | 3.49 ms: 1.08x faster                                        |
| telco                      | 8.40 ms                                                | 7.82 ms: 1.07x faster                                        |
| tomli_loads                | 2.12 sec                                               | 1.97 sec: 1.07x faster                                       |
| pyflate                    | 470 ms                                                 | 440 ms: 1.07x faster                                         |
| sympy_str                  | 273 ms                                                 | 260 ms: 1.05x faster                                         |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                        |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                        |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.05x faster                                         |
| thrift                     | 800 us                                                 | 765 us: 1.05x faster                                         |
| scimark_fft                | 367 ms                                                 | 351 ms: 1.04x faster                                         |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                         |
| sympy_sum                  | 150 ms                                                 | 145 ms: 1.04x faster                                         |
| xml_etree_process          | 60.5 ms                                                | 58.3 ms: 1.04x faster                                        |
| 2to3                       | 266 ms                                                 | 257 ms: 1.04x faster                                         |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                        |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                       |
| html5lib                   | 63.4 ms                                                | 61.4 ms: 1.03x faster                                        |
| xml_etree_generate         | 86.8 ms                                                | 84.2 ms: 1.03x faster                                        |
| mdp                        | 2.54 sec                                               | 2.47 sec: 1.03x faster                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.89 ms: 1.03x faster                                        |
| xml_etree_iterparse        | 101 ms                                                 | 98.7 ms: 1.03x faster                                        |
| genshi_xml                 | 50.5 ms                                                | 49.2 ms: 1.03x faster                                        |
| gc_traversal               | 4.90 ms                                                | 4.78 ms: 1.02x faster                                        |
| logging_silent             | 101 ns                                                 | 98.9 ns: 1.02x faster                                        |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                         |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                       |
| logging_simple             | 5.65 us                                                | 5.57 us: 1.01x faster                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.62 sec: 1.01x faster                                       |
| logging_format             | 6.23 us                                                | 6.14 us: 1.01x faster                                        |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.01x faster                                       |
| django_template            | 31.7 ms                                                | 31.3 ms: 1.01x faster                                        |
| sympy_expand               | 456 ms                                                 | 451 ms: 1.01x faster                                         |
| deltablue                  | 3.19 ms                                                | 3.16 ms: 1.01x faster                                        |
| sympy_integrate            | 19.8 ms                                                | 19.7 ms: 1.01x faster                                        |
| generators                 | 28.8 ms                                                | 28.6 ms: 1.00x faster                                        |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                         |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                       |
| pprint_safe_repr           | 727 ms                                                 | 732 ms: 1.01x slower                                         |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                       |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                        |
| chaos                      | 58.0 ms                                                | 58.7 ms: 1.01x slower                                        |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                        |
| shortest_path              | 487 ms                                                 | 493 ms: 1.01x slower                                         |
| crypto_pyaes               | 74.7 ms                                                | 76.1 ms: 1.02x slower                                        |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                         |
| connected_components       | 447 ms                                                 | 456 ms: 1.02x slower                                         |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.02x slower                                         |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 68.6 ms: 1.03x slower                                        |
| hexiom                     | 6.08 ms                                                | 6.27 ms: 1.03x slower                                        |
| unpickle_pure_python       | 213 us                                                 | 220 us: 1.03x slower                                         |
| regex_dna                  | 220 ms                                                 | 227 ms: 1.03x slower                                         |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                        |
| pickle_pure_python         | 302 us                                                 | 315 us: 1.04x slower                                         |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.05x slower                                        |
| nqueens                    | 80.9 ms                                                | 85.7 ms: 1.06x slower                                        |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.07x slower                                        |
| bench_thread_pool          | 818 us                                                 | 879 us: 1.08x slower                                         |
| json_loads                 | 27.2 us                                                | 30.0 us: 1.10x slower                                        |
| fannkuch                   | 394 ms                                                 | 436 ms: 1.11x slower                                         |
| nbody                      | 87.7 ms                                                | 97.4 ms: 1.11x slower                                        |
| coverage                   | 82.8 ms                                                | 92.0 ms: 1.11x slower                                        |
| many_optionals             | 857 us                                                 | 953 us: 1.11x slower                                         |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.16x slower                                        |
| python_startup_no_site     | 7.00 ms                                                | 8.24 ms: 1.18x slower                                        |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.34x slower                                        |
| bench_mp_pool              | 24.0 ms                                                | 83.6 ms: 3.49x slower                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (3): asyncio_websockets, sqlalchemy_imperative, json
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250323-3.14.0a6+-d737f33/bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
# Results vs. 3.13.0

- fork: mdboom
- ref: pyfloat_fromdouble
- machine: linux-x86_64
- commit hash: 9487962
- commit date: 2025-05-30
- overall geometric mean: 1.039x slower
- HPT reliability: 99.60%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                                |
| docutils       | 2.58 sec                                               | 2.57 sec: 1.00x faster                                              |
| html5lib       | 63.4 ms                                                | 62.4 ms: 1.02x faster                                               |
| sphinx         | 1.03 sec                                               | 1.00 sec: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                                |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                                |
| coroutines                 | 22.2 ms                                                | 24.9 ms: 1.12x slower                                               |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.3 ms: 1.10x faster                                               |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                |
| nbody          | 87.7 ms                                                | 95.8 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                  | 1.00x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.6 ms: 1.14x faster                                               |
| regex_effbot   | 3.77 ms                                                | 3.40 ms: 1.11x faster                                               |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                |
| regex_dna      | 220 ms                                                 | 222 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                |
| tomli_loads          | 2.12 sec                                               | 2.02 sec: 1.05x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 84.8 ms: 1.02x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 59.6 ms: 1.01x faster                                               |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                                |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.06x slower                                                |
| json_loads           | 27.2 us                                                | 29.3 us: 1.08x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.09x slower                                               |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                               |
| python_startup_no_site | 7.00 ms                                                | 6.95 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.06x faster                                               |
| genshi_xml      | 50.5 ms                                                | 49.6 ms: 1.02x faster                                               |
| django_template | 31.7 ms                                                | 33.0 ms: 1.04x slower                                               |
| mako            | 10.7 ms                                                | 11.4 ms: 1.07x slower                                               |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                |
| deepcopy                   | 354 us                                                 | 255 us: 1.39x faster                                                |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                               |
| go                         | 141 ms                                                 | 110 ms: 1.28x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.20x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                |
| regex_v8                   | 26.9 ms                                                | 23.6 ms: 1.14x faster                                               |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                                |
| richards                   | 47.5 ms                                                | 42.7 ms: 1.11x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.40 ms: 1.11x faster                                               |
| richards_super             | 53.7 ms                                                | 48.5 ms: 1.11x faster                                               |
| float                      | 78.7 ms                                                | 71.3 ms: 1.10x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                |
| pyflate                    | 470 ms                                                 | 430 ms: 1.09x faster                                                |
| dulwich_log                | 64.6 ms                                                | 59.7 ms: 1.08x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                              |
| spectral_norm              | 113 ms                                                 | 106 ms: 1.06x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                               |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 18.8 ms: 1.05x faster                                               |
| tomli_loads                | 2.12 sec                                               | 2.02 sec: 1.05x faster                                              |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                                |
| telco                      | 8.40 ms                                                | 8.07 ms: 1.04x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.51 sec: 1.04x faster                                              |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                               |
| comprehensions             | 16.5 us                                                | 15.9 us: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                              |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                               |
| sphinx                     | 1.03 sec                                               | 1.00 sec: 1.03x faster                                              |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.03x faster                                                |
| xml_etree_generate         | 86.8 ms                                                | 84.8 ms: 1.02x faster                                               |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                |
| genshi_xml                 | 50.5 ms                                                | 49.6 ms: 1.02x faster                                               |
| html5lib                   | 63.4 ms                                                | 62.4 ms: 1.02x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 59.6 ms: 1.01x faster                                               |
| json                       | 5.32 ms                                                | 5.26 ms: 1.01x faster                                               |
| sympy_expand               | 456 ms                                                 | 451 ms: 1.01x faster                                                |
| pathlib                    | 17.4 ms                                                | 17.2 ms: 1.01x faster                                               |
| python_startup_no_site     | 7.00 ms                                                | 6.95 ms: 1.01x faster                                               |
| hexiom                     | 6.08 ms                                                | 6.04 ms: 1.01x faster                                               |
| docutils                   | 2.58 sec                                               | 2.57 sec: 1.00x faster                                              |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                |
| regex_dna                  | 220 ms                                                 | 222 ms: 1.01x slower                                                |
| crypto_pyaes               | 74.7 ms                                                | 75.6 ms: 1.01x slower                                               |
| scimark_fft                | 367 ms                                                 | 371 ms: 1.01x slower                                                |
| nqueens                    | 80.9 ms                                                | 82.0 ms: 1.01x slower                                               |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                                |
| raytrace                   | 262 ms                                                 | 268 ms: 1.03x slower                                                |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                                |
| connected_components       | 447 ms                                                 | 462 ms: 1.03x slower                                                |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.20 ms: 1.03x slower                                               |
| gc_traversal               | 4.90 ms                                                | 5.06 ms: 1.03x slower                                               |
| fannkuch                   | 394 ms                                                 | 409 ms: 1.04x slower                                                |
| generators                 | 28.8 ms                                                | 30.0 ms: 1.04x slower                                               |
| django_template            | 31.7 ms                                                | 33.0 ms: 1.04x slower                                               |
| create_gc_cycles           | 2.45 ms                                                | 2.58 ms: 1.05x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.05x slower                                                |
| chaos                      | 58.0 ms                                                | 61.2 ms: 1.06x slower                                               |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.06x slower                                                |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.07x slower                                               |
| shortest_path              | 487 ms                                                 | 523 ms: 1.08x slower                                                |
| deltablue                  | 3.19 ms                                                | 3.44 ms: 1.08x slower                                               |
| json_loads                 | 27.2 us                                                | 29.3 us: 1.08x slower                                               |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.09x slower                                               |
| nbody                      | 87.7 ms                                                | 95.8 ms: 1.09x slower                                               |
| logging_simple             | 5.65 us                                                | 6.21 us: 1.10x slower                                               |
| pprint_safe_repr           | 727 ms                                                 | 810 ms: 1.12x slower                                                |
| pprint_pformat             | 1.48 sec                                               | 1.65 sec: 1.12x slower                                              |
| logging_format             | 6.23 us                                                | 6.97 us: 1.12x slower                                               |
| coroutines                 | 22.2 ms                                                | 24.9 ms: 1.12x slower                                               |
| many_optionals             | 857 us                                                 | 963 us: 1.12x slower                                                |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.53x slower                                               |
| logging_silent             | 101 ns                                                 | 470 ns: 4.65x slower                                                |
| coverage                   | 82.8 ms                                                | 418 ms: 5.05x slower                                                |
| thrift                     | 800 us                                                 | 148 ms: 184.85x slower                                              |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                        |

Benchmark hidden because not significant (3): sqlite_synth, asyncio_websockets, scimark_monte_carlo
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250530-3.15.0a0-9487962/bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.039x slower

# HPT report

- Reliability score: 99.60% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x
# Results vs. 3.13.0

- fork: brandtbucher
- ref: faster_pprint
- machine: linux-x86_64
- commit hash: ccfdf31
- commit date: 2025-06-17
- overall geometric mean: 1.039x faster
- HPT reliability: 99.79%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.04x faster                                                 |
| html5lib       | 63.4 ms                                                | 62.8 ms: 1.01x faster                                                |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                 |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.39x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 633 ms: 1.36x faster                                                 |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 505 ms: 1.13x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 497 ms: 1.09x faster                                                 |
| async_generators           | 433 ms                                                 | 415 ms: 1.04x faster                                                 |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                 |
| coroutines                 | 22.2 ms                                                | 25.9 ms: 1.16x slower                                                |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 73.9 ms: 1.06x faster                                                |
| pidigits       | 186 ms                                                 | 193 ms: 1.03x slower                                                 |
| nbody          | 87.7 ms                                                | 99.9 ms: 1.14x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.0 ms: 1.22x faster                                                |
| regex_effbot   | 3.77 ms                                                | 3.26 ms: 1.16x faster                                                |
| regex_dna      | 220 ms                                                 | 201 ms: 1.10x faster                                                 |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 144 ms: 1.07x faster                                                 |
| tomli_loads          | 2.12 sec                                               | 1.99 sec: 1.06x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 99.0 ms: 1.02x faster                                                |
| xml_etree_generate   | 86.8 ms                                                | 85.9 ms: 1.01x faster                                                |
| unpickle_pure_python | 213 us                                                 | 222 us: 1.04x slower                                                 |
| json_loads           | 27.2 us                                                | 28.5 us: 1.05x slower                                                |
| pickle_pure_python   | 302 us                                                 | 323 us: 1.07x slower                                                 |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.09x slower                                                |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                |
| python_startup_no_site | 7.00 ms                                                | 6.90 ms: 1.01x faster                                                |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.6 ms: 1.05x faster                                                |
| genshi_xml      | 50.5 ms                                                | 49.5 ms: 1.02x faster                                                |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                |
| mako            | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.08x faster                                               |
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                 |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.39x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                 |
| deepcopy                   | 354 us                                                 | 256 us: 1.38x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 633 ms: 1.36x faster                                                 |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                 |
| deepcopy_memo              | 38.4 us                                                | 29.5 us: 1.30x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                 |
| go                         | 141 ms                                                 | 114 ms: 1.23x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 22.0 ms: 1.22x faster                                                |
| deepcopy_reduce            | 3.24 us                                                | 2.76 us: 1.17x faster                                                |
| regex_effbot               | 3.77 ms                                                | 3.26 ms: 1.16x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 505 ms: 1.13x faster                                                 |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                                 |
| regex_dna                  | 220 ms                                                 | 201 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 497 ms: 1.09x faster                                                 |
| richards                   | 47.5 ms                                                | 43.6 ms: 1.09x faster                                                |
| dulwich_log                | 64.6 ms                                                | 59.4 ms: 1.09x faster                                                |
| spectral_norm              | 113 ms                                                 | 105 ms: 1.08x faster                                                 |
| xml_etree_parse            | 154 ms                                                 | 144 ms: 1.07x faster                                                 |
| richards_super             | 53.7 ms                                                | 50.1 ms: 1.07x faster                                                |
| pyflate                    | 470 ms                                                 | 440 ms: 1.07x faster                                                 |
| tomli_loads                | 2.12 sec                                               | 1.99 sec: 1.06x faster                                               |
| float                      | 78.7 ms                                                | 73.9 ms: 1.06x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                               |
| telco                      | 8.40 ms                                                | 7.96 ms: 1.06x faster                                                |
| thrift                     | 800 us                                                 | 764 us: 1.05x faster                                                 |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.05x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.6 ms: 1.05x faster                                                |
| async_generators           | 433 ms                                                 | 415 ms: 1.04x faster                                                 |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                |
| 2to3                       | 266 ms                                                 | 257 ms: 1.04x faster                                                 |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.55 sec: 1.03x faster                                               |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.03x faster                                               |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                               |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.02x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 99.0 ms: 1.02x faster                                                |
| comprehensions             | 16.5 us                                                | 16.1 us: 1.02x faster                                                |
| genshi_xml                 | 50.5 ms                                                | 49.5 ms: 1.02x faster                                                |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.02x faster                                                 |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.01x faster                                                |
| python_startup_no_site     | 7.00 ms                                                | 6.90 ms: 1.01x faster                                                |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.01x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 85.9 ms: 1.01x faster                                                |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.98 ms: 1.01x faster                                                |
| html5lib                   | 63.4 ms                                                | 62.8 ms: 1.01x faster                                                |
| hexiom                     | 6.08 ms                                                | 6.03 ms: 1.01x faster                                                |
| sympy_expand               | 456 ms                                                 | 453 ms: 1.01x faster                                                 |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                               |
| pprint_safe_repr           | 727 ms                                                 | 731 ms: 1.01x slower                                                 |
| nqueens                    | 80.9 ms                                                | 81.4 ms: 1.01x slower                                                |
| crypto_pyaes               | 74.7 ms                                                | 75.7 ms: 1.01x slower                                                |
| scimark_fft                | 367 ms                                                 | 374 ms: 1.02x slower                                                 |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 68.9 ms: 1.03x slower                                                |
| gc_traversal               | 4.90 ms                                                | 5.06 ms: 1.03x slower                                                |
| pidigits                   | 186 ms                                                 | 193 ms: 1.03x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 222 us: 1.04x slower                                                 |
| generators                 | 28.8 ms                                                | 30.1 ms: 1.05x slower                                                |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                                 |
| json_loads                 | 27.2 us                                                | 28.5 us: 1.05x slower                                                |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                 |
| mako                       | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.58 ms: 1.05x slower                                                |
| fannkuch                   | 394 ms                                                 | 415 ms: 1.05x slower                                                 |
| coverage                   | 82.8 ms                                                | 87.4 ms: 1.05x slower                                                |
| scimark_lu                 | 114 ms                                                 | 122 ms: 1.06x slower                                                 |
| chaos                      | 58.0 ms                                                | 61.9 ms: 1.07x slower                                                |
| pickle_pure_python         | 302 us                                                 | 323 us: 1.07x slower                                                 |
| shortest_path              | 487 ms                                                 | 525 ms: 1.08x slower                                                 |
| logging_simple             | 5.65 us                                                | 6.16 us: 1.09x slower                                                |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.09x slower                                                |
| connected_components       | 447 ms                                                 | 489 ms: 1.09x slower                                                 |
| logging_format             | 6.23 us                                                | 6.83 us: 1.10x slower                                                |
| deltablue                  | 3.19 ms                                                | 3.58 ms: 1.12x slower                                                |
| many_optionals             | 857 us                                                 | 961 us: 1.12x slower                                                 |
| nbody                      | 87.7 ms                                                | 99.9 ms: 1.14x slower                                                |
| coroutines                 | 22.2 ms                                                | 25.9 ms: 1.16x slower                                                |
| subparsers                 | 15.5 ms                                                | 23.5 ms: 1.52x slower                                                |
| logging_silent             | 101 ns                                                 | 474 ns: 4.69x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (5): docutils, sqlite_synth, xml_etree_process, djangocms, json
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250617-3.15.0a0-ccfdf31/bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 99.79% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x
# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.036x faster
- HPT reliability: 98.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                                  |
| html5lib       | 63.4 ms                                                | 62.2 ms: 1.02x faster                                                 |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                                  |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.38x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 625 ms: 1.38x faster                                                  |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 497 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                                  |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                  |
| coroutines                 | 22.2 ms                                                | 25.5 ms: 1.15x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 73.4 ms: 1.07x faster                                                 |
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                                  |
| nbody          | 87.7 ms                                                | 99.4 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                 |
| regex_effbot   | 3.77 ms                                                | 3.29 ms: 1.15x faster                                                 |
| regex_dna      | 220 ms                                                 | 203 ms: 1.08x faster                                                  |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                                  |
| tomli_loads          | 2.12 sec                                               | 2.01 sec: 1.06x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 98.9 ms: 1.02x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 85.3 ms: 1.02x faster                                                 |
| json_loads           | 27.2 us                                                | 28.2 us: 1.04x slower                                                 |
| unpickle_pure_python | 213 us                                                 | 222 us: 1.04x slower                                                  |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| python_startup_no_site | 7.00 ms                                                | 6.91 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 22.0 ms: 1.03x faster                                                 |
| django_template | 31.7 ms                                                | 32.4 ms: 1.02x slower                                                 |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                                  |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.38x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 625 ms: 1.38x faster                                                  |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                  |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.7 us: 1.29x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                  |
| go                         | 141 ms                                                 | 113 ms: 1.24x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 497 ms: 1.15x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.29 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                                  |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                                  |
| richards                   | 47.5 ms                                                | 43.4 ms: 1.10x faster                                                 |
| dulwich_log                | 64.6 ms                                                | 59.3 ms: 1.09x faster                                                 |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                                  |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.08x faster                                                  |
| regex_dna                  | 220 ms                                                 | 203 ms: 1.08x faster                                                  |
| richards_super             | 53.7 ms                                                | 49.7 ms: 1.08x faster                                                 |
| pyflate                    | 470 ms                                                 | 438 ms: 1.07x faster                                                  |
| float                      | 78.7 ms                                                | 73.4 ms: 1.07x faster                                                 |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.06x faster                                                |
| tomli_loads                | 2.12 sec                                               | 2.01 sec: 1.06x faster                                                |
| telco                      | 8.40 ms                                                | 8.06 ms: 1.04x faster                                                 |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.50 sec: 1.04x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                                 |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| genshi_text                | 22.6 ms                                                | 22.0 ms: 1.03x faster                                                 |
| thrift                     | 800 us                                                 | 781 us: 1.02x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 98.9 ms: 1.02x faster                                                 |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                  |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                |
| html5lib                   | 63.4 ms                                                | 62.2 ms: 1.02x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.85 us: 1.02x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 85.3 ms: 1.02x faster                                                 |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.02x faster                                                  |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.02x faster                                                  |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.01x faster                                                 |
| python_startup_no_site     | 7.00 ms                                                | 6.91 ms: 1.01x faster                                                 |
| comprehensions             | 16.5 us                                                | 16.3 us: 1.01x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                  |
| sympy_expand               | 456 ms                                                 | 455 ms: 1.00x faster                                                  |
| nqueens                    | 80.9 ms                                                | 81.7 ms: 1.01x slower                                                 |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 75.7 ms: 1.01x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.18 ms: 1.02x slower                                                 |
| djangocms                  | 22.3 us                                                | 22.8 us: 1.02x slower                                                 |
| django_template            | 31.7 ms                                                | 32.4 ms: 1.02x slower                                                 |
| shortest_path              | 487 ms                                                 | 501 ms: 1.03x slower                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.19 ms: 1.03x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 69.0 ms: 1.03x slower                                                 |
| scimark_fft                | 367 ms                                                 | 379 ms: 1.03x slower                                                  |
| generators                 | 28.8 ms                                                | 29.8 ms: 1.03x slower                                                 |
| json_loads                 | 27.2 us                                                | 28.2 us: 1.04x slower                                                 |
| gc_traversal               | 4.90 ms                                                | 5.09 ms: 1.04x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 222 us: 1.04x slower                                                  |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 120 ms: 1.05x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                 |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                 |
| coverage                   | 82.8 ms                                                | 87.8 ms: 1.06x slower                                                 |
| connected_components       | 447 ms                                                 | 474 ms: 1.06x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                                  |
| chaos                      | 58.0 ms                                                | 61.8 ms: 1.06x slower                                                 |
| fannkuch                   | 394 ms                                                 | 419 ms: 1.06x slower                                                  |
| logging_simple             | 5.65 us                                                | 6.24 us: 1.10x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                 |
| logging_format             | 6.23 us                                                | 6.91 us: 1.11x slower                                                 |
| deltablue                  | 3.19 ms                                                | 3.57 ms: 1.12x slower                                                 |
| many_optionals             | 857 us                                                 | 962 us: 1.12x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.66 sec: 1.12x slower                                                |
| pprint_safe_repr           | 727 ms                                                 | 818 ms: 1.13x slower                                                  |
| nbody                      | 87.7 ms                                                | 99.4 ms: 1.13x slower                                                 |
| coroutines                 | 22.2 ms                                                | 25.5 ms: 1.15x slower                                                 |
| subparsers                 | 15.5 ms                                                | 23.8 ms: 1.54x slower                                                 |
| logging_silent             | 101 ns                                                 | 468 ns: 4.64x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (5): genshi_xml, xml_etree_process, json, asyncio_websockets, docutils
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 98.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x
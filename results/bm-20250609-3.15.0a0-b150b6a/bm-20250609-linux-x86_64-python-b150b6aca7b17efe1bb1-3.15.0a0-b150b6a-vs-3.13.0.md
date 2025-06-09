# Results vs. 3.13.0

- fork: python
- ref: b150b6aca7b17efe1bb1
- machine: linux-x86_64
- commit hash: b150b6a
- commit date: 2025-06-09
- overall geometric mean: 1.038x slower
- HPT reliability: 99.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                                  |
| html5lib       | 63.4 ms                                                | 62.0 ms: 1.02x faster                                                 |
| sphinx         | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                  |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 632 ms: 1.36x faster                                                  |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 486 ms: 1.12x faster                                                  |
| async_generators           | 433 ms                                                 | 406 ms: 1.07x faster                                                  |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                  |
| coroutines                 | 22.2 ms                                                | 25.8 ms: 1.16x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.8 ms: 1.08x faster                                                 |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                  |
| nbody          | 87.7 ms                                                | 102 ms: 1.17x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.07 ms: 1.23x faster                                                 |
| regex_v8       | 26.9 ms                                                | 22.0 ms: 1.22x faster                                                 |
| regex_dna      | 220 ms                                                 | 181 ms: 1.21x faster                                                  |
| regex_compile  | 132 ms                                                 | 127 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 143 ms: 1.08x faster                                                  |
| tomli_loads          | 2.12 sec                                               | 2.03 sec: 1.04x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 99.4 ms: 1.02x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 85.5 ms: 1.02x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 60.0 ms: 1.01x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 220 us: 1.03x slower                                                  |
| json_loads           | 27.2 us                                                | 28.2 us: 1.04x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.07x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.10x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.1 ms: 1.04x faster                                                 |
| python_startup_no_site | 7.00 ms                                                | 6.90 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                 |
| django_template | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                 |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.08x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                  |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                                  |
| deepcopy                   | 354 us                                                 | 255 us: 1.39x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 632 ms: 1.36x faster                                                  |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.1 us: 1.32x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                  |
| go                         | 141 ms                                                 | 112 ms: 1.26x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.07 ms: 1.23x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 22.0 ms: 1.22x faster                                                 |
| regex_dna                  | 220 ms                                                 | 181 ms: 1.21x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.77 us: 1.17x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 486 ms: 1.12x faster                                                  |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                  |
| richards                   | 47.5 ms                                                | 43.6 ms: 1.09x faster                                                 |
| pyflate                    | 470 ms                                                 | 433 ms: 1.08x faster                                                  |
| float                      | 78.7 ms                                                | 72.8 ms: 1.08x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                                |
| richards_super             | 53.7 ms                                                | 49.8 ms: 1.08x faster                                                 |
| xml_etree_parse            | 154 ms                                                 | 143 ms: 1.08x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 59.9 ms: 1.08x faster                                                 |
| async_generators           | 433 ms                                                 | 406 ms: 1.07x faster                                                  |
| telco                      | 8.40 ms                                                | 7.95 ms: 1.06x faster                                                 |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                 |
| tomli_loads                | 2.12 sec                                               | 2.03 sec: 1.04x faster                                                |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                                 |
| python_startup             | 12.7 ms                                                | 12.1 ms: 1.04x faster                                                 |
| spectral_norm              | 113 ms                                                 | 109 ms: 1.04x faster                                                  |
| regex_compile              | 132 ms                                                 | 127 ms: 1.03x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.54 sec: 1.03x faster                                                |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                |
| sphinx                     | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.03x faster                                                  |
| html5lib                   | 63.4 ms                                                | 62.0 ms: 1.02x faster                                                 |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| comprehensions             | 16.5 us                                                | 16.2 us: 1.02x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.85 us: 1.02x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 99.4 ms: 1.02x faster                                                 |
| json                       | 5.32 ms                                                | 5.23 ms: 1.02x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 85.5 ms: 1.02x faster                                                 |
| python_startup_no_site     | 7.00 ms                                                | 6.90 ms: 1.01x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                  |
| sympy_expand               | 456 ms                                                 | 451 ms: 1.01x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 60.0 ms: 1.01x faster                                                 |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                  |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                  |
| scimark_fft                | 367 ms                                                 | 373 ms: 1.02x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 76.1 ms: 1.02x slower                                                 |
| gc_traversal               | 4.90 ms                                                | 5.00 ms: 1.02x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 68.6 ms: 1.03x slower                                                 |
| django_template            | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 220 us: 1.03x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.03x slower                                                  |
| json_loads                 | 27.2 us                                                | 28.2 us: 1.04x slower                                                 |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                  |
| generators                 | 28.8 ms                                                | 29.9 ms: 1.04x slower                                                 |
| fannkuch                   | 394 ms                                                 | 413 ms: 1.05x slower                                                  |
| shortest_path              | 487 ms                                                 | 511 ms: 1.05x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                 |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.07x slower                                                  |
| chaos                      | 58.0 ms                                                | 61.9 ms: 1.07x slower                                                 |
| logging_simple             | 5.65 us                                                | 6.05 us: 1.07x slower                                                 |
| connected_components       | 447 ms                                                 | 484 ms: 1.08x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 797 ms: 1.10x slower                                                  |
| logging_format             | 6.23 us                                                | 6.84 us: 1.10x slower                                                 |
| deltablue                  | 3.19 ms                                                | 3.51 ms: 1.10x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.10x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 1.64 sec: 1.11x slower                                                |
| many_optionals             | 857 us                                                 | 960 us: 1.12x slower                                                  |
| coroutines                 | 22.2 ms                                                | 25.8 ms: 1.16x slower                                                 |
| nbody                      | 87.7 ms                                                | 102 ms: 1.17x slower                                                  |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.53x slower                                                 |
| logging_silent             | 101 ns                                                 | 475 ns: 4.70x slower                                                  |
| coverage                   | 82.8 ms                                                | 426 ms: 5.14x slower                                                  |
| thrift                     | 800 us                                                 | 148 ms: 184.54x slower                                                |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (6): genshi_xml, scimark_sor, docutils, hexiom, nqueens, scimark_sparse_mat_mult
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250609-3.15.0a0-b150b6a/bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.038x slower

# HPT report

- Reliability score: 99.50% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x
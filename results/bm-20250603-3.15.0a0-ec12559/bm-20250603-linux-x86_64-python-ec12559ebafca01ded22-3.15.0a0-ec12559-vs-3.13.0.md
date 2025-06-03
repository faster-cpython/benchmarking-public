# Results vs. 3.13.0

- fork: python
- ref: ec12559ebafca01ded22
- machine: linux-x86_64
- commit hash: ec12559
- commit date: 2025-06-03
- overall geometric mean: 1.039x slower
- HPT reliability: 99.36%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                                  |
| html5lib       | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                 |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                                  |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 634 ms: 1.36x faster                                                  |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                  |
| async_generators           | 433 ms                                                 | 416 ms: 1.04x faster                                                  |
| coroutines                 | 22.2 ms                                                | 26.0 ms: 1.17x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.5 ms: 1.10x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| nbody          | 87.7 ms                                                | 98.1 ms: 1.12x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.22 ms: 1.17x faster                                                 |
| regex_v8       | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                 |
| regex_dna      | 220 ms                                                 | 194 ms: 1.14x faster                                                  |
| regex_compile  | 132 ms                                                 | 127 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.08x faster                                                  |
| tomli_loads          | 2.12 sec                                               | 2.01 sec: 1.05x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 99.4 ms: 1.02x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 85.9 ms: 1.01x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 60.0 ms: 1.01x faster                                                 |
| json_loads           | 27.2 us                                                | 27.9 us: 1.03x slower                                                 |
| unpickle_pure_python | 213 us                                                 | 220 us: 1.03x slower                                                  |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.06x slower                                                  |
| json_dumps           | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| python_startup_no_site | 7.00 ms                                                | 6.95 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.05x faster                                                 |
| genshi_xml      | 50.5 ms                                                | 49.5 ms: 1.02x faster                                                 |
| django_template | 31.7 ms                                                | 32.4 ms: 1.02x slower                                                 |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.06x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                                  |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                  |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 634 ms: 1.36x faster                                                  |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                  |
| go                         | 141 ms                                                 | 112 ms: 1.26x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.22 ms: 1.17x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                  |
| regex_dna                  | 220 ms                                                 | 194 ms: 1.14x faster                                                  |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                  |
| float                      | 78.7 ms                                                | 71.5 ms: 1.10x faster                                                 |
| richards                   | 47.5 ms                                                | 43.4 ms: 1.09x faster                                                 |
| pyflate                    | 470 ms                                                 | 432 ms: 1.09x faster                                                  |
| richards_super             | 53.7 ms                                                | 49.6 ms: 1.08x faster                                                 |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.08x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 59.7 ms: 1.08x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.05x faster                                                 |
| telco                      | 8.40 ms                                                | 7.96 ms: 1.05x faster                                                 |
| tomli_loads                | 2.12 sec                                               | 2.01 sec: 1.05x faster                                                |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                                 |
| async_generators           | 433 ms                                                 | 416 ms: 1.04x faster                                                  |
| spectral_norm              | 113 ms                                                 | 109 ms: 1.04x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.53 sec: 1.03x faster                                                |
| regex_compile              | 132 ms                                                 | 127 ms: 1.03x faster                                                  |
| json                       | 5.32 ms                                                | 5.15 ms: 1.03x faster                                                 |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| comprehensions             | 16.5 us                                                | 16.0 us: 1.03x faster                                                 |
| html5lib                   | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                 |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.03x faster                                                |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 49.5 ms: 1.02x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 99.4 ms: 1.02x faster                                                 |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                  |
| pathlib                    | 17.4 ms                                                | 17.2 ms: 1.01x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 85.9 ms: 1.01x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                  |
| sympy_expand               | 456 ms                                                 | 452 ms: 1.01x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.87 us: 1.01x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 60.0 ms: 1.01x faster                                                 |
| python_startup_no_site     | 7.00 ms                                                | 6.95 ms: 1.01x faster                                                 |
| hexiom                     | 6.08 ms                                                | 6.04 ms: 1.01x faster                                                 |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| nqueens                    | 80.9 ms                                                | 81.6 ms: 1.01x slower                                                 |
| crypto_pyaes               | 74.7 ms                                                | 75.5 ms: 1.01x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 67.9 ms: 1.02x slower                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.12 ms: 1.02x slower                                                 |
| gc_traversal               | 4.90 ms                                                | 5.00 ms: 1.02x slower                                                 |
| django_template            | 31.7 ms                                                | 32.4 ms: 1.02x slower                                                 |
| json_loads                 | 27.2 us                                                | 27.9 us: 1.03x slower                                                 |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 220 us: 1.03x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.04x slower                                                  |
| scimark_fft                | 367 ms                                                 | 380 ms: 1.04x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.04x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.57 ms: 1.05x slower                                                 |
| chaos                      | 58.0 ms                                                | 61.0 ms: 1.05x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.06x slower                                                  |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                 |
| fannkuch                   | 394 ms                                                 | 417 ms: 1.06x slower                                                  |
| generators                 | 28.8 ms                                                | 30.5 ms: 1.06x slower                                                 |
| connected_components       | 447 ms                                                 | 479 ms: 1.07x slower                                                  |
| shortest_path              | 487 ms                                                 | 523 ms: 1.07x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                 |
| logging_simple             | 5.65 us                                                | 6.17 us: 1.09x slower                                                 |
| logging_format             | 6.23 us                                                | 6.81 us: 1.09x slower                                                 |
| deltablue                  | 3.19 ms                                                | 3.52 ms: 1.10x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 812 ms: 1.12x slower                                                  |
| many_optionals             | 857 us                                                 | 958 us: 1.12x slower                                                  |
| nbody                      | 87.7 ms                                                | 98.1 ms: 1.12x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 1.66 sec: 1.12x slower                                                |
| coroutines                 | 22.2 ms                                                | 26.0 ms: 1.17x slower                                                 |
| subparsers                 | 15.5 ms                                                | 23.5 ms: 1.52x slower                                                 |
| logging_silent             | 101 ns                                                 | 475 ns: 4.71x slower                                                  |
| coverage                   | 82.8 ms                                                | 426 ms: 5.14x slower                                                  |
| thrift                     | 800 us                                                 | 148 ms: 184.59x slower                                                |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, docutils
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250603-3.15.0a0-ec12559/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.039x slower

# HPT report

- Reliability score: 99.36% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x
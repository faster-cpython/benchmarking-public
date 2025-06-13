# Results vs. 3.13.0

- fork: python
- ref: afc5ab6cce9d7095b99c
- machine: linux-x86_64
- commit hash: afc5ab6
- commit date: 2025-06-13
- overall geometric mean: 1.041x slower
- HPT reliability: 99.16%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                                  |
| html5lib       | 63.4 ms                                                | 61.8 ms: 1.03x faster                                                 |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                  |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 634 ms: 1.36x faster                                                  |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 492 ms: 1.10x faster                                                  |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                  |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                  |
| coroutines                 | 22.2 ms                                                | 26.1 ms: 1.18x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 73.6 ms: 1.07x faster                                                 |
| pidigits       | 186 ms                                                 | 192 ms: 1.03x slower                                                  |
| nbody          | 87.7 ms                                                | 102 ms: 1.16x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.22 ms: 1.17x faster                                                 |
| regex_v8       | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                 |
| regex_dna      | 220 ms                                                 | 194 ms: 1.13x faster                                                  |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 143 ms: 1.08x faster                                                  |
| tomli_loads          | 2.12 sec                                               | 2.03 sec: 1.04x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 99.1 ms: 1.02x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 85.4 ms: 1.02x faster                                                 |
| json_loads           | 27.2 us                                                | 27.8 us: 1.02x slower                                                 |
| unpickle_pure_python | 213 us                                                 | 222 us: 1.04x slower                                                  |
| pickle_pure_python   | 302 us                                                 | 324 us: 1.07x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| python_startup_no_site | 7.00 ms                                                | 6.92 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.6 ms: 1.05x faster                                                 |
| genshi_xml      | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                 |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                 |
| mako            | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.08x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                  |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                  |
| deepcopy                   | 354 us                                                 | 256 us: 1.39x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 634 ms: 1.36x faster                                                  |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.4 us: 1.31x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                  |
| go                         | 141 ms                                                 | 112 ms: 1.26x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.76 us: 1.17x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.22 ms: 1.17x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                  |
| regex_dna                  | 220 ms                                                 | 194 ms: 1.13x faster                                                  |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 492 ms: 1.10x faster                                                  |
| richards                   | 47.5 ms                                                | 43.4 ms: 1.10x faster                                                 |
| pyflate                    | 470 ms                                                 | 432 ms: 1.09x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 59.5 ms: 1.09x faster                                                 |
| richards_super             | 53.7 ms                                                | 49.8 ms: 1.08x faster                                                 |
| xml_etree_parse            | 154 ms                                                 | 143 ms: 1.08x faster                                                  |
| float                      | 78.7 ms                                                | 73.6 ms: 1.07x faster                                                 |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.06x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.6 ms: 1.05x faster                                                 |
| sympy_integrate            | 19.8 ms                                                | 18.9 ms: 1.05x faster                                                 |
| tomli_loads                | 2.12 sec                                               | 2.03 sec: 1.04x faster                                                |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                                  |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| telco                      | 8.40 ms                                                | 8.08 ms: 1.04x faster                                                 |
| json                       | 5.32 ms                                                | 5.13 ms: 1.04x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.54 sec: 1.03x faster                                                |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| sympy_str                  | 273 ms                                                 | 265 ms: 1.03x faster                                                  |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| comprehensions             | 16.5 us                                                | 16.1 us: 1.03x faster                                                 |
| spectral_norm              | 113 ms                                                 | 110 ms: 1.03x faster                                                  |
| html5lib                   | 63.4 ms                                                | 61.8 ms: 1.03x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 99.1 ms: 1.02x faster                                                 |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                                 |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                |
| xml_etree_generate         | 86.8 ms                                                | 85.4 ms: 1.02x faster                                                 |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                  |
| sympy_expand               | 456 ms                                                 | 450 ms: 1.01x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                 |
| python_startup_no_site     | 7.00 ms                                                | 6.92 ms: 1.01x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.88 us: 1.01x faster                                                 |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                  |
| nqueens                    | 80.9 ms                                                | 81.5 ms: 1.01x slower                                                 |
| gc_traversal               | 4.90 ms                                                | 4.95 ms: 1.01x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.15 ms: 1.01x slower                                                 |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                 |
| crypto_pyaes               | 74.7 ms                                                | 76.3 ms: 1.02x slower                                                 |
| json_loads                 | 27.2 us                                                | 27.8 us: 1.02x slower                                                 |
| generators                 | 28.8 ms                                                | 29.5 ms: 1.02x slower                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.18 ms: 1.03x slower                                                 |
| pidigits                   | 186 ms                                                 | 192 ms: 1.03x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 69.6 ms: 1.04x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 222 us: 1.04x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                  |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 120 ms: 1.04x slower                                                  |
| scimark_fft                | 367 ms                                                 | 386 ms: 1.05x slower                                                  |
| chaos                      | 58.0 ms                                                | 61.5 ms: 1.06x slower                                                 |
| create_gc_cycles           | 2.45 ms                                                | 2.60 ms: 1.06x slower                                                 |
| fannkuch                   | 394 ms                                                 | 418 ms: 1.06x slower                                                  |
| shortest_path              | 487 ms                                                 | 517 ms: 1.06x slower                                                  |
| connected_components       | 447 ms                                                 | 476 ms: 1.06x slower                                                  |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 324 us: 1.07x slower                                                  |
| logging_simple             | 5.65 us                                                | 6.07 us: 1.07x slower                                                 |
| logging_format             | 6.23 us                                                | 6.72 us: 1.08x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                 |
| deltablue                  | 3.19 ms                                                | 3.54 ms: 1.11x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 805 ms: 1.11x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.65 sec: 1.11x slower                                                |
| many_optionals             | 857 us                                                 | 960 us: 1.12x slower                                                  |
| nbody                      | 87.7 ms                                                | 102 ms: 1.16x slower                                                  |
| coroutines                 | 22.2 ms                                                | 26.1 ms: 1.18x slower                                                 |
| subparsers                 | 15.5 ms                                                | 23.5 ms: 1.52x slower                                                 |
| logging_silent             | 101 ns                                                 | 476 ns: 4.72x slower                                                  |
| coverage                   | 82.8 ms                                                | 423 ms: 5.10x slower                                                  |
| thrift                     | 800 us                                                 | 148 ms: 184.40x slower                                                |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                          |

Benchmark hidden because not significant (2): xml_etree_process, docutils
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250613-3.15.0a0-afc5ab6/bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.041x slower

# HPT report

- Reliability score: 99.16% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x
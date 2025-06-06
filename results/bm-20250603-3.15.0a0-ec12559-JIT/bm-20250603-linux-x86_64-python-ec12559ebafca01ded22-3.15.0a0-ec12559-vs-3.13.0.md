# Results vs. 3.13.0

- fork: python
- ref: ec12559ebafca01ded22
- machine: linux-x86_64
- commit hash: ec12559
- commit date: 2025-06-03
- overall geometric mean: 1.353x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                  |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                |
| html5lib       | 63.4 ms                                                | 61.4 ms: 1.03x faster                                                 |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                  |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 638 ms: 1.35x faster                                                  |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 506 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 497 ms: 1.09x faster                                                  |
| async_generators           | 433 ms                                                 | 430 ms: 1.01x faster                                                  |
| coroutines                 | 22.2 ms                                                | 25.5 ms: 1.15x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 64.5 ms: 1.22x faster                                                 |
| pidigits       | 186 ms                                                 | 191 ms: 1.02x slower                                                  |
| nbody          | 87.7 ms                                                | 91.8 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.1 ms: 1.22x faster                                                 |
| regex_effbot   | 3.77 ms                                                | 3.24 ms: 1.16x faster                                                 |
| regex_dna      | 220 ms                                                 | 197 ms: 1.11x faster                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.89 sec: 1.12x faster                                                |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 55.8 ms: 1.08x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 80.1 ms: 1.08x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 200 us: 1.07x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 97.4 ms: 1.04x faster                                                 |
| json_loads           | 27.2 us                                                | 27.8 us: 1.03x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| python_startup_no_site | 7.00 ms                                                | 6.98 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                 |
| genshi_xml      | 50.5 ms                                                | 49.2 ms: 1.03x faster                                                 |
| mako            | 10.7 ms                                                | 10.8 ms: 1.01x slower                                                 |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pprint_pformat             | 1.48 sec                                               | 1.45 us: 1018048.74x faster                                           |
| pprint_safe_repr           | 727 ms                                                 | 829 ns: 876532.23x faster                                             |
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.06x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                  |
| richards                   | 47.5 ms                                                | 33.4 ms: 1.42x faster                                                 |
| deepcopy                   | 354 us                                                 | 253 us: 1.40x faster                                                  |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                                  |
| richards_super             | 53.7 ms                                                | 39.4 ms: 1.36x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 638 ms: 1.35x faster                                                  |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.6 us: 1.30x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.65 us: 1.23x faster                                                 |
| float                      | 78.7 ms                                                | 64.5 ms: 1.22x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 22.1 ms: 1.22x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.24 ms: 1.16x faster                                                 |
| go                         | 141 ms                                                 | 123 ms: 1.15x faster                                                  |
| pyflate                    | 470 ms                                                 | 413 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 506 ms: 1.13x faster                                                  |
| spectral_norm              | 113 ms                                                 | 100 ms: 1.13x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.89 sec: 1.12x faster                                                |
| regex_dna                  | 220 ms                                                 | 197 ms: 1.11x faster                                                  |
| scimark_fft                | 367 ms                                                 | 332 ms: 1.10x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                  |
| pylint                     | 312 ms                                                 | 283 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 497 ms: 1.09x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 55.8 ms: 1.08x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 80.1 ms: 1.08x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.37 sec: 1.07x faster                                                |
| telco                      | 8.40 ms                                                | 7.88 ms: 1.07x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 200 us: 1.07x faster                                                  |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                 |
| dulwich_log                | 64.6 ms                                                | 60.9 ms: 1.06x faster                                                 |
| deltablue                  | 3.19 ms                                                | 3.06 ms: 1.05x faster                                                 |
| json                       | 5.32 ms                                                | 5.10 ms: 1.04x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 97.4 ms: 1.04x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                 |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                |
| html5lib                   | 63.4 ms                                                | 61.4 ms: 1.03x faster                                                 |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 49.2 ms: 1.03x faster                                                 |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                                 |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                  |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.96 ms: 1.01x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                  |
| async_generators           | 433 ms                                                 | 430 ms: 1.01x faster                                                  |
| sympy_str                  | 273 ms                                                 | 271 ms: 1.01x faster                                                  |
| python_startup_no_site     | 7.00 ms                                                | 6.98 ms: 1.00x faster                                                 |
| gc_traversal               | 4.90 ms                                                | 4.91 ms: 1.00x slower                                                 |
| mako                       | 10.7 ms                                                | 10.8 ms: 1.01x slower                                                 |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                                  |
| shortest_path              | 487 ms                                                 | 494 ms: 1.01x slower                                                  |
| connected_components       | 447 ms                                                 | 453 ms: 1.01x slower                                                  |
| sympy_expand               | 456 ms                                                 | 463 ms: 1.02x slower                                                  |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                |
| crypto_pyaes               | 74.7 ms                                                | 76.3 ms: 1.02x slower                                                 |
| pidigits                   | 186 ms                                                 | 191 ms: 1.02x slower                                                  |
| json_loads                 | 27.2 us                                                | 27.8 us: 1.03x slower                                                 |
| nqueens                    | 80.9 ms                                                | 83.2 ms: 1.03x slower                                                 |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                 |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                  |
| generators                 | 28.8 ms                                                | 30.0 ms: 1.04x slower                                                 |
| nbody                      | 87.7 ms                                                | 91.8 ms: 1.05x slower                                                 |
| create_gc_cycles           | 2.45 ms                                                | 2.57 ms: 1.05x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 170 us: 1.06x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.48 ms: 1.07x slower                                                 |
| chaos                      | 58.0 ms                                                | 61.9 ms: 1.07x slower                                                 |
| fannkuch                   | 394 ms                                                 | 421 ms: 1.07x slower                                                  |
| logging_simple             | 5.65 us                                                | 6.09 us: 1.08x slower                                                 |
| logging_format             | 6.23 us                                                | 6.74 us: 1.08x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                 |
| many_optionals             | 857 us                                                 | 973 us: 1.14x slower                                                  |
| coroutines                 | 22.2 ms                                                | 25.5 ms: 1.15x slower                                                 |
| subparsers                 | 15.5 ms                                                | 23.5 ms: 1.52x slower                                                 |
| logging_silent             | 101 ns                                                 | 471 ns: 4.66x slower                                                  |
| coverage                   | 82.8 ms                                                | 422 ms: 5.09x slower                                                  |
| thrift                     | 800 us                                                 | 148 ms: 184.77x slower                                                |
| Geometric mean             | (ref)                                                  | 1.32x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, scimark_monte_carlo
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250603-3.15.0a0-ec12559-JIT/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.353x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x
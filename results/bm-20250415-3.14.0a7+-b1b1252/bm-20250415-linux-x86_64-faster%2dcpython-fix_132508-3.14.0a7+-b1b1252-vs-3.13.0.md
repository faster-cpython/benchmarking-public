# Results vs. 3.13.0

- fork: faster-cpython
- ref: fix_132508
- machine: linux-x86_64
- commit hash: b1b1252
- commit date: 2025-04-15
- overall geometric mean: 1.058x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 250 ms: 1.06x faster                                                   |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.00x slower                                                 |
| html5lib       | 63.4 ms                                                | 59.6 ms: 1.06x faster                                                  |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 307 ms: 1.42x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 609 ms: 1.38x faster                                                   |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 246 ms: 1.30x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 479 ms: 1.20x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                   |
| async_generators           | 433 ms                                                 | 393 ms: 1.10x faster                                                   |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 68.8 ms: 1.14x faster                                                  |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                   |
| nbody          | 87.7 ms                                                | 96.6 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.25 ms: 1.16x faster                                                  |
| regex_v8       | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                  |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                   |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.95 sec: 1.09x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 58.4 ms: 1.04x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 84.5 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 98.7 ms: 1.03x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 316 us: 1.05x slower                                                   |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.3 ms: 1.05x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 8.28 ms: 1.18x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.6 ms: 1.10x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 49.3 ms: 1.02x faster                                                  |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                  |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.20 sec: 2.11x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 307 ms: 1.42x faster                                                   |
| deepcopy                   | 354 us                                                 | 251 us: 1.41x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 609 ms: 1.38x faster                                                   |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 28.4 us: 1.35x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 246 ms: 1.30x faster                                                   |
| go                         | 141 ms                                                 | 110 ms: 1.28x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.22x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 479 ms: 1.20x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.25 ms: 1.16x faster                                                  |
| float                      | 78.7 ms                                                | 68.8 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                  |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                   |
| richards                   | 47.5 ms                                                | 42.9 ms: 1.11x faster                                                  |
| async_generators           | 433 ms                                                 | 393 ms: 1.10x faster                                                   |
| telco                      | 8.40 ms                                                | 7.64 ms: 1.10x faster                                                  |
| genshi_text                | 22.6 ms                                                | 20.6 ms: 1.10x faster                                                  |
| richards_super             | 53.7 ms                                                | 49.1 ms: 1.10x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.95 sec: 1.09x faster                                                 |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.09x faster                                                   |
| pyflate                    | 470 ms                                                 | 434 ms: 1.08x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 59.8 ms: 1.08x faster                                                  |
| html5lib                   | 63.4 ms                                                | 59.6 ms: 1.06x faster                                                  |
| logging_silent             | 101 ns                                                 | 94.9 ns: 1.06x faster                                                  |
| 2to3                       | 266 ms                                                 | 250 ms: 1.06x faster                                                   |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                   |
| regex_dna                  | 220 ms                                                 | 209 ms: 1.05x faster                                                   |
| gc_traversal               | 4.90 ms                                                | 4.65 ms: 1.05x faster                                                  |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.05x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.05x faster                                                 |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.85 ms: 1.04x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 58.4 ms: 1.04x faster                                                  |
| pprint_safe_repr           | 727 ms                                                 | 703 ms: 1.03x faster                                                   |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| scimark_fft                | 367 ms                                                 | 356 ms: 1.03x faster                                                   |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 84.5 ms: 1.03x faster                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.44 sec: 1.03x faster                                                 |
| chaos                      | 58.0 ms                                                | 56.5 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 98.7 ms: 1.03x faster                                                  |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.03x faster                                                   |
| logging_simple             | 5.65 us                                                | 5.52 us: 1.02x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 49.3 ms: 1.02x faster                                                  |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.61 sec: 1.02x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                   |
| crypto_pyaes               | 74.7 ms                                                | 73.5 ms: 1.02x faster                                                  |
| logging_format             | 6.23 us                                                | 6.13 us: 1.02x faster                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 65.8 ms: 1.01x faster                                                  |
| sympy_expand               | 456 ms                                                 | 451 ms: 1.01x faster                                                   |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                   |
| raytrace                   | 262 ms                                                 | 262 ms: 1.00x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.00x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.13 ms: 1.01x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                  |
| shortest_path              | 487 ms                                                 | 493 ms: 1.01x slower                                                   |
| nqueens                    | 80.9 ms                                                | 81.9 ms: 1.01x slower                                                  |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                  |
| generators                 | 28.8 ms                                                | 29.5 ms: 1.03x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.03x slower                                                   |
| typing_runtime_protocols   | 160 us                                                 | 165 us: 1.03x slower                                                   |
| deltablue                  | 3.19 ms                                                | 3.32 ms: 1.04x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 316 us: 1.05x slower                                                   |
| python_startup             | 12.7 ms                                                | 13.3 ms: 1.05x slower                                                  |
| coverage                   | 82.8 ms                                                | 87.4 ms: 1.05x slower                                                  |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                  |
| fannkuch                   | 394 ms                                                 | 419 ms: 1.06x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 886 us: 1.08x slower                                                   |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                                  |
| many_optionals             | 857 us                                                 | 934 us: 1.09x slower                                                   |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                  |
| nbody                      | 87.7 ms                                                | 96.6 ms: 1.10x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.15x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 8.28 ms: 1.18x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.33x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.46x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (6): json, connected_components, sqlalchemy_imperative, sqlalchemy_declarative, asyncio_websockets, comprehensions
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250415-3.14.0a7+-b1b1252/bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.058x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x
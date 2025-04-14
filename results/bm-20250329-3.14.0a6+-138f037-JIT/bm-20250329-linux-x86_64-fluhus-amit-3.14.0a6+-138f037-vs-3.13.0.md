# Results vs. 3.13.0

- fork: fluhus
- ref: amit
- machine: linux-x86_64
- commit hash: 138f037
- commit date: 2025-03-29
- overall geometric mean: 1.056x faster
- HPT reliability: 99.62%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 262 ms: 1.02x faster                                   |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                 |
| html5lib       | 63.4 ms                                                | 61.5 ms: 1.03x faster                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                   |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                   |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                   |
| async_tree_io              | 838 ms                                                 | 613 ms: 1.37x faster                                   |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                   |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                   |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                   |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.04x slower                                  |
| Geometric mean             | (ref)                                                  | 1.22x faster                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 78.7 ms                                                | 63.0 ms: 1.25x faster                                  |
| nbody          | 87.7 ms                                                | 84.9 ms: 1.03x faster                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.1 ms: 1.16x faster                                  |
| regex_effbot   | 3.77 ms                                                | 3.47 ms: 1.09x faster                                  |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                   |
| regex_dna      | 220 ms                                                 | 223 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.85 sec: 1.14x faster                                 |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                   |
| xml_etree_process    | 60.5 ms                                                | 55.7 ms: 1.09x faster                                  |
| xml_etree_generate   | 86.8 ms                                                | 80.2 ms: 1.08x faster                                  |
| xml_etree_iterparse  | 101 ms                                                 | 97.7 ms: 1.04x faster                                  |
| unpickle_pure_python | 213 us                                                 | 211 us: 1.01x faster                                   |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                   |
| json_loads           | 27.2 us                                                | 30.0 us: 1.11x slower                                  |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.14x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                  |
| python_startup_no_site | 7.00 ms                                                | 8.20 ms: 1.17x slower                                  |
| Geometric mean         | (ref)                                                  | 1.10x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                  |
| genshi_xml      | 50.5 ms                                                | 49.9 ms: 1.01x faster                                  |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                  |
| mako            | 10.7 ms                                                | 11.1 ms: 1.04x slower                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.05x faster                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                   |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                   |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                   |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                   |
| async_tree_io              | 838 ms                                                 | 613 ms: 1.37x faster                                   |
| richards                   | 47.5 ms                                                | 35.2 ms: 1.35x faster                                  |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                   |
| deepcopy_memo              | 38.4 us                                                | 29.0 us: 1.32x faster                                  |
| richards_super             | 53.7 ms                                                | 40.7 ms: 1.32x faster                                  |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                   |
| float                      | 78.7 ms                                                | 63.0 ms: 1.25x faster                                  |
| spectral_norm              | 113 ms                                                 | 92.9 ms: 1.22x faster                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.20x faster                                  |
| scimark_fft                | 367 ms                                                 | 309 ms: 1.19x faster                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                   |
| regex_v8                   | 26.9 ms                                                | 23.1 ms: 1.16x faster                                  |
| tomli_loads                | 2.12 sec                                               | 1.85 sec: 1.14x faster                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                   |
| pylint                     | 312 ms                                                 | 281 ms: 1.11x faster                                   |
| go                         | 141 ms                                                 | 127 ms: 1.11x faster                                   |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.63 ms: 1.09x faster                                  |
| regex_effbot               | 3.77 ms                                                | 3.47 ms: 1.09x faster                                  |
| xml_etree_process          | 60.5 ms                                                | 55.7 ms: 1.09x faster                                  |
| telco                      | 8.40 ms                                                | 7.76 ms: 1.08x faster                                  |
| xml_etree_generate         | 86.8 ms                                                | 80.2 ms: 1.08x faster                                  |
| sqlite_synth               | 2.90 us                                                | 2.71 us: 1.07x faster                                  |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                  |
| dulwich_log                | 64.6 ms                                                | 60.4 ms: 1.07x faster                                  |
| deltablue                  | 3.19 ms                                                | 3.01 ms: 1.06x faster                                  |
| pyflate                    | 470 ms                                                 | 443 ms: 1.06x faster                                   |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                  |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                   |
| xml_etree_iterparse        | 101 ms                                                 | 97.7 ms: 1.04x faster                                  |
| logging_silent             | 101 ns                                                 | 97.6 ns: 1.04x faster                                  |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                   |
| nbody                      | 87.7 ms                                                | 84.9 ms: 1.03x faster                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.55 sec: 1.03x faster                                 |
| html5lib                   | 63.4 ms                                                | 61.5 ms: 1.03x faster                                  |
| gc_traversal               | 4.90 ms                                                | 4.76 ms: 1.03x faster                                  |
| logging_simple             | 5.65 us                                                | 5.50 us: 1.03x faster                                  |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                   |
| k_core                     | 2.37 sec                                               | 2.32 sec: 1.02x faster                                 |
| 2to3                       | 266 ms                                                 | 262 ms: 1.02x faster                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                   |
| pycparser                  | 1.20 sec                                               | 1.19 sec: 1.01x faster                                 |
| genshi_xml                 | 50.5 ms                                                | 49.9 ms: 1.01x faster                                  |
| unpickle_pure_python       | 213 us                                                 | 211 us: 1.01x faster                                   |
| generators                 | 28.8 ms                                                | 28.4 ms: 1.01x faster                                  |
| logging_format             | 6.23 us                                                | 6.18 us: 1.01x faster                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.01x faster                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.0 ms: 1.01x slower                                  |
| sympy_integrate            | 19.8 ms                                                | 20.0 ms: 1.01x slower                                  |
| sympy_str                  | 273 ms                                                 | 275 ms: 1.01x slower                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                  |
| chaos                      | 58.0 ms                                                | 58.8 ms: 1.01x slower                                  |
| regex_dna                  | 220 ms                                                 | 223 ms: 1.01x slower                                   |
| crypto_pyaes               | 74.7 ms                                                | 75.7 ms: 1.01x slower                                  |
| sympy_sum                  | 150 ms                                                 | 153 ms: 1.01x slower                                   |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                   |
| connected_components       | 447 ms                                                 | 454 ms: 1.02x slower                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 68.0 ms: 1.02x slower                                  |
| coverage                   | 82.8 ms                                                | 84.6 ms: 1.02x slower                                  |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                  |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                   |
| nqueens                    | 80.9 ms                                                | 83.2 ms: 1.03x slower                                  |
| shortest_path              | 487 ms                                                 | 501 ms: 1.03x slower                                   |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                  |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                  |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.04x slower                                  |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.04x slower                                   |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                 |
| sympy_expand               | 456 ms                                                 | 476 ms: 1.04x slower                                   |
| pprint_safe_repr           | 727 ms                                                 | 764 ms: 1.05x slower                                   |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                   |
| fannkuch                   | 394 ms                                                 | 419 ms: 1.06x slower                                   |
| pprint_pformat             | 1.48 sec                                               | 1.57 sec: 1.07x slower                                 |
| bench_thread_pool          | 818 us                                                 | 882 us: 1.08x slower                                   |
| json_loads                 | 27.2 us                                                | 30.0 us: 1.11x slower                                  |
| hexiom                     | 6.08 ms                                                | 6.78 ms: 1.12x slower                                  |
| many_optionals             | 857 us                                                 | 970 us: 1.13x slower                                   |
| comprehensions             | 16.5 us                                                | 18.8 us: 1.14x slower                                  |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.14x slower                                  |
| python_startup_no_site     | 7.00 ms                                                | 8.20 ms: 1.17x slower                                  |
| subparsers                 | 15.5 ms                                                | 21.2 ms: 1.37x slower                                  |
| bench_mp_pool              | 24.0 ms                                                | 83.0 ms: 3.46x slower                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (4): sphinx, asyncio_websockets, json, meteor_contest
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250329-3.14.0a6+-138f037-JIT/bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.056x faster

# HPT report

- Reliability score: 99.62% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x
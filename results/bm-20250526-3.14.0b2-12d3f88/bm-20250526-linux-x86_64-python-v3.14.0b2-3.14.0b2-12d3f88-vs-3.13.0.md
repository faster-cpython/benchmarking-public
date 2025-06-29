# Results vs. 3.13.0

- fork: python
- ref: v3.14.0b2
- machine: linux-x86_64
- commit hash: 12d3f88
- commit date: 2025-05-26
- overall geometric mean: 1.040x faster
- HPT reliability: 99.45%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                       |
| html5lib       | 63.4 ms                                                | 61.6 ms: 1.03x faster                                      |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                       |
| async_tree_io              | 838 ms                                                 | 595 ms: 1.41x faster                                       |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                       |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                       |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                       |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 491 ms: 1.17x faster                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                       |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                       |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                      |
| Geometric mean             | (ref)                                                  | 1.21x faster                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.7 ms: 1.11x faster                                      |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                       |
| nbody          | 87.7 ms                                                | 101 ms: 1.15x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 2.93 ms: 1.28x faster                                      |
| regex_v8       | 26.9 ms                                                | 22.5 ms: 1.20x faster                                      |
| regex_dna      | 220 ms                                                 | 194 ms: 1.13x faster                                       |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                       |
| Geometric mean | (ref)                                                  | 1.16x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                       |
| tomli_loads          | 2.12 sec                                               | 2.02 sec: 1.05x faster                                     |
| xml_etree_iterparse  | 101 ms                                                 | 98.9 ms: 1.02x faster                                      |
| xml_etree_generate   | 86.8 ms                                                | 85.2 ms: 1.02x faster                                      |
| xml_etree_process    | 60.5 ms                                                | 61.0 ms: 1.01x slower                                      |
| unpickle_pure_python | 213 us                                                 | 223 us: 1.05x slower                                       |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.07x slower                                       |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.11x slower                                      |
| json_loads           | 27.2 us                                                | 30.2 us: 1.11x slower                                      |
| Geometric mean       | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.91 ms: 1.01x faster                                      |
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                      |
| Geometric mean         | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.6 ms: 1.05x faster                                      |
| genshi_xml      | 50.5 ms                                                | 49.9 ms: 1.01x faster                                      |
| django_template | 31.7 ms                                                | 32.5 ms: 1.03x slower                                      |
| mako            | 10.7 ms                                                | 11.4 ms: 1.06x slower                                      |
| Geometric mean  | (ref)                                                  | 1.01x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.04x faster                                     |
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                       |
| async_tree_io              | 838 ms                                                 | 595 ms: 1.41x faster                                       |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                       |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                       |
| deepcopy                   | 354 us                                                 | 255 us: 1.39x faster                                       |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                       |
| deepcopy_memo              | 38.4 us                                                | 29.6 us: 1.30x faster                                      |
| regex_effbot               | 3.77 ms                                                | 2.93 ms: 1.28x faster                                      |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                       |
| go                         | 141 ms                                                 | 115 ms: 1.23x faster                                       |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.20x faster                                      |
| regex_v8                   | 26.9 ms                                                | 22.5 ms: 1.20x faster                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 491 ms: 1.17x faster                                       |
| regex_dna                  | 220 ms                                                 | 194 ms: 1.13x faster                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                       |
| float                      | 78.7 ms                                                | 70.7 ms: 1.11x faster                                      |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                       |
| richards                   | 47.5 ms                                                | 43.1 ms: 1.10x faster                                      |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                       |
| richards_super             | 53.7 ms                                                | 49.4 ms: 1.09x faster                                      |
| dulwich_log                | 64.6 ms                                                | 59.6 ms: 1.08x faster                                      |
| telco                      | 8.40 ms                                                | 7.92 ms: 1.06x faster                                      |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                     |
| spectral_norm              | 113 ms                                                 | 107 ms: 1.06x faster                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.47 sec: 1.05x faster                                     |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                       |
| tomli_loads                | 2.12 sec                                               | 2.02 sec: 1.05x faster                                     |
| genshi_text                | 22.6 ms                                                | 21.6 ms: 1.05x faster                                      |
| pyflate                    | 470 ms                                                 | 451 ms: 1.04x faster                                       |
| sympy_integrate            | 19.8 ms                                                | 19.1 ms: 1.04x faster                                      |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                       |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                       |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                     |
| html5lib                   | 63.4 ms                                                | 61.6 ms: 1.03x faster                                      |
| xml_etree_iterparse        | 101 ms                                                 | 98.9 ms: 1.02x faster                                      |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                     |
| xml_etree_generate         | 86.8 ms                                                | 85.2 ms: 1.02x faster                                      |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.02x faster                                      |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.01x faster                                       |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.01x faster                                       |
| python_startup_no_site     | 7.00 ms                                                | 6.91 ms: 1.01x faster                                      |
| genshi_xml                 | 50.5 ms                                                | 49.9 ms: 1.01x faster                                      |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                       |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                       |
| sqlite_synth               | 2.90 us                                                | 2.88 us: 1.01x faster                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.01 ms: 1.00x faster                                      |
| crypto_pyaes               | 74.7 ms                                                | 75.0 ms: 1.00x slower                                      |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                       |
| scimark_fft                | 367 ms                                                 | 369 ms: 1.01x slower                                       |
| xml_etree_process          | 60.5 ms                                                | 61.0 ms: 1.01x slower                                      |
| json                       | 5.32 ms                                                | 5.39 ms: 1.01x slower                                      |
| nqueens                    | 80.9 ms                                                | 81.8 ms: 1.01x slower                                      |
| gc_traversal               | 4.90 ms                                                | 4.96 ms: 1.01x slower                                      |
| hexiom                     | 6.08 ms                                                | 6.16 ms: 1.01x slower                                      |
| sympy_expand               | 456 ms                                                 | 463 ms: 1.01x slower                                       |
| sqlalchemy_declarative     | 133 ms                                                 | 135 ms: 1.01x slower                                       |
| shortest_path              | 487 ms                                                 | 494 ms: 1.02x slower                                       |
| pprint_safe_repr           | 727 ms                                                 | 738 ms: 1.02x slower                                       |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.02x slower                                     |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                       |
| django_template            | 31.7 ms                                                | 32.5 ms: 1.03x slower                                      |
| scimark_monte_carlo        | 66.8 ms                                                | 68.6 ms: 1.03x slower                                      |
| connected_components       | 447 ms                                                 | 460 ms: 1.03x slower                                       |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                      |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.5 ms: 1.03x slower                                      |
| chaos                      | 58.0 ms                                                | 60.1 ms: 1.04x slower                                      |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                      |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                       |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                       |
| unpickle_pure_python       | 213 us                                                 | 223 us: 1.05x slower                                       |
| create_gc_cycles           | 2.45 ms                                                | 2.58 ms: 1.05x slower                                      |
| fannkuch                   | 394 ms                                                 | 417 ms: 1.06x slower                                       |
| coverage                   | 82.8 ms                                                | 88.0 ms: 1.06x slower                                      |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.06x slower                                      |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.07x slower                                       |
| logging_simple             | 5.65 us                                                | 6.09 us: 1.08x slower                                      |
| deltablue                  | 3.19 ms                                                | 3.44 ms: 1.08x slower                                      |
| logging_format             | 6.23 us                                                | 6.74 us: 1.08x slower                                      |
| generators                 | 28.8 ms                                                | 31.3 ms: 1.09x slower                                      |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.11x slower                                      |
| json_loads                 | 27.2 us                                                | 30.2 us: 1.11x slower                                      |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                      |
| many_optionals             | 857 us                                                 | 978 us: 1.14x slower                                       |
| nbody                      | 87.7 ms                                                | 101 ms: 1.15x slower                                       |
| subparsers                 | 15.5 ms                                                | 24.1 ms: 1.56x slower                                      |
| logging_silent             | 101 ns                                                 | 473 ns: 4.69x slower                                       |
| Geometric mean             | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (2): docutils, asyncio_websockets
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250526-3.14.0b2-12d3f88/bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 99.45% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x
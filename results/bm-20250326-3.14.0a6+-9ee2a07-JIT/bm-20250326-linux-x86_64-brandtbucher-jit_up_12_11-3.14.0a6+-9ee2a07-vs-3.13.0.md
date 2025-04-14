# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_12_11
- machine: linux-x86_64
- commit hash: 9ee2a07
- commit date: 2025-03-26
- overall geometric mean: 1.039x faster
- HPT reliability: 96.80%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 264 ms: 1.01x faster                                                 |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                               |
| html5lib       | 63.4 ms                                                | 62.3 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 626 ms: 1.38x faster                                                 |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.35x faster                                                 |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                 |
| async_generators           | 433 ms                                                 | 415 ms: 1.04x faster                                                 |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                         |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.4 ms: 1.20x faster                                                |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                         |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                |
| regex_effbot   | 3.77 ms                                                | 3.48 ms: 1.08x faster                                                |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                 |
| regex_dna      | 220 ms                                                 | 226 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.88 sec: 1.13x faster                                               |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 80.5 ms: 1.08x faster                                                |
| xml_etree_process    | 60.5 ms                                                | 57.0 ms: 1.06x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 97.2 ms: 1.04x faster                                                |
| unpickle_pure_python | 213 us                                                 | 212 us: 1.01x faster                                                 |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                                 |
| json_loads           | 27.2 us                                                | 29.9 us: 1.10x slower                                                |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                |
| python_startup_no_site | 7.00 ms                                                | 8.18 ms: 1.17x slower                                                |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                |
| django_template | 31.7 ms                                                | 32.4 ms: 1.02x slower                                                |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 626 ms: 1.38x faster                                                 |
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                                 |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.35x faster                                                 |
| deepcopy_memo              | 38.4 us                                                | 29.0 us: 1.32x faster                                                |
| richards                   | 47.5 ms                                                | 35.9 ms: 1.32x faster                                                |
| richards_super             | 53.7 ms                                                | 40.6 ms: 1.32x faster                                                |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                 |
| spectral_norm              | 113 ms                                                 | 93.0 ms: 1.22x faster                                                |
| float                      | 78.7 ms                                                | 65.4 ms: 1.20x faster                                                |
| deepcopy_reduce            | 3.24 us                                                | 2.75 us: 1.18x faster                                                |
| scimark_fft                | 367 ms                                                 | 312 ms: 1.17x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                 |
| tomli_loads                | 2.12 sec                                               | 1.88 sec: 1.13x faster                                               |
| regex_v8                   | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                 |
| pylint                     | 312 ms                                                 | 282 ms: 1.11x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.63 ms: 1.09x faster                                                |
| telco                      | 8.40 ms                                                | 7.77 ms: 1.08x faster                                                |
| regex_effbot               | 3.77 ms                                                | 3.48 ms: 1.08x faster                                                |
| xml_etree_generate         | 86.8 ms                                                | 80.5 ms: 1.08x faster                                                |
| sqlite_synth               | 2.90 us                                                | 2.71 us: 1.07x faster                                                |
| dulwich_log                | 64.6 ms                                                | 60.8 ms: 1.06x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                |
| xml_etree_process          | 60.5 ms                                                | 57.0 ms: 1.06x faster                                                |
| pyflate                    | 470 ms                                                 | 443 ms: 1.06x faster                                                 |
| go                         | 141 ms                                                 | 133 ms: 1.05x faster                                                 |
| deltablue                  | 3.19 ms                                                | 3.05 ms: 1.05x faster                                                |
| async_generators           | 433 ms                                                 | 415 ms: 1.04x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 97.2 ms: 1.04x faster                                                |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                                |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                 |
| logging_silent             | 101 ns                                                 | 98.4 ns: 1.03x faster                                                |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.59 sec: 1.02x faster                                               |
| logging_simple             | 5.65 us                                                | 5.54 us: 1.02x faster                                                |
| gc_traversal               | 4.90 ms                                                | 4.80 ms: 1.02x faster                                                |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                 |
| html5lib                   | 63.4 ms                                                | 62.3 ms: 1.02x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                               |
| mdp                        | 2.54 sec                                               | 2.51 sec: 1.01x faster                                               |
| thrift                     | 800 us                                                 | 792 us: 1.01x faster                                                 |
| 2to3                       | 266 ms                                                 | 264 ms: 1.01x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 212 us: 1.01x faster                                                 |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 133 ms: 1.00x slower                                                 |
| generators                 | 28.8 ms                                                | 28.9 ms: 1.01x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                |
| shortest_path              | 487 ms                                                 | 491 ms: 1.01x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                                 |
| sympy_str                  | 273 ms                                                 | 276 ms: 1.01x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 67.6 ms: 1.01x slower                                                |
| meteor_contest             | 108 ms                                                 | 110 ms: 1.01x slower                                                 |
| sympy_integrate            | 19.8 ms                                                | 20.1 ms: 1.01x slower                                                |
| connected_components       | 447 ms                                                 | 455 ms: 1.02x slower                                                 |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                |
| django_template            | 31.7 ms                                                | 32.4 ms: 1.02x slower                                                |
| raytrace                   | 262 ms                                                 | 268 ms: 1.02x slower                                                 |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                 |
| regex_dna                  | 220 ms                                                 | 226 ms: 1.03x slower                                                 |
| chaos                      | 58.0 ms                                                | 59.9 ms: 1.03x slower                                                |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                |
| coverage                   | 82.8 ms                                                | 85.7 ms: 1.03x slower                                                |
| sympy_expand               | 456 ms                                                 | 474 ms: 1.04x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                               |
| nqueens                    | 80.9 ms                                                | 84.1 ms: 1.04x slower                                                |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                 |
| crypto_pyaes               | 74.7 ms                                                | 78.6 ms: 1.05x slower                                                |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                                 |
| fannkuch                   | 394 ms                                                 | 419 ms: 1.06x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 1.57 sec: 1.06x slower                                               |
| pprint_safe_repr           | 727 ms                                                 | 777 ms: 1.07x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 883 us: 1.08x slower                                                 |
| json_loads                 | 27.2 us                                                | 29.9 us: 1.10x slower                                                |
| many_optionals             | 857 us                                                 | 970 us: 1.13x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.90 ms: 1.14x slower                                                |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                |
| comprehensions             | 16.5 us                                                | 19.0 us: 1.15x slower                                                |
| python_startup_no_site     | 7.00 ms                                                | 8.18 ms: 1.17x slower                                                |
| subparsers                 | 15.5 ms                                                | 21.1 ms: 1.37x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 82.7 ms: 3.45x slower                                                |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (6): json, logging_format, genshi_xml, sphinx, asyncio_websockets, nbody
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250326-3.14.0a6+-9ee2a07-JIT/bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 96.80% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x
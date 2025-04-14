# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_has_space
- machine: linux-x86_64
- commit hash: 0c7e399
- commit date: 2025-03-25
- overall geometric mean: 1.040x faster
- HPT reliability: 98.54%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 264 ms: 1.01x faster                                                  |
| docutils       | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                  |
| async_tree_io              | 838 ms                                                 | 626 ms: 1.34x faster                                                  |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                  |
| async_generators           | 433 ms                                                 | 415 ms: 1.05x faster                                                  |
| coroutines                 | 22.2 ms                                                | 24.1 ms: 1.09x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.3 ms: 1.20x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.14 ms: 1.20x faster                                                 |
| regex_v8       | 26.9 ms                                                | 22.7 ms: 1.18x faster                                                 |
| regex_dna      | 220 ms                                                 | 213 ms: 1.03x faster                                                  |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.87 sec: 1.13x faster                                                |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 80.7 ms: 1.08x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 56.9 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 98.4 ms: 1.03x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 214 us: 1.01x slower                                                  |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.06x slower                                                  |
| json_loads           | 27.2 us                                                | 29.9 us: 1.10x slower                                                 |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.14x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                 |
| python_startup_no_site | 7.00 ms                                                | 8.18 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.05x faster                                                 |
| django_template | 31.7 ms                                                | 31.8 ms: 1.01x slower                                                 |
| mako            | 10.7 ms                                                | 10.9 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                  |
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                                  |
| async_tree_io              | 838 ms                                                 | 626 ms: 1.34x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 28.9 us: 1.33x faster                                                 |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                  |
| richards                   | 47.5 ms                                                | 36.4 ms: 1.31x faster                                                 |
| richards_super             | 53.7 ms                                                | 41.3 ms: 1.30x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                  |
| float                      | 78.7 ms                                                | 65.3 ms: 1.20x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.14 ms: 1.20x faster                                                 |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.19x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 22.7 ms: 1.18x faster                                                 |
| scimark_fft                | 367 ms                                                 | 313 ms: 1.17x faster                                                  |
| spectral_norm              | 113 ms                                                 | 97.0 ms: 1.17x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.87 sec: 1.13x faster                                                |
| pylint                     | 312 ms                                                 | 282 ms: 1.11x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                  |
| go                         | 141 ms                                                 | 129 ms: 1.09x faster                                                  |
| telco                      | 8.40 ms                                                | 7.79 ms: 1.08x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 80.7 ms: 1.08x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.72 us: 1.07x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 56.9 ms: 1.06x faster                                                 |
| dulwich_log                | 64.6 ms                                                | 60.8 ms: 1.06x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.75 ms: 1.06x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.06x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.05x faster                                                 |
| async_generators           | 433 ms                                                 | 415 ms: 1.05x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.6 ms: 1.04x faster                                                 |
| pyflate                    | 470 ms                                                 | 450 ms: 1.04x faster                                                  |
| deltablue                  | 3.19 ms                                                | 3.08 ms: 1.04x faster                                                 |
| regex_dna                  | 220 ms                                                 | 213 ms: 1.03x faster                                                  |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 98.4 ms: 1.03x faster                                                 |
| logging_silent             | 101 ns                                                 | 98.2 ns: 1.03x faster                                                 |
| thrift                     | 800 us                                                 | 778 us: 1.03x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                                |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                  |
| mdp                        | 2.54 sec                                               | 2.50 sec: 1.02x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.63 sec: 1.01x faster                                                |
| gc_traversal               | 4.90 ms                                                | 4.85 ms: 1.01x faster                                                 |
| 2to3                       | 266 ms                                                 | 264 ms: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| django_template            | 31.7 ms                                                | 31.8 ms: 1.01x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 214 us: 1.01x slower                                                  |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.1 ms: 1.01x slower                                                 |
| sympy_str                  | 273 ms                                                 | 276 ms: 1.01x slower                                                  |
| generators                 | 28.8 ms                                                | 29.2 ms: 1.01x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 153 ms: 1.02x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 20.1 ms: 1.02x slower                                                 |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                                 |
| mako                       | 10.7 ms                                                | 10.9 ms: 1.02x slower                                                 |
| shortest_path              | 487 ms                                                 | 498 ms: 1.02x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                  |
| connected_components       | 447 ms                                                 | 458 ms: 1.02x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 68.7 ms: 1.03x slower                                                 |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 753 ms: 1.04x slower                                                  |
| raytrace                   | 262 ms                                                 | 271 ms: 1.04x slower                                                  |
| chaos                      | 58.0 ms                                                | 60.2 ms: 1.04x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                |
| sympy_expand               | 456 ms                                                 | 477 ms: 1.05x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 78.2 ms: 1.05x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                  |
| coverage                   | 82.8 ms                                                | 86.7 ms: 1.05x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 1.55 sec: 1.05x slower                                                |
| nqueens                    | 80.9 ms                                                | 85.0 ms: 1.05x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.06x slower                                                  |
| fannkuch                   | 394 ms                                                 | 423 ms: 1.07x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 880 us: 1.08x slower                                                  |
| coroutines                 | 22.2 ms                                                | 24.1 ms: 1.09x slower                                                 |
| json_loads                 | 27.2 us                                                | 29.9 us: 1.10x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.81 ms: 1.12x slower                                                 |
| many_optionals             | 857 us                                                 | 971 us: 1.13x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.14x slower                                                 |
| comprehensions             | 16.5 us                                                | 18.9 us: 1.15x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 8.18 ms: 1.17x slower                                                 |
| subparsers                 | 15.5 ms                                                | 21.1 ms: 1.36x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 82.7 ms: 3.45x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (9): sphinx, logging_simple, html5lib, genshi_xml, nbody, json, asyncio_websockets, sqlalchemy_declarative, logging_format
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250325-3.14.0a6+-0c7e399-JIT/bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 98.54% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
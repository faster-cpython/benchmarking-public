# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: method_jit_2_5
- machine: linux-x86_64
- commit hash: e8e0a8d
- commit date: 2025-03-25
- overall geometric mean: 1.020x faster
- HPT reliability: 91.35%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.03x faster                                                       |
| html5lib       | 63.4 ms                                                | 62.2 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 319 ms: 1.37x faster                                                       |
| async_tree_io              | 838 ms                                                 | 623 ms: 1.35x faster                                                       |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 476 ms: 1.14x faster                                                       |
| async_generators           | 433 ms                                                 | 406 ms: 1.07x faster                                                       |
| coroutines                 | 22.2 ms                                                | 24.9 ms: 1.12x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.4 ms: 1.12x faster                                                      |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.5 ms: 1.14x faster                                                      |
| regex_effbot   | 3.77 ms                                                | 3.47 ms: 1.08x faster                                                      |
| regex_compile  | 132 ms                                                 | 130 ms: 1.01x faster                                                       |
| regex_dna      | 220 ms                                                 | 224 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.08x faster                                                       |
| tomli_loads          | 2.12 sec                                               | 2.04 sec: 1.04x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 99.0 ms: 1.02x faster                                                      |
| xml_etree_generate   | 86.8 ms                                                | 85.7 ms: 1.01x faster                                                      |
| xml_etree_process    | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                      |
| unpickle_pure_python | 213 us                                                 | 224 us: 1.05x slower                                                       |
| pickle_pure_python   | 302 us                                                 | 331 us: 1.09x slower                                                       |
| json_loads           | 27.2 us                                                | 30.0 us: 1.10x slower                                                      |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                      |
| python_startup_no_site | 7.00 ms                                                | 8.21 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 22.0 ms: 1.03x faster                                                      |
| django_template | 31.7 ms                                                | 32.7 ms: 1.03x slower                                                      |
| mako            | 10.7 ms                                                | 12.0 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 319 ms: 1.37x faster                                                       |
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                                       |
| async_tree_io              | 838 ms                                                 | 623 ms: 1.35x faster                                                       |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                       |
| deepcopy_memo              | 38.4 us                                                | 30.7 us: 1.25x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.19x faster                                                      |
| go                         | 141 ms                                                 | 121 ms: 1.16x faster                                                       |
| scimark_fft                | 367 ms                                                 | 315 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                       |
| regex_v8                   | 26.9 ms                                                | 23.5 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 476 ms: 1.14x faster                                                       |
| spectral_norm              | 113 ms                                                 | 99.7 ms: 1.14x faster                                                      |
| float                      | 78.7 ms                                                | 70.4 ms: 1.12x faster                                                      |
| pylint                     | 312 ms                                                 | 286 ms: 1.09x faster                                                       |
| regex_effbot               | 3.77 ms                                                | 3.47 ms: 1.08x faster                                                      |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.08x faster                                                       |
| dulwich_log                | 64.6 ms                                                | 59.8 ms: 1.08x faster                                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.68 ms: 1.08x faster                                                      |
| async_generators           | 433 ms                                                 | 406 ms: 1.07x faster                                                       |
| gc_traversal               | 4.90 ms                                                | 4.65 ms: 1.05x faster                                                      |
| sqlite_synth               | 2.90 us                                                | 2.76 us: 1.05x faster                                                      |
| telco                      | 8.40 ms                                                | 7.99 ms: 1.05x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 2.04 sec: 1.04x faster                                                     |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                                      |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                     |
| genshi_text                | 22.6 ms                                                | 22.0 ms: 1.03x faster                                                      |
| 2to3                       | 266 ms                                                 | 259 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 101 ms                                                 | 99.0 ms: 1.02x faster                                                      |
| richards                   | 47.5 ms                                                | 46.6 ms: 1.02x faster                                                      |
| html5lib                   | 63.4 ms                                                | 62.2 ms: 1.02x faster                                                      |
| mdp                        | 2.54 sec                                               | 2.50 sec: 1.02x faster                                                     |
| richards_super             | 53.7 ms                                                | 53.0 ms: 1.01x faster                                                      |
| xml_etree_generate         | 86.8 ms                                                | 85.7 ms: 1.01x faster                                                      |
| connected_components       | 447 ms                                                 | 441 ms: 1.01x faster                                                       |
| regex_compile              | 132 ms                                                 | 130 ms: 1.01x faster                                                       |
| pyflate                    | 470 ms                                                 | 464 ms: 1.01x faster                                                       |
| xml_etree_process          | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.01x faster                                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.67 sec: 1.00x faster                                                     |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                       |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                      |
| logging_simple             | 5.65 us                                                | 5.72 us: 1.01x slower                                                      |
| generators                 | 28.8 ms                                                | 29.2 ms: 1.02x slower                                                      |
| logging_format             | 6.23 us                                                | 6.33 us: 1.02x slower                                                      |
| sympy_integrate            | 19.8 ms                                                | 20.1 ms: 1.02x slower                                                      |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 160 us                                                 | 163 us: 1.02x slower                                                       |
| meteor_contest             | 108 ms                                                 | 110 ms: 1.02x slower                                                       |
| regex_dna                  | 220 ms                                                 | 224 ms: 1.02x slower                                                       |
| sympy_expand               | 456 ms                                                 | 466 ms: 1.02x slower                                                       |
| shortest_path              | 487 ms                                                 | 498 ms: 1.02x slower                                                       |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.03x slower                                                       |
| thrift                     | 800 us                                                 | 823 us: 1.03x slower                                                       |
| scimark_monte_carlo        | 66.8 ms                                                | 68.7 ms: 1.03x slower                                                      |
| django_template            | 31.7 ms                                                | 32.7 ms: 1.03x slower                                                      |
| sympy_str                  | 273 ms                                                 | 282 ms: 1.03x slower                                                       |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                      |
| deltablue                  | 3.19 ms                                                | 3.32 ms: 1.04x slower                                                      |
| sympy_sum                  | 150 ms                                                 | 157 ms: 1.04x slower                                                       |
| crypto_pyaes               | 74.7 ms                                                | 77.8 ms: 1.04x slower                                                      |
| fannkuch                   | 394 ms                                                 | 412 ms: 1.05x slower                                                       |
| chaos                      | 58.0 ms                                                | 61.1 ms: 1.05x slower                                                      |
| unpickle_pure_python       | 213 us                                                 | 224 us: 1.05x slower                                                       |
| nqueens                    | 80.9 ms                                                | 85.9 ms: 1.06x slower                                                      |
| bench_thread_pool          | 818 us                                                 | 883 us: 1.08x slower                                                       |
| pickle_pure_python         | 302 us                                                 | 331 us: 1.09x slower                                                       |
| hexiom                     | 6.08 ms                                                | 6.68 ms: 1.10x slower                                                      |
| raytrace                   | 262 ms                                                 | 288 ms: 1.10x slower                                                       |
| json_loads                 | 27.2 us                                                | 30.0 us: 1.10x slower                                                      |
| coroutines                 | 22.2 ms                                                | 24.9 ms: 1.12x slower                                                      |
| coverage                   | 82.8 ms                                                | 92.9 ms: 1.12x slower                                                      |
| pprint_safe_repr           | 727 ms                                                 | 815 ms: 1.12x slower                                                       |
| mako                       | 10.7 ms                                                | 12.0 ms: 1.12x slower                                                      |
| pprint_pformat             | 1.48 sec                                               | 1.66 sec: 1.12x slower                                                     |
| many_optionals             | 857 us                                                 | 962 us: 1.12x slower                                                       |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                      |
| python_startup_no_site     | 7.00 ms                                                | 8.21 ms: 1.17x slower                                                      |
| comprehensions             | 16.5 us                                                | 20.8 us: 1.26x slower                                                      |
| subparsers                 | 15.5 ms                                                | 21.2 ms: 1.37x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 83.1 ms: 3.47x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (8): pycparser, logging_silent, nbody, scimark_sor, asyncio_websockets, sphinx, genshi_xml, json
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, docutils, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250325-3.14.0a6+-e8e0a8d-JIT/bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2_5-3.14.0a6+-e8e0a8d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.020x faster

# HPT report

- Reliability score: 91.35% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x
# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: lower_jit_tier1
- machine: linux-x86_64
- commit hash: 4d50db6
- commit date: 2024-12-13
- overall geometric mean: 1.032x faster
- HPT reliability: 95.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                        |
| docutils       | 2.58 sec                                               | 2.73 sec: 1.06x slower                                                      |
| html5lib       | 63.4 ms                                                | 64.2 ms: 1.01x slower                                                       |
| sphinx         | 1.03 sec                                               | 1.06 sec: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                        |
| async_tree_io_tg           | 861 ms                                                 | 605 ms: 1.42x faster                                                        |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                        |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                        |
| async_tree_memoization     | 437 ms                                                 | 335 ms: 1.30x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 476 ms: 1.14x faster                                                        |
| async_generators           | 433 ms                                                 | 446 ms: 1.03x slower                                                        |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.08x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.8 ms: 1.08x faster                                                       |
| nbody          | 87.7 ms                                                | 83.6 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.21 ms: 1.17x faster                                                       |
| regex_v8       | 26.9 ms                                                | 25.2 ms: 1.07x faster                                                       |
| regex_dna      | 220 ms                                                 | 211 ms: 1.04x faster                                                        |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.13x faster                                                        |
| xml_etree_generate   | 86.8 ms                                                | 77.3 ms: 1.12x faster                                                       |
| xml_etree_process    | 60.5 ms                                                | 54.6 ms: 1.11x faster                                                       |
| unpickle_pure_python | 213 us                                                 | 194 us: 1.10x faster                                                        |
| tomli_loads          | 2.12 sec                                               | 1.93 sec: 1.10x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 94.7 ms: 1.07x faster                                                       |
| json_loads           | 27.2 us                                                | 26.0 us: 1.04x faster                                                       |
| pickle_pure_python   | 302 us                                                 | 316 us: 1.05x slower                                                        |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                       |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 9.95 ms: 1.07x faster                                                       |
| genshi_text     | 22.6 ms                                                | 23.7 ms: 1.05x slower                                                       |
| django_template | 31.7 ms                                                | 34.2 ms: 1.08x slower                                                       |
| genshi_xml      | 50.5 ms                                                | 56.2 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                        |
| async_tree_io_tg           | 861 ms                                                 | 605 ms: 1.42x faster                                                        |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                        |
| deepcopy                   | 354 us                                                 | 268 us: 1.32x faster                                                        |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                        |
| async_tree_memoization     | 437 ms                                                 | 335 ms: 1.30x faster                                                        |
| deepcopy_memo              | 38.4 us                                                | 29.4 us: 1.30x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.21x faster                                                       |
| regex_effbot               | 3.77 ms                                                | 3.21 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 476 ms: 1.14x faster                                                        |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.13x faster                                                        |
| telco                      | 8.40 ms                                                | 7.46 ms: 1.13x faster                                                       |
| go                         | 141 ms                                                 | 125 ms: 1.12x faster                                                        |
| xml_etree_generate         | 86.8 ms                                                | 77.3 ms: 1.12x faster                                                       |
| json                       | 5.32 ms                                                | 4.76 ms: 1.12x faster                                                       |
| xml_etree_process          | 60.5 ms                                                | 54.6 ms: 1.11x faster                                                       |
| scimark_fft                | 367 ms                                                 | 333 ms: 1.10x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 194 us: 1.10x faster                                                        |
| tomli_loads                | 2.12 sec                                               | 1.93 sec: 1.10x faster                                                      |
| pathlib                    | 17.4 ms                                                | 16.0 ms: 1.08x faster                                                       |
| crypto_pyaes               | 74.7 ms                                                | 69.1 ms: 1.08x faster                                                       |
| float                      | 78.7 ms                                                | 72.8 ms: 1.08x faster                                                       |
| mako                       | 10.7 ms                                                | 9.95 ms: 1.07x faster                                                       |
| pyflate                    | 470 ms                                                 | 438 ms: 1.07x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 94.7 ms: 1.07x faster                                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.39 sec: 1.07x faster                                                      |
| regex_v8                   | 26.9 ms                                                | 25.2 ms: 1.07x faster                                                       |
| pylint                     | 312 ms                                                 | 293 ms: 1.07x faster                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 62.8 ms: 1.06x faster                                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.76 ms: 1.06x faster                                                       |
| nbody                      | 87.7 ms                                                | 83.6 ms: 1.05x faster                                                       |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                                       |
| json_loads                 | 27.2 us                                                | 26.0 us: 1.04x faster                                                       |
| richards                   | 47.5 ms                                                | 45.6 ms: 1.04x faster                                                       |
| regex_dna                  | 220 ms                                                 | 211 ms: 1.04x faster                                                        |
| thrift                     | 800 us                                                 | 770 us: 1.04x faster                                                        |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                                        |
| fannkuch                   | 394 ms                                                 | 382 ms: 1.03x faster                                                        |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                        |
| richards_super             | 53.7 ms                                                | 52.3 ms: 1.03x faster                                                       |
| gc_traversal               | 4.90 ms                                                | 4.77 ms: 1.03x faster                                                       |
| connected_components       | 447 ms                                                 | 437 ms: 1.02x faster                                                        |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                        |
| k_core                     | 2.37 sec                                               | 2.32 sec: 1.02x faster                                                      |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                        |
| scimark_lu                 | 114 ms                                                 | 113 ms: 1.01x faster                                                        |
| shortest_path              | 487 ms                                                 | 482 ms: 1.01x faster                                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.44 ms: 1.00x faster                                                       |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 108 ms                                                 | 109 ms: 1.01x slower                                                        |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                       |
| html5lib                   | 63.4 ms                                                | 64.2 ms: 1.01x slower                                                       |
| logging_format             | 6.23 us                                                | 6.35 us: 1.02x slower                                                       |
| logging_simple             | 5.65 us                                                | 5.78 us: 1.02x slower                                                       |
| sqlglot_parse              | 1.26 ms                                                | 1.30 ms: 1.03x slower                                                       |
| sphinx                     | 1.03 sec                                               | 1.06 sec: 1.03x slower                                                      |
| chaos                      | 58.0 ms                                                | 59.7 ms: 1.03x slower                                                       |
| deltablue                  | 3.19 ms                                                | 3.28 ms: 1.03x slower                                                       |
| async_generators           | 433 ms                                                 | 446 ms: 1.03x slower                                                        |
| sqlglot_optimize           | 53.4 ms                                                | 55.0 ms: 1.03x slower                                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.62 ms: 1.03x slower                                                       |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                       |
| pprint_safe_repr           | 727 ms                                                 | 755 ms: 1.04x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 157 ms: 1.04x slower                                                        |
| pprint_pformat             | 1.48 sec                                               | 1.54 sec: 1.04x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 316 us: 1.05x slower                                                        |
| genshi_text                | 22.6 ms                                                | 23.7 ms: 1.05x slower                                                       |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                        |
| sympy_str                  | 273 ms                                                 | 287 ms: 1.05x slower                                                        |
| sympy_integrate            | 19.8 ms                                                | 20.8 ms: 1.05x slower                                                       |
| docutils                   | 2.58 sec                                               | 2.73 sec: 1.06x slower                                                      |
| sympy_expand               | 456 ms                                                 | 484 ms: 1.06x slower                                                        |
| dulwich_log                | 64.6 ms                                                | 68.9 ms: 1.07x slower                                                       |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.08x slower                                                       |
| nqueens                    | 80.9 ms                                                | 87.3 ms: 1.08x slower                                                       |
| raytrace                   | 262 ms                                                 | 282 ms: 1.08x slower                                                        |
| django_template            | 31.7 ms                                                | 34.2 ms: 1.08x slower                                                       |
| bench_thread_pool          | 818 us                                                 | 884 us: 1.08x slower                                                        |
| logging_silent             | 101 ns                                                 | 111 ns: 1.10x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.10x slower                                                       |
| mdp                        | 2.54 sec                                               | 2.81 sec: 1.10x slower                                                      |
| genshi_xml                 | 50.5 ms                                                | 56.2 ms: 1.11x slower                                                       |
| hexiom                     | 6.08 ms                                                | 6.93 ms: 1.14x slower                                                       |
| many_optionals             | 857 us                                                 | 992 us: 1.16x slower                                                        |
| generators                 | 28.8 ms                                                | 34.2 ms: 1.19x slower                                                       |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                                       |
| bench_mp_pool              | 24.0 ms                                                | 81.3 ms: 3.39x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                |

Benchmark hidden because not significant (8): meteor_contest, spectral_norm, sqlalchemy_imperative, pidigits, coverage, asyncio_websockets, pycparser, djangocms
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241213-3.14.0a2+-4d50db6-JIT/bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6.json: mypy2

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 95.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x
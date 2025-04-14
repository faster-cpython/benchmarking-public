# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: baseline_jit
- machine: linux-x86_64
- commit hash: e55b89a
- commit date: 2025-03-19
- overall geometric mean: 1.025x faster
- HPT reliability: 91.19%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                     |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                     |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                     |
| async_tree_memoization     | 437 ms                                                 | 319 ms: 1.37x faster                                                     |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                     |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                     |
| async_generators           | 433 ms                                                 | 411 ms: 1.05x faster                                                     |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.2 ms: 1.09x faster                                                    |
| nbody          | 87.7 ms                                                | 91.1 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.21 ms: 1.17x faster                                                    |
| regex_v8       | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                    |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                     |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.83 sec: 1.16x faster                                                   |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 97.4 ms: 1.04x faster                                                    |
| xml_etree_generate   | 86.8 ms                                                | 85.4 ms: 1.02x faster                                                    |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                     |
| json_loads           | 27.2 us                                                | 29.9 us: 1.10x slower                                                    |
| unpickle_pure_python | 213 us                                                 | 235 us: 1.10x slower                                                     |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                    |
| python_startup_no_site | 7.00 ms                                                | 8.18 ms: 1.17x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                    |
| genshi_xml      | 50.5 ms                                                | 49.3 ms: 1.02x faster                                                    |
| django_template | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                    |
| mako            | 10.7 ms                                                | 11.8 ms: 1.10x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                     |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                     |
| deepcopy                   | 354 us                                                 | 256 us: 1.39x faster                                                     |
| async_tree_memoization     | 437 ms                                                 | 319 ms: 1.37x faster                                                     |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                     |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                     |
| deepcopy_memo              | 38.4 us                                                | 29.4 us: 1.31x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                     |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                                    |
| regex_effbot               | 3.77 ms                                                | 3.21 ms: 1.17x faster                                                    |
| scimark_fft                | 367 ms                                                 | 313 ms: 1.17x faster                                                     |
| tomli_loads                | 2.12 sec                                               | 1.83 sec: 1.16x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                     |
| go                         | 141 ms                                                 | 125 ms: 1.13x faster                                                     |
| regex_v8                   | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                    |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.50 ms: 1.12x faster                                                    |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                     |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                     |
| float                      | 78.7 ms                                                | 72.2 ms: 1.09x faster                                                    |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.09x faster                                                     |
| dulwich_log                | 64.6 ms                                                | 59.8 ms: 1.08x faster                                                    |
| richards                   | 47.5 ms                                                | 44.1 ms: 1.08x faster                                                    |
| richards_super             | 53.7 ms                                                | 50.5 ms: 1.06x faster                                                    |
| async_generators           | 433 ms                                                 | 411 ms: 1.05x faster                                                     |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                    |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                                    |
| logging_silent             | 101 ns                                                 | 97.0 ns: 1.04x faster                                                    |
| xml_etree_iterparse        | 101 ms                                                 | 97.4 ms: 1.04x faster                                                    |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                   |
| thrift                     | 800 us                                                 | 771 us: 1.04x faster                                                     |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                                     |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                     |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                                    |
| telco                      | 8.40 ms                                                | 8.16 ms: 1.03x faster                                                    |
| mdp                        | 2.54 sec                                               | 2.48 sec: 1.03x faster                                                   |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                     |
| genshi_xml                 | 50.5 ms                                                | 49.3 ms: 1.02x faster                                                    |
| logging_format             | 6.23 us                                                | 6.10 us: 1.02x faster                                                    |
| k_core                     | 2.37 sec                                               | 2.32 sec: 1.02x faster                                                   |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                     |
| logging_simple             | 5.65 us                                                | 5.55 us: 1.02x faster                                                    |
| xml_etree_generate         | 86.8 ms                                                | 85.4 ms: 1.02x faster                                                    |
| generators                 | 28.8 ms                                                | 28.6 ms: 1.00x faster                                                    |
| sqlalchemy_declarative     | 133 ms                                                 | 133 ms: 1.00x faster                                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.71 sec: 1.01x slower                                                   |
| django_template            | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                    |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                    |
| connected_components       | 447 ms                                                 | 454 ms: 1.01x slower                                                     |
| gc_traversal               | 4.90 ms                                                | 4.98 ms: 1.02x slower                                                    |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                     |
| sympy_integrate            | 19.8 ms                                                | 20.2 ms: 1.02x slower                                                    |
| raytrace                   | 262 ms                                                 | 268 ms: 1.03x slower                                                     |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                   |
| sympy_expand               | 456 ms                                                 | 471 ms: 1.03x slower                                                     |
| pprint_pformat             | 1.48 sec                                               | 1.53 sec: 1.03x slower                                                   |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                    |
| pyflate                    | 470 ms                                                 | 487 ms: 1.04x slower                                                     |
| scimark_monte_carlo        | 66.8 ms                                                | 69.4 ms: 1.04x slower                                                    |
| nbody                      | 87.7 ms                                                | 91.1 ms: 1.04x slower                                                    |
| chaos                      | 58.0 ms                                                | 60.5 ms: 1.04x slower                                                    |
| pprint_safe_repr           | 727 ms                                                 | 759 ms: 1.04x slower                                                     |
| deltablue                  | 3.19 ms                                                | 3.36 ms: 1.05x slower                                                    |
| nqueens                    | 80.9 ms                                                | 85.4 ms: 1.06x slower                                                    |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                     |
| crypto_pyaes               | 74.7 ms                                                | 79.7 ms: 1.07x slower                                                    |
| typing_runtime_protocols   | 160 us                                                 | 172 us: 1.08x slower                                                     |
| bench_thread_pool          | 818 us                                                 | 880 us: 1.08x slower                                                     |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                    |
| json_loads                 | 27.2 us                                                | 29.9 us: 1.10x slower                                                    |
| unpickle_pure_python       | 213 us                                                 | 235 us: 1.10x slower                                                     |
| mako                       | 10.7 ms                                                | 11.8 ms: 1.10x slower                                                    |
| coverage                   | 82.8 ms                                                | 91.5 ms: 1.10x slower                                                    |
| fannkuch                   | 394 ms                                                 | 438 ms: 1.11x slower                                                     |
| many_optionals             | 857 us                                                 | 963 us: 1.12x slower                                                     |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                    |
| python_startup_no_site     | 7.00 ms                                                | 8.18 ms: 1.17x slower                                                    |
| hexiom                     | 6.08 ms                                                | 7.41 ms: 1.22x slower                                                    |
| comprehensions             | 16.5 us                                                | 21.5 us: 1.30x slower                                                    |
| subparsers                 | 15.5 ms                                                | 21.1 ms: 1.37x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.46x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (11): sphinx, meteor_contest, sympy_sum, xml_etree_process, pidigits, html5lib, asyncio_websockets, sqlalchemy_imperative, sympy_str, shortest_path, json
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250319-3.14.0a6+-e55b89a-JIT/bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.025x faster

# HPT report

- Reliability score: 91.19% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
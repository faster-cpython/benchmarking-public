# Results vs. base

- fork: Fidget-Spinner
- ref: baseline_jit
- machine: linux-x86_64
- commit hash: e55b89a
- commit date: 2025-03-19
- overall geometric mean: 1.016x slower
- HPT reliability: 72.95%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250318-linux-x86_64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                 | 260 ms: 1.01x faster                                                     |
| docutils       | 2.70 sec                                                               | 2.66 sec: 1.01x faster                                                   |
| html5lib       | 62.6 ms                                                                | 63.4 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250318-linux-x86_64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_generators           | 420 ms                                                                 | 411 ms: 1.02x faster                                                     |
| async_tree_memoization     | 320 ms                                                                 | 319 ms: 1.00x faster                                                     |
| async_tree_cpu_io_mixed    | 491 ms                                                                 | 498 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                 | 481 ms: 1.01x slower                                                     |
| coroutines                 | 23.4 ms                                                                | 24.4 ms: 1.04x slower                                                    |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_none, async_tree_io_tg, asyncio_websockets, async_tree_io, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250318-linux-x86_64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                     |
| nbody          | 87.3 ms                                                                | 91.1 ms: 1.04x slower                                                    |
| float          | 64.7 ms                                                                | 72.2 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250318-linux-x86_64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.45 ms                                                                | 3.21 ms: 1.08x faster                                                    |
| regex_dna      | 224 ms                                                                 | 216 ms: 1.04x faster                                                     |
| regex_compile  | 127 ms                                                                 | 128 ms: 1.01x slower                                                     |
| regex_v8       | 23.3 ms                                                                | 23.9 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250318-linux-x86_64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 11.8 ms                                                                | 11.4 ms: 1.03x faster                                                    |
| tomli_loads          | 1.86 sec                                                               | 1.83 sec: 1.02x faster                                                   |
| pickle_pure_python   | 324 us                                                                 | 320 us: 1.01x faster                                                     |
| xml_etree_iterparse  | 97.9 ms                                                                | 97.4 ms: 1.01x faster                                                    |
| xml_etree_parse      | 140 ms                                                                 | 141 ms: 1.01x slower                                                     |
| xml_etree_generate   | 80.0 ms                                                                | 85.4 ms: 1.07x slower                                                    |
| unpickle_pure_python | 215 us                                                                 | 235 us: 1.09x slower                                                     |
| xml_etree_process    | 55.4 ms                                                                | 60.4 ms: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                             |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250318-linux-x86_64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.23 ms                                                                | 8.18 ms: 1.01x faster                                                    |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250318-linux-x86_64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 50.3 ms                                                                | 49.3 ms: 1.02x faster                                                    |
| django_template | 31.7 ms                                                                | 31.9 ms: 1.00x slower                                                    |
| genshi_text     | 21.2 ms                                                                | 21.5 ms: 1.01x slower                                                    |
| mako            | 11.0 ms                                                                | 11.8 ms: 1.07x slower                                                    |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20250318-linux-x86_64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-linux-x86_64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot               | 3.45 ms                                                                | 3.21 ms: 1.08x faster                                                    |
| scimark_sparse_mat_mult    | 4.71 ms                                                                | 4.50 ms: 1.05x faster                                                    |
| regex_dna                  | 224 ms                                                                 | 216 ms: 1.04x faster                                                     |
| go                         | 129 ms                                                                 | 125 ms: 1.04x faster                                                     |
| json_dumps                 | 11.8 ms                                                                | 11.4 ms: 1.03x faster                                                    |
| async_generators           | 420 ms                                                                 | 411 ms: 1.02x faster                                                     |
| scimark_lu                 | 119 ms                                                                 | 117 ms: 1.02x faster                                                     |
| thrift                     | 788 us                                                                 | 771 us: 1.02x faster                                                     |
| genshi_xml                 | 50.3 ms                                                                | 49.3 ms: 1.02x faster                                                    |
| pprint_pformat             | 1.56 sec                                                               | 1.53 sec: 1.02x faster                                                   |
| meteor_contest             | 110 ms                                                                 | 108 ms: 1.02x faster                                                     |
| tomli_loads                | 1.86 sec                                                               | 1.83 sec: 1.02x faster                                                   |
| sympy_expand               | 478 ms                                                                 | 471 ms: 1.02x faster                                                     |
| shortest_path              | 495 ms                                                                 | 488 ms: 1.01x faster                                                     |
| create_gc_cycles           | 2.51 ms                                                                | 2.47 ms: 1.01x faster                                                    |
| pycparser                  | 1.17 sec                                                               | 1.16 sec: 1.01x faster                                                   |
| pickle_pure_python         | 324 us                                                                 | 320 us: 1.01x faster                                                     |
| docutils                   | 2.70 sec                                                               | 2.66 sec: 1.01x faster                                                   |
| dulwich_log                | 60.5 ms                                                                | 59.8 ms: 1.01x faster                                                    |
| sympy_str                  | 277 ms                                                                 | 274 ms: 1.01x faster                                                     |
| 2to3                       | 262 ms                                                                 | 260 ms: 1.01x faster                                                     |
| deepcopy                   | 258 us                                                                 | 256 us: 1.01x faster                                                     |
| sympy_sum                  | 152 ms                                                                 | 150 ms: 1.01x faster                                                     |
| pprint_safe_repr           | 765 ms                                                                 | 759 ms: 1.01x faster                                                     |
| connected_components       | 457 ms                                                                 | 454 ms: 1.01x faster                                                     |
| subparsers                 | 21.3 ms                                                                | 21.1 ms: 1.01x faster                                                    |
| deepcopy_reduce            | 2.72 us                                                                | 2.70 us: 1.01x faster                                                    |
| sqlalchemy_imperative      | 17.0 ms                                                                | 16.9 ms: 1.01x faster                                                    |
| python_startup_no_site     | 8.23 ms                                                                | 8.18 ms: 1.01x faster                                                    |
| xml_etree_iterparse        | 97.9 ms                                                                | 97.4 ms: 1.01x faster                                                    |
| sqlglot_v2_normalize       | 107 ms                                                                 | 107 ms: 1.01x faster                                                     |
| many_optionals             | 968 us                                                                 | 963 us: 1.01x faster                                                     |
| async_tree_memoization     | 320 ms                                                                 | 319 ms: 1.00x faster                                                     |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                    |
| gc_traversal               | 5.00 ms                                                                | 4.98 ms: 1.00x faster                                                    |
| bench_thread_pool          | 882 us                                                                 | 880 us: 1.00x faster                                                     |
| django_template            | 31.7 ms                                                                | 31.9 ms: 1.00x slower                                                    |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x slower                                                     |
| mdp                        | 2.47 sec                                                               | 2.48 sec: 1.00x slower                                                   |
| regex_compile              | 127 ms                                                                 | 128 ms: 1.01x slower                                                     |
| logging_silent             | 96.3 ns                                                                | 97.0 ns: 1.01x slower                                                    |
| pathlib                    | 16.7 ms                                                                | 16.8 ms: 1.01x slower                                                    |
| xml_etree_parse            | 140 ms                                                                 | 141 ms: 1.01x slower                                                     |
| json                       | 5.29 ms                                                                | 5.34 ms: 1.01x slower                                                    |
| genshi_text                | 21.2 ms                                                                | 21.5 ms: 1.01x slower                                                    |
| html5lib                   | 62.6 ms                                                                | 63.4 ms: 1.01x slower                                                    |
| bpe_tokeniser              | 4.65 sec                                                               | 4.71 sec: 1.01x slower                                                   |
| async_tree_cpu_io_mixed    | 491 ms                                                                 | 498 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                 | 481 ms: 1.01x slower                                                     |
| typing_runtime_protocols   | 169 us                                                                 | 172 us: 1.02x slower                                                     |
| chaos                      | 59.4 ms                                                                | 60.5 ms: 1.02x slower                                                    |
| sqlite_synth               | 2.73 us                                                                | 2.78 us: 1.02x slower                                                    |
| scimark_monte_carlo        | 67.8 ms                                                                | 69.4 ms: 1.02x slower                                                    |
| nqueens                    | 83.3 ms                                                                | 85.4 ms: 1.02x slower                                                    |
| generators                 | 27.9 ms                                                                | 28.6 ms: 1.03x slower                                                    |
| regex_v8                   | 23.3 ms                                                                | 23.9 ms: 1.03x slower                                                    |
| crypto_pyaes               | 77.4 ms                                                                | 79.7 ms: 1.03x slower                                                    |
| sqlglot_v2_transpile       | 1.60 ms                                                                | 1.65 ms: 1.03x slower                                                    |
| fannkuch                   | 423 ms                                                                 | 438 ms: 1.03x slower                                                     |
| sqlglot_v2_parse           | 1.29 ms                                                                | 1.34 ms: 1.04x slower                                                    |
| nbody                      | 87.3 ms                                                                | 91.1 ms: 1.04x slower                                                    |
| coroutines                 | 23.4 ms                                                                | 24.4 ms: 1.04x slower                                                    |
| telco                      | 7.74 ms                                                                | 8.16 ms: 1.05x slower                                                    |
| pyflate                    | 458 ms                                                                 | 487 ms: 1.06x slower                                                     |
| mako                       | 11.0 ms                                                                | 11.8 ms: 1.07x slower                                                    |
| xml_etree_generate         | 80.0 ms                                                                | 85.4 ms: 1.07x slower                                                    |
| coverage                   | 84.4 ms                                                                | 91.5 ms: 1.08x slower                                                    |
| unpickle_pure_python       | 215 us                                                                 | 235 us: 1.09x slower                                                     |
| hexiom                     | 6.79 ms                                                                | 7.41 ms: 1.09x slower                                                    |
| xml_etree_process          | 55.4 ms                                                                | 60.4 ms: 1.09x slower                                                    |
| deltablue                  | 3.04 ms                                                                | 3.36 ms: 1.11x slower                                                    |
| float                      | 64.7 ms                                                                | 72.2 ms: 1.12x slower                                                    |
| spectral_norm              | 93.5 ms                                                                | 104 ms: 1.12x slower                                                     |
| comprehensions             | 18.9 us                                                                | 21.5 us: 1.14x slower                                                    |
| richards                   | 35.4 ms                                                                | 44.1 ms: 1.25x slower                                                    |
| richards_super             | 40.2 ms                                                                | 50.5 ms: 1.26x slower                                                    |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (20): pylint, sphinx, bench_mp_pool, k_core, async_tree_memoization_tg, async_tree_none, logging_format, sympy_integrate, sqlglot_v2_optimize, async_tree_io_tg, asyncio_websockets, sqlalchemy_declarative, json_loads, async_tree_io, scimark_fft, deepcopy_memo, raytrace, logging_simple, scimark_sor, async_tree_none_tg

- Geometric mean (including insignificant results): 1.016x slower

# HPT report

- Reliability score: 72.95% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x
# Results vs. base

- fork: Fidget-Spinner
- ref: method_jit_2
- machine: linux-x86_64
- commit hash: 3374b51
- commit date: 2025-03-25
- overall geometric mean: 1.024x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6+-ef06508 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                                 | 259 ms: 1.02x faster                                                     |
| docutils       | 2.69 sec                                                               | 2.67 sec: 1.01x faster                                                   |
| html5lib       | 62.8 ms                                                                | 62.3 ms: 1.01x faster                                                    |
| sphinx         | 1.03 sec                                                               | 1.04 sec: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6+-ef06508 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_generators           | 416 ms                                                                 | 402 ms: 1.04x faster                                                     |
| async_tree_none_tg         | 251 ms                                                                 | 255 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed_tg | 477 ms                                                                 | 483 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed    | 495 ms                                                                 | 502 ms: 1.01x slower                                                     |
| async_tree_memoization     | 316 ms                                                                 | 320 ms: 1.01x slower                                                     |
| async_tree_none            | 262 ms                                                                 | 267 ms: 1.02x slower                                                     |
| async_tree_memoization_tg  | 311 ms                                                                 | 317 ms: 1.02x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (4): coroutines, asyncio_websockets, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6+-ef06508 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 187 ms: 1.01x slower                                                     |
| float          | 65.2 ms                                                                | 70.9 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6+-ef06508 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 23.3 ms                                                                | 22.7 ms: 1.02x faster                                                    |
| regex_effbot   | 3.17 ms                                                                | 3.24 ms: 1.02x slower                                                    |
| regex_compile  | 127 ms                                                                 | 131 ms: 1.03x slower                                                     |
| regex_dna      | 211 ms                                                                 | 219 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6+-ef06508 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                                    |
| json_loads           | 29.7 us                                                                | 29.9 us: 1.01x slower                                                    |
| xml_etree_parse      | 140 ms                                                                 | 142 ms: 1.02x slower                                                     |
| xml_etree_iterparse  | 97.7 ms                                                                | 100 ms: 1.03x slower                                                     |
| pickle_pure_python   | 324 us                                                                 | 334 us: 1.03x slower                                                     |
| unpickle_pure_python | 214 us                                                                 | 223 us: 1.04x slower                                                     |
| tomli_loads          | 1.86 sec                                                               | 2.01 sec: 1.08x slower                                                   |
| xml_etree_generate   | 79.7 ms                                                                | 86.6 ms: 1.09x slower                                                    |
| xml_etree_process    | 55.8 ms                                                                | 60.7 ms: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                                  | 1.04x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6+-ef06508 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                                    |
| python_startup_no_site | 8.18 ms                                                                | 8.23 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6+-ef06508 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 50.0 ms                                                                | 50.9 ms: 1.02x slower                                                    |
| django_template | 31.9 ms                                                                | 33.1 ms: 1.04x slower                                                    |
| genshi_text     | 21.2 ms                                                                | 22.2 ms: 1.05x slower                                                    |
| mako            | 11.0 ms                                                                | 11.7 ms: 1.06x slower                                                    |
| Geometric mean  | (ref)                                                                  | 1.04x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20250323-linux-x86_64-python-ef06508f8ef1d2943b2f-3.14.0a6+-ef06508 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| go                         | 129 ms                                                                 | 119 ms: 1.08x faster                                                     |
| hexiom                     | 6.83 ms                                                                | 6.56 ms: 1.04x faster                                                    |
| scimark_sparse_mat_mult    | 4.79 ms                                                                | 4.62 ms: 1.04x faster                                                    |
| async_generators           | 416 ms                                                                 | 402 ms: 1.04x faster                                                     |
| fannkuch                   | 423 ms                                                                 | 411 ms: 1.03x faster                                                     |
| regex_v8                   | 23.3 ms                                                                | 22.7 ms: 1.02x faster                                                    |
| 2to3                       | 264 ms                                                                 | 259 ms: 1.02x faster                                                     |
| deepcopy_reduce            | 2.71 us                                                                | 2.66 us: 1.02x faster                                                    |
| deepcopy                   | 263 us                                                                 | 259 us: 1.02x faster                                                     |
| scimark_fft                | 318 ms                                                                 | 314 ms: 1.01x faster                                                     |
| crypto_pyaes               | 78.9 ms                                                                | 78.0 ms: 1.01x faster                                                    |
| html5lib                   | 62.8 ms                                                                | 62.3 ms: 1.01x faster                                                    |
| meteor_contest             | 110 ms                                                                 | 109 ms: 1.01x faster                                                     |
| scimark_lu                 | 119 ms                                                                 | 118 ms: 1.01x faster                                                     |
| scimark_sor                | 120 ms                                                                 | 120 ms: 1.01x faster                                                     |
| sqlglot_v2_optimize        | 54.2 ms                                                                | 53.8 ms: 1.01x faster                                                    |
| docutils                   | 2.69 sec                                                               | 2.67 sec: 1.01x faster                                                   |
| create_gc_cycles           | 2.47 ms                                                                | 2.46 ms: 1.00x faster                                                    |
| bpe_tokeniser              | 4.60 sec                                                               | 4.61 sec: 1.00x slower                                                   |
| python_startup             | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                                    |
| many_optionals             | 968 us                                                                 | 974 us: 1.01x slower                                                     |
| python_startup_no_site     | 8.18 ms                                                                | 8.23 ms: 1.01x slower                                                    |
| pidigits                   | 186 ms                                                                 | 187 ms: 1.01x slower                                                     |
| sqlalchemy_declarative     | 133 ms                                                                 | 134 ms: 1.01x slower                                                     |
| sqlite_synth               | 2.73 us                                                                | 2.75 us: 1.01x slower                                                    |
| json_dumps                 | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                                    |
| sqlglot_v2_normalize       | 107 ms                                                                 | 108 ms: 1.01x slower                                                     |
| nqueens                    | 84.4 ms                                                                | 85.2 ms: 1.01x slower                                                    |
| mdp                        | 2.48 sec                                                               | 2.50 sec: 1.01x slower                                                   |
| json_loads                 | 29.7 us                                                                | 29.9 us: 1.01x slower                                                    |
| pprint_pformat             | 1.56 sec                                                               | 1.57 sec: 1.01x slower                                                   |
| chaos                      | 60.5 ms                                                                | 61.2 ms: 1.01x slower                                                    |
| async_tree_none_tg         | 251 ms                                                                 | 255 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed_tg | 477 ms                                                                 | 483 ms: 1.01x slower                                                     |
| sphinx                     | 1.03 sec                                                               | 1.04 sec: 1.01x slower                                                   |
| logging_silent             | 99.2 ns                                                                | 101 ns: 1.01x slower                                                     |
| async_tree_cpu_io_mixed    | 495 ms                                                                 | 502 ms: 1.01x slower                                                     |
| async_tree_memoization     | 316 ms                                                                 | 320 ms: 1.01x slower                                                     |
| telco                      | 7.77 ms                                                                | 7.88 ms: 1.01x slower                                                    |
| pprint_safe_repr           | 755 ms                                                                 | 768 ms: 1.02x slower                                                     |
| genshi_xml                 | 50.0 ms                                                                | 50.9 ms: 1.02x slower                                                    |
| json                       | 5.25 ms                                                                | 5.34 ms: 1.02x slower                                                    |
| async_tree_none            | 262 ms                                                                 | 267 ms: 1.02x slower                                                     |
| async_tree_memoization_tg  | 311 ms                                                                 | 317 ms: 1.02x slower                                                     |
| xml_etree_parse            | 140 ms                                                                 | 142 ms: 1.02x slower                                                     |
| regex_effbot               | 3.17 ms                                                                | 3.24 ms: 1.02x slower                                                    |
| dulwich_log                | 60.4 ms                                                                | 61.7 ms: 1.02x slower                                                    |
| subparsers                 | 21.0 ms                                                                | 21.4 ms: 1.02x slower                                                    |
| deepcopy_memo              | 28.9 us                                                                | 29.7 us: 1.03x slower                                                    |
| sympy_integrate            | 20.1 ms                                                                | 20.6 ms: 1.03x slower                                                    |
| xml_etree_iterparse        | 97.7 ms                                                                | 100 ms: 1.03x slower                                                     |
| regex_compile              | 127 ms                                                                 | 131 ms: 1.03x slower                                                     |
| pickle_pure_python         | 324 us                                                                 | 334 us: 1.03x slower                                                     |
| bench_thread_pool          | 879 us                                                                 | 908 us: 1.03x slower                                                     |
| regex_dna                  | 211 ms                                                                 | 219 ms: 1.03x slower                                                     |
| sqlglot_v2_transpile       | 1.60 ms                                                                | 1.66 ms: 1.03x slower                                                    |
| sqlglot_v2_parse           | 1.29 ms                                                                | 1.34 ms: 1.04x slower                                                    |
| gc_traversal               | 4.66 ms                                                                | 4.83 ms: 1.04x slower                                                    |
| django_template            | 31.9 ms                                                                | 33.1 ms: 1.04x slower                                                    |
| pylint                     | 281 ms                                                                 | 292 ms: 1.04x slower                                                     |
| unpickle_pure_python       | 214 us                                                                 | 223 us: 1.04x slower                                                     |
| sympy_str                  | 275 ms                                                                 | 286 ms: 1.04x slower                                                     |
| genshi_text                | 21.2 ms                                                                | 22.2 ms: 1.05x slower                                                    |
| sympy_sum                  | 152 ms                                                                 | 159 ms: 1.05x slower                                                     |
| pyflate                    | 448 ms                                                                 | 472 ms: 1.05x slower                                                     |
| logging_simple             | 5.57 us                                                                | 5.88 us: 1.06x slower                                                    |
| mako                       | 11.0 ms                                                                | 11.7 ms: 1.06x slower                                                    |
| logging_format             | 6.26 us                                                                | 6.65 us: 1.06x slower                                                    |
| generators                 | 28.6 ms                                                                | 30.5 ms: 1.07x slower                                                    |
| raytrace                   | 270 ms                                                                 | 289 ms: 1.07x slower                                                     |
| tomli_loads                | 1.86 sec                                                               | 2.01 sec: 1.08x slower                                                   |
| spectral_norm              | 95.4 ms                                                                | 103 ms: 1.08x slower                                                     |
| xml_etree_generate         | 79.7 ms                                                                | 86.6 ms: 1.09x slower                                                    |
| float                      | 65.2 ms                                                                | 70.9 ms: 1.09x slower                                                    |
| xml_etree_process          | 55.8 ms                                                                | 60.7 ms: 1.09x slower                                                    |
| thrift                     | 773 us                                                                 | 841 us: 1.09x slower                                                     |
| sqlalchemy_imperative      | 16.9 ms                                                                | 18.3 ms: 1.09x slower                                                    |
| comprehensions             | 18.9 us                                                                | 20.7 us: 1.10x slower                                                    |
| coverage                   | 85.0 ms                                                                | 93.7 ms: 1.10x slower                                                    |
| deltablue                  | 3.08 ms                                                                | 3.44 ms: 1.12x slower                                                    |
| richards                   | 36.1 ms                                                                | 45.1 ms: 1.25x slower                                                    |
| richards_super             | 41.1 ms                                                                | 52.5 ms: 1.28x slower                                                    |
| Geometric mean             | (ref)                                                                  | 1.02x slower                                                             |

Benchmark hidden because not significant (14): connected_components, nbody, k_core, typing_runtime_protocols, scimark_monte_carlo, coroutines, sympy_expand, asyncio_websockets, pycparser, pathlib, async_tree_io_tg, bench_mp_pool, shortest_path, async_tree_io

- Geometric mean (including insignificant results): 1.024x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x
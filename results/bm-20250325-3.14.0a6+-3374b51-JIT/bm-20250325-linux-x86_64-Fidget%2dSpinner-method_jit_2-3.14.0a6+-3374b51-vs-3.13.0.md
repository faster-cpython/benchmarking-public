# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: method_jit_2
- machine: linux-x86_64
- commit hash: 3374b51
- commit date: 2025-03-25
- overall geometric mean: 1.017x faster
- HPT reliability: 66.74%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.03x faster                                                     |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                   |
| html5lib       | 63.4 ms                                                | 62.3 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                     |
| async_tree_io_tg           | 861 ms                                                 | 624 ms: 1.38x faster                                                     |
| async_tree_memoization     | 437 ms                                                 | 320 ms: 1.36x faster                                                     |
| async_tree_io              | 838 ms                                                 | 628 ms: 1.34x faster                                                     |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.12x faster                                                     |
| async_generators           | 433 ms                                                 | 402 ms: 1.08x faster                                                     |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.9 ms: 1.11x faster                                                    |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.7 ms: 1.18x faster                                                    |
| regex_effbot   | 3.77 ms                                                | 3.24 ms: 1.16x faster                                                    |
| regex_compile  | 132 ms                                                 | 131 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.08x faster                                                     |
| tomli_loads          | 2.12 sec                                               | 2.01 sec: 1.05x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 100 ms: 1.01x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 223 us: 1.05x slower                                                     |
| json_loads           | 27.2 us                                                | 29.9 us: 1.10x slower                                                    |
| pickle_pure_python   | 302 us                                                 | 334 us: 1.10x slower                                                     |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                    |
| python_startup_no_site | 7.00 ms                                                | 8.23 ms: 1.18x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 22.2 ms: 1.02x faster                                                    |
| genshi_xml      | 50.5 ms                                                | 50.9 ms: 1.01x slower                                                    |
| django_template | 31.7 ms                                                | 33.1 ms: 1.05x slower                                                    |
| mako            | 10.7 ms                                                | 11.7 ms: 1.09x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                     |
| async_tree_io_tg           | 861 ms                                                 | 624 ms: 1.38x faster                                                     |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                     |
| async_tree_memoization     | 437 ms                                                 | 320 ms: 1.36x faster                                                     |
| async_tree_io              | 838 ms                                                 | 628 ms: 1.34x faster                                                     |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                     |
| deepcopy_memo              | 38.4 us                                                | 29.7 us: 1.29x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                     |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                                    |
| regex_v8                   | 26.9 ms                                                | 22.7 ms: 1.18x faster                                                    |
| go                         | 141 ms                                                 | 119 ms: 1.18x faster                                                     |
| scimark_fft                | 367 ms                                                 | 314 ms: 1.17x faster                                                     |
| regex_effbot               | 3.77 ms                                                | 3.24 ms: 1.16x faster                                                    |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.12x faster                                                     |
| float                      | 78.7 ms                                                | 70.9 ms: 1.11x faster                                                    |
| spectral_norm              | 113 ms                                                 | 103 ms: 1.10x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.62 ms: 1.09x faster                                                    |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.08x faster                                                     |
| async_generators           | 433 ms                                                 | 402 ms: 1.08x faster                                                     |
| pylint                     | 312 ms                                                 | 292 ms: 1.07x faster                                                     |
| telco                      | 8.40 ms                                                | 7.88 ms: 1.07x faster                                                    |
| sqlite_synth               | 2.90 us                                                | 2.75 us: 1.06x faster                                                    |
| richards                   | 47.5 ms                                                | 45.1 ms: 1.06x faster                                                    |
| tomli_loads                | 2.12 sec                                               | 2.01 sec: 1.05x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 61.7 ms: 1.05x faster                                                    |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                                   |
| 2to3                       | 266 ms                                                 | 259 ms: 1.03x faster                                                     |
| richards_super             | 53.7 ms                                                | 52.5 ms: 1.02x faster                                                    |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                                    |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                     |
| genshi_text                | 22.6 ms                                                | 22.2 ms: 1.02x faster                                                    |
| html5lib                   | 63.4 ms                                                | 62.3 ms: 1.02x faster                                                    |
| bpe_tokeniser              | 4.69 sec                                               | 4.61 sec: 1.02x faster                                                   |
| mdp                        | 2.54 sec                                               | 2.50 sec: 1.02x faster                                                   |
| gc_traversal               | 4.90 ms                                                | 4.83 ms: 1.01x faster                                                    |
| regex_compile              | 132 ms                                                 | 131 ms: 1.01x faster                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 100 ms: 1.01x faster                                                     |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                     |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                                    |
| pyflate                    | 470 ms                                                 | 472 ms: 1.01x slower                                                     |
| sqlalchemy_declarative     | 133 ms                                                 | 134 ms: 1.01x slower                                                     |
| genshi_xml                 | 50.5 ms                                                | 50.9 ms: 1.01x slower                                                    |
| scimark_monte_carlo        | 66.8 ms                                                | 68.0 ms: 1.02x slower                                                    |
| shortest_path              | 487 ms                                                 | 503 ms: 1.03x slower                                                     |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                   |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                     |
| connected_components       | 447 ms                                                 | 463 ms: 1.03x slower                                                     |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.04x slower                                                     |
| sympy_integrate            | 19.8 ms                                                | 20.6 ms: 1.04x slower                                                    |
| sympy_expand               | 456 ms                                                 | 474 ms: 1.04x slower                                                     |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                    |
| logging_simple             | 5.65 us                                                | 5.88 us: 1.04x slower                                                    |
| crypto_pyaes               | 74.7 ms                                                | 78.0 ms: 1.04x slower                                                    |
| fannkuch                   | 394 ms                                                 | 411 ms: 1.05x slower                                                     |
| django_template            | 31.7 ms                                                | 33.1 ms: 1.05x slower                                                    |
| unpickle_pure_python       | 213 us                                                 | 223 us: 1.05x slower                                                     |
| sympy_str                  | 273 ms                                                 | 286 ms: 1.05x slower                                                     |
| thrift                     | 800 us                                                 | 841 us: 1.05x slower                                                     |
| nqueens                    | 80.9 ms                                                | 85.2 ms: 1.05x slower                                                    |
| chaos                      | 58.0 ms                                                | 61.2 ms: 1.05x slower                                                    |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                    |
| pprint_safe_repr           | 727 ms                                                 | 768 ms: 1.06x slower                                                     |
| sympy_sum                  | 150 ms                                                 | 159 ms: 1.06x slower                                                     |
| generators                 | 28.8 ms                                                | 30.5 ms: 1.06x slower                                                    |
| pprint_pformat             | 1.48 sec                                               | 1.57 sec: 1.06x slower                                                   |
| logging_format             | 6.23 us                                                | 6.65 us: 1.07x slower                                                    |
| deltablue                  | 3.19 ms                                                | 3.44 ms: 1.08x slower                                                    |
| hexiom                     | 6.08 ms                                                | 6.56 ms: 1.08x slower                                                    |
| sqlalchemy_imperative      | 16.9 ms                                                | 18.3 ms: 1.09x slower                                                    |
| mako                       | 10.7 ms                                                | 11.7 ms: 1.09x slower                                                    |
| json_loads                 | 27.2 us                                                | 29.9 us: 1.10x slower                                                    |
| pickle_pure_python         | 302 us                                                 | 334 us: 1.10x slower                                                     |
| raytrace                   | 262 ms                                                 | 289 ms: 1.10x slower                                                     |
| bench_thread_pool          | 818 us                                                 | 908 us: 1.11x slower                                                     |
| coverage                   | 82.8 ms                                                | 93.7 ms: 1.13x slower                                                    |
| many_optionals             | 857 us                                                 | 974 us: 1.14x slower                                                     |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                    |
| python_startup_no_site     | 7.00 ms                                                | 8.23 ms: 1.18x slower                                                    |
| comprehensions             | 16.5 us                                                | 20.7 us: 1.26x slower                                                    |
| subparsers                 | 15.5 ms                                                | 21.4 ms: 1.39x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 83.4 ms: 3.48x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (9): regex_dna, logging_silent, xml_etree_generate, asyncio_websockets, xml_etree_process, meteor_contest, json, nbody, sphinx
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250325-3.14.0a6+-3374b51-JIT/bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.017x faster

# HPT report

- Reliability score: 66.74% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x
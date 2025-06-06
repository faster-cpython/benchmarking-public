# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: lto_fix
- machine: linux-x86_64
- commit hash: 8891cd2
- commit date: 2025-04-07
- overall geometric mean: 1.064x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 250 ms: 1.06x faster                                                |
| docutils       | 2.58 sec                                               | 2.58 sec: 1.00x faster                                              |
| html5lib       | 63.4 ms                                                | 61.5 ms: 1.03x faster                                               |
| sphinx         | 1.03 sec                                               | 1.00 sec: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 609 ms: 1.41x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 311 ms: 1.41x faster                                                |
| async_tree_io              | 838 ms                                                 | 606 ms: 1.38x faster                                                |
| async_tree_none            | 350 ms                                                 | 255 ms: 1.37x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 246 ms: 1.30x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 484 ms: 1.18x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                |
| async_generators           | 433 ms                                                 | 392 ms: 1.11x faster                                                |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                               |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.3 ms: 1.17x faster                                               |
| nbody          | 87.7 ms                                                | 91.0 ms: 1.04x slower                                               |
| pidigits       | 186 ms                                                 | 194 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.04 ms: 1.24x faster                                               |
| regex_v8       | 26.9 ms                                                | 22.7 ms: 1.19x faster                                               |
| regex_dna      | 220 ms                                                 | 205 ms: 1.07x faster                                                |
| regex_compile  | 132 ms                                                 | 124 ms: 1.06x faster                                                |
| Geometric mean | (ref)                                                  | 1.14x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                |
| tomli_loads          | 2.12 sec                                               | 1.97 sec: 1.07x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 97.8 ms: 1.04x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 58.5 ms: 1.03x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 84.2 ms: 1.03x faster                                               |
| unpickle_pure_python | 213 us                                                 | 211 us: 1.01x faster                                                |
| pickle_pure_python   | 302 us                                                 | 314 us: 1.04x slower                                                |
| json_loads           | 27.2 us                                                | 29.0 us: 1.07x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.12x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                               |
| python_startup_no_site | 7.00 ms                                                | 8.20 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                               |
| genshi_xml      | 50.5 ms                                                | 48.7 ms: 1.04x faster                                               |
| django_template | 31.7 ms                                                | 31.5 ms: 1.00x faster                                               |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                               |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.08x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                                |
| deepcopy                   | 354 us                                                 | 251 us: 1.41x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 609 ms: 1.41x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 311 ms: 1.41x faster                                                |
| async_tree_io              | 838 ms                                                 | 606 ms: 1.38x faster                                                |
| async_tree_none            | 350 ms                                                 | 255 ms: 1.37x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 28.2 us: 1.36x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 246 ms: 1.30x faster                                                |
| go                         | 141 ms                                                 | 109 ms: 1.29x faster                                                |
| regex_effbot               | 3.77 ms                                                | 3.04 ms: 1.24x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.64 us: 1.23x faster                                               |
| regex_v8                   | 26.9 ms                                                | 22.7 ms: 1.19x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 484 ms: 1.18x faster                                                |
| float                      | 78.7 ms                                                | 67.3 ms: 1.17x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                |
| spectral_norm              | 113 ms                                                 | 102 ms: 1.11x faster                                                |
| async_generators           | 433 ms                                                 | 392 ms: 1.11x faster                                                |
| richards                   | 47.5 ms                                                | 43.1 ms: 1.10x faster                                               |
| telco                      | 8.40 ms                                                | 7.68 ms: 1.09x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                |
| dulwich_log                | 64.6 ms                                                | 59.3 ms: 1.09x faster                                               |
| richards_super             | 53.7 ms                                                | 49.5 ms: 1.09x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                              |
| regex_dna                  | 220 ms                                                 | 205 ms: 1.07x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.97 sec: 1.07x faster                                              |
| pyflate                    | 470 ms                                                 | 439 ms: 1.07x faster                                                |
| regex_compile              | 132 ms                                                 | 124 ms: 1.06x faster                                                |
| 2to3                       | 266 ms                                                 | 250 ms: 1.06x faster                                                |
| scimark_fft                | 367 ms                                                 | 346 ms: 1.06x faster                                                |
| scimark_sor                | 122 ms                                                 | 115 ms: 1.06x faster                                                |
| logging_silent             | 101 ns                                                 | 95.5 ns: 1.06x faster                                               |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.06x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                               |
| genshi_xml                 | 50.5 ms                                                | 48.7 ms: 1.04x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.86 ms: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                              |
| logging_simple             | 5.65 us                                                | 5.46 us: 1.04x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 97.8 ms: 1.04x faster                                               |
| sympy_integrate            | 19.8 ms                                                | 19.2 ms: 1.03x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 58.5 ms: 1.03x faster                                               |
| logging_format             | 6.23 us                                                | 6.03 us: 1.03x faster                                               |
| chaos                      | 58.0 ms                                                | 56.2 ms: 1.03x faster                                               |
| pprint_safe_repr           | 727 ms                                                 | 704 ms: 1.03x faster                                                |
| xml_etree_generate         | 86.8 ms                                                | 84.2 ms: 1.03x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.55 sec: 1.03x faster                                              |
| html5lib                   | 63.4 ms                                                | 61.5 ms: 1.03x faster                                               |
| sphinx                     | 1.03 sec                                               | 1.00 sec: 1.03x faster                                              |
| crypto_pyaes               | 74.7 ms                                                | 72.7 ms: 1.03x faster                                               |
| scimark_monte_carlo        | 66.8 ms                                                | 65.1 ms: 1.03x faster                                               |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                |
| gc_traversal               | 4.90 ms                                                | 4.79 ms: 1.02x faster                                               |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                |
| json                       | 5.32 ms                                                | 5.21 ms: 1.02x faster                                               |
| pprint_pformat             | 1.48 sec                                               | 1.45 sec: 1.02x faster                                              |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                               |
| unpickle_pure_python       | 213 us                                                 | 211 us: 1.01x faster                                                |
| raytrace                   | 262 ms                                                 | 259 ms: 1.01x faster                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.01x faster                                                |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                |
| django_template            | 31.7 ms                                                | 31.5 ms: 1.00x faster                                               |
| sympy_expand               | 456 ms                                                 | 454 ms: 1.00x faster                                                |
| docutils                   | 2.58 sec                                               | 2.58 sec: 1.00x faster                                              |
| nqueens                    | 80.9 ms                                                | 81.3 ms: 1.01x slower                                               |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                               |
| connected_components       | 447 ms                                                 | 451 ms: 1.01x slower                                                |
| generators                 | 28.8 ms                                                | 29.2 ms: 1.01x slower                                               |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                                |
| shortest_path              | 487 ms                                                 | 499 ms: 1.03x slower                                                |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.03x slower                                                |
| hexiom                     | 6.08 ms                                                | 6.24 ms: 1.03x slower                                               |
| fannkuch                   | 394 ms                                                 | 406 ms: 1.03x slower                                                |
| coverage                   | 82.8 ms                                                | 85.8 ms: 1.04x slower                                               |
| pickle_pure_python         | 302 us                                                 | 314 us: 1.04x slower                                                |
| nbody                      | 87.7 ms                                                | 91.0 ms: 1.04x slower                                               |
| pidigits                   | 186 ms                                                 | 194 ms: 1.04x slower                                                |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                               |
| deltablue                  | 3.19 ms                                                | 3.33 ms: 1.04x slower                                               |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                               |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                               |
| json_loads                 | 27.2 us                                                | 29.0 us: 1.07x slower                                               |
| bench_thread_pool          | 818 us                                                 | 877 us: 1.07x slower                                                |
| many_optionals             | 857 us                                                 | 929 us: 1.08x slower                                                |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.12x slower                                               |
| python_startup_no_site     | 7.00 ms                                                | 8.20 ms: 1.17x slower                                               |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.1 ms: 3.43x slower                                               |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (2): comprehensions, asyncio_websockets
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250407-3.14.0a6+-8891cd2/bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x
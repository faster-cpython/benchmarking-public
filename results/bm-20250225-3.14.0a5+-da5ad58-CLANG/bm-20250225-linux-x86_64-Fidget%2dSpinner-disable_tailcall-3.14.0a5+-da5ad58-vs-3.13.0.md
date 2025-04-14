# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: linux-x86_64
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.051x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 278 ms: 1.04x slower                                                         |
| docutils       | 2.58 sec                                               | 2.73 sec: 1.06x slower                                                       |
| html5lib       | 63.4 ms                                                | 65.5 ms: 1.03x slower                                                        |
| sphinx         | 1.03 sec                                               | 1.06 sec: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 345 ms: 1.34x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 679 ms: 1.27x faster                                                         |
| async_tree_io              | 838 ms                                                 | 669 ms: 1.25x faster                                                         |
| async_tree_none            | 350 ms                                                 | 285 ms: 1.23x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 357 ms: 1.22x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 276 ms: 1.16x faster                                                         |
| async_generators           | 433 ms                                                 | 417 ms: 1.04x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 555 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 547 ms: 1.01x slower                                                         |
| coroutines                 | 22.2 ms                                                | 25.7 ms: 1.16x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.12x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 78.0 ms: 1.01x faster                                                        |
| pidigits       | 186 ms                                                 | 214 ms: 1.15x slower                                                         |
| nbody          | 87.7 ms                                                | 120 ms: 1.37x slower                                                         |
| Geometric mean | (ref)                                                  | 1.16x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.32 ms: 1.13x faster                                                        |
| regex_dna      | 220 ms                                                 | 196 ms: 1.12x faster                                                         |
| regex_v8       | 26.9 ms                                                | 26.6 ms: 1.01x faster                                                        |
| regex_compile  | 132 ms                                                 | 147 ms: 1.11x slower                                                         |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 163 ms: 1.06x slower                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 108 ms: 1.06x slower                                                         |
| xml_etree_generate   | 86.8 ms                                                | 95.6 ms: 1.10x slower                                                        |
| tomli_loads          | 2.12 sec                                               | 2.36 sec: 1.12x slower                                                       |
| xml_etree_process    | 60.5 ms                                                | 67.5 ms: 1.12x slower                                                        |
| json_loads           | 27.2 us                                                | 31.2 us: 1.15x slower                                                        |
| unpickle_pure_python | 213 us                                                 | 252 us: 1.18x slower                                                         |
| pickle_pure_python   | 302 us                                                 | 361 us: 1.19x slower                                                         |
| json_dumps           | 10.1 ms                                                | 13.2 ms: 1.30x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.14x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.15 ms: 1.02x slower                                                        |
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 25.5 ms: 1.13x slower                                                        |
| django_template | 31.7 ms                                                | 36.4 ms: 1.15x slower                                                        |
| genshi_xml      | 50.5 ms                                                | 60.8 ms: 1.20x slower                                                        |
| mako            | 10.7 ms                                                | 13.0 ms: 1.22x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.18x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 345 ms: 1.34x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 679 ms: 1.27x faster                                                         |
| async_tree_io              | 838 ms                                                 | 669 ms: 1.25x faster                                                         |
| async_tree_none            | 350 ms                                                 | 285 ms: 1.23x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 357 ms: 1.22x faster                                                         |
| deepcopy                   | 354 us                                                 | 291 us: 1.22x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 276 ms: 1.16x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 3.32 ms: 1.13x faster                                                        |
| regex_dna                  | 220 ms                                                 | 196 ms: 1.12x faster                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.54 ms: 1.11x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.94 us: 1.10x faster                                                        |
| pathlib                    | 17.4 ms                                                | 16.0 ms: 1.09x faster                                                        |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.09x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 35.6 us: 1.08x faster                                                        |
| pylint                     | 312 ms                                                 | 292 ms: 1.07x faster                                                         |
| telco                      | 8.40 ms                                                | 7.90 ms: 1.06x faster                                                        |
| coverage                   | 82.8 ms                                                | 79.1 ms: 1.05x faster                                                        |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                       |
| async_generators           | 433 ms                                                 | 417 ms: 1.04x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 555 ms: 1.03x faster                                                         |
| gc_traversal               | 4.90 ms                                                | 4.76 ms: 1.03x faster                                                        |
| shortest_path              | 487 ms                                                 | 478 ms: 1.02x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 26.6 ms: 1.01x faster                                                        |
| float                      | 78.7 ms                                                | 78.0 ms: 1.01x faster                                                        |
| connected_components       | 447 ms                                                 | 443 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 547 ms: 1.01x slower                                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.50 ms: 1.02x slower                                                        |
| python_startup_no_site     | 7.00 ms                                                | 7.15 ms: 1.02x slower                                                        |
| pyflate                    | 470 ms                                                 | 480 ms: 1.02x slower                                                         |
| sphinx                     | 1.03 sec                                               | 1.06 sec: 1.02x slower                                                       |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                        |
| html5lib                   | 63.4 ms                                                | 65.5 ms: 1.03x slower                                                        |
| sqlalchemy_declarative     | 133 ms                                                 | 138 ms: 1.04x slower                                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.87 sec: 1.04x slower                                                       |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                         |
| 2to3                       | 266 ms                                                 | 278 ms: 1.04x slower                                                         |
| sympy_sum                  | 150 ms                                                 | 157 ms: 1.05x slower                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.8 ms: 1.05x slower                                                        |
| dulwich_log                | 64.6 ms                                                | 68.1 ms: 1.05x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.73 sec: 1.06x slower                                                       |
| json                       | 5.32 ms                                                | 5.63 ms: 1.06x slower                                                        |
| thrift                     | 800 us                                                 | 847 us: 1.06x slower                                                         |
| xml_etree_parse            | 154 ms                                                 | 163 ms: 1.06x slower                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 108 ms: 1.06x slower                                                         |
| sympy_str                  | 273 ms                                                 | 290 ms: 1.06x slower                                                         |
| sympy_integrate            | 19.8 ms                                                | 21.1 ms: 1.06x slower                                                        |
| pycparser                  | 1.20 sec                                               | 1.28 sec: 1.07x slower                                                       |
| crypto_pyaes               | 74.7 ms                                                | 80.0 ms: 1.07x slower                                                        |
| richards_super             | 53.7 ms                                                | 57.7 ms: 1.07x slower                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 71.9 ms: 1.08x slower                                                        |
| meteor_contest             | 108 ms                                                 | 117 ms: 1.08x slower                                                         |
| logging_silent             | 101 ns                                                 | 109 ns: 1.08x slower                                                         |
| sqlglot_normalize          | 108 ms                                                 | 117 ms: 1.09x slower                                                         |
| richards                   | 47.5 ms                                                | 51.8 ms: 1.09x slower                                                        |
| sqlglot_optimize           | 53.4 ms                                                | 58.2 ms: 1.09x slower                                                        |
| sympy_expand               | 456 ms                                                 | 498 ms: 1.09x slower                                                         |
| scimark_lu                 | 114 ms                                                 | 125 ms: 1.10x slower                                                         |
| xml_etree_generate         | 86.8 ms                                                | 95.6 ms: 1.10x slower                                                        |
| comprehensions             | 16.5 us                                                | 18.2 us: 1.10x slower                                                        |
| regex_compile              | 132 ms                                                 | 147 ms: 1.11x slower                                                         |
| sqlglot_transpile          | 1.57 ms                                                | 1.75 ms: 1.11x slower                                                        |
| tomli_loads                | 2.12 sec                                               | 2.36 sec: 1.12x slower                                                       |
| xml_etree_process          | 60.5 ms                                                | 67.5 ms: 1.12x slower                                                        |
| bench_thread_pool          | 818 us                                                 | 917 us: 1.12x slower                                                         |
| mdp                        | 2.54 sec                                               | 2.86 sec: 1.12x slower                                                       |
| sqlglot_parse              | 1.26 ms                                                | 1.42 ms: 1.13x slower                                                        |
| genshi_text                | 22.6 ms                                                | 25.5 ms: 1.13x slower                                                        |
| raytrace                   | 262 ms                                                 | 296 ms: 1.13x slower                                                         |
| nqueens                    | 80.9 ms                                                | 92.0 ms: 1.14x slower                                                        |
| pidigits                   | 186 ms                                                 | 214 ms: 1.15x slower                                                         |
| django_template            | 31.7 ms                                                | 36.4 ms: 1.15x slower                                                        |
| json_loads                 | 27.2 us                                                | 31.2 us: 1.15x slower                                                        |
| chaos                      | 58.0 ms                                                | 66.8 ms: 1.15x slower                                                        |
| coroutines                 | 22.2 ms                                                | 25.7 ms: 1.16x slower                                                        |
| many_optionals             | 857 us                                                 | 998 us: 1.16x slower                                                         |
| fannkuch                   | 394 ms                                                 | 461 ms: 1.17x slower                                                         |
| unpickle_pure_python       | 213 us                                                 | 252 us: 1.18x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 361 us: 1.19x slower                                                         |
| scimark_sor                | 122 ms                                                 | 146 ms: 1.19x slower                                                         |
| genshi_xml                 | 50.5 ms                                                | 60.8 ms: 1.20x slower                                                        |
| pprint_safe_repr           | 727 ms                                                 | 876 ms: 1.21x slower                                                         |
| generators                 | 28.8 ms                                                | 34.7 ms: 1.21x slower                                                        |
| pprint_pformat             | 1.48 sec                                               | 1.80 sec: 1.22x slower                                                       |
| mako                       | 10.7 ms                                                | 13.0 ms: 1.22x slower                                                        |
| hexiom                     | 6.08 ms                                                | 7.47 ms: 1.23x slower                                                        |
| deltablue                  | 3.19 ms                                                | 3.94 ms: 1.23x slower                                                        |
| logging_simple             | 5.65 us                                                | 7.16 us: 1.27x slower                                                        |
| logging_format             | 6.23 us                                                | 7.92 us: 1.27x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 13.2 ms: 1.30x slower                                                        |
| nbody                      | 87.7 ms                                                | 120 ms: 1.37x slower                                                         |
| subparsers                 | 15.5 ms                                                | 23.4 ms: 1.51x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 83.5 ms: 3.48x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.07x slower                                                                 |

Benchmark hidden because not significant (3): go, asyncio_websockets, scimark_fft
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.051x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.05x
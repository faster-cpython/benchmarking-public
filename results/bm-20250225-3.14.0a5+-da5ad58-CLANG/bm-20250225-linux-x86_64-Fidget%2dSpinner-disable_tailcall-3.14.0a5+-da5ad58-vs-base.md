# Results vs. base

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: linux-x86_64
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.116x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 278 ms: 1.11x slower                                                         |
| docutils       | 2.57 sec                                                               | 2.73 sec: 1.06x slower                                                       |
| html5lib       | 59.1 ms                                                                | 65.5 ms: 1.11x slower                                                        |
| sphinx         | 985 ms                                                                 | 1.06 sec: 1.07x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.09x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_generators           | 378 ms                                                                 | 417 ms: 1.10x slower                                                         |
| async_tree_io              | 597 ms                                                                 | 669 ms: 1.12x slower                                                         |
| async_tree_memoization_tg  | 307 ms                                                                 | 345 ms: 1.12x slower                                                         |
| async_tree_none            | 251 ms                                                                 | 285 ms: 1.14x slower                                                         |
| async_tree_none_tg         | 241 ms                                                                 | 276 ms: 1.14x slower                                                         |
| async_tree_io_tg           | 594 ms                                                                 | 679 ms: 1.14x slower                                                         |
| async_tree_cpu_io_mixed    | 482 ms                                                                 | 555 ms: 1.15x slower                                                         |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                 | 547 ms: 1.15x slower                                                         |
| async_tree_memoization     | 308 ms                                                                 | 357 ms: 1.16x slower                                                         |
| coroutines                 | 21.8 ms                                                                | 25.7 ms: 1.18x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.13x slower                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                                 | 214 ms: 1.06x slower                                                         |
| float          | 67.6 ms                                                                | 78.0 ms: 1.15x slower                                                        |
| nbody          | 89.3 ms                                                                | 120 ms: 1.35x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.18x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.40 ms                                                                | 3.32 ms: 1.02x faster                                                        |
| regex_dna      | 194 ms                                                                 | 196 ms: 1.01x slower                                                         |
| regex_v8       | 26.1 ms                                                                | 26.6 ms: 1.02x slower                                                        |
| regex_compile  | 124 ms                                                                 | 147 ms: 1.18x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                                 | 163 ms: 1.01x slower                                                         |
| json_loads           | 30.0 us                                                                | 31.2 us: 1.04x slower                                                        |
| xml_etree_iterparse  | 102 ms                                                                 | 108 ms: 1.05x slower                                                         |
| json_dumps           | 12.1 ms                                                                | 13.2 ms: 1.09x slower                                                        |
| xml_etree_generate   | 85.1 ms                                                                | 95.6 ms: 1.12x slower                                                        |
| xml_etree_process    | 58.5 ms                                                                | 67.5 ms: 1.15x slower                                                        |
| pickle_pure_python   | 312 us                                                                 | 361 us: 1.16x slower                                                         |
| unpickle_pure_python | 217 us                                                                 | 252 us: 1.16x slower                                                         |
| tomli_loads          | 1.90 sec                                                               | 2.36 sec: 1.25x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.11x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                                | 7.15 ms: 1.02x slower                                                        |
| python_startup         | 12.7 ms                                                                | 13.1 ms: 1.03x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.7 ms                                                                | 13.0 ms: 1.11x slower                                                        |
| django_template | 30.3 ms                                                                | 36.4 ms: 1.20x slower                                                        |
| genshi_text     | 20.9 ms                                                                | 25.5 ms: 1.22x slower                                                        |
| genshi_xml      | 47.8 ms                                                                | 60.8 ms: 1.27x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.20x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal               | 5.01 ms                                                                | 4.76 ms: 1.05x faster                                                        |
| regex_effbot               | 3.40 ms                                                                | 3.32 ms: 1.02x faster                                                        |
| connected_components       | 447 ms                                                                 | 443 ms: 1.01x faster                                                         |
| coverage                   | 79.8 ms                                                                | 79.1 ms: 1.01x faster                                                        |
| shortest_path              | 480 ms                                                                 | 478 ms: 1.00x faster                                                         |
| xml_etree_parse            | 162 ms                                                                 | 163 ms: 1.01x slower                                                         |
| regex_dna                  | 194 ms                                                                 | 196 ms: 1.01x slower                                                         |
| regex_v8                   | 26.1 ms                                                                | 26.6 ms: 1.02x slower                                                        |
| python_startup_no_site     | 6.99 ms                                                                | 7.15 ms: 1.02x slower                                                        |
| python_startup             | 12.7 ms                                                                | 13.1 ms: 1.03x slower                                                        |
| mdp                        | 2.77 sec                                                               | 2.86 sec: 1.03x slower                                                       |
| json                       | 5.45 ms                                                                | 5.63 ms: 1.03x slower                                                        |
| json_loads                 | 30.0 us                                                                | 31.2 us: 1.04x slower                                                        |
| bench_mp_pool              | 80.0 ms                                                                | 83.5 ms: 1.04x slower                                                        |
| xml_etree_iterparse        | 102 ms                                                                 | 108 ms: 1.05x slower                                                         |
| meteor_contest             | 111 ms                                                                 | 117 ms: 1.06x slower                                                         |
| pathlib                    | 15.1 ms                                                                | 16.0 ms: 1.06x slower                                                        |
| docutils                   | 2.57 sec                                                               | 2.73 sec: 1.06x slower                                                       |
| sqlite_synth               | 2.65 us                                                                | 2.81 us: 1.06x slower                                                        |
| pidigits                   | 202 ms                                                                 | 214 ms: 1.06x slower                                                         |
| sphinx                     | 985 ms                                                                 | 1.06 sec: 1.07x slower                                                       |
| telco                      | 7.31 ms                                                                | 7.90 ms: 1.08x slower                                                        |
| pylint                     | 270 ms                                                                 | 292 ms: 1.08x slower                                                         |
| many_optionals             | 917 us                                                                 | 998 us: 1.09x slower                                                         |
| json_dumps                 | 12.1 ms                                                                | 13.2 ms: 1.09x slower                                                        |
| dulwich_log                | 62.2 ms                                                                | 68.1 ms: 1.09x slower                                                        |
| sqlalchemy_declarative     | 125 ms                                                                 | 138 ms: 1.10x slower                                                         |
| async_generators           | 378 ms                                                                 | 417 ms: 1.10x slower                                                         |
| scimark_sparse_mat_mult    | 4.11 ms                                                                | 4.54 ms: 1.10x slower                                                        |
| sqlalchemy_imperative      | 16.1 ms                                                                | 17.8 ms: 1.11x slower                                                        |
| html5lib                   | 59.1 ms                                                                | 65.5 ms: 1.11x slower                                                        |
| sympy_sum                  | 142 ms                                                                 | 157 ms: 1.11x slower                                                         |
| 2to3                       | 250 ms                                                                 | 278 ms: 1.11x slower                                                         |
| sympy_integrate            | 18.9 ms                                                                | 21.1 ms: 1.11x slower                                                        |
| mako                       | 11.7 ms                                                                | 13.0 ms: 1.11x slower                                                        |
| crypto_pyaes               | 71.9 ms                                                                | 80.0 ms: 1.11x slower                                                        |
| bench_thread_pool          | 821 us                                                                 | 917 us: 1.12x slower                                                         |
| async_tree_io              | 597 ms                                                                 | 669 ms: 1.12x slower                                                         |
| bpe_tokeniser              | 4.35 sec                                                               | 4.87 sec: 1.12x slower                                                       |
| async_tree_memoization_tg  | 307 ms                                                                 | 345 ms: 1.12x slower                                                         |
| sqlglot_optimize           | 51.8 ms                                                                | 58.2 ms: 1.12x slower                                                        |
| xml_etree_generate         | 85.1 ms                                                                | 95.6 ms: 1.12x slower                                                        |
| sympy_str                  | 258 ms                                                                 | 290 ms: 1.12x slower                                                         |
| sympy_expand               | 441 ms                                                                 | 498 ms: 1.13x slower                                                         |
| scimark_lu                 | 110 ms                                                                 | 125 ms: 1.14x slower                                                         |
| async_tree_none            | 251 ms                                                                 | 285 ms: 1.14x slower                                                         |
| thrift                     | 742 us                                                                 | 847 us: 1.14x slower                                                         |
| sqlglot_normalize          | 103 ms                                                                 | 117 ms: 1.14x slower                                                         |
| async_tree_none_tg         | 241 ms                                                                 | 276 ms: 1.14x slower                                                         |
| async_tree_io_tg           | 594 ms                                                                 | 679 ms: 1.14x slower                                                         |
| pyflate                    | 420 ms                                                                 | 480 ms: 1.14x slower                                                         |
| typing_runtime_protocols   | 146 us                                                                 | 167 us: 1.14x slower                                                         |
| pycparser                  | 1.12 sec                                                               | 1.28 sec: 1.14x slower                                                       |
| raytrace                   | 259 ms                                                                 | 296 ms: 1.14x slower                                                         |
| async_tree_cpu_io_mixed    | 482 ms                                                                 | 555 ms: 1.15x slower                                                         |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                 | 547 ms: 1.15x slower                                                         |
| float                      | 67.6 ms                                                                | 78.0 ms: 1.15x slower                                                        |
| xml_etree_process          | 58.5 ms                                                                | 67.5 ms: 1.15x slower                                                        |
| pickle_pure_python         | 312 us                                                                 | 361 us: 1.16x slower                                                         |
| async_tree_memoization     | 308 ms                                                                 | 357 ms: 1.16x slower                                                         |
| sqlglot_transpile          | 1.51 ms                                                                | 1.75 ms: 1.16x slower                                                        |
| unpickle_pure_python       | 217 us                                                                 | 252 us: 1.16x slower                                                         |
| scimark_monte_carlo        | 61.8 ms                                                                | 71.9 ms: 1.16x slower                                                        |
| fannkuch                   | 395 ms                                                                 | 461 ms: 1.17x slower                                                         |
| subparsers                 | 19.9 ms                                                                | 23.4 ms: 1.17x slower                                                        |
| comprehensions             | 15.5 us                                                                | 18.2 us: 1.18x slower                                                        |
| sqlglot_parse              | 1.21 ms                                                                | 1.42 ms: 1.18x slower                                                        |
| coroutines                 | 21.8 ms                                                                | 25.7 ms: 1.18x slower                                                        |
| deepcopy_reduce            | 2.50 us                                                                | 2.94 us: 1.18x slower                                                        |
| regex_compile              | 124 ms                                                                 | 147 ms: 1.18x slower                                                         |
| deepcopy                   | 247 us                                                                 | 291 us: 1.18x slower                                                         |
| pprint_safe_repr           | 737 ms                                                                 | 876 ms: 1.19x slower                                                         |
| pprint_pformat             | 1.50 sec                                                               | 1.80 sec: 1.20x slower                                                       |
| deepcopy_memo              | 29.7 us                                                                | 35.6 us: 1.20x slower                                                        |
| django_template            | 30.3 ms                                                                | 36.4 ms: 1.20x slower                                                        |
| logging_silent             | 90.3 ns                                                                | 109 ns: 1.21x slower                                                         |
| richards_super             | 47.6 ms                                                                | 57.7 ms: 1.21x slower                                                        |
| genshi_text                | 20.9 ms                                                                | 25.5 ms: 1.22x slower                                                        |
| chaos                      | 54.6 ms                                                                | 66.8 ms: 1.22x slower                                                        |
| nqueens                    | 73.9 ms                                                                | 92.0 ms: 1.24x slower                                                        |
| go                         | 113 ms                                                                 | 140 ms: 1.24x slower                                                         |
| tomli_loads                | 1.90 sec                                                               | 2.36 sec: 1.25x slower                                                       |
| generators                 | 27.9 ms                                                                | 34.7 ms: 1.25x slower                                                        |
| scimark_fft                | 295 ms                                                                 | 370 ms: 1.26x slower                                                         |
| hexiom                     | 5.94 ms                                                                | 7.47 ms: 1.26x slower                                                        |
| spectral_norm              | 82.3 ms                                                                | 104 ms: 1.27x slower                                                         |
| richards                   | 40.8 ms                                                                | 51.8 ms: 1.27x slower                                                        |
| genshi_xml                 | 47.8 ms                                                                | 60.8 ms: 1.27x slower                                                        |
| deltablue                  | 2.98 ms                                                                | 3.94 ms: 1.32x slower                                                        |
| logging_simple             | 5.37 us                                                                | 7.16 us: 1.33x slower                                                        |
| logging_format             | 5.94 us                                                                | 7.92 us: 1.33x slower                                                        |
| scimark_sor                | 109 ms                                                                 | 146 ms: 1.34x slower                                                         |
| nbody                      | 89.3 ms                                                                | 120 ms: 1.35x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.13x slower                                                                 |

Benchmark hidden because not significant (3): create_gc_cycles, k_core, asyncio_websockets
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.116x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: 1.02x
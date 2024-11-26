# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_dwarf
- machine: linux-x86_64
- commit hash: 1ce520b
- commit date: 2024-11-15
- overall geometric mean: 1.002x faster
- HPT reliability: 51.06%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 276 ms: 1.04x slower                                                 |
| docutils       | 2.59 sec                                               | 3.00 sec: 1.16x slower                                               |
| html5lib       | 64.2 ms                                                | 66.4 ms: 1.04x slower                                                |
| sphinx         | 1.03 sec                                               | 1.17 sec: 1.14x slower                                               |
| Geometric mean | (ref)                                                  | 1.09x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 375 ms: 1.24x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 413 ms: 1.07x faster                                                 |
| async_tree_none            | 351 ms                                                 | 330 ms: 1.06x faster                                                 |
| coroutines                 | 22.7 ms                                                | 22.5 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 561 ms: 1.03x slower                                                 |
| async_generators           | 436 ms                                                 | 454 ms: 1.04x slower                                                 |
| async_tree_io_tg           | 857 ms                                                 | 964 ms: 1.13x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 83.5 ms: 1.04x faster                                                |
| float          | 79.2 ms                                                | 76.4 ms: 1.04x faster                                                |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.5 ms: 1.07x faster                                                |
| regex_dna      | 218 ms                                                 | 216 ms: 1.01x faster                                                 |
| regex_effbot   | 3.73 ms                                                | 3.79 ms: 1.02x slower                                                |
| regex_compile  | 132 ms                                                 | 138 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_process    | 60.6 ms                                                | 54.5 ms: 1.11x faster                                                |
| tomli_loads          | 2.14 sec                                               | 1.93 sec: 1.11x faster                                               |
| xml_etree_generate   | 86.7 ms                                                | 78.6 ms: 1.10x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 99.9 ms: 1.01x faster                                                |
| json_loads           | 27.2 us                                                | 26.9 us: 1.01x faster                                                |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.01x slower                                                 |
| json_dumps           | 10.6 ms                                                | 10.7 ms: 1.02x slower                                                |
| pickle_pure_python   | 310 us                                                 | 321 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.11 ms: 1.02x slower                                                |
| python_startup         | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.3 ms: 1.07x faster                                                |
| django_template | 35.2 ms                                                | 33.4 ms: 1.05x faster                                                |
| genshi_text     | 23.5 ms                                                | 26.3 ms: 1.12x slower                                                |
| genshi_xml      | 50.9 ms                                                | 59.7 ms: 1.17x slower                                                |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 29.2 us: 1.34x faster                                                |
| deepcopy                   | 358 us                                                 | 271 us: 1.32x faster                                                 |
| richards                   | 48.7 ms                                                | 38.9 ms: 1.25x faster                                                |
| async_tree_memoization_tg  | 464 ms                                                 | 375 ms: 1.24x faster                                                 |
| richards_super             | 54.9 ms                                                | 45.8 ms: 1.20x faster                                                |
| deepcopy_reduce            | 3.20 us                                                | 2.74 us: 1.17x faster                                                |
| telco                      | 8.54 ms                                                | 7.61 ms: 1.12x faster                                                |
| scimark_fft                | 364 ms                                                 | 326 ms: 1.12x faster                                                 |
| xml_etree_process          | 60.6 ms                                                | 54.5 ms: 1.11x faster                                                |
| go                         | 144 ms                                                 | 129 ms: 1.11x faster                                                 |
| tomli_loads                | 2.14 sec                                               | 1.93 sec: 1.11x faster                                               |
| xml_etree_generate         | 86.7 ms                                                | 78.6 ms: 1.10x faster                                                |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.57 ms: 1.10x faster                                                |
| crypto_pyaes               | 75.3 ms                                                | 68.9 ms: 1.09x faster                                                |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                |
| bpe_tokeniser              | 4.75 sec                                               | 4.39 sec: 1.08x faster                                               |
| json                       | 5.36 ms                                                | 4.97 ms: 1.08x faster                                                |
| mako                       | 11.1 ms                                                | 10.3 ms: 1.07x faster                                                |
| fannkuch                   | 404 ms                                                 | 377 ms: 1.07x faster                                                 |
| regex_v8                   | 26.2 ms                                                | 24.5 ms: 1.07x faster                                                |
| async_tree_memoization     | 442 ms                                                 | 413 ms: 1.07x faster                                                 |
| async_tree_none            | 351 ms                                                 | 330 ms: 1.06x faster                                                 |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                                 |
| scimark_monte_carlo        | 67.4 ms                                                | 63.9 ms: 1.06x faster                                                |
| pyflate                    | 471 ms                                                 | 448 ms: 1.05x faster                                                 |
| django_template            | 35.2 ms                                                | 33.4 ms: 1.05x faster                                                |
| scimark_sor                | 124 ms                                                 | 118 ms: 1.04x faster                                                 |
| connected_components       | 444 ms                                                 | 425 ms: 1.04x faster                                                 |
| nbody                      | 87.0 ms                                                | 83.5 ms: 1.04x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                               |
| float                      | 79.2 ms                                                | 76.4 ms: 1.04x faster                                                |
| logging_format             | 6.40 us                                                | 6.21 us: 1.03x faster                                                |
| thrift                     | 809 us                                                 | 787 us: 1.03x faster                                                 |
| pprint_safe_repr           | 728 ms                                                 | 713 ms: 1.02x faster                                                 |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                 |
| logging_simple             | 5.72 us                                                | 5.63 us: 1.02x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 99.9 ms: 1.01x faster                                                |
| shortest_path              | 481 ms                                                 | 474 ms: 1.01x faster                                                 |
| json_loads                 | 27.2 us                                                | 26.9 us: 1.01x faster                                                |
| logging_silent             | 102 ns                                                 | 101 ns: 1.01x faster                                                 |
| regex_dna                  | 218 ms                                                 | 216 ms: 1.01x faster                                                 |
| coroutines                 | 22.7 ms                                                | 22.5 ms: 1.01x faster                                                |
| gc_traversal               | 4.37 ms                                                | 4.36 ms: 1.00x faster                                                |
| mdp                        | 2.72 sec                                               | 2.73 sec: 1.00x slower                                               |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| unpickle_pure_python       | 216 us                                                 | 217 us: 1.01x slower                                                 |
| chaos                      | 58.1 ms                                                | 58.6 ms: 1.01x slower                                                |
| typing_runtime_protocols   | 165 us                                                 | 167 us: 1.01x slower                                                 |
| deltablue                  | 3.23 ms                                                | 3.27 ms: 1.01x slower                                                |
| regex_effbot               | 3.73 ms                                                | 3.79 ms: 1.02x slower                                                |
| json_dumps                 | 10.6 ms                                                | 10.7 ms: 1.02x slower                                                |
| python_startup_no_site     | 6.96 ms                                                | 7.11 ms: 1.02x slower                                                |
| python_startup             | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 561 ms: 1.03x slower                                                 |
| raytrace                   | 267 ms                                                 | 275 ms: 1.03x slower                                                 |
| pickle_pure_python         | 310 us                                                 | 321 us: 1.03x slower                                                 |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.03x slower                                                |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                |
| html5lib                   | 64.2 ms                                                | 66.4 ms: 1.04x slower                                                |
| 2to3                       | 267 ms                                                 | 276 ms: 1.04x slower                                                 |
| sqlglot_normalize          | 108 ms                                                 | 112 ms: 1.04x slower                                                 |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.8 ms: 1.04x slower                                                |
| async_generators           | 436 ms                                                 | 454 ms: 1.04x slower                                                 |
| regex_compile              | 132 ms                                                 | 138 ms: 1.04x slower                                                 |
| dulwich_log                | 64.3 ms                                                | 68.0 ms: 1.06x slower                                                |
| sqlglot_transpile          | 1.58 ms                                                | 1.68 ms: 1.06x slower                                                |
| sqlglot_optimize           | 53.7 ms                                                | 57.4 ms: 1.07x slower                                                |
| bench_thread_pool          | 822 us                                                 | 886 us: 1.08x slower                                                 |
| sympy_expand               | 463 ms                                                 | 508 ms: 1.10x slower                                                 |
| sympy_str                  | 275 ms                                                 | 302 ms: 1.10x slower                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 147 ms: 1.10x slower                                                 |
| genshi_text                | 23.5 ms                                                | 26.3 ms: 1.12x slower                                                |
| create_gc_cycles           | 2.41 ms                                                | 2.70 ms: 1.12x slower                                                |
| async_tree_io_tg           | 857 ms                                                 | 964 ms: 1.13x slower                                                 |
| hexiom                     | 6.16 ms                                                | 6.98 ms: 1.13x slower                                                |
| sphinx                     | 1.03 sec                                               | 1.17 sec: 1.14x slower                                               |
| nqueens                    | 78.4 ms                                                | 89.3 ms: 1.14x slower                                                |
| sympy_sum                  | 150 ms                                                 | 173 ms: 1.15x slower                                                 |
| docutils                   | 2.59 sec                                               | 3.00 sec: 1.16x slower                                               |
| sympy_integrate            | 19.9 ms                                                | 23.2 ms: 1.17x slower                                                |
| genshi_xml                 | 50.9 ms                                                | 59.7 ms: 1.17x slower                                                |
| generators                 | 29.0 ms                                                | 34.3 ms: 1.18x slower                                                |
| pylint                     | 313 ms                                                 | 376 ms: 1.20x slower                                                 |
| k_core                     | 2.35 sec                                               | 3.56 sec: 1.51x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 85.2 ms: 3.55x slower                                                |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (8): scimark_lu, async_tree_cpu_io_mixed, pprint_pformat, coverage, spectral_norm, asyncio_websockets, async_tree_none_tg, async_tree_io
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241115-3.14.0a1+-1ce520b-JIT/bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.002x faster
# HPT report

- Reliability score: 51.06% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.13x
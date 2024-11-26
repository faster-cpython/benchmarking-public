# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_dwarf
- machine: linux-x86_64
- commit hash: 68dd6e6
- commit date: 2024-11-15
- overall geometric mean: 1.002x slower
- HPT reliability: 60.88%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 282 ms: 1.06x slower                                                 |
| docutils       | 2.59 sec                                               | 2.95 sec: 1.14x slower                                               |
| html5lib       | 64.2 ms                                                | 67.6 ms: 1.05x slower                                                |
| sphinx         | 1.03 sec                                               | 1.18 sec: 1.14x slower                                               |
| Geometric mean | (ref)                                                  | 1.10x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.06x faster                                                 |
| async_tree_none            | 351 ms                                                 | 329 ms: 1.06x faster                                                 |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 566 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 553 ms: 1.01x slower                                                 |
| async_generators           | 436 ms                                                 | 458 ms: 1.05x slower                                                 |
| async_tree_io_tg           | 857 ms                                                 | 977 ms: 1.14x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (4): async_tree_none_tg, coroutines, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 83.2 ms: 1.05x faster                                                |
| float          | 79.2 ms                                                | 76.5 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.58 ms: 1.04x faster                                                |
| regex_dna      | 218 ms                                                 | 210 ms: 1.04x faster                                                 |
| regex_v8       | 26.2 ms                                                | 25.3 ms: 1.04x faster                                                |
| regex_compile  | 132 ms                                                 | 141 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.94 sec: 1.10x faster                                               |
| xml_etree_generate   | 86.7 ms                                                | 79.1 ms: 1.10x faster                                                |
| xml_etree_process    | 60.6 ms                                                | 56.0 ms: 1.08x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                 |
| json_loads           | 27.2 us                                                | 26.5 us: 1.03x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 101 ms: 1.01x faster                                                 |
| unpickle_pure_python | 216 us                                                 | 219 us: 1.02x slower                                                 |
| pickle_pure_python   | 310 us                                                 | 318 us: 1.02x slower                                                 |
| json_dumps           | 10.6 ms                                                | 10.9 ms: 1.03x slower                                                |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.13 ms: 1.02x slower                                                |
| python_startup         | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.1 ms: 1.09x faster                                                |
| django_template | 35.2 ms                                                | 33.7 ms: 1.04x faster                                                |
| genshi_text     | 23.5 ms                                                | 24.8 ms: 1.05x slower                                                |
| genshi_xml      | 50.9 ms                                                | 59.0 ms: 1.16x slower                                                |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 268 us: 1.34x faster                                                 |
| deepcopy_memo              | 39.1 us                                                | 29.5 us: 1.32x faster                                                |
| richards                   | 48.7 ms                                                | 39.8 ms: 1.22x faster                                                |
| richards_super             | 54.9 ms                                                | 44.9 ms: 1.22x faster                                                |
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                                 |
| deepcopy_reduce            | 3.20 us                                                | 2.72 us: 1.18x faster                                                |
| scimark_fft                | 364 ms                                                 | 320 ms: 1.14x faster                                                 |
| telco                      | 8.54 ms                                                | 7.64 ms: 1.12x faster                                                |
| tomli_loads                | 2.14 sec                                               | 1.94 sec: 1.10x faster                                               |
| xml_etree_generate         | 86.7 ms                                                | 79.1 ms: 1.10x faster                                                |
| crypto_pyaes               | 75.3 ms                                                | 68.8 ms: 1.09x faster                                                |
| mako                       | 11.1 ms                                                | 10.1 ms: 1.09x faster                                                |
| xml_etree_process          | 60.6 ms                                                | 56.0 ms: 1.08x faster                                                |
| go                         | 144 ms                                                 | 133 ms: 1.08x faster                                                 |
| json                       | 5.36 ms                                                | 4.97 ms: 1.08x faster                                                |
| pathlib                    | 17.5 ms                                                | 16.3 ms: 1.07x faster                                                |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.06x faster                                                 |
| async_tree_none            | 351 ms                                                 | 329 ms: 1.06x faster                                                 |
| mdp                        | 2.72 sec                                               | 2.57 sec: 1.06x faster                                               |
| logging_format             | 6.40 us                                                | 6.06 us: 1.06x faster                                                |
| fannkuch                   | 404 ms                                                 | 383 ms: 1.05x faster                                                 |
| bpe_tokeniser              | 4.75 sec                                               | 4.51 sec: 1.05x faster                                               |
| scimark_monte_carlo        | 67.4 ms                                                | 64.3 ms: 1.05x faster                                                |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                 |
| nbody                      | 87.0 ms                                                | 83.2 ms: 1.05x faster                                                |
| logging_silent             | 102 ns                                                 | 97.3 ns: 1.05x faster                                                |
| logging_simple             | 5.72 us                                                | 5.48 us: 1.04x faster                                                |
| django_template            | 35.2 ms                                                | 33.7 ms: 1.04x faster                                                |
| regex_effbot               | 3.73 ms                                                | 3.58 ms: 1.04x faster                                                |
| regex_dna                  | 218 ms                                                 | 210 ms: 1.04x faster                                                 |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.86 ms: 1.04x faster                                                |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                                 |
| regex_v8                   | 26.2 ms                                                | 25.3 ms: 1.04x faster                                                |
| pyflate                    | 471 ms                                                 | 455 ms: 1.04x faster                                                 |
| float                      | 79.2 ms                                                | 76.5 ms: 1.03x faster                                                |
| scimark_sor                | 124 ms                                                 | 120 ms: 1.03x faster                                                 |
| pprint_pformat             | 1.49 sec                                               | 1.45 sec: 1.03x faster                                               |
| json_loads                 | 27.2 us                                                | 26.5 us: 1.03x faster                                                |
| pprint_safe_repr           | 728 ms                                                 | 711 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 566 ms: 1.02x faster                                                 |
| thrift                     | 809 us                                                 | 795 us: 1.02x faster                                                 |
| connected_components       | 444 ms                                                 | 436 ms: 1.02x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 101 ms: 1.01x faster                                                 |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.00x faster                                                 |
| typing_runtime_protocols   | 165 us                                                 | 166 us: 1.01x slower                                                 |
| chaos                      | 58.1 ms                                                | 58.8 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 553 ms: 1.01x slower                                                 |
| deltablue                  | 3.23 ms                                                | 3.28 ms: 1.02x slower                                                |
| unpickle_pure_python       | 216 us                                                 | 219 us: 1.02x slower                                                 |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                                 |
| python_startup_no_site     | 6.96 ms                                                | 7.13 ms: 1.02x slower                                                |
| pickle_pure_python         | 310 us                                                 | 318 us: 1.02x slower                                                 |
| raytrace                   | 267 ms                                                 | 274 ms: 1.03x slower                                                 |
| json_dumps                 | 10.6 ms                                                | 10.9 ms: 1.03x slower                                                |
| python_startup             | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.6 ms: 1.03x slower                                                |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.04x slower                                                |
| async_generators           | 436 ms                                                 | 458 ms: 1.05x slower                                                 |
| html5lib                   | 64.2 ms                                                | 67.6 ms: 1.05x slower                                                |
| genshi_text                | 23.5 ms                                                | 24.8 ms: 1.05x slower                                                |
| 2to3                       | 267 ms                                                 | 282 ms: 1.06x slower                                                 |
| dulwich_log                | 64.3 ms                                                | 68.2 ms: 1.06x slower                                                |
| regex_compile              | 132 ms                                                 | 141 ms: 1.06x slower                                                 |
| sqlglot_transpile          | 1.58 ms                                                | 1.69 ms: 1.07x slower                                                |
| comprehensions             | 16.5 us                                                | 17.6 us: 1.07x slower                                                |
| sqlglot_normalize          | 108 ms                                                 | 116 ms: 1.08x slower                                                 |
| gc_traversal               | 4.37 ms                                                | 4.73 ms: 1.08x slower                                                |
| bench_thread_pool          | 822 us                                                 | 889 us: 1.08x slower                                                 |
| sympy_expand               | 463 ms                                                 | 506 ms: 1.09x slower                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 148 ms: 1.11x slower                                                 |
| sympy_str                  | 275 ms                                                 | 304 ms: 1.11x slower                                                 |
| create_gc_cycles           | 2.41 ms                                                | 2.70 ms: 1.12x slower                                                |
| sqlglot_optimize           | 53.7 ms                                                | 60.5 ms: 1.13x slower                                                |
| nqueens                    | 78.4 ms                                                | 88.7 ms: 1.13x slower                                                |
| docutils                   | 2.59 sec                                               | 2.95 sec: 1.14x slower                                               |
| sphinx                     | 1.03 sec                                               | 1.18 sec: 1.14x slower                                               |
| async_tree_io_tg           | 857 ms                                                 | 977 ms: 1.14x slower                                                 |
| hexiom                     | 6.16 ms                                                | 7.10 ms: 1.15x slower                                                |
| genshi_xml                 | 50.9 ms                                                | 59.0 ms: 1.16x slower                                                |
| sympy_sum                  | 150 ms                                                 | 176 ms: 1.17x slower                                                 |
| sympy_integrate            | 19.9 ms                                                | 23.6 ms: 1.19x slower                                                |
| pylint                     | 313 ms                                                 | 383 ms: 1.22x slower                                                 |
| generators                 | 29.0 ms                                                | 35.9 ms: 1.24x slower                                                |
| k_core                     | 2.35 sec                                               | 3.61 sec: 1.53x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 85.2 ms: 3.55x slower                                                |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                         |

Benchmark hidden because not significant (8): async_tree_none_tg, coroutines, asyncio_websockets, pidigits, shortest_path, pycparser, coverage, async_tree_io
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241115-3.14.0a1+-68dd6e6-JIT/bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.002x slower
# HPT report

- Reliability score: 60.88% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x
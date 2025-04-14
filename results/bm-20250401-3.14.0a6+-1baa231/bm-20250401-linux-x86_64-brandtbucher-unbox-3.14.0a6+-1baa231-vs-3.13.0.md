# Results vs. 3.13.0

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: 1baa231
- commit date: 2025-04-01
- overall geometric mean: 1.029x faster
- HPT reliability: 86.81%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                          |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                        |
| html5lib       | 63.4 ms                                                | 62.9 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 323 ms: 1.43x faster                                          |
| async_tree_io_tg           | 861 ms                                                 | 626 ms: 1.37x faster                                          |
| async_tree_memoization     | 437 ms                                                 | 321 ms: 1.36x faster                                          |
| async_tree_io              | 838 ms                                                 | 630 ms: 1.33x faster                                          |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                          |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                          |
| async_generators           | 433 ms                                                 | 401 ms: 1.08x faster                                          |
| coroutines                 | 22.2 ms                                                | 21.5 ms: 1.03x faster                                         |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 78.7 ms                                                | 74.8 ms: 1.05x faster                                         |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                          |
| nbody          | 87.7 ms                                                | 98.5 ms: 1.12x slower                                         |
| Geometric mean | (ref)                                                  | 1.02x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.9 ms: 1.17x faster                                         |
| regex_effbot   | 3.77 ms                                                | 3.24 ms: 1.16x faster                                         |
| regex_compile  | 132 ms                                                 | 131 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                  |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.83 sec: 1.15x faster                                        |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                          |
| xml_etree_iterparse  | 101 ms                                                 | 99.7 ms: 1.02x faster                                         |
| xml_etree_generate   | 86.8 ms                                                | 85.5 ms: 1.02x faster                                         |
| xml_etree_process    | 60.5 ms                                                | 60.0 ms: 1.01x faster                                         |
| unpickle_pure_python | 213 us                                                 | 225 us: 1.06x slower                                          |
| pickle_pure_python   | 302 us                                                 | 325 us: 1.08x slower                                          |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.15x slower                                         |
| json_loads           | 27.2 us                                                | 32.0 us: 1.18x slower                                         |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                         |
| python_startup_no_site | 7.00 ms                                                | 8.19 ms: 1.17x slower                                         |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.8 ms: 1.04x faster                                         |
| django_template | 31.7 ms                                                | 32.5 ms: 1.03x slower                                         |
| mako            | 10.7 ms                                                | 11.9 ms: 1.12x slower                                         |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                  |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.26 sec: 2.02x faster                                        |
| async_tree_memoization_tg  | 463 ms                                                 | 323 ms: 1.43x faster                                          |
| async_tree_io_tg           | 861 ms                                                 | 626 ms: 1.37x faster                                          |
| async_tree_memoization     | 437 ms                                                 | 321 ms: 1.36x faster                                          |
| deepcopy                   | 354 us                                                 | 263 us: 1.35x faster                                          |
| async_tree_io              | 838 ms                                                 | 630 ms: 1.33x faster                                          |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                          |
| deepcopy_memo              | 38.4 us                                                | 30.7 us: 1.25x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                          |
| deepcopy_reduce            | 3.24 us                                                | 2.76 us: 1.17x faster                                         |
| regex_v8                   | 26.9 ms                                                | 22.9 ms: 1.17x faster                                         |
| regex_effbot               | 3.77 ms                                                | 3.24 ms: 1.16x faster                                         |
| go                         | 141 ms                                                 | 121 ms: 1.16x faster                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                          |
| tomli_loads                | 2.12 sec                                               | 1.83 sec: 1.15x faster                                        |
| spectral_norm              | 113 ms                                                 | 98.2 ms: 1.15x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                          |
| pylint                     | 312 ms                                                 | 281 ms: 1.11x faster                                          |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                          |
| dulwich_log                | 64.6 ms                                                | 59.6 ms: 1.08x faster                                         |
| async_generators           | 433 ms                                                 | 401 ms: 1.08x faster                                          |
| telco                      | 8.40 ms                                                | 7.95 ms: 1.06x faster                                         |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                         |
| float                      | 78.7 ms                                                | 74.8 ms: 1.05x faster                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.48 sec: 1.05x faster                                        |
| genshi_text                | 22.6 ms                                                | 21.8 ms: 1.04x faster                                         |
| coroutines                 | 22.2 ms                                                | 21.5 ms: 1.03x faster                                         |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                        |
| richards_super             | 53.7 ms                                                | 52.2 ms: 1.03x faster                                         |
| richards                   | 47.5 ms                                                | 46.2 ms: 1.03x faster                                         |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                          |
| sqlite_synth               | 2.90 us                                                | 2.86 us: 1.02x faster                                         |
| xml_etree_iterparse        | 101 ms                                                 | 99.7 ms: 1.02x faster                                         |
| xml_etree_generate         | 86.8 ms                                                | 85.5 ms: 1.02x faster                                         |
| generators                 | 28.8 ms                                                | 28.4 ms: 1.01x faster                                         |
| chaos                      | 58.0 ms                                                | 57.5 ms: 1.01x faster                                         |
| xml_etree_process          | 60.5 ms                                                | 60.0 ms: 1.01x faster                                         |
| regex_compile              | 132 ms                                                 | 131 ms: 1.01x faster                                          |
| html5lib                   | 63.4 ms                                                | 62.9 ms: 1.01x faster                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.00x faster                                          |
| hexiom                     | 6.08 ms                                                | 6.09 ms: 1.00x slower                                         |
| sympy_integrate            | 19.8 ms                                                | 19.9 ms: 1.01x slower                                         |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                          |
| logging_format             | 6.23 us                                                | 6.28 us: 1.01x slower                                         |
| logging_simple             | 5.65 us                                                | 5.70 us: 1.01x slower                                         |
| connected_components       | 447 ms                                                 | 451 ms: 1.01x slower                                          |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                          |
| scimark_sor                | 122 ms                                                 | 124 ms: 1.01x slower                                          |
| coverage                   | 82.8 ms                                                | 83.9 ms: 1.01x slower                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.2 ms: 1.02x slower                                         |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                        |
| shortest_path              | 487 ms                                                 | 498 ms: 1.02x slower                                          |
| sympy_expand               | 456 ms                                                 | 467 ms: 1.02x slower                                          |
| django_template            | 31.7 ms                                                | 32.5 ms: 1.03x slower                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 68.7 ms: 1.03x slower                                         |
| nqueens                    | 80.9 ms                                                | 83.2 ms: 1.03x slower                                         |
| typing_runtime_protocols   | 160 us                                                 | 165 us: 1.03x slower                                          |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                          |
| gc_traversal               | 4.90 ms                                                | 5.07 ms: 1.04x slower                                         |
| json                       | 5.32 ms                                                | 5.52 ms: 1.04x slower                                         |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                         |
| pprint_safe_repr           | 727 ms                                                 | 759 ms: 1.04x slower                                          |
| pprint_pformat             | 1.48 sec                                               | 1.55 sec: 1.05x slower                                        |
| comprehensions             | 16.5 us                                                | 17.4 us: 1.05x slower                                         |
| unpickle_pure_python       | 213 us                                                 | 225 us: 1.06x slower                                          |
| scimark_fft                | 367 ms                                                 | 394 ms: 1.08x slower                                          |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.08x slower                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.43 ms: 1.08x slower                                         |
| bench_thread_pool          | 818 us                                                 | 889 us: 1.09x slower                                          |
| fannkuch                   | 394 ms                                                 | 430 ms: 1.09x slower                                          |
| scimark_lu                 | 114 ms                                                 | 126 ms: 1.10x slower                                          |
| crypto_pyaes               | 74.7 ms                                                | 83.0 ms: 1.11x slower                                         |
| deltablue                  | 3.19 ms                                                | 3.55 ms: 1.11x slower                                         |
| mako                       | 10.7 ms                                                | 11.9 ms: 1.12x slower                                         |
| nbody                      | 87.7 ms                                                | 98.5 ms: 1.12x slower                                         |
| many_optionals             | 857 us                                                 | 964 us: 1.13x slower                                          |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.15x slower                                         |
| python_startup_no_site     | 7.00 ms                                                | 8.19 ms: 1.17x slower                                         |
| json_loads                 | 27.2 us                                                | 32.0 us: 1.18x slower                                         |
| subparsers                 | 15.5 ms                                                | 21.3 ms: 1.38x slower                                         |
| bench_mp_pool              | 24.0 ms                                                | 83.6 ms: 3.49x slower                                         |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                  |

Benchmark hidden because not significant (9): genshi_xml, sphinx, meteor_contest, regex_dna, pycparser, pyflate, asyncio_websockets, logging_silent, sympy_str
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250401-3.14.0a6+-1baa231/bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.029x faster

# HPT report

- Reliability score: 86.81% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
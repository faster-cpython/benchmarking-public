# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: a7640fc
- commit date: 2025-05-12
- overall geometric mean: 1.032x slower
- HPT reliability: 99.08%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 263 ms: 1.01x faster                                                        |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.03x slower                                                      |
| html5lib       | 63.4 ms                                                | 61.0 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                                        |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                        |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                                        |
| async_tree_io_tg           | 861 ms                                                 | 634 ms: 1.36x faster                                                        |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 506 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 496 ms: 1.10x faster                                                        |
| async_generators           | 433 ms                                                 | 423 ms: 1.02x faster                                                        |
| coroutines                 | 22.2 ms                                                | 25.2 ms: 1.13x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 64.5 ms: 1.22x faster                                                       |
| pidigits       | 186 ms                                                 | 191 ms: 1.03x slower                                                        |
| nbody          | 87.7 ms                                                | 94.3 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.06 ms: 1.23x faster                                                       |
| regex_v8       | 26.9 ms                                                | 23.0 ms: 1.17x faster                                                       |
| regex_dna      | 220 ms                                                 | 205 ms: 1.07x faster                                                        |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.88 sec: 1.12x faster                                                      |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                        |
| xml_etree_generate   | 86.8 ms                                                | 79.8 ms: 1.09x faster                                                       |
| xml_etree_process    | 60.5 ms                                                | 55.8 ms: 1.08x faster                                                       |
| unpickle_pure_python | 213 us                                                 | 201 us: 1.06x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 98.3 ms: 1.03x faster                                                       |
| pickle_pure_python   | 302 us                                                 | 324 us: 1.07x slower                                                        |
| json_loads           | 27.2 us                                                | 29.7 us: 1.10x slower                                                       |
| json_dumps           | 10.1 ms                                                | 12.0 ms: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.3 ms: 1.03x faster                                                       |
| python_startup_no_site | 7.00 ms                                                | 6.96 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.7 ms: 1.04x faster                                                       |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                       |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.05x faster                                                      |
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                                        |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                        |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                                        |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                        |
| async_tree_io_tg           | 861 ms                                                 | 634 ms: 1.36x faster                                                        |
| richards                   | 47.5 ms                                                | 35.0 ms: 1.36x faster                                                       |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                        |
| richards_super             | 53.7 ms                                                | 41.0 ms: 1.31x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                        |
| deepcopy_memo              | 38.4 us                                                | 30.1 us: 1.27x faster                                                       |
| regex_effbot               | 3.77 ms                                                | 3.06 ms: 1.23x faster                                                       |
| float                      | 78.7 ms                                                | 64.5 ms: 1.22x faster                                                       |
| deepcopy_reduce            | 3.24 us                                                | 2.75 us: 1.18x faster                                                       |
| regex_v8                   | 26.9 ms                                                | 23.0 ms: 1.17x faster                                                       |
| go                         | 141 ms                                                 | 124 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 506 ms: 1.13x faster                                                        |
| scimark_fft                | 367 ms                                                 | 326 ms: 1.13x faster                                                        |
| tomli_loads                | 2.12 sec                                               | 1.88 sec: 1.12x faster                                                      |
| spectral_norm              | 113 ms                                                 | 101 ms: 1.12x faster                                                        |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 496 ms: 1.10x faster                                                        |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                        |
| telco                      | 8.40 ms                                                | 7.71 ms: 1.09x faster                                                       |
| xml_etree_generate         | 86.8 ms                                                | 79.8 ms: 1.09x faster                                                       |
| xml_etree_process          | 60.5 ms                                                | 55.8 ms: 1.08x faster                                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.36 sec: 1.08x faster                                                      |
| regex_dna                  | 220 ms                                                 | 205 ms: 1.07x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 201 us: 1.06x faster                                                        |
| dulwich_log                | 64.6 ms                                                | 61.2 ms: 1.06x faster                                                       |
| deltablue                  | 3.19 ms                                                | 3.05 ms: 1.05x faster                                                       |
| pyflate                    | 470 ms                                                 | 450 ms: 1.04x faster                                                        |
| genshi_text                | 22.6 ms                                                | 21.7 ms: 1.04x faster                                                       |
| html5lib                   | 63.4 ms                                                | 61.0 ms: 1.04x faster                                                       |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                                       |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                      |
| python_startup             | 12.7 ms                                                | 12.3 ms: 1.03x faster                                                       |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 98.3 ms: 1.03x faster                                                       |
| async_generators           | 433 ms                                                 | 423 ms: 1.02x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                                      |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                        |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                                       |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                        |
| 2to3                       | 266 ms                                                 | 263 ms: 1.01x faster                                                        |
| pathlib                    | 17.4 ms                                                | 17.2 ms: 1.01x faster                                                       |
| shortest_path              | 487 ms                                                 | 483 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.00 ms: 1.01x faster                                                       |
| python_startup_no_site     | 7.00 ms                                                | 6.96 ms: 1.01x faster                                                       |
| gc_traversal               | 4.90 ms                                                | 4.95 ms: 1.01x slower                                                       |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                       |
| crypto_pyaes               | 74.7 ms                                                | 76.5 ms: 1.02x slower                                                       |
| pidigits                   | 186 ms                                                 | 191 ms: 1.03x slower                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 68.6 ms: 1.03x slower                                                       |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.03x slower                                                      |
| fannkuch                   | 394 ms                                                 | 405 ms: 1.03x slower                                                        |
| raytrace                   | 262 ms                                                 | 271 ms: 1.03x slower                                                        |
| sympy_expand               | 456 ms                                                 | 472 ms: 1.04x slower                                                        |
| pprint_pformat             | 1.48 sec                                               | 1.53 sec: 1.04x slower                                                      |
| chaos                      | 58.0 ms                                                | 60.1 ms: 1.04x slower                                                       |
| pprint_safe_repr           | 727 ms                                                 | 753 ms: 1.04x slower                                                        |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                        |
| nqueens                    | 80.9 ms                                                | 85.2 ms: 1.05x slower                                                       |
| create_gc_cycles           | 2.45 ms                                                | 2.58 ms: 1.05x slower                                                       |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                       |
| pickle_pure_python         | 302 us                                                 | 324 us: 1.07x slower                                                        |
| nbody                      | 87.7 ms                                                | 94.3 ms: 1.08x slower                                                       |
| hexiom                     | 6.08 ms                                                | 6.54 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 160 us                                                 | 174 us: 1.08x slower                                                        |
| comprehensions             | 16.5 us                                                | 18.0 us: 1.09x slower                                                       |
| json_loads                 | 27.2 us                                                | 29.7 us: 1.10x slower                                                       |
| logging_format             | 6.23 us                                                | 6.86 us: 1.10x slower                                                       |
| bench_thread_pool          | 818 us                                                 | 909 us: 1.11x slower                                                        |
| logging_simple             | 5.65 us                                                | 6.29 us: 1.11x slower                                                       |
| coroutines                 | 22.2 ms                                                | 25.2 ms: 1.13x slower                                                       |
| generators                 | 28.8 ms                                                | 32.6 ms: 1.13x slower                                                       |
| many_optionals             | 857 us                                                 | 986 us: 1.15x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 12.0 ms: 1.18x slower                                                       |
| subparsers                 | 15.5 ms                                                | 23.9 ms: 1.54x slower                                                       |
| bench_mp_pool              | 24.0 ms                                                | 93.3 ms: 3.89x slower                                                       |
| logging_silent             | 101 ns                                                 | 472 ns: 4.67x slower                                                        |
| coverage                   | 82.8 ms                                                | 419 ms: 5.05x slower                                                        |
| thrift                     | 800 us                                                 | 148 ms: 185.53x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.07x slower                                                                |

Benchmark hidden because not significant (7): sphinx, sympy_str, genshi_xml, json, scimark_sor, connected_components, asyncio_websockets
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250512-3.15.0a0-a7640fc-JIT/bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.032x slower

# HPT report

- Reliability score: 99.08% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x
# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_11_8
- machine: linux-x86_64
- commit hash: 414beb9
- commit date: 2025-03-28
- overall geometric mean: 1.039x faster
- HPT reliability: 98.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_8-3.14.0a6+-414beb9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 263 ms: 1.01x faster                                                |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                              |
| html5lib       | 63.4 ms                                                | 62.8 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_8-3.14.0a6+-414beb9 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.27x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 470 ms: 1.16x faster                                                |
| async_generators           | 433 ms                                                 | 414 ms: 1.05x faster                                                |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                               |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_8-3.14.0a6+-414beb9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.2 ms: 1.21x faster                                               |
| pidigits       | 186 ms                                                 | 186 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_8-3.14.0a6+-414beb9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.18 ms: 1.18x faster                                               |
| regex_v8       | 26.9 ms                                                | 23.6 ms: 1.14x faster                                               |
| regex_dna      | 220 ms                                                 | 210 ms: 1.05x faster                                                |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_8-3.14.0a6+-414beb9 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.86 sec: 1.14x faster                                              |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.11x faster                                                |
| xml_etree_generate   | 86.8 ms                                                | 80.4 ms: 1.08x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 56.9 ms: 1.06x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 98.8 ms: 1.02x faster                                               |
| unpickle_pure_python | 213 us                                                 | 212 us: 1.01x faster                                                |
| pickle_pure_python   | 302 us                                                 | 325 us: 1.08x slower                                                |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.15x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_8-3.14.0a6+-414beb9 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                               |
| python_startup_no_site | 7.00 ms                                                | 8.19 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_8-3.14.0a6+-414beb9 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.6 ms: 1.05x faster                                               |
| genshi_xml      | 50.5 ms                                                | 50.0 ms: 1.01x faster                                               |
| django_template | 31.7 ms                                                | 32.1 ms: 1.01x slower                                               |
| mako            | 10.7 ms                                                | 10.9 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_8-3.14.0a6+-414beb9 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                |
| deepcopy                   | 354 us                                                 | 263 us: 1.35x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.27x faster                                                |
| float                      | 78.7 ms                                                | 65.2 ms: 1.21x faster                                               |
| spectral_norm              | 113 ms                                                 | 94.5 ms: 1.20x faster                                               |
| richards                   | 47.5 ms                                                | 39.8 ms: 1.19x faster                                               |
| richards_super             | 53.7 ms                                                | 45.4 ms: 1.18x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.18 ms: 1.18x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                |
| deepcopy_reduce            | 3.24 us                                                | 2.76 us: 1.17x faster                                               |
| scimark_fft                | 367 ms                                                 | 316 ms: 1.16x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 470 ms: 1.16x faster                                                |
| regex_v8                   | 26.9 ms                                                | 23.6 ms: 1.14x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.86 sec: 1.14x faster                                              |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.11x faster                                                |
| pylint                     | 312 ms                                                 | 282 ms: 1.10x faster                                                |
| xml_etree_generate         | 86.8 ms                                                | 80.4 ms: 1.08x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.71 us: 1.07x faster                                               |
| telco                      | 8.40 ms                                                | 7.85 ms: 1.07x faster                                               |
| go                         | 141 ms                                                 | 132 ms: 1.06x faster                                                |
| xml_etree_process          | 60.5 ms                                                | 56.9 ms: 1.06x faster                                               |
| pyflate                    | 470 ms                                                 | 442 ms: 1.06x faster                                                |
| dulwich_log                | 64.6 ms                                                | 60.9 ms: 1.06x faster                                               |
| deltablue                  | 3.19 ms                                                | 3.03 ms: 1.05x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                              |
| regex_dna                  | 220 ms                                                 | 210 ms: 1.05x faster                                                |
| async_generators           | 433 ms                                                 | 414 ms: 1.05x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.6 ms: 1.05x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.84 ms: 1.04x faster                                               |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                               |
| logging_silent             | 101 ns                                                 | 97.6 ns: 1.04x faster                                               |
| mdp                        | 2.54 sec                                               | 2.48 sec: 1.03x faster                                              |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 98.8 ms: 1.02x faster                                               |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.02x faster                                              |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.61 sec: 1.02x faster                                              |
| gc_traversal               | 4.90 ms                                                | 4.82 ms: 1.02x faster                                               |
| logging_format             | 6.23 us                                                | 6.14 us: 1.02x faster                                               |
| logging_simple             | 5.65 us                                                | 5.59 us: 1.01x faster                                               |
| 2to3                       | 266 ms                                                 | 263 ms: 1.01x faster                                                |
| html5lib                   | 63.4 ms                                                | 62.8 ms: 1.01x faster                                               |
| genshi_xml                 | 50.5 ms                                                | 50.0 ms: 1.01x faster                                               |
| thrift                     | 800 us                                                 | 794 us: 1.01x faster                                                |
| unpickle_pure_python       | 213 us                                                 | 212 us: 1.01x faster                                                |
| pidigits                   | 186 ms                                                 | 186 ms: 1.01x faster                                                |
| generators                 | 28.8 ms                                                | 29.0 ms: 1.01x slower                                               |
| raytrace                   | 262 ms                                                 | 265 ms: 1.01x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                               |
| django_template            | 31.7 ms                                                | 32.1 ms: 1.01x slower                                               |
| sqlalchemy_declarative     | 133 ms                                                 | 135 ms: 1.01x slower                                                |
| crypto_pyaes               | 74.7 ms                                                | 75.8 ms: 1.02x slower                                               |
| shortest_path              | 487 ms                                                 | 494 ms: 1.02x slower                                                |
| sympy_str                  | 273 ms                                                 | 278 ms: 1.02x slower                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 68.0 ms: 1.02x slower                                               |
| mako                       | 10.7 ms                                                | 10.9 ms: 1.02x slower                                               |
| sympy_integrate            | 19.8 ms                                                | 20.2 ms: 1.02x slower                                               |
| connected_components       | 447 ms                                                 | 459 ms: 1.03x slower                                                |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                |
| nqueens                    | 80.9 ms                                                | 83.5 ms: 1.03x slower                                               |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                               |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.5 ms: 1.04x slower                                               |
| chaos                      | 58.0 ms                                                | 60.4 ms: 1.04x slower                                               |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                              |
| coverage                   | 82.8 ms                                                | 86.6 ms: 1.05x slower                                               |
| sympy_expand               | 456 ms                                                 | 480 ms: 1.05x slower                                                |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.05x slower                                                |
| fannkuch                   | 394 ms                                                 | 416 ms: 1.06x slower                                                |
| pprint_safe_repr           | 727 ms                                                 | 774 ms: 1.06x slower                                                |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                               |
| pprint_pformat             | 1.48 sec                                               | 1.59 sec: 1.08x slower                                              |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.08x slower                                                |
| bench_thread_pool          | 818 us                                                 | 884 us: 1.08x slower                                                |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.86 ms: 1.13x slower                                               |
| comprehensions             | 16.5 us                                                | 18.9 us: 1.15x slower                                               |
| many_optionals             | 857 us                                                 | 984 us: 1.15x slower                                                |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.15x slower                                               |
| python_startup_no_site     | 7.00 ms                                                | 8.19 ms: 1.17x slower                                               |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 83.1 ms: 3.47x slower                                               |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (6): json, sphinx, asyncio_websockets, meteor_contest, nbody, scimark_lu
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250328-3.14.0a6+-414beb9-JIT/bm-20250328-linux-x86_64-brandtbucher-jit_up_11_8-3.14.0a6+-414beb9.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 98.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x
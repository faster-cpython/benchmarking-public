# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_11_11
- machine: linux-x86_64
- commit hash: ffcb0ed
- commit date: 2025-03-26
- overall geometric mean: 1.033x faster
- HPT reliability: 95.40%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 264 ms: 1.01x faster                                                 |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.04x slower                                               |
| html5lib       | 63.4 ms                                                | 63.7 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                 |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                 |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 501 ms: 1.14x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                                 |
| async_generators           | 433 ms                                                 | 419 ms: 1.03x faster                                                 |
| coroutines                 | 22.2 ms                                                | 24.1 ms: 1.08x slower                                                |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                         |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.8 ms: 1.19x faster                                                |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                         |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                |
| regex_effbot   | 3.77 ms                                                | 3.39 ms: 1.11x faster                                                |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                 |
| regex_dna      | 220 ms                                                 | 225 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.86 sec: 1.14x faster                                               |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 80.4 ms: 1.08x faster                                                |
| xml_etree_process    | 60.5 ms                                                | 56.4 ms: 1.07x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 98.6 ms: 1.03x faster                                                |
| unpickle_pure_python | 213 us                                                 | 214 us: 1.00x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 327 us: 1.08x slower                                                 |
| json_loads           | 27.2 us                                                | 30.0 us: 1.10x slower                                                |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                |
| python_startup_no_site | 7.00 ms                                                | 8.20 ms: 1.17x slower                                                |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                |
| genshi_xml      | 50.5 ms                                                | 50.0 ms: 1.01x faster                                                |
| django_template | 31.7 ms                                                | 32.4 ms: 1.02x slower                                                |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                 |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                 |
| deepcopy                   | 354 us                                                 | 262 us: 1.35x faster                                                 |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                 |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                 |
| scimark_fft                | 367 ms                                                 | 307 ms: 1.20x faster                                                 |
| float                      | 78.7 ms                                                | 65.8 ms: 1.19x faster                                                |
| spectral_norm              | 113 ms                                                 | 95.2 ms: 1.19x faster                                                |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 501 ms: 1.14x faster                                                 |
| richards                   | 47.5 ms                                                | 41.6 ms: 1.14x faster                                                |
| tomli_loads                | 2.12 sec                                               | 1.86 sec: 1.14x faster                                               |
| richards_super             | 53.7 ms                                                | 47.2 ms: 1.14x faster                                                |
| regex_v8                   | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.39 ms: 1.11x faster                                                |
| pylint                     | 312 ms                                                 | 282 ms: 1.10x faster                                                 |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.63 ms: 1.09x faster                                                |
| go                         | 141 ms                                                 | 130 ms: 1.08x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 80.4 ms: 1.08x faster                                                |
| xml_etree_process          | 60.5 ms                                                | 56.4 ms: 1.07x faster                                                |
| sqlite_synth               | 2.90 us                                                | 2.71 us: 1.07x faster                                                |
| pyflate                    | 470 ms                                                 | 441 ms: 1.07x faster                                                 |
| dulwich_log                | 64.6 ms                                                | 60.8 ms: 1.06x faster                                                |
| telco                      | 8.40 ms                                                | 7.93 ms: 1.06x faster                                                |
| logging_silent             | 101 ns                                                 | 95.6 ns: 1.06x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                |
| pathlib                    | 17.4 ms                                                | 16.6 ms: 1.05x faster                                                |
| deltablue                  | 3.19 ms                                                | 3.06 ms: 1.04x faster                                                |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                                 |
| async_generators           | 433 ms                                                 | 419 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 98.6 ms: 1.03x faster                                                |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.32 sec: 1.02x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.62 sec: 1.02x faster                                               |
| thrift                     | 800 us                                                 | 788 us: 1.01x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 50.0 ms: 1.01x faster                                                |
| 2to3                       | 266 ms                                                 | 264 ms: 1.01x faster                                                 |
| logging_format             | 6.23 us                                                | 6.19 us: 1.01x faster                                                |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 214 us: 1.00x slower                                                 |
| html5lib                   | 63.4 ms                                                | 63.7 ms: 1.01x slower                                                |
| shortest_path              | 487 ms                                                 | 490 ms: 1.01x slower                                                 |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 134 ms: 1.01x slower                                                 |
| sympy_str                  | 273 ms                                                 | 277 ms: 1.02x slower                                                 |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                                 |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                                |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                                 |
| sympy_integrate            | 19.8 ms                                                | 20.2 ms: 1.02x slower                                                |
| regex_dna                  | 220 ms                                                 | 225 ms: 1.02x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 154 ms: 1.02x slower                                                 |
| gc_traversal               | 4.90 ms                                                | 5.01 ms: 1.02x slower                                                |
| django_template            | 31.7 ms                                                | 32.4 ms: 1.02x slower                                                |
| crypto_pyaes               | 74.7 ms                                                | 76.5 ms: 1.02x slower                                                |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.4 ms: 1.03x slower                                                |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 69.1 ms: 1.03x slower                                                |
| coverage                   | 82.8 ms                                                | 85.7 ms: 1.04x slower                                                |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                |
| connected_components       | 447 ms                                                 | 464 ms: 1.04x slower                                                 |
| chaos                      | 58.0 ms                                                | 60.5 ms: 1.04x slower                                                |
| sympy_expand               | 456 ms                                                 | 476 ms: 1.04x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.70 sec: 1.04x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.05x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 768 ms: 1.06x slower                                                 |
| nqueens                    | 80.9 ms                                                | 86.1 ms: 1.06x slower                                                |
| pprint_pformat             | 1.48 sec                                               | 1.58 sec: 1.07x slower                                               |
| fannkuch                   | 394 ms                                                 | 426 ms: 1.08x slower                                                 |
| coroutines                 | 22.2 ms                                                | 24.1 ms: 1.08x slower                                                |
| pickle_pure_python         | 302 us                                                 | 327 us: 1.08x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 886 us: 1.08x slower                                                 |
| json_loads                 | 27.2 us                                                | 30.0 us: 1.10x slower                                                |
| hexiom                     | 6.08 ms                                                | 6.82 ms: 1.12x slower                                                |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                |
| many_optionals             | 857 us                                                 | 985 us: 1.15x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 8.20 ms: 1.17x slower                                                |
| comprehensions             | 16.5 us                                                | 19.4 us: 1.18x slower                                                |
| subparsers                 | 15.5 ms                                                | 21.1 ms: 1.37x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 83.2 ms: 3.47x slower                                                |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (8): pycparser, json, mdp, generators, asyncio_websockets, sphinx, logging_simple, nbody
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250326-3.14.0a6+-ffcb0ed-JIT/bm-20250326-linux-x86_64-brandtbucher-jit_up_11_11-3.14.0a6+-ffcb0ed.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 95.40% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
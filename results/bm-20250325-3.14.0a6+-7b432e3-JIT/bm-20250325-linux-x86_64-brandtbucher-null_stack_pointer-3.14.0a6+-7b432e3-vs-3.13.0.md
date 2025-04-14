# Results vs. 3.13.0

- fork: brandtbucher
- ref: null_stack_pointer
- machine: linux-x86_64
- commit hash: 7b432e3
- commit date: 2025-03-25
- overall geometric mean: 1.045x faster
- HPT reliability: 99.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 263 ms: 1.01x faster                                                       |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.48x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 624 ms: 1.38x faster                                                       |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                       |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                       |
| async_generators           | 433 ms                                                 | 414 ms: 1.05x faster                                                       |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.1 ms: 1.21x faster                                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.16 ms: 1.19x faster                                                      |
| regex_v8       | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                      |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                       |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                     |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                       |
| xml_etree_generate   | 86.8 ms                                                | 80.2 ms: 1.08x faster                                                      |
| xml_etree_process    | 60.5 ms                                                | 56.1 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 97.8 ms: 1.04x faster                                                      |
| unpickle_pure_python | 213 us                                                 | 210 us: 1.02x faster                                                       |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                                       |
| json_loads           | 27.2 us                                                | 29.9 us: 1.10x slower                                                      |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                      |
| python_startup_no_site | 7.00 ms                                                | 8.22 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                      |
| mako           | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.48x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 624 ms: 1.38x faster                                                       |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                       |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                       |
| richards                   | 47.5 ms                                                | 35.5 ms: 1.34x faster                                                      |
| richards_super             | 53.7 ms                                                | 40.2 ms: 1.34x faster                                                      |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                       |
| deepcopy_memo              | 38.4 us                                                | 29.5 us: 1.30x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                       |
| spectral_norm              | 113 ms                                                 | 92.7 ms: 1.22x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.68 us: 1.21x faster                                                      |
| float                      | 78.7 ms                                                | 65.1 ms: 1.21x faster                                                      |
| scimark_fft                | 367 ms                                                 | 307 ms: 1.19x faster                                                       |
| regex_effbot               | 3.77 ms                                                | 3.16 ms: 1.19x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                       |
| regex_v8                   | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                       |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                                       |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                       |
| go                         | 141 ms                                                 | 127 ms: 1.10x faster                                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.57 ms: 1.10x faster                                                      |
| xml_etree_generate         | 86.8 ms                                                | 80.2 ms: 1.08x faster                                                      |
| telco                      | 8.40 ms                                                | 7.77 ms: 1.08x faster                                                      |
| xml_etree_process          | 60.5 ms                                                | 56.1 ms: 1.08x faster                                                      |
| dulwich_log                | 64.6 ms                                                | 60.6 ms: 1.07x faster                                                      |
| sqlite_synth               | 2.90 us                                                | 2.73 us: 1.06x faster                                                      |
| pyflate                    | 470 ms                                                 | 442 ms: 1.06x faster                                                       |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                     |
| deltablue                  | 3.19 ms                                                | 3.02 ms: 1.06x faster                                                      |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                      |
| pathlib                    | 17.4 ms                                                | 16.6 ms: 1.05x faster                                                      |
| async_generators           | 433 ms                                                 | 414 ms: 1.05x faster                                                       |
| thrift                     | 800 us                                                 | 765 us: 1.05x faster                                                       |
| xml_etree_iterparse        | 101 ms                                                 | 97.8 ms: 1.04x faster                                                      |
| logging_simple             | 5.65 us                                                | 5.49 us: 1.03x faster                                                      |
| logging_silent             | 101 ns                                                 | 98.2 ns: 1.03x faster                                                      |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                       |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.58 sec: 1.02x faster                                                     |
| mdp                        | 2.54 sec                                               | 2.49 sec: 1.02x faster                                                     |
| k_core                     | 2.37 sec                                               | 2.32 sec: 1.02x faster                                                     |
| logging_format             | 6.23 us                                                | 6.12 us: 1.02x faster                                                      |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                       |
| unpickle_pure_python       | 213 us                                                 | 210 us: 1.02x faster                                                       |
| generators                 | 28.8 ms                                                | 28.4 ms: 1.01x faster                                                      |
| 2to3                       | 266 ms                                                 | 263 ms: 1.01x faster                                                       |
| gc_traversal               | 4.90 ms                                                | 4.84 ms: 1.01x faster                                                      |
| pidigits                   | 186 ms                                                 | 186 ms: 1.01x faster                                                       |
| sympy_str                  | 273 ms                                                 | 275 ms: 1.01x slower                                                       |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                                       |
| sympy_integrate            | 19.8 ms                                                | 20.0 ms: 1.01x slower                                                      |
| scimark_monte_carlo        | 66.8 ms                                                | 67.7 ms: 1.01x slower                                                      |
| connected_components       | 447 ms                                                 | 453 ms: 1.01x slower                                                       |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.2 ms: 1.01x slower                                                      |
| shortest_path              | 487 ms                                                 | 494 ms: 1.02x slower                                                       |
| create_gc_cycles           | 2.45 ms                                                | 2.50 ms: 1.02x slower                                                      |
| chaos                      | 58.0 ms                                                | 59.6 ms: 1.03x slower                                                      |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                                       |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                     |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.03x slower                                                       |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                      |
| coverage                   | 82.8 ms                                                | 86.0 ms: 1.04x slower                                                      |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                      |
| crypto_pyaes               | 74.7 ms                                                | 77.9 ms: 1.04x slower                                                      |
| sympy_expand               | 456 ms                                                 | 476 ms: 1.04x slower                                                       |
| mako                       | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                                       |
| nqueens                    | 80.9 ms                                                | 86.2 ms: 1.07x slower                                                      |
| pprint_safe_repr           | 727 ms                                                 | 783 ms: 1.08x slower                                                       |
| bench_thread_pool          | 818 us                                                 | 883 us: 1.08x slower                                                       |
| fannkuch                   | 394 ms                                                 | 425 ms: 1.08x slower                                                       |
| pprint_pformat             | 1.48 sec                                               | 1.62 sec: 1.10x slower                                                     |
| json_loads                 | 27.2 us                                                | 29.9 us: 1.10x slower                                                      |
| hexiom                     | 6.08 ms                                                | 6.82 ms: 1.12x slower                                                      |
| comprehensions             | 16.5 us                                                | 18.5 us: 1.12x slower                                                      |
| many_optionals             | 857 us                                                 | 971 us: 1.13x slower                                                       |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                      |
| python_startup_no_site     | 7.00 ms                                                | 8.22 ms: 1.17x slower                                                      |
| subparsers                 | 15.5 ms                                                | 21.1 ms: 1.37x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 83.1 ms: 3.47x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (10): sphinx, genshi_xml, scimark_lu, asyncio_websockets, meteor_contest, sqlalchemy_declarative, html5lib, django_template, json, nbody
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250325-3.14.0a6+-7b432e3-JIT/bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 99.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
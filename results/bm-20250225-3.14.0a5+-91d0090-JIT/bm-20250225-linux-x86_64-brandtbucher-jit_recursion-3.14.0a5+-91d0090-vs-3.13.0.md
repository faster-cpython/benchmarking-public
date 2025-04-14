# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_recursion
- machine: linux-x86_64
- commit hash: 91d0090
- commit date: 2025-02-25
- overall geometric mean: 1.034x faster
- HPT reliability: 99.71%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 262 ms: 1.02x faster                                                  |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                |
| html5lib       | 63.4 ms                                                | 62.1 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                  |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                  |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 333 ms: 1.31x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                                  |
| async_generators           | 433 ms                                                 | 407 ms: 1.06x faster                                                  |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.08x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.4 ms: 1.09x faster                                                 |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                  |
| nbody          | 87.7 ms                                                | 89.6 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.38 ms: 1.12x faster                                                 |
| regex_v8       | 26.9 ms                                                | 25.6 ms: 1.05x faster                                                 |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 79.6 ms: 1.09x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 56.2 ms: 1.08x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 97.5 ms: 1.04x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 207 us: 1.03x faster                                                  |
| pickle_pure_python   | 302 us                                                 | 326 us: 1.08x slower                                                  |
| json_loads           | 27.2 us                                                | 30.1 us: 1.11x slower                                                 |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.13x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.16 ms: 1.02x slower                                                 |
| python_startup         | 12.7 ms                                                | 13.0 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.6 ms: 1.00x faster                                                 |
| genshi_text     | 22.6 ms                                                | 22.7 ms: 1.01x slower                                                 |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                  |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                  |
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                                  |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 333 ms: 1.31x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 31.2 us: 1.23x faster                                                 |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.21x faster                                                 |
| scimark_fft                | 367 ms                                                 | 314 ms: 1.17x faster                                                  |
| spectral_norm              | 113 ms                                                 | 97.4 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                                  |
| telco                      | 8.40 ms                                                | 7.51 ms: 1.12x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.38 ms: 1.12x faster                                                 |
| pylint                     | 312 ms                                                 | 280 ms: 1.12x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                  |
| go                         | 141 ms                                                 | 128 ms: 1.10x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 79.6 ms: 1.09x faster                                                 |
| float                      | 78.7 ms                                                | 72.4 ms: 1.09x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.65 ms: 1.08x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 56.2 ms: 1.08x faster                                                 |
| async_generators           | 433 ms                                                 | 407 ms: 1.06x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.73 us: 1.06x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.47 sec: 1.05x faster                                                |
| regex_v8                   | 26.9 ms                                                | 25.6 ms: 1.05x faster                                                 |
| thrift                     | 800 us                                                 | 765 us: 1.05x faster                                                  |
| pyflate                    | 470 ms                                                 | 450 ms: 1.04x faster                                                  |
| richards                   | 47.5 ms                                                | 45.6 ms: 1.04x faster                                                 |
| richards_super             | 53.7 ms                                                | 51.7 ms: 1.04x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 97.5 ms: 1.04x faster                                                 |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                  |
| unpickle_pure_python       | 213 us                                                 | 207 us: 1.03x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.02x faster                                                |
| connected_components       | 447 ms                                                 | 438 ms: 1.02x faster                                                  |
| html5lib                   | 63.4 ms                                                | 62.1 ms: 1.02x faster                                                 |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                                  |
| mdp                        | 2.54 sec                                               | 2.50 sec: 1.02x faster                                                |
| 2to3                       | 266 ms                                                 | 262 ms: 1.02x faster                                                  |
| json                       | 5.32 ms                                                | 5.26 ms: 1.01x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.01x faster                                                |
| shortest_path              | 487 ms                                                 | 481 ms: 1.01x faster                                                  |
| generators                 | 28.8 ms                                                | 28.5 ms: 1.01x faster                                                 |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.62 us: 1.01x faster                                                 |
| logging_format             | 6.23 us                                                | 6.20 us: 1.01x faster                                                 |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                 |
| mako                       | 10.7 ms                                                | 10.6 ms: 1.00x faster                                                 |
| sqlglot_optimize           | 53.4 ms                                                | 53.6 ms: 1.00x slower                                                 |
| genshi_text                | 22.6 ms                                                | 22.7 ms: 1.01x slower                                                 |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                  |
| sympy_str                  | 273 ms                                                 | 276 ms: 1.01x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 163 us: 1.01x slower                                                  |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                 |
| fannkuch                   | 394 ms                                                 | 401 ms: 1.02x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 20.2 ms: 1.02x slower                                                 |
| nbody                      | 87.7 ms                                                | 89.6 ms: 1.02x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 7.16 ms: 1.02x slower                                                 |
| nqueens                    | 80.9 ms                                                | 82.8 ms: 1.02x slower                                                 |
| gc_traversal               | 4.90 ms                                                | 5.03 ms: 1.03x slower                                                 |
| sqlglot_parse              | 1.26 ms                                                | 1.30 ms: 1.03x slower                                                 |
| python_startup             | 12.7 ms                                                | 13.0 ms: 1.03x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 1.52 sec: 1.03x slower                                                |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                  |
| coverage                   | 82.8 ms                                                | 85.3 ms: 1.03x slower                                                 |
| sqlglot_transpile          | 1.57 ms                                                | 1.62 ms: 1.03x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 68.9 ms: 1.03x slower                                                 |
| sympy_expand               | 456 ms                                                 | 472 ms: 1.03x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                |
| chaos                      | 58.0 ms                                                | 60.4 ms: 1.04x slower                                                 |
| dulwich_log                | 64.6 ms                                                | 67.4 ms: 1.04x slower                                                 |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.04x slower                                                 |
| deltablue                  | 3.19 ms                                                | 3.40 ms: 1.06x slower                                                 |
| raytrace                   | 262 ms                                                 | 279 ms: 1.07x slower                                                  |
| logging_silent             | 101 ns                                                 | 108 ns: 1.07x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 326 us: 1.08x slower                                                  |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.08x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 881 us: 1.08x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.67 ms: 1.10x slower                                                 |
| json_loads                 | 27.2 us                                                | 30.1 us: 1.11x slower                                                 |
| many_optionals             | 857 us                                                 | 965 us: 1.13x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.13x slower                                                 |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 82.1 ms: 3.43x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (9): sphinx, meteor_contest, asyncio_websockets, genshi_xml, create_gc_cycles, regex_dna, sympy_sum, pprint_safe_repr, crypto_pyaes
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 99.71% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
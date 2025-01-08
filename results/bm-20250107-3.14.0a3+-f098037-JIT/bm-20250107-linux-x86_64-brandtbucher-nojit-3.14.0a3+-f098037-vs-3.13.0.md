# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.040x faster
- HPT reliability: 99.31%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                          |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.04x slower                                        |
| html5lib       | 63.4 ms                                                | 64.1 ms: 1.01x slower                                         |
| sphinx         | 1.03 sec                                               | 1.05 sec: 1.01x slower                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 305 ms: 1.52x faster                                          |
| async_tree_io_tg           | 861 ms                                                 | 586 ms: 1.47x faster                                          |
| async_tree_io              | 838 ms                                                 | 608 ms: 1.38x faster                                          |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                          |
| async_tree_memoization     | 437 ms                                                 | 326 ms: 1.34x faster                                          |
| async_tree_none_tg         | 319 ms                                                 | 245 ms: 1.30x faster                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 468 ms: 1.16x faster                                          |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                          |
| async_generators           | 433 ms                                                 | 447 ms: 1.03x slower                                          |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.07x slower                                         |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 78.7 ms                                                | 68.1 ms: 1.16x faster                                         |
| nbody          | 87.7 ms                                                | 85.0 ms: 1.03x faster                                         |
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.41 ms: 1.10x faster                                         |
| regex_v8       | 26.9 ms                                                | 24.9 ms: 1.08x faster                                         |
| regex_dna      | 220 ms                                                 | 214 ms: 1.03x faster                                          |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.85 sec: 1.14x faster                                        |
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.12x faster                                          |
| xml_etree_generate   | 86.8 ms                                                | 77.8 ms: 1.12x faster                                         |
| unpickle_pure_python | 213 us                                                 | 193 us: 1.11x faster                                          |
| xml_etree_process    | 60.5 ms                                                | 54.9 ms: 1.10x faster                                         |
| xml_etree_iterparse  | 101 ms                                                 | 94.8 ms: 1.07x faster                                         |
| pickle_pure_python   | 302 us                                                 | 325 us: 1.08x slower                                          |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.10x slower                                         |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                  |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                         |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                         |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.1 ms: 1.05x faster                                         |
| django_template | 31.7 ms                                                | 32.8 ms: 1.04x slower                                         |
| genshi_text     | 22.6 ms                                                | 24.0 ms: 1.06x slower                                         |
| genshi_xml      | 50.5 ms                                                | 57.4 ms: 1.14x slower                                         |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 305 ms: 1.52x faster                                          |
| async_tree_io_tg           | 861 ms                                                 | 586 ms: 1.47x faster                                          |
| deepcopy_memo              | 38.4 us                                                | 27.8 us: 1.38x faster                                         |
| async_tree_io              | 838 ms                                                 | 608 ms: 1.38x faster                                          |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                          |
| async_tree_memoization     | 437 ms                                                 | 326 ms: 1.34x faster                                          |
| deepcopy                   | 354 us                                                 | 265 us: 1.34x faster                                          |
| async_tree_none_tg         | 319 ms                                                 | 245 ms: 1.30x faster                                          |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.19x faster                                         |
| scimark_fft                | 367 ms                                                 | 308 ms: 1.19x faster                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 468 ms: 1.16x faster                                          |
| float                      | 78.7 ms                                                | 68.1 ms: 1.16x faster                                         |
| tomli_loads                | 2.12 sec                                               | 1.85 sec: 1.14x faster                                        |
| go                         | 141 ms                                                 | 124 ms: 1.13x faster                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.46 ms: 1.13x faster                                         |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.12x faster                                          |
| xml_etree_generate         | 86.8 ms                                                | 77.8 ms: 1.12x faster                                         |
| telco                      | 8.40 ms                                                | 7.54 ms: 1.11x faster                                         |
| unpickle_pure_python       | 213 us                                                 | 193 us: 1.11x faster                                          |
| regex_effbot               | 3.77 ms                                                | 3.41 ms: 1.10x faster                                         |
| richards                   | 47.5 ms                                                | 43.1 ms: 1.10x faster                                         |
| xml_etree_process          | 60.5 ms                                                | 54.9 ms: 1.10x faster                                         |
| crypto_pyaes               | 74.7 ms                                                | 68.3 ms: 1.09x faster                                         |
| pathlib                    | 17.4 ms                                                | 16.0 ms: 1.09x faster                                         |
| richards_super             | 53.7 ms                                                | 49.7 ms: 1.08x faster                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 61.8 ms: 1.08x faster                                         |
| spectral_norm              | 113 ms                                                 | 105 ms: 1.08x faster                                          |
| regex_v8                   | 26.9 ms                                                | 24.9 ms: 1.08x faster                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.37 sec: 1.07x faster                                        |
| pylint                     | 312 ms                                                 | 291 ms: 1.07x faster                                          |
| xml_etree_iterparse        | 101 ms                                                 | 94.8 ms: 1.07x faster                                         |
| scimark_sor                | 122 ms                                                 | 115 ms: 1.07x faster                                          |
| json                       | 5.32 ms                                                | 5.03 ms: 1.06x faster                                         |
| sqlite_synth               | 2.90 us                                                | 2.76 us: 1.05x faster                                         |
| mako                       | 10.7 ms                                                | 10.1 ms: 1.05x faster                                         |
| pyflate                    | 470 ms                                                 | 449 ms: 1.05x faster                                          |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.05x faster                                        |
| fannkuch                   | 394 ms                                                 | 379 ms: 1.04x faster                                          |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                        |
| nbody                      | 87.7 ms                                                | 85.0 ms: 1.03x faster                                         |
| regex_dna                  | 220 ms                                                 | 214 ms: 1.03x faster                                          |
| connected_components       | 447 ms                                                 | 435 ms: 1.03x faster                                          |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                          |
| pprint_safe_repr           | 727 ms                                                 | 709 ms: 1.02x faster                                          |
| gc_traversal               | 4.90 ms                                                | 4.79 ms: 1.02x faster                                         |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                          |
| thrift                     | 800 us                                                 | 786 us: 1.02x faster                                          |
| scimark_lu                 | 114 ms                                                 | 112 ms: 1.02x faster                                          |
| shortest_path              | 487 ms                                                 | 481 ms: 1.01x faster                                          |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.01x faster                                          |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                          |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                         |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                         |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                         |
| html5lib                   | 63.4 ms                                                | 64.1 ms: 1.01x slower                                         |
| mdp                        | 2.54 sec                                               | 2.57 sec: 1.01x slower                                        |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                         |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                          |
| sphinx                     | 1.03 sec                                               | 1.05 sec: 1.01x slower                                        |
| sqlglot_optimize           | 53.4 ms                                                | 54.2 ms: 1.02x slower                                         |
| logging_format             | 6.23 us                                                | 6.38 us: 1.02x slower                                         |
| coverage                   | 82.8 ms                                                | 85.1 ms: 1.03x slower                                         |
| async_generators           | 433 ms                                                 | 447 ms: 1.03x slower                                          |
| logging_simple             | 5.65 us                                                | 5.83 us: 1.03x slower                                         |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                         |
| sympy_str                  | 273 ms                                                 | 282 ms: 1.03x slower                                          |
| dulwich_log                | 64.6 ms                                                | 66.8 ms: 1.03x slower                                         |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.04x slower                                          |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.04x slower                                          |
| django_template            | 31.7 ms                                                | 32.8 ms: 1.04x slower                                         |
| sympy_integrate            | 19.8 ms                                                | 20.6 ms: 1.04x slower                                         |
| chaos                      | 58.0 ms                                                | 60.6 ms: 1.04x slower                                         |
| docutils                   | 2.58 sec                                               | 2.70 sec: 1.04x slower                                        |
| sympy_expand               | 456 ms                                                 | 478 ms: 1.05x slower                                          |
| genshi_text                | 22.6 ms                                                | 24.0 ms: 1.06x slower                                         |
| logging_silent             | 101 ns                                                 | 108 ns: 1.07x slower                                          |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.07x slower                                         |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.08x slower                                          |
| raytrace                   | 262 ms                                                 | 282 ms: 1.08x slower                                          |
| nqueens                    | 80.9 ms                                                | 87.4 ms: 1.08x slower                                         |
| bench_thread_pool          | 818 us                                                 | 891 us: 1.09x slower                                          |
| deltablue                  | 3.19 ms                                                | 3.50 ms: 1.09x slower                                         |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.10x slower                                         |
| genshi_xml                 | 50.5 ms                                                | 57.4 ms: 1.14x slower                                         |
| many_optionals             | 857 us                                                 | 983 us: 1.15x slower                                          |
| hexiom                     | 6.08 ms                                                | 7.24 ms: 1.19x slower                                         |
| generators                 | 28.8 ms                                                | 36.7 ms: 1.28x slower                                         |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                         |
| bench_mp_pool              | 24.0 ms                                                | 81.5 ms: 3.40x slower                                         |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                  |

Benchmark hidden because not significant (6): meteor_contest, json_loads, sqlglot_normalize, sqlglot_parse, sqlalchemy_imperative, pprint_pformat
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250107-3.14.0a3+-f098037-JIT/bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037.json: mypy2

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 99.31% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
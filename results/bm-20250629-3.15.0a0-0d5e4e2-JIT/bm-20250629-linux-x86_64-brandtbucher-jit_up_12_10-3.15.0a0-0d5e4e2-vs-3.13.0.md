# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_12_10
- machine: linux-x86_64
- commit hash: 0d5e4e2
- commit date: 2025-06-29
- overall geometric mean: 1.060x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.03x faster                                                |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                              |
| html5lib       | 63.4 ms                                                | 61.3 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 320 ms: 1.45x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.39x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 492 ms: 1.10x faster                                                |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                |
| async_generators           | 433 ms                                                 | 438 ms: 1.01x slower                                                |
| coroutines                 | 22.2 ms                                                | 24.5 ms: 1.10x slower                                               |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.7 ms: 1.20x faster                                               |
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                                |
| nbody          | 87.7 ms                                                | 97.1 ms: 1.11x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.9 ms: 1.13x faster                                               |
| regex_effbot   | 3.77 ms                                                | 3.37 ms: 1.12x faster                                               |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.08x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.83 sec: 1.15x faster                                              |
| unpickle_pure_python | 213 us                                                 | 193 us: 1.11x faster                                                |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                |
| xml_etree_process    | 60.5 ms                                                | 55.8 ms: 1.08x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 80.6 ms: 1.08x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 98.5 ms: 1.03x faster                                               |
| json_loads           | 27.2 us                                                | 28.5 us: 1.05x slower                                               |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.07x slower                                                |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.09x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                               |
| python_startup_no_site | 7.00 ms                                                | 6.96 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 22.4 ms: 1.01x faster                                               |
| genshi_xml      | 50.5 ms                                                | 51.4 ms: 1.02x slower                                               |
| django_template | 31.7 ms                                                | 32.5 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.06x faster                                              |
| richards                   | 47.5 ms                                                | 32.4 ms: 1.47x faster                                               |
| async_tree_memoization_tg  | 463 ms                                                 | 320 ms: 1.45x faster                                                |
| richards_super             | 53.7 ms                                                | 37.6 ms: 1.43x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.39x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                |
| deepcopy                   | 354 us                                                 | 258 us: 1.37x faster                                                |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 29.9 us: 1.28x faster                                               |
| spectral_norm              | 113 ms                                                 | 90.2 ms: 1.26x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                                |
| float                      | 78.7 ms                                                | 65.7 ms: 1.20x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.20x faster                                               |
| scimark_fft                | 367 ms                                                 | 313 ms: 1.17x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                                |
| pyflate                    | 470 ms                                                 | 406 ms: 1.16x faster                                                |
| tomli_loads                | 2.12 sec                                               | 1.83 sec: 1.15x faster                                              |
| regex_v8                   | 26.9 ms                                                | 23.9 ms: 1.13x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.37 ms: 1.12x faster                                               |
| unpickle_pure_python       | 213 us                                                 | 193 us: 1.11x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 492 ms: 1.10x faster                                                |
| pylint                     | 312 ms                                                 | 283 ms: 1.10x faster                                                |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                |
| telco                      | 8.40 ms                                                | 7.72 ms: 1.09x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 55.8 ms: 1.08x faster                                               |
| dulwich_log                | 64.6 ms                                                | 59.7 ms: 1.08x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 80.6 ms: 1.08x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.39 sec: 1.07x faster                                              |
| deltablue                  | 3.19 ms                                                | 3.05 ms: 1.05x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                              |
| regex_dna                  | 220 ms                                                 | 212 ms: 1.04x faster                                                |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                              |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                |
| html5lib                   | 63.4 ms                                                | 61.3 ms: 1.03x faster                                               |
| pprint_safe_repr           | 727 ms                                                 | 704 ms: 1.03x faster                                                |
| pprint_pformat             | 1.48 sec                                               | 1.43 sec: 1.03x faster                                              |
| thrift                     | 800 us                                                 | 776 us: 1.03x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 98.5 ms: 1.03x faster                                               |
| 2to3                       | 266 ms                                                 | 259 ms: 1.03x faster                                                |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                               |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.94 ms: 1.02x faster                                               |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                |
| genshi_text                | 22.6 ms                                                | 22.4 ms: 1.01x faster                                               |
| logging_simple             | 5.65 us                                                | 5.60 us: 1.01x faster                                               |
| python_startup_no_site     | 7.00 ms                                                | 6.96 ms: 1.01x faster                                               |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.00x faster                                                |
| crypto_pyaes               | 74.7 ms                                                | 75.1 ms: 1.01x slower                                               |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                |
| async_generators           | 433 ms                                                 | 438 ms: 1.01x slower                                                |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                                |
| genshi_xml                 | 50.5 ms                                                | 51.4 ms: 1.02x slower                                               |
| nqueens                    | 80.9 ms                                                | 82.7 ms: 1.02x slower                                               |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                |
| djangocms                  | 22.3 us                                                | 22.8 us: 1.02x slower                                               |
| connected_components       | 447 ms                                                 | 457 ms: 1.02x slower                                                |
| shortest_path              | 487 ms                                                 | 498 ms: 1.02x slower                                                |
| django_template            | 31.7 ms                                                | 32.5 ms: 1.03x slower                                               |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                              |
| sympy_expand               | 456 ms                                                 | 469 ms: 1.03x slower                                                |
| hexiom                     | 6.08 ms                                                | 6.26 ms: 1.03x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                                |
| json_loads                 | 27.2 us                                                | 28.5 us: 1.05x slower                                               |
| logging_silent             | 101 ns                                                 | 106 ns: 1.05x slower                                                |
| gc_traversal               | 4.90 ms                                                | 5.17 ms: 1.06x slower                                               |
| generators                 | 28.8 ms                                                | 30.4 ms: 1.06x slower                                               |
| coverage                   | 82.8 ms                                                | 88.0 ms: 1.06x slower                                               |
| chaos                      | 58.0 ms                                                | 61.7 ms: 1.06x slower                                               |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.07x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.61 ms: 1.07x slower                                               |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.09x slower                                               |
| coroutines                 | 22.2 ms                                                | 24.5 ms: 1.10x slower                                               |
| nbody                      | 87.7 ms                                                | 97.1 ms: 1.11x slower                                               |
| many_optionals             | 857 us                                                 | 984 us: 1.15x slower                                                |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.53x slower                                               |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (8): sphinx, json, scimark_monte_carlo, sympy_str, comprehensions, logging_format, fannkuch, mako
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250629-3.15.0a0-0d5e4e2-JIT/bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x
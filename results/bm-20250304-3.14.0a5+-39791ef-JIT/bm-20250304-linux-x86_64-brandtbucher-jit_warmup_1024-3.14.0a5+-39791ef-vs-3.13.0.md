# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_warmup_1024
- machine: linux-x86_64
- commit hash: 39791ef
- commit date: 2025-03-04
- overall geometric mean: 1.041x faster
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 262 ms: 1.01x faster                                                    |
| docutils       | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                  |
| html5lib       | 63.4 ms                                                | 62.3 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                    |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                    |
| async_tree_io              | 838 ms                                                 | 608 ms: 1.38x faster                                                    |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                    |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                    |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                    |
| async_generators           | 433 ms                                                 | 404 ms: 1.07x faster                                                    |
| coroutines                 | 22.2 ms                                                | 24.0 ms: 1.08x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.9 ms: 1.13x faster                                                   |
| nbody          | 87.7 ms                                                | 91.4 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.46 ms: 1.09x faster                                                   |
| regex_v8       | 26.9 ms                                                | 25.1 ms: 1.07x faster                                                   |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                  | 1.05x faster                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.85 sec: 1.15x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 78.9 ms: 1.10x faster                                                   |
| xml_etree_process    | 60.5 ms                                                | 55.5 ms: 1.09x faster                                                   |
| xml_etree_parse      | 154 ms                                                 | 147 ms: 1.05x faster                                                    |
| unpickle_pure_python | 213 us                                                 | 203 us: 1.05x faster                                                    |
| xml_etree_iterparse  | 101 ms                                                 | 100 ms: 1.01x faster                                                    |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.06x slower                                                    |
| json_loads           | 27.2 us                                                | 30.0 us: 1.11x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.14 ms: 1.02x slower                                                   |
| python_startup         | 12.7 ms                                                | 13.0 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                   |
| genshi_text     | 22.6 ms                                                | 21.7 ms: 1.04x faster                                                   |
| django_template | 31.7 ms                                                | 31.5 ms: 1.01x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                    |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                    |
| async_tree_io              | 838 ms                                                 | 608 ms: 1.38x faster                                                    |
| deepcopy                   | 354 us                                                 | 263 us: 1.35x faster                                                    |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                    |
| deepcopy_memo              | 38.4 us                                                | 28.8 us: 1.33x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                    |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.21x faster                                                   |
| scimark_fft                | 367 ms                                                 | 310 ms: 1.18x faster                                                    |
| spectral_norm              | 113 ms                                                 | 96.0 ms: 1.18x faster                                                   |
| go                         | 141 ms                                                 | 120 ms: 1.17x faster                                                    |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                    |
| tomli_loads                | 2.12 sec                                               | 1.85 sec: 1.15x faster                                                  |
| float                      | 78.7 ms                                                | 69.9 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                    |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                    |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.56 ms: 1.10x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 78.9 ms: 1.10x faster                                                   |
| telco                      | 8.40 ms                                                | 7.70 ms: 1.09x faster                                                   |
| pyflate                    | 470 ms                                                 | 431 ms: 1.09x faster                                                    |
| xml_etree_process          | 60.5 ms                                                | 55.5 ms: 1.09x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.46 ms: 1.09x faster                                                   |
| richards                   | 47.5 ms                                                | 44.0 ms: 1.08x faster                                                   |
| async_generators           | 433 ms                                                 | 404 ms: 1.07x faster                                                    |
| gc_traversal               | 4.90 ms                                                | 4.58 ms: 1.07x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 25.1 ms: 1.07x faster                                                   |
| richards_super             | 53.7 ms                                                | 50.4 ms: 1.07x faster                                                   |
| mako                       | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.75 us: 1.05x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 147 ms: 1.05x faster                                                    |
| unpickle_pure_python       | 213 us                                                 | 203 us: 1.05x faster                                                    |
| thrift                     | 800 us                                                 | 764 us: 1.05x faster                                                    |
| bpe_tokeniser              | 4.69 sec                                               | 4.49 sec: 1.05x faster                                                  |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                    |
| genshi_text                | 22.6 ms                                                | 21.7 ms: 1.04x faster                                                   |
| crypto_pyaes               | 74.7 ms                                                | 71.8 ms: 1.04x faster                                                   |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.02x faster                                                  |
| generators                 | 28.8 ms                                                | 28.1 ms: 1.02x faster                                                   |
| mdp                        | 2.54 sec                                               | 2.49 sec: 1.02x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.56 us: 1.02x faster                                                   |
| shortest_path              | 487 ms                                                 | 478 ms: 1.02x faster                                                    |
| html5lib                   | 63.4 ms                                                | 62.3 ms: 1.02x faster                                                   |
| 2to3                       | 266 ms                                                 | 262 ms: 1.01x faster                                                    |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                    |
| xml_etree_iterparse        | 101 ms                                                 | 100 ms: 1.01x faster                                                    |
| create_gc_cycles           | 2.45 ms                                                | 2.42 ms: 1.01x faster                                                   |
| logging_format             | 6.23 us                                                | 6.18 us: 1.01x faster                                                   |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.01x faster                                                    |
| django_template            | 31.7 ms                                                | 31.5 ms: 1.01x faster                                                   |
| sqlglot_optimize           | 53.4 ms                                                | 53.7 ms: 1.01x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.01x slower                                                    |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.1 ms: 1.01x slower                                                   |
| sympy_str                  | 273 ms                                                 | 276 ms: 1.01x slower                                                    |
| fannkuch                   | 394 ms                                                 | 399 ms: 1.01x slower                                                    |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.02x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 738 ms: 1.02x slower                                                    |
| python_startup_no_site     | 7.00 ms                                                | 7.14 ms: 1.02x slower                                                   |
| sympy_integrate            | 19.8 ms                                                | 20.3 ms: 1.02x slower                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 68.4 ms: 1.02x slower                                                   |
| coverage                   | 82.8 ms                                                | 84.8 ms: 1.02x slower                                                   |
| python_startup             | 12.7 ms                                                | 13.0 ms: 1.02x slower                                                   |
| deltablue                  | 3.19 ms                                                | 3.27 ms: 1.02x slower                                                   |
| chaos                      | 58.0 ms                                                | 59.5 ms: 1.03x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.24 ms: 1.03x slower                                                   |
| sqlglot_transpile          | 1.57 ms                                                | 1.62 ms: 1.03x slower                                                   |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                                    |
| sqlglot_parse              | 1.26 ms                                                | 1.31 ms: 1.03x slower                                                   |
| dulwich_log                | 64.6 ms                                                | 66.7 ms: 1.03x slower                                                   |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.03x slower                                                    |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.04x slower                                                    |
| docutils                   | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                  |
| sympy_expand               | 456 ms                                                 | 475 ms: 1.04x slower                                                    |
| logging_silent             | 101 ns                                                 | 105 ns: 1.04x slower                                                    |
| nbody                      | 87.7 ms                                                | 91.4 ms: 1.04x slower                                                   |
| connected_components       | 447 ms                                                 | 467 ms: 1.04x slower                                                    |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.06x slower                                                    |
| bench_thread_pool          | 818 us                                                 | 880 us: 1.08x slower                                                    |
| comprehensions             | 16.5 us                                                | 17.8 us: 1.08x slower                                                   |
| coroutines                 | 22.2 ms                                                | 24.0 ms: 1.08x slower                                                   |
| json_loads                 | 27.2 us                                                | 30.0 us: 1.11x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.12x slower                                                   |
| many_optionals             | 857 us                                                 | 968 us: 1.13x slower                                                    |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 81.8 ms: 3.41x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (9): sphinx, nqueens, sqlalchemy_declarative, pidigits, asyncio_websockets, genshi_xml, json, regex_dna, scimark_sor
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 99.87% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
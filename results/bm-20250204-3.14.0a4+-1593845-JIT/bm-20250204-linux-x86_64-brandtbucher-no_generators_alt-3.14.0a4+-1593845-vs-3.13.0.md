# Results vs. 3.13.0

- fork: brandtbucher
- ref: no_generators_alt
- machine: linux-x86_64
- commit hash: 1593845
- commit date: 2025-02-04
- overall geometric mean: 1.037x faster
- HPT reliability: 97.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                                      |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 625 ms: 1.38x faster                                                      |
| async_tree_io              | 838 ms                                                 | 628 ms: 1.33x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 329 ms: 1.33x faster                                                      |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                                      |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                                      |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.6 ms: 1.16x faster                                                     |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| nbody          | 87.7 ms                                                | 90.0 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 2.98 ms: 1.26x faster                                                     |
| regex_dna      | 220 ms                                                 | 194 ms: 1.13x faster                                                      |
| regex_v8       | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                     |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.82 sec: 1.16x faster                                                    |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                      |
| xml_etree_generate   | 86.8 ms                                                | 79.3 ms: 1.10x faster                                                     |
| xml_etree_process    | 60.5 ms                                                | 56.4 ms: 1.07x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 95.2 ms: 1.06x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 201 us: 1.06x faster                                                      |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.05x slower                                                      |
| json_loads           | 27.2 us                                                | 28.7 us: 1.05x slower                                                     |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.12x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                     |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.00 ms: 1.07x faster                                                    |
| django_template | 31.7 ms                                                | 33.1 ms: 1.05x slower                                                     |
| genshi_text     | 22.6 ms                                                | 24.0 ms: 1.06x slower                                                     |
| genshi_xml      | 50.5 ms                                                | 62.1 ms: 1.23x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 625 ms: 1.38x faster                                                      |
| async_tree_io              | 838 ms                                                 | 628 ms: 1.33x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 329 ms: 1.33x faster                                                      |
| deepcopy                   | 354 us                                                 | 271 us: 1.31x faster                                                      |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                      |
| deepcopy_memo              | 38.4 us                                                | 30.2 us: 1.27x faster                                                     |
| regex_effbot               | 3.77 ms                                                | 2.98 ms: 1.26x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                      |
| spectral_norm              | 113 ms                                                 | 93.4 ms: 1.21x faster                                                     |
| scimark_fft                | 367 ms                                                 | 310 ms: 1.18x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.77 us: 1.17x faster                                                     |
| float                      | 78.7 ms                                                | 67.6 ms: 1.16x faster                                                     |
| tomli_loads                | 2.12 sec                                               | 1.82 sec: 1.16x faster                                                    |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                                      |
| regex_dna                  | 220 ms                                                 | 194 ms: 1.13x faster                                                      |
| regex_v8                   | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                                      |
| go                         | 141 ms                                                 | 126 ms: 1.12x faster                                                      |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                      |
| telco                      | 8.40 ms                                                | 7.59 ms: 1.11x faster                                                     |
| xml_etree_generate         | 86.8 ms                                                | 79.3 ms: 1.10x faster                                                     |
| pylint                     | 312 ms                                                 | 286 ms: 1.09x faster                                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.63 ms: 1.09x faster                                                     |
| pathlib                    | 17.4 ms                                                | 16.0 ms: 1.09x faster                                                     |
| richards                   | 47.5 ms                                                | 44.2 ms: 1.07x faster                                                     |
| xml_etree_process          | 60.5 ms                                                | 56.4 ms: 1.07x faster                                                     |
| richards_super             | 53.7 ms                                                | 50.2 ms: 1.07x faster                                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.39 sec: 1.07x faster                                                    |
| mako                       | 10.7 ms                                                | 10.00 ms: 1.07x faster                                                    |
| crypto_pyaes               | 74.7 ms                                                | 70.1 ms: 1.06x faster                                                     |
| scimark_sor                | 122 ms                                                 | 115 ms: 1.06x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 95.2 ms: 1.06x faster                                                     |
| unpickle_pure_python       | 213 us                                                 | 201 us: 1.06x faster                                                      |
| scimark_monte_carlo        | 66.8 ms                                                | 63.3 ms: 1.06x faster                                                     |
| sqlite_synth               | 2.90 us                                                | 2.76 us: 1.05x faster                                                     |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                                      |
| json                       | 5.32 ms                                                | 5.13 ms: 1.04x faster                                                     |
| thrift                     | 800 us                                                 | 773 us: 1.03x faster                                                      |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                                    |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                      |
| pyflate                    | 470 ms                                                 | 460 ms: 1.02x faster                                                      |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                                      |
| connected_components       | 447 ms                                                 | 439 ms: 1.02x faster                                                      |
| logging_format             | 6.23 us                                                | 6.13 us: 1.02x faster                                                     |
| shortest_path              | 487 ms                                                 | 481 ms: 1.01x faster                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                                      |
| logging_simple             | 5.65 us                                                | 5.60 us: 1.01x faster                                                     |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                      |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                     |
| fannkuch                   | 394 ms                                                 | 391 ms: 1.01x faster                                                      |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                                     |
| gc_traversal               | 4.90 ms                                                | 4.94 ms: 1.01x slower                                                     |
| sqlglot_optimize           | 53.4 ms                                                | 54.0 ms: 1.01x slower                                                     |
| python_startup_no_site     | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                     |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.01x slower                                                    |
| sqlglot_parse              | 1.26 ms                                                | 1.28 ms: 1.02x slower                                                     |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                     |
| typing_runtime_protocols   | 160 us                                                 | 163 us: 1.02x slower                                                      |
| pycparser                  | 1.20 sec                                               | 1.22 sec: 1.02x slower                                                    |
| pprint_safe_repr           | 727 ms                                                 | 740 ms: 1.02x slower                                                      |
| sympy_str                  | 273 ms                                                 | 278 ms: 1.02x slower                                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                     |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                      |
| chaos                      | 58.0 ms                                                | 59.3 ms: 1.02x slower                                                     |
| sympy_sum                  | 150 ms                                                 | 154 ms: 1.02x slower                                                      |
| nbody                      | 87.7 ms                                                | 90.0 ms: 1.03x slower                                                     |
| generators                 | 28.8 ms                                                | 29.6 ms: 1.03x slower                                                     |
| sympy_expand               | 456 ms                                                 | 469 ms: 1.03x slower                                                      |
| sympy_integrate            | 19.8 ms                                                | 20.4 ms: 1.03x slower                                                     |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.04x slower                                                     |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                    |
| django_template            | 31.7 ms                                                | 33.1 ms: 1.05x slower                                                     |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.05x slower                                                      |
| json_loads                 | 27.2 us                                                | 28.7 us: 1.05x slower                                                     |
| genshi_text                | 22.6 ms                                                | 24.0 ms: 1.06x slower                                                     |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                                     |
| dulwich_log                | 64.6 ms                                                | 69.2 ms: 1.07x slower                                                     |
| coverage                   | 82.8 ms                                                | 89.6 ms: 1.08x slower                                                     |
| bench_thread_pool          | 818 us                                                 | 894 us: 1.09x slower                                                      |
| nqueens                    | 80.9 ms                                                | 88.7 ms: 1.10x slower                                                     |
| logging_silent             | 101 ns                                                 | 111 ns: 1.10x slower                                                      |
| deltablue                  | 3.19 ms                                                | 3.52 ms: 1.10x slower                                                     |
| raytrace                   | 262 ms                                                 | 290 ms: 1.11x slower                                                      |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.12x slower                                                     |
| many_optionals             | 857 us                                                 | 962 us: 1.12x slower                                                      |
| hexiom                     | 6.08 ms                                                | 7.39 ms: 1.22x slower                                                     |
| genshi_xml                 | 50.5 ms                                                | 62.1 ms: 1.23x slower                                                     |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.39x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (5): meteor_contest, asyncio_websockets, mdp, html5lib, sphinx
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.037x faster

# HPT report

- Reliability score: 97.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
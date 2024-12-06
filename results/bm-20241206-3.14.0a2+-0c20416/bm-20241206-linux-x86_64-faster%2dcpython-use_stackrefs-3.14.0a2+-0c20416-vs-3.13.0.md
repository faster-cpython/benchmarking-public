# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 0c20416
- commit date: 2024-12-06
- overall geometric mean: 1.019x faster
- HPT reliability: 57.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                                      |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                    |
| html5lib       | 63.4 ms                                                | 65.2 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                      |
| async_tree_io              | 838 ms                                                 | 605 ms: 1.39x faster                                                      |
| async_tree_memoization_tg  | 463 ms                                                 | 335 ms: 1.38x faster                                                      |
| async_tree_none            | 350 ms                                                 | 274 ms: 1.28x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 346 ms: 1.26x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 263 ms: 1.21x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 500 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                                      |
| async_generators           | 433 ms                                                 | 428 ms: 1.01x faster                                                      |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                      |
| coroutines                 | 22.2 ms                                                | 24.5 ms: 1.10x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.18x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                                      |
| nbody          | 87.7 ms                                                | 98.4 ms: 1.12x slower                                                     |
| Geometric mean | (ref)                                                  | 1.04x slower                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.50 ms: 1.08x faster                                                     |
| regex_v8       | 26.9 ms                                                | 25.5 ms: 1.05x faster                                                     |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                      |
| regex_dna      | 220 ms                                                 | 222 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 143 ms: 1.08x faster                                                      |
| json_loads           | 27.2 us                                                | 26.0 us: 1.04x faster                                                     |
| xml_etree_process    | 60.5 ms                                                | 58.7 ms: 1.03x faster                                                     |
| xml_etree_generate   | 86.8 ms                                                | 84.5 ms: 1.03x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 99.4 ms: 1.02x faster                                                     |
| tomli_loads          | 2.12 sec                                               | 2.10 sec: 1.01x faster                                                    |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                      |
| pickle_pure_python   | 302 us                                                 | 331 us: 1.09x slower                                                      |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.03 ms: 1.00x slower                                                     |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 22.5 ms: 1.00x faster                                                     |
| genshi_xml      | 50.5 ms                                                | 50.7 ms: 1.00x slower                                                     |
| django_template | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                     |
| mako            | 10.7 ms                                                | 11.7 ms: 1.09x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                      |
| async_tree_io              | 838 ms                                                 | 605 ms: 1.39x faster                                                      |
| async_tree_memoization_tg  | 463 ms                                                 | 335 ms: 1.38x faster                                                      |
| deepcopy                   | 354 us                                                 | 268 us: 1.32x faster                                                      |
| async_tree_none            | 350 ms                                                 | 274 ms: 1.28x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 346 ms: 1.26x faster                                                      |
| deepcopy_memo              | 38.4 us                                                | 30.6 us: 1.25x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 263 ms: 1.21x faster                                                      |
| go                         | 141 ms                                                 | 118 ms: 1.19x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.81 us: 1.16x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 500 ms: 1.15x faster                                                      |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                                      |
| json                       | 5.32 ms                                                | 4.81 ms: 1.11x faster                                                     |
| create_gc_cycles           | 2.45 ms                                                | 2.24 ms: 1.10x faster                                                     |
| regex_effbot               | 3.77 ms                                                | 3.50 ms: 1.08x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                                    |
| xml_etree_parse            | 154 ms                                                 | 143 ms: 1.08x faster                                                      |
| telco                      | 8.40 ms                                                | 7.86 ms: 1.07x faster                                                     |
| k_core                     | 2.37 sec                                               | 2.22 sec: 1.07x faster                                                    |
| gc_traversal               | 4.90 ms                                                | 4.61 ms: 1.06x faster                                                     |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                                     |
| regex_v8                   | 26.9 ms                                                | 25.5 ms: 1.05x faster                                                     |
| richards                   | 47.5 ms                                                | 45.6 ms: 1.04x faster                                                     |
| json_loads                 | 27.2 us                                                | 26.0 us: 1.04x faster                                                     |
| richards_super             | 53.7 ms                                                | 51.8 ms: 1.04x faster                                                     |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                                      |
| xml_etree_process          | 60.5 ms                                                | 58.7 ms: 1.03x faster                                                     |
| thrift                     | 800 us                                                 | 778 us: 1.03x faster                                                      |
| xml_etree_generate         | 86.8 ms                                                | 84.5 ms: 1.03x faster                                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.56 sec: 1.03x faster                                                    |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 99.4 ms: 1.02x faster                                                     |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                      |
| async_generators           | 433 ms                                                 | 428 ms: 1.01x faster                                                      |
| crypto_pyaes               | 74.7 ms                                                | 74.0 ms: 1.01x faster                                                     |
| tomli_loads                | 2.12 sec                                               | 2.10 sec: 1.01x faster                                                    |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                      |
| genshi_text                | 22.6 ms                                                | 22.5 ms: 1.00x faster                                                     |
| python_startup_no_site     | 7.00 ms                                                | 7.03 ms: 1.00x slower                                                     |
| genshi_xml                 | 50.5 ms                                                | 50.7 ms: 1.00x slower                                                     |
| logging_format             | 6.23 us                                                | 6.27 us: 1.01x slower                                                     |
| sqlglot_normalize          | 108 ms                                                 | 109 ms: 1.01x slower                                                      |
| scimark_lu                 | 114 ms                                                 | 115 ms: 1.01x slower                                                      |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                      |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                    |
| sympy_integrate            | 19.8 ms                                                | 20.0 ms: 1.01x slower                                                     |
| regex_dna                  | 220 ms                                                 | 222 ms: 1.01x slower                                                      |
| django_template            | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                     |
| dulwich_log                | 64.6 ms                                                | 65.3 ms: 1.01x slower                                                     |
| sympy_expand               | 456 ms                                                 | 462 ms: 1.01x slower                                                      |
| coverage                   | 82.8 ms                                                | 84.0 ms: 1.01x slower                                                     |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                                      |
| connected_components       | 447 ms                                                 | 453 ms: 1.01x slower                                                      |
| sqlglot_optimize           | 53.4 ms                                                | 54.2 ms: 1.02x slower                                                     |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                      |
| shortest_path              | 487 ms                                                 | 496 ms: 1.02x slower                                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.13 ms: 1.02x slower                                                     |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.03x slower                                                      |
| deltablue                  | 3.19 ms                                                | 3.28 ms: 1.03x slower                                                     |
| raytrace                   | 262 ms                                                 | 269 ms: 1.03x slower                                                      |
| html5lib                   | 63.4 ms                                                | 65.2 ms: 1.03x slower                                                     |
| scimark_fft                | 367 ms                                                 | 379 ms: 1.03x slower                                                      |
| scimark_sor                | 122 ms                                                 | 126 ms: 1.04x slower                                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.63 ms: 1.04x slower                                                     |
| sqlglot_parse              | 1.26 ms                                                | 1.31 ms: 1.04x slower                                                     |
| spectral_norm              | 113 ms                                                 | 118 ms: 1.04x slower                                                      |
| scimark_monte_carlo        | 66.8 ms                                                | 69.8 ms: 1.04x slower                                                     |
| comprehensions             | 16.5 us                                                | 17.3 us: 1.05x slower                                                     |
| hexiom                     | 6.08 ms                                                | 6.36 ms: 1.05x slower                                                     |
| pyflate                    | 470 ms                                                 | 492 ms: 1.05x slower                                                      |
| bench_thread_pool          | 818 us                                                 | 857 us: 1.05x slower                                                      |
| nqueens                    | 80.9 ms                                                | 84.9 ms: 1.05x slower                                                     |
| pprint_safe_repr           | 727 ms                                                 | 769 ms: 1.06x slower                                                      |
| pprint_pformat             | 1.48 sec                                               | 1.57 sec: 1.06x slower                                                    |
| mdp                        | 2.54 sec                                               | 2.72 sec: 1.07x slower                                                    |
| chaos                      | 58.0 ms                                                | 62.4 ms: 1.07x slower                                                     |
| fannkuch                   | 394 ms                                                 | 429 ms: 1.09x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 331 us: 1.09x slower                                                      |
| mako                       | 10.7 ms                                                | 11.7 ms: 1.09x slower                                                     |
| coroutines                 | 22.2 ms                                                | 24.5 ms: 1.10x slower                                                     |
| many_optionals             | 857 us                                                 | 956 us: 1.12x slower                                                      |
| nbody                      | 87.7 ms                                                | 98.4 ms: 1.12x slower                                                     |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                     |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 78.7 ms: 3.28x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (10): djangocms, float, sympy_str, sphinx, sqlite_synth, sqlalchemy_imperative, logging_simple, logging_silent, generators, meteor_contest
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.019x faster

# HPT report

- Reliability score: 57.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x
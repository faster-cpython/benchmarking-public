# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: f5dec96
- commit date: 2024-12-06
- overall geometric mean: 1.024x faster
- HPT reliability: 93.37%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                                      |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                    |
| html5lib       | 63.4 ms                                                | 63.0 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io              | 838 ms                                                 | 605 ms: 1.39x faster                                                      |
| async_tree_memoization_tg  | 463 ms                                                 | 335 ms: 1.38x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 624 ms: 1.38x faster                                                      |
| async_tree_none            | 350 ms                                                 | 274 ms: 1.28x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 347 ms: 1.26x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 265 ms: 1.20x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 501 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 489 ms: 1.11x faster                                                      |
| async_generators           | 433 ms                                                 | 429 ms: 1.01x faster                                                      |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                      |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.18x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                                      |
| nbody          | 87.7 ms                                                | 97.1 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                  | 1.04x slower                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.35 ms: 1.13x faster                                                     |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                      |
| regex_v8       | 26.9 ms                                                | 26.4 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 145 ms: 1.06x faster                                                      |
| json_loads           | 27.2 us                                                | 26.2 us: 1.04x faster                                                     |
| xml_etree_process    | 60.5 ms                                                | 58.6 ms: 1.03x faster                                                     |
| xml_etree_generate   | 86.8 ms                                                | 84.7 ms: 1.03x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 99.2 ms: 1.02x faster                                                     |
| tomli_loads          | 2.12 sec                                               | 2.10 sec: 1.01x faster                                                    |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                      |
| pickle_pure_python   | 302 us                                                 | 326 us: 1.08x slower                                                      |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.09 ms: 1.01x slower                                                     |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 22.1 ms: 1.02x faster                                                     |
| genshi_xml      | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                     |
| django_template | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                     |
| mako            | 10.7 ms                                                | 11.8 ms: 1.11x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io              | 838 ms                                                 | 605 ms: 1.39x faster                                                      |
| async_tree_memoization_tg  | 463 ms                                                 | 335 ms: 1.38x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 624 ms: 1.38x faster                                                      |
| deepcopy                   | 354 us                                                 | 263 us: 1.35x faster                                                      |
| deepcopy_memo              | 38.4 us                                                | 30.0 us: 1.28x faster                                                     |
| async_tree_none            | 350 ms                                                 | 274 ms: 1.28x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 347 ms: 1.26x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 265 ms: 1.20x faster                                                      |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.79 us: 1.16x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 501 ms: 1.14x faster                                                      |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                      |
| regex_effbot               | 3.77 ms                                                | 3.35 ms: 1.13x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 489 ms: 1.11x faster                                                      |
| json                       | 5.32 ms                                                | 4.83 ms: 1.10x faster                                                     |
| create_gc_cycles           | 2.45 ms                                                | 2.27 ms: 1.08x faster                                                     |
| telco                      | 8.40 ms                                                | 7.81 ms: 1.08x faster                                                     |
| gc_traversal               | 4.90 ms                                                | 4.57 ms: 1.07x faster                                                     |
| k_core                     | 2.37 sec                                               | 2.21 sec: 1.07x faster                                                    |
| xml_etree_parse            | 154 ms                                                 | 145 ms: 1.06x faster                                                      |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                                     |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                                      |
| richards                   | 47.5 ms                                                | 45.7 ms: 1.04x faster                                                     |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                      |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                    |
| json_loads                 | 27.2 us                                                | 26.2 us: 1.04x faster                                                     |
| richards_super             | 53.7 ms                                                | 51.9 ms: 1.04x faster                                                     |
| logging_silent             | 101 ns                                                 | 97.5 ns: 1.04x faster                                                     |
| xml_etree_process          | 60.5 ms                                                | 58.6 ms: 1.03x faster                                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.57 sec: 1.03x faster                                                    |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                      |
| crypto_pyaes               | 74.7 ms                                                | 72.8 ms: 1.03x faster                                                     |
| connected_components       | 447 ms                                                 | 436 ms: 1.03x faster                                                      |
| xml_etree_generate         | 86.8 ms                                                | 84.7 ms: 1.03x faster                                                     |
| genshi_text                | 22.6 ms                                                | 22.1 ms: 1.02x faster                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 99.2 ms: 1.02x faster                                                     |
| thrift                     | 800 us                                                 | 785 us: 1.02x faster                                                      |
| regex_v8                   | 26.9 ms                                                | 26.4 ms: 1.02x faster                                                     |
| genshi_xml                 | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                     |
| shortest_path              | 487 ms                                                 | 479 ms: 1.02x faster                                                      |
| sqlite_synth               | 2.90 us                                                | 2.86 us: 1.02x faster                                                     |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                      |
| scimark_lu                 | 114 ms                                                 | 113 ms: 1.01x faster                                                      |
| async_generators           | 433 ms                                                 | 429 ms: 1.01x faster                                                      |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.01x faster                                                      |
| html5lib                   | 63.4 ms                                                | 63.0 ms: 1.01x faster                                                     |
| tomli_loads                | 2.12 sec                                               | 2.10 sec: 1.01x faster                                                    |
| coverage                   | 82.8 ms                                                | 83.2 ms: 1.00x slower                                                     |
| sqlglot_optimize           | 53.4 ms                                                | 53.7 ms: 1.01x slower                                                     |
| sympy_expand               | 456 ms                                                 | 459 ms: 1.01x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                      |
| dulwich_log                | 64.6 ms                                                | 65.1 ms: 1.01x slower                                                     |
| django_template            | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                     |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                    |
| sympy_integrate            | 19.8 ms                                                | 20.0 ms: 1.01x slower                                                     |
| logging_simple             | 5.65 us                                                | 5.71 us: 1.01x slower                                                     |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                                      |
| generators                 | 28.8 ms                                                | 29.1 ms: 1.01x slower                                                     |
| python_startup_no_site     | 7.00 ms                                                | 7.09 ms: 1.01x slower                                                     |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                     |
| pyflate                    | 470 ms                                                 | 476 ms: 1.01x slower                                                      |
| sqlglot_parse              | 1.26 ms                                                | 1.28 ms: 1.01x slower                                                     |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                     |
| deltablue                  | 3.19 ms                                                | 3.25 ms: 1.02x slower                                                     |
| hexiom                     | 6.08 ms                                                | 6.19 ms: 1.02x slower                                                     |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                                      |
| scimark_monte_carlo        | 66.8 ms                                                | 68.8 ms: 1.03x slower                                                     |
| mdp                        | 2.54 sec                                               | 2.62 sec: 1.03x slower                                                    |
| spectral_norm              | 113 ms                                                 | 117 ms: 1.03x slower                                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.19 ms: 1.03x slower                                                     |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.04x slower                                                      |
| pprint_safe_repr           | 727 ms                                                 | 755 ms: 1.04x slower                                                      |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                     |
| pprint_pformat             | 1.48 sec                                               | 1.54 sec: 1.04x slower                                                    |
| bench_thread_pool          | 818 us                                                 | 855 us: 1.05x slower                                                      |
| chaos                      | 58.0 ms                                                | 61.4 ms: 1.06x slower                                                     |
| nqueens                    | 80.9 ms                                                | 85.6 ms: 1.06x slower                                                     |
| fannkuch                   | 394 ms                                                 | 423 ms: 1.08x slower                                                      |
| scimark_sor                | 122 ms                                                 | 132 ms: 1.08x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 326 us: 1.08x slower                                                      |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                     |
| mako                       | 10.7 ms                                                | 11.8 ms: 1.11x slower                                                     |
| nbody                      | 87.7 ms                                                | 97.1 ms: 1.11x slower                                                     |
| many_optionals             | 857 us                                                 | 959 us: 1.12x slower                                                      |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.13x slower                                                     |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 79.1 ms: 3.30x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (9): sympy_str, regex_dna, sphinx, sqlglot_normalize, scimark_fft, djangocms, float, sqlalchemy_imperative, logging_format
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.024x faster

# HPT report

- Reliability score: 93.37% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x
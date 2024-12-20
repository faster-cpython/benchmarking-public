# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: ad7e1e6
- commit date: 2024-12-20
- overall geometric mean: 1.022x faster
- HPT reliability: 98.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.03x faster                                                      |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                    |
| html5lib       | 63.4 ms                                                | 63.7 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 629 ms: 1.37x faster                                                      |
| async_tree_io              | 838 ms                                                 | 629 ms: 1.33x faster                                                      |
| async_tree_none            | 350 ms                                                 | 270 ms: 1.30x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 342 ms: 1.28x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                      |
| async_generators           | 433 ms                                                 | 429 ms: 1.01x faster                                                      |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                      |
| nbody          | 87.7 ms                                                | 100 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x slower                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.54 ms: 1.06x faster                                                     |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                      |
| regex_v8       | 26.9 ms                                                | 26.5 ms: 1.01x faster                                                     |
| regex_dna      | 220 ms                                                 | 223 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.11x faster                                                      |
| tomli_loads          | 2.12 sec                                               | 1.98 sec: 1.07x faster                                                    |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                                     |
| json_loads           | 27.2 us                                                | 26.5 us: 1.03x faster                                                     |
| xml_etree_generate   | 86.8 ms                                                | 84.7 ms: 1.03x faster                                                     |
| xml_etree_process    | 60.5 ms                                                | 59.4 ms: 1.02x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 221 us: 1.04x slower                                                      |
| pickle_pure_python   | 302 us                                                 | 331 us: 1.09x slower                                                      |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.14x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                     |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 22.3 ms: 1.01x faster                                                     |
| django_template | 31.7 ms                                                | 33.0 ms: 1.04x slower                                                     |
| mako            | 10.7 ms                                                | 12.2 ms: 1.14x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                              |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 629 ms: 1.37x faster                                                      |
| async_tree_io              | 838 ms                                                 | 629 ms: 1.33x faster                                                      |
| deepcopy                   | 354 us                                                 | 267 us: 1.33x faster                                                      |
| async_tree_none            | 350 ms                                                 | 270 ms: 1.30x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 342 ms: 1.28x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                      |
| deepcopy_memo              | 38.4 us                                                | 31.0 us: 1.24x faster                                                     |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.76 us: 1.18x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                      |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.11x faster                                                      |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                                      |
| richards                   | 47.5 ms                                                | 44.5 ms: 1.07x faster                                                     |
| spectral_norm              | 113 ms                                                 | 106 ms: 1.07x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 1.98 sec: 1.07x faster                                                    |
| json                       | 5.32 ms                                                | 4.99 ms: 1.07x faster                                                     |
| telco                      | 8.40 ms                                                | 7.88 ms: 1.07x faster                                                     |
| regex_effbot               | 3.77 ms                                                | 3.54 ms: 1.06x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                                    |
| richards_super             | 53.7 ms                                                | 51.1 ms: 1.05x faster                                                     |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                    |
| scimark_fft                | 367 ms                                                 | 353 ms: 1.04x faster                                                      |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.04x faster                                                     |
| 2to3                       | 266 ms                                                 | 257 ms: 1.03x faster                                                      |
| thrift                     | 800 us                                                 | 776 us: 1.03x faster                                                      |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.90 ms: 1.03x faster                                                     |
| json_loads                 | 27.2 us                                                | 26.5 us: 1.03x faster                                                     |
| xml_etree_generate         | 86.8 ms                                                | 84.7 ms: 1.03x faster                                                     |
| mdp                        | 2.54 sec                                               | 2.48 sec: 1.02x faster                                                    |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                      |
| connected_components       | 447 ms                                                 | 438 ms: 1.02x faster                                                      |
| shortest_path              | 487 ms                                                 | 478 ms: 1.02x faster                                                      |
| xml_etree_process          | 60.5 ms                                                | 59.4 ms: 1.02x faster                                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.61 sec: 1.02x faster                                                    |
| generators                 | 28.8 ms                                                | 28.3 ms: 1.02x faster                                                     |
| regex_v8                   | 26.9 ms                                                | 26.5 ms: 1.01x faster                                                     |
| crypto_pyaes               | 74.7 ms                                                | 73.7 ms: 1.01x faster                                                     |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                      |
| genshi_text                | 22.6 ms                                                | 22.3 ms: 1.01x faster                                                     |
| async_generators           | 433 ms                                                 | 429 ms: 1.01x faster                                                      |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                                     |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                      |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.01x faster                                                      |
| create_gc_cycles           | 2.45 ms                                                | 2.44 ms: 1.00x faster                                                     |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                      |
| gc_traversal               | 4.90 ms                                                | 4.92 ms: 1.00x slower                                                     |
| html5lib                   | 63.4 ms                                                | 63.7 ms: 1.01x slower                                                     |
| sympy_integrate            | 19.8 ms                                                | 20.0 ms: 1.01x slower                                                     |
| pyflate                    | 470 ms                                                 | 475 ms: 1.01x slower                                                      |
| coverage                   | 82.8 ms                                                | 83.8 ms: 1.01x slower                                                     |
| python_startup_no_site     | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                     |
| sympy_expand               | 456 ms                                                 | 463 ms: 1.01x slower                                                      |
| regex_dna                  | 220 ms                                                 | 223 ms: 1.02x slower                                                      |
| logging_format             | 6.23 us                                                | 6.33 us: 1.02x slower                                                     |
| sqlglot_parse              | 1.26 ms                                                | 1.29 ms: 1.02x slower                                                     |
| scimark_sor                | 122 ms                                                 | 124 ms: 1.02x slower                                                      |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                     |
| logging_simple             | 5.65 us                                                | 5.77 us: 1.02x slower                                                     |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                    |
| sqlglot_transpile          | 1.57 ms                                                | 1.61 ms: 1.02x slower                                                     |
| typing_runtime_protocols   | 160 us                                                 | 165 us: 1.03x slower                                                      |
| nqueens                    | 80.9 ms                                                | 83.5 ms: 1.03x slower                                                     |
| unpickle_pure_python       | 213 us                                                 | 221 us: 1.04x slower                                                      |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                      |
| django_template            | 31.7 ms                                                | 33.0 ms: 1.04x slower                                                     |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                                      |
| deltablue                  | 3.19 ms                                                | 3.34 ms: 1.04x slower                                                     |
| scimark_monte_carlo        | 66.8 ms                                                | 69.8 ms: 1.05x slower                                                     |
| pprint_pformat             | 1.48 sec                                               | 1.55 sec: 1.05x slower                                                    |
| pprint_safe_repr           | 727 ms                                                 | 767 ms: 1.06x slower                                                      |
| hexiom                     | 6.08 ms                                                | 6.41 ms: 1.06x slower                                                     |
| comprehensions             | 16.5 us                                                | 17.5 us: 1.06x slower                                                     |
| bench_thread_pool          | 818 us                                                 | 873 us: 1.07x slower                                                      |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                                     |
| chaos                      | 58.0 ms                                                | 62.6 ms: 1.08x slower                                                     |
| fannkuch                   | 394 ms                                                 | 427 ms: 1.09x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 331 us: 1.09x slower                                                      |
| many_optionals             | 857 us                                                 | 962 us: 1.12x slower                                                      |
| mako                       | 10.7 ms                                                | 12.2 ms: 1.14x slower                                                     |
| nbody                      | 87.7 ms                                                | 100 ms: 1.14x slower                                                      |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.14x slower                                                     |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.42x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (9): djangocms, float, logging_silent, sympy_str, dulwich_log, sqlglot_optimize, asyncio_websockets, genshi_xml, sphinx
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241220-3.14.0a3+-ad7e1e6/bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6.json: mypy2

- Geometric mean (including insignificant results): 1.022x faster

# HPT report

- Reliability score: 98.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x
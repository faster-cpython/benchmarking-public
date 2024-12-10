# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 1069d98
- commit date: 2024-12-10
- overall geometric mean: 1.019x faster
- HPT reliability: 79.66%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.04x faster                                                      |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 637 ms: 1.35x faster                                                      |
| async_tree_io              | 838 ms                                                 | 639 ms: 1.31x faster                                                      |
| async_tree_none            | 350 ms                                                 | 275 ms: 1.27x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 345 ms: 1.27x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 258 ms: 1.24x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 500 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                                      |
| async_generators           | 433 ms                                                 | 426 ms: 1.02x faster                                                      |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                      |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.08x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.18x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 79.3 ms: 1.01x slower                                                     |
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                                      |
| nbody          | 87.7 ms                                                | 99.3 ms: 1.13x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.40 ms: 1.11x faster                                                     |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                      |
| regex_dna      | 220 ms                                                 | 226 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 98.6 ms: 1.03x faster                                                     |
| xml_etree_process    | 60.5 ms                                                | 59.5 ms: 1.02x faster                                                     |
| json_loads           | 27.2 us                                                | 26.7 us: 1.02x faster                                                     |
| tomli_loads          | 2.12 sec                                               | 2.09 sec: 1.01x faster                                                    |
| xml_etree_generate   | 86.8 ms                                                | 85.8 ms: 1.01x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                      |
| pickle_pure_python   | 302 us                                                 | 326 us: 1.08x slower                                                      |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                     |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 22.2 ms: 1.02x faster                                                     |
| genshi_xml      | 50.5 ms                                                | 51.1 ms: 1.01x slower                                                     |
| django_template | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                     |
| mako            | 10.7 ms                                                | 11.9 ms: 1.12x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                                      |
| deepcopy                   | 354 us                                                 | 262 us: 1.35x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 637 ms: 1.35x faster                                                      |
| async_tree_io              | 838 ms                                                 | 639 ms: 1.31x faster                                                      |
| async_tree_none            | 350 ms                                                 | 275 ms: 1.27x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 345 ms: 1.27x faster                                                      |
| deepcopy_memo              | 38.4 us                                                | 30.4 us: 1.26x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 258 ms: 1.24x faster                                                      |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.72 us: 1.19x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 500 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                                      |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                      |
| pylint                     | 312 ms                                                 | 281 ms: 1.11x faster                                                      |
| regex_effbot               | 3.77 ms                                                | 3.40 ms: 1.11x faster                                                     |
| telco                      | 8.40 ms                                                | 7.87 ms: 1.07x faster                                                     |
| json                       | 5.32 ms                                                | 5.07 ms: 1.05x faster                                                     |
| pathlib                    | 17.4 ms                                                | 16.6 ms: 1.05x faster                                                     |
| 2to3                       | 266 ms                                                 | 257 ms: 1.04x faster                                                      |
| richards                   | 47.5 ms                                                | 46.0 ms: 1.03x faster                                                     |
| connected_components       | 447 ms                                                 | 433 ms: 1.03x faster                                                      |
| crypto_pyaes               | 74.7 ms                                                | 72.5 ms: 1.03x faster                                                     |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 98.6 ms: 1.03x faster                                                     |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                                    |
| shortest_path              | 487 ms                                                 | 475 ms: 1.02x faster                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                      |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.5 ms: 1.02x faster                                                     |
| generators                 | 28.8 ms                                                | 28.1 ms: 1.02x faster                                                     |
| thrift                     | 800 us                                                 | 782 us: 1.02x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.59 sec: 1.02x faster                                                    |
| genshi_text                | 22.6 ms                                                | 22.2 ms: 1.02x faster                                                     |
| richards_super             | 53.7 ms                                                | 52.7 ms: 1.02x faster                                                     |
| async_generators           | 433 ms                                                 | 426 ms: 1.02x faster                                                      |
| logging_format             | 6.23 us                                                | 6.13 us: 1.02x faster                                                     |
| xml_etree_process          | 60.5 ms                                                | 59.5 ms: 1.02x faster                                                     |
| json_loads                 | 27.2 us                                                | 26.7 us: 1.02x faster                                                     |
| tomli_loads                | 2.12 sec                                               | 2.09 sec: 1.01x faster                                                    |
| logging_simple             | 5.65 us                                                | 5.58 us: 1.01x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.01x faster                                                    |
| xml_etree_generate         | 86.8 ms                                                | 85.8 ms: 1.01x faster                                                     |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                      |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                      |
| python_startup_no_site     | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                     |
| coverage                   | 82.8 ms                                                | 83.1 ms: 1.00x slower                                                     |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.01x slower                                                     |
| sqlglot_optimize           | 53.4 ms                                                | 53.8 ms: 1.01x slower                                                     |
| float                      | 78.7 ms                                                | 79.3 ms: 1.01x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                      |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                     |
| genshi_xml                 | 50.5 ms                                                | 51.1 ms: 1.01x slower                                                     |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                                      |
| sympy_integrate            | 19.8 ms                                                | 20.1 ms: 1.01x slower                                                     |
| dulwich_log                | 64.6 ms                                                | 65.5 ms: 1.01x slower                                                     |
| hexiom                     | 6.08 ms                                                | 6.18 ms: 1.02x slower                                                     |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                      |
| sympy_expand               | 456 ms                                                 | 465 ms: 1.02x slower                                                      |
| spectral_norm              | 113 ms                                                 | 116 ms: 1.02x slower                                                      |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                    |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.02x slower                                                      |
| deltablue                  | 3.19 ms                                                | 3.27 ms: 1.03x slower                                                     |
| pyflate                    | 470 ms                                                 | 481 ms: 1.03x slower                                                      |
| sqlglot_parse              | 1.26 ms                                                | 1.30 ms: 1.03x slower                                                     |
| sqlglot_transpile          | 1.57 ms                                                | 1.61 ms: 1.03x slower                                                     |
| gc_traversal               | 4.90 ms                                                | 5.03 ms: 1.03x slower                                                     |
| django_template            | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                     |
| regex_dna                  | 220 ms                                                 | 226 ms: 1.03x slower                                                      |
| pprint_safe_repr           | 727 ms                                                 | 750 ms: 1.03x slower                                                      |
| scimark_monte_carlo        | 66.8 ms                                                | 69.0 ms: 1.03x slower                                                     |
| raytrace                   | 262 ms                                                 | 271 ms: 1.03x slower                                                      |
| pprint_pformat             | 1.48 sec                                               | 1.55 sec: 1.05x slower                                                    |
| nqueens                    | 80.9 ms                                                | 84.6 ms: 1.05x slower                                                     |
| scimark_sor                | 122 ms                                                 | 128 ms: 1.05x slower                                                      |
| bench_thread_pool          | 818 us                                                 | 863 us: 1.06x slower                                                      |
| comprehensions             | 16.5 us                                                | 17.4 us: 1.06x slower                                                     |
| mdp                        | 2.54 sec                                               | 2.71 sec: 1.07x slower                                                    |
| chaos                      | 58.0 ms                                                | 62.0 ms: 1.07x slower                                                     |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.08x slower                                                     |
| fannkuch                   | 394 ms                                                 | 424 ms: 1.08x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 326 us: 1.08x slower                                                      |
| mako                       | 10.7 ms                                                | 11.9 ms: 1.12x slower                                                     |
| many_optionals             | 857 us                                                 | 967 us: 1.13x slower                                                      |
| nbody                      | 87.7 ms                                                | 99.3 ms: 1.13x slower                                                     |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.13x slower                                                     |
| subparsers                 | 15.5 ms                                                | 21.5 ms: 1.39x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (10): scimark_sparse_mat_mult, html5lib, djangocms, sphinx, logging_silent, sympy_str, meteor_contest, regex_v8, scimark_fft, sqlite_synth
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241210-3.14.0a2+-1069d98/bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98.json: mypy2

- Geometric mean (including insignificant results): 1.019x faster

# HPT report

- Reliability score: 79.66% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x
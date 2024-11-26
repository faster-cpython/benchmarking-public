# Results vs. 3.13.0

- fork: faster-cpython
- ref: mark_first_gc
- machine: linux-x86_64
- commit hash: 5e813c5
- commit date: 2024-11-04
- overall geometric mean: 1.031x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 256 ms: 1.04x faster                                                      |
| docutils       | 2.59 sec                                               | 2.62 sec: 1.01x slower                                                    |
| html5lib       | 64.2 ms                                                | 63.6 ms: 1.01x faster                                                     |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 316 ms: 1.47x faster                                                      |
| async_tree_io              | 842 ms                                                 | 637 ms: 1.32x faster                                                      |
| async_tree_none            | 351 ms                                                 | 268 ms: 1.31x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 339 ms: 1.30x faster                                                      |
| async_tree_io_tg           | 857 ms                                                 | 658 ms: 1.30x faster                                                      |
| async_tree_none_tg         | 321 ms                                                 | 254 ms: 1.26x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 495 ms: 1.17x faster                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 479 ms: 1.14x faster                                                      |
| async_generators           | 436 ms                                                 | 432 ms: 1.01x faster                                                      |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                      |
| coroutines                 | 22.7 ms                                                | 24.3 ms: 1.07x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 77.7 ms: 1.02x faster                                                     |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                      |
| nbody          | 87.0 ms                                                | 101 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.54 ms: 1.06x faster                                                     |
| regex_v8       | 26.2 ms                                                | 25.1 ms: 1.04x faster                                                     |
| regex_dna      | 218 ms                                                 | 210 ms: 1.04x faster                                                      |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 151 ms: 1.03x faster                                                      |
| xml_etree_process    | 60.6 ms                                                | 59.3 ms: 1.02x faster                                                     |
| xml_etree_generate   | 86.7 ms                                                | 85.2 ms: 1.02x faster                                                     |
| tomli_loads          | 2.14 sec                                               | 2.11 sec: 1.01x faster                                                    |
| json_loads           | 27.2 us                                                | 27.0 us: 1.01x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 101 ms: 1.01x faster                                                      |
| unpickle_pure_python | 216 us                                                 | 223 us: 1.03x slower                                                      |
| pickle_pure_python   | 310 us                                                 | 330 us: 1.06x slower                                                      |
| json_dumps           | 10.6 ms                                                | 11.3 ms: 1.07x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                     |
| python_startup         | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.5 ms: 1.05x faster                                                     |
| genshi_xml      | 50.9 ms                                                | 49.6 ms: 1.03x faster                                                     |
| django_template | 35.2 ms                                                | 34.6 ms: 1.02x faster                                                     |
| mako            | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 316 ms: 1.47x faster                                                      |
| deepcopy                   | 358 us                                                 | 270 us: 1.32x faster                                                      |
| async_tree_io              | 842 ms                                                 | 637 ms: 1.32x faster                                                      |
| async_tree_none            | 351 ms                                                 | 268 ms: 1.31x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 339 ms: 1.30x faster                                                      |
| async_tree_io_tg           | 857 ms                                                 | 658 ms: 1.30x faster                                                      |
| async_tree_none_tg         | 321 ms                                                 | 254 ms: 1.26x faster                                                      |
| deepcopy_memo              | 39.1 us                                                | 32.0 us: 1.22x faster                                                     |
| go                         | 144 ms                                                 | 121 ms: 1.19x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 495 ms: 1.17x faster                                                      |
| deepcopy_reduce            | 3.20 us                                                | 2.80 us: 1.14x faster                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 479 ms: 1.14x faster                                                      |
| pylint                     | 313 ms                                                 | 279 ms: 1.12x faster                                                      |
| pathlib                    | 17.5 ms                                                | 16.0 ms: 1.10x faster                                                     |
| telco                      | 8.54 ms                                                | 7.94 ms: 1.08x faster                                                     |
| json                       | 5.36 ms                                                | 5.02 ms: 1.07x faster                                                     |
| regex_effbot               | 3.73 ms                                                | 3.54 ms: 1.06x faster                                                     |
| genshi_text                | 23.5 ms                                                | 22.5 ms: 1.05x faster                                                     |
| regex_v8                   | 26.2 ms                                                | 25.1 ms: 1.04x faster                                                     |
| 2to3                       | 267 ms                                                 | 256 ms: 1.04x faster                                                      |
| thrift                     | 809 us                                                 | 777 us: 1.04x faster                                                      |
| logging_format             | 6.40 us                                                | 6.14 us: 1.04x faster                                                     |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                      |
| bpe_tokeniser              | 4.75 sec                                               | 4.57 sec: 1.04x faster                                                    |
| regex_dna                  | 218 ms                                                 | 210 ms: 1.04x faster                                                      |
| xml_etree_parse            | 156 ms                                                 | 151 ms: 1.03x faster                                                      |
| generators                 | 29.0 ms                                                | 28.1 ms: 1.03x faster                                                     |
| logging_simple             | 5.72 us                                                | 5.54 us: 1.03x faster                                                     |
| genshi_xml                 | 50.9 ms                                                | 49.6 ms: 1.03x faster                                                     |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.03x faster                                                      |
| sympy_str                  | 275 ms                                                 | 268 ms: 1.02x faster                                                      |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                                    |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                    |
| xml_etree_process          | 60.6 ms                                                | 59.3 ms: 1.02x faster                                                     |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                      |
| pyflate                    | 471 ms                                                 | 461 ms: 1.02x faster                                                      |
| sqlalchemy_imperative      | 17.1 ms                                                | 16.7 ms: 1.02x faster                                                     |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                      |
| float                      | 79.2 ms                                                | 77.7 ms: 1.02x faster                                                     |
| xml_etree_generate         | 86.7 ms                                                | 85.2 ms: 1.02x faster                                                     |
| sympy_expand               | 463 ms                                                 | 455 ms: 1.02x faster                                                      |
| django_template            | 35.2 ms                                                | 34.6 ms: 1.02x faster                                                     |
| typing_runtime_protocols   | 165 us                                                 | 162 us: 1.02x faster                                                      |
| tomli_loads                | 2.14 sec                                               | 2.11 sec: 1.01x faster                                                    |
| crypto_pyaes               | 75.3 ms                                                | 74.4 ms: 1.01x faster                                                     |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.98 ms: 1.01x faster                                                     |
| json_loads                 | 27.2 us                                                | 27.0 us: 1.01x faster                                                     |
| html5lib                   | 64.2 ms                                                | 63.6 ms: 1.01x faster                                                     |
| richards                   | 48.7 ms                                                | 48.2 ms: 1.01x faster                                                     |
| async_generators           | 436 ms                                                 | 432 ms: 1.01x faster                                                      |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 101 ms: 1.01x faster                                                      |
| sqlglot_optimize           | 53.7 ms                                                | 53.6 ms: 1.00x faster                                                     |
| dulwich_log                | 64.3 ms                                                | 64.2 ms: 1.00x faster                                                     |
| sympy_integrate            | 19.9 ms                                                | 19.9 ms: 1.00x faster                                                     |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                      |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                      |
| pprint_safe_repr           | 728 ms                                                 | 736 ms: 1.01x slower                                                      |
| coverage                   | 84.0 ms                                                | 85.0 ms: 1.01x slower                                                     |
| docutils                   | 2.59 sec                                               | 2.62 sec: 1.01x slower                                                    |
| python_startup_no_site     | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                     |
| python_startup             | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                     |
| bench_thread_pool          | 822 us                                                 | 840 us: 1.02x slower                                                      |
| gc_traversal               | 4.37 ms                                                | 4.47 ms: 1.02x slower                                                     |
| sqlglot_transpile          | 1.58 ms                                                | 1.62 ms: 1.02x slower                                                     |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.02x slower                                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.31 ms: 1.03x slower                                                     |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                     |
| hexiom                     | 6.16 ms                                                | 6.36 ms: 1.03x slower                                                     |
| nqueens                    | 78.4 ms                                                | 81.0 ms: 1.03x slower                                                     |
| unpickle_pure_python       | 216 us                                                 | 223 us: 1.03x slower                                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 69.9 ms: 1.04x slower                                                     |
| scimark_sor                | 124 ms                                                 | 128 ms: 1.04x slower                                                      |
| mako                       | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                     |
| deltablue                  | 3.23 ms                                                | 3.35 ms: 1.04x slower                                                     |
| raytrace                   | 267 ms                                                 | 278 ms: 1.04x slower                                                      |
| scimark_lu                 | 113 ms                                                 | 119 ms: 1.05x slower                                                      |
| chaos                      | 58.1 ms                                                | 61.7 ms: 1.06x slower                                                     |
| scimark_fft                | 364 ms                                                 | 387 ms: 1.06x slower                                                      |
| pickle_pure_python         | 310 us                                                 | 330 us: 1.06x slower                                                      |
| json_dumps                 | 10.6 ms                                                | 11.3 ms: 1.07x slower                                                     |
| coroutines                 | 22.7 ms                                                | 24.3 ms: 1.07x slower                                                     |
| create_gc_cycles           | 2.41 ms                                                | 2.58 ms: 1.07x slower                                                     |
| logging_silent             | 102 ns                                                 | 110 ns: 1.08x slower                                                      |
| k_core                     | 2.35 sec                                               | 2.63 sec: 1.12x slower                                                    |
| nbody                      | 87.0 ms                                                | 101 ms: 1.16x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 78.5 ms: 3.27x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (6): connected_components, richards_super, mdp, pprint_pformat, shortest_path, fannkuch
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241104-3.14.0a1+-5e813c5/bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5.json: sqlite_synth

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x
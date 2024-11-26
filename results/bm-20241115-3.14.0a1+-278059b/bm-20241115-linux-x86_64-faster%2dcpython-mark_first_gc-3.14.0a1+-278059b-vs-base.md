# Results vs. base

- fork: faster-cpython
- ref: mark_first_gc
- machine: linux-x86_64
- commit hash: 278059b
- commit date: 2024-11-15
- overall geometric mean: 1.034x faster
- HPT reliability: 50.53%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                 | 263 ms: 1.03x slower                                                      |
| docutils       | 2.70 sec                                                               | 2.65 sec: 1.02x faster                                                    |
| html5lib       | 65.5 ms                                                                | 67.5 ms: 1.03x slower                                                     |
| sphinx         | 1.06 sec                                                               | 1.03 sec: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 976 ms                                                                 | 627 ms: 1.56x faster                                                      |
| async_tree_io              | 855 ms                                                                 | 643 ms: 1.33x faster                                                      |
| async_tree_none_tg         | 324 ms                                                                 | 271 ms: 1.20x faster                                                      |
| async_tree_none            | 330 ms                                                                 | 283 ms: 1.17x faster                                                      |
| async_tree_memoization     | 414 ms                                                                 | 358 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed_tg | 566 ms                                                                 | 502 ms: 1.13x faster                                                      |
| async_tree_cpu_io_mixed    | 571 ms                                                                 | 514 ms: 1.11x faster                                                      |
| async_tree_memoization_tg  | 380 ms                                                                 | 352 ms: 1.08x faster                                                      |
| coroutines                 | 24.0 ms                                                                | 23.8 ms: 1.01x faster                                                     |
| async_generators           | 429 ms                                                                 | 433 ms: 1.01x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.15x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.2 ms                                                                | 96.5 ms: 1.01x faster                                                     |
| pidigits       | 188 ms                                                                 | 192 ms: 1.02x slower                                                      |
| float          | 80.2 ms                                                                | 84.2 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 225 ms                                                                 | 221 ms: 1.02x faster                                                      |
| regex_compile  | 130 ms                                                                 | 130 ms: 1.00x slower                                                      |
| regex_v8       | 24.6 ms                                                                | 24.8 ms: 1.01x slower                                                     |
| regex_effbot   | 3.83 ms                                                                | 3.86 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                                 | 155 ms: 1.03x faster                                                      |
| pickle_pure_python   | 329 us                                                                 | 324 us: 1.01x faster                                                      |
| json_dumps           | 11.3 ms                                                                | 11.2 ms: 1.01x faster                                                     |
| json_loads           | 26.8 us                                                                | 26.7 us: 1.01x faster                                                     |
| unpickle_pure_python | 219 us                                                                 | 221 us: 1.01x slower                                                      |
| tomli_loads          | 2.09 sec                                                               | 2.11 sec: 1.01x slower                                                    |
| xml_etree_generate   | 85.5 ms                                                                | 87.9 ms: 1.03x slower                                                     |
| xml_etree_process    | 59.2 ms                                                                | 61.9 ms: 1.04x slower                                                     |
| xml_etree_iterparse  | 106 ms                                                                 | 117 ms: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.02 ms                                                                | 6.72 ms: 1.04x faster                                                     |
| python_startup         | 12.7 ms                                                                | 12.4 ms: 1.02x faster                                                     |
| Geometric mean         | (ref)                                                                  | 1.03x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 22.3 ms                                                                | 22.2 ms: 1.01x faster                                                     |
| mako            | 11.4 ms                                                                | 11.6 ms: 1.01x slower                                                     |
| genshi_xml      | 50.4 ms                                                                | 51.4 ms: 1.02x slower                                                     |
| django_template | 32.1 ms                                                                | 32.9 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| gc_traversal               | 4.61 ms                                                                | 2.29 ms: 2.02x faster                                                     |
| k_core                     | 3.61 sec                                                               | 2.22 sec: 1.62x faster                                                    |
| create_gc_cycles           | 2.70 ms                                                                | 1.67 ms: 1.62x faster                                                     |
| async_tree_io_tg           | 976 ms                                                                 | 627 ms: 1.56x faster                                                      |
| async_tree_io              | 855 ms                                                                 | 643 ms: 1.33x faster                                                      |
| async_tree_none_tg         | 324 ms                                                                 | 271 ms: 1.20x faster                                                      |
| async_tree_none            | 330 ms                                                                 | 283 ms: 1.17x faster                                                      |
| async_tree_memoization     | 414 ms                                                                 | 358 ms: 1.16x faster                                                      |
| pylint                     | 319 ms                                                                 | 277 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed_tg | 566 ms                                                                 | 502 ms: 1.13x faster                                                      |
| async_tree_cpu_io_mixed    | 571 ms                                                                 | 514 ms: 1.11x faster                                                      |
| async_tree_memoization_tg  | 380 ms                                                                 | 352 ms: 1.08x faster                                                      |
| mdp                        | 2.68 sec                                                               | 2.51 sec: 1.07x faster                                                    |
| python_startup_no_site     | 7.02 ms                                                                | 6.72 ms: 1.04x faster                                                     |
| sqlalchemy_imperative      | 17.0 ms                                                                | 16.5 ms: 1.03x faster                                                     |
| generators                 | 28.8 ms                                                                | 27.9 ms: 1.03x faster                                                     |
| xml_etree_parse            | 159 ms                                                                 | 155 ms: 1.03x faster                                                      |
| python_startup             | 12.7 ms                                                                | 12.4 ms: 1.02x faster                                                     |
| sphinx                     | 1.06 sec                                                               | 1.03 sec: 1.02x faster                                                    |
| regex_dna                  | 225 ms                                                                 | 221 ms: 1.02x faster                                                      |
| go                         | 123 ms                                                                 | 121 ms: 1.02x faster                                                      |
| docutils                   | 2.70 sec                                                               | 2.65 sec: 1.02x faster                                                    |
| pycparser                  | 1.14 sec                                                               | 1.12 sec: 1.02x faster                                                    |
| comprehensions             | 17.1 us                                                                | 16.9 us: 1.02x faster                                                     |
| pickle_pure_python         | 329 us                                                                 | 324 us: 1.01x faster                                                      |
| json_dumps                 | 11.3 ms                                                                | 11.2 ms: 1.01x faster                                                     |
| scimark_sor                | 129 ms                                                                 | 127 ms: 1.01x faster                                                      |
| json                       | 4.99 ms                                                                | 4.92 ms: 1.01x faster                                                     |
| dulwich_log                | 65.8 ms                                                                | 65.1 ms: 1.01x faster                                                     |
| scimark_monte_carlo        | 69.3 ms                                                                | 68.6 ms: 1.01x faster                                                     |
| coroutines                 | 24.0 ms                                                                | 23.8 ms: 1.01x faster                                                     |
| nbody                      | 97.2 ms                                                                | 96.5 ms: 1.01x faster                                                     |
| scimark_lu                 | 117 ms                                                                 | 117 ms: 1.01x faster                                                      |
| sympy_expand               | 457 ms                                                                 | 454 ms: 1.01x faster                                                      |
| genshi_text                | 22.3 ms                                                                | 22.2 ms: 1.01x faster                                                     |
| json_loads                 | 26.8 us                                                                | 26.7 us: 1.01x faster                                                     |
| deepcopy_reduce            | 2.70 us                                                                | 2.69 us: 1.00x faster                                                     |
| bench_thread_pool          | 853 us                                                                 | 851 us: 1.00x faster                                                      |
| hexiom                     | 6.35 ms                                                                | 6.37 ms: 1.00x slower                                                     |
| regex_compile              | 130 ms                                                                 | 130 ms: 1.00x slower                                                      |
| scimark_fft                | 363 ms                                                                 | 364 ms: 1.00x slower                                                      |
| many_optionals             | 947 us                                                                 | 951 us: 1.00x slower                                                      |
| unpickle_pure_python       | 219 us                                                                 | 221 us: 1.01x slower                                                      |
| regex_v8                   | 24.6 ms                                                                | 24.8 ms: 1.01x slower                                                     |
| meteor_contest             | 107 ms                                                                 | 108 ms: 1.01x slower                                                      |
| regex_effbot               | 3.83 ms                                                                | 3.86 ms: 1.01x slower                                                     |
| logging_format             | 6.18 us                                                                | 6.23 us: 1.01x slower                                                     |
| tomli_loads                | 2.09 sec                                                               | 2.11 sec: 1.01x slower                                                    |
| async_generators           | 429 ms                                                                 | 433 ms: 1.01x slower                                                      |
| sqlglot_parse              | 1.30 ms                                                                | 1.32 ms: 1.01x slower                                                     |
| crypto_pyaes               | 73.8 ms                                                                | 74.6 ms: 1.01x slower                                                     |
| fannkuch                   | 410 ms                                                                 | 415 ms: 1.01x slower                                                      |
| richards                   | 46.3 ms                                                                | 46.8 ms: 1.01x slower                                                     |
| sqlglot_transpile          | 1.60 ms                                                                | 1.62 ms: 1.01x slower                                                     |
| deepcopy                   | 259 us                                                                 | 262 us: 1.01x slower                                                      |
| pyflate                    | 467 ms                                                                 | 472 ms: 1.01x slower                                                      |
| nqueens                    | 79.8 ms                                                                | 80.8 ms: 1.01x slower                                                     |
| deepcopy_memo              | 30.4 us                                                                | 30.8 us: 1.01x slower                                                     |
| deltablue                  | 3.37 ms                                                                | 3.42 ms: 1.01x slower                                                     |
| pathlib                    | 16.0 ms                                                                | 16.2 ms: 1.01x slower                                                     |
| mako                       | 11.4 ms                                                                | 11.6 ms: 1.01x slower                                                     |
| sqlite_synth               | 2.84 us                                                                | 2.88 us: 1.01x slower                                                     |
| sqlglot_normalize          | 107 ms                                                                 | 109 ms: 1.01x slower                                                      |
| sqlglot_optimize           | 53.4 ms                                                                | 54.3 ms: 1.02x slower                                                     |
| spectral_norm              | 115 ms                                                                 | 117 ms: 1.02x slower                                                      |
| genshi_xml                 | 50.4 ms                                                                | 51.4 ms: 1.02x slower                                                     |
| bpe_tokeniser              | 4.78 sec                                                               | 4.87 sec: 1.02x slower                                                    |
| pidigits                   | 188 ms                                                                 | 192 ms: 1.02x slower                                                      |
| django_template            | 32.1 ms                                                                | 32.9 ms: 1.03x slower                                                     |
| xml_etree_generate         | 85.5 ms                                                                | 87.9 ms: 1.03x slower                                                     |
| 2to3                       | 256 ms                                                                 | 263 ms: 1.03x slower                                                      |
| html5lib                   | 65.5 ms                                                                | 67.5 ms: 1.03x slower                                                     |
| coverage                   | 84.6 ms                                                                | 88.1 ms: 1.04x slower                                                     |
| logging_silent             | 105 ns                                                                 | 109 ns: 1.04x slower                                                      |
| xml_etree_process          | 59.2 ms                                                                | 61.9 ms: 1.04x slower                                                     |
| subparsers                 | 20.8 ms                                                                | 21.8 ms: 1.05x slower                                                     |
| float                      | 80.2 ms                                                                | 84.2 ms: 1.05x slower                                                     |
| bench_mp_pool              | 78.4 ms                                                                | 83.5 ms: 1.06x slower                                                     |
| xml_etree_iterparse        | 106 ms                                                                 | 117 ms: 1.10x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (18): sympy_str, scimark_sparse_mat_mult, sympy_integrate, shortest_path, typing_runtime_protocols, thrift, sympy_sum, sqlalchemy_declarative, pprint_pformat, chaos, richards_super, raytrace, telco, pprint_safe_repr, asyncio_websockets, logging_simple, connected_components, djangocms

- Geometric mean (including insignificant results): 1.034x faster
# HPT report

- Reliability score: 50.53% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.97x
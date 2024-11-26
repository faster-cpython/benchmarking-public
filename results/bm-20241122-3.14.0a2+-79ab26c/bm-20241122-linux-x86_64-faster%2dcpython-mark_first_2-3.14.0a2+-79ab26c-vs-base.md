# Results vs. base

- fork: faster-cpython
- ref: mark_first_2
- machine: linux-x86_64
- commit hash: 79ab26c
- commit date: 2024-11-22
- overall geometric mean: 1.036x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241121-linux-x86_64-python-1629d2ca56014beb2d46-3.14.0a2+-1629d2c | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 256 ms: 1.01x faster                                                     |
| docutils       | 2.67 sec                                                               | 2.61 sec: 1.02x faster                                                   |
| html5lib       | 65.6 ms                                                                | 62.7 ms: 1.05x faster                                                    |
| sphinx         | 1.05 sec                                                               | 1.02 sec: 1.03x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241121-linux-x86_64-python-1629d2ca56014beb2d46-3.14.0a2+-1629d2c | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 915 ms                                                                 | 616 ms: 1.49x faster                                                     |
| async_tree_io              | 901 ms                                                                 | 628 ms: 1.44x faster                                                     |
| async_tree_memoization_tg  | 396 ms                                                                 | 316 ms: 1.25x faster                                                     |
| async_tree_none_tg         | 313 ms                                                                 | 254 ms: 1.23x faster                                                     |
| async_tree_memoization     | 406 ms                                                                 | 340 ms: 1.20x faster                                                     |
| async_tree_none            | 325 ms                                                                 | 271 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 566 ms                                                                 | 479 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed    | 562 ms                                                                 | 492 ms: 1.14x faster                                                     |
| coroutines                 | 24.9 ms                                                                | 23.9 ms: 1.04x faster                                                    |
| async_generators           | 437 ms                                                                 | 427 ms: 1.02x faster                                                     |
| Geometric mean             | (ref)                                                                  | 1.19x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241121-linux-x86_64-python-1629d2ca56014beb2d46-3.14.0a2+-1629d2c | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 101 ms                                                                 | 93.6 ms: 1.08x faster                                                    |
| float          | 82.7 ms                                                                | 76.8 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241121-linux-x86_64-python-1629d2ca56014beb2d46-3.14.0a2+-1629d2c | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                 | 129 ms: 1.01x faster                                                     |
| regex_effbot   | 3.48 ms                                                                | 3.55 ms: 1.02x slower                                                    |
| regex_dna      | 222 ms                                                                 | 226 ms: 1.02x slower                                                     |
| regex_v8       | 26.3 ms                                                                | 26.8 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241121-linux-x86_64-python-1629d2ca56014beb2d46-3.14.0a2+-1629d2c | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 153 ms                                                                 | 139 ms: 1.10x faster                                                     |
| xml_etree_iterparse  | 104 ms                                                                 | 97.7 ms: 1.06x faster                                                    |
| pickle_pure_python   | 327 us                                                                 | 319 us: 1.02x faster                                                     |
| xml_etree_process    | 60.4 ms                                                                | 59.5 ms: 1.02x faster                                                    |
| xml_etree_generate   | 86.3 ms                                                                | 85.0 ms: 1.01x faster                                                    |
| tomli_loads          | 2.12 sec                                                               | 2.10 sec: 1.01x faster                                                   |
| unpickle_pure_python | 220 us                                                                 | 218 us: 1.01x faster                                                     |
| json_dumps           | 11.3 ms                                                                | 11.3 ms: 1.00x faster                                                    |
| json_loads           | 26.5 us                                                                | 26.6 us: 1.01x slower                                                    |
| Geometric mean       | (ref)                                                                  | 1.03x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241121-linux-x86_64-python-1629d2ca56014beb2d46-3.14.0a2+-1629d2c | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.7 ms: 1.00x faster                                                    |
| python_startup_no_site | 7.03 ms                                                                | 7.04 ms: 1.00x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241121-linux-x86_64-python-1629d2ca56014beb2d46-3.14.0a2+-1629d2c | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 32.5 ms                                                                | 32.0 ms: 1.02x faster                                                    |
| genshi_text     | 22.7 ms                                                                | 22.4 ms: 1.01x faster                                                    |
| genshi_xml      | 50.3 ms                                                                | 51.0 ms: 1.01x slower                                                    |
| mako            | 11.2 ms                                                                | 11.5 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241121-linux-x86_64-python-1629d2ca56014beb2d46-3.14.0a2+-1629d2c | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 915 ms                                                                 | 616 ms: 1.49x faster                                                     |
| async_tree_io              | 901 ms                                                                 | 628 ms: 1.44x faster                                                     |
| k_core                     | 2.89 sec                                                               | 2.29 sec: 1.26x faster                                                   |
| async_tree_memoization_tg  | 396 ms                                                                 | 316 ms: 1.25x faster                                                     |
| async_tree_none_tg         | 313 ms                                                                 | 254 ms: 1.23x faster                                                     |
| async_tree_memoization     | 406 ms                                                                 | 340 ms: 1.20x faster                                                     |
| async_tree_none            | 325 ms                                                                 | 271 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 566 ms                                                                 | 479 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed    | 562 ms                                                                 | 492 ms: 1.14x faster                                                     |
| xml_etree_parse            | 153 ms                                                                 | 139 ms: 1.10x faster                                                     |
| nbody                      | 101 ms                                                                 | 93.6 ms: 1.08x faster                                                    |
| float                      | 82.7 ms                                                                | 76.8 ms: 1.08x faster                                                    |
| create_gc_cycles           | 2.66 ms                                                                | 2.48 ms: 1.08x faster                                                    |
| bpe_tokeniser              | 4.92 sec                                                               | 4.58 sec: 1.08x faster                                                   |
| deltablue                  | 3.44 ms                                                                | 3.22 ms: 1.07x faster                                                    |
| xml_etree_iterparse        | 104 ms                                                                 | 97.7 ms: 1.06x faster                                                    |
| go                         | 125 ms                                                                 | 118 ms: 1.06x faster                                                     |
| logging_silent             | 112 ns                                                                 | 106 ns: 1.05x faster                                                     |
| fannkuch                   | 421 ms                                                                 | 401 ms: 1.05x faster                                                     |
| html5lib                   | 65.6 ms                                                                | 62.7 ms: 1.05x faster                                                    |
| coroutines                 | 24.9 ms                                                                | 23.9 ms: 1.04x faster                                                    |
| hexiom                     | 6.47 ms                                                                | 6.22 ms: 1.04x faster                                                    |
| crypto_pyaes               | 74.6 ms                                                                | 71.8 ms: 1.04x faster                                                    |
| raytrace                   | 281 ms                                                                 | 272 ms: 1.04x faster                                                     |
| pycparser                  | 1.18 sec                                                               | 1.14 sec: 1.04x faster                                                   |
| spectral_norm              | 119 ms                                                                 | 115 ms: 1.03x faster                                                     |
| comprehensions             | 17.4 us                                                                | 16.8 us: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 5.07 ms                                                                | 4.92 ms: 1.03x faster                                                    |
| sphinx                     | 1.05 sec                                                               | 1.02 sec: 1.03x faster                                                   |
| chaos                      | 62.6 ms                                                                | 60.8 ms: 1.03x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                                | 16.2 ms: 1.03x faster                                                    |
| richards_super             | 54.1 ms                                                                | 52.6 ms: 1.03x faster                                                    |
| deepcopy_reduce            | 2.74 us                                                                | 2.67 us: 1.02x faster                                                    |
| pyflate                    | 477 ms                                                                 | 465 ms: 1.02x faster                                                     |
| deepcopy_memo              | 31.0 us                                                                | 30.3 us: 1.02x faster                                                    |
| generators                 | 28.7 ms                                                                | 28.1 ms: 1.02x faster                                                    |
| pickle_pure_python         | 327 us                                                                 | 319 us: 1.02x faster                                                     |
| richards                   | 47.6 ms                                                                | 46.6 ms: 1.02x faster                                                    |
| nqueens                    | 82.0 ms                                                                | 80.2 ms: 1.02x faster                                                    |
| docutils                   | 2.67 sec                                                               | 2.61 sec: 1.02x faster                                                   |
| async_generators           | 437 ms                                                                 | 427 ms: 1.02x faster                                                     |
| sqlglot_parse              | 1.31 ms                                                                | 1.29 ms: 1.02x faster                                                    |
| mdp                        | 2.69 sec                                                               | 2.64 sec: 1.02x faster                                                   |
| telco                      | 7.94 ms                                                                | 7.80 ms: 1.02x faster                                                    |
| deepcopy                   | 263 us                                                                 | 259 us: 1.02x faster                                                     |
| django_template            | 32.5 ms                                                                | 32.0 ms: 1.02x faster                                                    |
| xml_etree_process          | 60.4 ms                                                                | 59.5 ms: 1.02x faster                                                    |
| xml_etree_generate         | 86.3 ms                                                                | 85.0 ms: 1.01x faster                                                    |
| genshi_text                | 22.7 ms                                                                | 22.4 ms: 1.01x faster                                                    |
| tomli_loads                | 2.12 sec                                                               | 2.10 sec: 1.01x faster                                                   |
| scimark_monte_carlo        | 69.8 ms                                                                | 69.1 ms: 1.01x faster                                                    |
| unpickle_pure_python       | 220 us                                                                 | 218 us: 1.01x faster                                                     |
| scimark_fft                | 373 ms                                                                 | 370 ms: 1.01x faster                                                     |
| 2to3                       | 258 ms                                                                 | 256 ms: 1.01x faster                                                     |
| thrift                     | 770 us                                                                 | 763 us: 1.01x faster                                                     |
| pathlib                    | 16.1 ms                                                                | 16.0 ms: 1.01x faster                                                    |
| sqlglot_transpile          | 1.61 ms                                                                | 1.60 ms: 1.01x faster                                                    |
| sqlglot_normalize          | 108 ms                                                                 | 108 ms: 1.01x faster                                                     |
| regex_compile              | 129 ms                                                                 | 129 ms: 1.01x faster                                                     |
| json_dumps                 | 11.3 ms                                                                | 11.3 ms: 1.00x faster                                                    |
| scimark_lu                 | 117 ms                                                                 | 116 ms: 1.00x faster                                                     |
| python_startup             | 12.8 ms                                                                | 12.7 ms: 1.00x faster                                                    |
| sqlglot_optimize           | 53.8 ms                                                                | 53.6 ms: 1.00x faster                                                    |
| bench_thread_pool          | 854 us                                                                 | 851 us: 1.00x faster                                                     |
| python_startup_no_site     | 7.03 ms                                                                | 7.04 ms: 1.00x slower                                                    |
| sympy_sum                  | 147 ms                                                                 | 148 ms: 1.00x slower                                                     |
| many_optionals             | 936 us                                                                 | 941 us: 1.00x slower                                                     |
| subparsers                 | 20.8 ms                                                                | 20.9 ms: 1.01x slower                                                    |
| json_loads                 | 26.5 us                                                                | 26.6 us: 1.01x slower                                                    |
| pprint_pformat             | 1.50 sec                                                               | 1.51 sec: 1.01x slower                                                   |
| json                       | 4.93 ms                                                                | 4.99 ms: 1.01x slower                                                    |
| pprint_safe_repr           | 735 ms                                                                 | 745 ms: 1.01x slower                                                     |
| genshi_xml                 | 50.3 ms                                                                | 51.0 ms: 1.01x slower                                                    |
| regex_effbot               | 3.48 ms                                                                | 3.55 ms: 1.02x slower                                                    |
| regex_dna                  | 222 ms                                                                 | 226 ms: 1.02x slower                                                     |
| regex_v8                   | 26.3 ms                                                                | 26.8 ms: 1.02x slower                                                    |
| bench_mp_pool              | 78.9 ms                                                                | 80.8 ms: 1.02x slower                                                    |
| mako                       | 11.2 ms                                                                | 11.5 ms: 1.03x slower                                                    |
| gc_traversal               | 4.68 ms                                                                | 4.95 ms: 1.06x slower                                                    |
| pylint                     | 262 ms                                                                 | 278 ms: 1.06x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (17): djangocms, meteor_contest, asyncio_websockets, scimark_sor, sqlalchemy_declarative, pidigits, typing_runtime_protocols, logging_simple, dulwich_log, sympy_str, sympy_integrate, sqlite_synth, logging_format, coverage, shortest_path, sympy_expand, connected_components

- Geometric mean (including insignificant results): 1.036x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x
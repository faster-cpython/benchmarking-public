# Results vs. base

- fork: brandtbucher
- ref: optimize_off_most
- machine: linux-x86_64
- commit hash: 32b9407
- commit date: 2024-11-18
- overall geometric mean: 1.056x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                 | 300 ms: 1.07x slower                                                      |
| docutils       | 2.93 sec                                                               | 3.27 sec: 1.12x slower                                                    |
| html5lib       | 66.3 ms                                                                | 69.7 ms: 1.05x slower                                                     |
| sphinx         | 1.17 sec                                                               | 1.22 sec: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.07x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| coroutines                 | 22.8 ms                                                                | 22.9 ms: 1.01x slower                                                     |
| asyncio_websockets         | 552 ms                                                                 | 556 ms: 1.01x slower                                                      |
| async_tree_none            | 337 ms                                                                 | 342 ms: 1.01x slower                                                      |
| async_generators           | 451 ms                                                                 | 457 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg | 563 ms                                                                 | 573 ms: 1.02x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 187 ms: 1.00x slower                                                      |
| float          | 76.5 ms                                                                | 80.7 ms: 1.05x slower                                                     |
| nbody          | 82.4 ms                                                                | 98.9 ms: 1.20x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.08x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.66 ms                                                                | 3.80 ms: 1.04x slower                                                     |
| regex_dna      | 211 ms                                                                 | 225 ms: 1.07x slower                                                      |
| regex_compile  | 142 ms                                                                 | 156 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                              |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads           | 26.5 us                                                                | 26.4 us: 1.00x faster                                                     |
| json_dumps           | 11.2 ms                                                                | 11.4 ms: 1.01x slower                                                     |
| unpickle_pure_python | 217 us                                                                 | 228 us: 1.05x slower                                                      |
| xml_etree_generate   | 79.5 ms                                                                | 83.6 ms: 1.05x slower                                                     |
| pickle_pure_python   | 322 us                                                                 | 342 us: 1.06x slower                                                      |
| tomli_loads          | 1.94 sec                                                               | 2.09 sec: 1.08x slower                                                    |
| xml_etree_process    | 55.6 ms                                                                | 60.8 ms: 1.09x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.04x slower                                                              |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.16 ms                                                                | 7.12 ms: 1.01x faster                                                     |
| python_startup         | 12.9 ms                                                                | 12.9 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 33.8 ms                                                                | 35.4 ms: 1.05x slower                                                     |
| genshi_text     | 25.2 ms                                                                | 27.2 ms: 1.08x slower                                                     |
| mako            | 10.1 ms                                                                | 11.2 ms: 1.12x slower                                                     |
| genshi_xml      | 57.8 ms                                                                | 67.6 ms: 1.17x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.10x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| gc_traversal               | 4.81 ms                                                                | 4.36 ms: 1.10x faster                                                     |
| create_gc_cycles           | 2.70 ms                                                                | 2.68 ms: 1.01x faster                                                     |
| python_startup_no_site     | 7.16 ms                                                                | 7.12 ms: 1.01x faster                                                     |
| json_loads                 | 26.5 us                                                                | 26.4 us: 1.00x faster                                                     |
| python_startup             | 12.9 ms                                                                | 12.9 ms: 1.00x faster                                                     |
| pidigits                   | 186 ms                                                                 | 187 ms: 1.00x slower                                                      |
| coroutines                 | 22.8 ms                                                                | 22.9 ms: 1.01x slower                                                     |
| asyncio_websockets         | 552 ms                                                                 | 556 ms: 1.01x slower                                                      |
| pathlib                    | 16.2 ms                                                                | 16.4 ms: 1.01x slower                                                     |
| coverage                   | 83.5 ms                                                                | 84.4 ms: 1.01x slower                                                     |
| shortest_path              | 482 ms                                                                 | 487 ms: 1.01x slower                                                      |
| json_dumps                 | 11.2 ms                                                                | 11.4 ms: 1.01x slower                                                     |
| bench_mp_pool              | 85.5 ms                                                                | 86.6 ms: 1.01x slower                                                     |
| async_tree_none            | 337 ms                                                                 | 342 ms: 1.01x slower                                                      |
| async_generators           | 451 ms                                                                 | 457 ms: 1.01x slower                                                      |
| sqlite_synth               | 2.79 us                                                                | 2.84 us: 1.02x slower                                                     |
| bench_thread_pool          | 899 us                                                                 | 915 us: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 563 ms                                                                 | 573 ms: 1.02x slower                                                      |
| telco                      | 7.50 ms                                                                | 7.64 ms: 1.02x slower                                                     |
| sqlalchemy_imperative      | 17.8 ms                                                                | 18.2 ms: 1.02x slower                                                     |
| connected_components       | 438 ms                                                                 | 447 ms: 1.02x slower                                                      |
| meteor_contest             | 108 ms                                                                 | 112 ms: 1.03x slower                                                      |
| sqlalchemy_declarative     | 147 ms                                                                 | 152 ms: 1.03x slower                                                      |
| subparsers                 | 21.2 ms                                                                | 22.0 ms: 1.04x slower                                                     |
| sphinx                     | 1.17 sec                                                               | 1.22 sec: 1.04x slower                                                    |
| regex_effbot               | 3.66 ms                                                                | 3.80 ms: 1.04x slower                                                     |
| sympy_expand               | 510 ms                                                                 | 530 ms: 1.04x slower                                                      |
| scimark_lu                 | 115 ms                                                                 | 119 ms: 1.04x slower                                                      |
| logging_simple             | 5.60 us                                                                | 5.85 us: 1.05x slower                                                     |
| typing_runtime_protocols   | 166 us                                                                 | 174 us: 1.05x slower                                                      |
| dulwich_log                | 67.5 ms                                                                | 70.8 ms: 1.05x slower                                                     |
| logging_format             | 6.17 us                                                                | 6.47 us: 1.05x slower                                                     |
| django_template            | 33.8 ms                                                                | 35.4 ms: 1.05x slower                                                     |
| unpickle_pure_python       | 217 us                                                                 | 228 us: 1.05x slower                                                      |
| xml_etree_generate         | 79.5 ms                                                                | 83.6 ms: 1.05x slower                                                     |
| nqueens                    | 89.6 ms                                                                | 94.2 ms: 1.05x slower                                                     |
| html5lib                   | 66.3 ms                                                                | 69.7 ms: 1.05x slower                                                     |
| sympy_str                  | 306 ms                                                                 | 323 ms: 1.05x slower                                                      |
| float                      | 76.5 ms                                                                | 80.7 ms: 1.05x slower                                                     |
| sympy_sum                  | 178 ms                                                                 | 188 ms: 1.06x slower                                                      |
| sqlglot_normalize          | 115 ms                                                                 | 122 ms: 1.06x slower                                                      |
| sympy_integrate            | 23.7 ms                                                                | 25.1 ms: 1.06x slower                                                     |
| crypto_pyaes               | 69.1 ms                                                                | 73.3 ms: 1.06x slower                                                     |
| pickle_pure_python         | 322 us                                                                 | 342 us: 1.06x slower                                                      |
| regex_dna                  | 211 ms                                                                 | 225 ms: 1.07x slower                                                      |
| raytrace                   | 285 ms                                                                 | 304 ms: 1.07x slower                                                      |
| 2to3                       | 281 ms                                                                 | 300 ms: 1.07x slower                                                      |
| bpe_tokeniser              | 4.46 sec                                                               | 4.79 sec: 1.07x slower                                                    |
| sqlglot_optimize           | 60.2 ms                                                                | 64.7 ms: 1.08x slower                                                     |
| tomli_loads                | 1.94 sec                                                               | 2.09 sec: 1.08x slower                                                    |
| genshi_text                | 25.2 ms                                                                | 27.2 ms: 1.08x slower                                                     |
| many_optionals             | 1.05 ms                                                                | 1.14 ms: 1.08x slower                                                     |
| mdp                        | 2.59 sec                                                               | 2.80 sec: 1.08x slower                                                    |
| deepcopy_reduce            | 2.70 us                                                                | 2.92 us: 1.08x slower                                                     |
| scimark_fft                | 320 ms                                                                 | 349 ms: 1.09x slower                                                      |
| regex_compile              | 142 ms                                                                 | 156 ms: 1.09x slower                                                      |
| xml_etree_process          | 55.6 ms                                                                | 60.8 ms: 1.09x slower                                                     |
| deepcopy_memo              | 29.4 us                                                                | 32.3 us: 1.10x slower                                                     |
| comprehensions             | 17.6 us                                                                | 19.4 us: 1.10x slower                                                     |
| scimark_sparse_mat_mult    | 4.54 ms                                                                | 5.00 ms: 1.10x slower                                                     |
| pyflate                    | 457 ms                                                                 | 505 ms: 1.10x slower                                                      |
| sqlglot_parse              | 1.33 ms                                                                | 1.47 ms: 1.10x slower                                                     |
| deepcopy                   | 269 us                                                                 | 298 us: 1.11x slower                                                      |
| sqlglot_transpile          | 1.70 ms                                                                | 1.89 ms: 1.11x slower                                                     |
| mako                       | 10.1 ms                                                                | 11.2 ms: 1.12x slower                                                     |
| spectral_norm              | 114 ms                                                                 | 127 ms: 1.12x slower                                                      |
| docutils                   | 2.93 sec                                                               | 3.27 sec: 1.12x slower                                                    |
| fannkuch                   | 391 ms                                                                 | 437 ms: 1.12x slower                                                      |
| pycparser                  | 1.15 sec                                                               | 1.28 sec: 1.12x slower                                                    |
| deltablue                  | 3.31 ms                                                                | 3.73 ms: 1.13x slower                                                     |
| chaos                      | 59.1 ms                                                                | 66.7 ms: 1.13x slower                                                     |
| logging_silent             | 98.9 ns                                                                | 112 ns: 1.14x slower                                                      |
| generators                 | 36.0 ms                                                                | 41.0 ms: 1.14x slower                                                     |
| scimark_monte_carlo        | 64.0 ms                                                                | 72.9 ms: 1.14x slower                                                     |
| go                         | 133 ms                                                                 | 151 ms: 1.14x slower                                                      |
| hexiom                     | 7.15 ms                                                                | 8.25 ms: 1.15x slower                                                     |
| scimark_sor                | 119 ms                                                                 | 138 ms: 1.16x slower                                                      |
| genshi_xml                 | 57.8 ms                                                                | 67.6 ms: 1.17x slower                                                     |
| nbody                      | 82.4 ms                                                                | 98.9 ms: 1.20x slower                                                     |
| richards                   | 40.0 ms                                                                | 48.8 ms: 1.22x slower                                                     |
| pprint_safe_repr           | 741 ms                                                                 | 910 ms: 1.23x slower                                                      |
| pprint_pformat             | 1.52 sec                                                               | 1.89 sec: 1.25x slower                                                    |
| richards_super             | 46.0 ms                                                                | 57.7 ms: 1.25x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.06x slower                                                              |

Benchmark hidden because not significant (14): async_tree_io_tg, regex_v8, json, k_core, async_tree_none_tg, xml_etree_iterparse, xml_etree_parse, thrift, djangocms, async_tree_memoization_tg, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed, pylint

- Geometric mean (including insignificant results): 1.056x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.02x
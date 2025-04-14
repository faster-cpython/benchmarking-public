# Results vs. 3.13.0

- fork: python
- ref: 555dc50c811e3e9ebdc3
- machine: windows-amd64
- commit hash: 555dc50
- commit date: 2025-02-06
- overall geometric mean: 1.011x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 227 ms: 1.06x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.4 ms: 1.03x slower                                                       |
| sphinx         | 617 ms                                                      | 645 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 225 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 406 ms: 1.22x faster                                                        |
| async_tree_io              | 513 ms                                                      | 423 ms: 1.21x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 223 ms: 1.19x faster                                                        |
| async_tree_none            | 219 ms                                                      | 189 ms: 1.16x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 339 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                                        |
| async_generators           | 223 ms                                                      | 221 ms: 1.01x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 306 ms: 1.02x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 12.9 ms: 1.03x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.8 ms: 1.11x faster                                                       |
| pidigits       | 146 ms                                                      | 151 ms: 1.03x slower                                                        |
| nbody          | 66.3 ms                                                     | 71.2 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.44 ms: 1.17x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 85.6 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 90.5 ms: 1.02x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                      |
| json_loads           | 15.1 us                                                     | 15.5 us: 1.03x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.4 ms: 1.05x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 56.4 ms: 1.06x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 39.5 ms: 1.08x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.72 ms: 1.08x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 148 us: 1.14x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 218 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.74 ms: 1.03x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                                       |
| django_template | 20.3 ms                                                     | 25.1 ms: 1.23x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4+-555dc50 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 510 us: 16.59x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 225 ms: 1.25x faster                                                        |
| pathlib                    | 75.3 ms                                                     | 60.9 ms: 1.24x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 406 ms: 1.22x faster                                                        |
| deepcopy                   | 223 us                                                      | 183 us: 1.22x faster                                                        |
| async_tree_io              | 513 ms                                                      | 423 ms: 1.21x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 19.2 us: 1.20x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 223 ms: 1.19x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.44 ms: 1.17x faster                                                       |
| async_tree_none            | 219 ms                                                      | 189 ms: 1.16x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 339 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                                        |
| float                      | 50.8 ms                                                     | 45.8 ms: 1.11x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 57.9 ms: 1.09x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.86 us: 1.09x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.70 ms: 1.03x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 90.5 ms: 1.02x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                                       |
| shortest_path              | 355 ms                                                      | 352 ms: 1.01x faster                                                        |
| async_generators           | 223 ms                                                      | 221 ms: 1.01x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.57 us: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.63 ms: 1.01x slower                                                       |
| go                         | 84.7 ms                                                     | 85.7 ms: 1.01x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.91 sec: 1.01x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                      |
| k_core                     | 1.70 sec                                                    | 1.73 sec: 1.02x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.02x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 306 ms: 1.02x slower                                                        |
| mako                       | 6.56 ms                                                     | 6.74 ms: 1.03x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                                       |
| json_loads                 | 15.1 us                                                     | 15.5 us: 1.03x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 47.0 ms: 1.03x slower                                                       |
| pidigits                   | 146 ms                                                      | 151 ms: 1.03x slower                                                        |
| pycparser                  | 695 ms                                                      | 717 ms: 1.03x slower                                                        |
| html5lib                   | 38.2 ms                                                     | 39.4 ms: 1.03x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 12.9 ms: 1.03x slower                                                       |
| fannkuch                   | 252 ms                                                      | 262 ms: 1.04x slower                                                        |
| bench_thread_pool          | 810 us                                                      | 847 us: 1.05x slower                                                        |
| sphinx                     | 617 ms                                                      | 645 ms: 1.05x slower                                                        |
| pyflate                    | 283 ms                                                      | 296 ms: 1.05x slower                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.4 ms: 1.05x slower                                                       |
| sympy_str                  | 167 ms                                                      | 175 ms: 1.05x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 75.6 ms: 1.05x slower                                                       |
| coverage                   | 45.3 ms                                                     | 47.7 ms: 1.05x slower                                                       |
| sympy_expand               | 286 ms                                                      | 301 ms: 1.05x slower                                                        |
| scimark_fft                | 175 ms                                                      | 185 ms: 1.06x slower                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 56.4 ms: 1.06x slower                                                       |
| 2to3                       | 215 ms                                                      | 227 ms: 1.06x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 57.8 ns: 1.06x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 90.2 ms: 1.06x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.5 ms: 1.06x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 85.6 ms: 1.06x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 89.4 ms: 1.06x slower                                                       |
| generators                 | 19.0 ms                                                     | 20.2 ms: 1.07x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.2 ms: 1.07x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.1 us: 1.07x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.05 sec: 1.07x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 60.8 ms: 1.07x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 34.9 ms: 1.07x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                      |
| nbody                      | 66.3 ms                                                     | 71.2 ms: 1.07x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 39.5 ms: 1.08x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.72 ms: 1.08x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 527 ms: 1.09x slower                                                        |
| logging_format             | 6.18 us                                                     | 6.73 us: 1.09x slower                                                       |
| chaos                      | 37.9 ms                                                     | 41.3 ms: 1.09x slower                                                       |
| richards                   | 26.3 ms                                                     | 28.7 ms: 1.09x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 44.7 ms: 1.10x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.33 us: 1.10x slower                                                       |
| richards_super             | 29.8 ms                                                     | 32.8 ms: 1.10x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 189 ms: 1.10x slower                                                        |
| mdp                        | 1.43 sec                                                    | 1.58 sec: 1.10x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.24 ms: 1.10x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 62.0 ms: 1.10x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.06 ms: 1.11x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 852 us: 1.12x slower                                                        |
| scimark_sor                | 76.2 ms                                                     | 85.4 ms: 1.12x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.15 ms: 1.13x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 148 us: 1.14x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 218 us: 1.17x slower                                                        |
| many_optionals             | 361 us                                                      | 434 us: 1.20x slower                                                        |
| django_template            | 20.3 ms                                                     | 25.1 ms: 1.23x slower                                                       |
| raytrace                   | 153 ms                                                      | 194 ms: 1.26x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.3 ms: 1.50x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (6): pylint, json, regex_dna, connected_components, genshi_xml, gc_traversal
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.011x faster

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown
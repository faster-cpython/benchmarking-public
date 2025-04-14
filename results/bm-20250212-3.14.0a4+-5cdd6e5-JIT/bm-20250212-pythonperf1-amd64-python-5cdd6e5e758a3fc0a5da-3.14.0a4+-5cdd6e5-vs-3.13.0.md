# Results vs. 3.13.0

- fork: python
- ref: 5cdd6e5e758a3fc0a5da
- machine: windows-amd64
- commit hash: 5cdd6e5
- commit date: 2025-02-12
- overall geometric mean: 1.024x faster
- HPT reliability: 83.84%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.76 sec: 1.15x slower                                                      |
| sphinx         | 617 ms                                                      | 655 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| async_tree_io              | 513 ms                                                      | 417 ms: 1.23x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 420 ms: 1.18x faster                                                        |
| async_tree_none            | 219 ms                                                      | 187 ms: 1.17x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 176 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 344 ms: 1.10x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 316 ms: 1.05x slower                                                        |
| async_generators           | 223 ms                                                      | 246 ms: 1.11x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 60.4 ms: 1.10x faster                                                       |
| float          | 50.8 ms                                                     | 48.4 ms: 1.05x faster                                                       |
| pidigits       | 146 ms                                                      | 150 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.7 ms: 1.62x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.43 ms: 1.19x faster                                                       |
| regex_dna      | 115 ms                                                      | 116 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 112 us: 1.16x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.20 sec: 1.15x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 50.3 ms: 1.06x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 89.9 ms: 1.03x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 36.2 ms: 1.01x faster                                                       |
| json_loads           | 15.1 us                                                     | 16.0 us: 1.06x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.76 ms: 1.09x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 213 us: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.1 ms: 1.03x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.33 ms: 1.23x faster                                                       |
| genshi_xml      | 33.9 ms                                                     | 36.5 ms: 1.08x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.8 ms: 1.11x slower                                                       |
| django_template | 20.3 ms                                                     | 25.8 ms: 1.27x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 503 us: 16.83x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 29.5 ms: 2.56x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.7 ms: 1.62x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.05 ms: 1.27x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.33 ms: 1.23x faster                                                       |
| async_tree_io              | 513 ms                                                      | 417 ms: 1.23x faster                                                        |
| scimark_fft                | 175 ms                                                      | 147 ms: 1.19x faster                                                        |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.43 ms: 1.19x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 420 ms: 1.18x faster                                                        |
| async_tree_none            | 219 ms                                                      | 187 ms: 1.17x faster                                                        |
| unpickle_pure_python       | 130 us                                                      | 112 us: 1.16x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.20 sec: 1.15x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 176 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                        |
| telco                      | 4.85 ms                                                     | 4.32 ms: 1.12x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 344 ms: 1.10x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.60 sec: 1.10x faster                                                      |
| nbody                      | 66.3 ms                                                     | 60.4 ms: 1.10x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 21.1 us: 1.09x faster                                                       |
| fannkuch                   | 252 ms                                                      | 232 ms: 1.08x faster                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 50.3 ms: 1.06x faster                                                       |
| float                      | 50.8 ms                                                     | 48.4 ms: 1.05x faster                                                       |
| json                       | 3.30 ms                                                     | 3.17 ms: 1.04x faster                                                       |
| dulwich_log                | 40.1 ms                                                     | 38.8 ms: 1.03x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.64 sec: 1.03x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.54 us: 1.03x faster                                                       |
| shortest_path              | 355 ms                                                      | 345 ms: 1.03x faster                                                        |
| connected_components       | 320 ms                                                      | 311 ms: 1.03x faster                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 89.9 ms: 1.03x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.98 us: 1.02x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 62.0 ms: 1.02x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 36.2 ms: 1.01x faster                                                       |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.01x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 46.3 ms: 1.02x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 996 ms: 1.02x slower                                                        |
| pidigits                   | 146 ms                                                      | 150 ms: 1.02x slower                                                        |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                        |
| go                         | 84.7 ms                                                     | 87.1 ms: 1.03x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.1 ms: 1.03x slower                                                       |
| sympy_str                  | 167 ms                                                      | 175 ms: 1.05x slower                                                        |
| sympy_expand               | 286 ms                                                      | 301 ms: 1.05x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 316 ms: 1.05x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 89.7 ms: 1.05x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 511 ms: 1.06x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 76.0 ms: 1.06x slower                                                       |
| json_loads                 | 15.1 us                                                     | 16.0 us: 1.06x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 858 us: 1.06x slower                                                        |
| sphinx                     | 617 ms                                                      | 655 ms: 1.06x slower                                                        |
| genshi_xml                 | 33.9 ms                                                     | 36.5 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 112 us: 1.08x slower                                                        |
| generators                 | 19.0 ms                                                     | 20.7 ms: 1.09x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.76 ms: 1.09x slower                                                       |
| coverage                   | 45.3 ms                                                     | 50.0 ms: 1.10x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 844 us: 1.10x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 16.8 ms: 1.11x slower                                                       |
| async_generators           | 223 ms                                                      | 246 ms: 1.11x slower                                                        |
| chaos                      | 37.9 ms                                                     | 42.1 ms: 1.11x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 45.6 ms: 1.12x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.8 ms: 1.12x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.6 us: 1.12x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.08 ms: 1.13x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 63.5 ms: 1.13x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 64.2 ms: 1.13x slower                                                       |
| logging_format             | 6.18 us                                                     | 7.01 us: 1.13x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 37.1 ms: 1.14x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.58 us: 1.14x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 213 us: 1.14x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.76 sec: 1.15x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 88.9 ms: 1.17x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.67 sec: 1.17x slower                                                      |
| sqlglot_normalize          | 172 ms                                                      | 203 ms: 1.18x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 4.58 ms: 1.19x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 65.8 ns: 1.21x slower                                                       |
| many_optionals             | 361 us                                                      | 438 us: 1.21x slower                                                        |
| richards_super             | 29.8 ms                                                     | 36.2 ms: 1.22x slower                                                       |
| richards                   | 26.3 ms                                                     | 32.1 ms: 1.22x slower                                                       |
| django_template            | 20.3 ms                                                     | 25.8 ms: 1.27x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.42 ms: 1.28x slower                                                       |
| raytrace                   | 153 ms                                                      | 208 ms: 1.35x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 15.8 ms: 1.46x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (9): pylint, pyflate, create_gc_cycles, bench_mp_pool, regex_compile, html5lib, xml_etree_iterparse, gc_traversal, pycparser
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.024x faster

# HPT report

- Reliability score: 83.84% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
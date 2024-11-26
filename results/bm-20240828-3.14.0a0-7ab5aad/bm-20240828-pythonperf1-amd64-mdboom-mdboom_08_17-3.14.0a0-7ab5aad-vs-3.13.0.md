# Results vs. 3.13.0

- fork: mdboom
- ref: mdboom_08_17
- machine: windows-amd64
- commit hash: 7ab5aad
- commit date: 2024-08-28
- overall geometric mean: 1.026x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 233 ms: 1.05x slower                                               |
| docutils       | 1.57 sec                                                    | 1.75 sec: 1.11x slower                                             |
| html5lib       | 38.9 ms                                                     | 41.9 ms: 1.08x slower                                              |
| Geometric mean | (ref)                                                       | 1.06x slower                                                       |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.14x faster                                               |
| async_tree_none_tg         | 209 ms                                                      | 199 ms: 1.05x faster                                               |
| async_tree_none            | 226 ms                                                      | 220 ms: 1.03x faster                                               |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 389 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 394 ms: 1.05x slower                                               |
| async_tree_io_tg           | 518 ms                                                      | 548 ms: 1.06x slower                                               |
| async_tree_io              | 521 ms                                                      | 581 ms: 1.11x slower                                               |
| coroutines                 | 12.8 ms                                                     | 14.4 ms: 1.13x slower                                              |
| async_generators           | 223 ms                                                      | 253 ms: 1.13x slower                                               |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                       |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                               |
| float          | 49.9 ms                                                     | 56.1 ms: 1.12x slower                                              |
| nbody          | 68.4 ms                                                     | 85.1 ms: 1.24x slower                                              |
| Geometric mean | (ref)                                                       | 1.13x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.0 ms: 1.43x faster                                              |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                               |
| regex_compile  | 80.5 ms                                                     | 90.4 ms: 1.12x slower                                              |
| Geometric mean | (ref)                                                       | 1.05x faster                                                       |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_parse      | 93.6 ms                                                     | 96.0 ms: 1.03x slower                                              |
| json_dumps           | 5.92 ms                                                     | 6.08 ms: 1.03x slower                                              |
| xml_etree_iterparse  | 61.8 ms                                                     | 65.1 ms: 1.05x slower                                              |
| xml_etree_generate   | 54.0 ms                                                     | 57.7 ms: 1.07x slower                                              |
| xml_etree_process    | 37.0 ms                                                     | 40.2 ms: 1.09x slower                                              |
| pickle_pure_python   | 190 us                                                      | 210 us: 1.11x slower                                               |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                               |
| tomli_loads          | 1.39 sec                                                    | 1.58 sec: 1.13x slower                                             |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                       |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 22.2 ms: 1.14x faster                                              |
| Geometric mean | (ref)                                                       | 1.07x faster                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 37.1 ms: 1.05x slower                                              |
| mako            | 6.35 ms                                                     | 6.98 ms: 1.10x slower                                              |
| django_template | 22.4 ms                                                     | 25.0 ms: 1.12x slower                                              |
| genshi_text     | 15.6 ms                                                     | 17.5 ms: 1.12x slower                                              |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 520 us: 16.90x faster                                              |
| regex_v8                   | 21.4 ms                                                     | 15.0 ms: 1.43x faster                                              |
| create_gc_cycles           | 1.26 ms                                                     | 908 us: 1.39x faster                                               |
| bench_mp_pool              | 86.4 ms                                                     | 68.4 ms: 1.26x faster                                              |
| gc_traversal               | 1.97 ms                                                     | 1.58 ms: 1.25x faster                                              |
| deepcopy                   | 226 us                                                      | 189 us: 1.20x faster                                               |
| deepcopy_memo              | 23.3 us                                                     | 20.3 us: 1.15x faster                                              |
| python_startup             | 25.4 ms                                                     | 22.2 ms: 1.14x faster                                              |
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.14x faster                                               |
| deepcopy_reduce            | 2.06 us                                                     | 1.92 us: 1.07x faster                                              |
| async_tree_none_tg         | 209 ms                                                      | 199 ms: 1.05x faster                                               |
| pathlib                    | 80.9 ms                                                     | 77.9 ms: 1.04x faster                                              |
| async_tree_none            | 226 ms                                                      | 220 ms: 1.03x faster                                               |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 389 ms: 1.01x slower                                               |
| mdp                        | 1.39 sec                                                    | 1.42 sec: 1.02x slower                                             |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                               |
| xml_etree_parse            | 93.6 ms                                                     | 96.0 ms: 1.03x slower                                              |
| json_dumps                 | 5.92 ms                                                     | 6.08 ms: 1.03x slower                                              |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                               |
| telco                      | 4.79 ms                                                     | 4.99 ms: 1.04x slower                                              |
| sympy_sum                  | 86.9 ms                                                     | 90.8 ms: 1.05x slower                                              |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 394 ms: 1.05x slower                                               |
| genshi_xml                 | 35.5 ms                                                     | 37.1 ms: 1.05x slower                                              |
| 2to3                       | 221 ms                                                      | 233 ms: 1.05x slower                                               |
| xml_etree_iterparse        | 61.8 ms                                                     | 65.1 ms: 1.05x slower                                              |
| dulwich_log                | 40.8 ms                                                     | 43.0 ms: 1.05x slower                                              |
| sympy_expand               | 291 ms                                                      | 308 ms: 1.06x slower                                               |
| async_tree_io_tg           | 518 ms                                                      | 548 ms: 1.06x slower                                               |
| sympy_str                  | 169 ms                                                      | 178 ms: 1.06x slower                                               |
| meteor_contest             | 73.5 ms                                                     | 77.8 ms: 1.06x slower                                              |
| generators                 | 19.5 ms                                                     | 20.6 ms: 1.06x slower                                              |
| crypto_pyaes               | 45.4 ms                                                     | 48.1 ms: 1.06x slower                                              |
| logging_simple             | 5.96 us                                                     | 6.32 us: 1.06x slower                                              |
| sympy_integrate            | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                              |
| xml_etree_generate         | 54.0 ms                                                     | 57.7 ms: 1.07x slower                                              |
| pylint                     | 211 ms                                                      | 227 ms: 1.08x slower                                               |
| html5lib                   | 38.9 ms                                                     | 41.9 ms: 1.08x slower                                              |
| typing_runtime_protocols   | 105 us                                                      | 114 us: 1.08x slower                                               |
| logging_format             | 6.26 us                                                     | 6.78 us: 1.08x slower                                              |
| xml_etree_process          | 37.0 ms                                                     | 40.2 ms: 1.09x slower                                              |
| sqlglot_optimize           | 32.9 ms                                                     | 36.0 ms: 1.10x slower                                              |
| mako                       | 6.35 ms                                                     | 6.98 ms: 1.10x slower                                              |
| coverage                   | 45.6 ms                                                     | 50.1 ms: 1.10x slower                                              |
| pickle_pure_python         | 190 us                                                      | 210 us: 1.11x slower                                               |
| sqlglot_normalize          | 175 ms                                                      | 193 ms: 1.11x slower                                               |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                               |
| docutils                   | 1.57 sec                                                    | 1.75 sec: 1.11x slower                                             |
| async_tree_io              | 521 ms                                                      | 581 ms: 1.11x slower                                               |
| django_template            | 22.4 ms                                                     | 25.0 ms: 1.12x slower                                              |
| hexiom                     | 3.89 ms                                                     | 4.36 ms: 1.12x slower                                              |
| float                      | 49.9 ms                                                     | 56.1 ms: 1.12x slower                                              |
| go                         | 87.0 ms                                                     | 97.6 ms: 1.12x slower                                              |
| regex_compile              | 80.5 ms                                                     | 90.4 ms: 1.12x slower                                              |
| genshi_text                | 15.6 ms                                                     | 17.5 ms: 1.12x slower                                              |
| pprint_safe_repr           | 494 ms                                                      | 555 ms: 1.12x slower                                               |
| coroutines                 | 12.8 ms                                                     | 14.4 ms: 1.13x slower                                              |
| tomli_loads                | 1.39 sec                                                    | 1.58 sec: 1.13x slower                                             |
| async_generators           | 223 ms                                                      | 253 ms: 1.13x slower                                               |
| spectral_norm              | 62.8 ms                                                     | 71.3 ms: 1.14x slower                                              |
| chaos                      | 38.5 ms                                                     | 44.0 ms: 1.14x slower                                              |
| nqueens                    | 56.7 ms                                                     | 64.7 ms: 1.14x slower                                              |
| pprint_pformat             | 999 ms                                                      | 1.14 sec: 1.15x slower                                             |
| pyflate                    | 283 ms                                                      | 325 ms: 1.15x slower                                               |
| logging_silent             | 54.6 ns                                                     | 62.9 ns: 1.15x slower                                              |
| sqlglot_transpile          | 956 us                                                      | 1.10 ms: 1.15x slower                                              |
| sqlglot_parse              | 771 us                                                      | 889 us: 1.15x slower                                               |
| comprehensions             | 10.3 us                                                     | 11.9 us: 1.16x slower                                              |
| deltablue                  | 1.92 ms                                                     | 2.24 ms: 1.17x slower                                              |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.86 ms: 1.17x slower                                              |
| fannkuch                   | 253 ms                                                      | 297 ms: 1.17x slower                                               |
| raytrace                   | 160 ms                                                      | 187 ms: 1.17x slower                                               |
| scimark_lu                 | 53.0 ms                                                     | 63.3 ms: 1.19x slower                                              |
| scimark_fft                | 172 ms                                                      | 207 ms: 1.20x slower                                               |
| scimark_monte_carlo        | 40.8 ms                                                     | 49.5 ms: 1.21x slower                                              |
| richards                   | 27.3 ms                                                     | 33.3 ms: 1.22x slower                                              |
| scimark_sor                | 76.2 ms                                                     | 93.0 ms: 1.22x slower                                              |
| richards_super             | 30.9 ms                                                     | 37.7 ms: 1.22x slower                                              |
| nbody                      | 68.4 ms                                                     | 85.1 ms: 1.24x slower                                              |
| pycparser                  | 683 ms                                                      | 871 ms: 1.28x slower                                               |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                       |

Benchmark hidden because not significant (7): async_tree_memoization, json, bench_thread_pool, json_loads, python_startup_no_site, regex_effbot, tornado_http
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240828-3.14.0a0-7ab5aad/bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.026x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown
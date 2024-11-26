# Results vs. 3.13.0

- fork: brandtbucher
- ref: jump_backoff
- machine: windows-amd64
- commit hash: 5dd5806
- commit date: 2024-11-13
- overall geometric mean: 1.007x faster
- HPT reliability: 92.90%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 229 ms: 1.04x slower                                                      |
| docutils       | 1.57 sec                                                    | 1.84 sec: 1.17x slower                                                    |
| sphinx         | 633 ms                                                      | 737 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.09x slower                                                              |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 258 ms: 1.12x faster                                                      |
| asyncio_websockets         | 318 ms                                                      | 292 ms: 1.09x faster                                                      |
| async_tree_none            | 226 ms                                                      | 214 ms: 1.05x faster                                                      |
| async_tree_none_tg         | 209 ms                                                      | 205 ms: 1.02x faster                                                      |
| async_tree_io              | 521 ms                                                      | 544 ms: 1.04x slower                                                      |
| coroutines                 | 12.8 ms                                                     | 13.5 ms: 1.06x slower                                                     |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 400 ms: 1.06x slower                                                      |
| async_generators           | 223 ms                                                      | 268 ms: 1.20x slower                                                      |
| async_tree_io_tg           | 518 ms                                                      | 626 ms: 1.21x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                              |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 56.7 ms: 1.21x faster                                                     |
| float          | 49.9 ms                                                     | 47.4 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                       | 1.08x faster                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.7 ms: 1.36x faster                                                     |
| regex_effbot   | 1.58 ms                                                     | 1.60 ms: 1.01x slower                                                     |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                      |
| regex_compile  | 80.5 ms                                                     | 87.6 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                       | 1.04x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 109 us: 1.23x faster                                                      |
| tomli_loads          | 1.39 sec                                                    | 1.26 sec: 1.10x faster                                                    |
| xml_etree_generate   | 54.0 ms                                                     | 49.7 ms: 1.09x faster                                                     |
| xml_etree_process    | 37.0 ms                                                     | 35.5 ms: 1.04x faster                                                     |
| json_loads           | 15.1 us                                                     | 14.7 us: 1.03x faster                                                     |
| xml_etree_iterparse  | 61.8 ms                                                     | 62.3 ms: 1.01x slower                                                     |
| json_dumps           | 5.92 ms                                                     | 6.20 ms: 1.05x slower                                                     |
| pickle_pure_python   | 190 us                                                      | 208 us: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 24.0 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                       | 1.03x faster                                                              |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.12 ms: 1.24x faster                                                     |
| genshi_text     | 15.6 ms                                                     | 18.4 ms: 1.18x slower                                                     |
| django_template | 22.4 ms                                                     | 26.6 ms: 1.19x slower                                                     |
| genshi_xml      | 35.5 ms                                                     | 44.0 ms: 1.24x slower                                                     |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 552 us: 15.94x faster                                                     |
| deepcopy_memo              | 23.3 us                                                     | 16.8 us: 1.39x faster                                                     |
| regex_v8                   | 21.4 ms                                                     | 15.7 ms: 1.36x faster                                                     |
| mako                       | 6.35 ms                                                     | 5.12 ms: 1.24x faster                                                     |
| unpickle_pure_python       | 133 us                                                      | 109 us: 1.23x faster                                                      |
| nbody                      | 68.4 ms                                                     | 56.7 ms: 1.21x faster                                                     |
| scimark_sor                | 76.2 ms                                                     | 63.5 ms: 1.20x faster                                                     |
| deepcopy                   | 226 us                                                      | 192 us: 1.18x faster                                                      |
| crypto_pyaes               | 45.4 ms                                                     | 39.9 ms: 1.14x faster                                                     |
| telco                      | 4.79 ms                                                     | 4.25 ms: 1.13x faster                                                     |
| spectral_norm              | 62.8 ms                                                     | 55.7 ms: 1.13x faster                                                     |
| async_tree_memoization_tg  | 288 ms                                                      | 258 ms: 1.12x faster                                                      |
| scimark_monte_carlo        | 40.8 ms                                                     | 36.7 ms: 1.11x faster                                                     |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.21 ms: 1.11x faster                                                     |
| scimark_fft                | 172 ms                                                      | 156 ms: 1.10x faster                                                      |
| tomli_loads                | 1.39 sec                                                    | 1.26 sec: 1.10x faster                                                    |
| deepcopy_reduce            | 2.06 us                                                     | 1.87 us: 1.10x faster                                                     |
| asyncio_websockets         | 318 ms                                                      | 292 ms: 1.09x faster                                                      |
| xml_etree_generate         | 54.0 ms                                                     | 49.7 ms: 1.09x faster                                                     |
| pathlib                    | 80.9 ms                                                     | 75.0 ms: 1.08x faster                                                     |
| connected_components       | 332 ms                                                      | 310 ms: 1.07x faster                                                      |
| json                       | 3.19 ms                                                     | 2.99 ms: 1.07x faster                                                     |
| python_startup             | 25.4 ms                                                     | 24.0 ms: 1.06x faster                                                     |
| pprint_pformat             | 999 ms                                                      | 944 ms: 1.06x faster                                                      |
| pprint_safe_repr           | 494 ms                                                      | 467 ms: 1.06x faster                                                      |
| async_tree_none            | 226 ms                                                      | 214 ms: 1.05x faster                                                      |
| float                      | 49.9 ms                                                     | 47.4 ms: 1.05x faster                                                     |
| bench_thread_pool          | 847 us                                                      | 807 us: 1.05x faster                                                      |
| xml_etree_process          | 37.0 ms                                                     | 35.5 ms: 1.04x faster                                                     |
| bpe_tokeniser              | 2.91 sec                                                    | 2.80 sec: 1.04x faster                                                    |
| shortest_path              | 362 ms                                                      | 350 ms: 1.03x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.7 us: 1.03x faster                                                     |
| gc_traversal               | 1.97 ms                                                     | 1.92 ms: 1.03x faster                                                     |
| meteor_contest             | 73.5 ms                                                     | 71.8 ms: 1.02x faster                                                     |
| async_tree_none_tg         | 209 ms                                                      | 205 ms: 1.02x faster                                                      |
| dulwich_log                | 40.8 ms                                                     | 40.4 ms: 1.01x faster                                                     |
| scimark_lu                 | 53.0 ms                                                     | 53.3 ms: 1.01x slower                                                     |
| xml_etree_iterparse        | 61.8 ms                                                     | 62.3 ms: 1.01x slower                                                     |
| regex_effbot               | 1.58 ms                                                     | 1.60 ms: 1.01x slower                                                     |
| pycparser                  | 683 ms                                                      | 693 ms: 1.01x slower                                                      |
| fannkuch                   | 253 ms                                                      | 258 ms: 1.02x slower                                                      |
| 2to3                       | 221 ms                                                      | 229 ms: 1.04x slower                                                      |
| async_tree_io              | 521 ms                                                      | 544 ms: 1.04x slower                                                      |
| pyflate                    | 283 ms                                                      | 296 ms: 1.05x slower                                                      |
| chaos                      | 38.5 ms                                                     | 40.4 ms: 1.05x slower                                                     |
| json_dumps                 | 5.92 ms                                                     | 6.20 ms: 1.05x slower                                                     |
| logging_simple             | 5.96 us                                                     | 6.25 us: 1.05x slower                                                     |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 57.9 ns: 1.06x slower                                                     |
| coroutines                 | 12.8 ms                                                     | 13.5 ms: 1.06x slower                                                     |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 400 ms: 1.06x slower                                                      |
| logging_format             | 6.26 us                                                     | 6.68 us: 1.07x slower                                                     |
| coverage                   | 45.6 ms                                                     | 48.7 ms: 1.07x slower                                                     |
| go                         | 87.0 ms                                                     | 93.1 ms: 1.07x slower                                                     |
| typing_runtime_protocols   | 105 us                                                      | 114 us: 1.08x slower                                                      |
| regex_compile              | 80.5 ms                                                     | 87.6 ms: 1.09x slower                                                     |
| create_gc_cycles           | 1.26 ms                                                     | 1.37 ms: 1.09x slower                                                     |
| sympy_str                  | 169 ms                                                      | 184 ms: 1.09x slower                                                      |
| sympy_sum                  | 86.9 ms                                                     | 94.9 ms: 1.09x slower                                                     |
| sympy_expand               | 291 ms                                                      | 320 ms: 1.10x slower                                                      |
| pickle_pure_python         | 190 us                                                      | 208 us: 1.10x slower                                                      |
| sympy_integrate            | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                     |
| nqueens                    | 56.7 ms                                                     | 64.1 ms: 1.13x slower                                                     |
| sqlglot_parse              | 771 us                                                      | 878 us: 1.14x slower                                                      |
| generators                 | 19.5 ms                                                     | 22.3 ms: 1.15x slower                                                     |
| pylint                     | 211 ms                                                      | 244 ms: 1.16x slower                                                      |
| sphinx                     | 633 ms                                                      | 737 ms: 1.16x slower                                                      |
| comprehensions             | 10.3 us                                                     | 12.0 us: 1.17x slower                                                     |
| mdp                        | 1.39 sec                                                    | 1.63 sec: 1.17x slower                                                    |
| docutils                   | 1.57 sec                                                    | 1.84 sec: 1.17x slower                                                    |
| sqlglot_optimize           | 32.9 ms                                                     | 38.7 ms: 1.17x slower                                                     |
| sqlglot_transpile          | 956 us                                                      | 1.13 ms: 1.18x slower                                                     |
| genshi_text                | 15.6 ms                                                     | 18.4 ms: 1.18x slower                                                     |
| django_template            | 22.4 ms                                                     | 26.6 ms: 1.19x slower                                                     |
| sqlglot_normalize          | 175 ms                                                      | 208 ms: 1.19x slower                                                      |
| async_generators           | 223 ms                                                      | 268 ms: 1.20x slower                                                      |
| async_tree_io_tg           | 518 ms                                                      | 626 ms: 1.21x slower                                                      |
| deltablue                  | 1.92 ms                                                     | 2.34 ms: 1.22x slower                                                     |
| richards_super             | 30.9 ms                                                     | 37.7 ms: 1.22x slower                                                     |
| genshi_xml                 | 35.5 ms                                                     | 44.0 ms: 1.24x slower                                                     |
| richards                   | 27.3 ms                                                     | 33.9 ms: 1.24x slower                                                     |
| hexiom                     | 3.89 ms                                                     | 5.05 ms: 1.30x slower                                                     |
| raytrace                   | 160 ms                                                      | 214 ms: 1.34x slower                                                      |
| k_core                     | 1.74 sec                                                    | 2.45 sec: 1.41x slower                                                    |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                              |

Benchmark hidden because not significant (7): python_startup_no_site, html5lib, xml_etree_parse, pidigits, async_tree_memoization, bench_mp_pool, async_tree_cpu_io_mixed
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241113-3.14.0a1+-5dd5806-JIT/bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806.json: sqlite_synth

- Geometric mean (including insignificant results): 1.007x faster
# HPT report

- Reliability score: 92.90% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown
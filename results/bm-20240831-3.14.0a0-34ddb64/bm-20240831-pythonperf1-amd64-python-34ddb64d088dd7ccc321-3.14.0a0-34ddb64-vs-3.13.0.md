# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-amd64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.012x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 226 ms: 1.02x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.69 sec: 1.08x slower                                                     |
| html5lib       | 38.9 ms                                                     | 40.7 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 250 ms: 1.15x faster                                                       |
| async_tree_none            | 226 ms                                                      | 210 ms: 1.08x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 260 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 390 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 399 ms: 1.06x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 564 ms: 1.09x slower                                                       |
| async_tree_io              | 521 ms                                                      | 573 ms: 1.10x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.10x slower                                                      |
| async_generators           | 223 ms                                                      | 249 ms: 1.11x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 152 ms: 1.03x slower                                                       |
| float          | 49.9 ms                                                     | 56.2 ms: 1.12x slower                                                      |
| nbody          | 68.4 ms                                                     | 83.6 ms: 1.22x slower                                                      |
| Geometric mean | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.5 ms: 1.38x faster                                                      |
| regex_effbot   | 1.58 ms                                                     | 1.54 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 116 ms: 1.01x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 91.5 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| xml_etree_parse      | 93.6 ms                                                     | 95.6 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 65.0 ms: 1.05x slower                                                      |
| json_dumps           | 5.92 ms                                                     | 6.24 ms: 1.05x slower                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 57.7 ms: 1.07x slower                                                      |
| pickle_pure_python   | 190 us                                                      | 208 us: 1.10x slower                                                       |
| xml_etree_process    | 37.0 ms                                                     | 40.9 ms: 1.10x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 149 us: 1.12x slower                                                       |
| tomli_loads          | 1.39 sec                                                    | 1.59 sec: 1.14x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 22.2 ms: 1.15x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.6 ms                                                     | 16.5 ms: 1.06x slower                                                      |
| django_template | 22.4 ms                                                     | 24.2 ms: 1.08x slower                                                      |
| mako            | 6.35 ms                                                     | 6.87 ms: 1.08x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 525 us: 16.76x faster                                                      |
| regex_v8                   | 21.4 ms                                                     | 15.5 ms: 1.38x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 917 us: 1.37x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.55 ms: 1.27x faster                                                      |
| bench_mp_pool              | 86.4 ms                                                     | 68.7 ms: 1.26x faster                                                      |
| deepcopy                   | 226 us                                                      | 186 us: 1.22x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 19.5 us: 1.20x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 250 ms: 1.15x faster                                                       |
| python_startup             | 25.4 ms                                                     | 22.2 ms: 1.15x faster                                                      |
| deepcopy_reduce            | 2.06 us                                                     | 1.90 us: 1.08x faster                                                      |
| async_tree_none            | 226 ms                                                      | 210 ms: 1.08x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 260 ms: 1.06x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| go                         | 87.0 ms                                                     | 84.7 ms: 1.03x faster                                                      |
| regex_effbot               | 1.58 ms                                                     | 1.54 ms: 1.02x faster                                                      |
| pathlib                    | 80.9 ms                                                     | 79.4 ms: 1.02x faster                                                      |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 390 ms: 1.02x slower                                                       |
| xml_etree_parse            | 93.6 ms                                                     | 95.6 ms: 1.02x slower                                                      |
| 2to3                       | 221 ms                                                      | 226 ms: 1.02x slower                                                       |
| pidigits                   | 148 ms                                                      | 152 ms: 1.03x slower                                                       |
| mdp                        | 1.39 sec                                                    | 1.43 sec: 1.03x slower                                                     |
| sympy_sum                  | 86.9 ms                                                     | 90.1 ms: 1.04x slower                                                      |
| html5lib                   | 38.9 ms                                                     | 40.7 ms: 1.05x slower                                                      |
| sympy_str                  | 169 ms                                                      | 177 ms: 1.05x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                                      |
| logging_simple             | 5.96 us                                                     | 6.25 us: 1.05x slower                                                      |
| xml_etree_iterparse        | 61.8 ms                                                     | 65.0 ms: 1.05x slower                                                      |
| sympy_expand               | 291 ms                                                      | 307 ms: 1.05x slower                                                       |
| crypto_pyaes               | 45.4 ms                                                     | 47.8 ms: 1.05x slower                                                      |
| json_dumps                 | 5.92 ms                                                     | 6.24 ms: 1.05x slower                                                      |
| generators                 | 19.5 ms                                                     | 20.6 ms: 1.05x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 16.5 ms: 1.06x slower                                                      |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 399 ms: 1.06x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.63 us: 1.06x slower                                                      |
| telco                      | 4.79 ms                                                     | 5.09 ms: 1.06x slower                                                      |
| meteor_contest             | 73.5 ms                                                     | 78.3 ms: 1.07x slower                                                      |
| xml_etree_generate         | 54.0 ms                                                     | 57.7 ms: 1.07x slower                                                      |
| spectral_norm              | 62.8 ms                                                     | 67.4 ms: 1.07x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.69 sec: 1.08x slower                                                     |
| django_template            | 22.4 ms                                                     | 24.2 ms: 1.08x slower                                                      |
| mako                       | 6.35 ms                                                     | 6.87 ms: 1.08x slower                                                      |
| coverage                   | 45.6 ms                                                     | 49.3 ms: 1.08x slower                                                      |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.66 ms: 1.08x slower                                                      |
| pylint                     | 211 ms                                                      | 228 ms: 1.08x slower                                                       |
| dulwich_log                | 40.8 ms                                                     | 44.4 ms: 1.09x slower                                                      |
| typing_runtime_protocols   | 105 us                                                      | 115 us: 1.09x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 564 ms: 1.09x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 191 ms: 1.10x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 208 us: 1.10x slower                                                       |
| async_tree_io              | 521 ms                                                      | 573 ms: 1.10x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.10x slower                                                      |
| sqlglot_optimize           | 32.9 ms                                                     | 36.3 ms: 1.10x slower                                                      |
| xml_etree_process          | 37.0 ms                                                     | 40.9 ms: 1.10x slower                                                      |
| chaos                      | 38.5 ms                                                     | 42.7 ms: 1.11x slower                                                      |
| hexiom                     | 3.89 ms                                                     | 4.32 ms: 1.11x slower                                                      |
| pprint_pformat             | 999 ms                                                      | 1.11 sec: 1.11x slower                                                     |
| pycparser                  | 683 ms                                                      | 759 ms: 1.11x slower                                                       |
| async_generators           | 223 ms                                                      | 249 ms: 1.11x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 149 us: 1.12x slower                                                       |
| pprint_safe_repr           | 494 ms                                                      | 555 ms: 1.12x slower                                                       |
| float                      | 49.9 ms                                                     | 56.2 ms: 1.12x slower                                                      |
| scimark_fft                | 172 ms                                                      | 195 ms: 1.13x slower                                                       |
| regex_compile              | 80.5 ms                                                     | 91.5 ms: 1.14x slower                                                      |
| pyflate                    | 283 ms                                                      | 322 ms: 1.14x slower                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.59 sec: 1.14x slower                                                     |
| logging_silent             | 54.6 ns                                                     | 62.5 ns: 1.14x slower                                                      |
| fannkuch                   | 253 ms                                                      | 291 ms: 1.15x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 65.2 ms: 1.15x slower                                                      |
| comprehensions             | 10.3 us                                                     | 11.8 us: 1.15x slower                                                      |
| sqlglot_transpile          | 956 us                                                      | 1.11 ms: 1.16x slower                                                      |
| sqlglot_parse              | 771 us                                                      | 891 us: 1.16x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 88.7 ms: 1.16x slower                                                      |
| raytrace                   | 160 ms                                                      | 188 ms: 1.17x slower                                                       |
| richards_super             | 30.9 ms                                                     | 36.2 ms: 1.17x slower                                                      |
| deltablue                  | 1.92 ms                                                     | 2.25 ms: 1.17x slower                                                      |
| scimark_lu                 | 53.0 ms                                                     | 62.3 ms: 1.18x slower                                                      |
| richards                   | 27.3 ms                                                     | 32.4 ms: 1.18x slower                                                      |
| scimark_monte_carlo        | 40.8 ms                                                     | 49.1 ms: 1.20x slower                                                      |
| nbody                      | 68.4 ms                                                     | 83.6 ms: 1.22x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (6): async_tree_none_tg, json, bench_thread_pool, python_startup_no_site, tornado_http, genshi_xml
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.012x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown
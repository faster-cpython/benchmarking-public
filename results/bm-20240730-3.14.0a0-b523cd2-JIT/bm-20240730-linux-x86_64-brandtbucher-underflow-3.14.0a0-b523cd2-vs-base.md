# Results vs. base

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: b523cd2
- commit date: 2024-07-30
- overall geometric mean: 1.01x slower
- HPT reliability: 99.59%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 273 ms                                                                | 278 ms: 1.02x slower                                             |
| docutils       | 2.91 sec                                                              | 3.09 sec: 1.06x slower                                           |
| html5lib       | 66.2 ms                                                               | 69.7 ms: 1.05x slower                                            |
| tornado_http   | 92.3 ms                                                               | 103 ms: 1.12x slower                                             |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| asyncio_websockets     | 559 ms                                                                | 555 ms: 1.01x faster                                             |
| asyncio_tcp_ssl        | 1.81 sec                                                              | 1.81 sec: 1.00x slower                                           |
| asyncio_tcp            | 505 ms                                                                | 509 ms: 1.01x slower                                             |
| async_tree_none        | 327 ms                                                                | 331 ms: 1.01x slower                                             |
| async_tree_memoization | 418 ms                                                                | 431 ms: 1.03x slower                                             |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                     |

Benchmark hidden because not significant (8): coroutines, async_generators, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 71.0 ms                                                               | 71.5 ms: 1.01x slower                                            |
| pidigits       | 186 ms                                                                | 187 ms: 1.01x slower                                             |
| nbody          | 79.7 ms                                                               | 81.3 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.81 ms                                                               | 3.66 ms: 1.04x faster                                            |
| regex_dna      | 226 ms                                                                | 221 ms: 1.02x faster                                             |
| regex_compile  | 134 ms                                                                | 140 ms: 1.05x slower                                             |
| regex_v8       | 24.5 ms                                                               | 25.9 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 213 us                                                                | 197 us: 1.08x faster                                             |
| xml_etree_iterparse  | 99.6 ms                                                               | 98.4 ms: 1.01x faster                                            |
| xml_etree_generate   | 79.7 ms                                                               | 78.9 ms: 1.01x faster                                            |
| xml_etree_process    | 56.4 ms                                                               | 56.0 ms: 1.01x faster                                            |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                            |
| pickle_pure_python   | 299 us                                                                | 304 us: 1.02x slower                                             |
| json_loads           | 27.7 us                                                               | 28.4 us: 1.03x slower                                            |
| tomli_loads          | 1.92 sec                                                              | 1.98 sec: 1.03x slower                                           |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                     |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.22 ms: 1.02x slower                                            |
| python_startup         | 10.5 ms                                                               | 10.7 ms: 1.02x slower                                            |
| Geometric mean         | (ref)                                                                 | 1.02x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text    | 24.1 ms                                                               | 23.4 ms: 1.03x faster                                            |
| mako           | 9.81 ms                                                               | 9.78 ms: 1.00x faster                                            |
| genshi_xml     | 53.8 ms                                                               | 59.9 ms: 1.11x slower                                            |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python     | 213 us                                                                | 197 us: 1.08x faster                                             |
| richards                 | 40.5 ms                                                               | 38.1 ms: 1.06x faster                                            |
| scimark_monte_carlo      | 60.9 ms                                                               | 57.8 ms: 1.05x faster                                            |
| scimark_sparse_mat_mult  | 4.40 ms                                                               | 4.20 ms: 1.05x faster                                            |
| spectral_norm            | 105 ms                                                                | 99.8 ms: 1.05x faster                                            |
| richards_super           | 46.4 ms                                                               | 44.4 ms: 1.04x faster                                            |
| deepcopy                 | 274 us                                                                | 263 us: 1.04x faster                                             |
| regex_effbot             | 3.81 ms                                                               | 3.66 ms: 1.04x faster                                            |
| genshi_text              | 24.1 ms                                                               | 23.4 ms: 1.03x faster                                            |
| scimark_fft              | 309 ms                                                                | 300 ms: 1.03x faster                                             |
| pprint_safe_repr         | 734 ms                                                                | 716 ms: 1.03x faster                                             |
| logging_silent           | 104 ns                                                                | 102 ns: 1.03x faster                                             |
| regex_dna                | 226 ms                                                                | 221 ms: 1.02x faster                                             |
| deepcopy_memo            | 29.0 us                                                               | 28.4 us: 1.02x faster                                            |
| nqueens                  | 84.5 ms                                                               | 83.0 ms: 1.02x faster                                            |
| scimark_sor              | 129 ms                                                                | 127 ms: 1.02x faster                                             |
| xml_etree_iterparse      | 99.6 ms                                                               | 98.4 ms: 1.01x faster                                            |
| telco                    | 7.82 ms                                                               | 7.73 ms: 1.01x faster                                            |
| scimark_lu               | 124 ms                                                                | 122 ms: 1.01x faster                                             |
| pprint_pformat           | 1.49 sec                                                              | 1.48 sec: 1.01x faster                                           |
| xml_etree_generate       | 79.7 ms                                                               | 78.9 ms: 1.01x faster                                            |
| pathlib                  | 16.1 ms                                                               | 16.0 ms: 1.01x faster                                            |
| asyncio_websockets       | 559 ms                                                                | 555 ms: 1.01x faster                                             |
| coverage                 | 91.7 ms                                                               | 91.0 ms: 1.01x faster                                            |
| xml_etree_process        | 56.4 ms                                                               | 56.0 ms: 1.01x faster                                            |
| crypto_pyaes             | 67.3 ms                                                               | 66.9 ms: 1.01x faster                                            |
| thrift                   | 797 us                                                                | 792 us: 1.01x faster                                             |
| bpe_tokeniser            | 4.52 sec                                                              | 4.50 sec: 1.00x faster                                           |
| mako                     | 9.81 ms                                                               | 9.78 ms: 1.00x faster                                            |
| gc_traversal             | 3.52 ms                                                               | 3.53 ms: 1.00x slower                                            |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.81 sec: 1.00x slower                                           |
| meteor_contest           | 105 ms                                                                | 105 ms: 1.00x slower                                             |
| create_gc_cycles         | 1.74 ms                                                               | 1.75 ms: 1.01x slower                                            |
| float                    | 71.0 ms                                                               | 71.5 ms: 1.01x slower                                            |
| asyncio_tcp              | 505 ms                                                                | 509 ms: 1.01x slower                                             |
| raytrace                 | 266 ms                                                                | 268 ms: 1.01x slower                                             |
| pidigits                 | 186 ms                                                                | 187 ms: 1.01x slower                                             |
| typing_runtime_protocols | 170 us                                                                | 172 us: 1.01x slower                                             |
| fannkuch                 | 363 ms                                                                | 367 ms: 1.01x slower                                             |
| pyflate                  | 431 ms                                                                | 436 ms: 1.01x slower                                             |
| json_dumps               | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                            |
| async_tree_none          | 327 ms                                                                | 331 ms: 1.01x slower                                             |
| sqlglot_optimize         | 55.9 ms                                                               | 56.6 ms: 1.01x slower                                            |
| hexiom                   | 6.68 ms                                                               | 6.78 ms: 1.01x slower                                            |
| python_startup_no_site   | 7.11 ms                                                               | 7.22 ms: 1.02x slower                                            |
| bench_thread_pool        | 815 us                                                                | 827 us: 1.02x slower                                             |
| comprehensions           | 16.1 us                                                               | 16.4 us: 1.02x slower                                            |
| python_startup           | 10.5 ms                                                               | 10.7 ms: 1.02x slower                                            |
| generators               | 32.7 ms                                                               | 33.3 ms: 1.02x slower                                            |
| 2to3                     | 273 ms                                                                | 278 ms: 1.02x slower                                             |
| pickle_pure_python       | 299 us                                                                | 304 us: 1.02x slower                                             |
| nbody                    | 79.7 ms                                                               | 81.3 ms: 1.02x slower                                            |
| json_loads               | 27.7 us                                                               | 28.4 us: 1.03x slower                                            |
| tomli_loads              | 1.92 sec                                                              | 1.98 sec: 1.03x slower                                           |
| async_tree_memoization   | 418 ms                                                                | 431 ms: 1.03x slower                                             |
| logging_format           | 6.07 us                                                               | 6.26 us: 1.03x slower                                            |
| logging_simple           | 5.47 us                                                               | 5.67 us: 1.04x slower                                            |
| dask                     | 363 ms                                                                | 379 ms: 1.05x slower                                             |
| regex_compile            | 134 ms                                                                | 140 ms: 1.05x slower                                             |
| sqlglot_normalize        | 111 ms                                                                | 117 ms: 1.05x slower                                             |
| html5lib                 | 66.2 ms                                                               | 69.7 ms: 1.05x slower                                            |
| regex_v8                 | 24.5 ms                                                               | 25.9 ms: 1.06x slower                                            |
| sympy_expand             | 507 ms                                                                | 538 ms: 1.06x slower                                             |
| docutils                 | 2.91 sec                                                              | 3.09 sec: 1.06x slower                                           |
| sympy_sum                | 170 ms                                                                | 183 ms: 1.07x slower                                             |
| sympy_integrate          | 22.4 ms                                                               | 24.2 ms: 1.08x slower                                            |
| mdp                      | 2.56 sec                                                              | 2.77 sec: 1.08x slower                                           |
| sympy_str                | 298 ms                                                                | 323 ms: 1.08x slower                                             |
| sqlglot_transpile        | 1.63 ms                                                               | 1.77 ms: 1.09x slower                                            |
| pylint                   | 355 ms                                                                | 390 ms: 1.10x slower                                             |
| deltablue                | 3.52 ms                                                               | 3.86 ms: 1.10x slower                                            |
| sqlglot_parse            | 1.30 ms                                                               | 1.42 ms: 1.10x slower                                            |
| genshi_xml               | 53.8 ms                                                               | 59.9 ms: 1.11x slower                                            |
| tornado_http             | 92.3 ms                                                               | 103 ms: 1.12x slower                                             |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                     |

Benchmark hidden because not significant (16): deepcopy_reduce, coroutines, go, xml_etree_parse, bench_mp_pool, async_generators, chaos, django_template, pycparser, json, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.59% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x
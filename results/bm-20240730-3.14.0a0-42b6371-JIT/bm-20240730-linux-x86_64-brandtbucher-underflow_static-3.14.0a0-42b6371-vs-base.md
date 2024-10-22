# Results vs. base

- fork: brandtbucher
- ref: underflow_static
- machine: linux-x86_64
- commit hash: 42b6371
- commit date: 2024-07-30
- overall geometric mean: 1.01x slower
- HPT reliability: 99.33%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 273 ms                                                                | 277 ms: 1.01x slower                                                    |
| docutils       | 2.91 sec                                                              | 2.97 sec: 1.02x slower                                                  |
| html5lib       | 66.2 ms                                                               | 62.7 ms: 1.06x faster                                                   |
| tornado_http   | 92.3 ms                                                               | 94.0 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization | 418 ms                                                                | 400 ms: 1.04x faster                                                    |
| coroutines             | 22.9 ms                                                               | 22.7 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl        | 1.81 sec                                                              | 1.80 sec: 1.01x faster                                                  |
| asyncio_tcp            | 505 ms                                                                | 507 ms: 1.00x slower                                                    |
| async_generators       | 453 ms                                                                | 465 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_memoization_tg, async_tree_none, asyncio_websockets, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 79.7 ms                                                               | 79.2 ms: 1.01x faster                                                   |
| pidigits       | 186 ms                                                                | 185 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.81 ms                                                               | 3.79 ms: 1.01x faster                                                   |
| regex_dna      | 226 ms                                                                | 231 ms: 1.02x slower                                                    |
| regex_compile  | 134 ms                                                                | 137 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 213 us                                                                | 207 us: 1.03x faster                                                    |
| xml_etree_process    | 56.4 ms                                                               | 55.9 ms: 1.01x faster                                                   |
| xml_etree_generate   | 79.7 ms                                                               | 79.1 ms: 1.01x faster                                                   |
| json_dumps           | 10.3 ms                                                               | 10.3 ms: 1.01x faster                                                   |
| json_loads           | 27.7 us                                                               | 28.0 us: 1.01x slower                                                   |
| tomli_loads          | 1.92 sec                                                              | 1.98 sec: 1.03x slower                                                  |
| pickle_pure_python   | 299 us                                                                | 315 us: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.14 ms: 1.00x slower                                                   |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                               | 9.91 ms: 1.01x slower                                                   |
| django_template | 36.1 ms                                                               | 36.6 ms: 1.01x slower                                                   |
| genshi_xml      | 53.8 ms                                                               | 57.2 ms: 1.06x slower                                                   |
| genshi_text     | 24.1 ms                                                               | 25.7 ms: 1.07x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.04x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo            | 29.0 us                                                               | 26.8 us: 1.08x faster                                                   |
| deltablue                | 3.52 ms                                                               | 3.26 ms: 1.08x faster                                                   |
| html5lib                 | 66.2 ms                                                               | 62.7 ms: 1.06x faster                                                   |
| async_tree_memoization   | 418 ms                                                                | 400 ms: 1.04x faster                                                    |
| richards_super           | 46.4 ms                                                               | 44.9 ms: 1.03x faster                                                   |
| scimark_sparse_mat_mult  | 4.40 ms                                                               | 4.27 ms: 1.03x faster                                                   |
| richards                 | 40.5 ms                                                               | 39.3 ms: 1.03x faster                                                   |
| unpickle_pure_python     | 213 us                                                                | 207 us: 1.03x faster                                                    |
| spectral_norm            | 105 ms                                                                | 102 ms: 1.02x faster                                                    |
| scimark_monte_carlo      | 60.9 ms                                                               | 59.6 ms: 1.02x faster                                                   |
| scimark_fft              | 309 ms                                                                | 303 ms: 1.02x faster                                                    |
| pycparser                | 1.16 sec                                                              | 1.14 sec: 1.02x faster                                                  |
| thrift                   | 797 us                                                                | 787 us: 1.01x faster                                                    |
| logging_silent           | 104 ns                                                                | 103 ns: 1.01x faster                                                    |
| json                     | 5.19 ms                                                               | 5.13 ms: 1.01x faster                                                   |
| coroutines               | 22.9 ms                                                               | 22.7 ms: 1.01x faster                                                   |
| xml_etree_process        | 56.4 ms                                                               | 55.9 ms: 1.01x faster                                                   |
| xml_etree_generate       | 79.7 ms                                                               | 79.1 ms: 1.01x faster                                                   |
| nbody                    | 79.7 ms                                                               | 79.2 ms: 1.01x faster                                                   |
| json_dumps               | 10.3 ms                                                               | 10.3 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.80 sec: 1.01x faster                                                  |
| coverage                 | 91.7 ms                                                               | 91.2 ms: 1.01x faster                                                   |
| regex_effbot             | 3.81 ms                                                               | 3.79 ms: 1.01x faster                                                   |
| pidigits                 | 186 ms                                                                | 185 ms: 1.00x faster                                                    |
| python_startup_no_site   | 7.11 ms                                                               | 7.14 ms: 1.00x slower                                                   |
| create_gc_cycles         | 1.74 ms                                                               | 1.74 ms: 1.00x slower                                                   |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                   |
| asyncio_tcp              | 505 ms                                                                | 507 ms: 1.00x slower                                                    |
| meteor_contest           | 105 ms                                                                | 105 ms: 1.01x slower                                                    |
| crypto_pyaes             | 67.3 ms                                                               | 67.8 ms: 1.01x slower                                                   |
| bench_thread_pool        | 815 us                                                                | 822 us: 1.01x slower                                                    |
| gc_traversal             | 3.52 ms                                                               | 3.55 ms: 1.01x slower                                                   |
| mako                     | 9.81 ms                                                               | 9.91 ms: 1.01x slower                                                   |
| json_loads               | 27.7 us                                                               | 28.0 us: 1.01x slower                                                   |
| deepcopy                 | 274 us                                                                | 277 us: 1.01x slower                                                    |
| sqlglot_transpile        | 1.63 ms                                                               | 1.65 ms: 1.01x slower                                                   |
| fannkuch                 | 363 ms                                                                | 368 ms: 1.01x slower                                                    |
| 2to3                     | 273 ms                                                                | 277 ms: 1.01x slower                                                    |
| typing_runtime_protocols | 170 us                                                                | 172 us: 1.01x slower                                                    |
| pyflate                  | 431 ms                                                                | 436 ms: 1.01x slower                                                    |
| django_template          | 36.1 ms                                                               | 36.6 ms: 1.01x slower                                                   |
| sympy_sum                | 170 ms                                                                | 173 ms: 1.01x slower                                                    |
| sympy_expand             | 507 ms                                                                | 515 ms: 1.02x slower                                                    |
| tornado_http             | 92.3 ms                                                               | 94.0 ms: 1.02x slower                                                   |
| comprehensions           | 16.1 us                                                               | 16.4 us: 1.02x slower                                                   |
| sympy_str                | 298 ms                                                                | 304 ms: 1.02x slower                                                    |
| regex_dna                | 226 ms                                                                | 231 ms: 1.02x slower                                                    |
| sympy_integrate          | 22.4 ms                                                               | 22.8 ms: 1.02x slower                                                   |
| hexiom                   | 6.68 ms                                                               | 6.82 ms: 1.02x slower                                                   |
| docutils                 | 2.91 sec                                                              | 2.97 sec: 1.02x slower                                                  |
| sqlglot_normalize        | 111 ms                                                                | 114 ms: 1.02x slower                                                    |
| go                       | 145 ms                                                                | 148 ms: 1.02x slower                                                    |
| sqlglot_parse            | 1.30 ms                                                               | 1.32 ms: 1.02x slower                                                   |
| async_generators         | 453 ms                                                                | 465 ms: 1.03x slower                                                    |
| sqlglot_optimize         | 55.9 ms                                                               | 57.4 ms: 1.03x slower                                                   |
| regex_compile            | 134 ms                                                                | 137 ms: 1.03x slower                                                    |
| tomli_loads              | 1.92 sec                                                              | 1.98 sec: 1.03x slower                                                  |
| deepcopy_reduce          | 2.72 us                                                               | 2.81 us: 1.03x slower                                                   |
| raytrace                 | 266 ms                                                                | 275 ms: 1.03x slower                                                    |
| logging_format           | 6.07 us                                                               | 6.28 us: 1.03x slower                                                   |
| generators               | 32.7 ms                                                               | 33.8 ms: 1.04x slower                                                   |
| logging_simple           | 5.47 us                                                               | 5.71 us: 1.04x slower                                                   |
| pickle_pure_python       | 299 us                                                                | 315 us: 1.06x slower                                                    |
| genshi_xml               | 53.8 ms                                                               | 57.2 ms: 1.06x slower                                                   |
| genshi_text              | 24.1 ms                                                               | 25.7 ms: 1.07x slower                                                   |
| chaos                    | 57.8 ms                                                               | 62.4 ms: 1.08x slower                                                   |
| mdp                      | 2.56 sec                                                              | 2.78 sec: 1.09x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (23): xml_etree_parse, async_tree_none_tg, async_tree_memoization_tg, async_tree_none, nqueens, asyncio_websockets, float, async_tree_io_tg, telco, bench_mp_pool, xml_etree_iterparse, regex_v8, bpe_tokeniser, pathlib, pprint_safe_repr, pprint_pformat, dask, async_tree_cpu_io_mixed_tg, scimark_lu, async_tree_cpu_io_mixed, scimark_sor, async_tree_io, pylint

# HPT report

- Reliability score: 99.33% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x
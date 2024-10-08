# Results vs. base

- fork: brandtbucher
- ref: underflow_static
- machine: linux-x86_64
- commit hash: 4dc2c65
- commit date: 2024-08-12
- overall geometric mean: 1.01x slower
- HPT reliability: 93.02%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 282 ms: 1.02x slower                                                    |
| docutils       | 3.01 sec                                                              | 3.30 sec: 1.10x slower                                                  |
| html5lib       | 66.7 ms                                                               | 69.6 ms: 1.04x slower                                                   |
| tornado_http   | 94.0 ms                                                               | 95.3 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|--------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| coroutines         | 22.9 ms                                                               | 22.6 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl    | 1.82 sec                                                              | 1.81 sec: 1.00x faster                                                  |
| asyncio_websockets | 555 ms                                                                | 558 ms: 1.01x slower                                                    |
| asyncio_tcp        | 504 ms                                                                | 515 ms: 1.02x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (9): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 81.6 ms                                                               | 80.3 ms: 1.02x faster                                                   |
| pidigits       | 186 ms                                                                | 188 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.76 ms                                                               | 3.75 ms: 1.00x faster                                                   |
| regex_compile  | 138 ms                                                                | 146 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 215 us                                                                | 203 us: 1.06x faster                                                    |
| pickle_pure_python   | 308 us                                                                | 303 us: 1.01x faster                                                    |
| xml_etree_generate   | 81.0 ms                                                               | 80.5 ms: 1.01x faster                                                   |
| xml_etree_iterparse  | 98.3 ms                                                               | 99.1 ms: 1.01x slower                                                   |
| tomli_loads          | 1.92 sec                                                              | 1.97 sec: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (4): json_loads, json_dumps, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 10.6 ms                                                               | 10.6 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 24.5 ms                                                               | 24.9 ms: 1.01x slower                                                   |
| genshi_xml      | 55.6 ms                                                               | 56.8 ms: 1.02x slower                                                   |
| mako            | 9.69 ms                                                               | 9.91 ms: 1.02x slower                                                   |
| django_template | 34.9 ms                                                               | 35.8 ms: 1.03x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| richards_super           | 46.6 ms                                                               | 40.2 ms: 1.16x faster                                                   |
| richards                 | 40.3 ms                                                               | 35.2 ms: 1.15x faster                                                   |
| unpickle_pure_python     | 215 us                                                                | 203 us: 1.06x faster                                                    |
| telco                    | 7.92 ms                                                               | 7.62 ms: 1.04x faster                                                   |
| scimark_sparse_mat_mult  | 4.42 ms                                                               | 4.30 ms: 1.03x faster                                                   |
| gc_traversal             | 3.89 ms                                                               | 3.78 ms: 1.03x faster                                                   |
| fannkuch                 | 375 ms                                                                | 365 ms: 1.03x faster                                                    |
| pathlib                  | 16.4 ms                                                               | 16.1 ms: 1.02x faster                                                   |
| spectral_norm            | 102 ms                                                                | 100 ms: 1.02x faster                                                    |
| crypto_pyaes             | 66.6 ms                                                               | 65.5 ms: 1.02x faster                                                   |
| nbody                    | 81.6 ms                                                               | 80.3 ms: 1.02x faster                                                   |
| nqueens                  | 85.0 ms                                                               | 83.6 ms: 1.02x faster                                                   |
| comprehensions           | 16.7 us                                                               | 16.4 us: 1.02x faster                                                   |
| pickle_pure_python       | 308 us                                                                | 303 us: 1.01x faster                                                    |
| deepcopy_memo            | 26.4 us                                                               | 26.0 us: 1.01x faster                                                   |
| coroutines               | 22.9 ms                                                               | 22.6 ms: 1.01x faster                                                   |
| thrift                   | 797 us                                                                | 787 us: 1.01x faster                                                    |
| json                     | 5.09 ms                                                               | 5.04 ms: 1.01x faster                                                   |
| typing_runtime_protocols | 170 us                                                                | 169 us: 1.01x faster                                                    |
| bpe_tokeniser            | 4.56 sec                                                              | 4.53 sec: 1.01x faster                                                  |
| xml_etree_generate       | 81.0 ms                                                               | 80.5 ms: 1.01x faster                                                   |
| regex_effbot             | 3.76 ms                                                               | 3.75 ms: 1.00x faster                                                   |
| asyncio_tcp_ssl          | 1.82 sec                                                              | 1.81 sec: 1.00x faster                                                  |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.00x faster                                                   |
| create_gc_cycles         | 1.78 ms                                                               | 1.78 ms: 1.00x slower                                                   |
| deltablue                | 3.14 ms                                                               | 3.15 ms: 1.01x slower                                                   |
| hexiom                   | 6.85 ms                                                               | 6.88 ms: 1.01x slower                                                   |
| asyncio_websockets       | 555 ms                                                                | 558 ms: 1.01x slower                                                    |
| xml_etree_iterparse      | 98.3 ms                                                               | 99.1 ms: 1.01x slower                                                   |
| logging_format           | 6.06 us                                                               | 6.11 us: 1.01x slower                                                   |
| meteor_contest           | 105 ms                                                                | 106 ms: 1.01x slower                                                    |
| logging_silent           | 98.3 ns                                                               | 99.3 ns: 1.01x slower                                                   |
| pidigits                 | 186 ms                                                                | 188 ms: 1.01x slower                                                    |
| genshi_text              | 24.5 ms                                                               | 24.9 ms: 1.01x slower                                                   |
| tornado_http             | 94.0 ms                                                               | 95.3 ms: 1.01x slower                                                   |
| go                       | 146 ms                                                                | 149 ms: 1.02x slower                                                    |
| asyncio_tcp              | 504 ms                                                                | 515 ms: 1.02x slower                                                    |
| 2to3                     | 276 ms                                                                | 282 ms: 1.02x slower                                                    |
| genshi_xml               | 55.6 ms                                                               | 56.8 ms: 1.02x slower                                                   |
| mako                     | 9.69 ms                                                               | 9.91 ms: 1.02x slower                                                   |
| sympy_expand             | 506 ms                                                                | 519 ms: 1.02x slower                                                    |
| scimark_monte_carlo      | 63.0 ms                                                               | 64.6 ms: 1.03x slower                                                   |
| tomli_loads              | 1.92 sec                                                              | 1.97 sec: 1.03x slower                                                  |
| django_template          | 34.9 ms                                                               | 35.8 ms: 1.03x slower                                                   |
| pycparser                | 1.19 sec                                                              | 1.22 sec: 1.03x slower                                                  |
| deepcopy                 | 258 us                                                                | 268 us: 1.04x slower                                                    |
| pyflate                  | 434 ms                                                                | 453 ms: 1.04x slower                                                    |
| html5lib                 | 66.7 ms                                                               | 69.6 ms: 1.04x slower                                                   |
| deepcopy_reduce          | 2.63 us                                                               | 2.75 us: 1.05x slower                                                   |
| mdp                      | 2.54 sec                                                              | 2.67 sec: 1.05x slower                                                  |
| sqlglot_optimize         | 57.2 ms                                                               | 60.3 ms: 1.05x slower                                                   |
| regex_compile            | 138 ms                                                                | 146 ms: 1.06x slower                                                    |
| sympy_integrate          | 23.0 ms                                                               | 24.4 ms: 1.06x slower                                                   |
| sqlglot_normalize        | 112 ms                                                                | 120 ms: 1.07x slower                                                    |
| sympy_str                | 300 ms                                                                | 323 ms: 1.08x slower                                                    |
| pylint                   | 370 ms                                                                | 404 ms: 1.09x slower                                                    |
| docutils                 | 3.01 sec                                                              | 3.30 sec: 1.10x slower                                                  |
| sympy_sum                | 174 ms                                                                | 191 ms: 1.10x slower                                                    |
| sqlglot_transpile        | 1.65 ms                                                               | 1.84 ms: 1.11x slower                                                   |
| chaos                    | 58.4 ms                                                               | 65.3 ms: 1.12x slower                                                   |
| sqlglot_parse            | 1.30 ms                                                               | 1.46 ms: 1.12x slower                                                   |
| generators               | 33.5 ms                                                               | 41.3 ms: 1.23x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (27): async_tree_memoization, pprint_pformat, async_tree_cpu_io_mixed_tg, async_tree_io_tg, raytrace, async_tree_none_tg, json_loads, async_tree_io, async_tree_memoization_tg, coverage, json_dumps, async_tree_cpu_io_mixed, async_tree_none, xml_etree_process, async_generators, bench_mp_pool, regex_dna, bench_thread_pool, python_startup_no_site, scimark_sor, regex_v8, float, scimark_lu, pprint_safe_repr, logging_simple, scimark_fft, xml_etree_parse

# HPT report

- Reliability score: 93.02% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x
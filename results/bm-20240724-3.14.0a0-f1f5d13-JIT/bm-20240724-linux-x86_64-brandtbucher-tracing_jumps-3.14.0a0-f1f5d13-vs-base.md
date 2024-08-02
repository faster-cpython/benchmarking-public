# Results vs. base

- fork: brandtbucher
- ref: tracing_jumps
- machine: linux-x86_64
- commit hash: f1f5d13
- commit date: 2024-07-24
- overall geometric mean: 1.00x slower
- HPT reliability: 60.72%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 276 ms: 1.01x slower                                                 |
| html5lib       | 65.2 ms                                                               | 65.9 ms: 1.01x slower                                                |
| tornado_http   | 94.4 ms                                                               | 93.7 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization | 414 ms                                                                | 402 ms: 1.03x faster                                                 |
| async_tree_none        | 328 ms                                                                | 325 ms: 1.01x faster                                                 |
| asyncio_websockets     | 558 ms                                                                | 556 ms: 1.00x faster                                                 |
| asyncio_tcp            | 501 ms                                                                | 504 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (9): async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_none_tg, coroutines, async_generators, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 81.6 ms                                                               | 80.2 ms: 1.02x faster                                                |
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                                | 134 ms: 1.01x faster                                                 |
| regex_dna      | 228 ms                                                                | 237 ms: 1.04x slower                                                 |
| regex_effbot   | 3.73 ms                                                               | 3.97 ms: 1.06x slower                                                |
| regex_v8       | 23.8 ms                                                               | 26.4 ms: 1.11x slower                                                |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|--------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate | 81.4 ms                                                               | 79.3 ms: 1.03x faster                                                |
| xml_etree_process  | 57.0 ms                                                               | 56.2 ms: 1.02x faster                                                |
| json_dumps         | 10.3 ms                                                               | 10.2 ms: 1.01x faster                                                |
| pickle_pure_python | 297 us                                                                | 294 us: 1.01x faster                                                 |
| json_loads         | 27.7 us                                                               | 28.2 us: 1.02x slower                                                |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (4): unpickle_pure_python, tomli_loads, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                                |
| python_startup_no_site | 7.24 ms                                                               | 7.20 ms: 1.01x faster                                                |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 58.0 ms                                                               | 53.2 ms: 1.09x faster                                                |
| genshi_text     | 24.6 ms                                                               | 24.2 ms: 1.02x faster                                                |
| mako            | 9.78 ms                                                               | 9.68 ms: 1.01x faster                                                |
| django_template | 35.9 ms                                                               | 36.2 ms: 1.01x slower                                                |
| Geometric mean  | (ref)                                                                 | 1.03x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20240724-linux-x86_64-python-9ac606080a0074cdf758-3.14.0a0-9ac6060 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml               | 58.0 ms                                                               | 53.2 ms: 1.09x faster                                                |
| gc_traversal             | 3.86 ms                                                               | 3.62 ms: 1.06x faster                                                |
| mdp                      | 2.66 sec                                                              | 2.54 sec: 1.04x faster                                               |
| nqueens                  | 87.0 ms                                                               | 83.6 ms: 1.04x faster                                                |
| async_tree_memoization   | 414 ms                                                                | 402 ms: 1.03x faster                                                 |
| pyflate                  | 436 ms                                                                | 424 ms: 1.03x faster                                                 |
| xml_etree_generate       | 81.4 ms                                                               | 79.3 ms: 1.03x faster                                                |
| comprehensions           | 16.5 us                                                               | 16.1 us: 1.02x faster                                                |
| deepcopy_reduce          | 2.80 us                                                               | 2.75 us: 1.02x faster                                                |
| nbody                    | 81.6 ms                                                               | 80.2 ms: 1.02x faster                                                |
| genshi_text              | 24.6 ms                                                               | 24.2 ms: 1.02x faster                                                |
| json                     | 5.17 ms                                                               | 5.09 ms: 1.02x faster                                                |
| xml_etree_process        | 57.0 ms                                                               | 56.2 ms: 1.02x faster                                                |
| regex_compile            | 136 ms                                                                | 134 ms: 1.01x faster                                                 |
| mako                     | 9.78 ms                                                               | 9.68 ms: 1.01x faster                                                |
| coverage                 | 92.4 ms                                                               | 91.5 ms: 1.01x faster                                                |
| async_tree_none          | 328 ms                                                                | 325 ms: 1.01x faster                                                 |
| json_dumps               | 10.3 ms                                                               | 10.2 ms: 1.01x faster                                                |
| meteor_contest           | 106 ms                                                                | 105 ms: 1.01x faster                                                 |
| sympy_sum                | 170 ms                                                                | 169 ms: 1.01x faster                                                 |
| tornado_http             | 94.4 ms                                                               | 93.7 ms: 1.01x faster                                                |
| python_startup           | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                                |
| pickle_pure_python       | 297 us                                                                | 294 us: 1.01x faster                                                 |
| typing_runtime_protocols | 169 us                                                                | 168 us: 1.01x faster                                                 |
| python_startup_no_site   | 7.24 ms                                                               | 7.20 ms: 1.01x faster                                                |
| bench_thread_pool        | 822 us                                                                | 818 us: 1.01x faster                                                 |
| bpe_tokeniser            | 4.53 sec                                                              | 4.50 sec: 1.01x faster                                               |
| create_gc_cycles         | 1.77 ms                                                               | 1.76 ms: 1.01x faster                                                |
| asyncio_websockets       | 558 ms                                                                | 556 ms: 1.00x faster                                                 |
| pidigits                 | 185 ms                                                                | 186 ms: 1.00x slower                                                 |
| logging_silent           | 103 ns                                                                | 103 ns: 1.00x slower                                                 |
| asyncio_tcp              | 501 ms                                                                | 504 ms: 1.01x slower                                                 |
| sympy_integrate          | 22.2 ms                                                               | 22.4 ms: 1.01x slower                                                |
| sympy_expand             | 501 ms                                                                | 504 ms: 1.01x slower                                                 |
| go                       | 145 ms                                                                | 146 ms: 1.01x slower                                                 |
| pathlib                  | 16.0 ms                                                               | 16.1 ms: 1.01x slower                                                |
| richards                 | 40.1 ms                                                               | 40.5 ms: 1.01x slower                                                |
| crypto_pyaes             | 66.8 ms                                                               | 67.4 ms: 1.01x slower                                                |
| html5lib                 | 65.2 ms                                                               | 65.9 ms: 1.01x slower                                                |
| sqlglot_normalize        | 112 ms                                                                | 113 ms: 1.01x slower                                                 |
| django_template          | 35.9 ms                                                               | 36.2 ms: 1.01x slower                                                |
| fannkuch                 | 369 ms                                                                | 373 ms: 1.01x slower                                                 |
| sqlglot_parse            | 1.28 ms                                                               | 1.30 ms: 1.01x slower                                                |
| 2to3                     | 272 ms                                                                | 276 ms: 1.01x slower                                                 |
| deepcopy_memo            | 28.2 us                                                               | 28.6 us: 1.01x slower                                                |
| sqlglot_transpile        | 1.61 ms                                                               | 1.63 ms: 1.01x slower                                                |
| deltablue                | 3.51 ms                                                               | 3.56 ms: 1.01x slower                                                |
| logging_simple           | 5.56 us                                                               | 5.64 us: 1.01x slower                                                |
| deepcopy                 | 269 us                                                                | 273 us: 1.01x slower                                                 |
| scimark_fft              | 307 ms                                                                | 312 ms: 1.01x slower                                                 |
| json_loads               | 27.7 us                                                               | 28.2 us: 1.02x slower                                                |
| richards_super           | 45.9 ms                                                               | 46.8 ms: 1.02x slower                                                |
| scimark_sparse_mat_mult  | 4.34 ms                                                               | 4.44 ms: 1.02x slower                                                |
| pprint_safe_repr         | 717 ms                                                                | 734 ms: 1.02x slower                                                 |
| spectral_norm            | 101 ms                                                                | 104 ms: 1.03x slower                                                 |
| hexiom                   | 6.52 ms                                                               | 6.74 ms: 1.03x slower                                                |
| scimark_sor              | 125 ms                                                                | 130 ms: 1.03x slower                                                 |
| pprint_pformat           | 1.46 sec                                                              | 1.51 sec: 1.04x slower                                               |
| regex_dna                | 228 ms                                                                | 237 ms: 1.04x slower                                                 |
| pycparser                | 1.12 sec                                                              | 1.17 sec: 1.05x slower                                               |
| regex_effbot             | 3.73 ms                                                               | 3.97 ms: 1.06x slower                                                |
| regex_v8                 | 23.8 ms                                                               | 26.4 ms: 1.11x slower                                                |
| generators               | 28.9 ms                                                               | 32.8 ms: 1.13x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (28): dask, async_tree_io_tg, unpickle_pure_python, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, chaos, async_tree_io, async_tree_none_tg, telco, coroutines, async_generators, thrift, sympy_str, sqlglot_optimize, logging_format, bench_mp_pool, float, docutils, asyncio_tcp_ssl, raytrace, tomli_loads, scimark_lu, dulwich_log, xml_etree_iterparse, scimark_monte_carlo, pylint, xml_etree_parse

# HPT report

- Reliability score: 60.72% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x
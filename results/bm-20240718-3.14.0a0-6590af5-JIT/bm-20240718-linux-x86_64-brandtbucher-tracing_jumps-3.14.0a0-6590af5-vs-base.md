# Results vs. base

- fork: brandtbucher
- ref: tracing_jumps
- machine: linux-x86_64
- commit hash: 6590af5
- commit date: 2024-07-18
- overall geometric mean: 1.00x faster
- HPT reliability: 98.33%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240718-linux-x86_64-python-7b36b67b1e585c541b41-3.14.0a0-7b36b67 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 275 ms: 1.01x slower                                                 |
| docutils       | 2.90 sec                                                              | 2.88 sec: 1.01x faster                                               |
| html5lib       | 63.5 ms                                                               | 65.9 ms: 1.04x slower                                                |
| tornado_http   | 94.9 ms                                                               | 92.5 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240718-linux-x86_64-python-7b36b67b1e585c541b41-3.14.0a0-7b36b67 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                 |
| nbody          | 81.0 ms                                                               | 82.4 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240718-linux-x86_64-python-7b36b67b1e585c541b41-3.14.0a0-7b36b67 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 133 ms                                                                | 132 ms: 1.01x faster                                                 |
| regex_dna      | 225 ms                                                                | 228 ms: 1.02x slower                                                 |
| regex_v8       | 24.8 ms                                                               | 25.4 ms: 1.02x slower                                                |
| regex_effbot   | 3.79 ms                                                               | 3.87 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240718-linux-x86_64-python-7b36b67b1e585c541b41-3.14.0a0-7b36b67 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 1.94 sec                                                              | 1.91 sec: 1.02x faster                                               |
| unpickle_pure_python | 217 us                                                                | 215 us: 1.01x faster                                                 |
| xml_etree_generate   | 80.7 ms                                                               | 79.9 ms: 1.01x faster                                                |
| json_loads           | 27.6 us                                                               | 27.4 us: 1.01x faster                                                |
| xml_etree_process    | 57.2 ms                                                               | 56.8 ms: 1.01x faster                                                |
| xml_etree_iterparse  | 99.1 ms                                                               | 98.9 ms: 1.00x faster                                                |
| json_dumps           | 10.2 ms                                                               | 10.4 ms: 1.02x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240718-linux-x86_64-python-7b36b67b1e585c541b41-3.14.0a0-7b36b67 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.01x faster                                                |
| python_startup_no_site | 7.20 ms                                                               | 7.17 ms: 1.00x faster                                                |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240718-linux-x86_64-python-7b36b67b1e585c541b41-3.14.0a0-7b36b67 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml     | 57.2 ms                                                               | 53.5 ms: 1.07x faster                                                |
| genshi_text    | 25.0 ms                                                               | 24.0 ms: 1.04x faster                                                |
| mako           | 9.91 ms                                                               | 9.65 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                         |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240718-linux-x86_64-python-7b36b67b1e585c541b41-3.14.0a0-7b36b67 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml               | 57.2 ms                                                               | 53.5 ms: 1.07x faster                                                |
| genshi_text              | 25.0 ms                                                               | 24.0 ms: 1.04x faster                                                |
| logging_format           | 6.25 us                                                               | 6.03 us: 1.04x faster                                                |
| pycparser                | 1.21 sec                                                              | 1.17 sec: 1.03x faster                                               |
| mako                     | 9.91 ms                                                               | 9.65 ms: 1.03x faster                                                |
| tornado_http             | 94.9 ms                                                               | 92.5 ms: 1.03x faster                                                |
| scimark_sor              | 132 ms                                                                | 129 ms: 1.02x faster                                                 |
| dulwich_log              | 69.3 ms                                                               | 67.8 ms: 1.02x faster                                                |
| tomli_loads              | 1.94 sec                                                              | 1.91 sec: 1.02x faster                                               |
| gc_traversal             | 3.77 ms                                                               | 3.71 ms: 1.02x faster                                                |
| logging_simple           | 5.57 us                                                               | 5.48 us: 1.02x faster                                                |
| sqlglot_optimize         | 56.1 ms                                                               | 55.3 ms: 1.02x faster                                                |
| go                       | 146 ms                                                                | 144 ms: 1.02x faster                                                 |
| pyflate                  | 427 ms                                                                | 421 ms: 1.01x faster                                                 |
| sympy_sum                | 172 ms                                                                | 169 ms: 1.01x faster                                                 |
| sympy_expand             | 508 ms                                                                | 501 ms: 1.01x faster                                                 |
| sympy_str                | 301 ms                                                                | 297 ms: 1.01x faster                                                 |
| nqueens                  | 84.9 ms                                                               | 83.8 ms: 1.01x faster                                                |
| bench_thread_pool        | 837 us                                                                | 826 us: 1.01x faster                                                 |
| deepcopy_reduce          | 2.78 us                                                               | 2.74 us: 1.01x faster                                                |
| deltablue                | 3.61 ms                                                               | 3.57 ms: 1.01x faster                                                |
| scimark_monte_carlo      | 61.0 ms                                                               | 60.4 ms: 1.01x faster                                                |
| unpickle_pure_python     | 217 us                                                                | 215 us: 1.01x faster                                                 |
| regex_compile            | 133 ms                                                                | 132 ms: 1.01x faster                                                 |
| xml_etree_generate       | 80.7 ms                                                               | 79.9 ms: 1.01x faster                                                |
| json_loads               | 27.6 us                                                               | 27.4 us: 1.01x faster                                                |
| pathlib                  | 16.1 ms                                                               | 16.0 ms: 1.01x faster                                                |
| xml_etree_process        | 57.2 ms                                                               | 56.8 ms: 1.01x faster                                                |
| docutils                 | 2.90 sec                                                              | 2.88 sec: 1.01x faster                                               |
| fannkuch                 | 360 ms                                                                | 358 ms: 1.01x faster                                                 |
| create_gc_cycles         | 1.76 ms                                                               | 1.75 ms: 1.01x faster                                                |
| meteor_contest           | 105 ms                                                                | 104 ms: 1.01x faster                                                 |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.01x faster                                                |
| async_generators         | 454 ms                                                                | 451 ms: 1.01x faster                                                 |
| python_startup_no_site   | 7.20 ms                                                               | 7.17 ms: 1.00x faster                                                |
| xml_etree_iterparse      | 99.1 ms                                                               | 98.9 ms: 1.00x faster                                                |
| bpe_tokeniser            | 4.56 sec                                                              | 4.57 sec: 1.00x slower                                               |
| pidigits                 | 185 ms                                                                | 186 ms: 1.00x slower                                                 |
| asyncio_websockets       | 555 ms                                                                | 558 ms: 1.00x slower                                                 |
| scimark_fft              | 314 ms                                                                | 316 ms: 1.01x slower                                                 |
| thrift                   | 797 us                                                                | 803 us: 1.01x slower                                                 |
| 2to3                     | 272 ms                                                                | 275 ms: 1.01x slower                                                 |
| scimark_lu               | 123 ms                                                                | 125 ms: 1.01x slower                                                 |
| logging_silent           | 105 ns                                                                | 106 ns: 1.01x slower                                                 |
| deepcopy_memo            | 28.8 us                                                               | 29.2 us: 1.01x slower                                                |
| pprint_pformat           | 1.47 sec                                                              | 1.49 sec: 1.02x slower                                               |
| regex_dna                | 225 ms                                                                | 228 ms: 1.02x slower                                                 |
| nbody                    | 81.0 ms                                                               | 82.4 ms: 1.02x slower                                                |
| spectral_norm            | 101 ms                                                                | 102 ms: 1.02x slower                                                 |
| typing_runtime_protocols | 168 us                                                                | 171 us: 1.02x slower                                                 |
| json_dumps               | 10.2 ms                                                               | 10.4 ms: 1.02x slower                                                |
| mdp                      | 2.56 sec                                                              | 2.61 sec: 1.02x slower                                               |
| hexiom                   | 6.53 ms                                                               | 6.67 ms: 1.02x slower                                                |
| regex_v8                 | 24.8 ms                                                               | 25.4 ms: 1.02x slower                                                |
| regex_effbot             | 3.79 ms                                                               | 3.87 ms: 1.02x slower                                                |
| html5lib                 | 63.5 ms                                                               | 65.9 ms: 1.04x slower                                                |
| scimark_sparse_mat_mult  | 4.19 ms                                                               | 4.35 ms: 1.04x slower                                                |
| generators               | 28.7 ms                                                               | 33.0 ms: 1.15x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (33): async_tree_memoization, crypto_pyaes, async_tree_cpu_io_mixed, xml_etree_parse, dask, async_tree_none_tg, comprehensions, coroutines, float, django_template, async_tree_cpu_io_mixed_tg, coverage, sqlglot_normalize, raytrace, bench_mp_pool, sympy_integrate, asyncio_tcp, async_tree_memoization_tg, sqlglot_transpile, asyncio_tcp_ssl, deepcopy, richards_super, json, async_tree_none, chaos, sqlglot_parse, pprint_safe_repr, pickle_pure_python, richards, async_tree_io_tg, telco, pylint, async_tree_io

# HPT report

- Reliability score: 98.33% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x
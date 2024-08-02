# Results vs. base

- fork: Fidget-Spinner
- ref: macro_ify
- machine: windows-amd64
- commit hash: 2302696
- commit date: 2024-07-02
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 223 ms                                                                     | 216 ms: 1.03x faster                                                      |
| docutils       | 1.68 sec                                                                   | 1.63 sec: 1.03x faster                                                    |
| html5lib       | 38.4 ms                                                                    | 36.1 ms: 1.06x faster                                                     |
| tornado_http   | 81.5 ms                                                                    | 80.2 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                      | 1.04x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 213 ms                                                                     | 201 ms: 1.06x faster                                                      |
| async_tree_none_tg         | 191 ms                                                                     | 183 ms: 1.04x faster                                                      |
| async_tree_memoization     | 255 ms                                                                     | 245 ms: 1.04x faster                                                      |
| async_tree_io              | 539 ms                                                                     | 517 ms: 1.04x faster                                                      |
| async_tree_cpu_io_mixed_tg | 385 ms                                                                     | 375 ms: 1.03x faster                                                      |
| Geometric mean             | (ref)                                                                      | 1.03x faster                                                              |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 79.9 ms                                                                    | 73.2 ms: 1.09x faster                                                     |
| float          | 56.3 ms                                                                    | 52.5 ms: 1.07x faster                                                     |
| pidigits       | 150 ms                                                                     | 149 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                                    | 14.7 ms: 1.18x faster                                                     |
| regex_compile  | 85.4 ms                                                                    | 79.4 ms: 1.08x faster                                                     |
| regex_dna      | 122 ms                                                                     | 118 ms: 1.03x faster                                                      |
| regex_effbot   | 1.61 ms                                                                    | 1.59 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                      | 1.07x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 150 us                                                                     | 131 us: 1.14x faster                                                      |
| pickle_pure_python   | 205 us                                                                     | 185 us: 1.11x faster                                                      |
| xml_etree_process    | 40.6 ms                                                                    | 38.1 ms: 1.07x faster                                                     |
| tomli_loads          | 1.55 sec                                                                   | 1.46 sec: 1.06x faster                                                    |
| xml_etree_iterparse  | 65.9 ms                                                                    | 62.6 ms: 1.05x faster                                                     |
| xml_etree_generate   | 57.9 ms                                                                    | 55.4 ms: 1.05x faster                                                     |
| json_dumps           | 5.99 ms                                                                    | 5.75 ms: 1.04x faster                                                     |
| xml_etree_parse      | 93.9 ms                                                                    | 93.2 ms: 1.01x faster                                                     |
| Geometric mean       | (ref)                                                                      | 1.06x faster                                                              |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|-----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.64 ms                                                                    | 6.78 ms: 1.13x faster                                                     |
| genshi_xml      | 35.9 ms                                                                    | 32.7 ms: 1.10x faster                                                     |
| django_template | 24.2 ms                                                                    | 22.5 ms: 1.08x faster                                                     |
| genshi_text     | 16.4 ms                                                                    | 15.3 ms: 1.08x faster                                                     |
| Geometric mean  | (ref)                                                                      | 1.09x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8                   | 17.3 ms                                                                    | 14.7 ms: 1.18x faster                                                     |
| unpickle_pure_python       | 150 us                                                                     | 131 us: 1.14x faster                                                      |
| comprehensions             | 11.9 us                                                                    | 10.5 us: 1.13x faster                                                     |
| deepcopy_memo              | 20.8 us                                                                    | 18.4 us: 1.13x faster                                                     |
| mako                       | 7.64 ms                                                                    | 6.78 ms: 1.13x faster                                                     |
| scimark_lu                 | 63.8 ms                                                                    | 57.0 ms: 1.12x faster                                                     |
| logging_silent             | 64.7 ns                                                                    | 57.9 ns: 1.12x faster                                                     |
| coroutines                 | 14.9 ms                                                                    | 13.4 ms: 1.12x faster                                                     |
| scimark_monte_carlo        | 48.1 ms                                                                    | 43.3 ms: 1.11x faster                                                     |
| scimark_sparse_mat_mult    | 2.99 ms                                                                    | 2.69 ms: 1.11x faster                                                     |
| pickle_pure_python         | 205 us                                                                     | 185 us: 1.11x faster                                                      |
| sqlglot_parse              | 889 us                                                                     | 808 us: 1.10x faster                                                      |
| typing_runtime_protocols   | 112 us                                                                     | 101 us: 1.10x faster                                                      |
| genshi_xml                 | 35.9 ms                                                                    | 32.7 ms: 1.10x faster                                                     |
| richards_super             | 33.4 ms                                                                    | 30.5 ms: 1.10x faster                                                     |
| richards                   | 29.7 ms                                                                    | 27.2 ms: 1.09x faster                                                     |
| crypto_pyaes               | 51.2 ms                                                                    | 46.9 ms: 1.09x faster                                                     |
| nbody                      | 79.9 ms                                                                    | 73.2 ms: 1.09x faster                                                     |
| chaos                      | 43.2 ms                                                                    | 39.6 ms: 1.09x faster                                                     |
| scimark_fft                | 211 ms                                                                     | 194 ms: 1.09x faster                                                      |
| sqlglot_transpile          | 1.10 ms                                                                    | 1.02 ms: 1.08x faster                                                     |
| go                         | 92.9 ms                                                                    | 86.0 ms: 1.08x faster                                                     |
| raytrace                   | 182 ms                                                                     | 168 ms: 1.08x faster                                                      |
| hexiom                     | 4.29 ms                                                                    | 3.97 ms: 1.08x faster                                                     |
| django_template            | 24.2 ms                                                                    | 22.5 ms: 1.08x faster                                                     |
| regex_compile              | 85.4 ms                                                                    | 79.4 ms: 1.08x faster                                                     |
| genshi_text                | 16.4 ms                                                                    | 15.3 ms: 1.08x faster                                                     |
| deepcopy_reduce            | 1.89 us                                                                    | 1.76 us: 1.07x faster                                                     |
| generators                 | 22.6 ms                                                                    | 21.0 ms: 1.07x faster                                                     |
| float                      | 56.3 ms                                                                    | 52.5 ms: 1.07x faster                                                     |
| pprint_safe_repr           | 535 ms                                                                     | 499 ms: 1.07x faster                                                      |
| deltablue                  | 2.17 ms                                                                    | 2.02 ms: 1.07x faster                                                     |
| telco                      | 4.97 ms                                                                    | 4.64 ms: 1.07x faster                                                     |
| pprint_pformat             | 1.09 sec                                                                   | 1.02 sec: 1.07x faster                                                    |
| spectral_norm              | 67.6 ms                                                                    | 63.2 ms: 1.07x faster                                                     |
| nqueens                    | 62.7 ms                                                                    | 58.7 ms: 1.07x faster                                                     |
| xml_etree_process          | 40.6 ms                                                                    | 38.1 ms: 1.07x faster                                                     |
| html5lib                   | 38.4 ms                                                                    | 36.1 ms: 1.06x faster                                                     |
| tomli_loads                | 1.55 sec                                                                   | 1.46 sec: 1.06x faster                                                    |
| async_tree_none            | 213 ms                                                                     | 201 ms: 1.06x faster                                                      |
| deepcopy                   | 183 us                                                                     | 173 us: 1.06x faster                                                      |
| meteor_contest             | 78.3 ms                                                                    | 74.0 ms: 1.06x faster                                                     |
| pyflate                    | 311 ms                                                                     | 295 ms: 1.05x faster                                                      |
| xml_etree_iterparse        | 65.9 ms                                                                    | 62.6 ms: 1.05x faster                                                     |
| async_generators           | 243 ms                                                                     | 231 ms: 1.05x faster                                                      |
| sympy_str                  | 172 ms                                                                     | 163 ms: 1.05x faster                                                      |
| sympy_expand               | 293 ms                                                                     | 279 ms: 1.05x faster                                                      |
| logging_simple             | 6.26 us                                                                    | 5.96 us: 1.05x faster                                                     |
| xml_etree_generate         | 57.9 ms                                                                    | 55.4 ms: 1.05x faster                                                     |
| async_tree_none_tg         | 191 ms                                                                     | 183 ms: 1.04x faster                                                      |
| sqlglot_optimize           | 34.9 ms                                                                    | 33.4 ms: 1.04x faster                                                     |
| scimark_sor                | 83.9 ms                                                                    | 80.4 ms: 1.04x faster                                                     |
| sqlglot_normalize          | 185 ms                                                                     | 178 ms: 1.04x faster                                                      |
| logging_format             | 6.70 us                                                                    | 6.43 us: 1.04x faster                                                     |
| async_tree_memoization     | 255 ms                                                                     | 245 ms: 1.04x faster                                                      |
| async_tree_io              | 539 ms                                                                     | 517 ms: 1.04x faster                                                      |
| json_dumps                 | 5.99 ms                                                                    | 5.75 ms: 1.04x faster                                                     |
| docutils                   | 1.68 sec                                                                   | 1.63 sec: 1.03x faster                                                    |
| 2to3                       | 223 ms                                                                     | 216 ms: 1.03x faster                                                      |
| thrift                     | 527 us                                                                     | 510 us: 1.03x faster                                                      |
| sympy_integrate            | 13.0 ms                                                                    | 12.5 ms: 1.03x faster                                                     |
| regex_dna                  | 122 ms                                                                     | 118 ms: 1.03x faster                                                      |
| fannkuch                   | 285 ms                                                                     | 277 ms: 1.03x faster                                                      |
| sympy_sum                  | 88.1 ms                                                                    | 85.6 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed_tg | 385 ms                                                                     | 375 ms: 1.03x faster                                                      |
| bench_thread_pool          | 767 us                                                                     | 748 us: 1.02x faster                                                      |
| tornado_http               | 81.5 ms                                                                    | 80.2 ms: 1.02x faster                                                     |
| regex_effbot               | 1.61 ms                                                                    | 1.59 ms: 1.01x faster                                                     |
| create_gc_cycles           | 892 us                                                                     | 883 us: 1.01x faster                                                      |
| bench_mp_pool              | 66.1 ms                                                                    | 65.4 ms: 1.01x faster                                                     |
| pathlib                    | 76.0 ms                                                                    | 75.4 ms: 1.01x faster                                                     |
| pidigits                   | 150 ms                                                                     | 149 ms: 1.01x faster                                                      |
| xml_etree_parse            | 93.9 ms                                                                    | 93.2 ms: 1.01x faster                                                     |
| mdp                        | 1.37 sec                                                                   | 1.43 sec: 1.04x slower                                                    |
| json                       | 2.98 ms                                                                    | 3.17 ms: 1.07x slower                                                     |
| pycparser                  | 759 ms                                                                     | 819 ms: 1.08x slower                                                      |
| Geometric mean             | (ref)                                                                      | 1.05x faster                                                              |

Benchmark hidden because not significant (11): pylint, async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed, python_startup, json_loads, coverage, gc_traversal, python_startup_no_site, asyncio_tcp, asyncio_tcp_ssl

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown
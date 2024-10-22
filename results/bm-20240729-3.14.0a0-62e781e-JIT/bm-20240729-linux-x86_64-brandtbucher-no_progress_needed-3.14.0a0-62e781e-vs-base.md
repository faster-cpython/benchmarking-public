# Results vs. base

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 62e781e
- commit date: 2024-07-29
- overall geometric mean: 1.00x slower
- HPT reliability: 97.83%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 273 ms                                                                | 282 ms: 1.03x slower                                                      |
| docutils       | 2.91 sec                                                              | 2.99 sec: 1.03x slower                                                    |
| html5lib       | 66.2 ms                                                               | 67.3 ms: 1.02x slower                                                     |
| tornado_http   | 92.3 ms                                                               | 92.8 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none        | 327 ms                                                                | 325 ms: 1.01x faster                                                      |
| asyncio_tcp_ssl        | 1.81 sec                                                              | 1.81 sec: 1.00x slower                                                    |
| asyncio_tcp            | 505 ms                                                                | 506 ms: 1.00x slower                                                      |
| async_generators       | 453 ms                                                                | 458 ms: 1.01x slower                                                      |
| async_tree_memoization | 418 ms                                                                | 427 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (8): async_tree_none_tg, coroutines, async_tree_io_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 71.0 ms                                                               | 70.5 ms: 1.01x faster                                                     |
| pidigits       | 186 ms                                                                | 186 ms: 1.00x slower                                                      |
| nbody          | 79.7 ms                                                               | 80.0 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.81 ms                                                               | 3.79 ms: 1.00x faster                                                     |
| regex_dna      | 226 ms                                                                | 229 ms: 1.01x slower                                                      |
| regex_v8       | 24.5 ms                                                               | 25.5 ms: 1.04x slower                                                     |
| regex_compile  | 134 ms                                                                | 143 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse    | 149 ms                                                                | 146 ms: 1.02x faster                                                      |
| tomli_loads        | 1.92 sec                                                              | 1.91 sec: 1.01x faster                                                    |
| pickle_pure_python | 299 us                                                                | 303 us: 1.01x slower                                                      |
| json_dumps         | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                                     |
| json_loads         | 27.7 us                                                               | 28.3 us: 1.02x slower                                                     |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_iterparse, unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                     |
| python_startup_no_site | 7.11 ms                                                               | 7.11 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 53.8 ms                                                               | 52.8 ms: 1.02x faster                                                     |
| django_template | 36.1 ms                                                               | 35.6 ms: 1.02x faster                                                     |
| mako            | 9.81 ms                                                               | 9.77 ms: 1.00x faster                                                     |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182 | bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deltablue                | 3.52 ms                                                               | 3.02 ms: 1.16x faster                                                     |
| deepcopy_memo            | 29.0 us                                                               | 26.9 us: 1.08x faster                                                     |
| logging_silent           | 104 ns                                                                | 98.4 ns: 1.06x faster                                                     |
| scimark_lu               | 124 ms                                                                | 118 ms: 1.05x faster                                                      |
| scimark_sor              | 129 ms                                                                | 123 ms: 1.05x faster                                                      |
| scimark_sparse_mat_mult  | 4.40 ms                                                               | 4.27 ms: 1.03x faster                                                     |
| spectral_norm            | 105 ms                                                                | 102 ms: 1.02x faster                                                      |
| deepcopy                 | 274 us                                                                | 268 us: 1.02x faster                                                      |
| crypto_pyaes             | 67.3 ms                                                               | 65.9 ms: 1.02x faster                                                     |
| xml_etree_parse          | 149 ms                                                                | 146 ms: 1.02x faster                                                      |
| typing_runtime_protocols | 170 us                                                                | 167 us: 1.02x faster                                                      |
| logging_format           | 6.07 us                                                               | 5.96 us: 1.02x faster                                                     |
| genshi_xml               | 53.8 ms                                                               | 52.8 ms: 1.02x faster                                                     |
| scimark_fft              | 309 ms                                                                | 304 ms: 1.02x faster                                                      |
| django_template          | 36.1 ms                                                               | 35.6 ms: 1.02x faster                                                     |
| coverage                 | 91.7 ms                                                               | 90.4 ms: 1.01x faster                                                     |
| thrift                   | 797 us                                                                | 787 us: 1.01x faster                                                      |
| json                     | 5.19 ms                                                               | 5.13 ms: 1.01x faster                                                     |
| logging_simple           | 5.47 us                                                               | 5.43 us: 1.01x faster                                                     |
| async_tree_none          | 327 ms                                                                | 325 ms: 1.01x faster                                                      |
| tomli_loads              | 1.92 sec                                                              | 1.91 sec: 1.01x faster                                                    |
| float                    | 71.0 ms                                                               | 70.5 ms: 1.01x faster                                                     |
| pathlib                  | 16.1 ms                                                               | 16.0 ms: 1.01x faster                                                     |
| regex_effbot             | 3.81 ms                                                               | 3.79 ms: 1.00x faster                                                     |
| mako                     | 9.81 ms                                                               | 9.77 ms: 1.00x faster                                                     |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                     |
| python_startup_no_site   | 7.11 ms                                                               | 7.11 ms: 1.00x slower                                                     |
| pidigits                 | 186 ms                                                                | 186 ms: 1.00x slower                                                      |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.81 sec: 1.00x slower                                                    |
| bpe_tokeniser            | 4.52 sec                                                              | 4.53 sec: 1.00x slower                                                    |
| nbody                    | 79.7 ms                                                               | 80.0 ms: 1.00x slower                                                     |
| asyncio_tcp              | 505 ms                                                                | 506 ms: 1.00x slower                                                      |
| generators               | 32.7 ms                                                               | 32.8 ms: 1.00x slower                                                     |
| bench_thread_pool        | 815 us                                                                | 818 us: 1.00x slower                                                      |
| tornado_http             | 92.3 ms                                                               | 92.8 ms: 1.00x slower                                                     |
| go                       | 145 ms                                                                | 146 ms: 1.01x slower                                                      |
| sympy_expand             | 507 ms                                                                | 511 ms: 1.01x slower                                                      |
| regex_dna                | 226 ms                                                                | 229 ms: 1.01x slower                                                      |
| async_generators         | 453 ms                                                                | 458 ms: 1.01x slower                                                      |
| gc_traversal             | 3.52 ms                                                               | 3.56 ms: 1.01x slower                                                     |
| pprint_pformat           | 1.49 sec                                                              | 1.51 sec: 1.01x slower                                                    |
| pickle_pure_python       | 299 us                                                                | 303 us: 1.01x slower                                                      |
| json_dumps               | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                                     |
| html5lib                 | 66.2 ms                                                               | 67.3 ms: 1.02x slower                                                     |
| meteor_contest           | 105 ms                                                                | 106 ms: 1.02x slower                                                      |
| sqlglot_normalize        | 111 ms                                                                | 113 ms: 1.02x slower                                                      |
| sqlglot_parse            | 1.30 ms                                                               | 1.32 ms: 1.02x slower                                                     |
| pyflate                  | 431 ms                                                                | 440 ms: 1.02x slower                                                      |
| json_loads               | 27.7 us                                                               | 28.3 us: 1.02x slower                                                     |
| scimark_monte_carlo      | 60.9 ms                                                               | 62.3 ms: 1.02x slower                                                     |
| async_tree_memoization   | 418 ms                                                                | 427 ms: 1.02x slower                                                      |
| sympy_str                | 298 ms                                                                | 306 ms: 1.03x slower                                                      |
| docutils                 | 2.91 sec                                                              | 2.99 sec: 1.03x slower                                                    |
| sympy_integrate          | 22.4 ms                                                               | 23.0 ms: 1.03x slower                                                     |
| 2to3                     | 273 ms                                                                | 282 ms: 1.03x slower                                                      |
| sqlglot_transpile        | 1.63 ms                                                               | 1.68 ms: 1.03x slower                                                     |
| fannkuch                 | 363 ms                                                                | 375 ms: 1.03x slower                                                      |
| sympy_sum                | 170 ms                                                                | 176 ms: 1.03x slower                                                      |
| comprehensions           | 16.1 us                                                               | 16.7 us: 1.04x slower                                                     |
| regex_v8                 | 24.5 ms                                                               | 25.5 ms: 1.04x slower                                                     |
| sqlglot_optimize         | 55.9 ms                                                               | 58.3 ms: 1.04x slower                                                     |
| richards                 | 40.5 ms                                                               | 42.3 ms: 1.04x slower                                                     |
| pycparser                | 1.16 sec                                                              | 1.22 sec: 1.05x slower                                                    |
| richards_super           | 46.4 ms                                                               | 48.7 ms: 1.05x slower                                                     |
| regex_compile            | 134 ms                                                                | 143 ms: 1.07x slower                                                      |
| hexiom                   | 6.68 ms                                                               | 7.68 ms: 1.15x slower                                                     |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (24): deepcopy_reduce, async_tree_none_tg, pprint_safe_repr, telco, coroutines, async_tree_io_tg, xml_etree_process, xml_etree_iterparse, asyncio_websockets, async_tree_cpu_io_mixed_tg, create_gc_cycles, unpickle_pure_python, async_tree_cpu_io_mixed, dask, bench_mp_pool, xml_etree_generate, async_tree_io, mdp, raytrace, chaos, async_tree_memoization_tg, genshi_text, nqueens, pylint

# HPT report

- Reliability score: 97.83% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x
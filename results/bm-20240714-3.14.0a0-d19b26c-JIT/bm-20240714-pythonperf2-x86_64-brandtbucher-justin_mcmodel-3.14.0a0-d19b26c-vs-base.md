# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.01x faster
- HPT reliability: 99.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                                      | 298 ms: 1.02x faster                                                        |
| docutils       | 3.08 sec                                                                    | 3.10 sec: 1.00x slower                                                      |
| html5lib       | 72.1 ms                                                                     | 69.1 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|---------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 387 ms                                                                      | 383 ms: 1.01x faster                                                        |
| Geometric mean            | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (7): async_tree_none, async_tree_memoization, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 75.2 ms                                                                     | 73.2 ms: 1.03x faster                                                       |
| pidigits       | 250 ms                                                                      | 251 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 138 ms                                                                      | 133 ms: 1.04x faster                                                        |
| regex_effbot   | 3.50 ms                                                                     | 3.58 ms: 1.02x slower                                                       |
| regex_v8       | 25.6 ms                                                                     | 27.1 ms: 1.06x slower                                                       |
| regex_dna      | 237 ms                                                                      | 262 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.08 sec                                                                    | 2.04 sec: 1.02x faster                                                      |
| xml_etree_process    | 58.7 ms                                                                     | 57.6 ms: 1.02x faster                                                       |
| xml_etree_generate   | 82.3 ms                                                                     | 80.9 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 99.4 ms                                                                     | 97.7 ms: 1.02x faster                                                       |
| unpickle_pure_python | 216 us                                                                      | 217 us: 1.00x slower                                                        |
| json_dumps           | 10.8 ms                                                                     | 11.0 ms: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_parse, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 9.02 ms                                                                     | 9.04 ms: 1.00x slower                                                       |
| python_startup         | 13.3 ms                                                                     | 13.4 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 65.5 ms                                                                     | 58.8 ms: 1.11x faster                                                       |
| genshi_text     | 29.1 ms                                                                     | 26.5 ms: 1.10x faster                                                       |
| django_template | 42.1 ms                                                                     | 40.8 ms: 1.03x faster                                                       |
| mako            | 9.22 ms                                                                     | 8.96 ms: 1.03x faster                                                       |
| Geometric mean  | (ref)                                                                       | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|---------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml                | 65.5 ms                                                                     | 58.8 ms: 1.11x faster                                                       |
| genshi_text               | 29.1 ms                                                                     | 26.5 ms: 1.10x faster                                                       |
| raytrace                  | 296 ms                                                                      | 275 ms: 1.07x faster                                                        |
| richards                  | 45.8 ms                                                                     | 43.0 ms: 1.06x faster                                                       |
| richards_super            | 52.7 ms                                                                     | 49.6 ms: 1.06x faster                                                       |
| gc_traversal              | 4.67 ms                                                                     | 4.43 ms: 1.05x faster                                                       |
| pycparser                 | 1.27 sec                                                                    | 1.20 sec: 1.05x faster                                                      |
| go                        | 163 ms                                                                      | 155 ms: 1.05x faster                                                        |
| html5lib                  | 72.1 ms                                                                     | 69.1 ms: 1.04x faster                                                       |
| pyflate                   | 455 ms                                                                      | 438 ms: 1.04x faster                                                        |
| coroutines                | 21.9 ms                                                                     | 21.0 ms: 1.04x faster                                                       |
| regex_compile             | 138 ms                                                                      | 133 ms: 1.04x faster                                                        |
| deltablue                 | 3.69 ms                                                                     | 3.57 ms: 1.03x faster                                                       |
| django_template           | 42.1 ms                                                                     | 40.8 ms: 1.03x faster                                                       |
| logging_simple            | 6.45 us                                                                     | 6.27 us: 1.03x faster                                                       |
| mako                      | 9.22 ms                                                                     | 8.96 ms: 1.03x faster                                                       |
| float                     | 75.2 ms                                                                     | 73.2 ms: 1.03x faster                                                       |
| logging_format            | 7.19 us                                                                     | 7.00 us: 1.03x faster                                                       |
| async_generators          | 386 ms                                                                      | 376 ms: 1.03x faster                                                        |
| create_gc_cycles          | 1.96 ms                                                                     | 1.92 ms: 1.02x faster                                                       |
| sympy_str                 | 310 ms                                                                      | 303 ms: 1.02x faster                                                        |
| 2to3                      | 305 ms                                                                      | 298 ms: 1.02x faster                                                        |
| tomli_loads               | 2.08 sec                                                                    | 2.04 sec: 1.02x faster                                                      |
| sympy_expand              | 523 ms                                                                      | 512 ms: 1.02x faster                                                        |
| xml_etree_process         | 58.7 ms                                                                     | 57.6 ms: 1.02x faster                                                       |
| deepcopy                  | 307 us                                                                      | 301 us: 1.02x faster                                                        |
| xml_etree_generate        | 82.3 ms                                                                     | 80.9 ms: 1.02x faster                                                       |
| xml_etree_iterparse       | 99.4 ms                                                                     | 97.7 ms: 1.02x faster                                                       |
| hexiom                    | 6.68 ms                                                                     | 6.57 ms: 1.02x faster                                                       |
| pprint_pformat            | 1.63 sec                                                                    | 1.60 sec: 1.02x faster                                                      |
| chaos                     | 65.1 ms                                                                     | 64.3 ms: 1.01x faster                                                       |
| spectral_norm             | 84.0 ms                                                                     | 82.9 ms: 1.01x faster                                                       |
| coverage                  | 83.8 ms                                                                     | 82.8 ms: 1.01x faster                                                       |
| sqlglot_optimize          | 62.9 ms                                                                     | 62.2 ms: 1.01x faster                                                       |
| async_tree_memoization_tg | 387 ms                                                                      | 383 ms: 1.01x faster                                                        |
| pathlib                   | 16.3 ms                                                                     | 16.1 ms: 1.01x faster                                                       |
| sqlglot_parse             | 1.40 ms                                                                     | 1.39 ms: 1.01x faster                                                       |
| thrift                    | 905 us                                                                      | 897 us: 1.01x faster                                                        |
| sqlglot_transpile         | 1.82 ms                                                                     | 1.80 ms: 1.01x faster                                                       |
| sqlglot_normalize         | 129 ms                                                                      | 128 ms: 1.01x faster                                                        |
| asyncio_websockets        | 394 ms                                                                      | 391 ms: 1.01x faster                                                        |
| dulwich_log               | 66.2 ms                                                                     | 65.9 ms: 1.01x faster                                                       |
| sympy_sum                 | 164 ms                                                                      | 164 ms: 1.00x faster                                                        |
| sympy_integrate           | 25.5 ms                                                                     | 25.4 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl           | 1.58 sec                                                                    | 1.58 sec: 1.00x faster                                                      |
| python_startup_no_site    | 9.02 ms                                                                     | 9.04 ms: 1.00x slower                                                       |
| python_startup            | 13.3 ms                                                                     | 13.4 ms: 1.00x slower                                                       |
| pidigits                  | 250 ms                                                                      | 251 ms: 1.00x slower                                                        |
| crypto_pyaes              | 69.8 ms                                                                     | 70.1 ms: 1.00x slower                                                       |
| unpickle_pure_python      | 216 us                                                                      | 217 us: 1.00x slower                                                        |
| docutils                  | 3.08 sec                                                                    | 3.10 sec: 1.00x slower                                                      |
| meteor_contest            | 129 ms                                                                      | 130 ms: 1.01x slower                                                        |
| typing_runtime_protocols  | 183 us                                                                      | 185 us: 1.01x slower                                                        |
| deepcopy_reduce           | 2.99 us                                                                     | 3.02 us: 1.01x slower                                                       |
| nqueens                   | 93.5 ms                                                                     | 94.7 ms: 1.01x slower                                                       |
| scimark_sor               | 123 ms                                                                      | 124 ms: 1.01x slower                                                        |
| bpe_tokeniser             | 5.12 sec                                                                    | 5.21 sec: 1.02x slower                                                      |
| json_dumps                | 10.8 ms                                                                     | 11.0 ms: 1.02x slower                                                       |
| json                      | 5.39 ms                                                                     | 5.50 ms: 1.02x slower                                                       |
| regex_effbot              | 3.50 ms                                                                     | 3.58 ms: 1.02x slower                                                       |
| fannkuch                  | 337 ms                                                                      | 346 ms: 1.03x slower                                                        |
| mdp                       | 2.55 sec                                                                    | 2.62 sec: 1.03x slower                                                      |
| telco                     | 8.09 ms                                                                     | 8.35 ms: 1.03x slower                                                       |
| scimark_monte_carlo       | 64.5 ms                                                                     | 66.9 ms: 1.04x slower                                                       |
| logging_silent            | 100 ns                                                                      | 105 ns: 1.04x slower                                                        |
| regex_v8                  | 25.6 ms                                                                     | 27.1 ms: 1.06x slower                                                       |
| scimark_sparse_mat_mult   | 3.97 ms                                                                     | 4.20 ms: 1.06x slower                                                       |
| scimark_fft               | 289 ms                                                                      | 306 ms: 1.06x slower                                                        |
| scimark_lu                | 114 ms                                                                      | 123 ms: 1.08x slower                                                        |
| regex_dna                 | 237 ms                                                                      | 262 ms: 1.11x slower                                                        |
| Geometric mean            | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (21): async_tree_none, async_tree_memoization, nbody, async_tree_io, async_tree_none_tg, bench_mp_pool, async_tree_cpu_io_mixed, generators, xml_etree_parse, pprint_safe_repr, async_tree_cpu_io_mixed_tg, tornado_http, json_loads, deepcopy_memo, comprehensions, asyncio_tcp, pickle_pure_python, dask, bench_thread_pool, pylint, async_tree_io_tg

# HPT report

- Reliability score: 99.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x
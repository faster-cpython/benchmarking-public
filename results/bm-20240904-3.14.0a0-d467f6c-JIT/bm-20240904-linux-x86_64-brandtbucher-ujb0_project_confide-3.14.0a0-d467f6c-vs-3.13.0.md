# Results vs. 3.13.0

- fork: brandtbucher
- ref: ujb0_project_confide
- machine: linux-x86_64
- commit hash: d467f6c
- commit date: 2024-09-04
- overall geometric mean: 1.015x slower
- HPT reliability: 80.83%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 294 ms: 1.10x slower                                                        |
| docutils       | 2.59 sec                                               | 3.52 sec: 1.36x slower                                                      |
| html5lib       | 64.2 ms                                                | 74.3 ms: 1.16x slower                                                       |
| tornado_http   | 92.4 ms                                                | 118 ms: 1.27x slower                                                        |
| Geometric mean | (ref)                                                  | 1.22x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 416 ms: 1.12x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 427 ms: 1.03x faster                                                        |
| async_tree_none           | 351 ms                                                 | 341 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 572 ms: 1.01x faster                                                        |
| asyncio_websockets        | 552 ms                                                 | 560 ms: 1.02x slower                                                        |
| async_generators          | 436 ms                                                 | 457 ms: 1.05x slower                                                        |
| coroutines                | 22.7 ms                                                | 23.8 ms: 1.05x slower                                                       |
| async_tree_io_tg          | 857 ms                                                 | 907 ms: 1.06x slower                                                        |
| async_tree_io             | 842 ms                                                 | 961 ms: 1.14x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 68.7 ms: 1.15x faster                                                       |
| nbody          | 87.0 ms                                                | 79.9 ms: 1.09x faster                                                       |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                       |
| regex_v8       | 26.2 ms                                                | 26.1 ms: 1.01x faster                                                       |
| regex_compile  | 132 ms                                                 | 152 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                 | 193 us: 1.12x faster                                                        |
| xml_etree_process    | 60.6 ms                                                | 54.7 ms: 1.11x faster                                                       |
| json_dumps           | 10.6 ms                                                | 9.72 ms: 1.09x faster                                                       |
| xml_etree_generate   | 86.7 ms                                                | 80.1 ms: 1.08x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.07x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 98.6 ms: 1.03x faster                                                       |
| json_loads           | 27.2 us                                                | 29.6 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (2): pickle_pure_python, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                       |
| python_startup_no_site | 6.96 ms                                                | 7.16 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.58 ms: 1.16x faster                                                       |
| genshi_text     | 23.5 ms                                                | 22.7 ms: 1.03x faster                                                       |
| django_template | 35.2 ms                                                | 40.5 ms: 1.15x slower                                                       |
| genshi_xml      | 50.9 ms                                                | 59.2 ms: 1.16x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 26.3 us: 1.49x faster                                                       |
| deepcopy                  | 358 us                                                 | 263 us: 1.36x faster                                                        |
| create_gc_cycles          | 2.41 ms                                                | 1.81 ms: 1.33x faster                                                       |
| deepcopy_reduce           | 3.20 us                                                | 2.69 us: 1.19x faster                                                       |
| scimark_fft               | 364 ms                                                 | 307 ms: 1.19x faster                                                        |
| richards                  | 48.7 ms                                                | 41.4 ms: 1.18x faster                                                       |
| python_startup            | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                       |
| scimark_monte_carlo       | 67.4 ms                                                | 57.9 ms: 1.17x faster                                                       |
| richards_super            | 54.9 ms                                                | 47.1 ms: 1.17x faster                                                       |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.34 ms: 1.16x faster                                                       |
| mako                      | 11.1 ms                                                | 9.58 ms: 1.16x faster                                                       |
| float                     | 79.2 ms                                                | 68.7 ms: 1.15x faster                                                       |
| gc_traversal              | 4.37 ms                                                | 3.82 ms: 1.14x faster                                                       |
| crypto_pyaes              | 75.3 ms                                                | 66.0 ms: 1.14x faster                                                       |
| spectral_norm             | 115 ms                                                 | 101 ms: 1.14x faster                                                        |
| unpickle_pure_python      | 216 us                                                 | 193 us: 1.12x faster                                                        |
| async_tree_memoization_tg | 464 ms                                                 | 416 ms: 1.12x faster                                                        |
| pathlib                   | 17.5 ms                                                | 15.8 ms: 1.11x faster                                                       |
| xml_etree_process         | 60.6 ms                                                | 54.7 ms: 1.11x faster                                                       |
| telco                     | 8.54 ms                                                | 7.82 ms: 1.09x faster                                                       |
| nbody                     | 87.0 ms                                                | 79.9 ms: 1.09x faster                                                       |
| json_dumps                | 10.6 ms                                                | 9.72 ms: 1.09x faster                                                       |
| xml_etree_generate        | 86.7 ms                                                | 80.1 ms: 1.08x faster                                                       |
| xml_etree_parse           | 156 ms                                                 | 145 ms: 1.07x faster                                                        |
| fannkuch                  | 404 ms                                                 | 380 ms: 1.07x faster                                                        |
| mdp                       | 2.72 sec                                               | 2.59 sec: 1.05x faster                                                      |
| pprint_safe_repr          | 728 ms                                                 | 695 ms: 1.05x faster                                                        |
| bpe_tokeniser             | 4.75 sec                                               | 4.53 sec: 1.05x faster                                                      |
| scimark_lu                | 113 ms                                                 | 108 ms: 1.04x faster                                                        |
| logging_silent            | 102 ns                                                 | 98.3 ns: 1.04x faster                                                       |
| genshi_text               | 23.5 ms                                                | 22.7 ms: 1.03x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 427 ms: 1.03x faster                                                        |
| scimark_sor               | 124 ms                                                 | 120 ms: 1.03x faster                                                        |
| async_tree_none           | 351 ms                                                 | 341 ms: 1.03x faster                                                        |
| xml_etree_iterparse       | 101 ms                                                 | 98.6 ms: 1.03x faster                                                       |
| pprint_pformat            | 1.49 sec                                               | 1.46 sec: 1.02x faster                                                      |
| regex_effbot              | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 572 ms: 1.01x faster                                                        |
| meteor_contest            | 109 ms                                                 | 108 ms: 1.01x faster                                                        |
| regex_v8                  | 26.2 ms                                                | 26.1 ms: 1.01x faster                                                       |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| comprehensions            | 16.5 us                                                | 16.6 us: 1.01x slower                                                       |
| asyncio_websockets        | 552 ms                                                 | 560 ms: 1.02x slower                                                        |
| pyflate                   | 471 ms                                                 | 484 ms: 1.03x slower                                                        |
| python_startup_no_site    | 6.96 ms                                                | 7.16 ms: 1.03x slower                                                       |
| logging_format            | 6.40 us                                                | 6.59 us: 1.03x slower                                                       |
| chaos                     | 58.1 ms                                                | 59.9 ms: 1.03x slower                                                       |
| bench_mp_pool             | 24.0 ms                                                | 24.9 ms: 1.04x slower                                                       |
| coverage                  | 84.0 ms                                                | 87.9 ms: 1.05x slower                                                       |
| logging_simple            | 5.72 us                                                | 6.00 us: 1.05x slower                                                       |
| async_generators          | 436 ms                                                 | 457 ms: 1.05x slower                                                        |
| coroutines                | 22.7 ms                                                | 23.8 ms: 1.05x slower                                                       |
| async_tree_io_tg          | 857 ms                                                 | 907 ms: 1.06x slower                                                        |
| raytrace                  | 267 ms                                                 | 284 ms: 1.06x slower                                                        |
| nqueens                   | 78.4 ms                                                | 84.5 ms: 1.08x slower                                                       |
| bench_thread_pool         | 822 us                                                 | 893 us: 1.09x slower                                                        |
| json_loads                | 27.2 us                                                | 29.6 us: 1.09x slower                                                       |
| deltablue                 | 3.23 ms                                                | 3.56 ms: 1.10x slower                                                       |
| 2to3                      | 267 ms                                                 | 294 ms: 1.10x slower                                                        |
| pycparser                 | 1.20 sec                                               | 1.35 sec: 1.12x slower                                                      |
| async_tree_io             | 842 ms                                                 | 961 ms: 1.14x slower                                                        |
| django_template           | 35.2 ms                                                | 40.5 ms: 1.15x slower                                                       |
| regex_compile             | 132 ms                                                 | 152 ms: 1.15x slower                                                        |
| html5lib                  | 64.2 ms                                                | 74.3 ms: 1.16x slower                                                       |
| sqlglot_normalize         | 108 ms                                                 | 125 ms: 1.16x slower                                                        |
| genshi_xml                | 50.9 ms                                                | 59.2 ms: 1.16x slower                                                       |
| generators                | 29.0 ms                                                | 34.1 ms: 1.18x slower                                                       |
| hexiom                    | 6.16 ms                                                | 7.40 ms: 1.20x slower                                                       |
| sympy_expand              | 463 ms                                                 | 559 ms: 1.21x slower                                                        |
| sympy_str                 | 275 ms                                                 | 345 ms: 1.26x slower                                                        |
| sqlglot_optimize          | 53.7 ms                                                | 67.6 ms: 1.26x slower                                                       |
| go                        | 144 ms                                                 | 181 ms: 1.26x slower                                                        |
| tornado_http              | 92.4 ms                                                | 118 ms: 1.27x slower                                                        |
| docutils                  | 2.59 sec                                               | 3.52 sec: 1.36x slower                                                      |
| sqlglot_parse             | 1.27 ms                                                | 1.75 ms: 1.37x slower                                                       |
| sqlglot_transpile         | 1.58 ms                                                | 2.19 ms: 1.38x slower                                                       |
| sympy_integrate           | 19.9 ms                                                | 27.5 ms: 1.38x slower                                                       |
| sympy_sum                 | 150 ms                                                 | 217 ms: 1.44x slower                                                        |
| pylint                    | 313 ms                                                 | 483 ms: 1.55x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.02x slower                                                                |

Benchmark hidden because not significant (8): json, regex_dna, pickle_pure_python, async_tree_none_tg, thrift, typing_runtime_protocols, tomli_loads, async_tree_cpu_io_mixed_tg
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240904-3.14.0a0-d467f6c-JIT/bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.015x slower
# HPT report

- Reliability score: 80.83% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x
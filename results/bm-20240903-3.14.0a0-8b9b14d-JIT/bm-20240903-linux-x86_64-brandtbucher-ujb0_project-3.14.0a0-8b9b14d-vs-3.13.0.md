# Results vs. 3.13.0

- fork: brandtbucher
- ref: ujb0_project
- machine: linux-x86_64
- commit hash: 8b9b14d
- commit date: 2024-09-03
- overall geometric mean: 1.019x slower
- HPT reliability: 94.40%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 296 ms: 1.11x slower                                                |
| docutils       | 2.59 sec                                               | 3.51 sec: 1.35x slower                                              |
| html5lib       | 64.2 ms                                                | 75.0 ms: 1.17x slower                                               |
| tornado_http   | 92.4 ms                                                | 117 ms: 1.27x slower                                                |
| Geometric mean | (ref)                                                  | 1.22x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 413 ms: 1.12x faster                                                |
| async_tree_memoization    | 442 ms                                                 | 426 ms: 1.04x faster                                                |
| async_tree_none           | 351 ms                                                 | 340 ms: 1.03x faster                                                |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 572 ms: 1.01x faster                                                |
| asyncio_websockets        | 552 ms                                                 | 559 ms: 1.01x slower                                                |
| async_tree_io_tg          | 857 ms                                                 | 885 ms: 1.03x slower                                                |
| async_generators          | 436 ms                                                 | 459 ms: 1.05x slower                                                |
| coroutines                | 22.7 ms                                                | 24.5 ms: 1.08x slower                                               |
| async_tree_io             | 842 ms                                                 | 953 ms: 1.13x slower                                                |
| Geometric mean            | (ref)                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 69.1 ms: 1.15x faster                                               |
| nbody          | 87.0 ms                                                | 80.7 ms: 1.08x faster                                               |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 26.4 ms: 1.01x slower                                               |
| regex_effbot   | 3.73 ms                                                | 3.87 ms: 1.04x slower                                               |
| regex_dna      | 218 ms                                                 | 230 ms: 1.05x slower                                                |
| regex_compile  | 132 ms                                                 | 155 ms: 1.17x slower                                                |
| Geometric mean | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_process    | 60.6 ms                                                | 54.2 ms: 1.12x faster                                               |
| xml_etree_generate   | 86.7 ms                                                | 78.4 ms: 1.11x faster                                               |
| unpickle_pure_python | 216 us                                                 | 197 us: 1.09x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                |
| json_dumps           | 10.6 ms                                                | 9.96 ms: 1.06x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 98.5 ms: 1.03x faster                                               |
| pickle_pure_python   | 310 us                                                 | 314 us: 1.01x slower                                                |
| json_loads           | 27.2 us                                                | 29.6 us: 1.09x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                               |
| python_startup_no_site | 6.96 ms                                                | 7.15 ms: 1.03x slower                                               |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.92 ms: 1.12x faster                                               |
| genshi_text     | 23.5 ms                                                | 22.8 ms: 1.03x faster                                               |
| django_template | 35.2 ms                                                | 39.7 ms: 1.13x slower                                               |
| genshi_xml      | 50.9 ms                                                | 60.8 ms: 1.19x slower                                               |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                        |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 26.1 us: 1.50x faster                                               |
| deepcopy                  | 358 us                                                 | 261 us: 1.37x faster                                                |
| create_gc_cycles          | 2.41 ms                                                | 1.79 ms: 1.34x faster                                               |
| gc_traversal              | 4.37 ms                                                | 3.60 ms: 1.21x faster                                               |
| python_startup            | 12.5 ms                                                | 10.6 ms: 1.18x faster                                               |
| scimark_fft               | 364 ms                                                 | 313 ms: 1.17x faster                                                |
| scimark_monte_carlo       | 67.4 ms                                                | 58.2 ms: 1.16x faster                                               |
| float                     | 79.2 ms                                                | 69.1 ms: 1.15x faster                                               |
| deepcopy_reduce           | 3.20 us                                                | 2.79 us: 1.15x faster                                               |
| crypto_pyaes              | 75.3 ms                                                | 65.9 ms: 1.14x faster                                               |
| spectral_norm             | 115 ms                                                 | 102 ms: 1.13x faster                                                |
| pathlib                   | 17.5 ms                                                | 15.6 ms: 1.12x faster                                               |
| async_tree_memoization_tg | 464 ms                                                 | 413 ms: 1.12x faster                                                |
| xml_etree_process         | 60.6 ms                                                | 54.2 ms: 1.12x faster                                               |
| mako                      | 11.1 ms                                                | 9.92 ms: 1.12x faster                                               |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.52 ms: 1.12x faster                                               |
| richards                  | 48.7 ms                                                | 43.9 ms: 1.11x faster                                               |
| xml_etree_generate        | 86.7 ms                                                | 78.4 ms: 1.11x faster                                               |
| fannkuch                  | 404 ms                                                 | 367 ms: 1.10x faster                                                |
| unpickle_pure_python      | 216 us                                                 | 197 us: 1.09x faster                                                |
| nbody                     | 87.0 ms                                                | 80.7 ms: 1.08x faster                                               |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                |
| json_dumps                | 10.6 ms                                                | 9.96 ms: 1.06x faster                                               |
| telco                     | 8.54 ms                                                | 8.13 ms: 1.05x faster                                               |
| bpe_tokeniser             | 4.75 sec                                               | 4.52 sec: 1.05x faster                                              |
| richards_super            | 54.9 ms                                                | 52.5 ms: 1.04x faster                                               |
| async_tree_memoization    | 442 ms                                                 | 426 ms: 1.04x faster                                                |
| genshi_text               | 23.5 ms                                                | 22.8 ms: 1.03x faster                                               |
| async_tree_none           | 351 ms                                                 | 340 ms: 1.03x faster                                                |
| xml_etree_iterparse       | 101 ms                                                 | 98.5 ms: 1.03x faster                                               |
| scimark_lu                | 113 ms                                                 | 110 ms: 1.02x faster                                                |
| pyflate                   | 471 ms                                                 | 461 ms: 1.02x faster                                                |
| meteor_contest            | 109 ms                                                 | 107 ms: 1.02x faster                                                |
| json                      | 5.36 ms                                                | 5.25 ms: 1.02x faster                                               |
| typing_runtime_protocols  | 165 us                                                 | 161 us: 1.02x faster                                                |
| logging_silent            | 102 ns                                                 | 99.8 ns: 1.02x faster                                               |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 572 ms: 1.01x faster                                                |
| pidigits                  | 186 ms                                                 | 185 ms: 1.00x faster                                                |
| mdp                       | 2.72 sec                                               | 2.73 sec: 1.00x slower                                              |
| regex_v8                  | 26.2 ms                                                | 26.4 ms: 1.01x slower                                               |
| pickle_pure_python        | 310 us                                                 | 314 us: 1.01x slower                                                |
| asyncio_websockets        | 552 ms                                                 | 559 ms: 1.01x slower                                                |
| comprehensions            | 16.5 us                                                | 16.8 us: 1.02x slower                                               |
| pprint_safe_repr          | 728 ms                                                 | 743 ms: 1.02x slower                                                |
| thrift                    | 809 us                                                 | 827 us: 1.02x slower                                                |
| chaos                     | 58.1 ms                                                | 59.4 ms: 1.02x slower                                               |
| python_startup_no_site    | 6.96 ms                                                | 7.15 ms: 1.03x slower                                               |
| pprint_pformat            | 1.49 sec                                               | 1.54 sec: 1.03x slower                                              |
| coverage                  | 84.0 ms                                                | 86.6 ms: 1.03x slower                                               |
| async_tree_io_tg          | 857 ms                                                 | 885 ms: 1.03x slower                                                |
| regex_effbot              | 3.73 ms                                                | 3.87 ms: 1.04x slower                                               |
| logging_simple            | 5.72 us                                                | 5.95 us: 1.04x slower                                               |
| bench_mp_pool             | 24.0 ms                                                | 25.0 ms: 1.04x slower                                               |
| logging_format            | 6.40 us                                                | 6.68 us: 1.04x slower                                               |
| async_generators          | 436 ms                                                 | 459 ms: 1.05x slower                                                |
| regex_dna                 | 218 ms                                                 | 230 ms: 1.05x slower                                                |
| raytrace                  | 267 ms                                                 | 284 ms: 1.06x slower                                                |
| nqueens                   | 78.4 ms                                                | 83.5 ms: 1.07x slower                                               |
| coroutines                | 22.7 ms                                                | 24.5 ms: 1.08x slower                                               |
| json_loads                | 27.2 us                                                | 29.6 us: 1.09x slower                                               |
| bench_thread_pool         | 822 us                                                 | 894 us: 1.09x slower                                                |
| deltablue                 | 3.23 ms                                                | 3.53 ms: 1.09x slower                                               |
| pycparser                 | 1.20 sec                                               | 1.33 sec: 1.10x slower                                              |
| 2to3                      | 267 ms                                                 | 296 ms: 1.11x slower                                                |
| django_template           | 35.2 ms                                                | 39.7 ms: 1.13x slower                                               |
| async_tree_io             | 842 ms                                                 | 953 ms: 1.13x slower                                                |
| sqlglot_normalize         | 108 ms                                                 | 125 ms: 1.16x slower                                                |
| html5lib                  | 64.2 ms                                                | 75.0 ms: 1.17x slower                                               |
| regex_compile             | 132 ms                                                 | 155 ms: 1.17x slower                                                |
| genshi_xml                | 50.9 ms                                                | 60.8 ms: 1.19x slower                                               |
| generators                | 29.0 ms                                                | 34.6 ms: 1.19x slower                                               |
| hexiom                    | 6.16 ms                                                | 7.42 ms: 1.20x slower                                               |
| sympy_expand              | 463 ms                                                 | 559 ms: 1.21x slower                                                |
| go                        | 144 ms                                                 | 179 ms: 1.25x slower                                                |
| sqlglot_optimize          | 53.7 ms                                                | 67.1 ms: 1.25x slower                                               |
| sympy_str                 | 275 ms                                                 | 344 ms: 1.25x slower                                                |
| tornado_http              | 92.4 ms                                                | 117 ms: 1.27x slower                                                |
| docutils                  | 2.59 sec                                               | 3.51 sec: 1.35x slower                                              |
| sqlglot_parse             | 1.27 ms                                                | 1.72 ms: 1.35x slower                                               |
| sqlglot_transpile         | 1.58 ms                                                | 2.17 ms: 1.37x slower                                               |
| sympy_integrate           | 19.9 ms                                                | 27.4 ms: 1.38x slower                                               |
| sympy_sum                 | 150 ms                                                 | 217 ms: 1.44x slower                                                |
| pylint                    | 313 ms                                                 | 480 ms: 1.54x slower                                                |
| Geometric mean            | (ref)                                                  | 1.02x slower                                                        |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_cpu_io_mixed_tg, tomli_loads, scimark_sor
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240903-3.14.0a0-8b9b14d-JIT/bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.019x slower
# HPT report

- Reliability score: 94.40% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x
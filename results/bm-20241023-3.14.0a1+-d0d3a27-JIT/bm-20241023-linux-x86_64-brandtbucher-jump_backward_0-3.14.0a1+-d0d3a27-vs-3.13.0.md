# Results vs. 3.13.0

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: d0d3a27
- commit date: 2024-10-23
- overall geometric mean: 1.043x slower
- HPT reliability: 98.16%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 288 ms: 1.08x slower                                                    |
| docutils       | 2.59 sec                                               | 3.41 sec: 1.31x slower                                                  |
| html5lib       | 64.2 ms                                                | 70.3 ms: 1.10x slower                                                   |
| sphinx         | 1.03 sec                                               | 1.36 sec: 1.31x slower                                                  |
| tornado_http   | 92.4 ms                                                | 112 ms: 1.21x slower                                                    |
| Geometric mean | (ref)                                                  | 1.20x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 408 ms: 1.14x faster                                                    |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                                    |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 596 ms: 1.03x slower                                                    |
| async_tree_none_tg         | 321 ms                                                 | 331 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 584 ms: 1.07x slower                                                    |
| async_generators           | 436 ms                                                 | 468 ms: 1.07x slower                                                    |
| async_tree_io_tg           | 857 ms                                                 | 956 ms: 1.12x slower                                                    |
| async_tree_io              | 842 ms                                                 | 940 ms: 1.12x slower                                                    |
| coroutines                 | 22.7 ms                                                | 26.6 ms: 1.17x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.04x slower                                                            |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 81.2 ms: 1.07x faster                                                   |
| float          | 79.2 ms                                                | 75.5 ms: 1.05x faster                                                   |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 26.1 ms: 1.01x faster                                                   |
| regex_dna      | 218 ms                                                 | 223 ms: 1.02x slower                                                    |
| regex_effbot   | 3.73 ms                                                | 3.94 ms: 1.06x slower                                                   |
| regex_compile  | 132 ms                                                 | 147 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                  | 1.04x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.95 sec: 1.10x faster                                                  |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                    |
| pickle_pure_python   | 310 us                                                 | 296 us: 1.05x faster                                                    |
| xml_etree_generate   | 86.7 ms                                                | 82.8 ms: 1.05x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 99.4 ms: 1.02x faster                                                   |
| json_loads           | 27.2 us                                                | 26.7 us: 1.02x faster                                                   |
| xml_etree_process    | 60.6 ms                                                | 59.8 ms: 1.01x faster                                                   |
| json_dumps           | 10.6 ms                                                | 11.0 ms: 1.04x slower                                                   |
| unpickle_pure_python | 216 us                                                 | 226 us: 1.05x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.9 ms: 1.05x faster                                                   |
| python_startup_no_site | 6.96 ms                                                | 7.22 ms: 1.04x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.5 ms: 1.06x faster                                                   |
| genshi_text     | 23.5 ms                                                | 26.6 ms: 1.13x slower                                                   |
| django_template | 35.2 ms                                                | 40.5 ms: 1.15x slower                                                   |
| genshi_xml      | 50.9 ms                                                | 62.8 ms: 1.23x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.11x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 30.1 us: 1.30x faster                                                   |
| deepcopy                   | 358 us                                                 | 276 us: 1.30x faster                                                    |
| scimark_fft                | 364 ms                                                 | 319 ms: 1.14x faster                                                    |
| async_tree_memoization_tg  | 464 ms                                                 | 408 ms: 1.14x faster                                                    |
| telco                      | 8.54 ms                                                | 7.64 ms: 1.12x faster                                                   |
| go                         | 144 ms                                                 | 129 ms: 1.12x faster                                                    |
| crypto_pyaes               | 75.3 ms                                                | 68.3 ms: 1.10x faster                                                   |
| deepcopy_reduce            | 3.20 us                                                | 2.91 us: 1.10x faster                                                   |
| tomli_loads                | 2.14 sec                                               | 1.95 sec: 1.10x faster                                                  |
| scimark_monte_carlo        | 67.4 ms                                                | 62.3 ms: 1.08x faster                                                   |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.66 ms: 1.08x faster                                                   |
| json                       | 5.36 ms                                                | 4.97 ms: 1.08x faster                                                   |
| nbody                      | 87.0 ms                                                | 81.2 ms: 1.07x faster                                                   |
| fannkuch                   | 404 ms                                                 | 378 ms: 1.07x faster                                                    |
| pathlib                    | 17.5 ms                                                | 16.4 ms: 1.07x faster                                                   |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                    |
| bpe_tokeniser              | 4.75 sec                                               | 4.48 sec: 1.06x faster                                                  |
| mako                       | 11.1 ms                                                | 10.5 ms: 1.06x faster                                                   |
| pickle_pure_python         | 310 us                                                 | 296 us: 1.05x faster                                                    |
| float                      | 79.2 ms                                                | 75.5 ms: 1.05x faster                                                   |
| xml_etree_generate         | 86.7 ms                                                | 82.8 ms: 1.05x faster                                                   |
| python_startup             | 12.5 ms                                                | 11.9 ms: 1.05x faster                                                   |
| scimark_sor                | 124 ms                                                 | 120 ms: 1.03x faster                                                    |
| mdp                        | 2.72 sec                                               | 2.65 sec: 1.02x faster                                                  |
| pprint_pformat             | 1.49 sec                                               | 1.46 sec: 1.02x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 99.4 ms: 1.02x faster                                                   |
| pprint_safe_repr           | 728 ms                                                 | 715 ms: 1.02x faster                                                    |
| json_loads                 | 27.2 us                                                | 26.7 us: 1.02x faster                                                   |
| xml_etree_process          | 60.6 ms                                                | 59.8 ms: 1.01x faster                                                   |
| pyflate                    | 471 ms                                                 | 467 ms: 1.01x faster                                                    |
| regex_v8                   | 26.2 ms                                                | 26.1 ms: 1.01x faster                                                   |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.00x faster                                                    |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                    |
| richards_super             | 54.9 ms                                                | 55.2 ms: 1.01x slower                                                   |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                                    |
| scimark_lu                 | 113 ms                                                 | 114 ms: 1.02x slower                                                    |
| typing_runtime_protocols   | 165 us                                                 | 167 us: 1.02x slower                                                    |
| regex_dna                  | 218 ms                                                 | 223 ms: 1.02x slower                                                    |
| thrift                     | 809 us                                                 | 826 us: 1.02x slower                                                    |
| richards                   | 48.7 ms                                                | 49.9 ms: 1.03x slower                                                   |
| chaos                      | 58.1 ms                                                | 59.5 ms: 1.03x slower                                                   |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 596 ms: 1.03x slower                                                    |
| async_tree_none_tg         | 321 ms                                                 | 331 ms: 1.03x slower                                                    |
| coverage                   | 84.0 ms                                                | 86.9 ms: 1.03x slower                                                   |
| python_startup_no_site     | 6.96 ms                                                | 7.22 ms: 1.04x slower                                                   |
| json_dumps                 | 10.6 ms                                                | 11.0 ms: 1.04x slower                                                   |
| unpickle_pure_python       | 216 us                                                 | 226 us: 1.05x slower                                                    |
| regex_effbot               | 3.73 ms                                                | 3.94 ms: 1.06x slower                                                   |
| logging_silent             | 102 ns                                                 | 108 ns: 1.06x slower                                                    |
| dulwich_log                | 64.3 ms                                                | 68.6 ms: 1.07x slower                                                   |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 584 ms: 1.07x slower                                                    |
| async_generators           | 436 ms                                                 | 468 ms: 1.07x slower                                                    |
| 2to3                       | 267 ms                                                 | 288 ms: 1.08x slower                                                    |
| comprehensions             | 16.5 us                                                | 17.8 us: 1.08x slower                                                   |
| html5lib                   | 64.2 ms                                                | 70.3 ms: 1.10x slower                                                   |
| raytrace                   | 267 ms                                                 | 295 ms: 1.11x slower                                                    |
| gc_traversal               | 4.37 ms                                                | 4.85 ms: 1.11x slower                                                   |
| regex_compile              | 132 ms                                                 | 147 ms: 1.11x slower                                                    |
| pycparser                  | 1.20 sec                                               | 1.34 sec: 1.11x slower                                                  |
| nqueens                    | 78.4 ms                                                | 87.3 ms: 1.11x slower                                                   |
| async_tree_io_tg           | 857 ms                                                 | 956 ms: 1.12x slower                                                    |
| async_tree_io              | 842 ms                                                 | 940 ms: 1.12x slower                                                    |
| create_gc_cycles           | 2.41 ms                                                | 2.69 ms: 1.12x slower                                                   |
| sqlglot_normalize          | 108 ms                                                 | 121 ms: 1.12x slower                                                    |
| sqlglot_parse              | 1.27 ms                                                | 1.44 ms: 1.13x slower                                                   |
| genshi_text                | 23.5 ms                                                | 26.6 ms: 1.13x slower                                                   |
| django_template            | 35.2 ms                                                | 40.5 ms: 1.15x slower                                                   |
| sympy_expand               | 463 ms                                                 | 536 ms: 1.16x slower                                                    |
| logging_format             | 6.40 us                                                | 7.43 us: 1.16x slower                                                   |
| sqlglot_transpile          | 1.58 ms                                                | 1.85 ms: 1.17x slower                                                   |
| bench_thread_pool          | 822 us                                                 | 963 us: 1.17x slower                                                    |
| coroutines                 | 22.7 ms                                                | 26.6 ms: 1.17x slower                                                   |
| logging_simple             | 5.72 us                                                | 6.90 us: 1.21x slower                                                   |
| tornado_http               | 92.4 ms                                                | 112 ms: 1.21x slower                                                    |
| sympy_str                  | 275 ms                                                 | 333 ms: 1.21x slower                                                    |
| hexiom                     | 6.16 ms                                                | 7.48 ms: 1.21x slower                                                   |
| genshi_xml                 | 50.9 ms                                                | 62.8 ms: 1.23x slower                                                   |
| deltablue                  | 3.23 ms                                                | 4.03 ms: 1.25x slower                                                   |
| sqlglot_optimize           | 53.7 ms                                                | 67.2 ms: 1.25x slower                                                   |
| generators                 | 29.0 ms                                                | 36.5 ms: 1.26x slower                                                   |
| docutils                   | 2.59 sec                                               | 3.41 sec: 1.31x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.36 sec: 1.31x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 208 ms: 1.38x slower                                                    |
| sympy_integrate            | 19.9 ms                                                | 27.6 ms: 1.39x slower                                                   |
| pylint                     | 313 ms                                                 | 468 ms: 1.50x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 89.9 ms: 3.75x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                            |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_none, spectral_norm
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.043x slower
# HPT report

- Reliability score: 98.16% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x
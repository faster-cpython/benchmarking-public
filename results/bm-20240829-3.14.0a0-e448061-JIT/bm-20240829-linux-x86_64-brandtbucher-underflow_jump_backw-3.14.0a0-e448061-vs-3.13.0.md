# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow_jump_backw
- machine: linux-x86_64
- commit hash: e448061
- commit date: 2024-08-29
- overall geometric mean: 1.034x slower
- HPT reliability: 99.03%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 290 ms: 1.09x slower                                                        |
| docutils       | 2.59 sec                                               | 3.58 sec: 1.38x slower                                                      |
| html5lib       | 64.2 ms                                                | 75.5 ms: 1.18x slower                                                       |
| tornado_http   | 92.4 ms                                                | 120 ms: 1.29x slower                                                        |
| Geometric mean | (ref)                                                  | 1.23x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 416 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 581 ms: 1.01x slower                                                        |
| asyncio_websockets         | 552 ms                                                 | 559 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 558 ms: 1.02x slower                                                        |
| async_tree_io_tg           | 857 ms                                                 | 896 ms: 1.05x slower                                                        |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                        |
| coroutines                 | 22.7 ms                                                | 24.0 ms: 1.06x slower                                                       |
| async_tree_io              | 842 ms                                                 | 966 ms: 1.15x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                                |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 70.4 ms: 1.12x faster                                                       |
| nbody          | 87.0 ms                                                | 80.3 ms: 1.08x faster                                                       |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.5 ms: 1.03x faster                                                       |
| regex_dna      | 218 ms                                                 | 221 ms: 1.01x slower                                                        |
| regex_effbot   | 3.73 ms                                                | 3.79 ms: 1.02x slower                                                       |
| regex_compile  | 132 ms                                                 | 147 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 310 us                                                 | 288 us: 1.08x faster                                                        |
| xml_etree_generate   | 86.7 ms                                                | 81.4 ms: 1.07x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                        |
| xml_etree_process    | 60.6 ms                                                | 57.2 ms: 1.06x faster                                                       |
| json_dumps           | 10.6 ms                                                | 9.97 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                                       |
| unpickle_pure_python | 216 us                                                 | 211 us: 1.02x faster                                                        |
| tomli_loads          | 2.14 sec                                               | 2.18 sec: 1.02x slower                                                      |
| json_loads           | 27.2 us                                                | 28.3 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.17x faster                                                       |
| python_startup_no_site | 6.96 ms                                                | 7.19 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.3 ms: 1.07x faster                                                       |
| genshi_text     | 23.5 ms                                                | 24.3 ms: 1.03x slower                                                       |
| django_template | 35.2 ms                                                | 42.1 ms: 1.20x slower                                                       |
| genshi_xml      | 50.9 ms                                                | 67.5 ms: 1.33x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.11x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 28.9 us: 1.35x faster                                                       |
| create_gc_cycles           | 2.41 ms                                                | 1.81 ms: 1.33x faster                                                       |
| deepcopy                   | 358 us                                                 | 272 us: 1.32x faster                                                        |
| scimark_fft                | 364 ms                                                 | 301 ms: 1.21x faster                                                        |
| python_startup             | 12.5 ms                                                | 10.6 ms: 1.17x faster                                                       |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.34 ms: 1.16x faster                                                       |
| gc_traversal               | 4.37 ms                                                | 3.78 ms: 1.16x faster                                                       |
| crypto_pyaes               | 75.3 ms                                                | 65.7 ms: 1.15x faster                                                       |
| scimark_monte_carlo        | 67.4 ms                                                | 58.9 ms: 1.15x faster                                                       |
| float                      | 79.2 ms                                                | 70.4 ms: 1.12x faster                                                       |
| deepcopy_reduce            | 3.20 us                                                | 2.86 us: 1.12x faster                                                       |
| telco                      | 8.54 ms                                                | 7.64 ms: 1.12x faster                                                       |
| pathlib                    | 17.5 ms                                                | 15.7 ms: 1.12x faster                                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 416 ms: 1.11x faster                                                        |
| nbody                      | 87.0 ms                                                | 80.3 ms: 1.08x faster                                                       |
| fannkuch                   | 404 ms                                                 | 373 ms: 1.08x faster                                                        |
| pickle_pure_python         | 310 us                                                 | 288 us: 1.08x faster                                                        |
| spectral_norm              | 115 ms                                                 | 107 ms: 1.08x faster                                                        |
| mako                       | 11.1 ms                                                | 10.3 ms: 1.07x faster                                                       |
| xml_etree_generate         | 86.7 ms                                                | 81.4 ms: 1.07x faster                                                       |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                                        |
| xml_etree_process          | 60.6 ms                                                | 57.2 ms: 1.06x faster                                                       |
| json_dumps                 | 10.6 ms                                                | 9.97 ms: 1.06x faster                                                       |
| pprint_safe_repr           | 728 ms                                                 | 688 ms: 1.06x faster                                                        |
| bpe_tokeniser              | 4.75 sec                                               | 4.49 sec: 1.06x faster                                                      |
| pyflate                    | 471 ms                                                 | 445 ms: 1.06x faster                                                        |
| pprint_pformat             | 1.49 sec                                               | 1.44 sec: 1.04x faster                                                      |
| json                       | 5.36 ms                                                | 5.18 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                                       |
| regex_v8                   | 26.2 ms                                                | 25.5 ms: 1.03x faster                                                       |
| unpickle_pure_python       | 216 us                                                 | 211 us: 1.02x faster                                                        |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                        |
| typing_runtime_protocols   | 165 us                                                 | 163 us: 1.01x faster                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| bench_mp_pool              | 24.0 ms                                                | 24.1 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 581 ms: 1.01x slower                                                        |
| regex_dna                  | 218 ms                                                 | 221 ms: 1.01x slower                                                        |
| asyncio_websockets         | 552 ms                                                 | 559 ms: 1.01x slower                                                        |
| regex_effbot               | 3.73 ms                                                | 3.79 ms: 1.02x slower                                                       |
| tomli_loads                | 2.14 sec                                               | 2.18 sec: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 558 ms: 1.02x slower                                                        |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                                        |
| thrift                     | 809 us                                                 | 831 us: 1.03x slower                                                        |
| mdp                        | 2.72 sec                                               | 2.80 sec: 1.03x slower                                                      |
| python_startup_no_site     | 6.96 ms                                                | 7.19 ms: 1.03x slower                                                       |
| genshi_text                | 23.5 ms                                                | 24.3 ms: 1.03x slower                                                       |
| scimark_sor                | 124 ms                                                 | 128 ms: 1.04x slower                                                        |
| json_loads                 | 27.2 us                                                | 28.3 us: 1.04x slower                                                       |
| coverage                   | 84.0 ms                                                | 87.4 ms: 1.04x slower                                                       |
| async_tree_io_tg           | 857 ms                                                 | 896 ms: 1.05x slower                                                        |
| comprehensions             | 16.5 us                                                | 17.3 us: 1.05x slower                                                       |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                        |
| coroutines                 | 22.7 ms                                                | 24.0 ms: 1.06x slower                                                       |
| raytrace                   | 267 ms                                                 | 284 ms: 1.06x slower                                                        |
| chaos                      | 58.1 ms                                                | 62.6 ms: 1.08x slower                                                       |
| 2to3                       | 267 ms                                                 | 290 ms: 1.09x slower                                                        |
| pycparser                  | 1.20 sec                                               | 1.32 sec: 1.10x slower                                                      |
| nqueens                    | 78.4 ms                                                | 86.6 ms: 1.11x slower                                                       |
| regex_compile              | 132 ms                                                 | 147 ms: 1.11x slower                                                        |
| bench_thread_pool          | 822 us                                                 | 914 us: 1.11x slower                                                        |
| richards                   | 48.7 ms                                                | 54.2 ms: 1.11x slower                                                       |
| logging_silent             | 102 ns                                                 | 113 ns: 1.11x slower                                                        |
| richards_super             | 54.9 ms                                                | 62.0 ms: 1.13x slower                                                       |
| async_tree_io              | 842 ms                                                 | 966 ms: 1.15x slower                                                        |
| hexiom                     | 6.16 ms                                                | 7.15 ms: 1.16x slower                                                       |
| logging_format             | 6.40 us                                                | 7.45 us: 1.17x slower                                                       |
| html5lib                   | 64.2 ms                                                | 75.5 ms: 1.18x slower                                                       |
| sqlglot_normalize          | 108 ms                                                 | 128 ms: 1.19x slower                                                        |
| generators                 | 29.0 ms                                                | 34.5 ms: 1.19x slower                                                       |
| django_template            | 35.2 ms                                                | 42.1 ms: 1.20x slower                                                       |
| logging_simple             | 5.72 us                                                | 6.91 us: 1.21x slower                                                       |
| sympy_expand               | 463 ms                                                 | 565 ms: 1.22x slower                                                        |
| sympy_str                  | 275 ms                                                 | 339 ms: 1.23x slower                                                        |
| sqlglot_optimize           | 53.7 ms                                                | 66.3 ms: 1.23x slower                                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.60 ms: 1.26x slower                                                       |
| go                         | 144 ms                                                 | 182 ms: 1.26x slower                                                        |
| sqlglot_transpile          | 1.58 ms                                                | 2.02 ms: 1.27x slower                                                       |
| tornado_http               | 92.4 ms                                                | 120 ms: 1.29x slower                                                        |
| genshi_xml                 | 50.9 ms                                                | 67.5 ms: 1.33x slower                                                       |
| sympy_integrate            | 19.9 ms                                                | 27.3 ms: 1.37x slower                                                       |
| docutils                   | 2.59 sec                                               | 3.58 sec: 1.38x slower                                                      |
| deltablue                  | 3.23 ms                                                | 4.46 ms: 1.38x slower                                                       |
| sympy_sum                  | 150 ms                                                 | 213 ms: 1.41x slower                                                        |
| pylint                     | 313 ms                                                 | 486 ms: 1.55x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.04x slower                                                                |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_none, async_tree_none_tg
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240829-3.14.0a0-e448061-JIT/bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.034x slower
# HPT report

- Reliability score: 99.03% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x
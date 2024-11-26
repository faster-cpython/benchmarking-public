# Results vs. 3.13.0

- fork: brandtbucher
- ref: deopt_tracing_32
- machine: linux-x86_64
- commit hash: a7a7e7f
- commit date: 2024-09-13
- overall geometric mean: 1.028x faster
- HPT reliability: 91.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 279 ms: 1.04x slower                                                    |
| docutils       | 2.59 sec                                               | 2.95 sec: 1.14x slower                                                  |
| html5lib       | 64.2 ms                                                | 64.7 ms: 1.01x slower                                                   |
| tornado_http   | 92.4 ms                                                | 94.6 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 387 ms: 1.20x faster                                                    |
| async_tree_memoization    | 442 ms                                                 | 394 ms: 1.12x faster                                                    |
| async_tree_none           | 351 ms                                                 | 315 ms: 1.11x faster                                                    |
| async_tree_none_tg        | 321 ms                                                 | 307 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 565 ms: 1.02x faster                                                    |
| asyncio_websockets        | 552 ms                                                 | 556 ms: 1.01x slower                                                    |
| async_generators          | 436 ms                                                 | 455 ms: 1.04x slower                                                    |
| coroutines                | 22.7 ms                                                | 24.9 ms: 1.10x slower                                                   |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 69.4 ms: 1.14x faster                                                   |
| nbody          | 87.0 ms                                                | 81.9 ms: 1.06x faster                                                   |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                  | 1.07x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.1 ms: 1.04x faster                                                   |
| regex_dna      | 218 ms                                                 | 221 ms: 1.01x slower                                                    |
| regex_compile  | 132 ms                                                 | 142 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 77.5 ms: 1.12x faster                                                   |
| tomli_loads          | 2.14 sec                                               | 1.92 sec: 1.12x faster                                                  |
| xml_etree_process    | 60.6 ms                                                | 54.7 ms: 1.11x faster                                                   |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                    |
| json_dumps           | 10.6 ms                                                | 10.1 ms: 1.05x faster                                                   |
| pickle_pure_python   | 310 us                                                 | 304 us: 1.02x faster                                                    |
| xml_etree_iterparse  | 101 ms                                                 | 99.7 ms: 1.02x faster                                                   |
| unpickle_pure_python | 216 us                                                 | 213 us: 1.01x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                            |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                   |
| python_startup_no_site | 6.96 ms                                                | 7.08 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.79 ms: 1.13x faster                                                   |
| django_template | 35.2 ms                                                | 35.8 ms: 1.02x slower                                                   |
| genshi_text     | 23.5 ms                                                | 25.1 ms: 1.07x slower                                                   |
| genshi_xml      | 50.9 ms                                                | 59.4 ms: 1.17x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 27.0 us: 1.45x faster                                                   |
| create_gc_cycles          | 2.41 ms                                                | 1.77 ms: 1.36x faster                                                   |
| deepcopy                  | 358 us                                                 | 264 us: 1.36x faster                                                    |
| deepcopy_reduce           | 3.20 us                                                | 2.62 us: 1.22x faster                                                   |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.21 ms: 1.20x faster                                                   |
| async_tree_memoization_tg | 464 ms                                                 | 387 ms: 1.20x faster                                                    |
| gc_traversal              | 4.37 ms                                                | 3.65 ms: 1.20x faster                                                   |
| scimark_fft               | 364 ms                                                 | 307 ms: 1.19x faster                                                    |
| richards                  | 48.7 ms                                                | 41.1 ms: 1.19x faster                                                   |
| python_startup            | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                   |
| richards_super            | 54.9 ms                                                | 47.3 ms: 1.16x faster                                                   |
| crypto_pyaes              | 75.3 ms                                                | 65.3 ms: 1.15x faster                                                   |
| spectral_norm             | 115 ms                                                 | 100 ms: 1.15x faster                                                    |
| float                     | 79.2 ms                                                | 69.4 ms: 1.14x faster                                                   |
| mako                      | 11.1 ms                                                | 9.79 ms: 1.13x faster                                                   |
| async_tree_memoization    | 442 ms                                                 | 394 ms: 1.12x faster                                                    |
| xml_etree_generate        | 86.7 ms                                                | 77.5 ms: 1.12x faster                                                   |
| tomli_loads               | 2.14 sec                                               | 1.92 sec: 1.12x faster                                                  |
| async_tree_none           | 351 ms                                                 | 315 ms: 1.11x faster                                                    |
| xml_etree_process         | 60.6 ms                                                | 54.7 ms: 1.11x faster                                                   |
| pathlib                   | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                   |
| json                      | 5.36 ms                                                | 4.95 ms: 1.08x faster                                                   |
| mdp                       | 2.72 sec                                               | 2.52 sec: 1.08x faster                                                  |
| scimark_monte_carlo       | 67.4 ms                                                | 62.6 ms: 1.08x faster                                                   |
| telco                     | 8.54 ms                                                | 7.93 ms: 1.08x faster                                                   |
| go                        | 144 ms                                                 | 135 ms: 1.07x faster                                                    |
| bpe_tokeniser             | 4.75 sec                                               | 4.45 sec: 1.07x faster                                                  |
| fannkuch                  | 404 ms                                                 | 380 ms: 1.07x faster                                                    |
| nbody                     | 87.0 ms                                                | 81.9 ms: 1.06x faster                                                   |
| xml_etree_parse           | 156 ms                                                 | 147 ms: 1.06x faster                                                    |
| scimark_sor               | 124 ms                                                 | 117 ms: 1.06x faster                                                    |
| json_dumps                | 10.6 ms                                                | 10.1 ms: 1.05x faster                                                   |
| logging_format            | 6.40 us                                                | 6.10 us: 1.05x faster                                                   |
| async_tree_none_tg        | 321 ms                                                 | 307 ms: 1.05x faster                                                    |
| regex_v8                  | 26.2 ms                                                | 25.1 ms: 1.04x faster                                                   |
| pyflate                   | 471 ms                                                 | 458 ms: 1.03x faster                                                    |
| thrift                    | 809 us                                                 | 789 us: 1.03x faster                                                    |
| logging_simple            | 5.72 us                                                | 5.58 us: 1.02x faster                                                   |
| meteor_contest            | 109 ms                                                 | 106 ms: 1.02x faster                                                    |
| pickle_pure_python        | 310 us                                                 | 304 us: 1.02x faster                                                    |
| typing_runtime_protocols  | 165 us                                                 | 161 us: 1.02x faster                                                    |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 565 ms: 1.02x faster                                                    |
| xml_etree_iterparse       | 101 ms                                                 | 99.7 ms: 1.02x faster                                                   |
| scimark_lu                | 113 ms                                                 | 111 ms: 1.01x faster                                                    |
| unpickle_pure_python      | 216 us                                                 | 213 us: 1.01x faster                                                    |
| pprint_safe_repr          | 728 ms                                                 | 720 ms: 1.01x faster                                                    |
| pprint_pformat            | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                  |
| pidigits                  | 186 ms                                                 | 185 ms: 1.00x faster                                                    |
| logging_silent            | 102 ns                                                 | 102 ns: 1.00x slower                                                    |
| asyncio_websockets        | 552 ms                                                 | 556 ms: 1.01x slower                                                    |
| html5lib                  | 64.2 ms                                                | 64.7 ms: 1.01x slower                                                   |
| chaos                     | 58.1 ms                                                | 58.5 ms: 1.01x slower                                                   |
| regex_dna                 | 218 ms                                                 | 221 ms: 1.01x slower                                                    |
| pycparser                 | 1.20 sec                                               | 1.21 sec: 1.01x slower                                                  |
| bench_thread_pool         | 822 us                                                 | 835 us: 1.02x slower                                                    |
| python_startup_no_site    | 6.96 ms                                                | 7.08 ms: 1.02x slower                                                   |
| django_template           | 35.2 ms                                                | 35.8 ms: 1.02x slower                                                   |
| tornado_http              | 92.4 ms                                                | 94.6 ms: 1.02x slower                                                   |
| raytrace                  | 267 ms                                                 | 276 ms: 1.03x slower                                                    |
| dulwich_log               | 64.3 ms                                                | 66.7 ms: 1.04x slower                                                   |
| async_generators          | 436 ms                                                 | 455 ms: 1.04x slower                                                    |
| 2to3                      | 267 ms                                                 | 279 ms: 1.04x slower                                                    |
| sqlglot_parse             | 1.27 ms                                                | 1.35 ms: 1.06x slower                                                   |
| sqlglot_normalize         | 108 ms                                                 | 115 ms: 1.07x slower                                                    |
| coverage                  | 84.0 ms                                                | 89.6 ms: 1.07x slower                                                   |
| genshi_text               | 23.5 ms                                                | 25.1 ms: 1.07x slower                                                   |
| regex_compile             | 132 ms                                                 | 142 ms: 1.07x slower                                                    |
| nqueens                   | 78.4 ms                                                | 84.8 ms: 1.08x slower                                                   |
| sqlglot_transpile         | 1.58 ms                                                | 1.72 ms: 1.08x slower                                                   |
| coroutines                | 22.7 ms                                                | 24.9 ms: 1.10x slower                                                   |
| sqlglot_optimize          | 53.7 ms                                                | 59.0 ms: 1.10x slower                                                   |
| deltablue                 | 3.23 ms                                                | 3.55 ms: 1.10x slower                                                   |
| sympy_str                 | 275 ms                                                 | 305 ms: 1.11x slower                                                    |
| sympy_expand              | 463 ms                                                 | 517 ms: 1.11x slower                                                    |
| hexiom                    | 6.16 ms                                                | 6.89 ms: 1.12x slower                                                   |
| docutils                  | 2.59 sec                                               | 2.95 sec: 1.14x slower                                                  |
| generators                | 29.0 ms                                                | 33.2 ms: 1.15x slower                                                   |
| sympy_integrate           | 19.9 ms                                                | 23.0 ms: 1.16x slower                                                   |
| sympy_sum                 | 150 ms                                                 | 174 ms: 1.16x slower                                                    |
| genshi_xml                | 50.9 ms                                                | 59.4 ms: 1.17x slower                                                   |
| pylint                    | 313 ms                                                 | 379 ms: 1.21x slower                                                    |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (7): json_loads, comprehensions, regex_effbot, bench_mp_pool, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240913-3.14.0a0-a7a7e7f-JIT/bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.028x faster
# HPT report

- Reliability score: 91.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x
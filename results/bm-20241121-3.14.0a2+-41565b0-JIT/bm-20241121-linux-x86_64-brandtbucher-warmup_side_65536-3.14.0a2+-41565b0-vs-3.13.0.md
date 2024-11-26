# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_side_65536
- machine: linux-x86_64
- commit hash: 41565b0
- commit date: 2024-11-21
- overall geometric mean: 1.016x faster
- HPT reliability: 65.80%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 260 ms: 1.03x faster                                                      |
| docutils       | 2.59 sec                                               | 2.71 sec: 1.04x slower                                                    |
| html5lib       | 64.2 ms                                                | 67.4 ms: 1.05x slower                                                     |
| sphinx         | 1.03 sec                                               | 1.08 sec: 1.05x slower                                                    |
| Geometric mean | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 400 ms: 1.16x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 407 ms: 1.09x faster                                                      |
| async_tree_none            | 351 ms                                                 | 325 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 561 ms: 1.03x faster                                                      |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                      |
| coroutines                 | 22.7 ms                                                | 23.4 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 568 ms: 1.04x slower                                                      |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                      |
| async_tree_io_tg           | 857 ms                                                 | 916 ms: 1.07x slower                                                      |
| async_tree_io              | 842 ms                                                 | 906 ms: 1.08x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 84.8 ms: 1.03x faster                                                     |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                      |
| float          | 79.2 ms                                                | 82.3 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.40 ms: 1.10x faster                                                     |
| regex_v8       | 26.2 ms                                                | 25.0 ms: 1.05x faster                                                     |
| regex_compile  | 132 ms                                                 | 131 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                 | 194 us: 1.11x faster                                                      |
| xml_etree_generate   | 86.7 ms                                                | 78.8 ms: 1.10x faster                                                     |
| tomli_loads          | 2.14 sec                                               | 1.99 sec: 1.08x faster                                                    |
| xml_etree_process    | 60.6 ms                                                | 57.1 ms: 1.06x faster                                                     |
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.04x faster                                                      |
| json_loads           | 27.2 us                                                | 26.3 us: 1.04x faster                                                     |
| pickle_pure_python   | 310 us                                                 | 323 us: 1.04x slower                                                      |
| json_dumps           | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                     |
| python_startup         | 12.5 ms                                                | 12.9 ms: 1.03x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.2 ms: 1.09x faster                                                     |
| django_template | 35.2 ms                                                | 33.1 ms: 1.06x faster                                                     |
| genshi_text     | 23.5 ms                                                | 24.9 ms: 1.06x slower                                                     |
| genshi_xml      | 50.9 ms                                                | 56.2 ms: 1.10x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 267 us: 1.34x faster                                                      |
| deepcopy_memo              | 39.1 us                                                | 29.1 us: 1.34x faster                                                     |
| richards                   | 48.7 ms                                                | 39.3 ms: 1.24x faster                                                     |
| richards_super             | 54.9 ms                                                | 45.6 ms: 1.20x faster                                                     |
| deepcopy_reduce            | 3.20 us                                                | 2.69 us: 1.19x faster                                                     |
| pylint                     | 313 ms                                                 | 269 ms: 1.16x faster                                                      |
| async_tree_memoization_tg  | 464 ms                                                 | 400 ms: 1.16x faster                                                      |
| scimark_fft                | 364 ms                                                 | 315 ms: 1.15x faster                                                      |
| go                         | 144 ms                                                 | 126 ms: 1.14x faster                                                      |
| telco                      | 8.54 ms                                                | 7.63 ms: 1.12x faster                                                     |
| unpickle_pure_python       | 216 us                                                 | 194 us: 1.11x faster                                                      |
| xml_etree_generate         | 86.7 ms                                                | 78.8 ms: 1.10x faster                                                     |
| regex_effbot               | 3.73 ms                                                | 3.40 ms: 1.10x faster                                                     |
| crypto_pyaes               | 75.3 ms                                                | 68.6 ms: 1.10x faster                                                     |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.62 ms: 1.09x faster                                                     |
| mako                       | 11.1 ms                                                | 10.2 ms: 1.09x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 407 ms: 1.09x faster                                                      |
| pathlib                    | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                     |
| tomli_loads                | 2.14 sec                                               | 1.99 sec: 1.08x faster                                                    |
| json                       | 5.36 ms                                                | 4.97 ms: 1.08x faster                                                     |
| async_tree_none            | 351 ms                                                 | 325 ms: 1.08x faster                                                      |
| xml_etree_process          | 60.6 ms                                                | 57.1 ms: 1.06x faster                                                     |
| bpe_tokeniser              | 4.75 sec                                               | 4.47 sec: 1.06x faster                                                    |
| django_template            | 35.2 ms                                                | 33.1 ms: 1.06x faster                                                     |
| mdp                        | 2.72 sec                                               | 2.58 sec: 1.05x faster                                                    |
| regex_v8                   | 26.2 ms                                                | 25.0 ms: 1.05x faster                                                     |
| fannkuch                   | 404 ms                                                 | 388 ms: 1.04x faster                                                      |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.04x faster                                                      |
| json_loads                 | 27.2 us                                                | 26.3 us: 1.04x faster                                                     |
| pyflate                    | 471 ms                                                 | 455 ms: 1.04x faster                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                      |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                    |
| scimark_monte_carlo        | 67.4 ms                                                | 65.5 ms: 1.03x faster                                                     |
| scimark_sor                | 124 ms                                                 | 120 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 561 ms: 1.03x faster                                                      |
| deltablue                  | 3.23 ms                                                | 3.14 ms: 1.03x faster                                                     |
| 2to3                       | 267 ms                                                 | 260 ms: 1.03x faster                                                      |
| nbody                      | 87.0 ms                                                | 84.8 ms: 1.03x faster                                                     |
| logging_format             | 6.40 us                                                | 6.25 us: 1.02x faster                                                     |
| thrift                     | 809 us                                                 | 791 us: 1.02x faster                                                      |
| logging_simple             | 5.72 us                                                | 5.61 us: 1.02x faster                                                     |
| logging_silent             | 102 ns                                                 | 100 ns: 1.01x faster                                                      |
| regex_compile              | 132 ms                                                 | 131 ms: 1.01x faster                                                      |
| meteor_contest             | 109 ms                                                 | 109 ms: 1.00x slower                                                      |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                      |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                      |
| pprint_safe_repr           | 728 ms                                                 | 736 ms: 1.01x slower                                                      |
| coverage                   | 84.0 ms                                                | 85.4 ms: 1.02x slower                                                     |
| python_startup_no_site     | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                     |
| sympy_sum                  | 150 ms                                                 | 153 ms: 1.02x slower                                                      |
| sympy_str                  | 275 ms                                                 | 280 ms: 1.02x slower                                                      |
| pprint_pformat             | 1.49 sec                                               | 1.52 sec: 1.02x slower                                                    |
| sqlglot_optimize           | 53.7 ms                                                | 55.1 ms: 1.02x slower                                                     |
| sqlglot_transpile          | 1.58 ms                                                | 1.62 ms: 1.03x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.31 ms: 1.03x slower                                                     |
| sympy_expand               | 463 ms                                                 | 477 ms: 1.03x slower                                                      |
| python_startup             | 12.5 ms                                                | 12.9 ms: 1.03x slower                                                     |
| coroutines                 | 22.7 ms                                                | 23.4 ms: 1.03x slower                                                     |
| sqlglot_normalize          | 108 ms                                                 | 111 ms: 1.03x slower                                                      |
| sympy_integrate            | 19.9 ms                                                | 20.7 ms: 1.04x slower                                                     |
| dulwich_log                | 64.3 ms                                                | 66.8 ms: 1.04x slower                                                     |
| pickle_pure_python         | 310 us                                                 | 323 us: 1.04x slower                                                      |
| float                      | 79.2 ms                                                | 82.3 ms: 1.04x slower                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 568 ms: 1.04x slower                                                      |
| chaos                      | 58.1 ms                                                | 60.4 ms: 1.04x slower                                                     |
| docutils                   | 2.59 sec                                               | 2.71 sec: 1.04x slower                                                    |
| sphinx                     | 1.03 sec                                               | 1.08 sec: 1.05x slower                                                    |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                      |
| raytrace                   | 267 ms                                                 | 280 ms: 1.05x slower                                                      |
| html5lib                   | 64.2 ms                                                | 67.4 ms: 1.05x slower                                                     |
| json_dumps                 | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                     |
| genshi_text                | 23.5 ms                                                | 24.9 ms: 1.06x slower                                                     |
| bench_thread_pool          | 822 us                                                 | 872 us: 1.06x slower                                                      |
| comprehensions             | 16.5 us                                                | 17.6 us: 1.07x slower                                                     |
| async_tree_io_tg           | 857 ms                                                 | 916 ms: 1.07x slower                                                      |
| async_tree_io              | 842 ms                                                 | 906 ms: 1.08x slower                                                      |
| gc_traversal               | 4.37 ms                                                | 4.73 ms: 1.08x slower                                                     |
| genshi_xml                 | 50.9 ms                                                | 56.2 ms: 1.10x slower                                                     |
| create_gc_cycles           | 2.41 ms                                                | 2.67 ms: 1.11x slower                                                     |
| hexiom                     | 6.16 ms                                                | 6.83 ms: 1.11x slower                                                     |
| nqueens                    | 78.4 ms                                                | 89.2 ms: 1.14x slower                                                     |
| generators                 | 29.0 ms                                                | 35.6 ms: 1.23x slower                                                     |
| k_core                     | 2.35 sec                                               | 2.92 sec: 1.24x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 79.2 ms: 3.30x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (9): spectral_norm, connected_components, async_tree_none_tg, scimark_lu, regex_dna, xml_etree_iterparse, shortest_path, typing_runtime_protocols, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241121-3.14.0a2+-41565b0-JIT/bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.016x faster
# HPT report

- Reliability score: 65.80% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x
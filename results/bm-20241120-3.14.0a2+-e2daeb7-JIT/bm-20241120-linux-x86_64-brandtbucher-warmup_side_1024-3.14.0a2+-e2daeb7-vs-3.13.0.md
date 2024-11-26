# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_side_1024
- machine: linux-x86_64
- commit hash: e2daeb7
- commit date: 2024-11-20
- overall geometric mean: 1.017x faster
- HPT reliability: 89.51%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 261 ms: 1.02x faster                                                     |
| docutils       | 2.59 sec                                               | 2.81 sec: 1.08x slower                                                   |
| html5lib       | 64.2 ms                                                | 67.2 ms: 1.05x slower                                                    |
| sphinx         | 1.03 sec                                               | 1.10 sec: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 397 ms: 1.17x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 410 ms: 1.08x faster                                                     |
| async_tree_none            | 351 ms                                                 | 328 ms: 1.07x faster                                                     |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 561 ms: 1.03x faster                                                     |
| coroutines                 | 22.7 ms                                                | 22.8 ms: 1.01x slower                                                    |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 562 ms: 1.03x slower                                                     |
| async_generators           | 436 ms                                                 | 451 ms: 1.04x slower                                                     |
| async_tree_io_tg           | 857 ms                                                 | 921 ms: 1.07x slower                                                     |
| async_tree_io              | 842 ms                                                 | 914 ms: 1.09x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 84.8 ms: 1.03x faster                                                    |
| float          | 79.2 ms                                                | 78.2 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.38 ms: 1.10x faster                                                    |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                     |
| regex_v8       | 26.2 ms                                                | 25.7 ms: 1.02x faster                                                    |
| regex_dna      | 218 ms                                                 | 220 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                 | 191 us: 1.13x faster                                                     |
| tomli_loads          | 2.14 sec                                               | 1.94 sec: 1.10x faster                                                   |
| xml_etree_generate   | 86.7 ms                                                | 79.5 ms: 1.09x faster                                                    |
| xml_etree_process    | 60.6 ms                                                | 56.2 ms: 1.08x faster                                                    |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                     |
| json_loads           | 27.2 us                                                | 26.4 us: 1.03x faster                                                    |
| pickle_pure_python   | 310 us                                                 | 323 us: 1.04x slower                                                     |
| json_dumps           | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.08 ms: 1.02x slower                                                    |
| python_startup         | 12.5 ms                                                | 12.9 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.2 ms: 1.08x faster                                                    |
| django_template | 35.2 ms                                                | 33.0 ms: 1.06x faster                                                    |
| genshi_text     | 23.5 ms                                                | 24.2 ms: 1.03x slower                                                    |
| genshi_xml      | 50.9 ms                                                | 55.5 ms: 1.09x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 268 us: 1.34x faster                                                     |
| deepcopy_memo              | 39.1 us                                                | 29.3 us: 1.34x faster                                                    |
| richards                   | 48.7 ms                                                | 40.6 ms: 1.20x faster                                                    |
| deepcopy_reduce            | 3.20 us                                                | 2.70 us: 1.19x faster                                                    |
| richards_super             | 54.9 ms                                                | 46.4 ms: 1.18x faster                                                    |
| async_tree_memoization_tg  | 464 ms                                                 | 397 ms: 1.17x faster                                                     |
| scimark_fft                | 364 ms                                                 | 315 ms: 1.16x faster                                                     |
| telco                      | 8.54 ms                                                | 7.46 ms: 1.15x faster                                                    |
| pylint                     | 313 ms                                                 | 274 ms: 1.14x faster                                                     |
| unpickle_pure_python       | 216 us                                                 | 191 us: 1.13x faster                                                     |
| go                         | 144 ms                                                 | 129 ms: 1.11x faster                                                     |
| crypto_pyaes               | 75.3 ms                                                | 67.7 ms: 1.11x faster                                                    |
| json                       | 5.36 ms                                                | 4.82 ms: 1.11x faster                                                    |
| tomli_loads                | 2.14 sec                                               | 1.94 sec: 1.10x faster                                                   |
| regex_effbot               | 3.73 ms                                                | 3.38 ms: 1.10x faster                                                    |
| xml_etree_generate         | 86.7 ms                                                | 79.5 ms: 1.09x faster                                                    |
| mako                       | 11.1 ms                                                | 10.2 ms: 1.08x faster                                                    |
| pathlib                    | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                    |
| xml_etree_process          | 60.6 ms                                                | 56.2 ms: 1.08x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 410 ms: 1.08x faster                                                     |
| async_tree_none            | 351 ms                                                 | 328 ms: 1.07x faster                                                     |
| django_template            | 35.2 ms                                                | 33.0 ms: 1.06x faster                                                    |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.74 ms: 1.06x faster                                                    |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                     |
| fannkuch                   | 404 ms                                                 | 384 ms: 1.05x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                                   |
| bpe_tokeniser              | 4.75 sec                                               | 4.51 sec: 1.05x faster                                                   |
| logging_format             | 6.40 us                                                | 6.10 us: 1.05x faster                                                    |
| logging_simple             | 5.72 us                                                | 5.49 us: 1.04x faster                                                    |
| thrift                     | 809 us                                                 | 779 us: 1.04x faster                                                     |
| pyflate                    | 471 ms                                                 | 455 ms: 1.04x faster                                                     |
| scimark_monte_carlo        | 67.4 ms                                                | 65.3 ms: 1.03x faster                                                    |
| json_loads                 | 27.2 us                                                | 26.4 us: 1.03x faster                                                    |
| scimark_sor                | 124 ms                                                 | 120 ms: 1.03x faster                                                     |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 561 ms: 1.03x faster                                                     |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                     |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.03x faster                                                     |
| nbody                      | 87.0 ms                                                | 84.8 ms: 1.03x faster                                                    |
| 2to3                       | 267 ms                                                 | 261 ms: 1.02x faster                                                     |
| regex_v8                   | 26.2 ms                                                | 25.7 ms: 1.02x faster                                                    |
| connected_components       | 444 ms                                                 | 438 ms: 1.01x faster                                                     |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.01x faster                                                     |
| float                      | 79.2 ms                                                | 78.2 ms: 1.01x faster                                                    |
| deltablue                  | 3.23 ms                                                | 3.20 ms: 1.01x faster                                                    |
| mdp                        | 2.72 sec                                               | 2.71 sec: 1.00x faster                                                   |
| coroutines                 | 22.7 ms                                                | 22.8 ms: 1.01x slower                                                    |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                     |
| chaos                      | 58.1 ms                                                | 58.6 ms: 1.01x slower                                                    |
| regex_dna                  | 218 ms                                                 | 220 ms: 1.01x slower                                                     |
| coverage                   | 84.0 ms                                                | 84.8 ms: 1.01x slower                                                    |
| typing_runtime_protocols   | 165 us                                                 | 167 us: 1.01x slower                                                     |
| logging_silent             | 102 ns                                                 | 103 ns: 1.01x slower                                                     |
| sqlglot_normalize          | 108 ms                                                 | 109 ms: 1.02x slower                                                     |
| python_startup_no_site     | 6.96 ms                                                | 7.08 ms: 1.02x slower                                                    |
| gc_traversal               | 4.37 ms                                                | 4.45 ms: 1.02x slower                                                    |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.4 ms: 1.02x slower                                                    |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                                     |
| sqlglot_transpile          | 1.58 ms                                                | 1.63 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 562 ms: 1.03x slower                                                     |
| genshi_text                | 23.5 ms                                                | 24.2 ms: 1.03x slower                                                    |
| sqlglot_optimize           | 53.7 ms                                                | 55.5 ms: 1.03x slower                                                    |
| sympy_expand               | 463 ms                                                 | 479 ms: 1.03x slower                                                     |
| python_startup             | 12.5 ms                                                | 12.9 ms: 1.03x slower                                                    |
| sympy_str                  | 275 ms                                                 | 284 ms: 1.03x slower                                                     |
| async_generators           | 436 ms                                                 | 451 ms: 1.04x slower                                                     |
| pickle_pure_python         | 310 us                                                 | 323 us: 1.04x slower                                                     |
| sympy_integrate            | 19.9 ms                                                | 20.8 ms: 1.04x slower                                                    |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.04x slower                                                    |
| dulwich_log                | 64.3 ms                                                | 67.2 ms: 1.04x slower                                                    |
| html5lib                   | 64.2 ms                                                | 67.2 ms: 1.05x slower                                                    |
| sympy_sum                  | 150 ms                                                 | 158 ms: 1.05x slower                                                     |
| json_dumps                 | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                    |
| comprehensions             | 16.5 us                                                | 17.3 us: 1.05x slower                                                    |
| sphinx                     | 1.03 sec                                               | 1.10 sec: 1.06x slower                                                   |
| bench_thread_pool          | 822 us                                                 | 872 us: 1.06x slower                                                     |
| async_tree_io_tg           | 857 ms                                                 | 921 ms: 1.07x slower                                                     |
| raytrace                   | 267 ms                                                 | 287 ms: 1.08x slower                                                     |
| docutils                   | 2.59 sec                                               | 2.81 sec: 1.08x slower                                                   |
| async_tree_io              | 842 ms                                                 | 914 ms: 1.09x slower                                                     |
| genshi_xml                 | 50.9 ms                                                | 55.5 ms: 1.09x slower                                                    |
| create_gc_cycles           | 2.41 ms                                                | 2.66 ms: 1.11x slower                                                    |
| nqueens                    | 78.4 ms                                                | 89.5 ms: 1.14x slower                                                    |
| hexiom                     | 6.16 ms                                                | 7.13 ms: 1.16x slower                                                    |
| k_core                     | 2.35 sec                                               | 2.89 sec: 1.23x slower                                                   |
| generators                 | 29.0 ms                                                | 35.6 ms: 1.23x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 79.4 ms: 3.31x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (6): async_tree_none_tg, pprint_safe_repr, shortest_path, xml_etree_iterparse, pidigits, pprint_pformat
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241120-3.14.0a2+-e2daeb7-JIT/bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.017x faster
# HPT report

- Reliability score: 89.51% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x
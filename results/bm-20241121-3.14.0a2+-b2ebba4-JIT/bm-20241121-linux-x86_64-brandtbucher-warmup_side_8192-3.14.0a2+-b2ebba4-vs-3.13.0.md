# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_side_8192
- machine: linux-x86_64
- commit hash: b2ebba4
- commit date: 2024-11-21
- overall geometric mean: 1.018x faster
- HPT reliability: 89.58%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 260 ms: 1.03x faster                                                     |
| docutils       | 2.59 sec                                               | 2.75 sec: 1.06x slower                                                   |
| html5lib       | 64.2 ms                                                | 66.1 ms: 1.03x slower                                                    |
| sphinx         | 1.03 sec                                               | 1.08 sec: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 399 ms: 1.16x faster                                                     |
| async_tree_none            | 351 ms                                                 | 324 ms: 1.08x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 410 ms: 1.08x faster                                                     |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 560 ms: 1.03x faster                                                     |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                     |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 565 ms: 1.04x slower                                                     |
| async_generators           | 436 ms                                                 | 456 ms: 1.05x slower                                                     |
| async_tree_io_tg           | 857 ms                                                 | 911 ms: 1.06x slower                                                     |
| async_tree_io              | 842 ms                                                 | 909 ms: 1.08x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 81.4 ms: 1.07x faster                                                    |
| float          | 79.2 ms                                                | 78.4 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.43 ms: 1.09x faster                                                    |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                     |
| regex_v8       | 26.2 ms                                                | 26.0 ms: 1.01x faster                                                    |
| regex_dna      | 218 ms                                                 | 224 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                 | 192 us: 1.12x faster                                                     |
| xml_etree_generate   | 86.7 ms                                                | 79.1 ms: 1.10x faster                                                    |
| xml_etree_process    | 60.6 ms                                                | 55.8 ms: 1.09x faster                                                    |
| tomli_loads          | 2.14 sec                                               | 2.00 sec: 1.07x faster                                                   |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                     |
| json_loads           | 27.2 us                                                | 26.2 us: 1.04x faster                                                    |
| pickle_pure_python   | 310 us                                                 | 328 us: 1.06x slower                                                     |
| json_dumps           | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.06 ms: 1.01x slower                                                    |
| python_startup         | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.3 ms: 1.08x faster                                                    |
| django_template | 35.2 ms                                                | 33.6 ms: 1.04x faster                                                    |
| genshi_text     | 23.5 ms                                                | 24.3 ms: 1.03x slower                                                    |
| genshi_xml      | 50.9 ms                                                | 60.4 ms: 1.19x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 29.3 us: 1.33x faster                                                    |
| deepcopy                   | 358 us                                                 | 273 us: 1.31x faster                                                     |
| richards                   | 48.7 ms                                                | 38.6 ms: 1.26x faster                                                    |
| richards_super             | 54.9 ms                                                | 44.5 ms: 1.23x faster                                                    |
| deepcopy_reduce            | 3.20 us                                                | 2.75 us: 1.16x faster                                                    |
| async_tree_memoization_tg  | 464 ms                                                 | 399 ms: 1.16x faster                                                     |
| scimark_fft                | 364 ms                                                 | 316 ms: 1.15x faster                                                     |
| pylint                     | 313 ms                                                 | 273 ms: 1.14x faster                                                     |
| go                         | 144 ms                                                 | 128 ms: 1.12x faster                                                     |
| unpickle_pure_python       | 216 us                                                 | 192 us: 1.12x faster                                                     |
| telco                      | 8.54 ms                                                | 7.67 ms: 1.11x faster                                                    |
| crypto_pyaes               | 75.3 ms                                                | 68.2 ms: 1.10x faster                                                    |
| xml_etree_generate         | 86.7 ms                                                | 79.1 ms: 1.10x faster                                                    |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.62 ms: 1.09x faster                                                    |
| json                       | 5.36 ms                                                | 4.93 ms: 1.09x faster                                                    |
| regex_effbot               | 3.73 ms                                                | 3.43 ms: 1.09x faster                                                    |
| xml_etree_process          | 60.6 ms                                                | 55.8 ms: 1.09x faster                                                    |
| async_tree_none            | 351 ms                                                 | 324 ms: 1.08x faster                                                     |
| mako                       | 11.1 ms                                                | 10.3 ms: 1.08x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 410 ms: 1.08x faster                                                     |
| pathlib                    | 17.5 ms                                                | 16.3 ms: 1.08x faster                                                    |
| tomli_loads                | 2.14 sec                                               | 2.00 sec: 1.07x faster                                                   |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                     |
| nbody                      | 87.0 ms                                                | 81.4 ms: 1.07x faster                                                    |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.07x faster                                                   |
| bpe_tokeniser              | 4.75 sec                                               | 4.51 sec: 1.05x faster                                                   |
| logging_format             | 6.40 us                                                | 6.08 us: 1.05x faster                                                    |
| scimark_sor                | 124 ms                                                 | 118 ms: 1.05x faster                                                     |
| scimark_monte_carlo        | 67.4 ms                                                | 64.6 ms: 1.04x faster                                                    |
| django_template            | 35.2 ms                                                | 33.6 ms: 1.04x faster                                                    |
| thrift                     | 809 us                                                 | 776 us: 1.04x faster                                                     |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                                     |
| json_loads                 | 27.2 us                                                | 26.2 us: 1.04x faster                                                    |
| pyflate                    | 471 ms                                                 | 455 ms: 1.04x faster                                                     |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 560 ms: 1.03x faster                                                     |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                     |
| 2to3                       | 267 ms                                                 | 260 ms: 1.03x faster                                                     |
| fannkuch                   | 404 ms                                                 | 394 ms: 1.03x faster                                                     |
| logging_simple             | 5.72 us                                                | 5.59 us: 1.02x faster                                                    |
| scimark_lu                 | 113 ms                                                 | 111 ms: 1.02x faster                                                     |
| connected_components       | 444 ms                                                 | 437 ms: 1.02x faster                                                     |
| deltablue                  | 3.23 ms                                                | 3.18 ms: 1.01x faster                                                    |
| float                      | 79.2 ms                                                | 78.4 ms: 1.01x faster                                                    |
| regex_v8                   | 26.2 ms                                                | 26.0 ms: 1.01x faster                                                    |
| gc_traversal               | 4.37 ms                                                | 4.35 ms: 1.00x faster                                                    |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                     |
| logging_silent             | 102 ns                                                 | 103 ns: 1.01x slower                                                     |
| typing_runtime_protocols   | 165 us                                                 | 167 us: 1.01x slower                                                     |
| python_startup_no_site     | 6.96 ms                                                | 7.06 ms: 1.01x slower                                                    |
| chaos                      | 58.1 ms                                                | 59.0 ms: 1.02x slower                                                    |
| sqlglot_transpile          | 1.58 ms                                                | 1.62 ms: 1.02x slower                                                    |
| sympy_str                  | 275 ms                                                 | 281 ms: 1.02x slower                                                     |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                    |
| mdp                        | 2.72 sec                                               | 2.78 sec: 1.02x slower                                                   |
| regex_dna                  | 218 ms                                                 | 224 ms: 1.02x slower                                                     |
| python_startup             | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                    |
| html5lib                   | 64.2 ms                                                | 66.1 ms: 1.03x slower                                                    |
| genshi_text                | 23.5 ms                                                | 24.3 ms: 1.03x slower                                                    |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                     |
| sympy_expand               | 463 ms                                                 | 479 ms: 1.03x slower                                                     |
| sqlglot_optimize           | 53.7 ms                                                | 55.5 ms: 1.03x slower                                                    |
| sqlglot_normalize          | 108 ms                                                 | 111 ms: 1.03x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 565 ms: 1.04x slower                                                     |
| sympy_integrate            | 19.9 ms                                                | 20.7 ms: 1.04x slower                                                    |
| dulwich_log                | 64.3 ms                                                | 67.1 ms: 1.04x slower                                                    |
| async_generators           | 436 ms                                                 | 456 ms: 1.05x slower                                                     |
| sphinx                     | 1.03 sec                                               | 1.08 sec: 1.05x slower                                                   |
| pickle_pure_python         | 310 us                                                 | 328 us: 1.06x slower                                                     |
| docutils                   | 2.59 sec                                               | 2.75 sec: 1.06x slower                                                   |
| bench_thread_pool          | 822 us                                                 | 871 us: 1.06x slower                                                     |
| comprehensions             | 16.5 us                                                | 17.5 us: 1.06x slower                                                    |
| json_dumps                 | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                    |
| async_tree_io_tg           | 857 ms                                                 | 911 ms: 1.06x slower                                                     |
| raytrace                   | 267 ms                                                 | 286 ms: 1.07x slower                                                     |
| async_tree_io              | 842 ms                                                 | 909 ms: 1.08x slower                                                     |
| create_gc_cycles           | 2.41 ms                                                | 2.64 ms: 1.10x slower                                                    |
| hexiom                     | 6.16 ms                                                | 6.96 ms: 1.13x slower                                                    |
| nqueens                    | 78.4 ms                                                | 89.4 ms: 1.14x slower                                                    |
| genshi_xml                 | 50.9 ms                                                | 60.4 ms: 1.19x slower                                                    |
| generators                 | 29.0 ms                                                | 35.6 ms: 1.23x slower                                                    |
| k_core                     | 2.35 sec                                               | 2.94 sec: 1.25x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 79.3 ms: 3.31x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (9): async_tree_none_tg, sqlalchemy_imperative, meteor_contest, xml_etree_iterparse, pidigits, shortest_path, pprint_pformat, pprint_safe_repr, coverage
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241121-3.14.0a2+-b2ebba4-JIT/bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.018x faster
# HPT report

- Reliability score: 89.58% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x
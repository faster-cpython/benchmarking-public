# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_side_4096
- machine: linux-x86_64
- commit hash: bba66e4
- commit date: 2024-11-20
- overall geometric mean: 1.020x faster
- HPT reliability: 95.62%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 259 ms: 1.03x faster                                                     |
| docutils       | 2.59 sec                                               | 2.77 sec: 1.07x slower                                                   |
| html5lib       | 64.2 ms                                                | 66.3 ms: 1.03x slower                                                    |
| sphinx         | 1.03 sec                                               | 1.09 sec: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 396 ms: 1.17x faster                                                     |
| async_tree_none            | 351 ms                                                 | 325 ms: 1.08x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 411 ms: 1.08x faster                                                     |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 562 ms: 1.03x faster                                                     |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 562 ms: 1.03x slower                                                     |
| async_generators           | 436 ms                                                 | 450 ms: 1.03x slower                                                     |
| async_tree_io_tg           | 857 ms                                                 | 910 ms: 1.06x slower                                                     |
| async_tree_io              | 842 ms                                                 | 903 ms: 1.07x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (2): async_tree_none_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 83.2 ms: 1.05x faster                                                    |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.42 ms: 1.09x faster                                                    |
| regex_v8       | 26.2 ms                                                | 25.5 ms: 1.03x faster                                                    |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                 | 195 us: 1.11x faster                                                     |
| xml_etree_generate   | 86.7 ms                                                | 79.0 ms: 1.10x faster                                                    |
| tomli_loads          | 2.14 sec                                               | 1.96 sec: 1.09x faster                                                   |
| xml_etree_process    | 60.6 ms                                                | 55.7 ms: 1.09x faster                                                    |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                     |
| json_loads           | 27.2 us                                                | 26.1 us: 1.04x faster                                                    |
| pickle_pure_python   | 310 us                                                 | 317 us: 1.02x slower                                                     |
| json_dumps           | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                    |
| python_startup         | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.0 ms: 1.10x faster                                                    |
| django_template | 35.2 ms                                                | 33.3 ms: 1.06x faster                                                    |
| genshi_text     | 23.5 ms                                                | 25.1 ms: 1.07x slower                                                    |
| genshi_xml      | 50.9 ms                                                | 58.5 ms: 1.15x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 266 us: 1.35x faster                                                     |
| deepcopy_memo              | 39.1 us                                                | 29.2 us: 1.34x faster                                                    |
| richards                   | 48.7 ms                                                | 38.7 ms: 1.26x faster                                                    |
| richards_super             | 54.9 ms                                                | 44.7 ms: 1.23x faster                                                    |
| deepcopy_reduce            | 3.20 us                                                | 2.67 us: 1.20x faster                                                    |
| async_tree_memoization_tg  | 464 ms                                                 | 396 ms: 1.17x faster                                                     |
| scimark_fft                | 364 ms                                                 | 313 ms: 1.16x faster                                                     |
| pylint                     | 313 ms                                                 | 271 ms: 1.15x faster                                                     |
| telco                      | 8.54 ms                                                | 7.50 ms: 1.14x faster                                                    |
| json                       | 5.36 ms                                                | 4.77 ms: 1.12x faster                                                    |
| crypto_pyaes               | 75.3 ms                                                | 67.2 ms: 1.12x faster                                                    |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.52 ms: 1.12x faster                                                    |
| unpickle_pure_python       | 216 us                                                 | 195 us: 1.11x faster                                                     |
| mako                       | 11.1 ms                                                | 10.0 ms: 1.10x faster                                                    |
| xml_etree_generate         | 86.7 ms                                                | 79.0 ms: 1.10x faster                                                    |
| tomli_loads                | 2.14 sec                                               | 1.96 sec: 1.09x faster                                                   |
| regex_effbot               | 3.73 ms                                                | 3.42 ms: 1.09x faster                                                    |
| xml_etree_process          | 60.6 ms                                                | 55.7 ms: 1.09x faster                                                    |
| async_tree_none            | 351 ms                                                 | 325 ms: 1.08x faster                                                     |
| go                         | 144 ms                                                 | 133 ms: 1.08x faster                                                     |
| pyflate                    | 471 ms                                                 | 438 ms: 1.08x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 411 ms: 1.08x faster                                                     |
| pathlib                    | 17.5 ms                                                | 16.3 ms: 1.07x faster                                                    |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                                     |
| django_template            | 35.2 ms                                                | 33.3 ms: 1.06x faster                                                    |
| bpe_tokeniser              | 4.75 sec                                               | 4.50 sec: 1.06x faster                                                   |
| mdp                        | 2.72 sec                                               | 2.59 sec: 1.05x faster                                                   |
| thrift                     | 809 us                                                 | 773 us: 1.05x faster                                                     |
| nbody                      | 87.0 ms                                                | 83.2 ms: 1.05x faster                                                    |
| json_loads                 | 27.2 us                                                | 26.1 us: 1.04x faster                                                    |
| fannkuch                   | 404 ms                                                 | 390 ms: 1.04x faster                                                     |
| logging_format             | 6.40 us                                                | 6.20 us: 1.03x faster                                                    |
| logging_silent             | 102 ns                                                 | 98.5 ns: 1.03x faster                                                    |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                     |
| 2to3                       | 267 ms                                                 | 259 ms: 1.03x faster                                                     |
| regex_v8                   | 26.2 ms                                                | 25.5 ms: 1.03x faster                                                    |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                     |
| scimark_sor                | 124 ms                                                 | 120 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 562 ms: 1.03x faster                                                     |
| scimark_monte_carlo        | 67.4 ms                                                | 65.7 ms: 1.03x faster                                                    |
| logging_simple             | 5.72 us                                                | 5.59 us: 1.02x faster                                                    |
| connected_components       | 444 ms                                                 | 435 ms: 1.02x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                   |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                     |
| pprint_safe_repr           | 728 ms                                                 | 716 ms: 1.02x faster                                                     |
| pprint_pformat             | 1.49 sec                                               | 1.47 sec: 1.02x faster                                                   |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                     |
| deltablue                  | 3.23 ms                                                | 3.18 ms: 1.01x faster                                                    |
| coverage                   | 84.0 ms                                                | 83.1 ms: 1.01x faster                                                    |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                     |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                     |
| scimark_lu                 | 113 ms                                                 | 114 ms: 1.01x slower                                                     |
| python_startup_no_site     | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                    |
| sympy_str                  | 275 ms                                                 | 280 ms: 1.02x slower                                                     |
| pickle_pure_python         | 310 us                                                 | 317 us: 1.02x slower                                                     |
| typing_runtime_protocols   | 165 us                                                 | 168 us: 1.02x slower                                                     |
| chaos                      | 58.1 ms                                                | 59.3 ms: 1.02x slower                                                    |
| sympy_expand               | 463 ms                                                 | 475 ms: 1.02x slower                                                     |
| sqlglot_normalize          | 108 ms                                                 | 110 ms: 1.02x slower                                                     |
| python_startup             | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                    |
| sqlglot_transpile          | 1.58 ms                                                | 1.63 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 562 ms: 1.03x slower                                                     |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                     |
| html5lib                   | 64.2 ms                                                | 66.3 ms: 1.03x slower                                                    |
| async_generators           | 436 ms                                                 | 450 ms: 1.03x slower                                                     |
| sqlglot_optimize           | 53.7 ms                                                | 55.6 ms: 1.03x slower                                                    |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                                    |
| gc_traversal               | 4.37 ms                                                | 4.54 ms: 1.04x slower                                                    |
| sympy_integrate            | 19.9 ms                                                | 20.7 ms: 1.04x slower                                                    |
| dulwich_log                | 64.3 ms                                                | 67.1 ms: 1.04x slower                                                    |
| json_dumps                 | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                    |
| sphinx                     | 1.03 sec                                               | 1.09 sec: 1.06x slower                                                   |
| comprehensions             | 16.5 us                                                | 17.5 us: 1.06x slower                                                    |
| bench_thread_pool          | 822 us                                                 | 872 us: 1.06x slower                                                     |
| async_tree_io_tg           | 857 ms                                                 | 910 ms: 1.06x slower                                                     |
| raytrace                   | 267 ms                                                 | 285 ms: 1.07x slower                                                     |
| genshi_text                | 23.5 ms                                                | 25.1 ms: 1.07x slower                                                    |
| docutils                   | 2.59 sec                                               | 2.77 sec: 1.07x slower                                                   |
| async_tree_io              | 842 ms                                                 | 903 ms: 1.07x slower                                                     |
| create_gc_cycles           | 2.41 ms                                                | 2.65 ms: 1.10x slower                                                    |
| nqueens                    | 78.4 ms                                                | 88.5 ms: 1.13x slower                                                    |
| hexiom                     | 6.16 ms                                                | 7.02 ms: 1.14x slower                                                    |
| genshi_xml                 | 50.9 ms                                                | 58.5 ms: 1.15x slower                                                    |
| k_core                     | 2.35 sec                                               | 2.92 sec: 1.24x slower                                                   |
| generators                 | 29.0 ms                                                | 36.5 ms: 1.26x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 78.8 ms: 3.28x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (7): async_tree_none_tg, sqlalchemy_imperative, float, xml_etree_iterparse, coroutines, shortest_path, regex_dna
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241120-3.14.0a2+-bba66e4-JIT/bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.020x faster
# HPT report

- Reliability score: 95.62% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x
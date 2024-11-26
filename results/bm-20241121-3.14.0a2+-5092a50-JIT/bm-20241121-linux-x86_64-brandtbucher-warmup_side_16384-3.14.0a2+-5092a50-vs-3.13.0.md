# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_side_16384
- machine: linux-x86_64
- commit hash: 5092a50
- commit date: 2024-11-21
- overall geometric mean: 1.017x faster
- HPT reliability: 83.34%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 260 ms: 1.03x faster                                                      |
| docutils       | 2.59 sec                                               | 2.75 sec: 1.06x slower                                                    |
| html5lib       | 64.2 ms                                                | 65.8 ms: 1.03x slower                                                     |
| sphinx         | 1.03 sec                                               | 1.08 sec: 1.05x slower                                                    |
| Geometric mean | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 398 ms: 1.16x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 410 ms: 1.08x faster                                                      |
| async_tree_none            | 351 ms                                                 | 326 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 566 ms: 1.02x faster                                                      |
| coroutines                 | 22.7 ms                                                | 22.5 ms: 1.01x faster                                                     |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                      |
| async_generators           | 436 ms                                                 | 453 ms: 1.04x slower                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 568 ms: 1.04x slower                                                      |
| async_tree_io_tg           | 857 ms                                                 | 911 ms: 1.06x slower                                                      |
| async_tree_io              | 842 ms                                                 | 909 ms: 1.08x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 83.4 ms: 1.04x faster                                                     |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.42 ms: 1.09x faster                                                     |
| regex_v8       | 26.2 ms                                                | 24.9 ms: 1.05x faster                                                     |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                      |
| regex_dna      | 218 ms                                                 | 223 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                 | 194 us: 1.11x faster                                                      |
| xml_etree_generate   | 86.7 ms                                                | 78.7 ms: 1.10x faster                                                     |
| tomli_loads          | 2.14 sec                                               | 1.96 sec: 1.09x faster                                                    |
| xml_etree_process    | 60.6 ms                                                | 55.7 ms: 1.09x faster                                                     |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                      |
| json_loads           | 27.2 us                                                | 26.3 us: 1.04x faster                                                     |
| pickle_pure_python   | 310 us                                                 | 324 us: 1.05x slower                                                      |
| json_dumps           | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.11 ms: 1.02x slower                                                     |
| python_startup         | 12.5 ms                                                | 12.9 ms: 1.04x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.1 ms: 1.10x faster                                                     |
| django_template | 35.2 ms                                                | 33.4 ms: 1.05x faster                                                     |
| genshi_text     | 23.5 ms                                                | 25.1 ms: 1.07x slower                                                     |
| genshi_xml      | 50.9 ms                                                | 60.5 ms: 1.19x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 29.3 us: 1.34x faster                                                     |
| deepcopy                   | 358 us                                                 | 269 us: 1.33x faster                                                      |
| richards                   | 48.7 ms                                                | 40.2 ms: 1.21x faster                                                     |
| richards_super             | 54.9 ms                                                | 46.2 ms: 1.19x faster                                                     |
| pylint                     | 313 ms                                                 | 268 ms: 1.17x faster                                                      |
| async_tree_memoization_tg  | 464 ms                                                 | 398 ms: 1.16x faster                                                      |
| deepcopy_reduce            | 3.20 us                                                | 2.78 us: 1.15x faster                                                     |
| telco                      | 8.54 ms                                                | 7.49 ms: 1.14x faster                                                     |
| go                         | 144 ms                                                 | 126 ms: 1.14x faster                                                      |
| scimark_fft                | 364 ms                                                 | 320 ms: 1.14x faster                                                      |
| json                       | 5.36 ms                                                | 4.81 ms: 1.11x faster                                                     |
| unpickle_pure_python       | 216 us                                                 | 194 us: 1.11x faster                                                      |
| xml_etree_generate         | 86.7 ms                                                | 78.7 ms: 1.10x faster                                                     |
| crypto_pyaes               | 75.3 ms                                                | 68.4 ms: 1.10x faster                                                     |
| mako                       | 11.1 ms                                                | 10.1 ms: 1.10x faster                                                     |
| regex_effbot               | 3.73 ms                                                | 3.42 ms: 1.09x faster                                                     |
| tomli_loads                | 2.14 sec                                               | 1.96 sec: 1.09x faster                                                    |
| xml_etree_process          | 60.6 ms                                                | 55.7 ms: 1.09x faster                                                     |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.64 ms: 1.09x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 410 ms: 1.08x faster                                                      |
| async_tree_none            | 351 ms                                                 | 326 ms: 1.08x faster                                                      |
| pathlib                    | 17.5 ms                                                | 16.5 ms: 1.06x faster                                                     |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                                      |
| regex_v8                   | 26.2 ms                                                | 24.9 ms: 1.05x faster                                                     |
| bpe_tokeniser              | 4.75 sec                                               | 4.51 sec: 1.05x faster                                                    |
| django_template            | 35.2 ms                                                | 33.4 ms: 1.05x faster                                                     |
| logging_format             | 6.40 us                                                | 6.09 us: 1.05x faster                                                     |
| fannkuch                   | 404 ms                                                 | 386 ms: 1.05x faster                                                      |
| nbody                      | 87.0 ms                                                | 83.4 ms: 1.04x faster                                                     |
| logging_simple             | 5.72 us                                                | 5.49 us: 1.04x faster                                                     |
| pyflate                    | 471 ms                                                 | 452 ms: 1.04x faster                                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 64.8 ms: 1.04x faster                                                     |
| scimark_sor                | 124 ms                                                 | 119 ms: 1.04x faster                                                      |
| json_loads                 | 27.2 us                                                | 26.3 us: 1.04x faster                                                     |
| thrift                     | 809 us                                                 | 781 us: 1.04x faster                                                      |
| logging_silent             | 102 ns                                                 | 98.9 ns: 1.03x faster                                                     |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.03x faster                                                      |
| 2to3                       | 267 ms                                                 | 260 ms: 1.03x faster                                                      |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                    |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 566 ms: 1.02x faster                                                      |
| deltablue                  | 3.23 ms                                                | 3.16 ms: 1.02x faster                                                     |
| scimark_lu                 | 113 ms                                                 | 111 ms: 1.02x faster                                                      |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                      |
| connected_components       | 444 ms                                                 | 438 ms: 1.01x faster                                                      |
| coroutines                 | 22.7 ms                                                | 22.5 ms: 1.01x faster                                                     |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                                      |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                      |
| mdp                        | 2.72 sec                                               | 2.75 sec: 1.01x slower                                                    |
| typing_runtime_protocols   | 165 us                                                 | 167 us: 1.01x slower                                                      |
| sympy_str                  | 275 ms                                                 | 279 ms: 1.01x slower                                                      |
| regex_dna                  | 218 ms                                                 | 223 ms: 1.02x slower                                                      |
| sqlglot_transpile          | 1.58 ms                                                | 1.61 ms: 1.02x slower                                                     |
| sympy_sum                  | 150 ms                                                 | 153 ms: 1.02x slower                                                      |
| python_startup_no_site     | 6.96 ms                                                | 7.11 ms: 1.02x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.02x slower                                                     |
| html5lib                   | 64.2 ms                                                | 65.8 ms: 1.03x slower                                                     |
| spectral_norm              | 115 ms                                                 | 119 ms: 1.03x slower                                                      |
| chaos                      | 58.1 ms                                                | 59.7 ms: 1.03x slower                                                     |
| sympy_expand               | 463 ms                                                 | 477 ms: 1.03x slower                                                      |
| sqlglot_optimize           | 53.7 ms                                                | 55.3 ms: 1.03x slower                                                     |
| sqlglot_normalize          | 108 ms                                                 | 111 ms: 1.03x slower                                                      |
| python_startup             | 12.5 ms                                                | 12.9 ms: 1.04x slower                                                     |
| sympy_integrate            | 19.9 ms                                                | 20.6 ms: 1.04x slower                                                     |
| async_generators           | 436 ms                                                 | 453 ms: 1.04x slower                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 568 ms: 1.04x slower                                                      |
| pickle_pure_python         | 310 us                                                 | 324 us: 1.05x slower                                                      |
| sphinx                     | 1.03 sec                                               | 1.08 sec: 1.05x slower                                                    |
| dulwich_log                | 64.3 ms                                                | 67.5 ms: 1.05x slower                                                     |
| raytrace                   | 267 ms                                                 | 283 ms: 1.06x slower                                                      |
| docutils                   | 2.59 sec                                               | 2.75 sec: 1.06x slower                                                    |
| json_dumps                 | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                     |
| async_tree_io_tg           | 857 ms                                                 | 911 ms: 1.06x slower                                                      |
| bench_thread_pool          | 822 us                                                 | 875 us: 1.07x slower                                                      |
| genshi_text                | 23.5 ms                                                | 25.1 ms: 1.07x slower                                                     |
| gc_traversal               | 4.37 ms                                                | 4.68 ms: 1.07x slower                                                     |
| async_tree_io              | 842 ms                                                 | 909 ms: 1.08x slower                                                      |
| hexiom                     | 6.16 ms                                                | 6.73 ms: 1.09x slower                                                     |
| comprehensions             | 16.5 us                                                | 18.2 us: 1.10x slower                                                     |
| create_gc_cycles           | 2.41 ms                                                | 2.67 ms: 1.11x slower                                                     |
| nqueens                    | 78.4 ms                                                | 87.8 ms: 1.12x slower                                                     |
| genshi_xml                 | 50.9 ms                                                | 60.5 ms: 1.19x slower                                                     |
| generators                 | 29.0 ms                                                | 35.2 ms: 1.22x slower                                                     |
| k_core                     | 2.35 sec                                               | 2.92 sec: 1.24x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 79.2 ms: 3.30x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (9): async_tree_none_tg, float, xml_etree_iterparse, pprint_safe_repr, meteor_contest, shortest_path, coverage, sqlalchemy_imperative, pprint_pformat
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241121-3.14.0a2+-5092a50-JIT/bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.017x faster
# HPT report

- Reliability score: 83.34% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x